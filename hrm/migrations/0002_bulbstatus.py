# Generated by Django 2.0.6 on 2020-02-15 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bulbstatus',
            fields=[
                ('trigger_id', models.AutoField(primary_key=True, serialize=False)),
                ('on', models.CharField(blank=True, default='', max_length=255)),
                ('off', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
    ]
