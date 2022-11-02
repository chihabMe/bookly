# Generated by Django 4.1.1 on 2022-11-01 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_profile_following'),
        ('actions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='action',
            name='user',
        ),
        migrations.AddField(
            model_name='action',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='accounts.profile'),
            preserve_default=False,
        ),
    ]