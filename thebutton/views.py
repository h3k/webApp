from django.shortcuts import render
from django.views.generic import View


class TheButton(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'thebutton/button.html', context)