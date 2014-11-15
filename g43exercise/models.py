from django.db import models
from django.utils import timezone
from django.conf import settings

import datetime

# Create your models here.
class Article(models.Model):
	# The barebones of a published Article. Includes a secondary image option
	article_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=50)
	pub_date = models.DateTimeField('date published')
	category = models.CharField(max_length=50)
	hero_image = models.ImageField(upload_to='heroes/', default='heroes/default-hero.jpg')
	optional_image = models.ImageField(upload_to='extra/', default='extra/default-hero.jpg')
	body_text = models.TextField(max_length=5000)
	def __str__(self):
		return self.title + ' by ' + self.author
	