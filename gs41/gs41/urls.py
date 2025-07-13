
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter


#creating a router and resgistering the viewsets
router = DefaultRouter()

router.register(r'singers', views.SingerViewSet)
router.register(r'songs', views.SongViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
