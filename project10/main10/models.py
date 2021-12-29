from django.db import models

# Create your models here.

class Picnic(models.Model):

    student_name = models.CharField(max_length=30)
    student_class = models.CharField(max_length=4)
    student_fee = models.IntegerField()

    def __str__(self):
        return str(self.student_name)

