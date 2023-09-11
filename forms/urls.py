from django.urls import path

from forms.views import CareerFormView

name = "forms"

urlpatterns = [
    path("career_form.html", CareerFormView.as_view(), name="forms.career_form"),
]