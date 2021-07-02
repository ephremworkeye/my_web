from django.shortcuts import render, get_object_or_404
from .models import Author, Post

# Create your views here.
def post_list(request):
    post_lists = Post.objects.all()
    return render(request, 'web/post_list.html', {'post_lists': post_lists })
    
def post_detail(request, id, slug):
    post = get_object_or_404(Post, id=id, slug=slug)
    return render(request, 'web/post_detail.html', {'post': post})
    
def contact(request):
    return render(request, 'web/contact.html')
    
def about(request):
    return render(request, 'web/about.html')
    
def work(request):
    post_lists = Post.objects.all()
    return render(request, 'web/work.html', {'post_lists': post_lists })
    
def terms(request):
    return render(request, 'web/terms.html')
    
def cookies(request):
    return render(request, 'web/cookies.html')
    
def privacy(request):
    return render(request, 'web/privacy.html')
    