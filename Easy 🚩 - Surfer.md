<p align="center">April 14, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{343}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/01dc672d-a7c9-425f-b466-64c242f8042c" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/4fe1cc18-807a-4b4f-8db2-7dc5f7c421ba"></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Surfer}}$$</h1>
<p align="center"><em>Surf some internal webpages to find the flag!</em>.<br>
It is classified as an easy-level CTF.<br>It is premium: only for subscribers.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/surfer">here</a>.</p>

<p align="center"> <img width="900px" src=""> </p>

<br>
<br>

<h2>Task 1 . Prove Yourself </h2>

<p>[  Start Machine  ]</p>

<p>
<em>Also credit goes to Sq00ky for the super special idea found in the initial foothold stage (not going to give any
spoilers away!)</em><br>

Please allow 3-5 minutes for the box to fully deploy once you hit the "Deploy" button.<br>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 1.1. <em>User 1 Flag.</em>Hint : <em>You're going to want to write a Python script for this. 'zA' = 'a'</em><br><a id='1.1'></a>
>> <strong><code>9184177ecaa83073cbbf36f1414cc029</code></strong><br>
<p></p>

<br>
<br>

<p>Used <code>nmap</code>.<br>
Discovered:<br>
  
-  2 ports open:  <code>22/ssh</code> and <code>80/http</code>.<br>
-  <code>http-robots.txt: 1 disallowed entry </code>.<br>
-  <code>/backup/chat.txt</code></br>
-  <code>/login.php</code></p>


```bash
:~/Surfer# nmap -sC -sV -sS -Pn -A -p- -T4 TargetIP
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
| http-robots.txt: 1 disallowed entry 
|_/backup/chat.txt
|_http-server-header: Apache/2.4.38 (Debian)
| http-title: 24X7 System+
|_Requested resource was /login.php
...
```

<br>

<p>Added the <code>TargetIP</code> and a domain name in <code>/etc/hosts</code>.</p>

<br>

```bash
~/Surfer# echo "TargetIP surfer.thm" | tee -a /etc/hosts
TargetIP surfer.thm
:~/Surfer# 
```

<br>

<p>Checked the content in <code>http://TargeIP/robots.txt</code>.<br><br>
Confirmed <code>/backup/chat.txt</code> dicovered in the <code>nmap</code> scan.</p>

<br>

```bash
:~/Surfer# curl http://surfer.thm/robots.txt
User-Agent: *
Disallow: /backup/chat.txt
:~/Surfer# 
```

<br>
<p>Checked the content in <code>http://TargeIP/backup/chat.txt</code>.<br><br>
Discovered <code>Admin</code>, <code>Kate</code>, <code>export2pdf tool</code> for <code>daily system reports</code>code> and <code>username>/code<:<code>password</code>covered in the <code>.</p>

<br>

```bash
:~/Surfer# curl http://surfer.thm/backup/chat.txt

Admin: I have finished setting up the new export2pdf tool.
Kate: Thanks, we will require daily system reports in pdf format.
Admin: Yes, I am updated about that.
Kate: Have you finished adding the internal server.
Admin: Yes, it should be serving flag from now.
Kate: Also Don't forget to change the creds, plz stop using your username as password.
Kate: Hello.. ?
:~/Surfer# 
```

