"""
URL configuration for BrandNewSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap
from website.views import *
from blog.sitemaps import *
from projects.sitemaps import *

sitemaps = {
    'static': StaticViewSitemap,
    'blog' : BlogSitemap,
    'projects' : ProjectSitemap,
}



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('blog/', include('blog.urls')),
    path('', include('account.urls')),
    path('projects/', include('projects.urls')),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    re_path(r'^robots\.txt', include('robots.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')), # The CKEditor path
    path('captcha/', include('captcha.urls')),
]

# admin interface Header
admin.site.site_header = 'Mikey'
admin.site.index_title = 'Admin Panel'

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#MAINTENANCE_MODE
from django.urls import re_path
from django.conf import settings
from django.views.generic.base import TemplateView

if settings.MAINTENANCE_MODE:
   urlpatterns.insert(0, re_path(r'^', TemplateView.as_view(template_name='maintenance.html'), name='maintenance'))
