from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

from book.models import Book
from main.forms import UserForm


# Create your views here.
def index(request):
    book_list = Book.objects.all()[:36]
    context = {'book_list' : book_list}
    return render(
       request,
        'main/main_view.html',
        context

    )

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'main/signup.html',{'form':form})
# Create your views here.



