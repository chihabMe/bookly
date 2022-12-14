# Generated by Django 4.1.1 on 2022-10-29 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_user'),
        ('books', '0004_alter_bookimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='likes',
            field=models.ManyToManyField(related_name='liked_books', to='accounts.profile'),
        ),
    ]
