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


<h3>Directory Enumeration</h3>
<p>1.2. <em>What is the 403/forbidden web page?</em> Hint : Try directory enumeration.<br>
<code>debug</code></p>

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

<p>

<h3>http://crylo.thm/debug</h3>
  
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


<p>
  
- Launched Burp Suite.<br>

- Clicked Login.<br>

- Enabled FoxyProxy in the right upper corner of the web browser.<br>

- Tried to log in with the credentials admin:admin.<br>

- Right-clicked over the Burp Suite´s Request panel, defined the name request.txt, and clicked Save.</p>
