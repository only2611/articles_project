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


# def form_valid(self, form):
#     article = get_object_or_404(Article, pk=self.kwargs.get("pk"))
#     user = self.request.user
#     form.instance.article = article
#     form.instance.author = user
#     return super().form_valid(form)
#
# def get_success_url(self):
#     return reverse("webapp:article_view", kwargs={"pk": self.object.article.pk})


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
        article.delete()
        return Response(article.pk)