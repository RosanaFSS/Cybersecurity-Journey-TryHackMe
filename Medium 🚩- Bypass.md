
<p><em>Answer the questions below</em></p>



<h3>Nmap</h3>

```bash
:~# nmap -sC -sV -Pn -T4 -p- cctv.thm
Starting Nmap 7.80 ( https://nmap.org ) at 2025-08-23 01:23 BST
Nmap scan report for cctv.thm (10.201.7.109)
Host is up (0.00075s latency).
Not shown: 65532 filtered ports
PORT    STATE SERVICE VERSION
22/tcp  open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.9 (Ubuntu Linux; protocol 2.0)
80/tcp  open  http    Apache httpd 2.4.41
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: 403 Forbidden
443/tcp open  ssl/ssl Apache httpd (SSL-only mode)
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: 403 Forbidden
| ssl-cert: Subject: commonName=cctv.thm/organizationName=cctv.thm/stateOrProvinceName=Tokyo/countryName=AU
| Not valid before: 2023-08-30T10:08:16
|_Not valid after:  2024-08-29T10:08:16
| tls-alpn: 
|_  http/1.1
MAC Address: 16:FF:EC:EC:B7:03 (Unknown)
Service Info: Host: default; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 104.56 seconds
```

<h3>Web port 80</h3>
<br>

<img width="1061" height="670" alt="image" src="https://github.com/user-attachments/assets/ad575ec8-3580-49ba-a3f7-db2e1d562da8" />

<br>
<br>


<img width="1052" height="569" alt="image" src="https://github.com/user-attachments/assets/e4f1e2d7-4793-4b38-a1b4-97fcea4571b2" />

<br>
<br>

<img width="1056" height="247" alt="image" src="https://github.com/user-attachments/assets/ca64e4e2-9b4f-46cf-8ee8-a52db4bfc385" />

<br>
<br>

<img width="1057" height="374" alt="image" src="https://github.com/user-attachments/assets/7db2b0de-0c83-4e40-ae1f-10879017905a" />

<br>
<br>
<h3>Make a UDP request to the machine with source port number 5000. Once done, you can fetch the flag through /fpassword.php?id=1</h3>
<br>

```bash
:~# nc -u -p 5000 cctv.thm 6666
hi
```

<br>

```bash
https://cctv.thm/fpassword.php/?id=1?
```

<img width="1060" height="166" alt="image" src="https://github.com/user-attachments/assets/9e37967b-7250-4ebc-9e36-a380bffc42a0" />

<br>
<br>

<p>1.1. What is the flag value after accessing the endpoint cctv.thm/fpassword.php?id=1?<br>
<code>THM{10001}</code></p>

<br>
<br>
<h3>Make a TCP request to fpassword.php?id=2 with user-agent set as "I am Steve Friend". Once done, you can fetch the flag through /fpassword.php?id=2</h3>
<br>

```bash
:~# curl -s 'http://cctv.thm/' -H 'User-Agent: I am Steve Friend'
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>403 Forbidden</title>
</head><body>
<h1>Forbidden</h1>
<p>You don't have permission to access this resource.</p>
<hr>
<address>Apache/2.4.41 (Ubuntu) Server at cctv.thm Port 80</address>
</body></html>
```

<br>

```bash
https://cctv.thm/fpassword.php/?id=2?
```

<br>
<br>

<img width="1057" height="166" alt="image" src="https://github.com/user-attachments/assets/3b7d6729-6161-4a9e-b149-7a4b6dc22888" />

<br>
<br>

<p>1.2. What is the flag value after accessing the endpoint cctv.thm/fpassword.php?id=2?<br>
<code>THM{10125}</code></p>


<br>
<br>
<h3>Send a ping packet to the machine appearing as Mozilla browser (Hint: packet content with user agent set as Mozilla). Once done, you can fetch the flag through /fpassword.php?id=3</h3>
<br>

```bash
:~# echo -n Mozilla | xxd -p
4d6f7a696c6c61
```

<br>

```bash
:~# ping -c 2 cctv.thm -p 4d6f7a696c6c61
PATTERN: 0x4d6f7a696c6c61
PING cctv.thm (10.201.7.109) 56(84) bytes of data.
64 bytes from cctv.thm (10.201.7.109): icmp_seq=1 ttl=64 time=0.911 ms
64 bytes from cctv.thm (10.201.7.109): icmp_seq=2 ttl=64 time=0.552 ms

--- cctv.thm ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1001ms
rtt min/avg/max/mdev = 0.552/0.731/0.911/0.179 ms
```

<br>

```bash
https://cctv.thm/fpassword.php/?id=3?
```

<br>
<br>

<img width="1056" height="241" alt="image" src="https://github.com/user-attachments/assets/af301fb2-e06a-42c9-aeca-c8e0df03a571" />

<br>
<br>

<p>1.3. What is the flag value after accessing the endpoint cctv.thm/fpassword.php?id=3?<br>
<code>THM{13231}</code></p>

<br>
<br>
<h3>Attempt to login to the FTP server with content containing the word "user" in it. Once done, you can fetch the flag from /fpassword.php?id=4</h3>
<br>

```bash
:~# ftp huser@cctv.thm
```

<br>

```bash
https://cctv.thm/fpassword.php/?id=4?
```

<br>
<br>

<img width="1062" height="171" alt="image" src="https://github.com/user-attachments/assets/7ff9068a-aabe-414a-9eeb-55cdcbc9bc45" />

<br>
<br>

<p>1.4. What is the flag value after accessing the endpoint cctv.thm/fpassword.php?id=4?<br>
<code>THM{33120}</code></p>

<br>
<br>
<h3>Send TCP request to flagger.cgi endpoint with a host header containing more than 50 characters. Once done, you can fetch the flag from /fpassword.php?id=5</h3>
<br>

```bash
:~# for i in {1..50}; do echo -n A; done; echo
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
```

<br>

```bash
:~# curl -s 'http://cctv.thm/flagger.cgi' -H 'Host: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>403 Forbidden</title>
</head><body>
<h1>Forbidden</h1>
<p>You don't have permission to access this resource.</p>
<hr>
<address>Apache/2.4.41 (Ubuntu) Server at aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa Port 80</address>
</body></html>
```

<br>
<br>

<img width="1057" height="188" alt="image" src="https://github.com/user-attachments/assets/310b18fe-d055-4bfe-a362-9d995cf2fd15" />

<br>
<br>

<p>1.5. What is the flag value after accessing the endpoint cctv.thm/fpassword.php?id=5?<br>
<code>THM{12319}</code></p>

<br>
<br>

