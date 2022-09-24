from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from api_v3.views import ArticleViewSet, LogoutView

app_name = "api_v3"


router = DefaultRouter()
router.register("articles", ArticleViewSet)



urlpatterns = [
    path("", include(router.urls)),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('logout/', LogoutView, name='logout'),

]
