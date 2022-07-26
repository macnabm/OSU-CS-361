from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Address
from .serializers import AddressSerializer


class AddressView(APIView):
    def get(self, request):
        contents = []
        for address in Address.objects.all():
            contents.append(
                {
                    "first_name"         : address.occupant.first_name,
			        "last_name"          : address.occupant.last_name,
			        "street_address"     : address.street_address,
			        "zipCode"            : address.zipCode,
			        "state"              : address.state,
			        "city"               : address.city,
                }
            )
        finalJson = {"Addresses" : contents}
        return Response(finalJson, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.data)
        data = request.data['Address']
        serializer = AddressSerializer(data=data)
        if serializer.is_valid():
            print("woo hoo valid")
            serializer.save()
            return Response("address added!!",status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response("address not added...", status=status.HTTP_406_NOT_ACCEPTABLE)