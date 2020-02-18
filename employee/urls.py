"""employee URL Configuration

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
from django.urls import path
from django.conf.urls import url
from hrm.api import UserList, Bulbdata,temperature_reading
from hrm import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'https://immense-castle-47898.herokuapp.com/',views.home),
    # url(r'^$', 'index', name='index'),
    url(r'bulb_status',views.bulb,name='bulb_status'),
    url(r'api/users_list/', UserList.as_view(), name='user_list'),
    url(r'api/bulb_data/', Bulbdata.as_view(), name='bulb_data'),


]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
