import json

from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
from rest_framework.response import Response
from django.shortcuts import render
from django.views import View
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from api_v2.serializers import ArticleSerializer, ArticleModelsSerializer
from webapp.models import Article


# Create your views here.


class ArticleView(APIView):
    serializer_class = ArticleModelsSerializer

    def get(self, request, *args, **kwargs):
        if kwargs:
            article = get_object_or_404(Article, pk=self.kwargs.get("pk"))
            article_data = self.serializer_class(article,).data
            return Response(article_data)
        else:
            articles = Article.objects.all()
            articles_data = self.serializer_class(articles, many=True).data
            return Response(articles_data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def put(self, request, *args, pk, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        serializer = self.serializer_class(data=request.data, instance=article)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, pk, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        kwargs["pk"] = article.pk
        article.delete()
        return Response(kwargs["pk"])
