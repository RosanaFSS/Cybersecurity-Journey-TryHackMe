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

<p>And again and again to discover enumerate directories and files.</p>

```bash
~/biteme# ffuf -u http://TargetIP/console/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt -fc 403 -e .php,.phps

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://TargetIP/console/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt
 :: Extensions       : .php .phps 
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
 :: Filter           : Response status: 403
________________________________________________

config.php              [Status: 200, Size: 0, Words: 1, Lines: 1]
css                     [Status: 301, Size: 318, Words: 20, Lines: 10]
dashboard.php           [Status: 302, Size: 0, Words: 1, Lines: 1]
config.phps             [Status: 200, Size: 354, Words: 17, Lines: 4]
functions.php           [Status: 200, Size: 0, Words: 1, Lines: 1]
functions.phps          [Status: 200, Size: 2010, Words: 93, Lines: 4]
index.phps              [Status: 200, Size: 9325, Words: 297, Lines: 3]
index.php               [Status: 200, Size: 3961, Words: 306, Lines: 40]
index.php               [Status: 200, Size: 3961, Words: 306, Lines: 40]
robots.txt              [Status: 200, Size: 25, Words: 3, Lines: 2]
securimage              [Status: 301, Size: 325, Words: 20, Lines: 10]
:: Progress: [13965/13965] :: Job [1/1] :: 314 req/sec :: Duration: [0:00:04] :: Errors: 0 ::
:~/biteme# 
```

<p>And again and again and again to enumerate <code>securimage</code>.<br>
Pay attention: it is NOT  <code>secureimage</code>.<br>I lost a bit of time here.</p>

```bash
:~/biteme# ffuf -u http://biteme.thm/console/securimage/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt -fr '/\..*'

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://biteme.thm/console/securimage/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
 :: Filter           : Regexp: /\..*
________________________________________________

audio                   [Status: 301, Size: 331, Words: 20, Lines: 10]
backgrounds             [Status: 301, Size: 337, Words: 20, Lines: 10]
database                [Status: 301, Size: 334, Words: 20, Lines: 10]
examples                [Status: 301, Size: 334, Words: 20, Lines: 10]
.htpasswd               [Status: 403, Size: 277, Words: 20, Lines: 10]
images                  [Status: 301, Size: 332, Words: 20, Lines: 10]
.hta                    [Status: 403, Size: 277, Words: 20, Lines: 10]
.htaccess               [Status: 403, Size: 277, Words: 20, Lines: 10]
:: Progress: [4655/4655] :: Job [1/1] :: 49 req/sec :: Duration: [0:00:05] :: Errors: 0 ::
:~/biteme# 

```
 
<br>

![image](https://github.com/user-attachments/assets/e7d387e2-a5a7-4511-b332-6d1b0e2c2770)

<br>

<p>Navigated to <code>http://TargetIP/console/config.phps</code>.<br><br>
Discovered a <code>LOGIN_USER</code>:<code>6a61736f6e5f746573745f6163636f756e74</code>.</p>


<br>

![image](https://github.com/user-attachments/assets/7d7cb122-aebd-428c-bcc7-42614440bc53)

<br>

<br>

<p>Navigated to <code>http://TargetIP/console/index.phps</code>.<br><br>
There are details of the access method.<br>
Ii is a friendlier view of the source code of <code>index.html</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/ea634c53-ea5f-49a5-b28e-b75672cbdeae)

<br>

<p>Navigated to <code>http://TargetIP/console/functions.phps</code>.<br><br>
Discovered <code>bin2hex</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/6de91091-4eeb-4c8a-9917-89d01515fdd6)



<br>

<p>Used <code>CyberChef</code>.<br><br>Discovered<code>jason_test_account</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/1dc17bab-0ff1-488e-8fa6-18c3c0103cb0)

<br>






