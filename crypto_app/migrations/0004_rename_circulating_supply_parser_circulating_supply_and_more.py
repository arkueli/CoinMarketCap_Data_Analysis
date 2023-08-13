# Generated by Django 4.2 on 2023-07-12 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_app', '0003_alter_parser_one_hour_alter_parser_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parser',
            old_name='Circulating_supply',
            new_name='circulating_supply',
        ),
        migrations.RenameField(
            model_name='parser',
            old_name='Market_Cap',
            new_name='market_cap',
        ),
        migrations.RenameField(
            model_name='parser',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='parser',
            old_name='One_hour',
            new_name='one_hour',
        ),
        migrations.RenameField(
            model_name='parser',
            old_name='Price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='parser',
            old_name='Rank',
            new_name='rank',
        ),
        migrations.RenameField(
            model_name='parser',
            old_name='Symbol',
            new_name='symbol',
        ),
        migrations.RenameField(
            model_name='parser',
            old_name='Volume_24h',
            new_name='volume_24h',
        ),
    ]