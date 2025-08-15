<h1 align="center">Contrabando</h1>
<p align="center">2025, August 15<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>466</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Never tell me the odds.</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/5a1e2441-6336-4ce2-8100-1032df5091bc"><br>
Access this TryHackMe´s walkthrough <a href="https://tryhackme.com/room/theblobblog">here </a>.<br>
<img width="1200px" src=""></p>

<br>
<br>

<h2>Task 1 . Capture the Flags!</h2>
<p>Our company was excited to release our new product, but a recent attack has forced us to go down for maintenance. They have asked you to conduct a vulnerability assessment to help identify how the attack occurred.<br>

Are you up for it?<br>

Great kid! Don't get cocky.<br>

Please allow the VM 5 minutes to fully boot up.</p>

<br>
<p><em>Answer the questions below</em></p>

<p>1.1. What is the first flag?<br>
<code>_________________________</code></p>

<br>

<p>1.2. What is the second flag?<br>
<code>_________________________</code></p>

<br>

<h2 align="center">Enumeration</h2>
<br>
<br>
<h3>Nikto</h3>

```bash
:~/Contrabando# nikto -h  xx.xxx.xx.xx
...
```

<br>
<br>
<h3>ping</h3>

```bash
:~/Contrabando# ping -c 4 xx.xxx.xx.xx
...
```

<br>
<br>
<h3>Traceroute</h3>

```bash
:~/Contrabando#traceroute xx.xxx.xx.xx
...
```

<br>



<img width="1294" height="360" alt="image" src="https://github.com/user-attachments/assets/7d6a8114-b216-4012-a7f0-96ee35a69054" />

<br>
<br>
<h3>Nmap</h3>

<p>

- 22 : ssh<br>
- 80 : http</p>

<br>

```bash
:~/Contrabando# nmap -sT -p- -T4 xx.xxx.xx.xx
...
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp

open  http
```

<br>

```bash
:~/Contrabando# nmap -A --min-rate=1000 xx.xxx.xx.xx
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.55 ((Unix))
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.55 (Unix)
|_http-title: Site doesn't have a title (text/html).
```

<br>


```bash
:~/Contrabando# nmap -T4 -A -v --max-rtt-timeout 1500ms --min-rate 4500 --max-os-tries 1 -Pn --osscan-limit 1 --script vuln,http-enum,smb-enum-shares.nse xx.xxx.xx.xx
...
PORT   STATE SERVICE
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
...
80/tcp open  http    Apache httpd 2.4.55 ((Unix))
| http-enum: 
|_  /page/: Potentially interesting folder
|_http-server-header: Apache/2.4.55 (Unix)
...
|_http-trace: TRACE is enabled

open  http
```

<br>
<br>
<h3>Dirsearch</h3>

```bash
:~/Contrabando# dirsearch -u http://xx.xxx.xx.xx
...
[xx:xx:xx] 200 -  820B  - /cgi-bin/printenv
[xx:xx:xx] 200 -    1KB - /cgi-bin/test-cgi

Task Completed
```

<br>

```bash
:~/Contrabando# dirsearch -u http://xx.xxx.xx.xx/ -t 100 -i 200
...
[xx:xx:xx] 200 -    1KB - /cgi-bin/test-cgi
[xx:xx:xx] 200 -  820B  - /cgi-bin/printenv
```

<br>

<img width="1270" height="322" alt="image" src="https://github.com/user-attachments/assets/3eb59635-ff82-4d03-9003-8e3103dfb092" />

<br>
<br>



