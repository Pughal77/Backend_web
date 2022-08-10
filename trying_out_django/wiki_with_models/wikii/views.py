from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import community_article_data 
from .forms import new_entry

'''def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("user:login"))
    user_list = community_article_data.objects.filter(user = request.user)
    for obj in user_list:
        user_list = []
        user_list.append(obj.pk)
    def title_retriever(id):
        retrieved_title = community_article_data.objects.get(pk=id)
        return retrieved_title.title

    
    community_list = community_article_data.pk
    return render(request, "pages/home.html",{
        "community_list": community_list,
        "user_list": user_list,
        "title_retriever": title_retriever()
        })'''
# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("user:login"))
    user_list = community_article_data.objects.filter(user = request.user)
    community_list = community_article_data.objects.all()
    return render(request, "pages/home.html",{
        "community_list": community_list,
        "user_list": user_list,
        })

def new(request):
    if request.method == "POST":
        article = new_entry(request.POST)
        if article.is_valid():
            details = article.save(commit=False)
            details.user = request.user
            article.save()
            return HttpResponseRedirect(reverse("wikii:home"))
        else:
            return render(request,"page/new.html",{
                "new_entry": article
                })
    
    return render(request,"pages/new.html",{
        "new_entry": new_entry()
        })
def article(request, pk):
    requested_title = community_article_data.objects.get(pk=pk)
    
    return render(request,"pages/article.html",{
        "title": requested_title.title,
        "entry": requested_title.entry,
        "pk": requested_title.pk
        })
def edit(request, pk):
    edit_auth = False
    current = community_article_data.objects.get(pk=pk)
    if request.user == current.user:
        edit_auth = True
    if request.method == "POST":
        edit = new_entry(request.POST)
        if edit.is_valid():
                
            current.title = edit.cleaned_data["title"]
            current.entry = edit.cleaned_data["entry"]
            current.save()
        else:
            return render(request,"pages/edit.html",{
                "id": pk,
                "edit_entry": edit
            })
    
    return render(request,"pages/edit.html",{
        "id": pk,
        "edit_entry": new_entry(),
        "edit_auth": edit_auth
    })