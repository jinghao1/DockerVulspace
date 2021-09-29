# DongTai-python-vulspace
[![django-project](https://img.shields.io/badge/django%20versions-3.0.3-blue)](https://www.djangoproject.com/) 


## 项目介绍
DongTai-WebAPI 用于处理DongTai用户资源管理的相关请求，包括：


- 项目管理请求
- 漏洞管理
- 用户数据检索
- 系统配置资源
- 用户/角色管理
- Agent部署管理
- 租户管理
- 部署文档检索



### 部署方案
- 源码部署
- 容器部署

**源码部署**

1.初始化数据库

- 安装MySql 5.7，创建数据库`DongTai-webapi`，运行数据库文件`conf/db.sql`
- 进入`webapi`目录，运行`python manage.py createsuperuser`命令创建管理员

2.修改配置文件

- 复制配置文件`conf/config.ini.example`为`conf/config.ini`并需改其中的配置；其中，`engine`对应的url为`DongTai-engine`的服务地址，`apiserver`对应的url为`DongTai-openapi`的服务地址

3.运行服务

- 运行`python manage.py runserver`启动服务

**容器部署**

1.初始化数据库

- 安装MySql 5.7，创建数据库`DongTai-webapi`，运行数据库文件`conf/db.sql`
- 进入`webapi`目录，运行`python manage.py createsuperuser`命令创建管理员

2.修改配置文件

复制配置文件`conf/config.ini.example`为`conf/config.ini`并需改其中的配置；其中：
- `engine`对应的url为`DongTai-engine`的服务地址
- `apiserver`对应的url为`DongTai-openapi`的服务地址

3.构建镜像
```
$ docker build -t huoxian/dongtai-python-vulspace:latest .
```

4.启动容器
```
$ docker run -d -p 8000:8000 --restart=always --name dongtai-python-vulspace huoxian/dongtai-python-vulspace:latest
```

### 文档
- [官方文档](https://huoxianclub.github.io/LingZhi/#/)
- [快速体验](http://aws.iast.huoxian.cn:8000/login)
