# Generated by Django 4.0.5 on 2022-06-11 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steam_ID', models.PositiveIntegerField()),
                ('nickname', models.CharField(max_length=30)),
                ('on_server', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_on', models.BooleanField(default=False)),
            ],
        ),
    ]
