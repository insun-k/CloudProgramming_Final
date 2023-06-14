import csv

import django
from django.db.models import Count
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from book import crowling
from book.models import Post, Book

django.setup()

A = Book.objects.aggregate(Count('id'))
B = str(A).split(':')[1].split('}')[0].split(' ')[1]
print(B)

if int(B) < 320:
   crowling.function()
else:
    pass

# Create your views here.
class FeedList(ListView):
    model = Post
    template_name = 'book/feed_list.html'


class FeedDetail(DetailView):
    model = Post
    template_name = 'book/feed_detail.html'




