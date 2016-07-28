from django.conf.urls import url
from account import views


urlpatterns = [
    url(r'^account/(?P<userID>[0-9]+)/$', views.account, name='account'),
    url(r'^register/$', views.register, name='register'),
    url(r'^userLogin/$', views.userLogin, name='userLogin'),
    url(r'^userLogout/$', views.userLogout, name='userLogout'),
    url(r'^photoUrlUpdate/(?P<userID>[0-9]+)/$', views.photoUrlUpdate, name='photoUrlUpdate'),
    url(r'^profileUpdate/(?P<userID>[0-9]+)/$', views.profileUpdate, name='profileUpdate'),
]