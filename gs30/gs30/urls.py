from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


#creating router object
router = DefaultRouter()

#registering the viewset with the router
router.register('studentapi', views.StudentModelViewSet,
                basename = 'student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), # include the router's URLs
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),
]