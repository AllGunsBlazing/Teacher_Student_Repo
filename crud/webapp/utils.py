import os
import tempfile
from google.oauth2 import service_account
from googleapiclient.discovery import build, MediaFileUpload
from webapp.models import Record

def upload_file_to_drive(uploaded_file):
    SCOPES = ['https://www.googleapis.com/auth/drive.file']
    SERVICE_ACCOUNT_FILE = 'credentials_GOOGLE_API.json'

    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    
    service = build('drive', 'v3', credentials=creds)
    
    # Save the uploaded file to a temporary location
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    for chunk in uploaded_file.chunks():
        temp_file.write(chunk)
    temp_file.close()
    
    file_metadata = {'name': uploaded_file.name}
    media = MediaFileUpload(temp_file.name, resumable=True)
    
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    
    file_id = file.get('id')
    
    # Delete the temporary file
    os.remove(temp_file.name)
    
    if file_id:
        # Make the file publicly accessible
        permission = {
            'type': 'anyone',
            'role': 'reader',
        }
        service.permissions().create(fileId=file_id, body=permission).execute()
    
    if file_id:
        return f"https://drive.google.com/file/d/{file_id}/view?usp=sharing"
    return None

def fetch_google_sheets_data():
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    SERVICE_ACCOUNT_FILE = 'credentials_GOOGLE_API.json'

    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    SHEET_ID = '1zPnkTeFZhU5Yep-im2048jOFqP3b4ip5RkYYS4zKX9s'
    SHEET_RANGE = 'Form responses 1!B2:Q'

    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    result = sheet.values().get(spreadsheetId=SHEET_ID, range=SHEET_RANGE).execute()
    values = result.get('values', [])

    if not values:
        return "No data found."
    else:
        messages = []
        for row in values:
            row_length = len(row)
            record, created = Record.objects.update_or_create(
                email=row[2] if row_length > 2 else None,
                defaults={
                    'first_name': row[0] if row_length > 0 else None,
                    'last_name': row[1] if row_length > 1 else None,
                    'phone': row[3] if row_length > 3 else None,
                    'address': row[4] if row_length > 4 else None,
                    'city': row[5] if row_length > 5 else None,
                    'cgpa': row[6] if row_length > 6 else None,
                    'achievement': row[7] if row_length > 7 else None,
                    'Internship': row[8] if row_length > 8 else None,
                    'Placement': row[9] if row_length > 9 else None,
                    'HigherStudies': row[10] if row_length > 10 else None,
                    'Entreprenuership': row[11] if row_length > 11 else None,
                    'ExtraCurricular': row[12] if row_length > 12 else None,
                    'Publications': row[13] if row_length > 13 else None,
                    'PractiseSchool': row[14] if row_length > 14 else None,
                    'Conference': row[15] if row_length > 15 else None,
                }
            )
            if created:
                messages.append(f'Created record for {row[2]}')
            else:
                messages.append(f'Updated record for {row[2]}')
        return messages