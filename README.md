# gis_monitor

GIS 人车监控系统

# 初次启动

进入项目根目录：cd gis_monitor

创建并激活虚拟环境：conda

安装依赖：conda env create -f environment.yml

生成数据库迁移文件：python manage.py makemigrations

应用迁移：python manage.py migrate

启动开发服务器：python manage.py runserver 0.0.0.0:8000（局域网）

启动位置模拟器：python manage.py simulator

# 访问系统

http://localhost:8000(gis页面)

http://localhost:8000/api/(API浏览)

http://localhost:8000/admin/(Django管理后台)
