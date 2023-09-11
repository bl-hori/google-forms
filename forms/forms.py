from django import forms

from forms.models import CareerFormModel


class CareerForm(forms.ModelForm):
    class Meta:
        model = CareerFormModel
        fields = [
            'question_01',
            'question_02',
            'question_03',
            'question_04',
            'question_05',
            'question_06',
            'question_07',
            'question_08',
            'question_09',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

