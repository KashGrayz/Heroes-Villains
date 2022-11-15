from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super
from .models import SuperType
@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        super_type_type = request.query_params.get('type') #By parameter
        print(super_type_type)
        queryset = Super.objects.all()
        
        if super_type_type:
            queryset = queryset.filter(super_type__type=super_type_type)
        
        
        serializer = SuperSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def supers_list(request):

    super_types = SuperType.objects.all()

    custom_response = {}

    for super_type in super_types:

        supers = Super.objects.filter(super_type_id=super_type.id)

        super_serializer = SuperSerializer(supers, many=True)

        custom_response[super_type.type] = {
             "Super": super_serializer.data,         
        }
    
    return Response(custom_response)

@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):
    supers = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(supers);
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SuperSerializer(supers, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        supers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)