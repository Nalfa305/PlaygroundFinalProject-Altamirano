# Generated by Django 5.0.1 on 2024-02-01 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cliente',
            new_name='Client',
        ),
        migrations.RenameModel(
            old_name='Pais',
            new_name='Country',
        ),
        migrations.AlterModelOptions(
            name='country',
            options={},
        ),
    ]