#!/bin/bash
yum update -y
yum install -y python3 python3-pip git

pip3 install flask gunicorn

cd /home/ec2-user
git clone https://github.com/scotttennison/CS385homework4.git app
chown -R ec2-user:ec2-user /home/ec2-user/app

cat > /etc/systemd/system/flaskapp.service << SERVICE
[Unit]
Description=Flask App
After=network.target

[Service]
User=ec2-user
WorkingDirectory=/home/ec2-user/app
ExecStart=/usr/local/bin/gunicorn --bind 0.0.0.0:5000 app:app
Restart=always

[Install]
WantedBy=multi-user.target
SERVICE

systemctl daemon-reload
systemctl enable flaskapp
systemctl start flaskapp