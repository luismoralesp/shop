from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

# Project urls
api_urlpatterns = [
    path('api/', include([
        path('', include('api.commons.urls')),
        path('orders/', include('api.orders.urls')),
    ])),
]

# Swagger settings - API Documentation
schema_view = get_schema_view(
    openapi.Info(
        title='Shop API',
        default_version='v0.0.1',
    ),
    permission_classes=(AllowAny,),
    patterns=api_urlpatterns
)

# General URLs
urlpatterns = api_urlpatterns + [
    url(r'^docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
]
