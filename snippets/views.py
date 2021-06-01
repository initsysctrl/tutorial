from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404


# class JSONResponse(HttpResponse):
#     """
#     An HttpResponse that renders its content into JSON.
#     """
#
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)
#
#
# @api_view(['GET', 'POST'])
# def snippet_list(request):
#     """
#     列出所有的code snippets,或者创建一个新的snippet
#     :param request:
#     :return:
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return JSONResponse(data=serializer.data)
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return JSONResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# # 一个视图函数标记为被免除CSRF保护的看法
# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk):
#     """
#     获取、更新、或者删除一个code snippet
#     :param request:
#     :param pk:
#     :return:
#     """
#     try:
#         snippet = Snippet.objects.get(pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JSONResponse(data=serializer.data)
#
#     if request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data, status=status.HTTP_200_OK)
#         return JSONResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == 'DELETE':
#         snippet.delete()
#         return JSONResponse(status=status.HTTP_204_NO_CONTENT)


class SnippetList(APIView):
    def get(self, request):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)
        pass

    def post(self, request):
        serializer = SnippetSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk)
        except Snippet.DoesNotExist:
            return Http404

    def get(self, request, pk=1):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        print(serializer.data)
        # status.HTTP_302_FOUND
        return Response(serializer.data)

    def put(self, request, pk=1):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=1):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Test(APIView):
    def get(self, request):
        try:
            snippet = Snippet.objects.get(pk=1)
            serializer = SnippetSerializer(snippet)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Snippet.DoesNotExist:
            return Http404
