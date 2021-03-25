from django.db import models

# Create your models here.
class PersonalInfor(models.Model):
    STUDENT = 'ST'
    FRESHER = 'FR'
    SENIOR = 'SE'
    JUNIOR = 'JU'
    PROFESSOR = 'PR'
    name = models.CharField(max_length=200)
    LEVEL_CHOICES = [
        (STUDENT, 'Student'),
        (FRESHER, 'Fresher'),
        (JUNIOR, 'Junior'),
        (PROFESSOR, 'Professor')
    ]
    age = models.IntegerField(default=1)    
    level = models.CharField(max_length=2,choices=LEVEL_CHOICES,default=STUDENT)
    email = models.CharField(max_length=200)
