# Generated by Django 2.0.6 on 2020-02-15 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_name', models.CharField(blank=True, default='', max_length=255)),
                ('employee_age', models.IntegerField()),
                ('employee_ranking', models.FloatField()),
            ],
        ),
    ]
