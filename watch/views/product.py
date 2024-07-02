from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from ..models import BestSelling
from ..serializers import BestSellingSerializer


class BestSellingListView(ListAPIView):
    queryset = BestSelling.objects.all()
    serializer_class = BestSellingSerializer