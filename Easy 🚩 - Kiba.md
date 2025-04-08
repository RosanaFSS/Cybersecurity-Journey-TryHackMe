<p align="center">April 7, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{336}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
  <img width="160px" src="https://github.com/user-attachments/assets/2618b170-66fb-4cd0-8989-4baf6071e985"></p>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Kiba}}$$</h1>


<p align="center"><p align="center">April 7, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{336}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
  <img width="160px" src="https://github.com/user-attachments/assets/2618b170-66fb-4cd0-8989-4baf6071e985"></p>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Source}}$$</h1>


<p align="center">Exploit a recent vulnerability and hack Webmin, a web-based system configuration tool. It is classified as an easy-level challenge, and you can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed. Click <a href="https://tryhackme.com/room/source">Source</a>.</p>

<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/fc1265c6-2733-4273-9cb7-bb0dfddf3ffd"> </p>

<br>
<br> It is classified as an easy-level challenge, and you can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed. Click <a href="https://tryhackme.com/room/kiba">Kiba</a>.</p>

<p align="center"> <img width="900px" src=""> </p>

<br>
<br>

<h2 align="center">$$\textcolor{white}{\textnormal{Nmap}}$$</h2>


<p align="center">There are have 2 ports open: <code>ssh/22</code> and <code>webmin/10000</code>. </p>

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
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port5601-TCP:V=7.80%I=7%D=4/8%Time=67F4739D%P=x86_64-pc-linux-gnu%r(Get
SF:Request,D4,"HTTP/1\.1\x20302\x20Found\r\nlocation:\x20/app/kibana\r\nkb
SF:n-name:\x20kibana\r\nkbn-xpack-sig:\x20c4d007a8c4d04923283ef48ab54e3e6c
SF:\r\ncache-control:\x20no-cache\r\ncontent-length:\x200\r\nconnection:\x
SF:20close\r\nDate:\x20Tue,\x2008\x20Apr\x202025\x2000:53:49\x20GMT\r\n\r\
SF:n")%r(HTTPOptions,117,"HTTP/1\.1\x20404\x20Not\x20Found\r\nkbn-name:\x2
SF:0kibana\r\nkbn-xpack-sig:\x20c4d007a8c4d04923283ef48ab54e3e6c\r\nconten
SF:t-type:\x20application/json;\x20charset=utf-8\r\ncache-control:\x20no-c
SF:ache\r\ncontent-length:\x2038\r\nconnection:\x20close\r\nDate:\x20Tue,\
SF:x2008\x20Apr\x202025\x2000:53:49\x20GMT\r\n\r\n{\"statusCode\":404,\"er
SF:ror\":\"Not\x20Found\"}")%r(RTSPRequest,1C,"HTTP/1\.1\x20400\x20Bad\x20
SF:Request\r\n\r\n")%r(RPCCheck,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\n
SF:\r\n")%r(DNSVersionBindReqTCP,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\
SF:n\r\n")%r(DNSStatusRequestTCP,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\
SF:n\r\n")%r(Help,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\n\r\n")%r(SSLSe
SF:ssionReq,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\n\r\n")%r(TerminalSer
SF:verCookie,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\n\r\n")%r(TLSSession
SF:Req,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\n\r\n")%r(Kerberos,1C,"HTT
SF:P/1\.1\x20400\x20Bad\x20Request\r\n\r\n")%r(SMBProgNeg,1C,"HTTP/1\.1\x2
SF:0400\x20Bad\x20Request\r\n\r\n")%r(X11Probe,1C,"HTTP/1\.1\x20400\x20Bad
SF:\x20Request\r\n\r\n")%r(FourOhFourRequest,12D,"HTTP/1\.1\x20404\x20Not\
SF:x20Found\r\nkbn-name:\x20kibana\r\nkbn-xpack-sig:\x20c4d007a8c4d0492328
SF:3ef48ab54e3e6c\r\ncontent-type:\x20application/json;\x20charset=utf-8\r
SF:\ncache-control:\x20no-cache\r\ncontent-length:\x2060\r\nconnection:\x2
SF:0close\r\nDate:\x20Tue,\x2008\x20Apr\x202025\x2000:53:49\x20GMT\r\n\r\n
SF:{\"statusCode\":404,\"error\":\"Not\x20Found\",\"message\":\"Not\x20Fou
SF:nd\"}")%r(LPDString,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\n\r\n")%r(
SF:LDAPSearchReq,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\n\r\n")%r(LDAPBi
SF:ndReq,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\n\r\n")%r(SIPOptions,1C,
SF:"HTTP/1\.1\x20400\x20Bad\x20Request\r\n\r\n");
MAC Address: 02:13:8E:9F:C9:7F (Unknown)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.80%E=4%D=4/8%OT=22%CT=1%CU=32787%PV=Y%DS=1%DC=D%G=Y%M=02138E%TM
OS:=67F473A9%P=x86_64-pc-linux-gnu)SEQ(SP=107%GCD=1%ISR=10A%TI=Z%CI=I%II=I%
OS:TS=8)OPS(O1=M2301ST11NW7%O2=M2301ST11NW7%O3=M2301NNT11NW7%O4=M2301ST11NW
OS:7%O5=M2301ST11NW7%O6=M2301ST11)WIN(W1=68DF%W2=68DF%W3=68DF%W4=68DF%W5=68
OS:DF%W6=68DF)ECN(R=Y%DF=Y%T=40%W=6903%O=M2301NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=
OS:40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%
OS:O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=4
OS:0%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%
OS:Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=
OS:Y%DFI=N%T=40%CD=S)

Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.31 ms 10.10.16.119

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 27.15 seconds
root@ip-10-10-189-214:~# 


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




