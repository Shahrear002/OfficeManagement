# Generated by Django 2.1.4 on 2018-12-15 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee_info',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('cost', models.IntegerField()),
                ('totallCost', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
