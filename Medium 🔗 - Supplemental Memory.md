<h1 align="center">Supplemental memory<br><img width="1200px" src="https://github.com/user-attachments/assets/3c611801-4d91-40e8-b35b-a2395cf04ada"></h1>

<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/a6a395b7-d5e5-4749-81f1-45cc4619f512"><br>
June 14, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure,<br>
part of my <code>404</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br>
Investigate lateral movement, credential theft, and additional adversary actions in a memory dump.<a href="https://tryhackme.com/room/supplementalmemory"</a>here.<br>
<img width="1200px" src=""></p>

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
umair@Umairs-MacBook-Pro LaunchAgents % pwd   
/Users/umair/Library/LaunchAgents
umair@Umairs-MacBook-Pro LaunchAgents % plutil -p net.tunnelblick.tunnelblick.LaunchAtLogin.plist 
{
  "ExitTimeOut" => 0
  "Label" => "net.tunnelblick.tunnelblick.LaunchAtLogin"
  "LimitLoadToSessionType" => "Aqua"
  "ProcessType" => "Interactive"
  "ProgramArguments" => [
    0 => "/Applications/Tunnelblick.app/Contents/Resources/Tunnelblick-LaunchAtLogin"
  ]
  "RunAtLoad" => 1
}
```



<h2> Task 4 . Privilege Ecalation and Credential Dumping</h2>


<h2> Task 5 . Conclusion</h2>




