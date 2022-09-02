from django.shortcuts import render
from django.views import View


class HomeView(View):
    template_name = 'home/index.html'
    def get(self, request):
        text = "داشتن بیمه مسافرتی آن‌قدر مهم است که به شما توصیه می‌کنیم، اگر پول تهیه بیمه مسافرتی را ندارید، بهتر است سفر خارج از کشور نروید. اگر اهل سفر و ماجراجویی هستید، خرید بیمه مسافرتی دیگر برایتان یک خدمت لوکس و غیرضروری نیست."
        return render(request, self.template_name,{"text":text})


class ContactUsView(View):
    template_name = 'home/contact_us.html'

    def get(self, request):
        return render(request, self.template_name)


class AboutUsView(View):
    template_name = 'home/about_us.html'

    def get(self, request):
        return render(request, self.template_name)