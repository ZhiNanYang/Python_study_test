# Generated by Django 2.2.3 on 2019-08-29 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='email',
            field=models.CharField(default='yzn7020@163.com', max_length=64),
            preserve_default=False,
        ),
    ]
