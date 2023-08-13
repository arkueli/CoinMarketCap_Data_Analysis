# Generated by Django 4.2 on 2023-06-27 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crypto_app", "0002_alter_parser_one_hour_alter_parser_price_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="parser",
            name="One_hour",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="parser",
            name="Price",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="parser",
            name="seven_days",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="parser",
            name="twenty_four_hours",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
