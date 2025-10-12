<h1 align="center">M4tr1x: Exit Denied</h1>
<p align="center">2025, October 12<br>Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>524</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Free your mind. Exit from the M4tr1x...</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/c435a79d-756c-4e87-86b5-0c81a25e5f82"><br>
Access it <a href="https://tryhackme.com/room/m4tr1xexitdenied">here</a>.<br>
<img width="1200px" src=""></p>

<h2>Task 1 . Story</h2>
<br>

<p><em>Answer the question below</em></p>




<br>
<h1 align="center">Port Scanning<a id='1'></a></h1>
<p align="center"><strong>3</strong> open ports</p>
<br>

<div align="center"><p>

| **Port**           | **Service**          | **Version**                                                   |
|-------------------:|:---------------------|:--------------------------------------------------------------|
| `22`               |`SSH`                 | OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0) |
| `80`               |`HTTP`                |Apache httpd 2.4.41 ((Ubuntu))                                 |
| `3306`             |`mysql`               |MySQL 5.5.5-10.3.39-MariaDB-0ubuntu0.20.04.2                   |

</p></div><br>

```bash
:~/M4tr1xExitDenied# nmap -sT xx.xxx.xx.xx
...
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
3306/tcp open  mysql
...
```

```bash
:~/M4tr1xExitDenied# nmap -sC -sV -Pn -p- -T4 xx.xxx.xx.xx
...
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Linux-Bay
3306/tcp open  mysql   MySQL 5.5.5-10.3.39-MariaDB-0ubuntu0.20.04.2
| mysql-info: 
|   Protocol: 10
|   Version: 5.5.5-10.3.39-MariaDB-0ubuntu0.20.04.2
|   Thread ID: 115
|   Capabilities flags: 63486
|   Some Capabilities: SupportsTransactions, DontAllowDatabaseTableColumn, ConnectWithDatabase, Speaks41ProtocolOld, Support41Auth, FoundRows, IgnoreSigpipes, LongColumnFlag, InteractiveClient, SupportsLoadDataLocal, IgnoreSpaceBeforeParenthesis, ODBCClient, Speaks41ProtocolNew, SupportsCompression, SupportsMultipleStatments, SupportsMultipleResults, SupportsAuthPlugins
|   Status: Autocommit
|   Salt: ,DROrrg/R/1Kb-YX/}LD
|_  Auth Plugin Name: mysql_native_password
MAC Address: 16:FF:DA:4F:19:B5 (Unknown)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 9.93 seconds
```

<br>
<h1 align="center">Web Vulberability Scanning<a id='2'></a></h1>

```bash
~/M4tr1xExitDenied# nikto -h xx.xxx.xx.xx
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xx.xx
+ Target Hostname:    xx.xxx.xx.xx
+ Target Port:        80
+ Start Time:         2025-10-12 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ Cookie mybb[lastvisit] created without the httponly flag
+ Cookie mybb[lastactive] created without the httponly flag
+ Cookie sid created without the httponly flag
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ DEBUG HTTP verb may show server debugging information. See http://msdn.microsoft.com/en-us/library/e8z01xdh%28VS.80%29.aspx for details.
+ OSVDB-59619: /inc/config.php: Bookmark4U v1.8.3 include files are not protected and may contain remote source injection by using the 'prefix' variable.
+ Cookie adminsid created without the httponly flag
+ Uncommon header 'x-frame-options' found, with contents: SAMEORIGIN
+ Uncommon header 'referrer-policy' found, with contents: no-referrer
+ OSVDB-3092: /admin/: This might be interesting...
+ OSVDB-3092: /archive/: This might be interesting...
+ OSVDB-3092: /install/: This might be interesting...
+ OSVDB-3093: /admin/index.php: This might be interesting... has been seen in web logs from an unknown scanner.
+ Server leaks inodes via ETags, header found with file /images/, fields: 0x43 0x5ac3e49396000 
+ 6544 items checked: 0 error(s) and 14 item(s) reported on remote host
+ End Time:           2025-10-12 xx:xx:xx (GMT1) (8 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```




```bash
:~/M4tr1xExitDenied# gobuster dir -u http://exit-denied.thm/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -e -k
...
===============================================================
http://exit-denied.thm/images               (Status: 301) [Size: 319] [--> http://exit-denied.thm/images/]
http://exit-denied.thm/archive              (Status: 301) [Size: 320] [--> http://exit-denied.thm/archive/]
http://exit-denied.thm/login                (Status: 200) [Size: 241]
http://exit-denied.thm/files                (Status: 200) [Size: 240]
http://exit-denied.thm/uploads              (Status: 301) [Size: 320] [--> http://exit-denied.thm/uploads/]
http://exit-denied.thm/general              (Status: 200) [Size: 233]
http://exit-denied.thm/admin                (Status: 301) [Size: 318] [--> http://exit-denied.thm/admin/]
http://exit-denied.thm/ftp                  (Status: 200) [Size: 240]
http://exit-denied.thm/install              (Status: 301) [Size: 320] [--> http://exit-denied.thm/install/]
http://exit-denied.thm/cache                (Status: 301) [Size: 318] [--> http://exit-denied.thm/cache/]
http://exit-denied.thm/blue                 (Status: 200) [Size: 241]
http://exit-denied.thm/flag                 (Status: 200) [Size: 240]
http://exit-denied.thm/inc                  (Status: 301) [Size: 316] [--> http://exit-denied.thm/inc/]
http://exit-denied.thm/error                (Status: 200) [Size: 240]
http://exit-denied.thm/attachment           (Status: 200) [Size: 240]
http://exit-denied.thm/e-mail               (Status: 200) [Size: 240]
http://exit-denied.thm/secret               (Status: 200) [Size: 241]
http://exit-denied.thm/panel                (Status: 200) [Size: 241]
http://exit-denied.thm/administrator        (Status: 200) [Size: 241]
http://exit-denied.thm/change_password      (Status: 200) [Size: 240]
http://exit-denied.thm/server-status        (Status: 403) [Size: 280]
Progress: 218275 / 218276 (100.00%)
```

```bash
:~/M4tr1xExitDenied# gobuster dir -u http://exit-denied.thm/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -e -k -x php,txt,js,bak
...
===============================================================
http://exit-denied.thm/.php                 (Status: 403) [Size: 280]
http://exit-denied.thm/images               (Status: 301) [Size: 319] [--> http://exit-denied.thm/images/]
http://exit-denied.thm/contact.php          (Status: 200) [Size: 9936]
http://exit-denied.thm/rss.php              (Status: 302) [Size: 0] [--> syndication.php]
http://exit-denied.thm/login                (Status: 200) [Size: 241]
http://exit-denied.thm/archive              (Status: 301) [Size: 320] [--> http://exit-denied.thm/archive/]
http://exit-denied.thm/index.php            (Status: 200) [Size: 10588]
http://exit-denied.thm/files                (Status: 200) [Size: 240]
http://exit-denied.thm/search.php           (Status: 200) [Size: 14791]
http://exit-denied.thm/misc.php             (Status: 200) [Size: 0]
http://exit-denied.thm/uploads              (Status: 301) [Size: 320] [--> http://exit-denied.thm/uploads/]
http://exit-denied.thm/stats.php            (Status: 200) [Size: 10250]
http://exit-denied.thm/general              (Status: 200) [Size: 233]
http://exit-denied.thm/calendar.php         (Status: 200) [Size: 25885]
http://exit-denied.thm/global.php           (Status: 200) [Size: 98]
http://exit-denied.thm/admin                (Status: 301) [Size: 318] [--> http://exit-denied.thm/admin/]
http://exit-denied.thm/member.php           (Status: 302) [Size: 0] [--> index.php]
http://exit-denied.thm/online.php           (Status: 200) [Size: 9866]
http://exit-denied.thm/showthread.php       (Status: 200) [Size: 9002]
http://exit-denied.thm/report.php           (Status: 200) [Size: 9603]
http://exit-denied.thm/portal.php           (Status: 200) [Size: 11991]
http://exit-denied.thm/memberlist.php       (Status: 200) [Size: 31959]
http://exit-denied.thm/ftp                  (Status: 200) [Size: 240]
http://exit-denied.thm/css.php              (Status: 200) [Size: 0]
http://exit-denied.thm/install              (Status: 301) [Size: 320] [--> http://exit-denied.thm/install/]
http://exit-denied.thm/announcements.php    (Status: 200) [Size: 8832]
http://exit-denied.thm/polls.php            (Status: 200) [Size: 0]
http://exit-denied.thm/private.php          (Status: 200) [Size: 9684]
http://exit-denied.thm/cache                (Status: 301) [Size: 318] [--> http://exit-denied.thm/cache/]
http://exit-denied.thm/blue                 (Status: 200) [Size: 241]
http://exit-denied.thm/syndication.php      (Status: 200) [Size: 395]
http://exit-denied.thm/flag                 (Status: 200) [Size: 240]
http://exit-denied.thm/inc                  (Status: 301) [Size: 316] [--> http://exit-denied.thm/inc/]
http://exit-denied.thm/newreply.php         (Status: 200) [Size: 8830]
http://exit-denied.thm/error                (Status: 200) [Size: 240]
http://exit-denied.thm/printthread.php      (Status: 200) [Size: 8830]
http://exit-denied.thm/captcha.php          (Status: 200) [Size: 0]
http://exit-denied.thm/usercp.php           (Status: 200) [Size: 9772]
http://exit-denied.thm/attachment           (Status: 200) [Size: 240]
http://exit-denied.thm/attachment.php       (Status: 200) [Size: 8834]
http://exit-denied.thm/e-mail               (Status: 200) [Size: 240]
http://exit-denied.thm/newthread.php        (Status: 200) [Size: 8807]
http://exit-denied.thm/secret               (Status: 200) [Size: 241]
http://exit-denied.thm/panel                (Status: 200) [Size: 241]
http://exit-denied.thm/task.php             (Status: 200) [Size: 43]
http://exit-denied.thm/administrator        (Status: 200) [Size: 241]
http://exit-denied.thm/warnings.php         (Status: 200) [Size: 9603]
http://exit-denied.thm/reputation.php       (Status: 200) [Size: 8849]
http://exit-denied.thm/htaccess.txt         (Status: 200) [Size: 3088]
http://exit-denied.thm/moderation.php       (Status: 200) [Size: 9596]
http://exit-denied.thm/change_password      (Status: 200) [Size: 240]
http://exit-denied.thm/server-status        (Status: 403) [Size: 280]
http://exit-denied.thm/editpost.php         (Status: 200) [Size: 9603]
Progress: 1091375 / 1091380 (100.00%)
```



```bash
:~/M4tr1xExitDenied# dirsearch -u http://10.201.96.34 -r -R 3
```

<br>
<h1 align="center">Directory and File Enumeration<a id='6'></a></h1>

<p>

/admin/<br>
/admin/backups<br>
/admin/index.php<br>
/administrator<br>
/adminlogon<br>
/adminpanel<br>
/attachment.php<br>
/cache/<br>
/calendar.php<br>
/contact.php<br>
/e-mail<br>
/editpost.php
/error
/files
/flag
/ftp
/general
/global.php
/htaccess.txt
/images/
/inc/
/install/
/install/index.php?upgrade
/jscripts/
/login
/memberlist.php
/misc.php
/modcp.php
/newreply.php
/newthread.php
/online.php
/panel
/printthread.php
/private.php
/report.php
/reputation.php
/search.php
/secret
/stats.php
/uploads/
/usercp.php
/admin/inc
/admin/jscripts/
/admin/modules/
/archive/global.php
/install/images/
/install/resources
/jscripts/report.js
/jscripts/usercp.js
/admin/jscripts/admincp.js
/admin/jscripts/search.js
/admin/jscripts/users.js



/archive/
/inc/config.php
/inc/settings.php

/inc/3rdparty/
/inc/languages/

/install/images/
/inc/plugins
/admin/modules/config/
/admin/modules/forum/
/admin/modules/home/
/admin/modules/style/
/admin/modules/tools/
/admin/modules/user/
/admin/styles/default/</p>

<img width="1034" height="834" alt="image" src="https://github.com/user-attachments/assets/86c1373d-e180-4a66-a0aa-33933eaafa60" />

<br>
<br>
<br>

<img width="1034" height="835" alt="image" src="https://github.com/user-attachments/assets/71194c2f-7625-4f4a-82b8-7751a52fade6" />

<br>
<br>
<br>

<img width="1039" height="660" alt="image" src="https://github.com/user-attachments/assets/ef38bc27-67af-4c55-b229-defa828d8781" />

<br>
<br>
<br>






```bash
:~/M4tr1xExitDenied# apt install mariadb-client-core-10.3
```

```bash


```

```bash


```

```bash


```

```bash


```

```bash


```


```bash


```

```bash


```



Nmap done: 1 IP address (1 host up) scanned in 0.33 seconds
