# Generated by Django 2.2.3 on 2019-08-29 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0010_auto_20190829_1841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='user_type_id',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user_type',
            field=models.IntegerField(choices=[(1, '超级用户'), (2, '普通用户'), (3, 'VIP用户')], default=1),
        ),
    ]