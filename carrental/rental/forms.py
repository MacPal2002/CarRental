from django.forms import ModelForm, inlineformset_factory
from . import models
from django.contrib.auth.forms import UserCreationForm
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
        model = models.UserData
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'phone', 'identity_document_type', 'identity_document_no']
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
        exclude = ['id']
        widgets = {
            'country': forms.TextInput(attrs={'class': 'mb-3 form-control'}),
            'city': forms.TextInput(attrs={'class': 'mb-3 form-control'}),
            'post_code': forms.TextInput(attrs={'class': 'mb-3 form-control'}),
            'street': forms.TextInput(attrs={'class': 'mb-3 form-control'}),
            'building_no': forms.TextInput(attrs={'class': 'mb-3 form-control'}),
            'appartment_no': forms.TextInput(attrs={'class': 'mb-3 form-control'}),
        }


UserAddressFormSet = inlineformset_factory(
    parent_model=models.UserData,
    model= models.Address,
    form=AddressForm,
    extra=0,
    min_num=1,
    can_delete=False
)