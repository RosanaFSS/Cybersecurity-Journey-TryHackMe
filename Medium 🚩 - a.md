<h1 align="center">CMSpit<br><img width="1200px" src=""></h1>
<p align="center">June 18, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>408</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>This is a machine that allows you to practise web app hacking and privilege escalation using recent vulnerabilities.</em><br>
Click <a href="https://tryhackme.com/room/cmspit">here </a>to access the "room".<br>
<img width="80px" src="https://github.com/user-attachments/assets/5d595d6b-e29e-4ce1-9c1d-6bc04341b4d2"><br></p>

<h2> Task 1 . Ready Set Go</h2>
<p>You've identified that the CMS installed on the web server has several vulnerabilities that allow attackers to enumerate users and change account passwords.<br>

Your mission is to exploit these vulnerabilities and compromise the web server.</p>

<h4 align="left"> Answer the question below</h4>

> 1.1. <em>What is the name of the Content Management System (CMS) installed on the server?</em><br><a id='1.1'></a>
>> <strong><code>_________</code></strong><br>
<p></p>

<br>

<br>

<h3>nmap</h3>
<p>
  
</p>
- <code>-sS</code>/<code>-sT</code>/<code>-sA</code>/<code>-sW</code>/<code>-SM</code> = <code>TCP SYN</code>/<code>Connect()</code>/<code>ACK</code>/<code>Window</code>/<code>Maimon scans</code><br>
- <code>-sC</code> = equivalent to --script=default<br>
- <code>-p</code> =scan all ports<br>
- <code>-Pn</code> = Treat all hosts as online -- skip host discovery</p>


```bash
:~# nmap -Pn -p- 10.10.72.83
...
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
```

```bash
:~# nmap -sC -sV -p- 10.10.72.83
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 7f:25:f9:40:23:25:cd:29:8b:28:a9:d9:82:f5:49:e4 (RSA)
|   256 0a:f4:29:ed:55:43:19:e7:73:a7:09:79:30:a8:49:1b (ECDSA)
|_  256 2f:43:ad:a3:d1:5b:64:86:33:07:5d:94:f9:dc:a4:01 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
| http-title: Authenticate Please!
|_Requested resource was /auth/login?to=/
|_http-trane-info: Problem with XML parsing of /evox/about
...
```

```bash
TargetIP olympus.thm
```

<h3>dirsearch</h3>

```bash
:~# dirsearch -u http://olympus.thm/ -i200,301,302,401 -w /usr/share/dirb/wordlists/common.txt
...
Target: http://olympus.thm/

Starting: 
301 -  315B  - /~webmaster  ->  http://olympus.thm/~webmaster/
301 -  315B  - /javascript  ->  http://olympus.thm/javascript/
301 -  311B  - /static  ->  http://olympus.thm/static/

Task Completed
```

