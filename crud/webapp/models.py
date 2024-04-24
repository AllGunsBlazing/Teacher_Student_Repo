from django.db import models

class Record(models.Model):
    
    creation_date = models.DateTimeField(auto_now_add=True)

    first_name = models.CharField(max_length=200)

    last_name = models.CharField(max_length=255)

    email = models.CharField(max_length=255)
    
    phone = models.CharField(max_length=20)

    address = models.CharField(max_length=300)
    
    city = models.CharField(max_length=255)
    
    cgpa = models.IntegerField()     

    achievement = models.CharField(max_length=200, default='none')

    Internship = models.CharField(max_length=100, default='none')
    
    Placement = models.CharField(max_length=200, default='none')

    HigherStudies  = models.CharField(max_length=200, default='none')
    
    Entreprenuership = models.CharField(max_length=200, default='none')

    ExtraCurricular = models.CharField(max_length=200, default='none')

    Publications = models.CharField(max_length=200, default='none')

    PractiseSchool = models.CharField(max_length=200, default='none')

    Conference = models.CharField(max_length=200, default='none')
    def __str__(self):
        return self.first_name + "   " + self.last_name



    
    


