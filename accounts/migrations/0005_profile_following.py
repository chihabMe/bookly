# Generated by Django 4.1.1 on 2022-10-30 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(related_name='followers', through='accounts.Contact', to='accounts.profile'),
        ),
    ]