from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post # dot before models: current directory/application
# ^have to include the model we wrote in models.py 
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.
def post_list( request ) :
    posts = Post.objects.filter( published_date__lte = timezone.now() ).order_by( 'published_date' )
    return render( request, 'blog/post_list.html', { 'posts': posts } ) # last parameter is where we can add things for template to use
    # passing in 'posts', the variable for our queryset

def post_detail( request, pk ) : 
    post = get_object_or_404(Post, pk=pk)
    return render( request, 'blog/post_detail.html', {'post': post} )

def post_new( request ) :
    if request.method == "POST" :
        # if method is POST, then we want to construct POSTFORM w/ data from the form
        form = PostForm( request.POST )
        # check if form is valid:
        if form.is_valid() :
            post = form.save( commit = False ) # don't want to save the post yet -> want to add author 1st
            post.author = request.user
            post.published_date = timezone.now()
            post.save() 
            return redirect( 'post_detail', pk = post.pk )  
    else :
        form = PostForm()
    return render( request, 'blog/post_edit.html', { 'form': form } )

def post_edit( request, pk ) :
    post = get_object_or_404( Post, pk=pk ) 
    if request.method == "POST" :
        form = PostForm( request.POST, instance = post )
        if form.is_valid() :
            post = form.save( commit = False )
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect( 'post_detail', pk = post.pk )
    else :
        form = PostForm( instance = post )
    return render( request, 'blog/post_edit.html', {'form': form } )

    