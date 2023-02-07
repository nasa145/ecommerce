


from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    image = models.ImageField(upload_to="categories/%y/%m/%d", blank=True)
    slug = models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering = ('-name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('shop:products_by_category', args=[self.slug])

    def __str__(self):
        return self.name



class Brand(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)
    image = models.ImageField(upload_to="brand/images", blank=True)

    def __str_(self):
        return F"{self.name}"

    def get_absolute_url(self):
        return reverse('shop:products_by_brand', args=[self.slug])



class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    short_info = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="brand_products", blank=True)
    sale = models.BooleanField(default=False)
    SKU = models.CharField(max_length=250, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug] )

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(User,related_name='user', on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='reviews', on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review by {self.user} for {self.product}"


# A model to store emails for users who usubscribed for the newsletter page
class NewsletterSubscriber(models.Model):
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Newsletter Subscribers"

