# Generated by Django 4.0.1 on 2022-01-20 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Priorty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strPriorty', models.TextField(max_length=30)),
                ('strnotes', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strStatus', models.TextField(max_length=30)),
                ('strnotes', models.TextField(max_length=100)),
            ],
        ),
    ]
