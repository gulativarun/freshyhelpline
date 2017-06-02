from __future__ import unicode_literals

from django.db import models

# Create your models here.

class AccPost(models.Model):
	title = models.CharField(max_length =120)
	#context = 
