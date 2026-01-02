<h1 align="center"><a href="https://tryhackme.com/room/boogeyman3">Boogeyman 3</a></h1>
<h3 align="center">SOC Level 1 Learning Path &nbsp;|&nbsp; Capstone Challenge</h3>
<p align="center">This documents how I solved the Boogeyman 3 challenge. If you<br> find it helpful, consider coming back for research. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br><br><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=social" alt="Follow Rosana on GitHub"></a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2024, August 12 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-blue?style=flat-square&logo=linkedin" alt="Connect on LinkedIn"></a></p>


<div align="center"><p>
  
|   Previous Boogeyman´s Write-Ups  |
|:----------------------------------------------------------------------------:|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://github.com/RosanaFSS/Cybersecurity-Journey-TryHackMe/blob/CTFs-&-Infos/Medium%20%F0%9F%94%97%20Boogeyman%201.md">Boogeyman 1</a>  &nbsp;&nbsp; & &nbsp;&nbsp; Boogeyman 2 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|

</p></div>


<h2>Task 1 - Introduction</h2>
<p><em>Due to the previous attacks of Boogeyman, Quick Logistics LLC hired a managed security service provider to handle its Security Operations Center. Little did they know, the Boogeyman was still lurking and waiting for the right moment to return. </em></p>

<p>In this room, you will be tasked to analyse the new tactics, techniques, and procedures (TTPs) of the threat group named Boogeyman. </p>

<h6 align="center"><img width="400px" src="https://github.com/user-attachments/assets/e702a51d-c1d5-4095-b332-9d273c282ba7"><br>This image and all the theoretical content of<br>the present article is TryHackMe´s property.</h6>

<h3>Prerequisites</h3>
<p>This room may require the combined knowledge gained from the <a href="https://tryhackme.com/path-action/soclevel1/join">SOC L1 Path</a>. We recommend going through the following rooms before attempting this challenge.<br>

- <a href="https://tryhackme.com/room/sysmon">Sysmon</a><br>
- <a href="https://tryhackme.com/room/itsybitsy">ItsyBitsy</a><br>
- <a href="https://tryhackme.com/room/investigatingwithelk101">Investigating with ELK</a><br>
- <a href="https://tryhackme.com/room/boogeyman1">Boogeyman 1</a><br>
- <a href="https://tryhackme.com/room/boogeyman2">Boogeyman 2</a></p>


<h3>Investigation Platform</h3>
<p>Before we proceed, deploy the attached machine by clicking the Start Machine button in the upper-right-hand corner of the task. The provided virtual machine runs an Elastic Stack (ELK), which contains the logs that will be used throughout the room.<br>

Once the machine is up, access the Kibana console (via the AttackBox or VPN) using the credentials below.</p>

<h6 align="center"><img width="300px" src="https://github.com/user-attachments/assets/367dc038-7a9a-4925-8315-35a00f763b51"><br>This image and all the theoretical content of<br>the present article is TryHackMe´s property.</h6>

<p>Note: The Kibana instance may take 3-5 minutes to initialise.</p>

<p><em>Answer the question below</em></p>

<p>1.1. Let's end this Boogeyman incident!<br>
<code>No answer needed</code></p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/6fa36e22-7fa4-4acb-bff5-f72e84521cf9"><br></p>

<h2>Task 2 - The Chaos Inside</h2>
<h3>Lurking in the Dark</h3>

<p>Without tripping any security defences of Quick Logistics LLC, the Boogeyman was able to compromise one of the employees and stayed in the dark, waiting for the right moment to continue the attack. Using this initial email access, the threat actors attempted to expand the impact by targeting the CEO, Evan Hutchinson. </p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/421d7220-cef2-4ede-95ad-8dcbcc3f6280"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>The email appeared questionable, but Evan still opened the attachment despite the scepticism. After opening the attached document and seeing that nothing happened, Evan reported the phishing email to the security team.</p>

<h3>Initial Investigation</h3>

<p>Upon receiving the phishing email report, the security team investigated the workstation of the CEO. During this activity, the team discovered the email attachment in the downloads folder of the victim.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/8acbbe1d-de12-4859-a9e7-1ad7b10202b0"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>In addition, the security team also observed a file inside the ISO payload, as shown in the image below.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/ceff7cb5-50b1-4826-855a-de969603d90c"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Lastly, it was presumed by the security team that the incident occurred between August 29 and August 30, 2023.<br>

Given the initial findings, you are tasked to analyse and assess the impact of the compromise.</p>

<p><em>Answer the questions below</em></p>

<p>2.1. <em>What is the PID of the process that executed the initial stage 1 payload?</em><br>
<code>6392</code></p>
<br>
<p>

- click the <strong>Time Filter</strong> (the date range display in the top-right corner)<br>
- click over the <strong>Start date</strong> field<br>
- select the <strong>Absolute</strong> tab<br>
- enter <code>Aug 29, 2023 00:00:00.001</code> into <strong>Start date</strong><br>
- click <strong>Update</strong></p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/25ee54a8-6632-473f-ad50-7c986f65622b"><br>Rosana´s hands-on</p>
<p>

- click the <strong>Time Filter</strong> (the date range display in the top-right corner)<br>
- click over the <strong>End date</strong> field<br>
- select the <strong>Absolute</strong> tab<br>
- enter <code>Aug 30, 2024 23:59:59.999</code>< into <strong>End date</strong><br>
- click <strong>Update</strong></p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/3c664d2f-058f-4432-8d57-89133414db1c"><br>Rosana´s hands-on</p>

<p>
  
- note <strong>28,302</strong> hits = events</p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/d9f76f0c-859f-4909-bbdc-d4dd3f6dc87b"><br><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/5bdf1c4a-204f-456d-aad3-d90f3f1f421d"><br><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/fd4f661d-f48b-45e4-8fa7-3fc961abfa54"><br><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/fd4f661d-f48b-45e4-8fa7-3fc961abfa54"><br>Rosana´s hands-on<br>Rosana´s hands-on</p>



<br>
<p>2.2. <em>The stage 1 payload attempted to implant a file to another location. What is the full command-line value of this execution?</em><br>
<code>"C:\Windows\System32\xcopy.exe" /s /i /e /h D:\review.dat C:\Users\EVAN~1.HUT\AppData\Local\Temp\review.dat</code></p>

<p>

- discovered the answer in question 2.1. revisiting the process created on <strong>Aug 29, 2023 23:51:16.738</strong> with <code>process.name</code> : <code>xcopy.exe</code> and  <code>PID</code> : <code>3832</code></p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/2c503030-74ef-4733-b108-42aa0ea4e912"><br>Rosana´s hands-on</p>

<br>
<p>2.3. <em>The implanted file was eventually used and executed by the stage 1 payload. What is the full command-line value of this execution?</em><br>
<code>"C:\Windows\System32\rundll32.exe" D:\review.dat,DllRegisterServer</code></p>

<p>

- discovered the answer in question 2.1. revisiting the process created on <strong>Aug 29, 2023 23:51:16.771</strong> with <code>process.name</code> : <code>rundll32.exe</code> and  <code>PID</code> : <code>3680</code></p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/551b2de9-8dab-44a3-a3e2-0813d917454b"><br>Rosana´s hands-on</p>

<br>
<p>2.4. <em>The stage 1 payload established a persistence mechanism. What is the name of the scheduled task created by the malicious script?</em><br>
<code>Review</code></p>


<p>

- discovered the answer in question 2.1. revisiting the process created on <strong>Aug 29, 2023 23:51:16.809</strong> with <code>process.name</code> : <code>powershell.exee</code> and  <code>PID</code> : <code>6204</code></p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/8d5562f3-a518-4e07-a70d-0b777c7343d6"><br>Rosana´s hands-on</p>




<br>
<br>
<p>2.5. <em>The execution of the implanted file inside the machine has initiated a potential C2 connection. What is the IP and port used by this connection? (format: IP:port)</em><br>
<code>165.232.170.151:80</code></p>

<img width="1810" height="699" alt="image" src="https://github.com/user-attachments/assets/967d0bc4-f3ba-407f-a912-64db8679df49" />

<img width="1810" height="706" alt="image" src="https://github.com/user-attachments/assets/a56bc6c9-9bf5-44d7-8779-329910c7a492" />

<img width="1809" height="664" alt="image" src="https://github.com/user-attachments/assets/113c4af1-77bf-4a85-b1a4-d434e568d58c" />

<img width="1810" height="702" alt="image" src="https://github.com/user-attachments/assets/40414212-651d-4d67-9606-2262ecfda4e2" />

<img width="1798" height="705" alt="image" src="https://github.com/user-attachments/assets/71010626-4c2d-4d1f-8d23-71d90ac9cde6" />

<img width="1810" height="699" alt="image" src="https://github.com/user-attachments/assets/f3122a61-7904-48d9-abc0-4d25c4d35f92" />

<br>
<br>

<img width="1905" height="380" alt="image" src="https://github.com/user-attachments/assets/0257977b-b665-4bf9-b441-7716b59b025d" />

<img width="1914" height="265" alt="image" src="https://github.com/user-attachments/assets/e2d806b4-3a17-49f9-9bf1-3742525682dc" />

<br>
<br>
<p>2.6. <em>The attacker has discovered that the current access is a local administrator. What is the name of the process used by the attacker to execute a UAC bypass?</em><br>
<code>fodhelper.exe</code></p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/3256e255-d41a-467b-af35-9bd308f1c945"><br>Rosana´s hands-on</p>

<br>
<p>2.7. <em>Having a high privilege machine access, the attacker attempted to dump the credentials inside the machine. What is the GitHub link used by the attacker to download a tool for credential dumping?</em><br>
<code>https://github.com/gentilkiwi/mimikatz/releases/download/2.2.0-20220919/mimikatz_trunk.zip</code></p>
<p>

- update <strong>Start date</strong> field<br>
- filter <code>user.name</code> : <code>evan.hutchinson</code><br>
- filter <code>process.command_line</code> : <code>exists</code><br></p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/aba39530-7a83-4fa0-afba-0bc432836bd6"><br>Rosana´s hands-on</p>

<br>
<p>2.8. <em>After successfully dumping the credentials inside the machine, the attacker used the credentials to gain access to another machine. What is the username and hash of the new credential pair? (format: username:hash)</em><br>
<code>itadmin:F84769D250EB95EB2D7D8B4A1C5613F2</code></p>
<p>

- filter <code>user.name</code> : <code>allan.smith</code><br>
- filter <code>process.command_line</code> : <code>exists</code></p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/2876b3b6-454b-421f-90a3-349ba0e7832c"><br>Rosana´s hands-on</p>

<br>

<br>
<p>2.9. <em>Using the new credentials, the attacker attempted to enumerate accessible file shares. What is the name of the file accessed by the attacker from a remote share?</em><br>
<code>IT_Automation.ps1</code></p>
<p>

- filter <code>process.command_line</code> : <code>exists</code><br>
- filter <code>user.name</code> : <code>evan.hutchinson</code><br></p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/1164e5a2-1ccf-4cfb-b227-6c1763529fe2"><br>Rosana´s hands-on</p>

<br>
<p>2.10. <em>After getting the contents of the remote file, the attacker used the new credentials to move laterally. What is the new set of credentials discovered by the attacker? (format: username:password)</em><br>
<code>QUICKLOGISTICS\allan.smith:Tr!ckyP@ssw0rd987</code></p>
<p>


- update <strong>Start date</strong> field<br>
- filter <code>user.name</code> : <code>allan.smith</code><br>
- filter <code>process.command_line</code> : <code>exists</code><br></p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/57c18bb1-0302-4135-9cbd-ab2de9925769"><br>Rosana´s hands-on</p>

<br>
<p>2.11. <em>What is the hostname of the attacker's target machine for its lateral movement attempt?</em><br>
<code>WKSTN-1327</code></p>
<p>

- update <strong>Start date</strong> field<br>
- filter <code>process.name</code> : <code>exists</code><br>
- search <code>review.dat</code></p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/e1967417-e7d7-4a8e-b8e4-584181b52d6d"><br>Rosana´s hands-on</p>

<br>
<p>2.12. <em>Using the malicious command executed by the attacker from the first machine to move laterally, what is the parent process name of the malicious command executed on the second compromised machine?</em><br>
<code>wsmprovhost.exe</code></p>
<p>

- update <strong>Start date</strong> field<br>
- filter <code>event.code</code> : <code>1</code><br>
- filter <code>host.name</code> : <code>DC01.quicklogistics.org</code></p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/008017eb-9c08-4ef1-9f95-5642100af59c"><br>Rosana´s hands-on</p>

<br>
<p>2.13. <em>The attacker then dumped the hashes in this second machine. What is the username and hash of the newly dumped credentials? (format: username:hash)</em><br>
<code>administrator:00f80f2538dcb54e7adc715c0e7091ec</code></p>
<p>

- filter <code>user.name</code> : <code>allan.smith</code><br>
- filter <code>process.command_line</code> : <code>exists</code></p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/b1dbcfd8-80ee-4b97-8f68-155a71575796"><br>Rosana´s hands-on</p>

<br>
<p>2.14. <em>After gaining access to the domain controller, the attacker attempted to dump the hashes via a DCSync attack. Aside from the administrator account, what account did the attacker dump?</em><br>
<code>backupda</code></p>
<p>

- filter <code>event.code</code> : <code>1</code><br>
- filter <code>host.name</code> : <code>DC01.quicklogistics.org</code><br>
- search <code>DCSync</code></p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/1d0fcd44-f056-4f3a-86e4-b2a576e13450"><br>Rosana´s hands-on</p>

<br>
<p>2.15. <em>After dumping the hashes, the attacker attempted to download another remote file to execute ransomware. What is the link used by the attacker to download the ransomware binary?</em><br>
<code>http://ff.sillytechninja.io/ransomboogey.exe</code></p>
<p>

- filter <code>event.code</code> : <code>1</code><br>
- filter <code>host.name</code> : <code>DC01.quicklogistics.org</code></p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/0e2ff53a-0fa9-4af5-950b-4affaf5b3a69"><br>Rosana´s hands-on</p>

<br>


<h2>Summary</h2>

<p>

- Aug 30, 2023 00.09.57.186 - attacker <strong>evan.hutchinson</strong> tried to dump credentials using <strong>mimikatz</strong> tool from GitHub<br>
- Aug 29, 2023 23:51:16.738 - attacker <strong>evan.hutchinson</strong> implanted <strong>review.dat</strong> executing <strong>xcopy.exe</strong><br>
- Aug 29, 2023 23:51:16.771 - attacker <strong>evan.hutchinson</strong> executed <strong>rundll32.exe</strong> against <strong>review.dat</strong><br>
- Aug 29, 2023 23:51:16.809 - attacker <strong>evan.hutchinson</strong> created the scheduled task <strong>Review</strong> as a persistence mechanism executing <strong>powershell.exe</strong><br>
- Aug 29, 2023 23:54:16.129 - attacker <strong>evan.hutchinson</strong> discovered <strong>local administrator</strong> as the current access<br>
- Aug 29, 2023 23:54:49.043 - attacker <strong>evan.hutchinson</strong> bypassed UAC executing <strong>foodhelper.exe</strong><br>
- Aug 30, 2023 00:11:26.438 - attacker <strong>evan.hutchinson</strong> enumerated credentials on <strong>WKSTN-0051</strong> host<br>
- Aug 30, 2023 00:13:37.090 - attacker <strong>evan.hutchinson</strong> tried to gain access to <strong>WKSTN-1327</strong> using <strong>itadmin</code>´s credentials<br>
- Aug 30, 2023 00:19:52.889 - gained access to another machine, and accessed a remote share<br>
- Aug 30, 2023 00:20:57.172 - attacker <strong>evan.hutchinson</strong> gained access to <strong>allan.smith</strong> moving laterally from host <strong>WKSTN-0051</strong> to <strong>WKSTN-1327</strong><br>
- Aug 30, 2023 00:21:53.284 - as <strong>allan.smith</strong> attacker <strong>evan.hutchinson</strong> executed malicious command on WKSTN-1327<br>
- Aug 30, 2023 00:20:59.159 - as <strong>allan.smith</strong> attacker <strong>evan.hutchinson</strong> executed <strong>wsmprovhost.exe</strong><br>
- Aug 30, 2023 01:29:09.409 - as <strong>allan.smith</strong> attacker <strong>evan.hutchinson</strong> tried to dump credentials using <strong>mimikatz</strong> tool from GitHub<br>
- Aug 30, 2023 01:30:25.545 - attacker <strong>evan.hutchinson</strong> tried to gain access to <strong>WKSTN-1327</strong> using <strong>itadmin</code>´s credentials through <strong>allan.smith</strong> access<br>
- Aug 30, 2023 01:30:51.647 - as <strong>allan.smith</strong> attacker <strong>evan.hutchinson</strong> enumerated credentials on <strong>WKSTN-1327</strong> and discovered <strong>administrator</strong><br>
- Aug 30, 2023 01:31:39.426 - as <strong>allan.smith</strong> attacker <strong>evan.hutchinson</strong> tried to dump <strong>Administrator</strong> credentials<br>
- Aug 30, 2023 01:46:18.577 - as <strong>Administrator</strong> attacker <strong>evan.hutchinson</strong> tried to dump credentials using <strong>mimikatz</strong> tool from GitHub<br>
- Aug 30, 2023 01:47:57.809 - as <strong>Administrator</strong> attacker <strong>evan.hutchinson</strong> dumped hashes via a DCSync attack on <strong>DC01</strong><br>
- Aug 30, 2023 01:53:13.738 - as <strong>Administrator</strong> attacker <strong>evan.hutchinson</strong> downloaded the binary<strongramsomboogey.exe</strong> to <strong>DC-01</strong</p>
