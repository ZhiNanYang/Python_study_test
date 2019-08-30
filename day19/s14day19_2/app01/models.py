from django.db import models


class UserGroup(models.Model):
    """docstring for UserGroup"""
    uid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=32, db_column='cp')
    ctime = models.DateTimeField(auto_now_add=True, null=True)
    atime = models.DateTimeField(auto_now=True, null=True)


# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=32, verbose_name="user")
    password = models.CharField(max_length=64)
    email = models.CharField(max_length=64, null=True)
    # gender = models.CharField(max_length=60, null=True)
    test = models.URLField(max_length=19, null=True, blank=True)
    user_group = models.ForeignKey(
        "UserGroup", to_field='uid', default=1, on_delete=models.CASCADE
    )

    user_type_choices = (
        (1, "超级用户"),
        (2, "普通用户"),
        (3, "VIP用户"),
    )

    user_type = models.IntegerField(choices=user_type_choices, default=1)
