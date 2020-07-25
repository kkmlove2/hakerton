from django import forms
from .models import Blog

class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "body", "image"]
        widgets = {
            'title' : forms.TextInput(attrs ={'class' : 'form_title','placeholder':'30자 이내로 입력 가능합니다.'}),
            'body' : forms.TextInput(attrs={'class' : 'form_body'}),
        }
        lables = {
            'title' : '제목',
            'body' : '내용',
            'image' : '사진',
        }
        required = {
            'image' : False,
        }

def __init__(self, *args, **kwargs):
    super(BlogPost, self).__init__(*args, **kwargs)
    self.fields['title'].widget.attrs['maxlength'] = 30