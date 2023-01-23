# Generated by Django 3.2 on 2023-01-12 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketsales', '0005_auto_20230110_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timemodel',
            name='Status',
            field=models.IntegerField(choices=[(1, 'ticket sale is started for this session'), (2, 'ticket sale is over'), (3, 'this session is canceled'), (4, 'ticket is still being sold')], verbose_name='status'),
        ),
    ]