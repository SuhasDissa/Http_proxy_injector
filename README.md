
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

## How To use

There are two ways to run this

- Run the executables (Recommended)
- Run from source code

## Running from Executables

### Installing Dependancies

First Download the correct executables according to your needs

[![Download For SSH](https://img.shields.io/badge/Download_For_SSH-238636?style=for-the-badge&logoColor=white)](https://github.com/SuhasDissa/Http_proxy_injector/releases/download/V1/SSH_Executables.zip)

[![Download For SSL](https://img.shields.io/badge/Download_For_SSL-238636?style=for-the-badge&logoColor=white)](https://github.com/SuhasDissa/Http_proxy_injector/releases/download/V1/SSL_Executables.zip)

Then install these dependancies

```bash
  sshpass
  netcat-openbsd
  corkscrew
  nc
```

Use `sudo apt install <package>` for Debian based distros and use `sudo pacman -S <package>` for Arch based distros

Modify the settings.ini file according to your needs

### How to configure settings.ini file

Run the **SettingsEditor** and edit the settings.

### How to use

Run **InjectorSSH** or **InjectorSSL** in terminal

<p style="color:red;">Warning: Do not run http_Injector by double clicking it!</p>

```bash
cd /path/to/http/injector/folder/
chmod +x ./InjectorSSH
./InjectorSSH
```

Install [Proxy Switcher](https://add0n.com/proxy-switcher.html) extension on you Browser and choose the following settings

![Screenshot](./Screenshot.png)
