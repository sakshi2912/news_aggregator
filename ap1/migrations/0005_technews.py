# Generated by Django 3.0.5 on 2020-04-19 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ap1', '0004_weatherdetails_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='technews',
            fields=[
                ('headlines', models.CharField(max_length=500, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=2500)),
                ('hyperlink', models.URLField(max_length=2000)),
                ('source', models.CharField(max_length=2000)),
            ],
        ),
    ]
