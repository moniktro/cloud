from django.db import models
from django.contrib.auth.models import User

class uploadvideo(models.Model):
	name	= models.CharField(max_length=200)
	video	= models.FileField(upload_to='videos/videos_temp/')
	date	= models.DateTimeField()
	status	= models.BooleanField(default=True)
	message	= models.CharField(max_length=200)
	datepublish = models.DateTimeField()
	user	= models.ForeignKey(User)
