from django.urls import path, include, re_path
from django.views.static import serve
from .views import home
from django.conf import settings
from django.conf.urls.static import static

static_urlpatterns = [
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^assets/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]

urlpatterns = [
    path('', home, name='dashboard'),
    path("", include(static_urlpatterns))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)
