from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=200,db_index=True) 
	slug = models.SlugField(max_length=200,unique=True)
	class Meta:
		ordering = ('name',)
		verbose_name = 'category' 
		verbose_name_plural = 'categories'
	def __str__(self): 
		return self.name

	def get_absolute_url(self):
		return reverse('cake:product_list_by_category',args=[self.slug])






class Product(models.Model):
	category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE) 
	name = models.CharField(max_length=200, db_index=True) 
	slug = models.SlugField(max_length=200, db_index=True)
	image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
	description = models.TextField(blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	class Meta:
		ordering = ('name',) 
		index_together = (('id', 'slug'),)
	def __str__(self): 
		return self.name

	def get_absolute_url(self):
		return reverse('cake:product_detail',args=[self.id, self.slug])

class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    def get_photo_url(self):
    	if self.images and hasattr(self.images, 'url'):
    		return self.images.url
    	else:
    		return "https://alumni.crg.eu/sites/default/files/default_images/default-picture_0_0.png"


class Contact(models.Model):
	name = models.CharField(max_length=200, db_index=True) 
	email = models.EmailField()
	body = models.TextField()



