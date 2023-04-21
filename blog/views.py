from django.shortcuts import render,get_object_or_404 , HttpResponseRedirect

from django.utils import timezone
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.

def blog_view(request, **kwargs):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    for post in posts: # turn publish_status on(Ture) if published_date is passed
        if post.publish_status == False:
            post.publish_status = True
            post.save() 

    if kwargs.get('cat_name') != None:  # posts by category
        posts = posts.filter(category__name=kwargs['cat_name'])

    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])


    # pagination
    posts = Paginator(posts, 3)
    try :
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)



    context={'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single_view(request,pid):
    post = get_object_or_404(Post, pk=pid , published_date__lte=timezone.now())
    post.counted_views +=1  # count views
    post.save()

    next_post = Post.objects.filter(publish_status=True,
                                     published_date__gt=post.published_date,
                                        ).order_by('published_date').first()
    previous_post = Post.objects.filter(publish_status=True,
                                         published_date__lt=post.published_date,
                                            ).order_by('published_date').last()
    
    # Comment Area
    comments = Comment.objects.filter(post=post.id,approved=True)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # new_comment = form.save(commit=False)
            # new_comment.name = 'Unknown'     # warning simple-captcha is enabled.
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your comment submited successfully.')
        else:
            messages.add_message(request, messages.ERROR, "Your comment didn't submit, make sure you have a comment ticket and try again.")

    if not post.login_require :
        form = CommentForm()
        context = { 'post': post,
                    'next_post': next_post,
                    'previous_post': previous_post,
                    'comments': comments,
                    'form': form,
                        }
        return render(request, 'blog/blog-single.html', context)
    else:
        if request.user.is_authenticated:
            form = CommentForm()
            context = { 'post': post,
                        'next_post': next_post,
                        'previous_post': previous_post,
                        'comments': comments,
                        'form': form,
                            }
            return render(request, 'blog/blog-single.html', context)
        else:
            return render(request, 'account/login.html', )
            


def blog_search(request):
    posts =Post.objects.filter(published_date__lte=timezone.now())
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(summary__contains=s)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)