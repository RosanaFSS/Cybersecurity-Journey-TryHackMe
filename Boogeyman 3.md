<h1 align="center"><a href="https://tryhackme.com/room/boogeyman3">Boogeyman 3</a></h1>
<h3 align="center">SOC Level 1 Learning Path &nbsp;|&nbsp; Capstone Challenge</h3>
<p align="center"><em>This documents how I solved the Boogeyman 3 challenge.<br>If you find it helpful, consider coming back for research.</em><br><br><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=social" alt="Follow Rosana on GitHub"></a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2024, July 26 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-blue?style=flat-square&logo=linkedin" alt="Connect on LinkedIn"></a></p>

<div align="center">
  
|             Previous Boogeyman´s Investigations          |
|:--------------------------------------------------------:|
|<a href="https://github.com/RosanaFSS/Cybersecurity-Journey-TryHackMe/blob/CTFs-&-Infos/Medium%20%F0%9F%94%97%20Boogeyman%201.md">Boogeyman 1</a>  &nbsp;&nbsp; & &nbsp;&nbsp; Boogeyman 2 Walkthroughs|

<div></p>


<h2 align="left">Task 1 - Introduction</a></h2>
<p align="left"><em>Due to the previous attacks of Boogeyman, Quick Logistics LLC hired a managed security service provider to handle its Security Operations Center. Little did they know, the Boogeyman was still lurking and waiting for the right moment to return. </em></p>

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

<br>
<h2>Task 2 • The Chaos Inside.</h2>
<h3>Lurking in the Dark</h3>

<p>Without tripping any security defences of Quick Logistics LLC, the Boogeyman was able to compromise one of the employees and stayed in the dark, waiting for the right moment to continue the attack. Using this initial email access, the threat actors attempted to expand the impact by targeting the CEO, Evan Hutchinson. </p>

<img width="1438" height="597" alt="image" src="https://github.com/user-attachments/assets/421d7220-cef2-4ede-95ad-8dcbcc3f6280" />


<p>The email appeared questionable, but Evan still opened the attachment despite the scepticism. After opening the attached document and seeing that nothing happened, Evan reported the phishing email to the security team.</p>

<h3>Initial Investigation</h3>h3>

<p>Upon receiving the phishing email report, the security team investigated the workstation of the CEO. During this activity, the team discovered the email attachment in the downloads folder of the victim.</p>

<img width="2250" height="434" alt="image" src="https://github.com/user-attachments/assets/8acbbe1d-de12-4859-a9e7-1ad7b10202b0" />


<p>In addition, the security team also observed a file inside the ISO payload, as shown in the image below.</p>

<img width="2246" height="846" alt="image" src="https://github.com/user-attachments/assets/ceff7cb5-50b1-4826-855a-de969603d90c" />


<p>Lastly, it was presumed by the security team that the incident occurred between August 29 and August 30, 2023.<br>

Given the initial findings, you are tasked to analyse and assess the impact of the compromise.</p>

<p><em>Answer the questions below</em></p>

<br>
<p>2.1. <em>What is the PID of the process that executed the initial stage 1 payload?</em><br>
<code>6392</code></p>

<br>
<p>2.2. <em>The stage 1 payload attempted to implant a file to another location. What is the full command-line value of this execution?</em><br>
<code>"C:\Windows\System32\xcopy.exe" /s /i /e /h D:\review.dat C:\Users\EVAN~1.HUT\AppData\Local\Temp\review.dat</code></p>

<br>
<p>2.3. <em>The implanted file was eventually used and executed by the stage 1 payload. What is the full command-line value of this execution?</em><br>
<code>"C:\Windows\System32\rundll32.exe" D:\review.dat,DllRegisterServer</code></p>

<br>
<p>2.4. <em>The stage 1 payload established a persistence mechanism. What is the name of the scheduled task created by the malicious script?</em><br>
<code>Review</code></p>

<br>
<p>2.5. <em>The execution of the implanted file inside the machine has initiated a potential C2 connection. What is the IP and port used by this connection? (format: IP:port)</em><br>
<code>165.232.170.151:80</code></p>

<br>
<p>2.6. <em>The attacker has discovered that the current access is a local administrator. What is the name of the process used by the attacker to execute a UAC bypass?</em><br>
<code>fodhelper.exe</code></p>


<br>
<p>2.7. <em>Having a high privilege machine access, the attacker attempted to dump the credentials inside the machine. What is the GitHub link used by the attacker to download a tool for credential dumping?</em><br>
<code>https://github.com/gentilkiwi/mimikatz/releases/download/2.2.0-20220919/mimikatz_trunk.zip</code></p>

![August-12-2024 - TryHackMe - SOC Level 1 Learning Path - Capstone Challenges - Boogeyman3, Image 9](https://github.com/user-attachments/assets/7e1dd69f-91a7-4187-a07f-bed8cdfef771)


<br>
<p>2.8. <em>After successfully dumping the credentials inside the machine, the attacker used the credentials to gain access to another machine. What is the username and hash of the new credential pair? (format: username:hash)</em><br>
<code>itadmin:F84769D250EB95EB2D7D8B4A1C5613F2</code></p>


<br>
<p>2.9. <em>Using the new credentials, the attacker attempted to enumerate accessible file shares. What is the name of the file accessed by the attacker from a remote share?</em><br>
<code>IT_Automation.ps1</code></p>


<br>
<p>2.10. <em>After getting the contents of the remote file, the attacker used the new credentials to move laterally. What is the new set of credentials discovered by the attacker? (format: username:password)</em><br>
<code>QUICKLOGISTICS\allan.smith:Tr!ckyP@ssw0rd987</code></p>

<br>
<p>2.11. <em>What is the hostname of the attacker's target machine for its lateral movement attempt?</em><br>
<code>WKSTN-1327</code></p>

<br>
<p>2.12. <em>Using the malicious command executed by the attacker from the first machine to move laterally, what is the parent process name of the malicious command executed on the second compromised machine?</em><br>
<code>wsmprovhost.exe</code></p>


<br>
<p>2.13. <em>The attacker then dumped the hashes in this second machine. What is the username and hash of the newly dumped credentials? (format: username:hash)</em><br>
<code>administrator:00f80f2538dcb54e7adc715c0e7091ec</code></p>

<br>
<p>2.14. <em>After gaining access to the domain controller, the attacker attempted to dump the hashes via a DCSync attack. Aside from the administrator account, what account did the attacker dump?</em><br>
<code>backupda</code></p>



<p>2.15. <em>After dumping the hashes, the attacker attempted to download another remote file to execute ransomware. What is the link used by the attacker to download the ransomware binary?</em><br>
<code>http://ff.sillytechninja.io/ransomboogey.exe</code></p>



![August-12-2024 - TryHackMe - SOC Level 1 Learning Path - Capstone Challenges - Boogeyman3, Image 1000 Last answer](https://github.com/user-attachments/assets/2d5d28bd-93e0-4953-9d7f-2bfdabb4b22b)
