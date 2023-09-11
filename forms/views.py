from django.urls import reverse_lazy
from django.views.generic import FormView

from forms.forms import CareerForm
from forms.models import CareerFormModel


class CareerFormView(FormView):
    template_name = "forms/career_form.html"
    model = CareerFormModel
    form_class = CareerForm
    success_url = reverse_lazy('forms.career_form')

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        career_form = CareerFormModel(**cleaned_data)
        career_form.user = self.request.user
        career_form.save()

        return super().form_valid(form)