from django import forms
from . import models


class PackForm(forms.ModelForm):

    class Meta:
        model = models.Order
        fields = ['email', 'discord', 'skype', 'name']
