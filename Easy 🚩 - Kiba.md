<p align="center"><p align="center">April 7, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{336}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
  <img width="160px" src="https://github.com/user-attachments/assets/2618b170-66fb-4cd0-8989-4baf6071e985"></p>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Kiba}}$$</h1>


<p align="center">Identify the critical security flaw in the data visualization dashboard, that allows execute remote code execution. It is classified as an easy-level challenge, and you can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed. Click <a href="https://tryhackme.com/room/kiba">Kiba</a>.</p>

<p align="center"> <img width="900px" src=""> </p>

<br>
<br> It is classified as an easy-level challenge, and you can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed. Click <a href="https://tryhackme.com/room/kiba">Kiba</a>.</p>

<p align="center"> <img width="900px" src=""> </p>

<br>
<br>

<h2 align="center">$$\textcolor{white}{\textnormal{Nmap}}$$</h2>


<p align="center">There are have 3 ports open: <code>ssh/22</code>, <code>http/80</code> and <code>esmagent?/5601</code>. </p>

```bash
oot@ip-10-10-189-214:~# nmap -sC -sV -sS -O -A -Pn -p- 10.10.16.119
Starting Nmap 7.80 ( https://nmap.org ) at 2025-04-08 01:53 BST
Nmap scan report for 10.10.16.119
Host is up (0.00031s latency).
Not shown: 65532 closed ports
PORT     STATE SERVICE   VERSION
22/tcp   open  ssh       OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 9d:f8:d1:57:13:24:81:b6:18:5d:04:8e:d2:38:4f:90 (RSA)
|   256 e1:e6:7a:a1:a1:1c:be:03:d2:4e:27:1b:0d:0a:ec:b1 (ECDSA)
|_  256 2a:ba:e5:c5:fb:51:38:17:45:e7:b1:54:ca:a1:a3:fc (ED25519)
80/tcp   open  http      Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
5601/tcp open  esmagent?
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, Help, Kerberos, LDAPBindReq, LDAPSearchReq, LPDString, RPCCheck, RTSPRequest, SIPOptions, SMBProgNeg, SSLSessionReq, TLSSessionReq, TerminalServerCookie, X11Probe: 
|     HTTP/1.1 400 Bad Request
|   FourOhFourRequest: 
|     HTTP/1.1 404 Not Found
|     kbn-name: kibana
|     kbn-xpack-sig: c4d007a8c4d04923283ef48ab54e3e6c
|     content-type: application/json; charset=utf-8
|     cache-control: no-cache
|     content-length: 60
|     connection: close
|     Date: Tue, 08 Apr 2025 00:53:49 GMT
|     {"statusCode":404,"error":"Not Found","message":"Not Found"}
|   GetRequest: 
|     HTTP/1.1 302 Found
|     location: /app/kibana
|     kbn-name: kibana
|     kbn-xpack-sig: c4d007a8c4d04923283ef48ab54e3e6c
|     cache-control: no-cache
|     content-length: 0
|     connection: close
|     Date: Tue, 08 Apr 2025 00:53:49 GMT
|   HTTPOptions: 
|     HTTP/1.1 404 Not Found
|     kbn-name: kibana
|     kbn-xpack-sig: c4d007a8c4d04923283ef48ab54e3e6c
|     content-type: application/json; charset=utf-8
|     cache-control: no-cache
|     content-length: 38
|     connection: close
|     Date: Tue, 08 Apr 2025 00:53:49 GMT
|_    {"statusCode":404,"error":"Not Found"}
...
```

<br>

<h2 align="center">$$\textcolor{white}{\textnormal{Kibana}}$$</h2>
<p>Kibana versions before 5.6.15 and 6.6.1 contain an arbitrary code execution flaw.</p>




<br>

<h2 align="center">$$\textcolor{white}{\textnormal{Navigated to http://TargetIP:5601}}$$</h2>

![image](https://github.com/user-attachments/assets/db494326-46c0-418c-81ca-4aaaf48f54f7)

<br>

![image](https://github.com/user-attachments/assets/4bdaf403-5030-4c5e-adb1-66183ce154ac)

<br>


<h2 align="center">$$\textcolor{white}{\textnormal{ve-2019-7609}}$$</h2>

https://nvd.nist.gov/vuln/detail/cve-2019-7609

![image](https://github.com/user-attachments/assets/0b3b8237-3715-4e9f-bf03-f73056bba5dd)




