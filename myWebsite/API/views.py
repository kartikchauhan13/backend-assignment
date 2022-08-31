from django.shortcuts import render
from .models import User
from .serializers import DataSer
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter
from .pagination import Pagination



class UserList(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):


    serializer_class = DataSer
    queryset = User.objects.all()
    pagination_class=Pagination
    filter_backends = [OrderingFilter , SearchFilter]
    search_fields=['^first_name' ,'^last_name']



    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
       return self.create(request, *args, **kwargs)

class UserDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView):

    serializer_class = DataSer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)





