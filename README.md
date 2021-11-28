
# Http Injector Python

Bypass ISP firewalls Browse the internet through ssh tunnel



## How it works

This script tricks your isp into thinking you are using a special data pack (ex: teams.microsoft.com)
and allows you to browse any website using that pack
  
## Special thanks to

This project is a modified version of the following project. make sure to check their project.
 - [abdoxfox/http-ssl-ssh-injector](https://github.com/abdoxfox/http-ssl-ssh-injector)
 
  
## Disclaimer
I'm not responsible for anything you do with this

  
## Installing

First install these dependancies

```bash
  sshpass
  netcat-openbsd
  corkscrew
  nc
  python3
```

Use `sudo apt install <package>` for Debian based distros and use `sudo pacman -S <package>` for Arch based distros

Modify the settings.ini file according to your needs

## How to configure settings.ini file

Fill the following lines with your credentials. 
Use an **SSH server** if you want to use **SSH mode** or use an **SSL Supported server** if you want to use **SSL mode**

```
host = your.ssh.server
port = your port
username = username
password = password
```

### How to switch between SSH and SSL mode

open the `ssh.py` file and goto **line 34**
then change the variable according to following 

- SSH mode: `arg = '1'`
- SSL mode: `arg = '2'`

## How to use

Then run http.sh in terminal
```bash
cd /path/to/http/injector/folder/
chmod +x ./http.sh
./http.sh
```

Install [Proxy Switcher](https://add0n.com/proxy-switcher.html) extension on you Browser and choose the following settings

![Screenshot](./Screenshot.png)

  
