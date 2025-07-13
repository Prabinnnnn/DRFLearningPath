from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter


#creating router object
router = DefaultRouter()

#registering the viewset with the router
router.register('studentapi', views.StudentModelViewSet,
                basename = 'student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), # include the router's URLs
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]