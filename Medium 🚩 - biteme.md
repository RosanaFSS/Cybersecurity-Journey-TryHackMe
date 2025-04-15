<p align="center">April 14, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{343}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/4fe1cc18-807a-4b4f-8db2-7dc5f7c421ba"></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{biteme}}$$</h1>
<p align="center"><em>Stay out of my server!</em>.<br>
It is classified as a medium-level CTF.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/biteme">here</a>.</p>

<p align="center"> <img width="900px" src=""> </p>


<br>
<br>

<h2>Task 1 . Take a biten </h2>

<p>[  Start Machine  ]</p>

<p>Start the machine and get the flags...</p>


<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 1.1. <em>What is the user flag?</em><br><a id='1.1'></a>
>> <strong><code>______</code></strong><br>
<p></p>

<br>
<br>


<p>Used <code>nmap</code>.<br>
Discovered:<br>
  
-  2 ports open:  <code>22/ssh</code> and <code>80/http</code>.</p>


```bash
:~/bitemet# nmap -Pn -A -p- TargetIP
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.6 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works

```

<br>

<p>Used <code>ffuf</code>.<br>
Discovered:<br>
  
-  there is or are <code>.html</code> files.<br>

```bash
:~/biteme# ffuf -u http://TargetIP/indexFUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/web-extensions.txt

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://TargetIP/indexFUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Discovery/Web-Content/web-extensions.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
________________________________________________

.html                   [Status: 200, Size: 10918, Words: 3499, Lines: 376]
:: Progress: [39/39] :: Job [1/1] :: 21 req/sec :: Duration: [0:00:05] :: Errors: 0 ::


```

-  directory<code>/console</code> and <code>index.html</code>.<br>

```bash

:~/biteme# ffuf -u http://TargetIP/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt -fc 403

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://TargetIP/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
 :: Filter           : Response status: 403
________________________________________________

console                 [Status: 301, Size: 314, Words: 20, Lines: 10]
index.html              [Status: 200, Size: 10918, Words: 3499, Lines: 376]
:: Progress: [4655/4655] :: Job [1/1] :: 125 req/sec :: Duration: [0:00:04] :: Errors: 0 ::
:~/biteme#

```


</p>

<br>

<p>Added <code>TargetIP</code> and a domain name to <code>/etc/hosts</code>.</p>

<br>

<p>Navigated to <code>http://TargetIP</code>.<br><br>
It is a default <code>Apache</code> web page.</p>

<br>

![image](https://github.com/user-attachments/assets/b703bab1-69bd-476d-9902-05b50ce6a0d6)

<br>

<p>Navigated to <code>http://TargetIP/console/</code>.<br><br>
It is a <code>sign in</code> web page with <code>captcha</code>.</p>


<br>

![image](https://github.com/user-attachments/assets/18539297-685a-4289-82d0-1e1dfd9a0ceb)

<br>


<p>Viewed source code.<br><br>Wow ... many discoveries.</p>

<br>

![image](https://github.com/user-attachments/assets/75151f7f-ba7a-4d04-a516-4bee00056de7)

<br>

![image](https://github.com/user-attachments/assets/c72ea93f-33db-47c5-8d50-f045488ee775)

<br>


<p>Used <code>ffuf</code> again to discover which file extensions there are in <code>http://TargetIP/console</code>.<br>
Discovered<br>
  
-  <code>.php</code> <br>
-  <code>.phps</code> </p>

```bash
:~/biteme# ffuf -u http://biteme.thm/console/indexFUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/web-extensions.txt

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://biteme.thm/console/indexFUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Discovery/Web-Content/web-extensions.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
________________________________________________

.php                    [Status: 200, Size: 3961, Words: 306, Lines: 40]
.phps                   [Status: 200, Size: 9325, Words: 297, Lines: 3]
:: Progress: [39/39] :: Job [1/1] :: 26 req/sec :: Duration: [0:00:04] :: Errors: 0 ::
```

<br>

```bash




