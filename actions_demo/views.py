from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Memo
# Create your views here.

class MemoAPIView(APIView):
    def post(self, request):
        print(request.data)
        
        memo = Memo.objects.create(title = request.data["title"], user= request.data["user"])
        memo.save()
        
        return Response({"message": "success"})
    