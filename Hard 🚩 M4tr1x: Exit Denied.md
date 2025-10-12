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
<h1 align="center">Directory and File Enumeration<a id='1'></a></h1>

```bash
xx.xxx.xx.xx exitdenied.thm
```

<br>
<h1 align="center">Port Scanning<a id='2'></a></h1>
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
:~/M4tr1xExitDenied# nmap -sT exitdenied.thm
...
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
3306/tcp open  mysql
...
```

```bash
:~/M4tr1xExitDenied# nmap -sC -sV -Pn -p22,80,3306 -T4  exitdenied.thm
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
|   Some Capabilities: ConnectWithDatabase, SupportsTransactions, Speaks41ProtocolOld, IgnoreSigpipes, Support41Auth, SupportsLoadDataLocal, FoundRows, SupportsCompression, DontAllowDatabaseTableColumn, Speaks41ProtocolNew, InteractiveClient, ODBCClient, LongColumnFlag, IgnoreSpaceBeforeParenthesis, SupportsMultipleStatments, SupportsMultipleResults, SupportsAuthPlugins
|   Status: Autocommit
|   Salt: $kqv}1w)a0h@Bks"J1T4
|_  Auth Plugin Name: mysql_native_password
```

<br>
<h1 align="center">Web Vulberability Scanning<a id='3'></a></h1>

```bash
:~/M4tr1xExitDenied# nikto -h exitdenied.thm

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

<br>
<h1 align="center">Directory and File Enumeration<a id='4'></a></h1>

```bash
:~/M4tr1xExitDenied# gobuster dir -u http://exitdenied.thm/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -e -k -q
http://exitdenied.thm/images               (Status: 301) [Size: 317] [--> http://exitdenied.thm/images/]
http://exitdenied.thm/login                (Status: 200) [Size: 241]
http://exitdenied.thm/archive              (Status: 301) [Size: 318] [--> http://exitdenied.thm/archive/]
http://exitdenied.thm/files                (Status: 200) [Size: 240]
http://exitdenied.thm/uploads              (Status: 301) [Size: 318] [--> http://exitdenied.thm/uploads/]
http://exitdenied.thm/general              (Status: 200) [Size: 233]
http://exitdenied.thm/admin                (Status: 301) [Size: 316] [--> http://exitdenied.thm/admin/]
http://exitdenied.thm/ftp                  (Status: 200) [Size: 240]
http://exitdenied.thm/install              (Status: 301) [Size: 318] [--> http://exitdenied.thm/install/]
http://exitdenied.thm/cache                (Status: 301) [Size: 316] [--> http://exitdenied.thm/cache/]
http://exitdenied.thm/blue                 (Status: 200) [Size: 241]
http://exitdenied.thm/flag                 (Status: 200) [Size: 240]
http://exitdenied.thm/inc                  (Status: 301) [Size: 314] [--> http://exitdenied.thm/inc/]
http://exitdenied.thm/error                (Status: 200) [Size: 240]
http://exitdenied.thm/attachment           (Status: 200) [Size: 240]
http://exitdenied.thm/e-mail               (Status: 200) [Size: 240]
http://exitdenied.thm/secret               (Status: 200) [Size: 241]
http://exitdenied.thm/panel                (Status: 200) [Size: 241]
http://exitdenied.thm/administrator        (Status: 200) [Size: 241]
http://exitdenied.thm/change_password      (Status: 200) [Size: 240]
http://exitdenied.thm/server-status        (Status: 403) [Size: 279]
```

<br>
<br>
<br>
<p align="center">exitdenied.thm/general</p>

<img width="1137" height="726" alt="image" src="https://github.com/user-attachments/assets/9998cb7e-f2ee-42d5-93d4-72d9721b3c13" />


<br>
<br>
<br>
<p align="center">exitdenied.thm/admin</p>

<img width="1143" height="473" alt="image" src="https://github.com/user-attachments/assets/340c43f6-4d5f-4484-950d-6c38429928ef" />



<img width="1195" height="363" alt="image" src="https://github.com/user-attachments/assets/6628ad39-54a2-4e53-922f-da6dd9ac33fd" />

<br>
<br>
<br>
<p align="center">exitdenied.thm/flag & exitdenied.thm/ftp</p>

<img width="818" height="805" alt="image" src="https://github.com/user-attachments/assets/7f7282a3-9e2d-4a64-9ad8-08423f11a8a4" />

<br>
<br>
<br>
<p align="center">exitdenied.thm/blue</p>

<img width="422" height="716" alt="image" src="https://github.com/user-attachments/assets/a589382b-638e-419a-9a02-a08c0f5b125a" />



```bash
:~/M4tr1xExitDenied# gobuster dir -u http://exitdenied.thm/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -e -k -q -x php,txt,js,bak
http://exitdenied.thm/.php                 (Status: 403) [Size: 279]
http://exitdenied.thm/images               (Status: 301) [Size: 317] [--> http://exitdenied.thm/images/]
http://exitdenied.thm/index.php            (Status: 200) [Size: 10588]
http://exitdenied.thm/contact.php          (Status: 200) [Size: 9936]
http://exitdenied.thm/rss.php              (Status: 302) [Size: 0] [--> syndication.php]
http://exitdenied.thm/search.php           (Status: 200) [Size: 14791]
http://exitdenied.thm/login                (Status: 200) [Size: 241]
http://exitdenied.thm/archive              (Status: 301) [Size: 318] [--> http://exitdenied.thm/archive/]
http://exitdenied.thm/files                (Status: 200) [Size: 240]
http://exitdenied.thm/misc.php             (Status: 200) [Size: 0]
http://exitdenied.thm/uploads              (Status: 301) [Size: 318] [--> http://exitdenied.thm/uploads/]
http://exitdenied.thm/stats.php            (Status: 200) [Size: 10250]
http://exitdenied.thm/calendar.php         (Status: 200) [Size: 25885]
http://exitdenied.thm/general              (Status: 200) [Size: 233]
http://exitdenied.thm/global.php           (Status: 200) [Size: 98]
http://exitdenied.thm/admin                (Status: 301) [Size: 316] [--> http://exitdenied.thm/admin/]
http://exitdenied.thm/online.php           (Status: 200) [Size: 9858]
http://exitdenied.thm/member.php           (Status: 302) [Size: 0] [--> index.php]
http://exitdenied.thm/showthread.php       (Status: 200) [Size: 9002]
http://exitdenied.thm/report.php           (Status: 200) [Size: 9603]
http://exitdenied.thm/portal.php           (Status: 200) [Size: 11991]
http://exitdenied.thm/memberlist.php       (Status: 200) [Size: 31959]
http://exitdenied.thm/ftp                  (Status: 200) [Size: 240]
http://exitdenied.thm/css.php              (Status: 200) [Size: 0]
http://exitdenied.thm/install              (Status: 301) [Size: 318] [--> http://exitdenied.thm/install/]
http://exitdenied.thm/announcements.php    (Status: 200) [Size: 8832]
http://exitdenied.thm/polls.php            (Status: 200) [Size: 0]
http://exitdenied.thm/private.php          (Status: 200) [Size: 9684]
http://exitdenied.thm/cache                (Status: 301) [Size: 316] [--> http://exitdenied.thm/cache/]
http://exitdenied.thm/blue                 (Status: 200) [Size: 241]
http://exitdenied.thm/syndication.php      (Status: 200) [Size: 395]
http://exitdenied.thm/flag                 (Status: 200) [Size: 240]
http://exitdenied.thm/inc                  (Status: 301) [Size: 314] [--> http://exitdenied.thm/inc/]
http://exitdenied.thm/newreply.php         (Status: 200) [Size: 8830]
http://exitdenied.thm/error                (Status: 200) [Size: 240]
http://exitdenied.thm/printthread.php      (Status: 200) [Size: 8830]
http://exitdenied.thm/captcha.php          (Status: 200) [Size: 0]
http://exitdenied.thm/usercp.php           (Status: 200) [Size: 9772]
http://exitdenied.thm/attachment           (Status: 200) [Size: 240]
http://exitdenied.thm/attachment.php       (Status: 200) [Size: 8834]
http://exitdenied.thm/e-mail               (Status: 200) [Size: 240]
http://exitdenied.thm/newthread.php        (Status: 200) [Size: 8807]
http://exitdenied.thm/secret               (Status: 200) [Size: 241]
http://exitdenied.thm/task.php             (Status: 200) [Size: 43]
http://exitdenied.thm/panel                (Status: 200) [Size: 241]
http://exitdenied.thm/administrator        (Status: 200) [Size: 241]
http://exitdenied.thm/warnings.php         (Status: 200) [Size: 9603]
http://exitdenied.thm/reputation.php       (Status: 200) [Size: 8849]
http://exitdenied.thm/htaccess.txt         (Status: 200) [Size: 3088]
http://exitdenied.thm/moderation.php       (Status: 200) [Size: 9596]
http://exitdenied.thm/moderation.php       (Status: 200) [Size: 9596]
http://exitdenied.thm/change_password      (Status: 200) [Size: 240]
http://exitdenied.thm/server-status        (Status: 403) [Size: 279]
http://exitdenied.thm/editpost.php         (Status: 200) [Size: 9603]
```

<img width="1191" height="831" alt="image" src="https://github.com/user-attachments/assets/a6ed2d94-9bdf-4a51-9d90-9dbfa9300659" />

<br>
<br>
<br>

```bash
:~/M4tr1xExitDenied# gobuster dir -u http://exitdenied.thm/inc/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -e -k -q -x php,txt,js,bak
http://exitdenied.thm/inc/.php                 (Status: 403) [Size: 279]
http://exitdenied.thm/inc/plugins              (Status: 301) [Size: 322] [--> http://exitdenied.thm/inc/plugins/]
http://exitdenied.thm/inc/languages            (Status: 301) [Size: 324] [--> http://exitdenied.thm/inc/languages/]
http://exitdenied.thm/inc/config.php           (Status: 200) [Size: 0]
http://exitdenied.thm/inc/settings.php         (Status: 200) [Size: 0]
http://exitdenied.thm/inc/functions.php        (Status: 200) [Size: 0]
http://exitdenied.thm/inc/init.php             (Status: 200) [Size: 98]
http://exitdenied.thm/inc/tasks                (Status: 301) [Size: 320] [--> http://exitdenied.thm/inc/tasks/]
http://exitdenied.thm/inc/3rdparty             (Status: 301) [Size: 323] [--> http://exitdenied.thm/inc/3rdparty/]
```

<img width="1264" height="192" alt="image" src="https://github.com/user-attachments/assets/76bd5c7f-f286-4293-acc3-c2b5f580f707" />

<br>
<br>
<br>

```bash
:~/M4tr1xExitDenied# gobuster dir -u http://exitdenied.thm/inc/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -e -k -q -x php,txt,js,bak
http://exitdenied.thm/inc/.php                 (Status: 403) [Size: 279]
http://exitdenied.thm/inc/plugins              (Status: 301) [Size: 322] [--> http://exitdenied.thm/inc/plugins/]
http://exitdenied.thm/inc/languages            (Status: 301) [Size: 324] [--> http://exitdenied.thm/inc/languages/]
http://exitdenied.thm/inc/config.php           (Status: 200) [Size: 0]
http://exitdenied.thm/inc/settings.php         (Status: 200) [Size: 0]
http://exitdenied.thm/inc/functions.php        (Status: 200) [Size: 0]
http://exitdenied.thm/inc/init.php             (Status: 200) [Size: 98]
http://exitdenied.thm/inc/tasks                (Status: 301) [Size: 320] [--> http://exitdenied.thm/inc/tasks/]
http://exitdenied.thm/inc/3rdparty             (Status: 301) [Size: 323] [--> http://exitdenied.thm/inc/3rdparty/]
```


```bash
:~/M4tr1xExitDenied# dirsearch -u http://10.201.96.34 -r -R 3
```

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


http://10.201.54.83/memberlist.php?sort=regdate&order=ascending&perpage=20&page=2


<img width="1121" height="509" alt="image" src="https://github.com/user-attachments/assets/8ba5478f-65de-4662-a830-8437f189d835" />


Register > I Agree


<img width="1117" height="610" alt="image" src="https://github.com/user-attachments/assets/dda675d8-55fa-4ae4-b4ec-f7b9017ec1ed" />


<img width="1105" height="334" alt="image" src="https://github.com/user-attachments/assets/1acf84f8-0adf-4232-87bb-7703f378646f" />

<img width="1114" height="332" alt="image" src="https://github.com/user-attachments/assets/ee093acf-77be-4d7b-b0e1-40c8b57eda5d" />


Find All Posts

<img width="1118" height="648" alt="image" src="https://github.com/user-attachments/assets/5e63b000-a23e-429d-9540-b6950bf371e4" />



<img width="1119" height="461" alt="image" src="https://github.com/user-attachments/assets/97b543f7-481f-49fb-897c-f9143ad517ee" />



Thread: Bug Bounty Program

<img width="1115" height="676" alt="image" src="https://github.com/user-attachments/assets/1ecde1b4-4239-4e0b-923b-4fc2705b5983" />

/bugbountyHQ

<img width="1125" height="608" alt="image" src="https://github.com/user-attachments/assets/16f477b5-f94e-4eee-bb20-71551bb91168" />

Bug Bounty Report Formm

<img width="1128" height="361" alt="image" src="https://github.com/user-attachments/assets/285daa1d-b6ed-4265-b8b3-14b05cc76877" />


Page Source

<img width="1117" height="297" alt="image" src="https://github.com/user-attachments/assets/4af2151d-b442-4917-8fe2-0e17c9c9cf21" />


/devBuilds/modManagerv2.plugin

<p>1.4. What is the name of that interesting plugin?<br>
<code>modManagerv2</code></p>

<img width="1132" height="750" alt="image" src="https://github.com/user-attachments/assets/138093bd-2764-433e-a838-b5fe5aee131b" />


/*
if (!defined('IN_MYBB'))
{
    die('Direct initialization of this file is not allowed.<br /><br />Please make sure IN_MYBB is defined.');
}

global $mybb;

require_once MYBB_ROOT . "inc/tools/manage/settings.php";
require_once MYBB_ROOT . "inc/tools/manage/settings.php";
require_once MYBB_ROOT . "inc/tools/manage/SQL/settings.php";
require_once MYBB_ROOT . "inc/tools/manage/SQL/settings.php";
$sql_p = file_get_contents('inc/tools/manage/SQL/p.txt'); //read SQL password from p.txt


// All pages
$plugins->add_hook('global_start', 'modManager_load_library');

// 1.8 has jQuery, not Prototype
if ($mybb->version_code >= 1700)
{
    $plugins->add_hook('global_intermediate', 'modManager_load_plugin_hook_any');
}
else
{
    $plugins->add_hook('global_start', 'modManager_load_plugin_hook_any');
}

// No permission page
$plugins->add_hook('no_permission', 'modManager_plugin_hook_error_no_permission');

// Callback handler
$plugins->add_hook('global_end', 'modManager_login_callback');

// Social Link
$plugins->add_hook('usercp_profile_start', 'modManager_login_social_link', 25);

/*---------------------------------------------------*/
//!!!!!!SQL LOGIN for modManager (needed for reading login_keys for user migration)
define('localhost', 'localhost:3306');
//mysql connect using user 'mod' and password from 'sql_p varirable'
$db = mysql_connect('localhost','mod',$sql_p);


/*---------------------------------------------------*/


/showteam.php


<img width="1113" height="693" alt="image" src="https://github.com/user-attachments/assets/5515882f-f249-4a45-a0af-f134c2945a72" />




<p>1.6. Interesting... I believe only the keymaker could help you crack it. Find him. Where did he tell you to go to?<br>
<code>/0100101101100101011110010110110101100001011010110110010101110010</code></p>

reportPanel.php


<img width="1119" height="340" alt="image" src="https://github.com/user-attachments/assets/1d447b72-b9e3-4160-bc50-e2c862c14370" />


Page Source

<img width="1127" height="714" alt="image" src="https://github.com/user-attachments/assets/00556026-4e7c-40fd-80e7-57070a618f69" />


Keymaker message:
1 16 5 18 13 21 20 1 20 9 15 14 15 6 15 14 12 25 20 8 5 5 14 7 12 9 19 8 12 5 20 20 5 18 19 23 9 12 12 15 16 5 14 20 8 5 12 15 3 11 19

1 4 4 18 5 19 19: /0100101101100101011110010110110101100001011010110110010101110010

<p>1.7. Did you try cracking the file?<br>
<code>/0100101101100101011110010110110101100001011010110110010101110010</code></p>

<p>

- https://planetcalc.com/4884/</p>


<img width="1429" height="646" alt="image" src="https://github.com/user-attachments/assets/f4dc860c-fea4-434a-b07f-42c13a6a8d33" />


a p e r m u t a t i o n o f o n l y t h e e n g l i s h l e t t e r s w i l l o p e n t h e l o c k s



<img width="1414" height="489" alt="image" src="https://github.com/user-attachments/assets/71168eba-bad7-4008-97fa-cf23579f46aa" />

a d d r e s s


http://10.201.54.83/0100101101100101011110010110110101100001011010110110010101110010


<img width="1112" height="273" alt="image" src="https://github.com/user-attachments/assets/b8eb7ad0-bbab-434d-a291-8987570475e1" />



<img width="1123" height="386" alt="image" src="https://github.com/user-attachments/assets/753ca216-26f8-4c7b-ab4b-e31dc7cc75f3" />





<img width="1113" height="666" alt="image" src="https://github.com/user-attachments/assets/0914887a-8ca2-430b-a468-8ea19711681a" />






PalacerKing



<img width="1119" height="509" alt="image" src="https://github.com/user-attachments/assets/8f191e6c-6da2-4e7e-bcfa-3b67b732ffa7" />



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
