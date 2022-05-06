from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from api.serializers import *

from rest_framework.views import APIView

class PostList(APIView):
    def get(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201, safe=False)
        return JsonResponse(serializer.errors, status=400, safe=False)

