from django.db import models

# Create your models here.
class fullmore(models.Model):
	
	headlines = models.CharField(max_length = 500,primary_key = True)
	description = models.CharField(max_length = 2500,)
	hyperlink = models.URLField(max_length=2000,)
	source = models.CharField(max_length = 2000,)
class covid(models.Model):
	place = models.CharField(max_length = 200,)
	number = models.CharField(max_length = 200,)
class covid1(models.Model):
	place = models.CharField(max_length = 200,)
	number = models.CharField(max_length = 200,)

	
