# Generated by Django 5.0.6 on 2024-05-19 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='seller_message',
            field=models.TextField(blank=True),
        ),
    ]
