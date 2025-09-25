<h1 align="center">Supplemental memory<br><img width="1200px" src="https://github.com/user-attachments/assets/3c611801-4d91-40e8-b35b-a2395cf04ada"></h1>

<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/a6a395b7-d5e5-4749-81f1-45cc4619f512"><br>
June 16, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure,<br>
part of my <code>406</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br>
Investigate lateral movement, credential theft, and additional adversary actions in a memory dump.<a href="https://tryhackme.com/room/supplementalmemory"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/387d68a7-8bc3-476c-8c23-fc20467bc0ec"></p>
<br>
  
<h2> Task 1 . Introduction</h2>

<p>As a DFIR team member in this room, you are tasked with conducting a memory analysis of a Windows workstation image suspected to have been compromised by a threat actor.<br><br>

This room is designed for DFIR team members, Threat Hunters, and SOC L2/L3 analysts who want to improve and reinforce their skills in memory analysis during a potential incident in order to understand better the value that memory dump investigation can provide in such scenarios.</p>

<h3>Learning Objectives</h3>
<p> In this room, we will examine the footprints of the adversary's actions in the compromised Linux server. Some of the key topics that we will cover are:<br>

- Uncover the TryHatMe breach with just a memory dump.<br>
- Identify suspicious processes and network connections.<br>
- Explore traces of execution and discovery actions.<br>
- Detect signs of potential lateral movement and credential dumping.</p>

<h3>Prerequisites</h3>

<p>It is suggested to clear the following rooms first before proceeding:<br>

- <a href="https://tryhackme.com/room/windowsmemoryandprocs/">Windows Memory & Processes</a><br>
- <a href="https://tryhackme.com/room/windowsmemoryanduseractivity">Windows Memory & User Activity</a><br>
- <a href="https://tryhackme.com/room/windowsmemoryandnetwork">Windows Memory & Network</a></p>

<h3 align="left"> Answer the question below</h3>

> 1.1. <em>Let's start!</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

<h2> Task 2 . TryHatMe Attack Scneario</h2>

![image](https://github.com/user-attachments/assets/8ea2508d-11fc-4fd1-9c98-b8eadd51b13c)

<p>We’ve set up a hands-on scenario for you, where you’ll step into the role of a DFIR team member.</p>

<h3>Scenario</h3>
<p>During the initial stages of the investigation, it was confirmed that the TryHatMe CEO's host WIN-001 was compromised. The attacker successfully obtained credentials belonging to Cain Omoore, a Domain IT Administrators group member who remotely helped the CEO with the endpoint configuration and cached his credentials on the host.<br><br>

Given the privileges associated with Cain's account, the internal security team suspects that the attacker laterally moved to other systems within the environment or even to Cain's host - WIN-015.<br><br>

Since Cain stores access keys to the TryHatMe factory control system on his WIN-015, your first priority is to investigate his host for any lateral movement or data exfiltration traces. For this, you have been provided with a memory dump of WIN-015. Good luck!</p>

<h3>Company Information TryHatMe</h3>
<h5>Network Map</h5>
<p>Note: The network map displays only a limited portion of the network — not all assets in the organisation are represented.</p>

![image](https://github.com/user-attachments/assets/cd4e72d1-4588-4d1e-b59a-25e2040e78eb)


The machine will take approximately 2 minutes to boot up and will start in split view. In case the VM is not visible, you can click the Show Split View button at the top of the page. If you prefer using SSH, you can use the following credentials:


<h3>Machine Access</h3>


![image](https://github.com/user-attachments/assets/6ce016c1-dab0-4b82-aae0-59f67c1540ff)

<p>The memory dump details are as follows:<br>

- File Name: <code>WIN-015-20250522-111717.dmp</code><br>
- File MD5 Hash: <code>15fd7b30b20b53e7374aa8894413c686</code><br>
- File Location: <code>/home/analyst/memory/WIN-015</code><br><br>

To execute Volatility 3 for analysis, use the <code>vol</code> command, example: <code>vol -f WIN-015-20250522-111717.dmp windows.psscan</code>.<br><br>

Note: The first time you run a Volatility plugin, it may take a while to complete due to initial setup and caching. This is expected behaviour. Subsequent runs will be much faster and more responsive. Thank you for your patience!<br><br>

Additionally, you can find some pre-cooked results from Volatility plugins in the following directory for your convenience:<br>
<code>/home/analyst/memory/WIN-015/precooked</code><br><br>

Good luck, and stay sharp - every minute counts!</p>

<h3 align="left"> Answer the question below</h3>

> 2.1. <em>Are you ready to begin?</em><br><a id='2.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

<h2> Task 3 . Lateral Movement aned Discovery</h2>

<p>Let’s try to either prove or disprove the team’s suspicions regarding traces of the threat actor’s movement to the WIN-015 host.<br><br>

Below are a few tips on how different lateral movement techniques can be identified using memory analysis.</p>

<h3>Detecting Lateral Movement via PsExec Execution</h3>

<p>Volatility Terminal</p>

```bash
analyst@tryhackme$ vol -f ransomhub.dmp windows.pstree
PID     PPID    ImageFileName
4       0       System
* 272   4       smss.exe
* 384     376     csrss.exe
* 460     376       wininit.exe
* 600     460         services.exe
** 3772   600           psexesvc.exe
*** 3916  3772            512370d.exe
```

<h3>Detecting Lateral Movement via WMI Execution</h3>

<p>Volatility Terminal</p>

```bash
analyst@tryhackme$ vol -f conti.dmp windows.pstree
PID     PPID    ImageFileName
4       0       System
* 272   4       smss.exe
* 384     376     csrss.exe
* 460     376       wininit.exe
* 600     460         services.exe
** 1244   600           svchost.exe
*** 2416  1244            wmiprvse.exe
**** 5156 2416             cobaltrs.exe
```

<h3>Detecting Lateral Movement via PowerShell Remote</h3>

<p>Volatility Terminal</p>

```bash
analyst@tryhackme$ vol -f FIN12.dmp windows.pstree
PID     PPID    ImageFileName
4       0       System
* 272   4       smss.exe
* 384     376     csrss.exe
* 460     376       wininit.exe
* 600     460         services.exe
** 1280   600           svchost.exe
*** 2532  1280            wsmprovhost.exe
**** 4896 2532              cmd.exe
***** 5012 4896               conhost.exe
***** 5144 4896               trickbot.exe
```

<h3 align="left"> Answer the questions below</h3>

> 3.1. <em>The IR team suspects that the threat actor may have performed lateral movement to this host. Which executed process provides evidence of this activity?</em><br><a id='3.1'></a>
>> <strong><code>wmiprvse.exe</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/34ca2e6e-92d1-4692-941e-5624170e0847)


<br>

> 3.2. <em>What is the MITRE technique ID associated with the lateral movement method used by the threat actor?</em><br><a id='3.2'></a>
>> <strong><code>t1021.006</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/7de65b12-cd40-49bd-85c2-91d24fff89e1)

![image](https://github.com/user-attachments/assets/be6d698a-df55-49cd-b278-4b89e40ec8cb)



<br>

> 3.3. <em>Which other process was executed as part of the lateral movement activity to this host?</em><br><a id='3.3'></a>
>> <strong><code>TeamsView.exe</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/459a4558-fc48-4a41-ade9-d5ab4f34631a)

![image](https://github.com/user-attachments/assets/adfe70e7-001f-4d06-a3ce-ef3bcbc8c175)

![image](https://github.com/user-attachments/assets/74b859e3-64c3-440a-a251-4eb38f2a5ff8)


<br>

> 3.4. <em>What is the Security Identifier (SID) of the user account under which the process was executed on this host?</em><br><a id='3.4'></a>
>> <strong><code>S-1-5-21-3147497877-3647478928-1701467185-1008</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/dcbd996c-8c35-4e06-b3b3-83526aebb6c4)


<br>

> 3.5. <em>What is the name of the domain-related security group the user account was a member of?</em><br><a id='3.5'></a>
>> <strong><code>Domain Users</code></strong><br>
<p></p>

<br>

> 3.6. <em>Which processes related to discovery activity were executed by the threat actor on this host? Format: In alphabetical order</em><br><a id='3.6'></a>
>> <strong><code>ipconfig.exe,systeminfo.exe,whoami.exe</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/76a812b0-7af8-4ce8-a6fa-6fb919db4568)

<br>

> 3.7. <em>What is the Command and Control IP address that the threat actor connected to from this host as a result of the previously executed actions? Format: IP Address:Port</em><br><a id='3.7'></a>
>> <strong><code>34.244.169.133:1995</code></strong><br>
<p></p>


![image](https://github.com/user-attachments/assets/735b6e47-9602-4f66-8058-6bad3a5ae8d2)


<br>

<h2> Task 4 . Privilege Ecalation and Credential Dumping</h2>

<h3 align="left"> Answer the questions below</h3>


> 4.1. <em>Conduct a deeper investigation and identify another suspicious process on the host. Provide a full path to the process in your answer.</em><br><a id='4.1'></a>
>> <strong><code>C:\Windows\Temp\pan.exe</code></strong><br>
<p></p>


![image](https://github.com/user-attachments/assets/bb068cd0-6ac6-49f0-ab8a-0d976189bf68)

<br>

> 4.2. <em>Which account was used to execute this malicious process?</em><br><a id='4.2'></a>
>> <strong><code>Local System</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/e490c87d-6af0-4a38-a757-cd6611b2ded9)

<br>

> 4.3. <em>What was the malicious command line executed by the process?</em><br><a id='4.3'></a>
>> <strong><code>privilege::debug sekurlsa::logonpasswords</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/2cb7863c-95c4-41df-b8ba-06a356ef77cc)

<br>

> 4.4. <em>Given the command line from the previous question, which well-known hacker tool is most likely the malicious process?</em><br><a id='4.4'></a>
>> <strong><code>Mimikatz</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/422324c2-3692-4e2c-be85-b5192724c867)

<br>

> 4.5. <em>Which MITRE ATT&CK technique ID corresponds to the method the attacker employed to evade detection, as identified in the previous steps?</em><br><a id='4.5'></a>
>> <strong><code>T1036</code></strong><br>
<p></p>


<br>

<h2> Task 5 . Conclusion</h2>

<h3 align="left"> Answer the questionsbelow</h3>

> 5.1. <em>Well Done!</em><br><a id='5.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>

<h1 align="center">Room Completed</h1>
<br>
<p align="center"><img width="1000px" src="https://github.com/user-attachments/assets/d3951dc3-7aef-4f94-9da6-261fb65911a3"><br>
                  <img width="1000px" src="https://github.com/user-attachments/assets/c4341a4b-daf3-4506-8292-0f52fba07e9"></p>

<h1 align="center"> My TryHackMe Journey</h1>
<br>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| June 16 2025      | 406      |     203ʳᵈ    |      5ᵗʰ     |     374ᵗʰ   |     7ᵗʰ    |  107,875 |    780    |     62    |

</div>

<p align="center"> Global All Time:  203ʳᵈ<br><br>
<img width="240px" src="https://github.com/user-attachments/assets/a46986cc-1b45-4fc7-a835-624107ab6eb1"><br>
<img width="1000px" src="https://github.com/user-attachments/assets/f1353cd2-5441-44ab-807a-6dbb39e87351"></p>
<p align="center"> Brazil All Time:     5ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/f3aa2835-1a45-47f8-b71a-171445593e98"> </p>
<p align="center"> Global monthly:    374ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/35f846df-aa20-49b4-b8fe-58db6d177d4c"> </p
<p align="center"> Brazil monthly:       7ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/ddab973b-d995-44e5-ab35-fcf97b46eb13"> </p>

<h1 align="center">Thanks for coming!!!</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<h1 align="center">Thank you</h1>
<p align="center"><a href="https://tryhackme.com/p/tryhackme">tryhackme</a> and <a href="https://tryhackme.com/p/krotovolb">krotovolb</a>  for investing your time and effort to develop this challenge so that I could sharpen my skills!</p> 
