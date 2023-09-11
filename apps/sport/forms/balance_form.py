from django import forms
from sport.models import UserProfile

class BalanceRechargeForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['balance']