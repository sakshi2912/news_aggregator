# Generated by Django 3.0.5 on 2020-04-19 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ap1', '0002_sportsnews'),
    ]

    operations = [
        migrations.CreateModel(
            name='weatherdetails',
            fields=[
                ('city', models.CharField(max_length=500, primary_key=True, serialize=False)),
                ('temperature', models.CharField(max_length=2500)),
                ('pressure', models.CharField(max_length=2000)),
                ('humidity', models.CharField(max_length=2000)),
            ],
        ),
    ]
