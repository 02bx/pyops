# Generated by Django 2.0.6 on 2019-02-14 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navi', '0002_navi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navi',
            name='url',
            field=models.URLField(max_length=2000, verbose_name='网址'),
        ),
    ]