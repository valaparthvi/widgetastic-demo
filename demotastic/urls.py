"""demotastic URL Configuration

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
from widgetastic_demo import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.UserView.as_view(), name='register'),
    url(r'^dynamic/$', views.DynamicView.as_view(), name='dynamic'),
    url(r'^datepicker/$', views.DatePickerView.as_view(), name='datepicker'),
]
