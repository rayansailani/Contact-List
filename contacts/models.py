from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    # image
    contact_number = models.CharField(max_length=11)
    description = models.TextField(max_length=250)
