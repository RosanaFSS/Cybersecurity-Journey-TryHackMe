<h1 align="center">Plotted-EMR</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/c73c4e43-529b-43a1-9cdd-57930a7382db"><br>
August 30, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>481</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Everything here is plotted!</em>.<br>
Access it <a href="https://tryhackme.com/room/plottedemr"</a>here.<br>
<img width="1200px" src=""></p>

.

<br>
<br>

<h2>Task 1 . Introduction</h2>
<p>Happy Hunting!<br>

Note: This machine may take up to 5 mins to start its services fully.<br>

Tip: Enumeration is key!</p>

<p><em>Answer the question below</em></p>

<p>1.1. Ready<br>
<code>No answer needed</code></p>

<h2>Task 2 . Compromise</h2>

<p><em>Answer the questions below</em></p>

<p>2.1. What is flag 1?<br>
<code>______</code></p>

<p>2.2. What is flag 2?<br>
<code>______</code></p>

<p>2.2. What is flag 2?<br>
<code>______</code></p>



<h2>Nmap</h2>

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

<h2>Gobuster</h2>

```bash
:~# gobuster dir -u http://xx.xxx.xx.xxx/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 80
...
/admin                (Status: 200) [Size: 33]
/shadow               (Status: 200) [Size: 61]
/passwd               (Status: 200) [Size: 61]
/server-status        (Status: 403) [Size: 278]
```

```bash
:~# gobuster dir -u http://xx.xxx.xx.xxx:8890/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 80
...
/portal               (Status: 301) [Size: 322] [--> http://xx.xxx.xx.xxx:8890/portal/]
/80                   (Status: 301) [Size: 318] [--> http://xx.xxx.xx.xxx:8890/80/]
/server-status        (Status: 403) [Size: 280]
Progress: 218275 / 218276 (100.00%)
```

<h2>xx.xxx.xx.xxx:8890/portal</h2>
<p>

- redirects xx.xxx.xx.xxx:8890/portal/interface/login/login.php?site=default</p>

<img width="1103" height="371" alt="image" src="https://github.com/user-attachments/assets/1952d0b6-179c-40a5-b128-3436ec52c782" />

<img width="1112" height="517" alt="image" src="https://github.com/user-attachments/assets/33f62a5b-c598-46eb-9df5-d5083aae1f34" />

<p>

- /admin.php<br>
- /LICENSE<br>
- setup.php<br>
- /index.php  --> interface/login/login.php?site=default<br>
- /controller.php</p>

```bash
:~# gobuster dir -u http://xx.xxx.xx.xxx:8890/portal/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 80 -x php
...
/templates            (Status: 301) [Size: 332] [--> http://xx.xxx.xx.xxx:8890/portal/templates/]
/services             (Status: 301) [Size: 331] [--> http://xx.xxx.xx.xxx:8890/portal/services/]
/modules              (Status: 301) [Size: 330] [--> http://xx.xxx.xx.xxx:8890/portal/modules/]
/common               (Status: 301) [Size: 329] [--> http://xx.xxx.xx.xxx:8890/portal/common/]
/library              (Status: 301) [Size: 330] [--> http://xx.xxx.xx.xxx:8890/portal/library/]
/public               (Status: 301) [Size: 329] [--> http://xx.xxx.xx.xxx:8890/portal/public/]
/version.php          (Status: 200) [Size: 0]
/admin.php            (Status: 200) [Size: 937]
/portal               (Status: 403) [Size: 280]
/tests                (Status: 301) [Size: 328] [--> http://xx.xxx.xx.xxx:8890/portal/tests/]
/sites                (Status: 301) [Size: 328] [--> http://xx.xxx.xx.xxx:8890/portal/sites/]
/custom               (Status: 301) [Size: 329] [--> http://xx.xxx.xx.xxx:8890/portal/custom/]
/contrib              (Status: 301) [Size: 330] [--> http://xx.xxx.xx.xxx:8890/portal/contrib/]
/interface            (Status: 301) [Size: 332] [--> http://xx.xxx.xx.xxx:8890/portal/interface/]
/vendor               (Status: 301) [Size: 329] [--> http://xx.xxx.xx.xxx:8890/portal/vendor/]
/config               (Status: 301) [Size: 329] [--> http://xx.xxx.xx.xxx:8890/portal/config/]
/setup.php            (Status: 200) [Size: 1214]
/images               (Status: 301) [Size: 329] [--> http://xx.xxx.xx.xxx:8890/portal/images/]
/index.php            (Status: 302) [Size: 0] [--> interface/login/login.php?site=default]
/.php                 (Status: 403) [Size: 280]
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
/controllers          (Status: 301) [Size: 334] [--> http://xx.xxx.xx.xxx:8890/portal//controllers/]
Progress: 654825 / 654828 (100.00%)
```

<p>

- /index.php<br>
- /logout.php</p>

```bash
:~# gobuster dir -u http://xx.xxx.xx.xxx:8890/portal/interface/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 80 -x php
...
/.php                 (Status: 403) [Size: 280]
/index.php            (Status: 200) [Size: 37]
/login                (Status: 301) [Size: 338] [--> http://10.201.15.123:8890/portal/interface/login/]
/main                 (Status: 301) [Size: 337] [--> http://10.201.15.123:8890/portal/interface/main/]
/themes               (Status: 301) [Size: 339] [--> http://10.201.15.123:8890/portal/interface/themes/]
/modules              (Status: 301) [Size: 340] [--> http://10.201.15.123:8890/portal/interface/modules/]
/reports              (Status: 301) [Size: 340] [--> http://10.201.15.123:8890/portal/interface/reports/]
/forms                (Status: 301) [Size: 338] [--> http://10.201.15.123:8890/portal/interface/forms/]
/pic                  (Status: 301) [Size: 336] [--> http://10.201.15.123:8890/portal/interface/pic/]
/language             (Status: 301) [Size: 341] [--> http://10.201.15.123:8890/portal/interface/language/]
/logout.php           (Status: 200) [Size: 37]
/orders               (Status: 301) [Size: 339] [--> http://10.201.15.123:8890/portal/interface/orders/]
/new                  (Status: 301) [Size: 336] [--> http://10.201.15.123:8890/portal/interface/new/]
/drugs                (Status: 301) [Size: 338] [--> http://10.201.15.123:8890/portal/interface/drugs/]
/fax                  (Status: 301) [Size: 336] [--> http://10.201.15.123:8890/portal/interface/fax/]
/practice             (Status: 301) [Size: 341] [--> http://10.201.15.123:8890/portal/interface/practice/]
/billing              (Status: 301) [Size: 340] [--> http://10.201.15.123:8890/portal/interface/billing/]
/super                (Status: 403) [Size: 280]
/usergroup            (Status: 301) [Size: 342] [--> http://10.201.15.123:8890/portal/interface/usergroup/]
/globals.php          (Status: 200) [Size: 37]
/esign                (Status: 301) [Size: 338] [--> http://10.201.15.123:8890/portal/interface/esign/]
/product_registration (Status: 301) [Size: 353] [--> http://10.201.15.123:8890/portal/interface/product_registration/]
/clickmap             (Status: 301) [Size: 341] [--> http://10.201.15.123:8890/portal/interface/clickmap/]
Progress: 654825 / 654828 (100.00%)
```

<h2>xx.xxx.xx.xxx:8890/portal/admin.php</h2>
<p>

- Site ID = default<br>
- DB Name = opememr<br>
- Site Name = OpenEMR<br>
- Version  = 5.0.1 (3)<br>
- Action = <code>Login</code><br>
- <code>Add New Site</code></p>

<img width="1124" height="120" alt="image" src="https://github.com/user-attachments/assets/b2faea4a-0988-453e-833d-b84c94f859ca" />

<h2>xx.xxx.xx.xxx:8890/portal/setup.php</h2>
<p>

- Site ID: default <code>Continue</code></p>

<img width="1128" height="275" alt="image" src="https://github.com/user-attachments/assets/6dcc8615-55ac-4f4b-b1ff-ed0dd52ca6ba" />









