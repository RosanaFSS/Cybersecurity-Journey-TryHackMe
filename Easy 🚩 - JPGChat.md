<p align="center">April 13, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{342}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/962ae40d-abca-4ea0-9255-663cad56a1a5"></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{JPGChat}}$$</h1>
<p align="center"><em>Exploiting poorly made custom chatting service written in a certain language...</em>.<br>
 It is classified as an easy-level CTF.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/jpgchat">here</a>.</p>

<p align="center"> <img width="900px" src=""> </p>

<br>
<br>

<h2>Task 1 . Flags </h2>

<p>[  Start Machine  ]</p>

<p>Hack into the machine and retrieve the flag.<br>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 1.1. <em>Establish a foothold and get user.txt.</em> Hint : <em>Can you get the applications source code, this can be found at the admins github. Where could we be able to find the admins name? Check out the whole application.</em><br><a id='1.1'></a>
>> <strong><code>JPC{487030410a543503cbb59ece16178318}</code></strong><br>
<p></p>

<br>

```bash
:~/JPGChat# nmap -sC -sV -sS -Pn -A -p- -T4 TargetIP
...
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
3000/tcp open  ppp?
| fingerprint-strings: 
|   GenericLines, NULL: 
|     Welcome to JPChat
|     source code of this service can be found at our admin's github
|     MESSAGE USAGE: use [MESSAGE] to message the (currently) only channel
|_    REPORT USAGE: use [REPORT] to report someone to the admins (with proof)
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?
...
Device type: general purpose
Running: Linux 3.X
OS CPE: cpe:/o:linux:linux_kernel:3
OS details: Linux 3.10 - 3.13
...
```

<br>

![image](https://github.com/user-attachments/assets/eb446426-8c49-485f-bea4-dda4ec5c28fe)

<br>

![image](https://github.com/user-attachments/assets/7b6359b4-5358-4c7d-af33-7864de242296)

<br>

![image](https://github.com/user-attachments/assets/7a4a18a1-ac9d-419b-9c2c-ff7d2a02ab55)

<br>

![image](https://github.com/user-attachments/assets/66c69c4c-d677-4b14-9e0b-a64dde237ba8)

<br>
<br>

> 1.2. <em>Escalate your privileges to root and read root.txt.</em> Hint : <em>In the sudo -l output, you can see that PYTHONPATH variable will be kept. Can you exploit this? Google around</em><br><a id='1.2'></a>
>> <strong><code>_____</code></strong><br>
<p></p>

<br>
