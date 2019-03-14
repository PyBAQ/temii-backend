"""temii URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

api_urls = [
    url(r"^", include("apps.charlas.urls")),
    url(r'^', include('rest_framework.urls')),
]

if settings.DEBUG:
    from rest_framework.documentation import include_docs_urls
    api_urls += [url(r'^docs/', include_docs_urls(title='API Temii'))]



urlpatterns = [
    url(r'^api/', include(api_urls)),
    url(r'^admin/', include(admin.site.urls)),
]
