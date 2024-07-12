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

    achievement = models.FileField(blank=True,null=True)

    Internship = models.FileField(blank=True,null=True)
    
    Placement = models.FileField(blank=True,null=True)

    HigherStudies  = models.FileField(blank=True,null=True)
    
    Entreprenuership = models.FileField(blank=True,null=True)

    ExtraCurricular = models.FileField(blank=True,null=True)

    Publications = models.FileField(blank=True,null=True)

    PractiseSchool = models.FileField(blank=True,null=True)

    Conference = models.FileField(blank=True,null=True)
    def __str__(self):
        return self.first_name + "   " + self.last_name



    
    


