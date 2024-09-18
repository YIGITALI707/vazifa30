from rest_framework.serializers import ModelSerializer

from .models import Cars


class CarsSerializers(ModelSerializer):
    class Meta:
        model=Cars
        fields='__all__'