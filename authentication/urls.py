from urllib.parse import urlparse
from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter
# app_name = 'pot'
# router = SimpleRouter(trailing_slash=True)

router = DefaultRouter()

router.register(r'users',views.UserViewSet,basename = 'users')
urlpatterns = router.urls

# urlpatterns = [
#     path('',views.HelloAuthView.as_view(),name = 'hello_auth'),
#     path('signup/',views.UserCreateView.as_view(),name = 'sign_up'),
#     path('users/',views.UserViewSet,name = 'Users'),
# ]
