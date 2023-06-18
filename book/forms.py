from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from book.models import Post, Comment


class BookSearchForm(forms.Form):
    search_book = forms.CharField(label=False)


class ReportForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('book_name','content','image','category')
        labels = {
            'book_name' : '책 제목',
            'content' : '내용',
            'image' : '첨부파일',
            'category' : '카테고리'

        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ('post', 'user',)
