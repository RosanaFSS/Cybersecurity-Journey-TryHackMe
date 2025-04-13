<p align="center">April 13, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{342}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/962ae40d-abca-4ea0-9255-663cad56a1a5"></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Haskhell}}$$</h1>
<p align="center"><em>Teach your CS professor that his PhD isn't in security.</em>.<br>
 It is classified as a medium-level CTF.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/haskhell">here</a>.</p>

<p align="center"> <img width="900px" src=""> </p>


<br>
<br>

<h2>Task 1 . HaskHell </h2>

<p>[  Start Machine  ]</p>

<p>Show your professor that his PhD isn't in security.<br>

Please send comments/concerns/hatemail to @passthehashbrwn on Twitter.</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 1.1. <em>Get the flag in the user.txt file.</em><br><a id='1.1'></a>
>> <strong><code>___</code></strong><br>
<p></p>

<br>


<p>Used <code>nmapo</code>.  Discovered:<br>
.  2 ports open:  <code>22/ssh</code> and <code>5001/Gunicorn</code>code>.<br>
.  <code>http-server-header: gunicorn/19.7.1</code></br>
.  <code>http-title: Homepage</code></p>


```bash
:~/HaskHell# nmap -sC -sV -sS -Pn -A -p- -T4 TargetIP
...
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
5001/tcp open  http    Gunicorn 19.7.1
|_http-server-header: gunicorn/19.7.1
|_http-title: Homepage
```

<br>

<p>Navigated to <code>http://TargetIP:5001</code></p>

<br>

![image](https://github.com/user-attachments/assets/708e34e1-f698-44b5-a307-8568e07661d6)

<br>

<p>Viewed page source.<br>
Identified:<br>
. <code>/homework1</code><br>
. <code>Our book for the course (free!): http://learnyouahaskell.com/chapters</code><br>
. <code>The complete Haskell package repository. ... grading system: https://hackage.haskell.org/</code></p>

<br>

![image](https://github.com/user-attachments/assets/5f7f31e7-2f3d-43be-ac82-04d84697c2f7)

<br>


<p>Added <code>Homepage</code> and <code>TargetIP</code> to <code>/etc/hosts</code>.</p>

<br>


![image](https://github.com/user-attachments/assets/c8afea6a-d981-44a2-a115-5fbccd5f61a6)

<br>

<p>Clicked <code>homework here</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/0a21fae4-ede3-4692-a0e1-99711e0cd9bf)

<br>





```bash
:~/HaskHell# nmap -sC -sV -sS -Pn -A -p- -T4 TargetIP
...
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
5001/tcp open  http    Gunicorn 19.7.1
|_http-server-header: gunicorn/19.7.1
|_http-title: Homepage
```

> 1.2. <em>Obtain the flag in root.txt.</em><br><a id='1.2'></a>
>> <strong><code>___</code></strong><br>
<p></p>

<br><br>



