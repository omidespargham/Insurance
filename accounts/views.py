from random import randint
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login, authenticate
from django.views import View
from django.contrib import messages
from accounts.forms import UserLogInForm, UserRegisterForm, UserProfileEditForm, UserRegisterVerifyForm
from accounts.models import RGScode
from .models import User
from API_SMS import sms
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


class UserRegisterView(View):
    template_name = "accounts/register.html"
    form_class = UserRegisterForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.success(
                request, f"برای ثبت حساب جدید ابتدا از حساب خود خارج شوید", "warning")
            return redirect("home:home")
        request.next = request.GET.get("next")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        context = {
            "form": self.form_class
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cl = form.cleaned_data
            self.request.session["user_info"] = {
                "phone_number": cl["phone_number"],
                "email": cl["email"],
                "full_name": cl["full_name"],
                "password": cl["password"]
            }
            random_code = randint(0, 9999)
            RGScode.objects.create(
                phone_number=cl["phone_number"], code=random_code)
            sms(cl["phone_number"], random_code)
            return redirect("accounts:user_register_verify")
        return render(request, self.template_name, {"form": form})



class UserLogInView(View):
    template_name = "accounts/login.html"
    form_class = UserLogInForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.success(
                request, f"برای ورود با حسابی دیگر ابتدا از حساب خود خارج شوید", "warning")
            return redirect("home:home")
        request.next = request.GET.get("next")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        context = {
            "form": self.form_class
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cl = form.cleaned_data
            user = authenticate(
                username=cl["phone_or_email"], password=cl["password"])
            if user:
                login(request, user)
                messages.success(request, "خوش آمدید", "success")
                if request.next:
                    return redirect(request.next)
                return redirect("home:home")
            messages.error(request, "اطلاعات مطابقت ندارد !", "danger")

        return render(request, self.template_name, {"form": form})


class UserLogOutView(LoginRequiredMixin, View):

    def get(self, request):
        logout(request)
        return redirect("home:home")


class UserRegisterVerifyView(View):
    form_class = UserRegisterVerifyForm
    template_name = "accounts/verify_code.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.success(
                request, "نمیتوانید وارد این صفحه شوید !", "success")
            return redirect("home:home")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        context = {
            "form": self.form_class()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            code = form.cleaned_data["code"]
            try:
                user_info = request.session["user_info"]
                code = RGScode.objects.get(
                    phone_number=user_info["phone_number"], code=code)
                User.objects.create_user(phone_number=user_info["phone_number"], email=user_info["email"],
                                         full_name=user_info["full_name"], password=user_info["password"])
                code.delete()
                authed_user = authenticate(
                    username=user_info["phone_number"], password=user_info["password"])
                login(request, authed_user)
                messages.success(
                    request, f"شما ثبت نام کردید", "success")
                return redirect("home:home")
            except RGScode.DoesNotExist:
                return render(request, self.template_name, {"form": form, "is_not_true_code": True})
        return render(request, self.template_name, {"form": form})


class UserProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "accounts/user_profile.html", {"user": request.user})


class UserProfileEditView(LoginRequiredMixin, View):
    form_class = UserProfileEditForm
    template_name = "accounts/user_profile_edit.html"

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class(instance=request.user)})

    def post(self, request):
        form = self.form_class(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.profile.img = request.FILES["img"]
            user.profile.save()
            user.save()
            return redirect("accounts:user_profile")
        return render(request, self.template_name, {"form": form})


class UserPasswordResetView(auth_views.PasswordResetView):
    email_template_name = 'accounts/password_reset_email.html'
    success_url = reverse_lazy('accounts:password_reset_done')
    template_name = 'accounts/password_reset_form.html'


class UserPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')


class UserPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'
