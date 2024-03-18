# Generated by Django 4.2.10 on 2024-03-18 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_account_accountstock_accountcurrency'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountstock',
            name='average_sell_cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
