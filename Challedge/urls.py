from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       
                       url(r'^main/$', 'chatting.views.main_view', name='main_view'),
                       
                       url(r'^chat/$', 'chatting.views.chat_view'),
                       
                       url(r'^admin/', include(admin.site.urls)),
                       
                       url(r'^login_check/', 'chatting.views.login_check'),
                       )
