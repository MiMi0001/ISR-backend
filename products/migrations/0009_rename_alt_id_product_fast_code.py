# Generated by Django 4.2.1 on 2023-05-17 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_rename_productcategory_pricecategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='alt_id',
            new_name='fast_code',
        ),
    ]
