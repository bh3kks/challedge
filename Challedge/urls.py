from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    
	url(r'^main/$', 'chatting.views.main_view', name='main_view'),
	# 메인 화면 url

	url(r'^chat/$', 'chatting.views.chat_view', name='chat_view'),
	# 메인 화면 url


    url(r'^admin/', include(admin.site.urls)),
)
