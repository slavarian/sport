# Generated by Django 4.2.4 on 2023-09-04 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0002_alter_command_options_alter_game_start_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='пользователь')),
                ('balance', models.ImageField(default=0, upload_to='', verbose_name='баланс пользователя')),
                ('bet_counter', models.ImageField(default=0, upload_to='', verbose_name='сделано ставок')),
                ('bet_wins', models.ImageField(default=0, upload_to='', verbose_name='победных ставок')),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'пользователи',
                'ordering': ('username',),
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Время')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport.user', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Транзакция',
                'verbose_name_plural': 'Транзакции',
            },
        ),
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ставка')),
                ('is_winner', models.BooleanField(default=False, verbose_name='Победа')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport.game_start', verbose_name='Игра')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport.command', verbose_name='Выбранная команда')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport.user', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Ставка',
                'verbose_name_plural': 'Ставки',
            },
        ),
    ]
