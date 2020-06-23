from django.contrib import admin
from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("helloViewset", views.HelloViewSet, base_name = "helloViewset")
router.register("profile", views.UserProfileViewSet)
router.register("feed", views.UserProfileFeedViewSet)
urlpatterns = [
    path("an_apiview/", views.HelloApiView.as_view()), #The HelloApiView is a rest_framework class that's why you need the .as_view
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
