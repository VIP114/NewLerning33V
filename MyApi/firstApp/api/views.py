from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated

from rest_framework import viewsets
from .serializer import carspecsSerializer
from firstApp.models import carspecs

@api_view()
@permission_classes([AllowAny])
def firstFunction(request):
    print(request.query_params)
    print(request.query_params['num'])
    number = request.query_params['num']
    new_number = int(number) * 2
    return Response({'message':'we received your requiest','result': new_number})


class CarSpecsViewset(viewsets.ModelViewSet):
    serializer_class = carspecsSerializer
    
    def get_queryset(self):
        car_specs = carspecs.objects.all()
        return car_specs
    
    def retrieve(self,request,*args,**kwargs):
        params = kwargs
        print(params['pk'])
        params_list = params['pk'].split('-')
        cars =carspecs.objects.filter(car_brand=params_list[0],car_model=params_list[1])
        serializer =carspecsSerializer(cars,many = True)
        return Response(serializer.data)