from django.db.models import Count
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api_v2.serializers import ArticleModelsSerializer
from webapp.models import Article


# Create your views here.
class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelsSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


    # ДЛЯ ВСЕГО КОММЕНТАРИЕВ
    @action(methods=['GET'], detail=False, url_path="comments_count")
    def get_comments_count(self, request, *args, **kwargs):
        return Response(self.queryset.aggregate(comments_count= Count("comments__id")))

    # для подсчета комментариев к одной статье
    @action(methods=['GET'], detail=True, url_path="comments_count")
    def get_comments_count(self, request, *args, **kwargs):
        print(kwargs)
        return Response({"count":self.get_object().comments.count()})


    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        return super().get_permissions()



def LogoutView(self, request, *args, **kwargs):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = self.request.user
        token = Token.objects.get(user=user)
        token.delete()
        return Response({"status": "ok"})




