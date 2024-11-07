<p align="center">November 7, 2024</p>
<p align="center">Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{185}}$$-day-streak in  <a href="https://tryhackme.com/r/hacktivities">TryHackMe</a>.</p>

<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; TryHack3M: Sch3Ma D3Mon &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}}$$
</h1>
<p align="center">A guided challenge to learn about SQL injection exploits.</p>
<p align="center">Access this 🆓 TryHackMe CTF Room clicking <a href="https://tryhackme.com/r/room/sch3mad3mon">TryHack3M: Sch3Ma D3Mon</a>.</p><br>
<p align="center">
  <img height="150px" hspace="20" src="https://github.com/user-attachments/assets/459ff707-087e-47c8-9c33-c6397677b3c1">
  <img height="150px" src="https://github.com/user-attachments/assets/c5776d7a-4d2d-491a-b9ab-c400c2ac751f">
</p>

<p align="center">Summary</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [A Public Computer with a VPN](#1) &nbsp;&nbsp;&nbsp;&nbsp;▪️&nbsp;&nbsp;&nbsp;&nbsp; [Connected Tables](#2) &nbsp;&nbsp;&nbsp;&nbsp;▪️&nbsp;&nbsp;&nbsp;&nbsp; [Unlisted](#3) &nbsp;&nbsp;&nbsp;&nbsp;▪️&nbsp;&nbsp;&nbsp;&nbsp; [From DB to OS](#4) &nbsp;&nbsp;&nbsp;&nbsp;▪️&nbsp;&nbsp;&nbsp;&nbsp;[Finding a Needle in a Malwarestack](#5) &nbsp;&nbsp;&nbsp;&nbsp;▪️&nbsp;&nbsp;&nbsp;&nbsp; [User Flag](#7) &nbsp;&nbsp;&nbsp;&nbsp;▪️&nbsp;&nbsp;&nbsp;&nbsp; [Operation Defang](#8)  &nbsp;&nbsp;&nbsp;&nbsp;▪️&nbsp;&nbsp;&nbsp;&nbsp; [Room Complete](#9) &nbsp;&nbsp;&nbsp;&nbsp;▪️&nbsp;&nbsp;&nbsp;&nbsp; [My Journey](#10)

<br>
<br>
<br>
<h2>Task 1. A Public Computer with a VPN<a id='1'></a></h2>

<p>After weeks of meticulous observation and planning, we pinpointed the public computer that the suspect uses to access their website. The computer is located in a quiet corner of the local library. Although the computer has a warning sign that all computer activity is monitored, the suspect doesn’t seem to care. They only check for installed key loggers before establishing a VPN connection and logging in to their criminal marketplace. This time, we were ready:</p>

<ul style="list-style-type:square">
    <li>We have set the browser to log the session’s TLS keys; this logging was achieved by adding an extra option to the browser shortcut. Executing chromium --ssl-key-log-file=~/ssl-key.log dumps the TLS keys to the ssl-key.log file.</li>
    <li>We were capturing all traffic on that computer.</li>
</ul></p>

<p>By the time they finished, we had a log of used TLS keys and an encrypted packet capture. You can access these files by clicking the Download Task Files button or navigating to /root/Rooms/TryHack3M/sch3MaD3Mon on the AttackBox. Using the TLS key log file, Wireshark should be able to decrypt all exchanged traffic.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>
<br>

> 1.1. <em>What is the suspect’s username?.</em><br><a id='1.1'></a>
>> <code><strong>lannister</strong></code>

> 1.2. <em>What is the suspect’s password?</em><br><a id='1.2'></a>
>> <code><strong>hrpTfL42wMv3</strong></code>



<br>

<h2>Room Complete<a id='9'></a></h2>
<p>Keep learning, keep growing!<br>

![image](https://github.com/user-attachments/assets/445eb4bd-cae7-4f87-9baf-ae2d1e85783a)

<h2>My Journey<a id='10'></a></h2>
<p></p>Following I share the status of my journey in TryHackMe.</p>

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     |
| :---------------: | :------- | :----------- | :----------- | :---------- | :--------- | :------  | :-------- |
|                   |          | WorldWide    | Brazil       | WorldWide   | Brazil     |          | Completed |
| November 7, 2024  | 185      |       1,286ª |          28ª |      4,298ª |        60ª | 53,942   |       405 |

![image](https://github.com/user-attachments/assets/269011a6-5ffa-477c-9ebf-c1afaed0a69e)


<p style="text-align: center;">Thank you for coming. Hope to learn together again!!</p>

