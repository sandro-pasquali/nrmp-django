from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

	url(r'^$', 'home.views.index'),
	url(r'^candidate/(?P<candidate_id>\d+)/$', 'home.views.candidate'),
	url(r'^program/(?P<program_id>\d+)/$', 'home.views.program'),


    # Examples:
    # url(r'^$', 'nrmp.views.home', name='home'),
    # url(r'^nrmp/', include('nrmp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
