# Generated by Django 4.2.2 on 2023-07-21 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
    ]