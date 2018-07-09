from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, render_to_response
from django.utils import timezone
from .models import Post




def blog(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog.html', {'posts': posts})

    
   