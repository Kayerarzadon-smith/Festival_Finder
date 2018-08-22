from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.landing),
	url(r'^login$', views.login),
	url(r'^logout$', views.logout),
	url(r'^register$', views.register),
	url(r'^home$', views.dashboard),
	url(r'^New$', views.FestivalAdderPage),
	url(r'^create$', views.CreateActivityProcessor),
	url(r'^activity/home$', views.dashboard),
	url(r'^activity/logout$', views.logout),
	url(r'^activity/(?P<id>\d+)$', views.ActivityInfoPage),
	url(r'^delete/(?P<id>\d+)$', views.delete),
	url(r'^join/(?P<id>\d+)$', views.Join),
	url(r'^leave/(?P<id>\d+)$', views.Leave),
]