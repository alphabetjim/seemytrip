# Generated by Django 4.2.11 on 2024-03-13 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travellerprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traveller',
            name='profile_photo',
            field=models.ImageField(blank=True, default='placeholder', upload_to='profileImages/'),
        ),
    ]
