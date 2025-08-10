<h1 align="center">CERTain Doom</h1>
<p align="center">2025, August 10<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>461</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Bob has since joined the CERT team and developed a nifty new site. Is there more than meets the eye</em>?<br>
<img width="80px" src="https://github.com/user-attachments/assets/7c079b1a-7fa9-4ade-9565-1f55cda42c48"><br>
Access this hard-level CTF clicking <a href="https://tryhackme.com/room/certaindoom">here </a>.<br>
<img width="1200px" src=""></p>

<br>


<h2>Task 1 . Deploy the VM</h2>
<p><code>Bob</code>´s finally joined the <code>CERT team</code> and has created a new front page. Surely nothing can go wrong.<br>



(Please give a few minutes for the VM to boot properly)</p>

<p><em>Answer the question below</em></p>

<p>1.1. I've started the VM and waited a few minutes for it to boot.<br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 . Flagz</h2>
<p>There's no way in, or is there?</p>

<p><em>Answer the questions below</em></p>

<p>2.1. What is the web flag? Hint : Today's lucky number is 11<br>
<code>________________________________</code></p>

<br>

<p>2.2. What is the user's flag?<br>
<code>________________________________</code></p>

<br>

<p>2.3. What is the super secret flag? Hint : supersonic subatomic<br>
<code>________________________________</code></p>

<br>

<h3>nmap</h3>

<p>

- <code>&nbsp;&nbsp;22</code> &nbsp; : &nbsp; <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ssh</code> &nbsp; : &nbsp; <code>OpenSSH 8.0</code><br>
- <code>&nbsp;&nbsp;80</code> &nbsp; : &nbsp; <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;http</code> &nbsp; : &nbsp; <code>hastatic-1.0.0</code><br>
- <code>8080</code>           &nbsp; : &nbsp; <code>http-proxy</code> &nbsp; : <code>Apache Tomcat 97</code></p>

```bash
:~/CERTainDoom# nmap -sC -sV -Pn -n -p- -T4 xx.xxx.xxx.xxx
...
PORT     STATE  SERVICE    VERSION
22/tcp   open   ssh        OpenSSH 8.0 (protocol 2.0)
| ssh-hostkey: 
...
80/tcp   open   http       hastatic-1.0.0
| fingerprint-strings: 
|   GetRequest, HTTPOptions: 
|     HTTP/1.0 200 OK
|     Content-Length: 117674
|     Accept-Ranges: bytes
|     Date: Sun, 10 Aug 2025 12:57:17 GMT
|     Server: hastatic-1.0.0
|     Content-Type: text/html
|     Cache-Control: no-transform,public,max-age=300,s-maxage=900
|     Last-Modified: Thu, 26-Jan-2023 22:44:29 UTC
|     ETag: 98eb1c6fb079742e0b8682cb642c5c777329ebbe
|     Vary: Accept-Encoding
|     Referrer-Policy: strict-origin-when-cross-origin
|     X-Frame-Options: SAMEORIGIN
|     X-XSS-Protection: 1; mode=block
|     <!doctype html>
|     <html class="no-js" lang="">
|     <head>
|     <meta charset="utf-8">
|     <title>Super Secret Admin Page</title>
|     <meta name="description" content="">
|     <meta name="viewport" content="width=device-width, initial-scale=1">
|     <meta property="og:title" content="Hydra's Super Secret Admin Page">
|     <meta property="og:type" content="website">
|     <meta property="og:url" content="https://admin.certain-doom.thm">
|_    <meta property="og:image" content="">
|_http-server-header: hastatic-1.0.0
|_http-title: Super Secret Admin Page
8080/tcp open   http-proxy Apache Tomcat 9?
| fingerprint-strings: 
|   GetRequest, HTTPOptions: 
|     HTTP/1.1 404 
|     Content-Type: text/html;charset=utf-8
|     Content-Language: en
|     Content-Length: 431
|     Date: Sun, 10 Aug 2025 12:57:17 GMT
|     Connection: close
|     Server: Apache Tomcat 9?
|     <!doctype html><html lang="en"><head><title>HTTP Status 404 
|     Found</title><style type="text/css">body {font-family:Tahoma,Arial,sans-serif;} h1, h2, h3, b {color:white;background-color:#525D76;} h1 {font-size:22px;} h2 {font-size:16px;} h3 {font-size:14px;} p {font-size:12px;} a {color:black;} .line {height:1px;background-color:#525D76;border:none;}</style></head><body><h1>HTTP Status 404 
|     Found</h1></body></html>
|   RTSPRequest: 
|     HTTP/1.1 400 
|     Content-Type: text/html;charset=utf-8
|     Content-Language: en
|     Content-Length: 435
|     Date: Sun, 10 Aug 2025 12:57:17 GMT
|     Connection: close
|     Server: Apache Tomcat 9?
|     <!doctype html><html lang="en"><head><title>HTTP Status 400 
|     Request</title><style type="text/css">body {font-family:Tahoma,Arial,sans-serif;} h1, h2, h3, b {color:white;background-color:#525D76;} h1 {font-size:22px;} h2 {font-size:16px;} h3 {font-size:14px;} p {font-size:12px;} a {color:black;} .line {height:1px;background-color:#525D76;border:none;}</style></head><body><h1>HTTP Status 400 
|_    Request</h1></body></html>
|_http-server-header: Apache Tomcat 9?
|_http-title: HTTP Status 404 \xE2\x80\x93 Not Found
9090/tcp closed zeus-admin
```


```bash

```

```bash

```

```bash

```

```bash

```

```bash

```
