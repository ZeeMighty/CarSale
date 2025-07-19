from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Car
from .serializers import CarSerializer


class CarAPIView(APIView):
    def get(self, request:str | None) -> Response:
        cars = Car.objects.all().values()
        return Response({"Cars": list(cars)})
    
    def post(self, request:str | None) -> Response:
        post_new = Car.objects.create(
            title=request.data["title"],
            price=request.data["price"],
        )
        return Response({"post": model_to_dict(post_new)})
# class CarAPIView(generics.ListAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer