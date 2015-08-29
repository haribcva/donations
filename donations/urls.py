from django.conf.urls import patterns, url

from donations import views

urlpatterns = patterns('',
            url(r'^$', views.all_room_detail, name='all_room_detail'),
            url(r'^rooms$', views.all_room_detail, name='all_room_detail'),
            url(r'^rooms/(?P<room_name>\w+)/$', views.room_detail, name='room_detail'),
            )
