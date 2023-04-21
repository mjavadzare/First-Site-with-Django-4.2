from django import template
from django.template.defaultfilters import stringfilter
from blog.models import *

register = template.Library()

@register.filter
@stringfilter
def upto(value, delimiter=None):
    return value.split(delimiter)[0]
upto.is_safe = True

@register.inclusion_tag('website/widgets/latest-posts.html', name='latest_posts')
def latest_posts(arg=6):
    posts = Post.objects.filter(publish_status= True).order_by('-published_date')[:arg]
    cat_dict = {}
    categories = Category.objects.all()
    for name in categories:
        cat_dict[name] = name
    return {'latest_posts': posts,'categories': cat_dict.items() }


