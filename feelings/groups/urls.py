from django.conf.urls import url, include

from . import views


company_patterns = [
    url(r'^create/$', views.Create.as_view(), name='create'),
    url(r'edit/(?P<slug>[-\w]+)/$', views.Update.as_view(), name='update'),
    url(r'^(?P<slug>[-\w]+)/$', views.Detail.as_view(), name='detail'),
]


urlpatterns = [
    url(r'^companies/', include(company_patterns, namespace='companies')),
]