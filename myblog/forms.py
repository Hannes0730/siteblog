from django import forms
from .models import Post, Category


choices = Category.objects.all().values_list('name', 'name')
choice_list =[]

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'summary', 'image', 'add_file')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'add title to your post'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'add tag to you title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'name', 'type':'hidden'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'add content'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Input a short summary...'}),

        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'summary')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'add title to your post'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'add tag to you title'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'add content'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'add content'}),
        }