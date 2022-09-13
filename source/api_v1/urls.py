from django.urls import path, include

from api_v1.views import echo_view, get_token_view, articles_view

app_name = "api_v1"

urls_articles =[
    path("", articles_view)
]


urlpatterns = [
    path("echo", echo_view),
    path("get-token", get_token_view),
    path("articles", include(urls_articles), name="article_view")
]