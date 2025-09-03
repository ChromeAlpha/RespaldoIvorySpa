from django.db import models

class project(models.Model):
    name = models.CharField(max_length=200)
