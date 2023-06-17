from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from book.models import Post


class BookSearchForm(forms.Form):
    search_book = forms.CharField(label='Search Book')


class ReportForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('book_name','content','image','category')