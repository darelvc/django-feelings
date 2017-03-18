from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url('^', include('django.contrib.auth.urls')),
]
