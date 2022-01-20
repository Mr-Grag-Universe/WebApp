# import django.forms

from .models import Car
import django.forms as fm
from django.forms import ModelForm, TextInput, ModelMultipleChoiceField, ChoiceField, CharField, Form


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = [
            'mark',
            'year',
            'mileage',
            # 'rent',
            'box',
            'drive',
            'rul',
            'condition',
            'owners',
            'PTS',
            # 'tamozna',
            # 'barter',
            'V',
            'P',
            'toplivo',
            # 'garant',
        ]
        NAMES = [
            (1, "bmw"),
            (2, "honda"),
        ]

        '''
        widgets = {'name': TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Название вашей машины',
                }),
            # 'name': ModelMultipleChoiceField(choices=),
            # 'name': Positiv(("Название"), )

            'mark': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Марка',
            }),
        }
        '''

        widgets = {'mark': fm.TextInput(attrs={
                        'class': '#',
                        'placeholder': 'моя марка',
                    }),
                   'year': fm.TextInput(attrs={
                        'class': '#',
                        'placeholder': 'год',
                   }),
                   'mileage': fm.TextInput(),
                   # 'rent': fm.TextInput(),
                    'box': fm.CheckboxInput(),
                    'drive': fm.CheckboxInput(),
                   'rul': fm.CheckboxInput(),
                   'condition': fm.CheckboxInput(),
                   'owners': fm.TextInput(),
                   'PTS': fm.CheckboxInput(),
                   # 'tamozna': fm.CheckboxInput(),
                   # 'barter': fm.CheckboxInput(),
                   'V': fm.TextInput(),
                   'P': fm.TextInput(),
                    'toplivo': fm.CheckboxInput(),
                   # 'garant': fm.CheckboxInput(),
                   }
