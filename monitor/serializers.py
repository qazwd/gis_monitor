from rest_framework import serializers
from .models import Person, Vehicle
import re


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"

    def validate_phone(self, value):
        pattern = r'^1[3-9]\d{9}$'
        if not re.match(pattern, value):
            raise serializers.ValidationError("请输入有效的中国大陆手机号码")
        return value
    
    def validate_latitude(self, value):
        if not -90 <= value <= 90:
            raise serializers.ValidationError("纬度值必须在 -90 到 90 之间")
        return value

    def validate_longitude(self, value):
        if not -180 <= value <= 180:
            raise serializers.ValidationError("经度值必须在 -180 到 180 之间")
        return value


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"

    def validate_plate(self, value):
        # 验证普通小型汽车、大型汽车号牌
        pattern = r'^[京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领][A-HJ-NP-Z][A-HJ-NP-Z0-9]{4}[A-HJ-NP-Z0-9挂学警港澳]$'
        if not re.match(pattern, value):
            raise serializers.ValidationError("请输入有效的车牌号")
        return value
    
    def validate_phone(self, value):
        pattern = r'^1[3-9]\d{9}$'
        if not re.match(pattern, value):
            raise serializers.ValidationError("请输入有效的中国大陆手机号码")
        return value
    
    def validate_latitude(self, value):
        if not -90 <= value <= 90:
            raise serializers.ValidationError("纬度值必须在 -90 到 90 之间")
        return value

    def validate_longitude(self, value):
        if not -180 <= value <= 180:
            raise serializers.ValidationError("经度值必须在 -180 到 180 之间")
        return value

# class PersonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Person
#         fields = ['id', 'name', 'gender', 'phone', 'purpose', 'latitude', 'longitude']  # 仅暴露必要字段

# class VehicleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Vehicle
#         fields = ['id', 'plate', 'driver', 'phone', 'purpose', 'latitude', 'longitude']
