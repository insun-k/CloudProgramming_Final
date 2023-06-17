from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BookSearchForm(forms.Form):
    search_book = forms.CharField(label='Search Book')


