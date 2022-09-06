from django.shortcuts import render
from django.views import View


class HomeView(View):
    template_name = 'home/index.html'
    def get(self, request):
        return render(request, self.template_name)


class ContactUsView(View):
    template_name = 'home/contact_us.html'

    def get(self, request):
        return render(request, self.template_name)


class AboutUsView(View):
    template_name = 'home/about_us.html'

    def get(self, request):
        return render(request, self.template_name)