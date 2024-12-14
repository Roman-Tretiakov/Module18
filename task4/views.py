from django.views.generic import TemplateView


class BaseView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_page'] = 'Главная страница'
        context['main'] = 'Главная'
        context['shop'] = 'Магазин'
        context['basket'] = 'Корзина'
        context['games'] = 'Игры'
        context['game_list'] = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
        context['buy_button'] = 'Купить'
        context['back_button'] = 'Вернуться обратно'
        context['basket_message'] = 'Извините, ваша корзина пуста!'
        return context


class Main(BaseView):
    template_name = 'fourth_task/main_page_template.html'


class Shop(BaseView):
    template_name = 'fourth_task/shop_template.html'


class Basket(BaseView):
    template_name = 'fourth_task/basket_template.html'
