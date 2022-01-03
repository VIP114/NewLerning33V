from rest_framework import serializers
from firstApp.models import carspecs

class carspecsSerializer(serializers.ModelSerializer):
    class Meta:
        model = carspecs
        fields =['id', 'car_brand', 'car_model', 'production_year',
                  'car_body', 'engine_type']
        depth = 1