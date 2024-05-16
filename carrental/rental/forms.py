from django.forms import ModelForm, inlineformset_factory
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django import forms


class RegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields["password1"].widget.attrs.update({
            "class": "mb-3 form-control",
        })
        self.fields["password2"].widget.attrs.update({
            "class": "mb-3 form-control",
        })
    class Meta:
        model = models.User
        # exclude = ['id']
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'phone', 'identity_document_type', 'identity_document_no']
        labels = {
            'phone': _('Numer telefonu'),
            'identity_document_type': _('Rodzaj dokumentu tożsamości'),
            'identity_document_no': _('Numer dokumentu tożsamości'),
        }
        help_texts = {'username': "",}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'mb-3 form-control'}),
            'email': forms.EmailInput(attrs={'class': 'mb-3 form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'mb-3 form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'mb-3 form-control'}),
            'phone': forms.TextInput(attrs={'class': 'mb-3 form-control'}),
            'identity_document_type': forms.Select(attrs={'class': 'mb-3 form-select'}),
            'identity_document_no': forms.TextInput(attrs={'class': 'mb-3 form-control'}),
        }


class AddressForm(ModelForm):
    class Meta:
        model = models.Address
        # fields = ['country', 'city', 'post_code', 'street', 'building_no', 'appartment_no']
        exclude = ['id']
        labels = {
            'country': _('Kraj'),
            'city': _('Miasto'),
            'post_code': _('Kod pocztowy'),
            'street': _('Ulica'),
            'building_no': _('Numer budynku'),
            'appartment_no': _('Numer mieszkania'),
        }
        widgets = {
            'country': forms.TextInput(attrs={'class': 'mb-3 form-control'}),
            'city': forms.TextInput(attrs={'class': 'mb-3 form-control'}),
            'post_code': forms.TextInput(attrs={'class': 'mb-3 form-control'}),
            'street': forms.TextInput(attrs={'class': 'mb-3 form-control'}),
            'building_no': forms.TextInput(attrs={'class': 'mb-3 form-control'}),
            'appartment_no': forms.TextInput(attrs={'class': 'mb-3 form-control'}),
        }


UserAddressFormSet = inlineformset_factory(
    parent_model=models.User,
    model= models.Address,
    form=AddressForm,
    extra=0,
    min_num=1,
    can_delete=False
)