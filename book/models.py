from django.db import models


# Create your models here.
class Book(models.Model):
    book_title = models.CharField(max_length=50)
    img_url = models.TextField(null=True)
    book_content = models.TextField(blank=True)
    book_link = models.TextField(null=True)
    book_genre = models.TextField(null = True)


class Post(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=30)
    #book_name = models.ForeignKey(Book, on_delete=models.PROTECT, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='book/images/%Y/%m/%d/')

    def __str__(self):
        return f'[{self.pk}] {self.book_name}'

    def get_absolute_url(self):
        return f'/book/feed/{self.pk}/'