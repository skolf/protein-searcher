from django.db import models
from django.conf import settings

class Search(models.Model):

    id = models.AutoField(primary_key=True)
    expression = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
