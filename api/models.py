from django.db import models
from django.conf import settings
from django.contrib.sessions.models import Session

class Protein(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1024)
    code = models.CharField(max_length=32)
    sequence_file_name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Search(models.Model):

    id = models.AutoField(primary_key=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    query = models.CharField(max_length=1024)
    processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Result(models.Model):

    id = models.AutoField(primary_key=True)
    search = models.OneToOneField(Search, on_delete=models.CASCADE)
    protein = models.ForeignKey(Protein, blank=True, null=True, on_delete=models.PROTECT)
    location = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
