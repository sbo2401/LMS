# Generated by Django 4.1 on 2022-08-24 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_remove_studentname_surname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalog', models.CharField(max_length=255)),
                ('collections', models.TextField(default='Name of book Collection')),
            ],
        ),
    ]
