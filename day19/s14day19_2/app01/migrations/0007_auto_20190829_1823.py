# Generated by Django 2.2.3 on 2019-08-29 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_usergroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergroup',
            name='caption',
            field=models.CharField(db_column='cp', max_length=32),
        ),
    ]
