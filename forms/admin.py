from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportMixin

from forms.models import CareerFormModel


class CareerFormResource(resources.ModelResource):
    class Meta:
        model = CareerFormModel
        widgets = {
            'timestamp': {'format': '%Y/%m/%d %H:%M:%S'},
        }
        exclude = ('user', )

class CareerFormAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = CareerFormResource

admin.site.register(CareerFormModel, CareerFormAdmin)
