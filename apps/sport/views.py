# Django
from django.shortcuts import render , redirect
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.db.models.query import QuerySet
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms.bet_form import BetForm
from .forms.regiser_form import RegistrationForm
from .forms.login_form import LoginForm
from .forms.balance_form import BalanceRechargeForm
from .models import UserProfile , Bet
from django.contrib.auth.decorators import login_required
# Local
from .models import Game_start


def index(request: HttpRequest):
    template_name: str = 'index.html'
    quriset : QuerySet[Game_start] =Game_start.objects.all()
    return render(
        request=request,
        template_name=template_name,
        context={
            'game': quriset
        }
    )

@login_required
def create_bet(request):
    try:
        user_account = UserProfile.objects.get(user=request.user) 
       
    except UserProfile.DoesNotExist:
        user_account = UserProfile(user=request.user)
        user_account.save()
    bets = Bet.objects.filter(user=user_account) 

    if request.method == 'POST':
        form = BetForm(request.POST)
        if form.is_valid():
            bet = form.save(commit=False)
            bet.user = user_account
            bet.save()
            return redirect('/sport/stavka')  
    else:
        form = BetForm()
    
    return render(request, 'stavka.html', {'form': form, 'user_account': user_account , 'bets':bets })


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('stavka') 
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('stavka/') 
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def recharge_balance(request):
    user_profile = request.user.user_account  # Получение профиля текущего пользователя

    if request.method == 'POST':
        form = BalanceRechargeForm(request.POST, instance=user_profile)
        if form.is_valid():
            new_balance = form.cleaned_data['balance'] 
            user_profile.balance += new_balance  
            user_profile.save() 
            return redirect('stavka')  
    else:
        form = BalanceRechargeForm(instance=user_profile)

    return render(request, 'recharge_balance.html', {'form': form})