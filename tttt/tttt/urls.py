from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'tttt.views.home', name='home'),
    url(r'^api/pc/feed/$', 'tttt.views.myfeed', name='myfeed'),
    url(r'^i\d*/$', 'tttt.views.deelconi', name='dellconi'),
    #url(r'^a64604\d*/$', 'tttt.views.deelcon64604', name='dellcona'),
    url(r'^a\d*/$', 'tttt.views.deelcon64607', name='dellcona'),
    url(r'^p\d*/*$', 'tttt.views.dellconp', name='dellconp'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^mytest$', 'tttt.views.mytest', name='home'),

    #url(r'^admin/', include(admin.site.urls)),
)
