# Generated by Django 4.2.1 on 2023-05-10 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_vat_description_alter_product_vat_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
