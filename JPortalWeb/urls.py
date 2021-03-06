"""JPortalWeb URL Configuration

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
from django.views import generic
from crawl.views import *
from registration import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.loginList.as_view()),
    url(r'^StudSubjectTaken/$', StudSubjectTaken.as_view()),
    url(r'^StudCGPAReport/$', StudCGPAReport.as_view()),
    url(r'^StudSubjectFaculty/$', StudSubjectFaculty.as_view()),
    url(r'^StudentEventGradesView/$', StudentEventGradesView.as_view()),
    url(r'^$', generic.TemplateView.as_view(template_name='mainview.html')),
]
