# Generated by Django 5.0.1 on 2024-02-02 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_productcategory_active_productsubcategory_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsubcategory',
            name='active',
        ),
    ]
