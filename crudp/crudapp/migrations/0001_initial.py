# Generated by Django 4.0.3 on 2022-12-20 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('address', models.TextField(max_length=200)),
            ],
        ),
    ]
