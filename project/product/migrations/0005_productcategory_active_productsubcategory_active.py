# Generated by Django 5.0.1 on 2024-02-02 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_category_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='productsubcategory',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
