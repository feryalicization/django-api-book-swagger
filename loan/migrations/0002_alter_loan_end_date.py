# Generated by Django 3.2 on 2022-04-24 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='end_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
