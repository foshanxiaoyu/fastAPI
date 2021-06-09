# fastAPI
记录过程
基床：centOs8 oracle cloud VPS ，目前还不能解决 firewalld 打开的阻数据
环境：python -m venv fast
加载环境：source /fast/bin/activate
pip install fastapi,uvicorn,request,pydantic,jinja2
pip freeze>requirements.txt
yum install nginx
nginx  
http{
server{
  listen 80;
  server_name xxxxxxxx;
  root /xxxxxxx;
  return 301 https://$host$request_uri;
  )
 
 server{
  listen 443 ssl http2; # http2 对应是H2协议
  server_name xxxxxxxxx;
  sslcert;
  sslcertkey;
  location /api/ {
     proxy_setheader X-Forwarded-Proto $scheme; # 此项对应fastapi 中设置的 --root-path /api 后的Css宣染
     proxy_pass http://localhost:XXXX/;  # 此端口要事先在cloud VPS 开启
     }
  }
}
