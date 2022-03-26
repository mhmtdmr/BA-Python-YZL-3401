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