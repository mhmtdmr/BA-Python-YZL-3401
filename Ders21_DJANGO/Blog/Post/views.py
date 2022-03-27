from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Blog

# Create your views here.
def merhaba(request):
    # return HttpResponse("<h1>Merhaba</h1>")
    datas = {"tarih":datetime.now,"isim":"Aysel","soyisim":"Demir"}
    return render(request,"merhaba.html",datas)

def world(request):
    return HttpResponse("<h1>Dünya</h1>")

def index(request):


    # # Veritabanından önceki kodlar.
    # b1 = Blog()
    # b1.BlogTitle = "Blog 1"
    # b1.BlogText = "Blog 1 Text"
   

    # b2 = Blog()
    # b2.BlogTitle = "Blog 2"
    # b2.BlogText = "Blog 2 Text"
    # blogs = [b1,b2] # Blogları listeye koyduk

    # # Veritabanından sonraki kodlar.

    # b1.save() # veritabanına kaydetsin.
    # b2.save()# veritabanına kaydetsin.

    blogs = Blog.objects.all() # veritabanındaki bütün Blog nesnelerini getir.
    return render(request,"index.html",{"bloglar":blogs})


def homepage(request):
    bloglist = Blog.objects.all()

    return render(request,"homepage.html",{"bloglar":bloglist})

def about(request):
    return render(request,"about.html")

def insertNewBlogs(request):
    b1 = Blog()
    b1.BlogTitle = "Blog 1 Title"
    b1.BlogText = "Blog 1 Text"

    b2 = Blog()
    b2.BlogTitle = "Blog 2 Title"
    b2.BlogText = "Blog 2 Text"

    b3 = Blog()
    b3.BlogTitle = "Blog 3 Title"
    b3.BlogText = "Blog 3 Text"

    b1.save()
    b2.save()
    b3.save()

    return HttpResponse("<h1> New blogs are added </h1>")

def blog(request,blogid:int):
    myBlog = Blog.objects.get(pk=blogid) 
    # context = {"blog":myBlog}
    return render(request,"blog.html",{"blog":myBlog})
