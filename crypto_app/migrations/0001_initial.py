# Generated by Django 4.2.2 on 2023-06-14 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rank', models.TextField()),
                ('Name', models.TextField()),
                ('Symbol', models.TextField()),
                ('Market_Cap', models.TextField()),
                ('Price', models.DecimalField(decimal_places=4, max_digits=5)),
                ('Circulating_supply', models.TextField()),
                ('Volume_24h', models.TextField()),
                ('One_hour', models.DecimalField(decimal_places=2, max_digits=5)),
                ('twenty_four_hours', models.DecimalField(decimal_places=2, max_digits=5)),
                ('seven_days', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
