"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import post.views
import account.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',post.views.main, name = "main"),
    path('new/',post.views.new, name = "new"),
    path('create/',post.views.create, name = "create"),
    path("update/<int:id>",post.views.update, name = "update"),
    path("blog_update/<int:id>",post.views.blog_update, name = "blog_update"),
    path("delete/<int:id>",post.views.delete, name = "delete"),
    path("more/<int:id>",post.views.more, name = "more"),
    path("back/<int:id>",post.views.back, name = "back"),
    path("like/",post.views.like, name = "like"),
    path("comment/<int:id>",post.views.comment, name = "comment"),
    path('account/',include(account.urls)),
    path("search/<int:id>",post.views.search, name = "search"),
    path('hashtag/<int:tag_id>/',post.views.hashtag, name = "hashtag"),
]
