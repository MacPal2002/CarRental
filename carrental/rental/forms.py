from django.forms import ModelForm, inlineformset_factory
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _


class RegistrationForm(UserCreationForm):
    class Meta:
        model = models.User
        # exclude = ['id']
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'phone']
        labels = {
            'phone': _('Numer trlefonu'),
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

UserAddressFormSet = inlineformset_factory(
    parent_model=models.User,
    model= models.Address,
    form=AddressForm,
    extra=0,
    min_num=1,
    can_delete=False
)