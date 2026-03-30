provider "aws" {
  region = var.aws_region
}

resource "aws_security_group" "app_sg" {
  name        = "cs385-app-sg"
  description = "Allow HTTP and SSH"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "app_server" {
  ami           = "ami-0ceecbb0f30a902a6"
  instance_type = "t2.micro"

  vpc_security_group_ids = [aws_security_group.app_sg.id]

user_data = <<-EOF
    #!/bin/bash
    yum update -y
    yum install -y python3 python3-pip git

    pip3 install flask gunicorn

    cd /home/ec2-user
    git clone https://github.com/scotttennison/CS385homework4.git app
    cd app

    echo "[Unit]" > /etc/systemd/system/flaskapp.service
    echo "Description=Flask App" >> /etc/systemd/system/flaskapp.service
    echo "After=network.target" >> /etc/systemd/system/flaskapp.service
    echo "[Service]" >> /etc/systemd/system/flaskapp.service
    echo "User=ec2-user" >> /etc/systemd/system/flaskapp.service
    echo "WorkingDirectory=/home/ec2-user/app" >> /etc/systemd/system/flaskapp.service
    echo "ExecStart=/usr/local/bin/gunicorn --bind 0.0.0.0:5000 app:app" >> /etc/systemd/system/flaskapp.service
    echo "Restart=always" >> /etc/systemd/system/flaskapp.service
    echo "[Install]" >> /etc/systemd/system/flaskapp.service
    echo "WantedBy=multi-user.target" >> /etc/systemd/system/flaskapp.service

    systemctl daemon-reload
    systemctl enable flaskapp
    systemctl start flaskapp
  EOF

  tags = {
    Name = "CS385-App-Server"
  }
}