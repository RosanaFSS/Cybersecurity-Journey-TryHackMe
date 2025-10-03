<h1 align="center">XDR: Operation Global Dagger2</h1>
<p align="center">2025, October 3<br>Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>515</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Investigate and detect potential threats across your environmentr</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/0768833b-b246-46a2-8298-ecbc3354b395"><br>
Access it <a href="https://tryhackme.com/room/vulnnetdotpy">here</a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/8e37fb43-f9df-42ce-a37f-96b457350897"></p>


<h2>Task 1 . Introduction</h2>
<p>Continuing to investigate the incident from Operation Global Dagger 1, we need to investigate more unusual user and machine behaviours, some persistent activities, malicious executions, and attempts by an attacker to disable the organisation's security solution.</p>

<h3>Room Objectives</h3>
<p>In the next task, you will be required to use different Microsoft Defender XDR products and features to detect and investigate various activities within your organisation, such as:<br>

- Malicious persistence activities<br>
- Malicious executions on devices<br>
- Evasion of security tools<br>
- Lateral movement</p>

<h3>Prerequisites</h3>
<p>
  
- <a href="https://tryhackme.com/room/xdroperationglobaldagger">Operation Global Dagger 1</a> room<br>
- <a href="https://tryhackme.com/module/defender">Microsoft Defender XDR module</a><br>
- <a href="https://tryhackme.com/room/mitre">MITRE room</a></p>

<p><em>Answer the question below</em></p>

<p>1.1. Good, let´s go!<br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 . Lab Instructions</h2>
<br>

<p><em>Answer the question below</em></p>

<p>2.1. I understand.<br>
<code>No answer needed</code></p>

<br>
<h2>Task 3 . <code>Investigate</code>  Operation Global Dagger</h2>
<p>Log in to the Defender XDR portal with the credentials below.<br>

Access your lab by clicking the <strong>Cloud Details</strong> button below in conjunction with the lab instructions from Task 2:</p>

<p>[   Cloud Details    ]</p>

<p>Navigate to <code>Incidents & response</code> -> <code>Incidents & alerts</code>code> -> <code>Incidents</code>code> to start your investigation.

On the Microsoft Defender portal, look for incident ID 54 <strong>Hands-on keyboard attack was launched from a compromised account (attack disruption)</strong> to begin.</p>


<p><em>Answer the questions below</em></p>

<p>3.1. What is the name of the alert generated due to persistent activities that was terminated by the system?<br>
<code>Suspicious service registration</code></p>

<img width="1887" height="879" alt="image" src="https://github.com/user-attachments/assets/020b813b-af8d-4653-8f57-2e516279b3e3" />

<br>
<br>
<br>

<img width="1900" height="321" alt="image" src="https://github.com/user-attachments/assets/16655c74-3710-4bec-bc14-4d0faf9cdec7" />

<br>
<br>
<br>

<img width="1883" height="461" alt="image" src="https://github.com/user-attachments/assets/84f14f3b-77f0-4be8-878f-08ce6d94e967" />

<br>
<br>
<br>
<p>3.2. How many suspicious evidence entities were found for the alert from question 1?<br>
<code>3</code></p>

<img width="1890" height="900" alt="image" src="https://github.com/user-attachments/assets/a4bb41dc-f2c0-4511-878b-f51adc58b46d" />

<br>
<br>
<br>
<p>3.3. What Registry operation did the attacker perform in the alert from question 1?<br>
<code>RegistryModification</code></p>

<img width="1885" height="472" alt="image" src="https://github.com/user-attachments/assets/583788a2-c932-472d-a03e-590ccf46c18c" />

<br>
<br>
<br>
<p>3.4. What is the object MD5 value of the initiation process from the alert in question 1?<br>
<code>*********************************</code></p>

<img width="1900" height="888" alt="image" src="https://github.com/user-attachments/assets/2ffe22de-4b5f-4f69-b16b-f264f03b35bd" />

<br>
<br>
<br>

<img width="1904" height="894" alt="image" src="https://github.com/user-attachments/assets/d1b01cd9-f553-46aa-88c5-03ba556d9a7b" />

<br>
<br>
<br>
<p>3.5. Find the alert <strong>Attempt to turn off Microsoft Defender Antivirus protection</strong> which has the "true positive" classification set. What is the Disabled setting value?<br>
<code>DisableRealtimeMonitoring</code></p>

<img width="1892" height="410" alt="image" src="https://github.com/user-attachments/assets/03f3c5fe-354f-4ddd-bc89-68db6c046364" />

<br>
<br>
<br>

<img width="1894" height="894" alt="image" src="https://github.com/user-attachments/assets/65ec95e1-c767-409d-ae64-058af5e24ec2" />

<br>
<br>
<br>

<img width="1904" height="602" alt="image" src="https://github.com/user-attachments/assets/86cf6111-0531-4d7a-aa3c-ac5ae9e99dae" />

<br>
<br>
<br>
<p>3.6. What command was used by the attacker to initiate the process in the alert from question 5?<br>
<code>reg  add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableRealtimeMonitoring" /t REG_DWORD /d "1" /f  </code></p>

<img width="1910" height="892" alt="image" src="https://github.com/user-attachments/assets/e8a22815-9450-4c28-b0dd-d08ce9c48ecb" />

<br>
<br>
<br>
<p>3.7. Find the alert <strong>Suspicious behavior by cmd.exe was observed</strong>strong> which has a classification set. What is the evidence entity name that has the process ID 2232?<br>
<code>WMIC.exe</code></p>

<img width="1904" height="883" alt="image" src="https://github.com/user-attachments/assets/b1045707-f90b-4ebe-8988-17e6632c4d14" />

<br>
<br>
<br>
<img width="1902" height="832" alt="image" src="https://github.com/user-attachments/assets/19e73206-fe0c-483d-8490-de5edb54f33c" />

<br>
<br>
<br>
<img width="1910" height="893" alt="image" src="https://github.com/user-attachments/assets/f1e21d7c-ded5-45c9-9942-954ac007b2cf" />

<br>
<br>
<br>
<p>3.8. What are the MITRE tactics related to the alert in question 7? (Answer in alphabetical order)<br>
<code>Discovery, Execution</code></p>

<img width="1912" height="888" alt="image" src="https://github.com/user-attachments/assets/6f8cfe6c-a054-4862-94c8-1d9222e34b8a" />

<br>
<br>
<br>
<p>3.9. What is the flag found in the alert from question 7?<br>
<code>THM{*************************}</code></p>

<img width="1893" height="874" alt="image" src="https://github.com/user-attachments/assets/3c197897-cc2e-4351-95f5-1abc640c891a" />

<br>
<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/184e0930-2bda-4ba0-a3d5-c32420c3ed17"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/c9b274c4-9849-4791-8401-97b65c3bbe1f"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, October</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|3       |Medium 🚩 - XDR: Operation Global Dagger2| 515  |     104ᵗʰ    |      4ᵗʰ     |     149ᵗʰ    |     3ʳᵈ    | 128,833  |    987    |    76     |
|3       |Medium 🚩 - VulnNet: dotpy             | 515    |     108ᵗʰ    |      4ᵗʰ     |     741ˢᵗ    |    11ˢᵗ    | 128,563  |    986    |    76     |
|2       |Medium 🔗 - Data Exfiltration Detection| 514    |     108ᵗʰ    |      4ᵗʰ     |     521ˢᵗ    |     8ᵗʰ    | 128,503  |    985    |    76     |
|1       |Medium 🔗 - Network Discovery Detection| 513    |     108ᵗʰ    |      4ᵗʰ     |     875ᵗʰ    |     7ᵗʰ    | 128,407  |    984    |    76     |
|1       |Medium 🚩 - Intranet                   | 513    |     108ᵗʰ    |      4ᵗʰ     |    3,357ᵗʰ   |    57ᵗʰ    | 128,335  |    983    |    76     |

</h6></div>
<br>

<p align="center">Global All Time:   104ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/536b28a4-62f1-4895-a3e4-9074eacf6b8"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/1a1f6746-60f2-47a2-bdc4-cf3fcdeb0ab7"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/13a70e64-5c6b-4bec-a26e-c5bf43dbbd51"><br>
                  Global monthly:     149ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/fbd0cc26-049b-4586-8b0e-ccb806023c15"><br>
                  Brazil monthly:       3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/7aafbe5c-41b3-4c4e-9f97-522a9a435a03"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
