from django.conf.urls import url

from . import views

app_name = 'fn'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detect$', views.detect, name='detect'),
    url(r'^result/(?P<url_hash>\w+)$', views.results, name='results'),
]
