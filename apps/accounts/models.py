from django.db import models


class Company(models.Model):

    name = models.CharField(max_length=60)


class User(models.Model):

    company = models.ForeignKey(Company)

    mobile = models.CharField(max_length=13, blank=False)
