"""
URL configuration for pro1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from app2.views import SchoolViewSet,Student1ViewSet,FilterViewSet

router =DefaultRouter()
router.register('school',SchoolViewSet)
router.register('stu2',Student1ViewSet)

router1 = DefaultRouter()
router1.register('filter',FilterViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('a1/',include('app1.urls')),
    path('a2/',include(router.urls)),
    path('a3/',include(router1.urls))
]
