# DockerVulspace
## 1.项目介绍 
DockerVulspace 是一款由Python编写的靶场项目<br>
漏洞类型包含：路径穿越、sql注入、命令执行、代码执行、xss、xxe、ssrf <br>
实现框架包含：django、flask <br>
目录结构：
 -  /dist: 前端代码，静态页面
 -  /djangosrc: 使用django框架实现前端对应api接口
 -  /flasksrc: 使用flask框架实现前端对应api接口
 -  /mysql: 数据库
 -  /nginx: nginx转发前端接口分别至 djangoweb/flaskweb容器
 -  /postgresql: 数据库
 -  /sqlite: 数据库
 -  /docker-compose.yml: docker-compose 一键部署文件，可按需修改（eg:port)

启动容器：
   -  mysite.nginx
   -  mysite.djangoweb
   -  mysite.flaskweb
   -  mysite.mysqldb
   -  mysite.postgresql

 
## 2.项目部署
1.代码拉取
```shell script
git clone https://github.com/jinghao1/DockerVulspace.git
```
2.镜像搭建
```shell script
docker-compose -p pythonVul build
```
3.服务启动
```shell script
docker-compose -p pythonVul up
``` 
4.浏览器直接访问
http://127.0.0.1:8003