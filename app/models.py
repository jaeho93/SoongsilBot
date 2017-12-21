from django.db import models

class PhoneBook(models.Model):
    department = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    spot = models.CharField(max_length=128)
    task = models.CharField(max_length=128)
    contact = models.CharField(max_length=128)

    def __str__(self):
        return self.title
# Create your models here.
