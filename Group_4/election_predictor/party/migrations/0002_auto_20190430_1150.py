# Generated by Django 2.1.7 on 2019-04-30 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentdetails',
            name='card_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='paymentdetails',
            name='credits',
            field=models.IntegerField(),
        ),
    ]
