from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .core import urls as core_urls
from .product import urls as product_urls
from .user import urls as user_urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(core_urls, namespace="core")),
    path("product/", include(product_urls, namespace="product")),
    path("user/", include(user_urls, namespace="user")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
