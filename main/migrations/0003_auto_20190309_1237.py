# Generated by Django 2.1.7 on 2019-03-09 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190309_1232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='char',
            old_name='FatePoints_bonus',
            new_name='CurrentFP',
        ),
    ]