<h1 align="center"> Windows Memory & Network<br><img width="1200px" src="https://github.com/user-attachments/assets/3c611801-4d91-40e8-b35b-a2395cf04ada"></h1>

<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/eec07c31-df33-48de-a52b-2b9b701ba625"><br>
June 11, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my401-day-streak in  <a href="https://tryhackme.com">TryHackMe</a><br>
Identify C2 traffic & post-exploit activity in Windows memory. <a href="https://tryhackme.com/room/windowsmemoryandnetwork"</a>here.<br><br>
<img width="1000px" src="5"></p>

<br>
<br>

<h2> Task 1 . Introduction</h2>

<p>This room continues the memory investigation from the previous analysis. This is the last room out of 3, and we will be focusing on how network activity and post-exploitation behavior are captured in RAM. We’ll examine artifacts from a live attack involving advance payloads like Meterpreter, suspicious child processes, and unusual outbound connections. All analyses will be performed using Volatility 3 and hands-on techniques applied directly to the memory dump.<br><br>

We’ll walk through real indicators tied to remote shells, persistence via startup folder abuse, and malware attempting outbound communications. Users will use memory structures, plugin outputs, and process inspection to track network behavior step by step.</p>

<h3>Learning Objectives</h3>
<p>

-  Identify network connections in a memory dump.<br>
- Identify suspicious ports and remote endpoints.<br>
- Link connections to processes.<br>
- Detect reverse shells and memory injections in a memory dump.<br>
- Trace PowerShell and C2 activity in memory.
- 
</p>

<h3>Prerequisites</h3>

<p>

- Volatility <br>
- Yara<br>
- Windows Memory & Processes<br>
- Windows Memory & User Activity
</p>

<h3 align="left"> Answer the question below</h3>

> 1.1. <em>Click to continue the room</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

<h2> Task 2 . Scenario Information</h2>

<h3>Scenario</h3>
<p></p>You are part of the incident response team handling an incident at TryHatMe - a company that exclusively sells hats online. You are tasked with analyzing a full memory dump of a potentially compromised Windows host. Before you, another analyst had already taken a full memory dump and gathered all the necessary information from the TryHatMe IT support team. You are a bit nervous since this is your first case, but don't worry; a senior analyst will guide you.</p>

<h3>Information Incident THM-0001</h3>

<p>

- On May 5th, 2025, at 07:30 CET, TryHatMe initiated its incident response plan and escalated the incident to us. After an initial triage, our team found a Windows host that was potentially compromised. The details of the host are as follows:<nbr>
--- Hostname: WIN-001
--- OS: Windows 1022H 10.0.19045
  
- At 07:45 CET, our analyst Steve Stevenson took a full memory dump of the Windows host and made a hash to ensure its integrity. The memory dump details are:
---Name: <code>THM-WIN-001_071528_07052025.dmp</code>
---MD5-hash: <code>78535fc49ab54fed57919255709ae650</code></p>


<h3>Company Information TryHatMe</h3>
<h4>Network Map</h4>

![image](https://github.com/user-attachments/assets/32b6a505-ccd7-4fef-b229-e9a416a1ecb3)


<h3 align="left"> Answer the question below</h3>

> 2.1. <em>I went through the case details and am ready to find out more.</em><br><a id='2.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

<h2> Task 3 . Environment & Setup</h2>

<h2> Task 4 . Analyzing Active Connections</h2>

<h2> Task 5 .  Investigating Remote Access and C2 Communications</h2>

<h2> Task 6 .  Post-Exploitation Communication</h2>

<h2> Task 7 .  Putting it All Together</h2>

<h2> Task 8 .  Conclusion</h2>




