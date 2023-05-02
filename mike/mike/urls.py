from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    # path("auth/", include("users.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    path("", include("main.urls", namespace="main")),
    # path("", include("about.urls", namespace="about")),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    )
