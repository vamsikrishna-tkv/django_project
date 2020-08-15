from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import ActivityPeriod,Users
from .serializers import ActivityPeriodSerializer,UsersSerializer
from rest_framework import viewsets


# class userList(APIView):
#     def get(self,request):
#         queryset = Users.objects.all()
#         ser=UsersSerializer(queryset,many=True)
#         return Response(ser.data)

class userList(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer



