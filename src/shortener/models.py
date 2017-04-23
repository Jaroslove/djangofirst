from django.db import models


class KirrURL(models.Model):
	"""docstring for KirrURL"""
	url = models.CharField(max_length=220)
	shortcode = models.CharField(max_length=15, unique=True)
	def __str__(self):
		return str(self.url)
	def __unicode__(self):
		return str(self.url)
		

