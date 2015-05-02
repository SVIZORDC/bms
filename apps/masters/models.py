from django.db import models

from apps.accounts.models import Company


class Project(models.Model):

    company = models.ForeignKey(Company)

    name = models.CharField(max_length=60)


class SourceMaster(models.Model):

    project = models.ForeignKey(Project)

    file = models.FileField(upload_to='source_masters')


class ReleaseMaster(models.Model):

    source_master = models.ForeignKey(SourceMaster)

    file = models.FileField(upload_to='release_masters')
