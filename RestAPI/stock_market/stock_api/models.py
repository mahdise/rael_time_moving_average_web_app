from django.db import models

class employees(models.Model):
    firstname=models.CharField(max_length=10)
    latname = models.CharField(max_length=10)
    emp_id=models.IntegerField()

    def __str__(self):
        return self.firstname

