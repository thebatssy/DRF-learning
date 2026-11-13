from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

# create router object
router = DefaultRouter() 

# register viewset with router
router.register('studentapi', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
