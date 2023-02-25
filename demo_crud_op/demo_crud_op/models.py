from django.db import models
from django import forms



class Employee(models.Model):
  e_name: models.CharField(unique=True,max_length=255)
  e_pass: models.CharField(max_length=255)
  