# Generated by Django 2.0.5 on 2018-06-08 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0003_labs'),
    ]

    operations = [
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Labname', models.CharField(max_length=100)),
                ('Servicename', models.CharField(max_length=100)),
                ('Servicecode', models.CharField(max_length=100)),
                ('Price', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=100)),
            ],
        ),
    ]