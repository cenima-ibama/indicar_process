from django.conf.urls import include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    #url(r'^$', TemplateView.as_view(template_name='base.html')),

    # Examples:
    # url(r'^$', 'indicarprocess.views.home', name='home'),
    url(r'^', include('imagery.urls')),
    url(r'^catalogo/', include('catalogo.urls')),
    url(r'^api/', include('tmsapi.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', admin.site.urls),
]

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls))]
