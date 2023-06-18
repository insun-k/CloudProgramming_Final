import csv

import django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Count, Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView

from book import crowling
from book.forms import BookSearchForm, ReportForm, CommentForm
from book.models import Post, Book, Category, Comment

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
        context['CommentForm'] = CommentForm
        return context


class FeedDetail(DetailView):
    model = Post
    template_name = 'book/feed_detail.html'

    def get_context_data(self, **kwargs):
        context = super(FeedDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['CommentForm'] = CommentForm
        return context



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


@login_required
@require_http_methods(['GET', 'POST'])
def CreateReport(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            return redirect('feed')
    else:
        form = ReportForm(request.POST)
    return render(request, 'book/create_report.html',{'form':form})


class UpdateReportView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['book_name','content','image','category']

    template_name = 'book/update_report.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().user:
            return super(UpdateReportView, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

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

@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
        return redirect(post.get_absolute_url())
    return redirect('main:login')

