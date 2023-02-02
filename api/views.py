from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from drf_yasg.openapi import Parameter, TYPE_STRING
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from api.handle_error import PersonNotFound
from .utils import Paginator
from .models import Person
from .serializer import PersonSerializer
from .swagger.handle_responses import (
    DeletedSerializer,
    PaginationPersonSerializer,
    PersonNotFoundSerializer,
)


class PersonWithoutIdView(APIView):
    pagination_class = Paginator

    @swagger_auto_schema(
        request_body=PersonSerializer,
        responses={201: PersonSerializer},
    )
    def post(self, request):
        """
        Create person endpoint
        """
        serializer = PersonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)

    @swagger_auto_schema(
        responses={200: PaginationPersonSerializer},
        manual_parameters=[
            Parameter(name="page", in_=openapi.IN_QUERY, type=TYPE_STRING),
            Parameter(name="page_size", in_=openapi.IN_QUERY, type=TYPE_STRING),
        ],
    )
    def get(self, request):
        """
        Get all persons endpoint
        """
        paginator = self.pagination_class()
        data = paginator.paginate_queryset(
            queryset=PersonSerializer(Person.get_all(), many=True).data,
            request=request,
        )
        return paginator.get_paginated_response(data)


class PersonWithIdView(APIView):
    @swagger_auto_schema(
        request_body=PersonSerializer,
        responses={200: PersonSerializer, 404: PersonNotFoundSerializer},
    )
    def patch(self, request, pk):
        """
        Partial update person by id endpoint
        """
        try:
            person = Person.get_by_id(pk=pk)
            serializer = PersonSerializer(instance=person, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except Person.DoesNotExist:
            raise PersonNotFound

    @swagger_auto_schema(
        responses={202: PersonSerializer, 404: PersonNotFoundSerializer},
    )
    def get(self, request, pk):
        """
        Get person by id endpoint
        """
        try:
            person = Person.get_by_id(pk=pk)
            serializer = PersonSerializer(instance=person)
            return Response(status=status.HTTP_202_ACCEPTED, data=serializer.data)
        except Person.DoesNotExist:
            raise PersonNotFound

    @swagger_auto_schema(
        responses={200: DeletedSerializer, 404: PersonNotFoundSerializer},
    )
    def delete(self, request, pk):
        """
        Delete person by id endpoint
        """
        try:
            person = Person.get_by_id(pk=pk)
            person.me_delete()
            return Response(
                status=status.HTTP_200_OK,
                data=DeletedSerializer({"message": "Successfully deleted."}).data,
            )
        except Person.DoesNotExist:
            raise PersonNotFound
