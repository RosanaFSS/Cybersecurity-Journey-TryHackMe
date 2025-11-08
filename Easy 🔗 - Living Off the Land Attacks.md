<h2 align="center">SOC Level 1 . Malware Concepts for SOC</h2>
<h1 align="center">Living Off the Land Attacks</h1>
<p align="center">2025, November 8  &nbsp; .  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure on my <code>1</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>Learn to detect and analyse Living Off the Land attacks using trusted Windows tools. &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/livingoffthelandattacks">here</a>.<br><br><img width="1200px" src="https://github.com/user-attachments/assets/b81870b5-7b1b-4bd8-b475-4b4771b496bf"></p>

<h2>Task 1 . Introduction</h2>

<p><em>Answer the question below</em></p>

<p>1.1. Click to start learning about Living Off The Land techniques!<br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 . Common LoL Tools and Techniques</h2>

<p><em>Answer the questions below</em></p>

<p>2.1. Which public site lists Unix/Linux native binaries and how they can be abused?<br>
<code>GTFOBins</code></p>

<p>2.2. Which Microsoft toolset includes PsExec and Autoruns, used for admin tasks and often misused by attackers?<br>
<code>Sysinternals</code></p>

<br>
<h2>Task 3 . Real-World Examples</h2>

<p><em>Answer the questions below</em></p>

<p>3.1. What MITRE technique ID covers WMI event subscriptions?<br>
<code>T1546.003</code></p>

<img width="1345" height="284" alt="image" src="https://github.com/user-attachments/assets/db5cdd76-a096-4010-9f70-669c74b6b699" />

<br>
<br>
<p>3.2. Which abbreviated name refers to one of the services that C2s, like Cobalt Strike, use to start or listen for remote services?<br>
<code>SMB</code></p>

<br>
<h2>Task 4 . Detecting LoL activity</h2>

<p><em>Answer the questions below</em></p>

<p>4.1. Which PowerShell switch is used to download text/strings and execute them?<br>
<code>IEX</code></p>

<img width="1254" height="250" alt="image" src="https://github.com/user-attachments/assets/09e38265-91f6-425d-abda-d0fd6eded124" />

<br>
<br>
<p>4.2. Which WMIC keyword triggers the creation of a new process on a remote host?<br>
<code>create</code></p>

<img width="1264" height="226" alt="image" src="https://github.com/user-attachments/assets/28b7210a-ca7a-479a-9f30-9a387f6c3078" />

<br>
<br>
<h2>Task 5 . Practical</h2>
<h3>Your virtual environment has been set up</h3>
<p>All machine details can be found at the top of the page.</p>

<p>Please start the machine, check the example, and then classify the alerts in the following URL to get the flag. https://LAB_WEB_URL.p.thmlabs.com </p>


<p><em>Answer the questions below</em></p>

<p>5.1. What is the flag?<br>
<code>THM{•••••••••••••••••••••••••••••••••}</code></p>

<img width="1320" height="811" alt="image" src="https://github.com/user-attachments/assets/426ae45f-8b9f-42b1-bbd4-571da1920d4c" />

<br>
<br>

<img width="1314" height="818" alt="image" src="https://github.com/user-attachments/assets/a1df2021-42b2-4c32-86a0-fd33bb1ef45a" />

<br>
<br>
<h2>Task 6 . Wrapping up</h2>
<p>In this room, we examined how attackers repurpose trusted Windows utilities to carry out malicious activity without introducing new binaries. By testing and analysing each command safely, we observed how legitimate administrative tools such as PowerShell, WMIC, Certutil, Mshta, Rundll32, and Scheduled Tasks can be abused for execution, persistence, lateral movement, or evasion. Through these exercises, we developed a clearer view of how to recognise, detect, and respond when normal system processes are used with malicious intent.<br>

We learned to:<br>

- Identify the built-in Windows tools most often abused in Living Off the Land attacks.<br>
- Understand how PowerShell enables fileless, in-memory, and automated execution.<br>
- Observe how WMIC supports remote process creation and system reconnaissance.<br>
- Recognise the ways Certutil downloads, encodes, or decodes malicious payloads.<br>
- Detect Mshta and Rundll32 being used to run scripts or DLL-based payloads.<br>
- Spot persistence mechanisms are created or triggered through Scheduled Tasks.<br>
- Interpret process command lines and SIEM detections to separate admin from attacker behaviour.<br>
- Apply defensive techniques such as enhanced logging, behavioural detection, and execution control to limit LoL activity.</p>


<p><em>Answer the question below</em></p>

<p>6.1. Click here to finish the room<br>
<code>No answer needed</code></p>

<br>
<br>
<br>
<h1 align="center">Completed</h1>

<p align="center">One more bug. That is one the reasons I slowed down my journey on TryHackMe.<img width="1200px" src="https://github.com/user-attachments/assets/5b031c74-bb5c-4a46-b953-94a093885679"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/4bd3dd9a-34de-4c46-9273-69979e3e4e02"><br><
                  <img width="1200px" src=https://github.com/user-attachments/assets/2bac8ec8-5150-4467-b932-5ad6c1fe39b1"><br><br><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/f4e95a47-7631-40bf-b878-0fe07d82c18e"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, November</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|8       |Easy 🔗 - Living of the Land Attacks  |   1    |      91ˢᵗ    |      4ᵗʰ     |  1,759ᵗʰ   |     17ᵗʰ     |    132,642  |    1,018    |    80     |
|8       |Hard 🚩 - Lost in RAMslation          |   1    |      91ˢᵗ    |      4ᵗʰ     |  2,547ᵗʰ   |     25ᵗʰ     |    132,580  |    1,017    |    80     |

</h6></div><br>

<br>

<p align="center">Global All Time:   91ˢᵗ<br><img width="250px" src="https://github.com/user-attachments/assets/06761d90-a26e-4dc6-afa1-f3b124d83007"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/1c5fe255-7e26-4e19-ae76-c7a767d2e548"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/36ff16d1-f999-40d9-b154-d0785e69dc38"><br>
                  Global monthly:    1,759ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/2c9710ac-53bc-4ed5-a56b-ed92b1c48b9"><br>
                  Brazil monthly:      17ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/109e9e64-8785-4e1b-8dd3-e5538a4162f5"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
