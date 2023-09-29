from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body')

        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "title-tag": forms.TextInput(attrs={'class': 'form-control'}),
            "author": forms.Select(attrs={'class': 'form-control'}),
            # "body": forms.Textarea(attrs={'class': 'form-control'}),
            "body" : forms.CharField(widget=CKEditorWidget()),
        }
class EditForm(forms.ModelForm):
      class Meta:
          model = Post
          fields = ('title', 'author', 'body')

          widgets = {
              "title": forms.TextInput(attrs={'class': 'form-control'}),
              "author": forms.Select(attrs={'class': 'form-control'}),
              # "body": forms.Textarea(attrs={'class': 'form-control'}),
              "body": forms.CharField(widget=CKEditorWidget()),
          }





