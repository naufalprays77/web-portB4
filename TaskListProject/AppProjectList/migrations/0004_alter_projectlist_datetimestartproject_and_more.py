# Generated by Django 4.0.1 on 2022-02-11 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProjectList', '0003_rename_datetimeendproject_projectlist_duedatetimeproject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectlist',
            name='datetimeStartProject',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='projectlist',
            name='dueDateTimeProject',
            field=models.DateField(),
        ),
    ]
