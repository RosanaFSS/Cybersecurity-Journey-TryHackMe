<h1 align="center">Unbaked Pie</h1>
<p align="center">July 24, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>444</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Don't over-baked your pie!</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/d890fb0e-d6a1-4543-a23b-ba6498d576df"><br>
Click <a href="https://tryhackme.com/room/unbakedpie">here </a>to access this TryHackMe CTF.<br>
<img width="1200px" src=""></p>


<br>
<br>

<h2>Task 1 . Capture The Flag</h2>
<p>Please allow 5 minutes for this instance to fully deploy before attacking. This VM was developed in collaboration with @ch4rm, thanks to him for the foothold and privilege escalation ideas. </p>


<p><em>Answer the questions below</em></p>

<br>

<p>1.1. User Flag<br>
<code>____</code></p>

<br>

<p>1.2. Root Flag<br>
<code>____</code></p>

<h3>nmap</h3>

<p>

- <code>5003</code> : <code>filemaker?</code><br>
</p>

```bash
:~/UnbakedPie# nmap -sC -sV -Pn TargetIP
...
PORT     STATE SERVICE    VERSION
5003/tcp open  filemaker?
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 OK
|     Date: Fri, 25 Jul 2025 xx:xx:xx GMT
|     Server: WSGIServer/0.2 CPython/3.8.6
|     Content-Type: text/html; charset=utf-8
|     X-Frame-Options: DENY
|     Vary: Cookie
|     Content-Length: 7453
|     X-Content-Type-Options: nosniff
|     Referrer-Policy: same-origin
|     Set-Cookie: csrftoken=gAyLhQzTTvGJSwxS5OaEE70fPwZOaupLbR2JDJ6OulMz4x7Ed6IaHiQFVIliIp9J; expires=Fri, 24 Jul 2026 xx:xx:xx GMT; Max-Age=31449600; Path=/; SameSite=Lax
|     <!DOCTYPE html>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
|     <meta name="description" content="">
|     <meta name="author" content="">
|     <title>[Un]baked | /</title>
|     <!-- Bootstrap core CSS -->
|     <link href="/static/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
|     <!-- Custom fonts for this template -->
|     <link href="/static/vendor/fontawesome-free/css/all.min.cs
|   HTTPOptions: 
|     HTTP/1.1 200 OK
|     Date: Fri, 25 Jul 2025 xx:xx:xx GMT
|     Server: WSGIServer/0.2 CPython/3.8.6
|     Content-Type: text/html; charset=utf-8
|     X-Frame-Options: DENY
|     Vary: Cookie
|     Content-Length: 7453
|     X-Content-Type-Options: nosniff
|     Referrer-Policy: same-origin
|     Set-Cookie: csrftoken=XpDKgK4t5EJhpyFLqtYaseopDyj6CGISbyNrVnx0hl2B0PQImUYqJV448Vjx1CM1; expires=Fri, 24 Jul 2026 xx:xx:xx GMT; Max-Age=31449600; Path=/; SameSite=Lax
|     <!DOCTYPE html>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
|     <meta name="description" content="">
|     <meta name="author" content="">
|     <title>[Un]baked | /</title>
|     <!-- Bootstrap core CSS -->
|     <link href="/static/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
|     <!-- Custom fonts for this template -->
|_    <link href="/static/vendor/fontawesome-free/css/all.min.cs
```

<h3>/etc/hosts</h3>

```bash
TargetIP   unbaked.thm
```

<h3>Web</h3>
<p>

- Homemade Pickle<br>
- Pickle Pie
</p>

<img width="1130" height="179" alt="image" src="https://github.com/user-attachments/assets/f63a790d-3fbb-4e6f-b463-0bfb56599ab1" />

<img width="1133" height="642" alt="image" src="https://github.com/user-attachments/assets/2d49e2f8-0fc3-42da-8a51-48dadb82eaff" />

<h3>csrftoken</h3>

<img width="1127" height="514" alt="image" src="https://github.com/user-attachments/assets/f7a835d8-a985-44e0-a7bf-9db4780d4171" />

<h3>search_cookie</h3>

<img width="1125" height="102" alt="image" src="https://github.com/user-attachments/assets/f862711b-f17d-4bc1-90fa-ff6bd9b20528" />

<h3> Search = test > ls >  hell</h3>

<img width="1097" height="233" alt="image" src="https://github.com/user-attachments/assets/4a4f313a-4773-4947-a94c-dbc256386bc0" />

```bash
:~/UnbakedPie# echo 'gASVCAAAAAAAAACMBHRlc3SULg==' | base64 -d | xxd
00000000: 8004 9508 0000 0000 0000 008c 0474 6573  .............tes
00000010: 7494 2e                                  t..
:~/UnbakedPie# echo 'gASVBgAAAAAAAACMAmxzlC4=' | base64 -d | xxd
00000000: 8004 9506 0000 0000 0000 008c 026c 7394  .............ls.
00000010: 2e                                       .
:~/UnbakedPie# echo 'gASVCQAAAAAAAACMBWhlbGxvlC4=' | base64 -d | xxd
00000000: 8004 9509 0000 0000 0000 008c 0568 656c  .............hel
00000010: 6c6f 942e                                lo..
```



<img width="1103" height="525" alt="image" src="https://github.com/user-attachments/assets/bb7c8fd9-a54c-44ed-8202-0cb5a3b02669" />

<img width="1110" height="237" alt="image" src="https://github.com/user-attachments/assets/185f34e1-feef-4727-a488-04961bfdeed6" />

<img width="1107" height="512" alt="image" src="https://github.com/user-attachments/assets/309387d6-cca8-4693-a676-ef3577ede72f" />


<img width="1088" height="340" alt="image" src="https://github.com/user-attachments/assets/d5ff35fe-fdde-44f6-9b22-e470bbad3582" />

<img width="1129" height="403" alt="image" src="https://github.com/user-attachments/assets/2f4539b0-3a5c-409c-909a-0aff253f4703" />

<img width="1128" height="441" alt="image" src="https://github.com/user-attachments/assets/76475db7-71a2-4b5f-8164-05a0622e1aa2" />





<h3>CyberChef</h3>




