from django.db import models


class Business(models.Model):
    caption = models.CharField(max_length=32)
    code = models.CharField(max_length=32, null=True)


class HOST(models.Model):
    nid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32, db_index=True)
    ip = models.GenericIPAddressField(protocol='ipv4', db_index=True)
    port = models.IntegerField()
    b = models.ForeignKey(to='Business', to_field='id', on_delete=models.CASCADE)
