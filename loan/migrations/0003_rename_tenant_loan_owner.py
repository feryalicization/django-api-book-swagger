# Generated by Django 3.2 on 2022-04-24 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0002_alter_loan_end_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loan',
            old_name='tenant',
            new_name='owner',
        ),
    ]