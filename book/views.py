import csv

import django
from django.db.models import Count, Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, CreateView

from book import crowling
from book.forms import BookSearchForm
from book.models import Post, Book, Category

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
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(FeedList, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context


class FeedDetail(DetailView):
    model = Post
    template_name = 'book/feed_detail.html'


class BookSearchView(FormView):           #책 검색
    form_class = BookSearchForm
    template_name = 'book/book_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_book']
        book_list = Book.objects.filter(book_title__icontains = searchWord).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = book_list

        return render(self.request, self.template_name, context)


class CreateReportView(CreateView):
    model = Post
    fields = ['book_name','content','image']
    template_name = 'book/create_report.html'


def categories_page(request, slug):
    if slug:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    context = {
        'category' : category,
        'categories' : Category.objects.all(),
        'post_list' : post_list,

    }
    return render(
        request,
        'book/feed_list.html',
        context
    )


