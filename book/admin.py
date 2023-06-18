from django.contrib import admin

from .models import Post, Book, Category, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Book)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}

admin.site.register(Category, CategoryAdmin)

admin.site.register(Comment)