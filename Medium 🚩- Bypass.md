<h1 align="center">Bypass</h1>
<p align="center">2025, August 23<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>474</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Use your defence evasion skills to take control of a secure network.</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/8cab783d-2a47-4e1b-bb76-71ba226fa3b1"><br>
Access this TryHackMe´s walkthrough <a href="https://tryhackme.com/room/bypass">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/a692f188-386c-49ad-a516-3c47e7ea5dde"></p>

<br>
<h2>Task 1 . Bypass</h2>

<p>Start the VM by clicking the <code>Start Machine</code> button at the top right of the task. You can complete the challenge by connecting through a VPN or the AttackBox containing all the essential tools.</p>

<p><em>The network security team has implemented state-of-the-art protection mechanisms using an IDS. Your task is to bypass the network security solution and gain access to the CCTV web panel of the company.</em></p>

<p><em>Answer the questions below</em></p>

<br>



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

<img width="1061" height="670" alt="image" src="https://github.com/user-attachments/assets/ad575ec8-3580-49ba-a3f7-db2e1d562da8" />

<br>
<br>


<img width="1052" height="569" alt="image" src="https://github.com/user-attachments/assets/e4f1e2d7-4793-4b38-a1b4-97fcea4571b2" />

<br>
<h3>Web port 80 /mail</h3>

<img width="1056" height="247" alt="image" src="https://github.com/user-attachments/assets/ca64e4e2-9b4f-46cf-8ee8-a52db4bfc385" />

<br>
<h3>Web port 80 /mail/dump.txt</h3>

```bash
From: steve@cctv.thm
To: mark@cctv.thm
Subject: Important Credentials

Hey Mark,

I have completed all the formalities for securing our CCTV web panel (cctv.thm:443). I have installed Suricata to automatically detect any invalid connection and enabled two-layer protection for the web panel. I will SMS you the passwords but incase if you misplace them, there is no possibility for recovery. 

We can recover the password only if we send some specially crafted packets 	
-	Make a UDP request to the machine with source port number 5000. Once done, you can fetch the flag through /fpassword.php?id=1
-	Make a TCP request to fpassword.php?id=2 with user-agent set as "I am Steve Friend". Once done, you can fetch the flag through /fpassword.php?id=2
-	Send a ping packet to the machine appearing as Mozilla browser (Hint: packet content with user agent set as Mozilla). Once done, you can fetch the flag through /fpassword.php?id=3
-	Attempt to login to the FTP server with content containing the word "user" in it. Once done, you can fetch the flag from /fpassword.php?id=4
-	Send TCP request to flagger.cgi endpoint with a host header containing more than 50 characters. Once done, you can fetch the flag from /fpassword.php?id=5

After receiving all the flags, you can visit the MACHINE IP that will ask you for the password. The first password will be concatenated values of all five flags you have received above.

For the second layer of security, I have enabled a wholly sandboxed login environment with no connection to the database and no possibility of command execution. The username is the computer's hostname, and the password is the same as the previous password. I will SMS you the details as well.


See ya soon

Steve
Dev Ops Engineer
```

<br>

<img width="1057" height="374" alt="image" src="https://github.com/user-attachments/assets/7db2b0de-0c83-4e40-ae1f-10879017905a" />

<br>
<br>
<h3>Crafted Packets</h3>

<p>1.1. What is the flag value after accessing the endpoint cctv.thm/fpassword.php?id=1?<br>
<code>THM{10001}</code></p>

<h4>Make a <code>UDP</code> request<br>to the machine with source port number 5000.<br>Once done, you can fetch the flag through /fpassword.php?id=1</h4>

```bash
:~# nc -u -p 5000 cctv.thm 6666
hi
```

```bash
https://cctv.thm/fpassword.php/?id=1?
```

<img width="1060" height="166" alt="image" src="https://github.com/user-attachments/assets/9e37967b-7250-4ebc-9e36-a380bffc42a0" />

<br>
<br>
<p>1.2. What is the flag value after accessing the endpoint cctv.thm/fpassword.php?id=2?<br>
<code>THM{10125}</code></p>

<h4>Make a <code>TCP</code> request<br>to fpassword.php?id=2 with user-agent set as "I am Steve Friend".<br>Once done, you can fetch the flag through /fpassword.php?id=2</h4>

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

```bash
https://cctv.thm/fpassword.php/?id=2?
```

<img width="1057" height="166" alt="image" src="https://github.com/user-attachments/assets/3b7d6729-6161-4a9e-b149-7a4b6dc22888" />

<br>
<br>
<p>1.3. What is the flag value after accessing the endpoint cctv.thm/fpassword.php?id=3?<br>
<code>THM{13231}</code></p>

<h4>Send a <code>ping</code> packet<br>to the machine appearing as Mozilla browser<br>(Hint: packet content with user agent set as Mozilla).<br>Once done, you can fetch the flag through /fpassword.php?id=3</h4>

```bash
:~# echo -n Mozilla | xxd -p
4d6f7a696c6c61
```

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

```bash
https://cctv.thm/fpassword.php/?id=3?
```

<img width="1056" height="241" alt="image" src="https://github.com/user-attachments/assets/af301fb2-e06a-42c9-aeca-c8e0df03a571" />

<br>
<br>
<p>1.4. What is the flag value after accessing the endpoint cctv.thm/fpassword.php?id=4?<br>
<code>THM{33120}</code></p>

<h4>Attempt to login to the <code>FTP</code> server<br>with content containing the word "user" in it.<br>Once done, you can fetch the flag from /fpassword.php?id=4</h4>

```bash
:~# ftp huser@cctv.thm
```

```bash
https://cctv.thm/fpassword.php/?id=4?
```
<img width="1062" height="171" alt="image" src="https://github.com/user-attachments/assets/7ff9068a-aabe-414a-9eeb-55cdcbc9bc45" />

<br>
<br>
<p>1.5. What is the flag value after accessing the endpoint cctv.thm/fpassword.php?id=5?<br>
<code>THM{12319}</code></p>

<h4>Send <code>TCP</code>code> request<br>to flagger.cgi endpoint with a host header containing more than 50 characters.<br>Once done, you can fetch the flag from /fpassword.php?id=5</h4>

```bash
:~# for i in {1..50}; do echo -n A; done; echo
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
```

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
<img width="1057" height="188" alt="image" src="https://github.com/user-attachments/assets/310b18fe-d055-4bfe-a362-9d995cf2fd15" />

<br>
<br>
<p>1.6. What is the password value for the first layer of security for the CCTV web panel?<br>
<code>THM{10001}THM{10125}THM{13231}THM{33120}THM{12319}</code></p>

```bash
...
After receiving all the flags, you can visit the MACHINE IP that will ask you for the password.
The first password will be concatenated values of all five flags you have received above.
```

<p><code>THM{10001}</code> + <code>THM{10125}</code> + <code>THM{13231}</code> + <code>THM{33120}</code> + <code>THM{12319}</code>code></p>

<br>
<br>
<p>1.7. What is the lsb_release -r -s command output from the attached machine?<br>
<code>20.04</code></p>

<br>

<img width="554" height="237" alt="image" src="https://github.com/user-attachments/assets/2b9fc05b-1f11-4ea9-8c8f-8c086931ab77" />

<br>

<img width="747" height="488" alt="image" src="https://github.com/user-attachments/assets/c43318fb-fd02-4feb-866a-bf81c97f233b" />

<br>

<img width="746" height="493" alt="image" src="https://github.com/user-attachments/assets/1730c316-b2d1-426b-99f0-8e9bb980d8ac" />

<br>
<br>
<p>1.8. What is the username for the CCTV web panel?<br>
<code>bypass</code></p>

```bash
...
For the second layer of security, I have enabled a wholly sandboxed login environment with no connection to the database and no possibility of command execution.

The username is the computer's hostname, and the password is the same as the previous password.
```

<br>

<img width="746" height="488" alt="image" src="https://github.com/user-attachments/assets/ee11eca2-0d96-4b2f-ad2e-565f7ce1dc1d" />

<br>
<br>
<p>1.9. What is the flag value after logging into the CCTV web panel?<br>
<code>THM{CCTV_HACKED_1011110}</code></p>

<p><code>bypass</code> : <code>THM{10001}THM{10125}THM{13231}THM{33120}THM{12319}</code></p>

<br>

<img width="553" height="419" alt="image" src="https://github.com/user-attachments/assets/e58f16cf-055c-4167-8821-af8134fe3deb" />

<br>
<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/dbdb0cee-cdba-441d-a7bb-393c289a040a"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/fe05ccf2-deb4-44cc-af41-a48b6c539142"></p>

<br>
<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 23   | 473      |     118ᵗʰ    |      5ᵗʰ     |     298ᵗʰ   |     7ᵗʰ    | 122,450  |    924   |    73     |

</div>

<p align="center">Global All Time:   118ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/6575961d-bd3b-45aa-af01-fce10169270c"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/5dc751e5-e901-4619-9f37-0b737ca5f793"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/b2ee4d80-408f-4a3e-b0be-bb06eb2a4d0e"><br>
                  Global monthly:    298ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/f5f4a89a-3ea7-41f6-973a-f511f9a54be9"><br>
                  Brazil monthly:      7ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/cded0009-8584-4306-9a38-dc369712d76f"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>

<br>
<br>
<h1 align="center">Penetration Tester  .  Red Teaming<br><img width="1200px" src="https://github.com/user-attachments/assets/86278db7-7cb4-4c1c-98bc-9658b04da827"></h1>
<p align="center">✅ Done &nbsp;&nbsp;&nbsp;&nbsp; ・ &nbsp;&nbsp;&nbsp;&nbsp;  ⬛  To-Do  &nbsp;&nbsp;&nbsp;&nbsp; ・ &nbsp;&nbsp;&nbsp;&nbsp;  🌌  In Progress  &nbsp;&nbsp;&nbsp;&nbsp;<br><br>Last update: 2025, August 23<br></p>

<div align="center"><h6>

|Path                       |Skill                   |Type           |Name                                      |Level |
|:--------------------------|:-----------------------|:--------------|:-----------------------------------------|:-----|
|<code>Entry</code> Penetration Tester|Red Teaming   |Walkthrough    |✅ Shells Overview                           |      |
|<code>Entry</code> Penetration Tester|Red Teaming   |Walkthrough    |✅ Nmap: The Basics                          ||
|<code>Entry</code> Penetration Tester|Red Teaming   |Walkthrough    |✅ Metasploit: Meterpreter                   ||
|<code>Entry</code> Penetration Tester|Red Teaming   |Walkthrough    |✅ Metasploit: Introduction                  ||
|<code>Entry</code> Penetration Tester|Red Teaming   |Walkthrough    |✅ Metasploit: Exploitation                  ||
|<code>Entry</code> Penetration Tester|Red Teaming   |Walkthrough    |✅ REmux The Tmux                            ||
|<br><br>                           |                        |               |                                              ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ Passive Reconnaissance                    ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ Intro to Malware Analysis                 ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ Nmap Basic Port Scans                     ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ Nmap Advanced Port Scans                  ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ Nmap Live Host Discovery                  ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ Security Operations                       ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ OWASP Top 1-2021                          ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ OWASP Broken Access Control               ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ MISP                                      ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ OpenCTI                                   ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ Wireshark: Traffic Analysis               ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ Investigating with ELK 101                ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ Brim                                      ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ Erlang/OTP SSH: CVE-2025-32433            ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ ParrotPost: Phishing Analysis             ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ Outlook NTLM Leak                         ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ Hosted Hypervisors                        ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ Forensic Imaging                          ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ Linux File System Analysis                ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ Redline                                   ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ Content Discovery                         ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ Intro to Pwntools                         ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ SQLMAP                                    ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ Core Windows Processes                    ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ Sysmon                                    ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ What the Shell?                           ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ MITRE                                     ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ MAL: REMux - The Redux                    ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ MAL: Strings                              ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ Rustscan                                  ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ Network Services                          ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ Network Services 2                        ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ Upload Vulnerabilities                    ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ YARA                                      ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ Buffer Overflows                          ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ Critical                                  ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ Eviction                                  ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ Probe                                     ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ Trooper                                   ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ Boogeyman 1                               ||
|<code>Junior</code> Penetration Tester  |Red Teaming|Walkthrough    |✅ Empire                                    ||
|<code>Junior</code> Penetration Tester  |Red Teaming|CTF, Challenge |✅ Juicy Details                             |Easy|
|<code>Junior</code> Penetration Tester  |Red Teaming|CTF, Challenge |✅ Cat Picturess                             |Easy|
|<code>Junior</code> Penetration Tester  |Red Teaming|CTF, Challenge |✅ GLITCH                                    |Easy|
|<code>Junior</code> Penetration Tester  |Red Teaming|CTF, Challenge |✅ Magician                                  |Easy|
|<code>Junior</code> Penetration Tester  |Red Teaming|CTF, Challenge |✅ Res                                       |Easy|
|<code>Junior</code> Penetration Tester  |Red Teaming|CTF, Challenge |✅ Chocolate Factory                         |Easy|
|<code>Junior</code> Penetration Tester  |Red Teaming|CTF, Challenge |✅ GamingServer                              |Easy|
|<code>Junior</code> Penetration Tester  |Red Teaming|CTF, Challenge |✅ Easy Peasy                                |Easy|
|<code>Junior</code> Penetration Tester  |Red Teaming|CTF, Challenge |✅ Madness                                   |Easy|
|<code>Junior</code> Penetration Tester  |Red Teaming|CTF, Challenge |✅ Reversing ELF                             |Easy|
|<code>Junior</code> Penetration Tester  |Red Teaming|CTF, Challenge |✅ Ninja Skills                              |Easy|
|<br><br>                        |                        |               |                                              ||
|<code>Mid</code> Penetration Tester     |Red Teaming|Walkthrough    |✅ Supplemental Memory                       |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|Walkthrough    |✅ APT28 in the Snare                        |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|Walkthrough    |✅ APT28 Inception Theory                    |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|Walkthrough    |✅ Logless Hunt                              |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|Walkthrough    |✅ Threat Hunting With YARA                  |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|Walkthrough    |✅ Windows Incident Surface                  |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|Walkthrough    |✅ Baselines and Anomalies                   |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|Walkthrough    |✅ Eradication and Remediation               |Easy|
|<code>Mid</code> Penetration Tester     |Red Teaming|Walkthrough    |✅ Atomic Bird Goes Purple #1                |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|Walkthrough    |✅ Atomic Bird Goes Purple #2                |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|Walkthrough    |✅ CVE-2023-38408                            |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|Walkthrough    |✅ Threat Intel & Containment                |Easy|
|<code>Mid</code> Penetration Tester     |Red Teaming|Walkthrough    |✅ Intro to Threat Emulation                 |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|Walkthrough    |✅ Threat Hunting: Introduction              |Easy|
|<code>Mid</code> Penetration Tester     |Red Teaming|Walkthrough    |✅ Threat Hunting: Endgame                   |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|Walkthrough    |✅ Threat Hunting: Pivoting                  |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|Walkthrough    |✅ LocalPotato                               |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|Walkthrough    |✅ Crylo                                     |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|Walkthrough    |✅ Atomic Red Team                           |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|Walkthrough    |✅ Tactical Detection                        |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|Walkthrough    |✅ Aurora EDR                                |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|Walkthrough    |✅ Tardigrade                                |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|Walkthrough    |✅ Signature Evasion                         |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|Walkthrough    |✅ Sandbox Evasion                           |Hard|
|<code>Mid</code> Penetration Tester     |Red Teaming|Walkthrough    |✅ CALDERA                                   |Hard|
|<code>Mid</code> Penetration Tester     |Red Teaming|Walkthrough    |✅ Living Off the Land                       |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|Walkthrough    |✅ Runtime Detection Evasion                 |Hard|
|<code>Mid</code> Penetration Tester     |Red Teaming|Walkthrough    |✅ Red Team Recon                            |Easy|
|<code>Mid</code> Penetration Tester     |Red Teaming|Walkthrough    |✅ Weaponization                             |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|CTF, Challenge |✅ Lockdown                                  |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|CTF, Challenge |⬛ Fortress                                  |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|CTF, Challenge |✅ Git and Crumpets                          |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|CTF, Challenge |⬛ Binary Heaven                             |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|CTF, Challenge |⬛ VulnNet: Active                           |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|CTF, Challenge |✅ VulnNet: dotjar                           |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|CTF, Challenge |⬛ SafeZone                                  |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|CTF, Challenge |✅ Tokyo Goul                                |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|CTF, Challenge |✅ Lunizz CTF                                |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|CTF, Challenge |✅ Madeye´s Castle                           |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|CTF, Challenge |✅ The Server From Hell                      |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|CTF, Challenge |✅ NerdHerd                                  |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|CTF, Challenge |✅ Looking Glass                             |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|CTF, Challenge |🌌 WWBuddy                                   |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|CTF, Challenge |✅ Ghizer                                    |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|CTF, Challenge |✅ Mnemonic                                  |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|CTF, Challenge |✅ Mindgames                                 |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|CTF, Challenge |✅ Peak Hill                                 |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|CTF, Challenge |✅ Nax                                       |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|CTF, Challenge |✅ dogcat                                    |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|CTF, Challenge |✅ Binex                                     |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|CTF, Challenge |✅ Break it                                  |Medium|
|<code>Mid</code> Penetration Tester     |Red Teaming|CTF, Challenge |✅ GoldenEye                                 |Medium|

</h6></div><br>
