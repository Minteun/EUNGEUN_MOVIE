# Generated by Django 3.0.7 on 2020-06-13 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20200611_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='rank',
            field=models.IntegerField(default=10),
        ),
    ]
