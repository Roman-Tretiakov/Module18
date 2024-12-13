from django.urls import path
from task3.views import Main, Shop, Basket

app_name = 'task3'

urlpatterns = [
    path('platform/', Main.as_view(), name='platform'),
    path('shop/', Shop.as_view(), name='shop'),
    path('basket/', Basket.as_view(), name='basket'),
]
