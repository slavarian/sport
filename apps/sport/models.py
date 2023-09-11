from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_account')
    
    balance = models.IntegerField(
        verbose_name='баланс пользователя',
        default=0,
        
    )
    bet_counter = models.IntegerField(
        verbose_name='сделано ставок',
        default=0,
        null=True
    )
    bet_wins = models.IntegerField(
        verbose_name='победных ставок',
        default=0,
        null=True
    )
    
    class Meta:
        ordering = ('user',)
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self) -> str:
        return self.user.username




class Сountry(models.Model):
    title = models.CharField(
        verbose_name='название комманды(игрового клуба)',
        max_length=100
    )
    class Meta:
        ordering = ('title',)
        verbose_name = 'страна'
        verbose_name_plural = 'страны'

    def __str__(self) -> str:
        return self.title

class Sport(models.Model):
    title = models.CharField(
        verbose_name='название спорта',
        max_length=100
    )
    class Meta:
        ordering = ('title',)
        verbose_name = 'вид спорта'
        verbose_name_plural = 'виды спорта'

    def __str__(self) -> str:
        return self.title

class Sportsman(models.Model):
    name = models.CharField(
        verbose_name='Имя спортсмена',
        max_length=100
    )
    surname = models.CharField(
        verbose_name='Фамилия спортсмена спортсмена',
        max_length=100
    )
    sport_type = models.ForeignKey(
        verbose_name='вид спорта',
        to=Sport,
        on_delete=models.CASCADE
    )
    сountry = models.ForeignKey(
        verbose_name='страна спортсмена',
        to=Сountry,
        on_delete=models.CASCADE
    )
    games_count = models.IntegerField(
        verbose_name='кол-во игр',
        default=0
    )
    class Meta:
        ordering = ('name',)
        verbose_name = 'спортсмен'
        verbose_name_plural = 'спортсмены'

    def __str__(self) -> str:
        return self.name

    
class Command(models.Model):
    title = models.CharField(
        verbose_name='название комманды(игрового клуба)',
        max_length=100
    )
    sport_type = models.ForeignKey(
        verbose_name='вид спорта',
        to=Sport,
        on_delete=models.CASCADE
    )
    game_structure =models.ManyToManyField(
        verbose_name='состав команды',
        to=Sportsman
     
    )
    сountry = models.ForeignKey(
        verbose_name='страна',
        to=Сountry,
        on_delete=models.CASCADE
    )
    class Meta:
        ordering = ('title',)
        verbose_name = 'комманда'
        verbose_name_plural = 'комманды'

    def __str__(self) -> str:
        return f"{self.title} || {self.сountry}"

class Status_game(models.Model):
    title = models.CharField(
        verbose_name='статус игры',
        max_length=100
    )
    class Meta:
        ordering = ('title',)
        verbose_name = 'статус игры'
        verbose_name_plural = 'статус игр'

    def __str__(self) -> str:
        return self.title



class Game_start(models.Model):
    one_command = models.ForeignKey(
        verbose_name='комманда 1',
        to=Command,
        related_name='game_starts_one',
        on_delete=models.CASCADE
    )
    two_command = models.ForeignKey(
        verbose_name='комманда 2',
        to=Command,
        related_name='game_starts_two',
        on_delete=models.CASCADE
    )

    cof1 = models.DecimalField(
        verbose_name='коф.победы 1 комманды',
        max_digits=2, 
        decimal_places=0,
        default=0
    )

    cof2 = models.DecimalField(
        verbose_name='коф.победы 2 комманды',
        max_digits=2, 
        decimal_places=0,
        default=0
    )

    time_start = models.DateTimeField(
        verbose_name='время начала матча'
    )
    status_game = models.ForeignKey(
        verbose_name='Статус игры',
        to = Status_game,
        on_delete=models.CASCADE
    )
    winners =  models.ForeignKey(
        verbose_name='победила комманда',
        to=Command,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    class Meta:
        ordering = ('one_command','two_command',)
        verbose_name = 'игра'
        verbose_name_plural = 'игры'

    def __str__(self) -> str:
        return f"{self.one_command} VS {self.two_command} : Время начала игры :{self.time_start},статус : {self.status_game}"
    
    def determine_winner(self):
        if self.cof1 > self.cof2:
            self.winners = self.one_command
        elif self.cof1 < self.cof2:
            self.winners = self.two_command
        else:
            self.winners = None
        self.save()

class Bet(models.Model):
    user = models.ForeignKey(
        UserProfile, 
        on_delete=models.CASCADE, 
        verbose_name='Пользователь')
    game = models.ForeignKey(
        Game_start, 
        on_delete=models.CASCADE, 
        verbose_name='Игра')
    team = models.ForeignKey(
        Command, on_delete=models.CASCADE, 
        verbose_name='Выбранная команда')
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name='Ставка')
    is_winner = models.BooleanField(
        default=False, 
        verbose_name='Победа')
    
    def save(self, *args, **kwargs):
        # проверка баланса пользователя перед созданием ставки
        if self.user.balance >= self.amount:
            super().save(*args, **kwargs)
        else:
            raise ValueError('Недостаточно средств на балансе')
        if self.user:
                # счетчик ставок +1 когда пользователь делает ставку
            self.user.bet_counter += 1
            self.user.save()  
        if self.team == self.game.winners:
            self.is_winner = True
            super().save(*args, **kwargs)
        if self.is_winner:
                # eсли ставка выигрышная, начисляем деньги на баланс пользователя , если проиграшная деньги отнимаются
            self.user.balance += self.amount * self.game.cof1 if self.team == self.game.one_command else self.amount * self.game.cof2
            self.user.bet_wins += 1
            self.user.save()
        else:
            self.user.balance - self.amount

    class Meta:
        verbose_name = 'Ставка'
        verbose_name_plural = 'Ставки'

