# Generated by Django 5.0.7 on 2024-07-30 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_balancesheet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='balancesheet',
            old_name='expense_id',
            new_name='expense',
        ),
    ]
