from rest_framework import serializers
from .models import BestSelling


class BestSellingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestSelling
        fields = "__all__"