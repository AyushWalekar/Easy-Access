
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.formView, name='formview'),
    url(r'^login$', views.login, name='formview'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^test$', views.test, name='test'),
    url(r'^[a-z]|\d$', views.post_list, name='post_list'),
]
