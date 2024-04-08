from django.db import models

class Record(models.Model):
    
    creation_date = models.DateTimeField(auto_now_add=True)

    first_name = models.CharField(max_length=200)

    last_name = models.CharField(max_length=255)

    email = models.CharField(max_length=255)
    
    phone = models.CharField(max_length=20)

    address = models.CharField(max_length=300)
    
    city = models.CharField(max_length=255)
    
    cgpa = models.IntegerField
    
    Achievements = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + "   " + self.last_name



    
    


