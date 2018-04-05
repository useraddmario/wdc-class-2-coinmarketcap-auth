# Generated by Django 2.0.3 on 2018-04-05 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cryptocurrency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=10)),
                ('rank', models.IntegerField()),
                ('market_cap_usd', models.DecimalField(decimal_places=2, max_digits=14)),
                ('price_usd', models.DecimalField(decimal_places=2, max_digits=7)),
                ('volume_usd_24h', models.DecimalField(decimal_places=2, max_digits=14)),
                ('available_supply', models.DecimalField(decimal_places=2, max_digits=20)),
                ('percent_change_24h', models.DecimalField(decimal_places=2, max_digits=5)),
                ('price_btc', models.DecimalField(blank=True, decimal_places=7, max_digits=8, null=True)),
                ('total_supply', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('max_supply', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('percent_change_1h', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('percent_change_7d', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Cryptocurrency',
                'verbose_name_plural': 'Cryptocurrencies',
            },
        ),
    ]
