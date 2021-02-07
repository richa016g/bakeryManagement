# Generated by Django 3.1.6 on 2021-02-07 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakeryitem', '0002_auto_20210207_1256'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BakeryItemPriceDetail',
        ),
        migrations.AddField(
            model_name='bakeryitem',
            name='costPrice',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bakeryitem',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bakeryitem',
            name='sellingPrice',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]