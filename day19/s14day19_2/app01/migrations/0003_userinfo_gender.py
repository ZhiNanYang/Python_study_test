# Generated by Django 2.2.3 on 2019-08-29 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_userinfo_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='gender',
            field=models.CharField(max_length=60, null=True),
        ),
    ]