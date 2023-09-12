from django.urls import reverse_lazy
from django.views.generic import FormView

from forms.forms import CareerForm
from forms.models import CareerFormModel


class CareerFormView(FormView):
    template_name = "forms/career_form.html"
    model = CareerFormModel
    form_class = CareerForm
    success_url = reverse_lazy('forms.career_form')

    def get_initial(self):
        form_value = super().get_initial()
        user = self.request.user
        if user.id:
            current_career_form = CareerFormModel.objects.filter(email=user.email).order_by('-timestamp').first()
            if current_career_form:
                form_value.update(vars(current_career_form))

        return form_value

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        career_form = CareerFormModel(**cleaned_data)
        career_form.user = self.request.user
        career_form.save()

        return super().form_valid(form)
