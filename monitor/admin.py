from django.contrib import admin
from .models import Person, Vehicle

# Register your models here.
admin.site.register(Person)
admin.site.register(Vehicle)

# 可运行 python manage.py createsuperuser 来创建超级用户
# 登录后，在后台管理界面可以添加、修改、删除人员和车辆数据
# 后台管理界面地址：http://127.0.0.1:8000/admin/ 登陆
# 用户名：admin 密码：123456
# 注意：生产环境请修改默认用户名和密码，确保安全
# 也可以通过 API 来操作数据，见 monitor/views.py 和 monitor/urls.py
# API 地址：http://127.0.0.1:8000/api/monitor/ （需要先启动项目，如 python manage.py runserver）
# 人员 API ：http://127.0.0.1:8000/api/monitor/people/
# 车辆 API ：http://127.0.0.1:8000/api/monitor/vehicles/
# 注意：需要在请求头中添加 Authorization: Bearer <token> ，其中 <token> 是登录后获取的 token
# 可以使用 Postman 等工具来测试 API
# 也可以使用前端页面来调用 API，见前端代码 monitor/templates/monitor/index.html
