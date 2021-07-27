from django.urls import path, include 
from profiles_api import views 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

#router.register('name', name_of_class)
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
# we have a queryset so the drf will determine the basename hisself from there.
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
    path('', include(router.urls)),
    path('login/', views.UserLoginApiView.as_view()),
]