from django.db import models

# Create your models here.


class People(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=30)
    email = models.EmailField(blank=True)


