"""async_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from async_app.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/', TestAsync.as_view()),
    url(r'^test_sync/', TestAsyncFromSync.as_view()),
    url(r'^db_sync/', TestDbCall.as_view()),
    url(r'^async_db/', TestAsyncDbCall.as_view()),
    url(r'^hello/', HelloWorld.as_view()),
]
