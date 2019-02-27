# Installing lamp server on ubuntu 18 
# https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-ubuntu-18-04
#Step 1 — Installing Apache and Updating the Firewall
  sudo apt update
  sudo apt install apache2
# Adjust the Firewall to Allow Web Traffic
  sudo ufw app list  [make sure that your firewall allows HTTP and HTTPS traffic]
    output 
      Available applications:
       Apache
       Apache Full
       Apache Secure
       OpenSSH
  sudo ufw app info "Apache Full"
    output
      Profile: Apache Full
      Title: Web Server (HTTP,HTTPS)
      Description: Apache v2 is the next generation of the omnipresent Apache web
      server.

      Ports:
        80,443/tcp
  sudo ufw allow in "Apache Full"
checking: http://your_server_ip
#step 2 - Installing PHP
 sudo apt install php libapache2-mod-php php-mysql
#step 3 Testing PHP Processing on your Web Server
sudo nano /var/www/html/info.php
info.php
  <?php
   phpinfo();
  ?>
sudo service apache2 restarted