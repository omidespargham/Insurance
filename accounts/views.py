from django.shortcuts import render
from django.views import View
from accounts.forms import RegisterForm
from accounts.models import User


class RegisterView(View):
    form_class = RegisterForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            User.objects.create()