from django.urls import path
from task4.views import Main, Shop, Basket

app_name = 'task4'

urlpatterns = [
    path('', Main.as_view(), name='platform'),
    path('shop/', Shop.as_view(), name='shop'),
    path('basket/', Basket.as_view(), name='basket'),
]
