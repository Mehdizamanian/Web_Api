"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include 
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken import views

from drf_spectacular.views import SpectacularAPIView,SpectacularRedocView,SpectacularSwaggerView # schema  python manage.py spectacular --file schema.yml


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apis.urls')),
    path('blog/', include('blog.urls')),

    # path("api-auth/login/login/login/", include("rest_framework.urls")), # rest_framework login url
    # path('api-token-auth/', views.obtain_auth_token),

    path("api-auth/", include("rest_framework.urls")), #login logout in by restframework....
    path("api/v1/dj-rest-auth/", include("dj_rest_auth.urls")), #login logout ... in by dj-rest-auth
    path("api/v1/dj-rest-auth/registration/",include("dj_rest_auth.registration.urls")),#registration by dj-rest-auth and # django-allauth~=0.48.0 then migrate 

    path("api/schema/", SpectacularAPIView.as_view(), name="schema"), # schema.yml downloder for machine 
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc",),#schema authentication view
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),#schema endpoints view
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)