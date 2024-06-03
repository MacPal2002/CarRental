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

class OrderForm(ModelForm):

    class Meta:
        model = models.Order
        exclude = ['id', 'payment_status', 'declared_order_duration' ]
        widgets = {
            'customer': forms.Select(attrs={'class': 'mb-3 form-control'}),
            'car': forms.Select(attrs={'class': 'mb-3 form-control', 'style': "pointer-events: none;"}),
            'declared_order_duration': forms.TextInput(attrs={'class': 'mb-3 form-control'}),
            'pickup_date': forms.DateInput(attrs={'class': 'mb-3 form-control', 'type': 'date'}),
            'return_date': forms.DateInput(attrs={'class': 'mb-3 form-control', 'type': 'date'}),
            'deposit': forms.TextInput(attrs={'class': 'mb-3 form-control', 'readonly': True}),
            'payment_method': forms.Select(attrs={'class': 'mb-3 form-control'}),
            'order_value': forms.TextInput(attrs={'class': 'mb-3 form-control', }),
        }