<p align="center">April 28, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{357}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/31522e39-894f-48bb-9cf7-6cbbe0541657" alt="Your Image Badge"><br></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{XDR : Execution}}$$</h1>
<p align="center"><em>Investigate and prevent techniques that run malicious code on local or remote systems using Defender XDR.</em>.<br>
It is classified as a medium-level walkthrough.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/xdrexecution">here</a>.</p>

<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/31cebadd-110e-4f53-bf1d-73e918fa1975"> </p>

<br>
<br>


<h2>Task 1 . Introduction </h2>
<p>[ ... ]</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 1.1. <em>Cool, let's go!</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>


<h2>Task 2 . Execution Attack Tatics </h2>
<p>[ ... ]</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 2.1. <em>What technique is it when a threat actor tries to use command-line tools to execute malicious commands?</em><br><a id='2.1'></a>
>> <strong><code>Command and scripting</code></strong><br>
<p></p>

<br>
<br>


<h2>Task 3 . Technique - PowerShell </h2>
<p>[ ... ]</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 3.1. <em>As part of mitigation, what rules can security admins configure to block suspicious script execution?</em><br><a id='3.1'></a>
>> <strong><code>Attack Surface Reduction</code></strong><br>
<p></p>

<br>


> 3.2. <em>Aside from running it locally, which other way can threat actors run PowerShell commands to execute a malicious payload?</em><br><a id='3.2'></a>
>> <strong><code>remotely</code></strong><br>
<p></p>

<br>
<br>


<h2>Task 4 . Technique - Scheduled Task / Job</h2>
<p>[ ... ]</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 4.1. <em>What can be implemented to prevent unauthorised administrators from setting up scheduled tasks on remote systems?</em><br><a id='4.1'></a>
>> <strong><code>Least Privilege Principle</code></strong><br>
<p></p>

<br>
<br>


<h2>Task 5 . Lab - Detect and Investigate</h2>
<h3>Lab Scenario</h3>
<p>In this lab task, as the security admin in charge of Microsoft Defender XDR, you receive an incident alert of a malicious PowerShell script on a user device and must investigate the incident before escalation. </p>

<p>Note: To follow through, you can use the lab credentials and URL below:</p>

<p>[  Credentials  ]</p>

<p>Additionally: The incidents shown in this task might differ from the ones in the lab.</p>

<p>Suspicious PowerShell Script<br>

- Click the Incidents & alert dropdown and select Incidents<br>
- On the incidents screen, modify the time range to 6 months<br>

![image](https://github.com/user-attachments/assets/738c731f-9b37-4da2-a33d-da3461b67e6a)


- Find the incident with the name Multi-stage incident involving Execution & Lateral movement on one endpoint (Incident Id: 42), and click the toggle icon to open the dropdown menu. Click the X to close the sidebar if it opened.<br>

![image](https://github.com/user-attachments/assets/fb547216-ea63-4246-9164-cc64ac32de54)

- Scroll down to find the incident A script with suspicious content was observed; to see more information regarding this incident scroll down on the sidebar.<br>
- Click the Open alert page to begin the investigation.<br>

![image](https://github.com/user-attachments/assets/2cbbcd38-d0b1-4e9a-b1e3-3fc5943933dc)

Since this is a multi-stage incident, it's expected to see other related incidents. However, we are particular about the suspicious PowerShell script.<br><br>

On the new screen, the following can be seen:<br>

1 . The device involved<br>
2 . The user account involved<br>
3 . The time of each execution or event<br>
4 . The event name. You can click on each event to see the script on the sidebar<br>
5 . The executed script<br>

![image](https://github.com/user-attachments/assets/2da6d763-a4ed-4e33-b5ad-cab3ac390a39)

- Click on Alert timeline to see our specific alert details.<br>

![image](https://github.com/user-attachments/assets/2237f407-9505-4cca-a562-219d82ccef5d)

- Click on Alert timeline to see our specific alert details.<br>

![image](https://github.com/user-attachments/assets/3855c48a-46bd-4508-955f-91a01d347dee)

To investigate this alert, in addition to the device and user account details, we can see the following details:<br>

- The date and time this script was executed<br>
- The severity of this alert (Medium)<br>
- The event, powershell.exe executed a script<br>
- The content of the script can be copied for further forensic investigations<br>


![image](https://github.com/user-attachments/assets/58ec0993-487f-43c3-a7eb-aca21210b878)

- Click the Remote execution dropdown for more details.<br><br>
As seen in the content, this script is going to execute an Invoke-Mimikatz.ps1 file from a GitHub repo remotely.<br>


![image](https://github.com/user-attachments/assets/1c69e92f-46cc-4453-b5e6-dc76bcb36ebc)

After investigation, if this alert is considered a malicious event, the following can be done to mitigate the threat and prevent further escalation.<br>

- We can run an antivirus scan.<br>
- Restrict applications from executing on this machine<br>
- Start Microsoft Defender XDR automated investigation<br>
- Isolate the device to prevent lateral movement or the attack from getting access to other devices<br>

![image](https://github.com/user-attachments/assets/f3207f60-7e6d-4510-b7e3-4923caab30d8)


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 5.1. <em>What is the severity of the incident A script with suspicious content was observed?</em><br><a id='5.1'></a>
>> <strong><code>medium</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/8522e511-20e5-433e-83d2-fcdbeaa5a3e9)


<br>

![image](https://github.com/user-attachments/assets/e6a92fcd-fbcb-4ff9-b5b5-15383b8620a6)


<br>

![image](https://github.com/user-attachments/assets/2023a4a4-fc53-4b95-83f4-13bff147bd05)


<br>

![image](https://github.com/user-attachments/assets/cbbb24de-48e3-4391-ba8e-de354d566697)


> 5.2. <em>What is the name of the script to be executed?</em><br><a id='5.2'></a>
>> <strong><code>Invoke-Mimikatz.ps1</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/86cb066b-9d5a-4f77-928f-97735e3e35de)



> 5.3. <em>What is the category of the A script with suspicious content was observed incident?</em><br><a id='5.3'></a>
>> <strong><code>Execution</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/a92d4955-2a58-4196-a368-82ba8930ecdd)


<br>
<br>


<h2>Task 6 . XDR: Prevent, Detect and Mitigate Execution Attacks</h2>
<p>[ ... ]</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 6.1. <em>On Microsoft Defender for Office 365, what security control will prevent the execution of harmful scripts or malware embedded in attachments?</em><br><a id='6.1'></a>
>> <strong><code>Safe Attachment</code></strong><br>
<p></p>

<br>


> 6.2. <em>On Microsoft Defender for Endpoint, what ASR rule do you need to prevent scripts from launching potentially malicious downloaded content?</em><br><a id='6.2'></a>
>> <strong><code>Block JavaScript or VBScript from launching downloaded executable content</code></strong><br>
<p></p>

<br>


> 6.3. <em>The Microsoft Defender for Endpoint's device discovery should be set to 'standard discovery' is a prerequisite for which mitigation and response?</em><br><a id='6.3'></a>
>> <strong><code> automatic attack disruption</code></strong><br>
<p></p>

<br>
<br>


<h2>Task 7 . Conclusion</h2>
<p>In this room, we discussed execution attack tactics and Microsoft Defender XDR's comprehensive approach to securing an organisation's digital environment through a layered defence strategy, ensuring enhanced protection against execution attacks.<br><br>

Specifically, we explored the following topics:<br>

- An overview of execution attack tactics.<br>
- PowerShell technique.<br>
- Schedule task/job technique.<br>
- Investigating an execution incident.<br>
- Discussed some prevention, detection, and mitigation techniques with Microsoft - Defender XDR.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 7.1 <em>I understand execution tactics and can investigate these!</em><br><a id='7.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center">
<img width="1000px" src="https://github.com/user-attachments/assets/df20cd0f-543e-4319-b801-bf1a52738cff"><br>
<img width="1000px" src="https://github.com/user-attachments/assets/911d8634-0f7a-4364-a5c2-bc82a0b1e3e6"></p>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>


<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| April 28, 2025    | 357      |     248ᵗʰ    |      6ᵗʰ     |     58ᵗʰ    |     2ⁿᵈ    |  98,075  |    695    |     60    |

</div>

<br>


<p align="center"> Global All Time:  248ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/b762d079-1215-4985-820c-b5df91add7c9"> </p>

<p align="center"> Brazil All Time:    6ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/eb64b7a7-8bac-46cc-8ee7-dd43cf9493af"> </p>

<p align="center"> Global monthly:    58ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/4090a3af-f4d7-4ab3-98bd-df4295f819f2"> </p>

<p align="center"> Brazil monthly:    2ⁿᵈ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/6097afe2-c4da-45cc-b09c-e9effe672143"> </p>


<br>
<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/tryhackme">tryhackme</a>, <a href="https://tryhackme.com/p/zieglers">zieglers</a> and <a href="https://tryhackme.com/p/HumaneJard">HumaneJard</a> for investing your time and effort to develop this challenge so that I could sharpen my skills!</p> 
