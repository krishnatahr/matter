from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     url(r'^$', 'maid.views.home', name='home'),
	 url(r'^admin/', include(admin.site.urls)),
     url(r'^redactor/', include('redactor.urls')),
	(r'^maid_profile/(?P<pk>\d+)/', 'maid.views.maid_profile'),
	(r'^maid_edit/(?P<pk>\d+)/', 'maid.views.agency_maid_edit'),
	(r'^print_maid_profile/(?P<pk>\d+)/', 'maid.views.print_maid_profile'),
    (r'^attach_maid_profile/(?P<pk>\d+)/', 'maid.views.attach_maid_profile'),
	(r'^aboutus/$', 'maid.views.aboutus'),
	(r'^services/$', 'maid.views.services'),
    (r'^maid_search/$', 'maid.views.search'),
	(r'^faq/$', 'maid.views.faq'),
	(r'^contactus/$', 'maid.views.contact'),
	(r'^agency_profile/$', 'maid.views.agency_profile'),
	(r'^maid_list/$', 'maid.views.maid_list'),
	(r'^login_view/$', 'maid.views.login_view'),
	(r'^logout_view/$', 'maid.views.logout_view'),
	(r'^agency_registration/$', 'maid.views.agency_registration'),
	(r'^add_maid/$', 'maid.views.add_maid'),
	(r'^edit_account/$', 'maid.views.edit_account'),
	(r'^agency_maid_list/$', 'maid.views.agency_maid_list'),
	(r'^maid_delete/$', 'maid.views.agency_maid_delete'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
