
# docker 学起来

```bash
docker pull/build
# 获取/创建镜像

docker images
# 查看已有镜像

docker run ubuntu
# 如果不存在则会自动下载

docker run nginx -p8080:80 -d nginx
# 访问 http://localhost:8080/ 就可以看到啦
# -p 是映射端口
# -d 是以守护进程运行

docker ps
# 你会看到类似这样的东西
# CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS              PORTS                  NAMES
# f2b2de69e375        nginx               "nginx -g 'daemon of…"   About a minute ago   Up About a minute   0.0.0.0:8080->80/tcp   ecstatic_almeida

docker cp index.html f2b2de69e375://usr/share/nginx/html
# 拷贝文件到 docke 里
## 访问 http://localhost:8080 可以看到

docker stop f2b2de69e375
# 停止容器
```

好了，休息一下。然后再次启动那个 nginx 容器，访问 http://localhost:8080，好像刚才的网页没有了呢。

因为 `docker cp` 做的修改只是暂存的，不是持久的，继续把玩。

```bash
docker cp index.html 764f680243c7://usr/share/nginx/html
# 再次复制，然后提交（注意 ID 有变化了）
docker commit -m "just test" 764f680243c7 this_version_name

docker images
# REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
# this_version_name   latest              f7cff4cf293d        3 seconds ago       109MB

docker rmi f7cff4cf293d
# 删除镜像
```

## Dockerfile

```bash
FROM alpine:latest
MAINTAINER jonge
CMD echo 'hello docker'

# FROM 来源
# 此 file 作者
# 命令

docker build -t hello_docker_from_file .
# 构建 docker 镜像
```
