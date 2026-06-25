from django.db import models

class StudentRegistration(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    course = models.CharField(max_length=50)

    def __str__(self):
        return self.name