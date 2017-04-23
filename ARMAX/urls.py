from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from Posts.views import home, about, contact, NewsView, NewsDetailView
from thebutton.views import TheButton

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', home.as_view(), name='home'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^about/', about.as_view(), name='about'),
    url(r'^contact/', contact, name='contact'),
    url(r'news/', NewsView.as_view(), name='news'),
    url(r'^(?P<pk>[0-9]+)/$', NewsDetailView.as_view(), name='detail'),
    url(r'^button/$', TheButton.as_view(), name='button'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)