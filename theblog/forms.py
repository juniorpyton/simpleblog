from django import forms
from .models import Post , Category, Comment

choices = Category.objects.all().values_list('name','name')

liste = []

for item in choices:
	liste.append(item)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','author','category','body','header_image')


		widgets = {
			'title':forms.TextInput(attrs={'class': 'form-control'}),
			'author':forms.TextInput(attrs={'class': 'form-control', 'value':' ', 'id':'mesut', 'type':'hidden'}),
			#'author':forms.Select(attrs={'class': 'form-control'}),
			'category':forms.Select(choices=liste, attrs={'class': 'form-control'}),
			'body' : forms.Textarea(attrs={'class': 'form-control'}),
		}


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name','body')


		widgets = {
			'name' : forms.TextInput(attrs={'class': 'form-control'}),
			'body' : forms.Textarea(attrs={'class': 'form-control'}),
		}