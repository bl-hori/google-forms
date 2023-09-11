from django.contrib import admin

from forms.models import CareerFormModel


class CareerFormAdmin(admin.ModelAdmin):
    pass

admin.site.register(CareerFormModel, CareerFormAdmin)
