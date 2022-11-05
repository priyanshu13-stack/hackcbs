# Generated by Django 4.1.3 on 2022-11-05 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='connect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200, unique=True)),
                ('position', models.CharField(default='', max_length=50)),
                ('company_name', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]