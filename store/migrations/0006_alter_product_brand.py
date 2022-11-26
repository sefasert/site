# Generated by Django 4.1.1 on 2022-10-21 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_product_brand_alter_product_durum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('PHILIPS', 'philips'), ('LG', 'lg'), ('ARÇELİK', 'arcelik'), ('Botech', 'botech'), ('SUNNY', 'sunny'), ('AWOX', 'awox'), ('GRUNDIG', 'grundig'), ('Arçelik-Beko-Grundig', 'arcelik-beko-grundig'), ('ONVO', 'onvo'), ('Dreamstar', 'dreamstar'), ('TECHNOBOX', 'technobox'), ('NEXT', 'next'), ('GEEPAS', 'geepas'), ('TCL', 'tcl'), ('CVS', 'cvs'), ('Dijitsu', 'dijitsu'), ('AUO', 'auo'), ('Profilo', 'profilo'), ('TELENOVA', 'telenova'), ('BEKO', 'beko'), ('SAMSUNG', 'samsung'), ('VESTEL', 'vestel'), ('ROWELL', 'rowell'), ('SANYO', 'sanyo')], max_length=50, null=True),
        ),
    ]
