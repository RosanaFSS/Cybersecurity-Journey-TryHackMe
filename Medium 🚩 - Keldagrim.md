<h1 align="center">Keldagrim</h1>
<p align="center"><em>The dwarves are hiding their gold</em>!<br>
<img width="80px" src="https://github.com/user-attachments/assets/ab6bbba1-eb21-4189-8b67-d239ae0f6af0"><br>
July 13, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.
It´s part of my <code>433</code>-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>. It is classified as a medium-level CTF.
You can join it clicking  <a href="https://tryhackme.com/room/keldagrim">here</a>.<br><br>
<img width="1200px" src=""></p>


<br>

<h2>Task 1 . Infiltrate the Forge</h2>
<p>Can you overcome the forge and steal all of the gold!</p>

<br>

<br>
<br>

Target = 10.10.64.159

<h1>Reconnaissance</h1>
<h3>Port Scanning with <code>nmap</code></h3>

```bash
:~/Keldagrim# nmap -sC -sV -p- -T4 TargetIP
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Werkzeug/3.0.6 Python/3.8.10
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 OK
|     Server: Werkzeug/3.0.6 Python/3.8.10
|     Date: Mon, xx Jul 2025 xx:xx:xx GMT
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 2634
|     Set-Cookie: session=WjNWbGMzUT0=; Path=/
|     Connection: close
|     <!DOCTYPE html>
|     <html>
|     <head>
|     <title> Home page </title>
|     <link rel="stylesheet" href="/static/bootstrap.css">
|     <script src="/static/jquery-3.5.1.slim.min.js"></script>
|     <script src="/static/bootstrap.bundle.min.js"></script>
|     <link rel="stylesheet" href="/static/style.css">
|     </head>
|     <body>
|     <div class="jumbotron jumbotron-fluid mb-0 py-4">
|     <div class="container ">
|     class="display-4">Keldagrim Forge</h1>
|     class="lead">Welcome to Keldagrim Forge! The number one gold selling website!</p>
|     </div>
|     </div>
|     class="nav bg-light justify-content-center">
|     class="nav-item">
|     class="nav-link active" href="/">Home</a>
|   HTTPOptions: 
|     HTTP/1.1 200 OK
|     Server: Werkzeug/3.0.6 Python/3.8.10
|     Date: Mon, xx Jul 2025 xx:xx:xx GMT
|     Content-Type: text/html; charset=utf-8
|     Allow: OPTIONS, HEAD, GET
|     Content-Length: 0
|     Connection: close
|   RTSPRequest: 
|     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
|     "http://www.w3.org/TR/html4/strict.dtd">
|     <html>
|     <head>
|     <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
|     <title>Error response</title>
|     </head>
|     <body>
|     <h1>Error response</h1>
|     <p>Error code: 400</p>
|     <p>Message: Bad request version ('RTSP/1.0').</p>
|     <p>Error code explanation: HTTPStatus.BAD_REQUEST - Bad request syntax or unsupported method.</p>
|     </body>
|_    </html>
| http-cookie-flags: 
|   /: 
|     session: 
|_      httponly flag not set
|_http-server-header: Werkzeug/3.0.6 Python/3.8.10
|_http-title:  Home page 
```

<h3>Web</code></h3>

<img width="1003" height="418" alt="image" src="https://github.com/user-attachments/assets/1fc27556-4f79-458a-a252-9f7f38a2da23" />

<p>
  
- WjNWbGMzUT0=<br>
- decoded from Base64 --> guest</p>


<p>

- admin encoded to Base64 --> YWRtaW4=</p>

<h3></h3>

```bash
:~/Keldagrim# nmap -sC -sV -p- -T4 10.10.64.159
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Werkzeug/3.0.6 Python/3.8.10
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 OK
|     Server: Werkzeug/3.0.6 Python/3.8.10
|     Date: Mon, xx Jul 2025 xx:xx:xx GMT
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 2634
|     Set-Cookie: session=WjNWbGMzUT0=; Path=/
|     Connection: close
|     <!DOCTYPE html>
|     <html>
|     <head>
|     <title> Home page </title>
|     <link rel="stylesheet" href="/static/bootstrap.css">
|     <script src="/static/jquery-3.5.1.slim.min.js"></script>
|     <script src="/static/bootstrap.bundle.min.js"></script>
|     <link rel="stylesheet" href="/static/style.css">
|     </head>
|     <body>
|     <div class="jumbotron jumbotron-fluid mb-0 py-4">
|     <div class="container ">
|     class="display-4">Keldagrim Forge</h1>
|     class="lead">Welcome to Keldagrim Forge! The number one gold selling website!</p>
|     </div>
|     </div>
|     class="nav bg-light justify-content-center">
|     class="nav-item">
|     class="nav-link active" href="/">Home</a>
|   HTTPOptions: 
|     HTTP/1.1 200 OK
|     Server: Werkzeug/3.0.6 Python/3.8.10
|     Date: Mon, xx Jul 2025 xx:xx:xx GMT
|     Content-Type: text/html; charset=utf-8
|     Allow: OPTIONS, HEAD, GET
|     Content-Length: 0
|     Connection: close
|   RTSPRequest: 
|     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
|     "http://www.w3.org/TR/html4/strict.dtd">
|     <html>
|     <head>
|     <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
|     <title>Error response</title>
|     </head>
|     <body>
|     <h1>Error response</h1>
|     <p>Error code: 400</p>
|     <p>Message: Bad request version ('RTSP/1.0').</p>
|     <p>Error code explanation: HTTPStatus.BAD_REQUEST - Bad request syntax or unsupported method.</p>
|     </body>
|_    </html>
| http-cookie-flags: 
|   /: 
|     session: 
|_      httponly flag not set
|_http-server-header: Werkzeug/3.0.6 Python/3.8.10
|_http-title:  Home page 
```

