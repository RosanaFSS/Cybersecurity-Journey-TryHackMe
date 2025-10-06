<h1 align="center">Island Orchestration</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/a11551ff-026d-4458-b5e4-3b15243ffccd"><br>
2025, October 6<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>517</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Looking for the next holiday destination? Look no further than the Islands of Orchestration</em><br>
Access it <a href="https://tryhackme.com/room/islandorchestration"</a>here.<br>
<img width="1200px" src=""></p>


<h2>Task 1 . Challenge</h2>
<p>Check out the best tropical islands to visit on your next vacation!<br>

Please allow 4 to 5 minutes for the VM to boot.</p>


<p><em>Answer the question below</em></p>

<p>1.1. What si the flag:<br>
<code>*******************************</code></p>


<br>
<br>
<h2 align="center">nmap</h2>

```bash
:~/PythonPlayground# nmap -sC -sV -Pn -p- -T4 xx.xxx.xx.xx
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
...
80/tcp open  http    Node.js Express framework
|_http-title: Python Playground!
```
