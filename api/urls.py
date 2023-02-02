from django.urls import path
from .views import PersonWithoutIdView, PersonWithIdView

urlpatterns = [
    path("persons/", PersonWithoutIdView.as_view(), name="PersonWithoutIdView"),
    path("persons/<int:pk>/", PersonWithIdView.as_view(), name="PersonWithIdView"),
]
