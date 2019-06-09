from django.db import models
from django.conf import settings

class Protein(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1024)
    code = models.CharField(max_length=32)
    sequence_file_name = models.CharField(max_length=255)

class Search(models.Model):

    id = models.AutoField(primary_key=True)
    query = models.CharField(max_length=1024)
    processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
