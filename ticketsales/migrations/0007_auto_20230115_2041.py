# Generated by Django 3.2 on 2023-01-15 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('ticketsales', '0006_alter_timemodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketmodel',
            name='Profilemodel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.profilemodel', verbose_name='user'),
        ),
        migrations.DeleteModel(
            name='Profilemodel',
        ),
    ]
