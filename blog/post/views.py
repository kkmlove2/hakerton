from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.utils import timezone
from django.http import HttpResponse
import json
from django.core.paginator import Paginator
from.forms import BlogPost
# Create your views here.

def main(request):
    blogs = Blog.objects.all().order_by('-id')
    paginator=Paginator(blogs,3)
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)
    return render(request, 'main.html',{"page_posts":page_posts})


def new (request):
    return render(request, "new.html")

def create(request):
    if request.method == 'POST':
        form = BlogPost(request.POST, request.FILES)
        if form.is_valid():
            blog= form.save(commit=False)
            blog.time = timezone.now()
            blog.save()
            body = form.cleaned_data.get('body')
            body_words = body.split()
            for word in body_words:
                if word[0] == "#":
                    tag = Hashtag.objects.get_or_create(content=word)
                    blog.hashtags.add(tag[0])
            return redirect('main')
        return redirect('main')
    elif request.method == 'GET':
        form = BlogPost()
        return render(request, "new.html",{"form":form})



def update(request,id):
    blog = get_object_or_404(Blog, pk = id)
    blog.title = request.GET["title"]
    blog.body = request.GET["body"]
    blog.name = request.GET["name"]
    blog.save()
    return redirect('main')

def blog_update(request,id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request, "updatepage.html",{"blog":blog})

def delete(request,id):
    blog = get_object_or_404(Blog, pk = id)
    blog.delete()
    return redirect('main')

def more(request,id):
    blog = get_object_or_404(Blog, pk = id)
    print(blog.body)
    comments = Comment.objects.filter(blog =  blog.id)
    body = blog.body
    body_word = body.split()
    blog_body = ""
    for word in body_word:
        if word[0] !='#':
            blog_body +=word
            blog_body +=' '

    return render(request, "more.html",{"blog":blog, "comments":comments,'blog_body':blog_body})

def back(request,id):
    blog = get_object_or_404(Blog, pk = id)
    return redirect('main')

def like(request):
    id = request.POST.get('pk',None)
    blog = get_object_or_404(Blog, pk=id)
    blog_like, blog_created = blog.like_set.get_or_create(user = request.user)
    if not blog_created:
        blog_like.delete()
        message = "좋아요 취소"
    else:
        message = "좋아요"
    context = {
                'message' : message,
                }
    return HttpResponse(json.dumps(context), content_type= "application/json")

def comment(request,id):
    if request.method == "POST":
        blog = get_object_or_404(Blog, pk=id)
        commentbody = request.POST["commentbody"]
        comment = Comment()
        comment.commentbody = commentbody
        comment.time = timezone.now()
        comment.blog = blog
        comment.blog = get_object_or_404(Blog, pk=id)
        comment.save()
        return redirect("more", id)
    else:
        return rendirect("main")


def hashtag(request,tag_id):
    h = Hashtag.objects.get(pk = tag_id)
    hashts = h.blog_set.all()
    return render(request, "hashtag.html",{"hashts":hashts})


def search(request, id):
    # search = request.GET["search"]
    searchs = Blog.objects.filter(title =  request.GET["search"])
    return render(request, "search.html",{"searchs":searchs})


