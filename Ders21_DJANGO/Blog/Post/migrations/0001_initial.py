# Generated by Django 4.0.3 on 2022-03-26 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('BlogID', models.AutoField(primary_key=True, serialize=False)),
                ('BlogTitle', models.CharField(max_length=100)),
                ('BlogText', models.TextField()),
            ],
        ),
    ]
