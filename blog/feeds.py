from django.contrib.syndication.views import Feed
from blog.models import Post
# from django.urls import reverse

class LatestEntriesFeed(Feed):
    title = "Blog newest posts"
    link = "/rss/feed"
    description = "best blog ever."

    def items(self):
        return Post.objects.filter(publish_status=True ).order_by('-published_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.summary

    # item_link is only needed if Post has no get_absolute_url method.
    # def item_link(self, item):
    #     return reverse('news-item', args=[item.pk])