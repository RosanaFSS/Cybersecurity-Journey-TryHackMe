<p align="center">April 14, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{343}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/e50c0c1e-db21-4aa6-bde4-60b1784e500b" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/4fe1cc18-807a-4b4f-8db2-7dc5f7c421ba"></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Surfer}}$$</h1>
<p align="center"><em>Surf some internal webpages to find the flag!</em>.<br>
It is classified as an easy-level CTF.<br>It is premium: only for subscribers.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/surfer">here</a>.</p>

<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/7f28836a-2869-46b1-be12-3c3b5dbe2cf5"> </p>

<br>
<br>

<h2>Task 1 . Prove Yourself </h2>

<p>[  Start Machine  ]</p>

<p> Woah, check out this radical app! Isn't it narly dude? We've been surfing through some webpages and we want to get you on board too! They said this application has some functionality that is only available for internal usage -- but if you catch the right wave, you can probably find the sweet stuff!<br><br>



Access this challenge by deploying both the vulnerable machine by pressing the green "Start Machine" button located within this task, and the TryHackMe AttackBox by pressing the  "Start AttackBox" button located at the top-right of the page.<br><br>

Navigate to the following URL using the AttackBox: HTTP://TargetIP<br><br>



Check out similar content on TryHackMe:<br>

- SSRF</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 1.1. <em>Uncover the flag on the hidden application page.</em><br><a id='1.1'></a>
>> <strong><code>flag{6255c55660e292cf0116c053c9937810}</code></strong><br>
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
Discovered<br><br>
  
- <code>Admin</code> and <code>Kate</code>.<br>
- <code>export2pdf tool</code> for <code>daily system reports</code>.<br>
- <code>Admin</code> is "using" default credentials.<br>
- there is an <code>internal server</code> up.</p>

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


<br>


<p>Navigated to <code>http://TargetIP/login.php</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/5183efb9-a093-4fca-bcfe-06e3c6c60b2d)

<br>

<p>Used <code>admin</code>:<code>admin</code>.<br><br>Clicked <code>Login</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/e3ddce7b-0957-4842-9943-275f43834861)

<br>

<p>Discovered <code>/internal/admin.php</code> and <code>172.17.0.2</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/7d567ee5-eb79-40e8-b79e-0c8d3b3592a9)



<br>

<p>Navigated to <code>http://TargetIP/internal/admin.php</code>.<br><br>Received the message: <code>This page can only be accesssed locally.</code></p>

<br>

![image](https://github.com/user-attachments/assets/42dfe4a7-5858-42bf-a7f1-bc1a061b7ad2)

<br>

<p>Returned the <code>admin</code>´s dashboard and scrolled down.<br><br>There is an <code>EXport to PDF</code> feature.</p>

<br>

![image](https://github.com/user-attachments/assets/351b774c-3e60-40cf-ba74-c675cc22a4bb)

<br>

<p>Clicked it and got something juicy.</p>

<br>

![image](https://github.com/user-attachments/assets/c5780393-0545-4d40-a5e7-62cd9ff4cadc)

<br>


<p>Got back to <code>http://TargetIP/index.php</code>.<br><br>
Launched <code>Burp Suite</code> and enabled <code>FoxyProxy</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/d8580e19-959d-4fde-8944-6b83dd65b00d)

<br>

<p>Clicked <code>Export to PDF</code>.</p>

<br>

<p>Analyzed what <code>Burp Suite</code> intercepted.</p>

<br>


![image](https://github.com/user-attachments/assets/819850c7-6bae-4cee-bbaa-c9437ce19a4f)

<br>

<p>Costumized the <code>url</code> to point to the path discovered.

<br>

![image](https://github.com/user-attachments/assets/05616d9e-daa5-484f-a0ba-69f996d3f93b)

<br>

<p>Clicked <code>Forward</code> and checked the web browser.</p>

<br>
<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center">
<img width="900px" src="https://github.com/user-attachments/assets/2e3c4dc9-ea6e-4ac3-8bc4-f04f84eb9e07"><br>
<img width="900px" src="https://github.com/user-attachments/assets/6c763410-e9da-4b5c-8d6e-cf50c70856bf"></p>


<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>


<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |Global        | Brazil       | Global      | Brazil     |          | Completed |           |
| April 14, 2025    | 343      |     286ᵗʰ    |        7ᵗʰ   |    233ʳᵈ    |     3ʳᵈ    |  93,443  |       662 |   59      |

</div>

<br>


<p align="center"> Global All Time: 286ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/6ba7c668-85e1-4de8-b0b5-230d60f1d792"> </p>

<p align="center"> Brazil All Time: 7ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/7d0e07cf-2ec4-4ea0-aa38-c25b864ae991"> </p>

<p align="center"> Global monthly: 233ʳᵈ<br><br><img width="900px" src="https://github.com/user-attachments/assets/37aa28b4-c266-44d3-9f2c-d3132d4bc831"> </p>

<p align="center"> Brazil monthly: 3ʳᵈ<br><br><img width="900px" src="https://github.com/user-attachments/assets/8a106b00-bb1e-4b1c-b7da-0361c297ea27"> </p>


<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/cmnatic">cmnatic</a> for investing your time and effort to develop this challenge so that I could sharpen my skills!</p> 
