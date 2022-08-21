from django.shortcuts import render, redirect
from django.views import View

from car.forms import ThirdPartyForm
# from home.forms import BimeUserForm
# from home.models import BimeUser
from car.models import ThirdPartyModel
from django.contrib.auth.mixins import LoginRequiredMixin

class RegisterView(LoginRequiredMixin,View):
    form_class = ThirdPartyForm
    template_name = 'car/ThirdPartyRegister.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        # form_user = BimeUserForm(request.POST)
        if form.is_valid() :
            cl = form.cleaned_data
            # cl_user = form_user.cleaned_data
            # user = BimeUser.objects.create(first_name=cl_user['first_name'], last_name=cl_user["last_name"],
            #                                email=cl_user["email"])
            ThirdPartyModel.objects.create(user=request.user, vehicle_type=cl["vehicle_type"],
                                           car_type=cl["car_type"], used=cl["used"],
                                           year_of_manufacture=cl["year_of_manufacture"],
                                           third_discount=cl["third_discount"],
                                           accident_discounts=cl["accident_discounts"],
                                           number_of_accidents=cl["number_of_accidents"],
                                           number_of_incidents=cl["number_of_incidents"],
                                           expiration_date=cl["expiration_date"],
                                           face_image=cl['face_image'],
                                           back_image=cl['back_image'],
                                           image_insurance_policy=cl['image_insurance_policy'],
                                           )

            return redirect("home:home")
        return render(request, self.template_name, {"form": form})
