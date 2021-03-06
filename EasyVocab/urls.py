"""EasyVocab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
import Home.views as home_views
import Authentication.views as auth_views
import Dictionary.views as dic_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Home
    path('', home_views.home),
    # Authentication
    path('login', auth_views.login),
    path('signup', auth_views.signup),
    path('logout', auth_views.logout),
    # Dictionary
    path('dicsearch', dic_views.dictionary_search),
    path('dictionary', dic_views.dictionary_home)

]
