from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#swagger url
schema_view = get_schema_view(
    openapi.Info(
        title="Timing-app API",
        default_version='v1',
        description="Simple Clockify app api",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('authentication.urls')),
    path('api/', include('timer.urls')),
    
    
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]

