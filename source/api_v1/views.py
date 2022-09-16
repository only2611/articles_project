from decimal import Decimal

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.shortcuts import render
from datetime import datetime
import json

from django.views import View
from django.views.decorators.csrf import ensure_csrf_cookie

from webapp.models import Article


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(['GET'])


# Create your views here.
def echo_view(request):
    print(request.body)
    body = json.loads(request.body)
    print(body.get("test"))
    response_data = {
        "method": request.method,
        "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "decimal": Decimal("1.2345454"),
        "body": body
    }
    # response_json_data = json.dumps(response_data)
    # print(response_json_data)
    # response["Content-Type"] = "application/json"
    response = JsonResponse(response_data)
    return response


def articles_view(request):






    print(request)
    if request.method == "GET":
        tag_id = request.GET.get("tag_id")
        if tag_id:
            articles = Article.objects.filter(tags__id=tag_id).values("title", "content")
        else:
            articles = Article.objects.values("title", "content")
        return JsonResponse(list(articles), safe=False)
    elif request.method == "POST":
        if request.body:
            body = json.loads(request.body)
            if len(body.get("title")) < 5:
                return JsonResponse({"message": "Error"}, status=400)
            # article = Article.objects.create(**body)
            return JsonResponse({"id": 1}, status=201)
        return JsonResponse({"message": "error"}, status=400)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


class LikesView(LoginRequiredMixin, View):
    def get(self, request, *args, pk, **kwargs):
        article = Article.objects.get(pk=pk)
        user = self.request.user
        if user in article.likes.all():
            article.likes.remove(user)
        else:
            article.likes.add(user)

        return JsonResponse({"count": article.likes.count()})
