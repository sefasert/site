# Generated by Django 4.1.1 on 2022-10-10 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_tags_alter_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('TCL', 'tcl'), ('Profilo', 'profilo'), ('NEXT', 'next'), ('SUNNY', 'sunny'), ('Dreamstar', 'dreamstar'), ('AUO', 'auo'), ('PHILIPS', 'philips'), ('VESTEL', 'vestel'), ('SAMSUNG', 'samsung'), ('BEKO', 'beko'), ('TECHNOBOX', 'technobox'), ('TELENOVA', 'telenova'), ('ARÇELİK', 'arcelik'), ('LG', 'lg'), ('CVS', 'cvs'), ('Botech', 'botech'), ('SANYO', 'sanyo'), ('Dijitsu', 'dijitsu'), ('AWOX', 'awox')], max_length=50, null=True),
        ),
    ]
