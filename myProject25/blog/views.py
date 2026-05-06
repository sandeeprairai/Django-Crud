from django.views.generic import ListView,DeleteView,CreateView,UpdateView,DetailView
from django.urls import reverse_lazy
from .models import Post

# list view
class PostListView(ListView):
    model=Post 
    template_name='blog/post_list.html'
    context_object_name='posts'

# detail view
class PostDetailView(DetailView):
    model=Post 
    template_name='blog/post_detail.html'
    context_object_name='post'
# Create view 
class PostCreateView(CreateView):
    model=Post 
    template_name='blog/post_form.html'
    fields=['title','content']
# Update view
class PostUpdateView(UpdateView):
    model=Post 
    template_name='blog/post_form.html'
    fields=['title','content']

# detail view 
class PostDeleteView(DeleteView):
    model=Post 
    template_name='blog/post_confirm_delete.html'
    success_url=reverse_lazy('post_list')