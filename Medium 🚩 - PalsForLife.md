<h1 align="center">PalsForLife</h1>
<p align="center">2025, August 11<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>462</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Abuse a misconfigured Kubernetes cluster</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/05ab7508-6a94-4e64-a46b-c5c72094d611"><br>
Access this TryHackMe´s walkthrough <a href="https://tryhackme.com/room/palsforlife">here </a>.<br>
<img width="1200px" src=""></p>


<h2>Task 1 . Download</h2>
<p>Connect to our network and deploy this machine. If you are unsure on how to get connected, complete the OpenVPN room first.<br>

Please allow 5 minutes for the machine to fully boot up.</p>

<p><em>Answer the question below</em></p>

<p><code>No answer needed</code></p>

<br>
<h2>Task 2 . Compromise the machine</h2>
<p align="center">Are you able to compromise this World Of Warcraft themed machine?<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/f3c2644f-418d-458b-b771-86ce8143f9be"><br>
Source: https://hearthstone.fandom.com/wiki/Leeroy_Jenkins</p>

<p><em>Answer the questions below</em></p>

<p>1.1. Flag 1. Hint : Must be hidden somewhere in the web tool<br>
<code>flag{Stick_to_the_plan!}</code></p>

<br>

<p>1.2. Flag 2. Hint : Get a shell<br>
<code>flag{_G0ddamit_Leeroy_}</code></p>

<br>

<p>1.3. Flag 3. Hint : kubectl<br>
<code>flag{Its_n0t_my_fault!}</code></p>

<br>

<p>1.4. Flag 4. Hint : Can we reuse a node image?<br>
<code>__________________</code></p>

<br>
<br>
<h3>nmap</h3>

```bash
:~/PalsForLife# nmap -sC -sV -Pn -p- -T4 xx.xxx.xx.xx
...
PORT      STATE SERVICE           VERSION
22/tcp    open  ssh               OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
6443/tcp  open  ssl/sun-sr-https?
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 401 Unauthorized
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     Date: Mon, 11 Aug 2025 23:16:26 GMT
|     Content-Length: 129
|     {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"Unauthorized","reason":"Unauthorized","code":401}
|   GenericLines, Help, Kerberos, RTSPRequest, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest, HTTPOptions: 
|     HTTP/1.0 401 Unauthorized
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     Date: Mon, 11 Aug 2025 xx:xx:xx GMT
|     Content-Length: 129
|_    {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"Unauthorized","reason":"Unauthorized","code":401}
| ssl-cert: Subject: commonName=k3s/organizationName=k3s
| Subject Alternative Name: DNS:kubernetes, DNS:kubernetes.default, DNS:kubernetes.default.svc.cluster.local, DNS:localhost, IP Address:xx.xxx.xx.xxx, IP Address:10.43.0.1, IP Address:127.0.0.1, IP Address:172.30.18.136, IP Address:192.168.1.244
| Not valid before: 2021-05-31Txx:xx:xx
|_Not valid after:  2026-08-11Txx:xx:xx
10250/tcp open  ssl/http          Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).
| ssl-cert: Subject: commonName=palsforlife
| Subject Alternative Name: DNS:palsforlife, DNS:localhost, IP Address:127.0.0.1, IP Address:xx.xxx.xx.xxx
| Not valid before: 2021-05-31Txx:xx:xx
|_Not valid after:  2026-08-11Txx:xx:xx
30180/tcp open  http              nginx 1.21.0
|_http-server-header: nginx/1.21.0
|_http-title: 403 Forbidden
31111/tcp open  unknown
| fingerprint-strings: 
|   GenericLines: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 200 OK
|     Content-Type: text/html; charset=UTF-8
|     Set-Cookie: lang=en-US; Path=/; Max-Age=2147483647
|     Set-Cookie: i_like_gitea=e3776816861a835b; Path=/; HttpOnly
|     Set-Cookie: _csrf=4aIokVGLH7M9affGyh6eFwgs4hI6MTc1NDk1NDE1NTc3NDc0MjkwOA%3D%3D; Path=/; Expires=Tue, 12 Aug 2025 xx:xx:xx GMT; HttpOnly
|     X-Frame-Options: SAMEORIGIN
|     Date: Mon, 11 Aug 2025 xx:xx:xx5 GMT
|     <!DOCTYPE html>
|     <html>
|     <head data-suburl="">
|     <meta charset="utf-8">
|     <meta name="viewport" content="width=device-width, initial-scale=1">
|     <meta http-equiv="x-ua-compatible" content="ie=edge">
|     <title>Gitea: Git with a cup of tea</title>
|     <meta name="theme-color" content="#6cc644">
|     <meta name="author" content="Gitea - Git with a cup of tea" />
|     <meta name="description" content="Gitea (Git with a cup of tea) is a painless self-hosted Git service written in Go" />
|     <meta name="keywords" content="go,git,self-hosted,gitea
|   HTTPOptions: 
|     HTTP/1.0 404 Not Found
|     Content-Type: text/html; charset=UTF-8
|     Set-Cookie: lang=en-US; Path=/; Max-Age=2147483647
|     Set-Cookie: i_like_gitea=68c507915e859143; Path=/; HttpOnly
|     Set-Cookie: _csrf=tbKcZy3e7ad5UbSS5j-PbY4o5f46MTc1NDk1NDE1NTc5NzI5NTEzMA%3D%3D; Path=/; Expires=Tue, 12 Aug 2025 xx:xx:xx GMT; HttpOnly
|     X-Frame-Options: SAMEORIGIN
|     Date: Mon, 11 Aug 2025 xx:xx:xx GMT
|     <!DOCTYPE html>
|     <html>
|     <head data-suburl="">
|     <meta charset="utf-8">
|     <meta name="viewport" content="width=device-width, initial-scale=1">
|     <meta http-equiv="x-ua-compatible" content="ie=edge">
|     <title>Page Not Found - Gitea: Git with a cup of tea</title>
|     <meta name="theme-color" content="#6cc644">
|     <meta name="author" content="Gitea - Git with a cup of tea" />
|     <meta name="description" content="Gitea (Git with a cup of tea) is a painless self-hosted Git service written in Go" />
|_    <meta name="keywords" content="
31112/tcp open  ssh               OpenSSH 7.5 (protocol 2.0)
| ssh-hostkey: 
...
```

<br>

<p><code>22</code> : ssh : OpenSSH 7.6p1 Ubuntu 4ubuntu0.3</p>

<p><code>6443</code> : ssl/sun-sr-https?<br>

- <code>xx.xxx.xx.xxx</code>, <code>10.43.0.1</code>, <code>127.0.0.1</code>, <code>172.30.18.136</code>, <code>192.168.1.244</code><br>
- <code>kubernetes</code>, <code>kubernetes.default</code>, <code>localhost</code><br>, <code>kubernetes.default.svc.cluster.local</code></p>

<p><code>10250</code> : ssl/http : Golang net/http server (Go-IPFS json-rpc or InfluxDB API)</p>

<p><code>30180</code> : http : nginx 1.21.0</p>

<p><code>31111</code> : Gitea</p>

<p><code>31112</code> : ssh</p>

<br>
<h3>gobuster</h3>

```bash
:~/PalsForLife# gobuster dir -u http://xx.xxx.xx.xxx:31111/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -t 50
...

```


```bash

```


```bash

```


```bash

```


```bash

```








<img width="400" height="457" alt="image" src="https://github.com/user-attachments/assets/0dd814ed-5de8-48b1-9c93-281ac028e877" />

