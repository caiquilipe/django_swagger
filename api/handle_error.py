from rest_framework.exceptions import APIException
from rest_framework import status
from django.utils.translation import gettext_lazy as _


class PersonNotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _("Person does not exist.")
    default_code = "not_found"
