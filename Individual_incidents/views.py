from django.shortcuts import render, redirect
from django.views import View

from Individual_incidents.forms import IndividualIncidentsForm
from Individual_incidents.models import IndividualIncidentsModel


class Individual_Incidents(View):
    template_name = 'Individual_incidents/Individual_incidents.html'
    form_class = IndividualIncidentsForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            IndividualIncidentsModel.objects.create(number_people=form.cleaned_data['number_people'],
                                                    limit_time=form.cleaned_data['limit_time'],
                                                    job_category=form.cleaned_data['job_category'])

            return redirect('home:home')
        return render(request, self.template_name, {'form': self.form_class})
