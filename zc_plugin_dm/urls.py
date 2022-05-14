"""zc_plugin_dm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Zuri Chat Direct Messaging Plugin API",
        default_version="v1",
        description="Contains all the available endpoints for the Zuri Chat DM plugin as compiled By Team Orpheus HNGi8",
        terms_of_service="https://dm.zuri.chat/dm/policies/terms/",
        contact=openapi.Contact(email="dm_plugin@zuri.chat"),
    ),
    url="https://dm.zuri.chat",
    # url="http://127.0.0.1:8000",
    public=True,
    permission_classes=(permissions.AllowAny,),
    # validators=["ssv"],
)


# app urls
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("backend.urls")),
    path("dm", include("backend.urls")),
]


# documentation urls
urlpatterns += [
    url(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    url(
        r"^docs/v1/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    url(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]
