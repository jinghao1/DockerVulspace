# DockerVulspace

## 项目介绍

DockerVulspace 是一款由Python编写的靶场项目

### 功能特性

* 可检测漏洞类型
  * 路径穿越
  * SQL 注入
  * 命令执行
  * 代码执行
  * XSS
  * XXE
  * SSRF
* 支持框架
  * Django
  * Flask

### 目录结构

- /dist: 前端代码，静态页面
- /djangosrc: 使用django框架实现前端对应api接口
- /flasksrc: 使用flask框架实现前端对应api接口
- /mysql: 数据库
- /nginx: nginx转发前端接口分别至 djangoweb/flaskweb容器
- /postgresql: 数据库
- /sqlite: 数据库
- /docker-compose.yml: docker-compose 一键部署文件，可按需修改（eg:port)

### 启动容器

- nginx
- mysqldb
- postgresql
- djangoweb
- flaskweb
 
## 项目部署

### 代码拉取

```shell script
git clone https://github.com/jinghao1/DockerVulspace.git
cd DockerVulspace
```

### 下载 Agent

从 [IAST 官网](https://iast.huoxian.cn/deploy) 下载 Python Agent， 解压后进入目录，将`dongtai_agent_python`文件夹复制至 `DockerVulspace/` 目录下

> 注意：项目名称可修改 `dongtai_agent_python/config.json` 中的 `project.name` 或者配置环境变量

```shell script
export projectName=demoProjectName
```

### 软件包镜像加速(可选)

```dockerfile
version: '3.4'

services:
  djangoweb:
    build:
      args:
        PYPI_MIRROR: https://pypi.tuna.tsinghua.edu.cn/simple
        DEBIAN_MIRROR: mirrors.aliyun.com
        DEBIAN_SECURITY_MIRROR: mirrors.aliyun.com

  flaskweb:
    build:
      args:
        PYPI_MIRROR: https://pypi.tuna.tsinghua.edu.cn/simple
        DEBIAN_MIRROR: mirrors.aliyun.com
        DEBIAN_SECURITY_MIRROR: mirrors.aliyun.com
```

保存以上内容为 `docker-compose.override.yml`, 这样在构建镜像时会使用相对应的软件包镜像, 可根据自身情况设置对应的软件包镜像地址

### 容器镜像构建

```shell script
docker-compose -p pythonVul build
```

### 服务启动
```shell script
docker-compose -p pythonVul up
``` 

### 浏览器直接访问

http://127.0.0.1:8003
