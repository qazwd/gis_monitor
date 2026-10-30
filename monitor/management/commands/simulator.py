import random
import time
from django.core.management.base import BaseCommand
from monitor.models import Person, Vehicle

class Command(BaseCommand):
    help = 'Simulate moving people and vehicles by updating their positions every 10 seconds.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting position simulator...'))
        try:
            while True:
                self.update_positions()
                time.sleep(10)  # 严格控制10秒更新一次
        except KeyboardInterrupt:
            self.stdout.write(self.style.WARNING('Simulator stopped by user'))

    def update_positions(self):
        """更新所有人员和车辆的位置"""
        # 更新人员位置
        persons = Person.objects.all()
        for person in persons:
            person.latitude += random.uniform(-0.00009, 0.00009)
            person.longitude += random.uniform(-0.00009, 0.00009)
            person.save()

        # 更新车辆位置
        vehicles = Vehicle.objects.all()
        for vehicle in vehicles:
            vehicle.latitude += random.uniform(-0.00009, 0.00009)
            vehicle.longitude += random.uniform(-0.00009, 0.00009)
            vehicle.save()

        self.stdout.write(self.style.SUCCESS(f'Updated {persons.count()} persons and {vehicles.count()} vehicles positions'))
        # 终端输出更新信息成功
        print('数据更新成功')
