from django.db import models
from django.urls import reverse

class Book(models.Model):
	name = models.CharField(max_length = 50)
	picture = models.ImageField()
	author = models.CharField(max_length = 30, default='anonymous')
	email = models.EmailField(blank = True)
	describe = models.TextField(default = 'demo book')
	def __str__(self):
		return self.name


class Author(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name
	
	def get_absolute_url(self):
		return reverse('books:author-update', args=[self.id])