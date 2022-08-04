from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post # dot before models: current directory/application
# ^have to include the model we wrote in models.py 

# Create your views here.
def post_list( request ) :
    posts = Post.objects.filter( published_date__lte = timezone.now() ).order_by( 'published_date' )
    return render( request, 'blog/post_list.html', { 'posts': posts } ) # last parameter is where we can add things for template to use
    # passing in 'posts', the variable for our queryset

def post_detail( request, pk ) :
    post = get_object_or_404(Post, pk=pk)
    return render( request, 'blog/post_detail.html', {'post': post} )
