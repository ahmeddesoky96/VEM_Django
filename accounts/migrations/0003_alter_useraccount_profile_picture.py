# Generated by Django 4.2.2 on 2023-06-25 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_useraccount_birth_date_useraccount_is_seller_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='profile_picture',
            field=models.ImageField(blank=True, default='static/profile_pictures/profile.png', null=True, upload_to='build/static/profile_pictures/'),
        ),
    ]
