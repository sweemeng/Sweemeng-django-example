from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=140)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=140)
    post_code = models.CharField(max_length=5)
