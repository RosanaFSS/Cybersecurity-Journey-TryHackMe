<h1 align="center">Sea Surfer</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/65646d1b-002b-4dbb-bd9f-4b240f90f042"><br>
2025, Spetember 1<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>483</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Ride the Wave!</em>.<br>
Access it <a href=..."</a>here.<br>
<img width="1200px" src="h..."></p>


<br>
<h2>Task 1 . Let´s go!</h2>
<p>It's a beautiful day to hit the beach and do some surfing.<br>

<em>Please allow up to 5 minutes for the machine to boot up.</em></p>

<p><em>Answer the questions below</em></p>

<p>1.1. What is user.txt<br>
<code>_______________</code></p>

<p>1.2. What is root.txt<br>
<code>______________</code></p>

<br>

<h2>nikto</h2>
<p>

- Server leaks inodes via ETags, header found with file /, fields: 0x2aa6 0x5dcde2b3f2ff9 <br>
- Uncommon header 'x-backend-server' found, with contents: seasurfer.thm</p>

```bash
:~/SeaSurfer# nikto -h xx.xxx.xxx.xxx
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xxx.xxx
+ Target Hostname:    ip-xx-xxx-xxx-xxx.ec2.internal
+ Target Port:        80
+ Start Time:         2025-09-01 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ Server leaks inodes via ETags, header found with file /, fields: 0x2aa6 0x5dcde2b3f2ff9 
+ The anti-clickjacking X-Frame-Options header is not present.
+ Uncommon header 'x-backend-server' found, with contents: seasurfer.thm
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: GET, POST, OPTIONS, HEAD 
+ 6544 items checked: 0 error(s) and 4 item(s) reported on remote host
+ End Time:           2025-09-01 xx:xx:xx (GMT1) (13 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<h2>curl</h2>
<p>

- Server: Apache/2.4.41<br>
X-Backend-Server: seasurfer.thm</p>

```bash
:~/SeaSurfer# curl xx.xxx.xxx.xxx -I
HTTP/1.1 200 OK
Date: Mon, 01 Sep 2025 xx:xx:xx GMT
Server: Apache/2.4.41 (Ubuntu)
Last-Modified: Sun, 17 Apr 2022 18:54:09 GMT
ETag: "2aa6-5dcde2b3f2ff9"
Accept-Ranges: bytes
Content-Length: 10918
Vary: Accept-Encoding
X-Backend-Server: seasurfer.thm
Content-Type: text/html
```

<h2>/etc/hosts</h2>

```bash
xx.xxx.xxx.xxx seasurfer.thm
```

<h2>nmap</h2>
<p>

- 22 : SSH : OpenSSH 8.2p1<br>
- 80 : HTTP : Wordpress 5.9.3, Apache/2.4.41</p>

```bash
:~/SeaSurfer# nmap -sC -sV -p- -T4 seasurfer.thm
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-generator: WordPress 5.9.3
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Sea Surfer &#8211; Ride the Wave!
```






