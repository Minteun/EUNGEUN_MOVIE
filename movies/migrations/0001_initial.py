# Generated by Django 2.1.15 on 2020-06-11 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster_path', models.TextField()),
                ('adult', models.BooleanField()),
                ('overview', models.TextField()),
                ('release_date', models.DateField()),
                ('original_title', models.CharField(max_length=300)),
                ('original_language', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=500)),
                ('backdrop_path', models.TextField()),
                ('popularity', models.FloatField()),
                ('vote_count', models.IntegerField()),
                ('video', models.BooleanField()),
                ('vote_average', models.FloatField()),
                ('genres', models.ManyToManyField(related_name='movies', to='movies.Genre')),
            ],
        ),
    ]