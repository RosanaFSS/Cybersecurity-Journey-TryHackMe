<h1 align="center">SOC Simulator &nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;&nbsp; <a href="https://tryhackme.com/soc-sim/scenarios?scenario=apt28-link-to-trouble-initial-access"> APT28: Initial Access</a></h1>
<p align="center"><img width="590px" src="https://github.com/user-attachments/assets/02f7e84c-766d-4ec6-935f-cfc5e59063e4"><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20JAN%2018-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Overview](#1) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Objectives](#2) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Methodology](#3) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Resources](#4)  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Practice](#5)


<br>
<br>
<br>
<br>
<h2>Overview<a id='1'></a></h2>
<p>Here at <code>TryGovMe</code>, our partners have been consistently targeted by <code>APT28</code> over the past few weeks and we are now preparing for a potential intrusion ourselves. To all SOC analysts on shift - please remain focused and prepared for a possible attack!<br>
Chapter of the APT28: Link to Trouble scenario.</p>

<h2>Objectives<a id='2'></a></h2>
<p>

- Identify and triage security alerts indicating malicious behaviour consistent with <code>APT28</code> activity.<br>
- Analyse <code>initial access techniques</code> used by <code>APT28</code> in enterprise environments.<br>
- Analyse and correlate various log types to identify anomalies and gain insight into adversary activity.</p>


<h2>Methodology<a id='3'></a></h2>
<p>
  
- Step 1<br><strong>Find all the true positives</strong><br>To complete a Scenario, find all the True Positive alerts. Keep triaging alerts until you've closed them all!<br><br>
- Step 2<br><strong>Read the documentation</strong><br>Before diving into the triage, take a moment to review the provided documentation. This will give you essential context and strategies for investigation.<br><br>
- Step 3<br><strong>Investigate the alert queu</strong><br>Your journey starts in the alert queue. Investigate each alert, and prioritise what seems most critical. Understanding the types of alerts can help you manage your time effectively.<br><br>
- Step 4<br><strong>Take ownership of an alert</strong><br>Click on an alert to take ownership. This action starts the timer for MTTR, so act fast! Use this to strategise how you spend time on each alert.<br><br>
- Step 5<br><strong>Deep dive with the SIEM & VM</strong><br>Use the SIEM to search logs and investigate indicators. The VM is there for deeper analysis. Combine these tools to verify what’s real and what’s a false alarm.<br><br>
- Step 6<br><strong>Write your findings as a report</strong><br>For each alert, determine whether it's a true positive or a false positive. Clearly document your findings, analysis, and actions taken. Submit the report when you're confident in your conclusions—accurate and well-written reports will earn you more points!<br><br>
- Step 7<br><strong>Analyse your performance</strong><br>After completing the scenario, dive into your wrap-up report to see how you performed. You’ll receive detailed feedback on your MTTR, points scored, the number of closed alerts, and personalised AI insights to enhance your future reporting.</p>


<br>
<h2>Resources<a id='4'></a></h2>
<p></p>

- <a href="https://attack.mitre.org/groups/G0007/"> MITRE ATT&CK > Groups > APT28</a><br>
- <a href="https://medium.com/@RosanaFS/apt28-in-the-snare-tryhackme-walkthrough-blue-team-advanced-persistent-threats-apts-ca5b1eafcb29"> APT28 in the Snare : TryHackMe Walkthrough</a><br>
- <a href="https://medium.com/@RosanaFS/apt28-inception-theory-681b3db08072"> APT28 Inception Theory : TryHackMe Walkthrough</a></p>

<br>
<h2>Practice<a id='5'></a></h2>


```bash
index=* query
| table timestamp, ComputerName, QueryName, QueryResults, User, Image, src_ip, url, ProcessId, ParentProcessId, ParentUser
|  sort by +_timestamp
```



➡
<p>
  
- Case ID: 2001<br>
- Suspicious Archive File Download Detected<br>
- Severity: Medium<br>
- Type: Download<br>
- Incident classification: <code>True Positive</code> - 10/10 points<br>
- Require Escalation?   <code>Yes</code> - 10/10 points</p>

```bash
Time of activity:
2024-12-07 15:22:30.966

List of Affected Entities: 
- User: DEV-QA-SERVER\Tom Barry
- ComputerName: Dev-QA-Server
- ProcessId: 4980

Reason for Classifying as True Positive:  
- Confirmed malicious file download.
- User DEV-QA-SERVER\Tom Barry used Google Chrome (chrome.exe) on  01/18/2026 17:12:40.399 to download a ".rar" file in the path C:\Users\Tom Barry\Downloads\Service_Configuration_Guide.rar" that might be a potentiral risk. There is the presence of ":Zone.Identifier" confirms  that the fille originated from the internat.  The use of a compresse archive file (.rar) for a "Configuration Guide" is susupicious as legitimate documention is typically distributed as .pdf or .docx.

Reason for Escalating the Alert: 
-  User DEV-QA-SERVER\Tom Barry donwloaded a .rar suspicious  Configuration Guide which might contain malicious content.

Recommended Remediation Actions:  
- Isolate, Kill, Delete the malicious file.

List of Attack Indicators: 
- RuleName: files_downloads
- Image: C:\Program - Files\Google\Chrome\Application\chrome.exe
- TargetFilename: C:\Users\Tom Barry\Downloads\Service_Configuration_Guide.rar:Zone.Identifier
```




<img width="1902" height="871" alt="image" src="https://github.com/user-attachments/assets/6a8cddb1-ad4b-44e3-bca7-65c62d48376d" />


```bash

```


```bash

```

```bash

```


<img width="1910" height="896" alt="image" src="https://github.com/user-attachments/assets/019b0fc2-6cc9-4fa4-ac22-59a553bd5db4" />


This alert detects DNS queries to rare or suspicious domains, which can suggest attempts to contact attacker-controlled infrastructure or bypass traditional network monitoring.
_____________________________________________________________________________
Case ID 2000 | Unexpexted DNS Query Detected
_____________________________________________________________________________
Time of activity:             01/18/2026 17:10:08.399
_____________________________________________________________________________
List of Affected Entities:    1
➡ username: HOST02\Ella Thompson
➡ computer nam:  HOST02
_____________________________________________________________________________
Reason for Classifying as True Positive:
➡ The malicious actor [         ]  used the Technique T1078 [ Valid Accounts ] for levering an spearphishing attack with embedded malicious link in the emails. 
➡ [Who:    ] clicked in the link of the malicious email with Subject [What:  ] at [  When:  ] and had its account compromised [ Cade ID:  What:  ].
➡ The malicious actor [ Who:   ] sent the email from [ Source IP:  ] : [ Source Port: ].
_____________________________________________________________________________
Reason for Escalating the Alert:
_____________________________________________________________________________
Recommended Remediation Actions:
_____________________________________________________________________________
List of Attack Indicators:
C:\Program Files\Sublime Text\sublime_text.exe

DATA
➡ datasource:                  Microsoft-Windows-Sysmon/Operational
➡ image:                       C:\Program Files\Sublime Text\sublime_text.exe

PROCESS
➡ process name:                nslookup.exe
➡ process PID:                 4796
➡ process command line:        1
➡ process working directory:   1

PARENT PROCESS
➡ process parent name:         powershell.exe
➡ process parent PID (PPID):   3728
➡ part process command line:   1



_____________________________________________________________________________
List of Attack Indicators:




