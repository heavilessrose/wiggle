"""wiggle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


from search.views import home, search, detail, entitlements

urlpatterns = [
    path('search', search, name='search'),
    path('entitlements', entitlements, name='entitlements'),
    re_path(r'^view/(?P<index>.*)/(?P<doc_id>.*)/$', detail, name='detail'),
    re_path('^$', home),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()