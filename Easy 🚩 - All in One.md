
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
<p align="center">Used <code>wpscan</code>. Discovered <code>mail-masta</code>, and <code>http://Target_IP/wordpress/wp-content/plugins/mail-masta/readme.txt</code>.</p>

```bash
:~/Allin1# wpscan --url http://Target_IP/wordpress -e ap
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

[+] Headers
 | Interesting Entry: Server: Apache/2.4.29 (Ubuntu)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://Target_IP/wordpress/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://Target_IP6/wordpress/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Upload directory has listing enabled: http://Target_IP/wordpress/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://Target_IP/wordpress/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 5.5.1 identified (Insecure, released on 2020-09-01).
 | Found By: Rss Generator (Passive Detection)
 |  - http://Target_IP/wordpress/index.php/feed/, <generator>https://wordpress.org/?v=5.5.1</generator>
 |  - http://Target_IP/wordpress/index.php/comments/feed/, <generator>https://wordpress.org/?v=5.5.1</generator>

[+] WordPress theme in use: twentytwenty
 | Location: http://Target_IP/wordpress/wp-content/themes/twentytwenty/
 | Last Updated: 2021-03-09T00:00:00.000Z
 | Readme: http://Target_IP/wordpress/wp-content/themes/twentytwenty/readme.txt
 | [!] The version is out of date, the latest version is 1.7
 | Style URL: http://Target_IP/wordpress/wp-content/themes/twentytwenty/style.css?ver=1.5
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
 |  - http://10.10.227.146Target_IP/wordpress/wp-content/themes/twentytwenty/style.css?ver=1.5, Match: 'Version: 1.5'

[+] Enumerating All Plugins (via Passive Methods)
[+] Checking Plugin Versions (via Passive and Aggressive Methods)

[i] Plugin(s) Identified:

[+] mail-masta
 | Location: http://Target_IP/wordpress/wp-content/plugins/mail-masta/
 | Latest Version: 1.0 (up to date)
 | Last Updated: 2014-09-19T07:52:00.000Z
 |
 | Found By: Urls In Homepage (Passive Detection)
 |
 | Version: 1.0 (80% confidence)
 | Found By: Readme - Stable Tag (Aggressive Detection)
 |  - http://Target_IP/wordpress/wp-content/plugins/mail-masta/readme.txt

[+] reflex-gallery
 | Location: http://Target_IP/wordpress/wp-content/plugins/reflex-gallery/
 | Latest Version: 3.1.7 (up to date)
 | Last Updated: 2021-03-10T02:38:00.000Z
 |
 | Found By: Urls In Homepage (Passive Detection)
 |
 | Version: 3.1.7 (80% confidence)
 | Found By: Readme - Stable Tag (Aggressive Detection)
 |  - http://Target_IP/wordpress/wp-content/plugins/reflex-gallery/readme.txt

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register
...
:~/Allin1# 
```


<br>
<p>Navigated to <code>http://Target_IP/wordpress/wp-content/plugins/mail-masta/readme.txt</code>.</p>

```bash
== Mail Masta ===

Contributors: mailmasta

Donate link: http://getmailmasta.com/

Tags: mail masta, autoresponder, automation, newsletters, campaigns, signup form, newsletter widget, marketing, email, notification, smtp, amazon ses

Requires at least: 3.0.1

Tested up to: 4.0.0

Stable tag: 1.0

License: GPLv2 or later

License URI: http://www.gnu.org/licenses/gpl-2.0.html



Freaking best newsletters, autoresponders, singup forms and reports for WordPress.



== Description ==



We love email marketing, so we made newsletter plugin that is full featured, beautiful and simple to use.

= Features =

* Highest deliverability of emails with Amazon SES
* Send and schedule campaigns
* Track opens, clicks and unsubscribes
* Lists of subscribers
* Signup forms
* Track countries
* Personalized mass email
* Full automatization of your site
* Beautiful design
* 24/7 support
* New features will be released regularly


== Installation ==



3 ways to install the plugin:



= 1. lazy approach (search & add) =

1. WordPress Admin > menu Plugins > Add

1. Search for `Mail Masta`

1. Install

1. Activate the plugin

1. A new menu `Mail Masta` will appear in your Admin



= 2. standard approach (upload) =

1. Download the plugin (.zip file) on the right column of this page

1. WordPress Admin > menu Plugins > Add

1. Select the tab "Upload"

1. Upload the .zip file

1. Activate the plugin

1. A new menu `Mail Masta` will appear in your Admin



= 3. hacker approach (FTP) =

1. Upload `mail-masta` folder to the `/wp-content/plugins/` directory through FTP

1. Activate the plugin through the 'Plugins' menu in WordPress

1. A new menu `Mail Masta` will appear in your Admin



== Frequently Asked Questions ==



You can <a href='http://getmailmasta.com/contact/'>ping Akil</a> for any questions. Sorry Akil, I know you hate me now.



== Screenshots ==


1. Overview of email campaigns

2. Report of campaign showing its open, click and unsubscribe rate

3. Second part of campaign report with map info of subscribers, link activity, last 10 opened emails and last 10 clicked links


== Changelog ==



= 1.0.0 =

* After months of hard work finally the release. We are broke, but happy.




![image](https://github.com/user-attachments/assets/0599826d-3aac-49dd-b6dc-42835d1f4cf4)

<br>

![image](https://github.com/user-attachments/assets/cdb2d590-5ff4-4762-b431-1cb82fc5b938)


<br>]
<p>Damn how much I hate the smell of  Vinegar ...<br>
Dvc W@iyur@123</p>

![image](https://github.com/user-attachments/assets/2033d795-5e74-46c8-957e-88ec4b16ef0b)


<br>


<p>i7md, i7m4d</p>

![image](https://github.com/user-attachments/assets/82ac062e-b77c-4f3b-b2d7-9d623ea25491)

<br>

![image](https://github.com/user-attachments/assets/27b4e0fd-97cd-4437-914c-80493ff3f132)


<br>
```

<p>http://allin1.thm/wordpress/wp-content/plugins/mail-masta/</p>

![image](https://github.com/user-attachments/assets/515adf30-48a2-4b30-aba2-393ae1601ca7)





<p>http://allin1.thm/wordpress/wp-content/plugins/mail-masta/inc/campaign/</p>

![image](https://github.com/user-attachments/assets/06f7434a-b6ba-416c-b7f6-9736b0eff06c)








