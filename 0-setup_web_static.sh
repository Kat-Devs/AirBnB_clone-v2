#!/usr/bin/env bash
# Bash script to setup web servers for web_static
# deployment

# Install Nginx 
sudo apt-get update
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

# Create directories and test html file
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

# Create test HTML
sudo echo "<html>
<head>
</head>
<body>
Holberton School
</body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbloic link to test fodler
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Set ownership
sudo chown -R ubuntu:ubuntu /data/

# Add nginx config to serve web_static content
if ! grep -q 'location /hbnb_static' /etc/nginx/sites-enabled/default
then 
    sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
fi

#Restart Nginx
sudo service nginx restart






