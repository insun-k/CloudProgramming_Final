from django import forms

class BookSearchForm(forms.Form):
    search_book = forms.CharField(label='Search Book')