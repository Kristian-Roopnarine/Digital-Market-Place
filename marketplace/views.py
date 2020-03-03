from django.shortcuts import render
from .models import Book
# Create your views here.

def book_list_view(request):
    context={}
    context['queryset'] = Book.objects.all()
    return render(request,'marketplace/book_list.html',context)