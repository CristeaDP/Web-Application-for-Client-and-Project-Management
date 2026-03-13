from django import forms
from my_project.models import Shops, Persons, Memberships

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shops
        fields = ['name', 'address', 'nr_produse']


class PersonForm(forms.ModelForm):
    class Meta:
        model = Persons
        fields = ['first_name', 'last_name', 'email']


class MembershipForm(forms.ModelForm):
    class Meta:
        model = Memberships
        fields = ['type', 'shop', 'person']
