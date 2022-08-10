from django.shortcuts import render
from django.views import View

from car.forms import ThirdPartyForm
from home.forms import BimeUserForm


class RegisterView(View):
    form_class = ThirdPartyForm
    template_name = 'car/ThirdPartyRequest.html'

    def get(self, request):
        return render(request, 'car/ThirdPartyRequest.html', {'form': self.form_class, "form2": BimeUserForm})
