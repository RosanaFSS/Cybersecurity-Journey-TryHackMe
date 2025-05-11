<p align="center">May 11, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{370}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/62cf4572-71af-43ed-898e-31c0887632ce" alt="streak"></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Oh My WebServer}}$$</h1>
<p align="center"><em>Can you root me?</em>.<br>
It is classified as a medium-level CTF.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/ohmyweb"</a>.</p>

<p align="center"> <img width="1000px" src=""> </p>

<br>
<br>

<h2>Task 1 . oh-My-Webserver</h2>

<h3>Hit me!</h3>
<p>Deploy the machine attached to this task and happy hacking!</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 1.1. <em>What is the user flag?</em><a id='1.1'></a>
>> <code><strong>__________</strong></code><br>


<br>

> 1.2. <em>What is the root flag?</em><a id='1.2'></a>
>> <code><strong>__________</strong></code><br>

<br>
<br>


<h3 align="center">$$\textcolor{white}{\textnormal{Nmap}}$$</h3>
<p align="center">There are have 2 ports open: <code>22/ssh/OpenSSH 8.2p1</code> and <code>80/http/Apache httpd 2.4.49</code>.</p>

```bash
:~/OhMyWebServer# nmap -sC -sV -Pn -p- -T4 ohmywebserver
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.49 ((Unix))
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.49 (Unix)
|_http-title: Consult - Business Consultancy Agency Template | Home
...
```

<br>
<h3 align="center">$$\textcolor{white}{\textnormal{Gobuster x http://TargetIP/webmasters/}}$$</h3>
<p align="center">Discovered <code>/assets/</code> and <code>/cgi-bin/</code>.</p>

<br>

```bash
:~# gobuster dir -u http://ohmywebserver/webmasters/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -fc 403 -t 100
...
===============================================================
/assets/              (Status: 200) [Size: 404]
/cgi-bin/             (Status: 403) [Size: 199]
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================
```


<br>

