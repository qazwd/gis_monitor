from django.db import models

# Create your models here.
class Person(models.Model):
    "人员监控数据模型"
    name = models.CharField(max_length=100, verbose_name="姓名")
    gender = models.CharField(max_length=10, choices=[("男", "男"),("女", "女")], verbose_name="性别")
    phone = models.CharField(max_length=20, verbose_name="电话")
    purpose = models.CharField(max_length=200, verbose_name="到访目的")
    latitude = models.FloatField(verbose_name="纬度")
    longitude = models.FloatField(verbose_name="经度")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "人员"
        verbose_name_plural = "人员"

class Vehicle(models.Model):
    "车辆监控数据模型"
    plate = models.CharField(max_length=20, verbose_name="车牌号码", unique=True)
    driver = models.CharField(max_length=100, verbose_name="驾驶员姓名")
    phone = models.CharField(max_length=20, verbose_name="驾驶员电话")
    purpose = models.CharField(max_length=200, verbose_name="到访目的")
    latitude = models.FloatField(verbose_name="纬度")
    longitude = models.FloatField(verbose_name="经度")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "车辆"
        verbose_name_plural = "车辆"
