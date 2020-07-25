from django.db import models
from account.models import * 

# Create your models here.
class Hashtag(models.Model):
    content = models.TextField(unique = True)
    def __str__(self):
        return self.content

class Blog(models.Model):
    writer = models.CharField(max_length=100)
    title = models.CharField(max_length=30)
    body = models.TextField()
    time = models.DateTimeField()
    name = models.CharField(max_length=10)
    hashtags = models.ManyToManyField(Hashtag, blank = True)
    likes = models.ManyToManyField(
        signIn,
        through = 'Like',
        through_fields=('blog', 'user'),
        related_name='likes',
    )

    def __str__(self):
        return self.title


class Like(models.Model):
    blog = models.ForeignKey(Blog, on_delete= models.CASCADE, null = True)
    user = models.ForeignKey(signIn, on_delete= models.CASCADE, null = True)

class Comment(models.Model):
    commentbody = models.CharField(max_length = 30)
    time = models.DateTimeField()
    blog = models.ForeignKey(Blog,on_delete = models.CASCADE)
   
    def __str__(self):
        return self.commentbody

