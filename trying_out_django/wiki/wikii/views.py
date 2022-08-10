from django.forms import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
# Create your views here.
class new_entry(forms.Form):
    title= forms.CharField(label="title")
    entry= forms.CharField(label="entry")    



def home(request):
    if "entry" and "title" not in request.session:
        request.session["entry"] = []
        request.session["title"] = []
        request.session["article"] = {}

    return render(request, "pages/home.html",{
        "new_entry": new_entry(),
        "list": request.session["title"]
        })

def new(request):
    if request.method == "POST":
        article = new_entry(request.POST)
        if article.is_valid():
            request.session["entry"] += [article.cleaned_data["entry"]]
            request.session["title"] += [article.cleaned_data["title"]]
            request.session["article"][article.cleaned_data["title"]] = article.cleaned_data["entry"]
            return HttpResponseRedirect(reverse("wikii:home"))
        else:
            return render(request,"page/new.html",{
                "new_entry": article
                })
    
    return render(request,"pages/new.html",{
        "new_entry": new_entry()
        })
def article(request, title):
    requested_title = title
    
    return render(request,"pages/article.html",{
        "title": requested_title,
        "entry": request.session["article"][requested_title]
        })