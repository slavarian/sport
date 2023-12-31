# Generated by Django 4.2.4 on 2023-09-11 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0014_remove_sportsman_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, verbose_name='почта')),
                ('username', models.CharField(max_length=100, verbose_name='никнейм')),
                ('balance', models.IntegerField(default=0, verbose_name='баланс пользователя')),
                ('bet_counter', models.IntegerField(default=0, null=True, verbose_name='сделано ставок')),
                ('bet_wins', models.IntegerField(default=0, null=True, verbose_name='победных ставок')),
            ],
            options={
                'verbose_name': 'баланс пользователя',
                'verbose_name_plural': 'баланс пользователей',
                'ordering': ('username',),
            },
        ),
        migrations.AlterModelOptions(
            name='useraccount',
            options={},
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='bet_counter',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='bet_wins',
        ),
        migrations.AlterField(
            model_name='game_start',
            name='cof1',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2, verbose_name='коф.победы 1 комманды'),
        ),
        migrations.AlterField(
            model_name='game_start',
            name='cof2',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2, verbose_name='коф.победы 2 комманды'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_account', to='sport.user'),
        ),
    ]
