# Generated by Django 5.0.1 on 2024-02-02 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_remove_productsubcategory_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsubcategory',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
