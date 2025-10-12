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
...
```

<img width="1195" height="363" alt="image" src="https://github.com/user-attachments/assets/6628ad39-54a2-4e53-922f-da6dd9ac33fd" />

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

<br>
<br>
<br>
<p align="center">exitdenied.thm/install</p>

<img width="1145" height="386" alt="image" src="https://github.com/user-attachments/assets/7eb1bbd5-e75d-47d9-b5c1-6ace926d1c32" />

<br>
<br>
<br>
<p align="center">exitdenied.thm/flag & exitdenied.thm/ftp & exitdenied.thm/error & exitdenied.thm/attachment & exitdenied.thm/e-mail & exitdenied.thm/change_password</p>

<img width="818" height="805" alt="image" src="https://github.com/user-attachments/assets/7f7282a3-9e2d-4a64-9ad8-08423f11a8a4" />

<br>
<br>
<br>
<p align="center">exitdenied.thm/blue & exitdenied.thm/secret & exitdenied.thm/panel & & exitdenied.thm/administrator</p>

<img width="422" height="716" alt="image" src="https://github.com/user-attachments/assets/a589382b-638e-419a-9a02-a08c0f5b125a" />

<br>
<br>
<br>

```bash
:~/M4tr1xExitDenied# gobuster dir -u http://exitdenied.thm/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -e -k -q -x php,txt,js,bak
...
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
...
http://exitdenied.thm/editpost.php         (Status: 200) [Size: 9603]
```

<img width="1191" height="831" alt="image" src="https://github.com/user-attachments/assets/a6ed2d94-9bdf-4a51-9d90-9dbfa9300659" />

<br>
<br>
<br>
<p align="center">exitdenied.thm/index.php</p>

<img width="1137" height="770" alt="image" src="https://github.com/user-attachments/assets/b424c517-4b6f-48ac-b7b3-8cfa7d438dd2" />

<br>
<br>
<br>
<p align="center">exitdenied.thm/memberlist.php</p>

<img width="1129" height="387" alt="image" src="https://github.com/user-attachments/assets/0ffe1ac7-de15-4fa2-a192-c8a217e6dfab" />

<br>
<br>
<br>
<p align="center">exitdenied.thm/showteam.php<br>Administrator : bigpaul<br>Moderators: ArnoldBagger, BlackCat, BlueMan, DotHaxer, DrBert, Jackwom, PalaceKing<br>Super Moderator: BlackCat</p>

<img width="1133" height="807" alt="image" src="https://github.com/user-attachments/assets/7fc28b2a-087c-4318-b57d-db85fa82e43b" />

<br>
<br>
<br>
<p align="center">Created <code>usernames.txt</code></p>

```bash
bigpaul
ArnoldBagger
BlackCat
BlueMan
DotHaxer
DrBert
Jackwom
PalaceKing
```

<br>
<p align="center">exitdenied.thm/memberlist.php?action=register > I Agree > answer question > ...</p>

<img width="1123" height="754" alt="image" src="https://github.com/user-attachments/assets/96ab918a-0a85-4be1-9f1a-33c782a4e4b5" />

<br>
<br>
<br>

<img width="1129" height="828" alt="image" src="https://github.com/user-attachments/assets/147bea97-43e3-432d-9110-4d48b5ca8482" />

<br>
<br>
<br>
<p align="center">Team > bigpaul > Threads > Bug Bounty Program<br>bugbountyHQ</p>

<img width="1134" height="754" alt="image" src="https://github.com/user-attachments/assets/65d6391a-ceaa-4115-9b69-4dd0932d4645" />

<br>
<br>
<br>
<p>1.2.Where did that white rabbit lead you to?<br>
<code>/resportPanel.php</code></p>
<br>
<p align="center">exitdenied.thm/bugbountyHQ<br>/reportPanel.php</p>

<img width="1130" height="458" alt="image" src="https://github.com/user-attachments/assets/4e2d8962-0e50-4a36-8164-3ece84187631" />

<br>
<br>
<br>

<img width="1132" height="473" alt="image" src="https://github.com/user-attachments/assets/79e7f8af-16f6-4046-af76-5ef0b16ac909" />

<br>
<br>
<br>
<p align="center">exitdenied.thm/reportPanel.php<br><br>deleted mod posts with attachments can still be accessed</p>

<img width="1131" height="299" alt="image" src="https://github.com/user-attachments/assets/0cfda2f2-4d63-49e4-aab4-6bd4a6208d13" />

<br>
<br>
<br>
<p align="center">3 in 5 online users use weak passwords such as: password123, Password123, crabfish, linux123, secret, piggybank, windowsxp, starwars, qwerty123, qwerty, supermario, Luisfactor05, james123, ect</p>

<img width="1122" height="184" alt="image" src="https://github.com/user-attachments/assets/91e619bd-f8ad-4694-8ec7-2fe2c67bfca8" />

<br>
<br>
<br>
<p align="center">exitdenied.thm/reportPanel.php page source/p>

<img width="1129" height="258" alt="image" src="https://github.com/user-attachments/assets/1a5016d1-191c-41ac-9a4c-1881e44eb5a5" />

<br>
<br>
<br>

```bash
Keymaker message:
1 16 5 18 13 21 20 1 20 9 15 14 15 6 15 14 12 25 20 8 5 5 14 7 12 9 19 8 12 5 20 20 5 18 19 23 9 12 12 15 16 5 14 20 8 5 12 15 3 11 19

1 4 4 18 5 19 19: /0100101101100101011110010110110101100001011010110110010101110010
```

<br>
<p align="center">Created <code>passwords.txt</code></p>

```bash
password123
Password123
crabfish
linux123
secret
piggybank
windowsxp
starwars
qwerty123
qwerty
supermario
Luisfactor05
james123
```


<br>
<p>1.3. Determine which vulnerability is the most appropriate at this time.<br>
<code>No answer needed</code></p>
<br>

<img width="1130" height="167" alt="image" src="https://github.com/user-attachments/assets/62a7ae94-d0c8-4756-82ba-88a91c2112a9" />

<br>
<br>
<br>
<p align="center">anti-bot registration questions repeats using pseudo random method - can be predicted using frequency analysis of responses</p>

<img width="1126" height="37" alt="image" src="https://github.com/user-attachments/assets/e310c6e0-e493-45ac-9aac-8f20a6e0ec9b" />

<br>
<br>
<br>
<p align="center">IP history plugin records users IP & User-Agent history. user Agent would not be sanitized so xss possible for <code>acp</code> page.</p>

<img width="1123" height="296" alt="image" src="https://github.com/user-attachments/assets/a1731731-27e9-42d8-a444-ee13015a007b" />
    
<br>
<br>
<br>
<p align="center">xss possible because plugin does not sanatize passed data (AR4)</p>

<img width="1118" height="31" alt="image" src="https://github.com/user-attachments/assets/e8750aeb-209d-41f5-a3d7-3df7f482f096" />

<br>
<br>
<br>
<p align="center">Launched Burp Suite, and enabled FoxyProxy.<br>Captured the login of the account registered previously. Sent to intruder. <code>Start attack</code>.</p>


<img width="1171" height="303" alt="image" src="https://github.com/user-attachments/assets/deb0fdea-e141-4351-a1ff-27cea6181791" />

<br>
<br>
<br>

<p align="center">PalacerKing</p>

<img width="1119" height="608" alt="image" src="https://github.com/user-attachments/assets/84461095-bcbe-436a-b1c3-4da16382199e" />
<br>
<br>
<br>

<p align="center">PalacerKing > User CP > Messenger > Sent Items > new plugin test</p>

<img width="1060" height="365" alt="image" src="https://github.com/user-attachments/assets/a53109a2-eb25-46ae-9719-d0df7a9987a2" />

<br>
<br>
<br>

<p align="center">ArnoldBagger > User CP > Messenger > Sent Items</p>

<img width="1118" height="571" alt="image" src="https://github.com/user-attachments/assets/27b29184-a959-45d5-9380-25aae5d17d74" />

<br>
<br>
<br>

<img width="1128" height="614" alt="image" src="https://github.com/user-attachments/assets/b5190b6b-82a3-4ff2-984f-0875c2f77eac" />

<br>
<br>
<br>
<p>1.4. What is the name of that interesting plugin?<br>
<code>modManagerv2</code></p>
<br>
<p align="center">/devBuilds</p>

<img width="1129" height="372" alt="image" src="https://github.com/user-attachments/assets/bca3dcd5-8fda-4d20-a180-aba23ca5e8d0" />

<br>
<br>
<br>

<img width="1118" height="316" alt="image" src="https://github.com/user-attachments/assets/f75ef256-7556-411c-b707-0456faf3d745" />

<br>
<br>
<br>
<p align="center">inc/tools/manage/SQL/p.txt'</p>

<img width="1124" height="477" alt="image" src="https://github.com/user-attachments/assets/594e6dc6-5666-46d3-90fa-709265ce8803" />

<br>
<br>
<br>
<p>1.5. What is the name of that encrypted file that you found?<br>
<code>p.txt.gpg</code></p>
<br>


```bash
:~/M4tr1xExitDenied# wget http://exitdenied.thm/devBuilds/p.txt.gpg
...
p.txt.gpg                            100%[=====================================================================>]     104  --.-KB/s    in 0s      

2025-10-12 xx:xx:xx (13.7 MB/s) - \u2018p.txt.gpg\u2019 saved [104/104]
```

```bash
:~/M4tr1xExitDenied# wget http://exitdenied.thm/devBuilds/modManagerv2.plugin
...

2025-10-12xx:xx:xx (624 MB/s) - \u2018modManagerv2.plugin\u2019 saved [5768/5768]
```

<br>
<br>
<br>
<p>1.6. Interesting... I believe only the keymaker could help you crack it. Find him. Where did he tell you to go to?<br>
<code>/0100101101100101011110010110110101100001011010110110010101110010</code></p>
<br>
<p align="center">exitdenied.thm/reportPanel.php page source/p>

```bash
Keymaker message:
1 16 5 18 13 21 20 1 20 9 15 14 15 6 15 14 12 25 20 8 5 5 14 7 12 9 19 8 12 5 20 20 5 18 19 23 9 12 12 15 16 5 14 20 8 5 12 15 3 11 19

1 4 4 18 5 19 19: /0100101101100101011110010110110101100001011010110110010101110010
```

<br>
<p>1.7. Did you try cracking the file?<br>
<code>No answer needed</code></p>
<br>

<p align="center">https://planetcalc.com/4884/</p>

<img width="1429" height="646" alt="image" src="https://github.com/user-attachments/assets/f4dc860c-fea4-434a-b07f-42c13a6a8d33" />

<br>
<br>
<br>

```bash
a p e r m u t a t i o n o f o n l y t h e e n g l i s h l e t t e r s w i l l o p e n t h e l o c k s
```

<br>

<img width="1414" height="489" alt="image" src="https://github.com/user-attachments/assets/71168eba-bad7-4008-97fa-cf23579f46aa" />

<br>
<br>
<br>

```bash
a d d r e s s
```

<p align="center">/0100101101100101011110010110110101100001011010110110010101110010</p>

<img width="1112" height="273" alt="image" src="https://github.com/user-attachments/assets/b8eb7ad0-bbab-434d-a291-8987570475e1" />

<br>
<br>
<br>

<p align="center">view-source:http://exitdenied.thm/0100101101100101011110010110110101100001011010110110010101110010<br>
ofqxvg</p>

<img width="1133" height="327" alt="image" src="https://github.com/user-attachments/assets/becc0e87-e66e-4d85-b244-a8ec0f0931d3" />

<br>
<br>
<br>




<p align="center">Launched Burp Suite, and enabled FoxyProxy.<br>Captured the login of the account registered previously. Sent to intruder. <code>Start attack</code>.</p>


```bash
:~/M4tr1xExitDenied# gobuster dir -u http://exitdenied.thm/admin/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -e -k -q -x php,txt,js,bak
...
http://exitdenied.thm/admin/index.php            (Status: 200) [Size: 1971]
http://exitdenied.thm/admin/modules              (Status: 301) [Size: 324] [--> http://exitdenied.thm/admin/modules/]
http://exitdenied.thm/admin/styles               (Status: 301) [Size: 323] [--> http://exitdenied.thm/admin/styles/]
http://exitdenied.thm/admin/inc                  (Status: 301) [Size: 320] [--> http://exitdenied.thm/admin/inc/]
http://exitdenied.thm/admin/backups              (Status: 301) [Size: 324] [--> http://exitdenied.thm/admin/backups/]
```

<br>
<br>
<br>
<p align="center">exitdenied.thm/admin/index.php<br>../member.php?action=lostpw<br>mybb.com<br>my_post_key = 887e9104f978065926ec023454066b03</p>

<img width="1143" height="504" alt="image" src="https://github.com/user-attachments/assets/0d8ecbdc-f740-4243-a38c-f0648c2c4b05" />

<br>
<br>
<br>

<img width="1142" height="733" alt="image" src="https://github.com/user-attachments/assets/cfd0d570-86c1-4862-9ebd-f83f6f7c8be5" />

<br>
<br>
<br>

```bash
:~/M4tr1xExitDenied# gobuster dir -u http://exitdenied.thm/inc/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -e -k -q -x php,txt,js,bak
...
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



