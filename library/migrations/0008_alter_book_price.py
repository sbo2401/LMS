# Generated by Django 4.1 on 2022-08-27 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Price',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]
