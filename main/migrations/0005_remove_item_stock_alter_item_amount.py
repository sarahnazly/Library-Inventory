# Generated by Django 4.2.5 on 2023-09-26 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_item_added_date_item_date_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='stock',
        ),
        migrations.AlterField(
            model_name='item',
            name='amount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
