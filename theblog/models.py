from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name 

	def get_absolute_url(self):
		return reverse('home')

class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	bio  = models.TextField()
	profil_pic = models.ImageField(null=True, blank=True, upload_to="images/")
	website_url = models.CharField(max_length=255 , blank=True, null=True)
	fb_url = models.CharField(max_length=255 , blank=True, null=True)

	def __str__(self):
		return str(self.user)

	def get_absolute_url(self):
		return reverse('home')
			
class Post(models.Model):
	title = models.CharField(max_length=255)
	header_image = models.ImageField(null=True, blank=True, upload_to="images/")
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.CharField(max_length=255, default= "Select Category")
	body = RichTextField(blank=True, null=True)
	#body = models.TextField()
	post_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.title + ' | ' + str(self.author) + ' |' + str(self.post_date)

	def get_absolute_url(self):
		#return reverse('article-detail', args=(str(self.id )))
		return reverse('home')

class Comment(models.Model):
	post = models.ForeignKey(Post, related_name="comments", null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	body = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s - %s' % (self.post, self.name)