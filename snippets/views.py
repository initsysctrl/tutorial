from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def snippet_list(request):
    """
    列出所有的code snippets,或者创建一个新的snippet
    :param request:
    :return:
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JSONResponse(data=serializer.data)
    if request.method == 'post':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        else:
            return JSONResponse(serializer.errors, status=400)


# 一个视图函数标记为被免除CSRF保护的看法
@csrf_exempt
def snippet_detail(request, pk):
    """
    获取、更新、或者删除一个code snippet
    :param request:
    :param pk:
    :return:
    """
    try:
        snippet = Snippet.objects.get(pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JSONResponse(data=serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=200)
        return JSONResponse(serializer.errors, status=400)

    if request.method == 'DELETE':
        snippet.delete()
        return JSONResponse(status=204)
