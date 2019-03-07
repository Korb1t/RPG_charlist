# Generated by Django 2.1.7 on 2019-03-06 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Char',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('person', models.CharField(max_length=32)),
                ('race', models.CharField(max_length=32)),
                ('clas', models.CharField(max_length=32)),
                ('Melee', models.IntegerField()),
                ('Range', models.IntegerField()),
                ('WillPower', models.IntegerField()),
                ('Strength', models.IntegerField()),
                ('Agility', models.IntegerField()),
                ('Intelligence', models.IntegerField()),
                ('Toughness', models.IntegerField()),
                ('Perception', models.IntegerField()),
                ('Fellowship', models.IntegerField()),
                ('FatePoints', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
    ]