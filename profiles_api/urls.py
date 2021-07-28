from django.urls import path, include 
from profiles_api import views 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

#router.register('name', name_of_class)
# we have a queryset so the drf will determine the basename hisself from there.
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.UserLoginApiView.as_view()),
]