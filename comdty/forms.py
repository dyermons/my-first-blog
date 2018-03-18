from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'file', 'image')
    #     fields 추가했으면 html 추가하고 manage.py makemigrations로 db 컬럼 추가해줘야함

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['file'].required = False
