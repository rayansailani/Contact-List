from django.db import models
from accounts.models import Account

# Create your models here.


class Contact(models.Model):
    user_name = models.ForeignKey(Account, on_delete = models.CASCADE)
    name = models.CharField(max_length=50,blank=False,null=False)
    contact_number = models.CharField(max_length=11,blank=False,null=False)
    description = models.TextField(max_length=250,blank=True,null = False)
