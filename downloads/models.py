from django.db import models

class download(models.Model):
	path=models.CharField(max_length=500)
	description=models.CharField(max_length=500)
	owner=models.CharField(max_length=100)