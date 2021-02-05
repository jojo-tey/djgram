from django.shortcuts import render
from django.views.generic.base import TemplateView
# TemplateView= 템플릿이 주어지면 해당 템플릿으로 렌더링
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class HomeView(TemplateView):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(HomeView, self).dispatch(request, *args, **kwargs)

    template_name = 'home.html'
