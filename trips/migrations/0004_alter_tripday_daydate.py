# Generated by Django 4.2.11 on 2024-03-20 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0003_tripday_daydate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripday',
            name='dayDate',
            field=models.DateField(blank=True),
        ),
    ]