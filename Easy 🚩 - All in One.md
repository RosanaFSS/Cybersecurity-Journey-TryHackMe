
<p align="center">March 22, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{320}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
  <img width="160px" src="https://github.com/user-attachments/assets/9b74bcc3-7aa7-4f11-aa81-9d643532d2b6"></p>

  <h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{All in One}}$$
</h1>

<p align="center">This is a fun box where you will get to exploit the system in several ways. Few intended and unintended paths to getting user and root access. It is classified as an easy-level CTF, and you can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed. <a href="https://tryhackme.com/room/allinonemj">All in One</a>.</p>

<p align="center"> <img width="900px" src=""> </p>

<br>
<br>

<h2 align="center">$$\textcolor{white}{\textnormal{Nmap}}$$</h2>

<p align="center">Added the Target_IP and the domain names discovered to /etc/hosts. </p>

<p align="center">There are have 3 ports open: <code>ftp/21</code>, <code>ssh/22</code>, and <code>http/80</code>.<br><code>Anonymous</code> is allowed to <code>ftp</code>. </p>

```bash
:~/Allin1# nmap -sV -sC -sS -A -O -p- -T5 allin1.thm
...
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:Target_IP
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
...
:~/Allin1# 
```

<h2 align="center">$$\textcolor{white}{\textnormal{Service Enumeration}}$$</h2>

<p align="center">Used <code>ffuf</code>: directories and files enumeration.<br> Discovered <code>wordpress</code>, and <code>hackthons</code> directories.</p>


```bash
:~/Allin1# ffuf -c -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt -u http://Target_IP/FUZZ

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://Target_IP/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
________________________________________________

...
wordpress               [Status: 301, Size: 318, Words: 20, Lines: 10]
...
hackathons              [Status: 200, Size: 197, Words: 19, Lines: 64]
...
server-status           [Status: 403, Size: 278, Words: 20, Lines: 10]
:: Progress: [207643/207643] :: Job [1/1] :: 10357 req/sec :: Duration: [0:00:22] :: Errors: 0 ::
:~/Allin1# 
```

<br>
<p align="center">Ran <code>fuff</code> to enumerate <code>wordpress</code>.Discovered <code>wp-content</code>, <code>wp-includes</code>, and <code>wp-admin</code>.</p>

```bash
:~/Allin1# ffuf -c -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt -u http://Target_IP/wordpress/FUZZ

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://Target_IP/wordpress/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
________________________________________________

wp-content              [Status: 301, Size: 329, Words: 20, Lines: 10]
wp-includes             [Status: 301, Size: 330, Words: 20, Lines: 10]
...
wp-admin                [Status: 301, Size: 327, Words: 20, Lines: 10]
...
:: Progress: [207643/207643] :: Job [1/1] :: 16565 req/sec :: Duration: [0:00:23] :: Errors: 0 ::
:~/Allin1# 
```


<br>
<p align="center">Ran <code>fuff</code> to enumerate <code>hackathons</code>.</p>

```bash
~/Allin1# ffuf -c -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt -u http://Target_IP/hackathons/FUZZ

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://Target_IP/hackathons/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
________________________________________________

:: Progress: [207643/207643] :: Job [1/1] :: 12004 req/sec :: Duration: [0:00:22] :: Errors: 0 ::

```

<br>

<p align="center">Used <code>ftp</code>. :-(</p>

```bash
:~/Allin1# ftp 10.10.227.146
Connected to 10.10.227.146.
220 (vsFTPd 3.0.3)
Name (10.10.227.146:root): Anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -lah
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 0        115          4096 Oct 06  2020 .
drwxr-xr-x    2 0        115          4096 Oct 06  2020 ..
226 Directory send OK.
ftp> exit
:~/Allin1#
```

<br>

<h2 align="center">$$\textcolor{white}{\textnormal{Service Enumeration - Wordpress}}$$</h2>

<br>
<p align="center">Used <code>wpscan</code>. Discovered <code>elyana</code>.</p>

```bash
~/Allin1# wpscan --url http://10.10.227.146/wordpress -e u
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.27
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

...
Interesting Finding(s):

...

[+] WordPress readme found: http://10.10.227.146/wordpress/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Upload directory has listing enabled: http://10.10.227.146/wordpress/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

...

[+] WordPress version 5.5.1 identified (Insecure, released on 2020-09-01).
 | Found By: Rss Generator (Passive Detection)
 |  - http://10.10.227.146/wordpress/index.php/feed/, <generator>https://wordpress.org/?v=5.5.1</generator>
 |  - http://10.10.227.146/wordpress/index.php/comments/feed/, <generator>https://wordpress.org/?v=5.5.1</generator>

[+] WordPress theme in use: twentytwenty
 | Location: http://10.10.227.146/wordpress/wp-content/themes/twentytwenty/
 | Last Updated: 2021-03-09T00:00:00.000Z
 | Readme: http://10.10.227.146/wordpress/wp-content/themes/twentytwenty/readme.txt
 | [!] The version is out of date, the latest version is 1.7
 | Style URL: http://10.10.227.146/wordpress/wp-content/themes/twentytwenty/style.css?ver=1.5
 | Style Name: Twenty Twenty
 | Style URI: https://wordpress.org/themes/twentytwenty/
 | Description: Our default theme for 2020 is designed to take full advantage of the flexibility of the block editor...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 |
 | Version: 1.5 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://10.10.227.146/wordpress/wp-content/themes/twentytwenty/style.css?ver=1.5, Match: 'Version: 1.5'

[+] Enumerating Users (via Passive and Aggressive Methods)
 Brute Forcing Author IDs - Time: 00:00:00 <=========================================================================================================================> (10 / 10) 100.00% Time: 00:00:00

[i] User(s) Identified:

[+] elyana
 | Found By: Author Posts - Author Pattern (Passive Detection)
 | Confirmed By:
 |  Rss Generator (Passive Detection)
 |  Wp Json Api (Aggressive Detection)
 |   - http://10.10.227.146/wordpress/index.php/wp-json/wp/v2/users/?per_page=100&page=1
 |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 |  Login Error Messages (Aggressive Detection)

...
:~/Allin1# 
```


<br>
<p>Navigated to <code>http://Target_IP/wordpress/wp-content/plugins/mail-masta/readme.txt</code>.</p>
<p>Damn how much I hate the smell of  Vinegar ...<br>
Encrypted String = Dvc W@iyur@123<br>
Key = KeepGping</p>
<p>Vinegar --> Vignere</p>


<p>http://allin1.thm/hackathons</p>

![image](https://github.com/user-attachments/assets/af1ef93c-20f6-4d5b-b3a1-89832ebab44f)

<br>


<p>Try H@ckme@123 --> H@ckme@123 <br>
elyana : H@ckme@123</p>


![image](https://github.com/user-attachments/assets/85d4808f-7927-4733-8540-2d8808607337)

<br>

<p>http://allin1.thm/wordpress/wp-admin was redirected to http://allin1.thm/wordpress/wp-admin/wp-login.php?redirect_to=http%3A%2F%2Fallin1.thm%2Fwordpress%2Fwp-admin%2F&reauth=1</p>

![image](https://github.com/user-attachments/assets/5370314b-a367-4bbe-8d98-3add872dcb11)












