# Generated by Django 4.2.5 on 2023-09-23 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_item_borrow_date_item_added_date_item_stock_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='added_date',
        ),
        migrations.AddField(
            model_name='item',
            name='date_added',
            field=models.DateField(auto_now_add=True),
            preserve_default=False,
        ),
    ]
