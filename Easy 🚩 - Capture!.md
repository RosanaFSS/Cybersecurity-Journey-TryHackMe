<p align="center">April 13, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{342}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/af2cb93f-e7c3-4bad-aa90-d496ef276726" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/962ae40d-abca-4ea0-9255-663cad56a1a5"></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Capture!}}$$</h1>
<p align="center"><em>"   "</em>.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/capture">here</a>.</p>

<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/c677b0af-399d-4991-ba90-fa5e39564b5a"> </p>


<br>
<br>

<h2>Task 1 . General Information </h2>

<p>[  Donwload Task Files ]</p>

<p>SecureSolaCoders has once again developed a web application. They were tired of hackers enumerating and exploiting their previous login form. They thought a Web Application Firewall (WAF) was too overkill and unnecessary, so they developed their own rate limiter and modified the code slightly.<br>

Before we start, download the required files by pressing the Download Task Files button.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 1.1. <em>I have downloaded the capture.zip file.</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br><br>

<h2>Task 2 . Bypass the login form</h2>

<p>[ Start Machine ]</p>

<p>Please wait approximately 3-5 minutes for the application to start.<br>

You can find the web application at: http://TargetIP</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 2.1. <em>What is the value of flag.txt?</em><br><a id='2.1'></a>
>> <strong><code>7df2eabce36f02ca8ed7f237f77ea416</code></strong><br>
<p></p>

<br><br>

<p>Unziped <code>capture.zip</code>.<br>
Two files were inflated:<br>
.    <code>passwords.txt</code><br>
.    <code>usernames.txt</code></p>

<br>

![image](https://github.com/user-attachments/assets/90aab410-0787-4276-99ac-020a26299e48)

<br>


<p>Used <code>nmapo</code>.  Discovered:<br>
.  just port <code>80</code> is open.<br>
.  <code>Requested resource was /login</code>.<br>
.  <code>http-server-header: Werkzeug/2.2.2 Python/3.8.10</code></br>
.  <code>http-title: Site doesn't have a title (text/html; charset=utf-8).</code></p>


```bash
:~/Capture# nmap -sC -sV -sS -Pn -A -T4 -p- TargetIP
...
PORT   STATE SERVICE VERSION
80/tcp open  http    Werkzeug/2.2.2 Python/3.8.10
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.1 404 NOT FOUND
|     Server: Werkzeug/2.2.2 Python/3.8.10
|     Date: Sun, 13 Apr ...
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
|     Date: Sun, 13 Apr 2025 ...
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
|     Date: Sun, 13 Apr 2025 ...
|     Content-Type: text/html; charset=utf-8
|     Allow: OPTIONS, GET, HEAD
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

<p>Used <code>gobuster</code>.  Discovered:<br>
.  <code>/home</code><br>
.  <code>/login</code></p>

```bash
:~/Capture# gobuster dir -u http://TargetIP -w /usr/share/wordlists/dirb/common.txt --random-agent -r -e -x html,php,aspx,asp,txt -b 403,404,501,502,503 -o report.txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://TargetIP
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   502,503,403,404,501
[+] User Agent:              Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.0.7) Gecko/20060911 Firefox/1.5.0.7
[+] Extensions:              html,php,aspx,asp,txt
[+] Follow Redirect:         true
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://TargetIP/home                 (Status: 200) [Size: 1942]
http://TargetIP/login                (Status: 200) [Size: 1942]
Progress: 27684 / 27690 (99.98%)
===============================================================
Finished
===============================================================

```


<p>Navigating to <code>http://TargetIP</code> or <code>http://TargetIP/home</code> I got redirected to <code>http://TargetIP/login</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/9a9df752-ed97-4b91-8827-a5ba8e9d0231)


<br>

<p>Viewed The page source.</p>

<br>

![image](https://github.com/user-attachments/assets/40688f55-dd8b-462b-b55f-fbf87118d9f2)

<br>


<p>Launched <code>Burp Suite</code>, enabled <code>FoxYProxy</code>, and tried to login using <code>researcher</code> : <code>password</code>.<br><br>
Below what was intercepted.<br><br>

Our <code>Input Payload</code> is <code>username=researcher&password=password</code>.</p>

<br>


```bash
POST /login HTTP/1.1
Host: TargetIP
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 37
Origin: http://TargetIP
Connection: keep-alive
Referer: http://TargetIP/login
Upgrade-Insecure-Requests: 1
Priority: u=0, i

username=researcher&password=password

```

<br>

<p>Ran <code>PasswordDiscovery.py</code>.<br>
Discovered <code>natalie</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/34c51a3a-c17a-463d-bb3e-e94374943b50)


<br>

![image](https://github.com/user-attachments/assets/4b300721-5f4f-4105-8656-0c65e5ce3046)



<br>



<br>

<p>Ran <code>PasswordDiscovery.py</code>.<br>
Discovered <code>sk8board</code></p>

![image](https://github.com/user-attachments/assets/76194f1e-2b05-4ea5-8eae-e1c607e453ed)

<br>

![image](https://github.com/user-attachments/assets/3e80ba6b-8d80-4805-8a0c-34cb0c98f627)

<br>
<br>

<p>Now we have <code>natalie</code>:<code>sk8board</code></p>

<br>

<p>Navigated to <code>http://TargetIP</code> again.</p>

<br>

![image](https://github.com/user-attachments/assets/b00e2880-5ef3-4e85-b8d5-631befe350d9)

<br>

![image](https://github.com/user-attachments/assets/806cdb4c-cc2e-4e7b-8732-34245bb01f22)

<br>


![image](https://github.com/user-attachments/assets/0a5a1e59-6b04-45e9-9703-306c4bfcaa89)

<br>

![image](https://github.com/user-attachments/assets/ee22cc80-6524-4b1c-8a3e-3350be3f519f)



<br>
<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center">
<img width="900px" src="https://github.com/user-attachments/assets/628a77fe-6bd1-433e-9c62-71279d7b95e4"><br>
<img width="900px" src="https://github.com/user-attachments/assets/170c1d0e-6eca-469e-9b6b-8db490ddf43c"></p>


<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>


<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |Global        | Brazil       | Global      | Brazil     |          | Completed |           |
| April 12, 2025    | 342      |     286ᵗʰ    |        8ᵗʰ   |    217ᵗʰ    |     2ⁿᵈ    |  93,198  |       656 |   59      |

</div>

<br>



<p align="center"> Global All Time: 290ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/72d1031c-d96b-4bdc-b5cd-1a913b198b75"> </p>

<p align="center"> Brazil All Time: 8ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/9fb390af-8d36-419b-966f-385c4e473fb8"> </p>

<p align="center"> Global monthly: 217ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/0739ecfe-df6d-46d9-b8a3-31db605b53326"> </p>

<p align="center"> Brazil monthly: 2ⁿᵈ<br><br><img width="900px" src="https://github.com/user-attachments/assets/a6c2f602-87bf-47e7-a4eb-bc16eaa9d4fd"> </p>


<br>


<p align="center">Weekly League: 4ᵗʰ Bronze<br><br><img width="900px" src="https://github.com/user-attachments/assets/f3caafb3-aa48-436d-b1dd-3754c223eef2"> </p>

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/tryhackme">tryhackme</a> and  <a href="https://tryhackme.com/p/toxicat0r">toxicat0r</a> for investing your time and effort to develop this walkthrough so that I could sharpen my skills!</p> 

