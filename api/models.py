from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255)

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    @classmethod
    def get_by_id(cls, pk: int):
        return cls.objects.get(id=pk)

    def me_delete(self):
        self.delete()
