from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'text', 'data']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи',
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи',
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Статья',
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации',
            })
        }
