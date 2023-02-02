from rest_framework import serializers
from api.serializer import PersonSerializer


class PersonNotFoundSerializer(serializers.Serializer):
    """
    Response person not found to swagger
    """

    detail = serializers.CharField(
        default="Person does not exist.", label="message error"
    )


class DeletedSerializer(serializers.Serializer):
    """
    Response successfully deleted to swagger
    """

    message = serializers.CharField(
        default="Successfully deleted.", label="success message"
    )


class PaginationPersonSerializer(serializers.Serializer):
    """
    Response pagination person to swagger
    """

    count = serializers.IntegerField()
    next = serializers.URLField(allow_null=True)
    previous = serializers.URLField(allow_null=True)
    results = PersonSerializer(many=True)
