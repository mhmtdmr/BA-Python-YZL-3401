from django.shortcuts import render
from News.models import News
# Create your views here.

def NewsHomePage(request):
    haberler = News.objects.all()
    veri = {
        "sehir":"İstanbul","ilce":"Kadıköy","mahalle":"Caferaga","news":haberler
        }
    return render(request,"homepage.html",veri)
