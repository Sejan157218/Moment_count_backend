from django.urls import path
from .views.product import BestSellingListView


urlpatterns = [
    path('best-selling/', BestSellingListView.as_view(), name="best selling watch"),
]