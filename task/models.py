from django.db import models

class Task(models.Model):
	alltasks = models.TextField(max_length=100)
# Create your models here.
