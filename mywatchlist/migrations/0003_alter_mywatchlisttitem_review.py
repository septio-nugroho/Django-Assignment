# Generated by Django 4.1 on 2022-11-23 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0002_mywatchlisttitem_delete_mywatchlistitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywatchlisttitem',
            name='review',
            field=models.TextField(),
        ),
    ]