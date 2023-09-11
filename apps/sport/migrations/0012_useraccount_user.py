# Generated by Django 4.2.4 on 2023-09-11 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sport', '0011_delete_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_account', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]