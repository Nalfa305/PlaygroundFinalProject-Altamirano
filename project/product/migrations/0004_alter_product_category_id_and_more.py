# Generated by Django 5.0.1 on 2024-02-02 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_product_category_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category_id',
            field=models.ManyToManyField(blank=True, limit_choices_to={'active': True}, null=True, to='product.productcategory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory_id',
            field=models.ManyToManyField(blank=True, limit_choices_to={'active': True}, null=True, to='product.productsubcategory'),
        ),
    ]
