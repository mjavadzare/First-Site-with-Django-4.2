from django.contrib.sitemaps import Sitemap
from projects.models import Project
from django.urls import reverse

class ProjectSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Project.objects.filter(publish_status=True)

    def lastmod(self, obj):
        return obj.published_date
    
    def location(self, item):
        return reverse('Projects:single', kwargs={'pid':item.id})
