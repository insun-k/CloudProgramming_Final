from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
    def get_absolute_url(self):
        return f'/book/feed/{self.slug}'

class Book(models.Model):
    book_title = models.CharField(max_length=50)
    img_url = models.TextField(null=True)
    book_content = models.TextField(blank=True)
    book_link = models.TextField(null=True)
    book_genre = models.TextField(null = True)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=30,blank=True)
    #book_name = models.ForeignKey(Book, on_delete=models.PROTECT, null=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='book/images/%Y/%m/%d/',blank=True,null=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}] {self.book_name}'

    def get_absolute_url(self):
        return f'/book/feed/{self.pk}/'



