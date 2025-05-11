<p align="center">May 11, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{370}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/62cf4572-71af-43ed-898e-31c0887632ce" alt="streak"></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Red}}$$</h1>
<p align="center"><em>A classic battle for the ages.</em>.<br>
It is classified as an easy-level CTF.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/redisl33t"</a>.</p>

<p align="center"> <img width="1000px" src=""> </p>

<br>
<br>

<h2>Task 1 . What are the flags:</h2>

<p>The match has started, and Red has taken the lead on you.<br>
But you are Blue, and only you can take Red down.<br><br>

However, Red has implemented some defense mechanisms that will make the battle a bit difficult:<br>
1. Red has been known to kick adversaries out of the machine. Is there a way around it?<br>
2. Red likes to change adversaries' passwords but tends to keep them relatively the same. <br>
3. Red likes to taunt adversaries in order to throw off their focus. Keep your mind sharp!<br><br>

This is a unique battle, and if you feel up to the challenge. Then by all means go for it!<br>

Whenever you are ready, click on the Start Machine button to fire up the Virtual Machine.</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 1.1. <em>What is the first flag?</em><a id='1.1'></a>
>> <code><strong>__________</strong></code><br>


<br>

> 1.2. <em>What is the second flag?</em><a id='1.2'></a>
>> <code><strong>__________</strong></code><br>

<br>

> 1.3. <em>What is the third flag?</em><a id='1.3'></a>
>> <code><strong>__________</strong></code><br>

<br>

> 1.4. <em>If you liked this room, I recommend checking out TryHackMe's King of the Hill.</em><a id='1.4'></a>
>> <code><strong>__________</strong></code><br>

<br>
<br>


<h3 align="center">$$\textcolor{white}{\textnormal{Nmap}}$$</h3>
<p align="center">There are have 2 ports open: <code>22/ssh/OpenSSH 8.2p1</code>.<br>
Identified <code>/index.php?page=home.html</code>.</p>

<br>

```bash
:~/Red# nmap -sC -sV -A -T4 red
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-title: Atlanta - Free business bootstrap template
|_Requested resource was /index.php?page=home.html
...
```

<br>

<h3 align="center">$$\textcolor{white}{\textnormal{http://TargetIP?page=home.html}}$$</h3>

![image](https://github.com/user-attachments/assets/fd3fbbdc-cd40-436a-b215-f78017cd065b)

<br>

![image](https://github.com/user-attachments/assets/860e3b03-5324-4175-b681-d18516cdadfd)

<br>


<h3 align="center">$$\textcolor{white}{\textnormal{Testing for LFI}}$$</h3>

<br>

<p align="center">Tested <code>?page=../../../etc/passwd</code></p>

<br>

![image](https://github.com/user-attachments/assets/d42226cd-30c4-429e-a41c-7c01423c6b9c)


<br>

<p align="center">Tested <code>?page=....//....//....//etc/passwd</code></p>

<br>

![image](https://github.com/user-attachments/assets/04e4548f-a7a2-4b1d-a18c-a8f572c465bf)

<br>

<p>......</p>

<p align="center">Tested <code>?page=php://filter/resource=/etc/passwd</code><br>
Identified users <code>root</code>, <code>blue</code>code> and <code>red</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/7c2d432d-f145-4bb5-b3cc-5d45185527bf)

<br>






