# third-party
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.pagination import PageNumberPagination

# Django
from django.http import Http404
from django.db import transaction

# local Django
from apps.category.models import Category
from apps.collection.models import Collection
from apps.tag.models import Tag
from apps.collection.serializers import CollectionSerializer, CollectionHeavySerializer, CollectionRelationSerializer

class VCollectionList(APIView, PageNumberPagination):
  permission_classes = (IsAdminUser,)
  serializer = CollectionSerializer

  def get(self, request, format=None):
    # consulta
    listr = Collection.objects.all().order_by('id')
    # respuesta
    results = self.paginate_queryset(listr, request)
    serializer = CollectionHeavySerializer(results, many=True)
    return self.get_paginated_response(serializer.data)

  def post(self, request, format=None):
    # return Response(request.data, status=status.HTTP_201_CREATED)
    response = self.serializer(data=request.data)
    if response.is_valid():
      result = response.save()
      res = CollectionHeavySerializer(result)
      return Response(res.data, status=status.HTTP_201_CREATED)
    else:
      return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)


class VCollectionDetail(APIView):
  permission_classes = (IsAdminUser,)
  serializer = CollectionHeavySerializer

  def get_object(self, pk):
    try:
      return Collection.objects.get(pk=pk)
    except Collection.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    response = self.serializer(self.get_object(pk))
    return Response(response.data, status=status.HTTP_200_OK)

  @transaction.atomic
  def put(self, request, pk, format=None):
    response = CollectionSerializer(self.get_object(pk), data=request.data)
    if response.is_valid():
      result = response.save()
      if type(result) == str:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
      else:
        res = self.serializer(result)
        return Response(res.data, status=status.HTTP_201_CREATED)
    else:
      return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    collection = self.get_object(pk)
    collection.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class VCollectionRelation(APIView):
  """
  edicion relaciones muchos a muchos
  """
  permission_classes = (IsAdminUser,)
  serializer = CollectionRelationSerializer

  def get_object(self, pk):
    try:
      return Collection.objects.get(pk=pk)
    except Collection.DoesNotExist:
      raise Http404

  @transaction.atomic
  def put(self, request, pk, format=None):
    response = self.serializer(data=request.data)
    if response.is_valid():
      result = response.save()
      res = CollectionHeavySerializer(
        self.get_object(pk)
      )
      return Response(res.data, status=status.HTTP_201_CREATED)
    else:
      return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)

  @transaction.atomic
  def delete(self, request, pk, format=None):
    response = self.serializer(data=request.data)
    if response.is_valid():

      collection = self.get_object(pk)

      for category_id in response.validated_data['categories']:
        category = Category.objects.get(id= category_id)
        collection.categories.remove(category)

      for tag_id in response.validated_data['tags']:
        tag = Tag.objects.get(id= tag_id)
        collection.tags.remove(tag)

      res = CollectionHeavySerializer(
        self.get_object(pk)
      )
      return Response(res.data, status=status.HTTP_201_CREATED)
    else:
      return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)