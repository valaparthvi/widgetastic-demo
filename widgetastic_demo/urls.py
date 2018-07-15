from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.UserView, name='register'),
    url(r'^dynamic', views.DynamicView, name='dynamic'),
]
