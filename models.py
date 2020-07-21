from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField()
	digital = models.BooleanField(default=False,null=True, blank=True)
	image = models.ImageField(null=True, blank=True)
	slug = models.SlugField(max_length=150, unique=True)

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
    
	def get_absolute_url(self):
		return reverse("single_page", kwargs={"slug":self.slug})

	class Meta:
         unique_together = ('slug', 'name') 
         ordering = ["-pk"]	

