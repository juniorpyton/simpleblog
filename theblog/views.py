from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post , Category, Comment, Contact
from .forms import PostForm , CommentForm
from django.urls import reverse_lazy

class HomeView(ListView):
 	model = Post
 	template_name = 'home.html'
 	#ordering = ['id']
 	ordering = ['-post_date']

 	def get_context_data(self, *args, **kwargs):
 		cat_menu = Category.objects.all()
 		context = super(HomeView, self).get_context_data(*args , **kwargs)
 		context["cat_menu"] = cat_menu
 		return context

def CategoryView(request, cats):
	category_post = Post.objects.filter(category=cats)
	return render(request, 'categories.html', {'cats':cats.title, 'category_post':category_post})

class ArticleDetailView(DetailView):
	model = Post
	template_name  = 'article_details.html'

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'
	#fields = '__all__'
	#fields = ('title','body')

class AddCategoryView(CreateView):
	model = Category
	#form_class = PostForm
	template_name = 'add_category.html'
	fields = '__all__'

	#fields = ('title','body')


class UpdatePostView(UpdateView):
	model = Post
	form_class = PostForm
	template_name = 'update_post.html'

class DeletePostView(DeleteView):
	model = Post
	template_name ='delete_post.html'
	success_url  = reverse_lazy('home')

class AddCommentView(CreateView):
	model = Comment
	template_name = 'add_comment.html'
	form_class = CommentForm
	def form_valid(self,form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)
	success_url  = reverse_lazy('home')

class AddContactView(CreateView):
	model = Contact
	template_name = 'contact.html'
	fields = '__all__'
	success_url = reverse_lazy('home')