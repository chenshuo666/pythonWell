"""s14django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from cmdb import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^h.html/', views.home),
    url(r'^index/',include("cmdb.urls")),
    #url(r'^article/',include("blogcontext.urls")),


    # url(r'^login', views.getLogin),
    # url(r'^home', views.getHome),
    # url(r'^index',views.getIndex),
    # url(r'^about',views.getAbout),
    # url(r'^blog',views.getBlog),
    # url(r'^contact',views.getContact),
    # url(r'^login_blog',views.getLogin_blog),
    # url(r'^portfolio',views.getPortfolio),
    # url(r'^register',views.getRegister)
]
