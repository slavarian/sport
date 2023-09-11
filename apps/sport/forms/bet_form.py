from django import forms
from sport.models import Bet 

class BetForm(forms.ModelForm):
    class Meta:
        model = Bet
        fields = ['game', 'team', 'amount']
