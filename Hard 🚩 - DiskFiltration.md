<p align="center">April 17, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{346}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/43c4495e-9e34-4f38-ad2a-1a701b4064f0" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/dbaabd6d-47b5-4cd6-9800-eb50114e599d" alt="streak"></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{DiskFiltration}}$$</h1>
<p align="center"><em>Test your Windows investigation skills on a critical data exfiltration case.</em>.<br>
It is classified as a hard-level CTF.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/diskfiltration">here</a>.</p>

<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/8e5a3c8b-b8fd-4d79-9628-b29253f67ec9"> </p>

<br>


<h2>Task 1 . Attack Chain </h2>
<p>An overview of the attack chain is provided in the table below:</p>

<br>

![image](https://github.com/user-attachments/assets/d804cc64-c54d-4b10-aee6-11ac530a8bbe)


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 1.1. <em>Ready for the challenge?</em><br><a id='1.1'></a>
>> <strong><code>NO answer needed</code></strong><br>
<p></p>

<br>
<br>


<h2>Task 2 . The Exfiltration Hunt </h2>

<p>[  Start Machine  ]</p>

<h3>Room Prerequisites</h3>

<p>Before solving this room, it is recommended to go through the following rooms:<br>

- Autopsy<br>
- Expediting Registry Analysis<br>
- File Carving<br>
- NTFS Analysis<br>
- Windows Forensics 1<br>
- Windows Forensics 2<br>
- Scenario</p>

<h3>Scenario</h3>
<p>Tech THM discovered their critical data had been leaked to the competitors. After an internal investigation, the company suspects Liam, a recently terminated employee who was working as a system engineer with Tech THM. This suspicion was raised as Liam had access to the leaked data in his company-provided workstation. He often worked late hours without clear justification for his extended presence. He was also caught roaming around the critical server room and taking pictures of the entry gate. Following these suspicions, Liam’s workstation (provided by the company) was investigated. The initial investigation suggests that an external entity was also helping Liam.<br><br>

Let's use the knowledge we gained from the previous modules of this path to search for traces of Liam's activities.</p>

<h3>Starting the Machine</h3>
<p>...</p>


<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 1.1. <em>What is the serial number of the USB device Liam used for exfiltration? </em>Hint : <em>If anywhere you get "&0" at the end of the serial number, ignore it, as it is just an instance identifier.</em><br><a id='1.1'></a>
>> <strong><code>2651931097993496666	</code></strong><br>
<p></p>

<br>

<p align="center">Launched <code>Autopsy</code>.</p>

![image](https://github.com/user-attachments/assets/533ac813-78e5-4832-afd6-baf7e16e7195)

<br>

<p align="center">Double-clicked <code>Open a Recent Case</code>.</p>

![image](https://github.com/user-attachments/assets/919eaa3f-0000-450b-9e2d-b2b9b8853bf1)

<br>

<p align="center">Clicked <code>Open</code>.</p>

![image](https://github.com/user-attachments/assets/da45f725-1563-4b60-9ecc-7d0d693534ce)

<br>

<p align="center">Clicked <code>Artifacts</code>.</p>


![image](https://github.com/user-attachments/assets/3ad77b06-ee4b-4e3e-abb1-cca2dd1a9040)


<br>

<p align="center">Clicked <code>USB Device Attached</code>.</p>


![image](https://github.com/user-attachments/assets/df8fb5c0-b56f-4b9e-94e1-57d4b64bf887)

<br>

<p align="center">nalyzed the <code>Device ID</code> field following the guidance provided in the hint.</p>


![image](https://github.com/user-attachments/assets/618d5e99-6e5b-4451-b653-11e459849aaa)

<br>

>1.2. <em>What is the profile name of the personal hotspot Liam used to evade network-level detection?</em><br><a id='1.2'></a>
>> <strong><code>Liam's Iphone</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/5ef140fb-43fa-4046-8a51-3e627da34502)

<br>

> 1.3. <em>What is the name of the zip file Liam copied from the USB to the machine for exfiltration instructions?</em><br><a id='1.3'></a>
>> <strong><code>Shadow_Plan.zip</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/782ce9e1-31f0-4fd8-a388-a682094cf4a3)



<br>

> 1.4. <em>What is the password for this zip file?</em>Hint : <em>Liam did open a text file containing this pass.</em><br><a id='1.4'></a>
>> <strong><code>Qwerty@123</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/21dd4c0b-248f-49a5-b606-2cdb36797b16)

<br>

> 1.5. <em>Time to reveal the external entity helping Liam! Who is the author of the PDF file stored in the zip file?</em><br><a id='1.5'></a>
>> <strong><code>Henry</code></strong><br>
<p></p>

<br>

<p>Exported <code>Shadow_Plan.zip</code> to the same directory of <code>exiftool.exe</code>.<br><br>
Unzipped <code>Shadow_Plan.zip</code> using the <code>password</code> just discovered.</p>

<br>

![image](https://github.com/user-attachments/assets/f0944d12-260f-49eb-ad9f-b747dcdc104b)

<br>

> 1.6. <em>What is the correct extension of the file that has no extension in the zip folder?</em><br><a id='1.6'></a>
>> <strong><code>png</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/14278bb5-7b9f-4fb1-b1ae-87e87bffd1f7)


<br>
<br>

> 1.7. <em>It looks like Liam searched for some files inside the file explorer. What are the names of these files? (alphabetical order)</em>Hint : <em>Spinning around the Wheel!</em><br><a id='1.7'></a>
>> <strong><code>Financial, Revenue</code></strong><br>
<p></p>

<br>

<p><code>/img_dis.E01/vol_vol3/Users/Administrator</code><br><br>
In <code>Application</code> window -----<code>Software\Microsoft\Windows\CurrentVersion\Explorer\WorWheelQuery</code></p>

<br>

![image](https://github.com/user-attachments/assets/b182e66c-6567-4beb-8781-30d01b47a526)

<br>

![image](https://github.com/user-attachments/assets/9a8f8c24-1f44-43db-8a5c-d224ee74268e)

<br>

![image](https://github.com/user-attachments/assets/49179d6d-7041-4d3c-a4fe-491353ac2657)


<br>

> 1.8. <em>What are the names of the folders that were present on the USB device? (alphabetical order)</em>Hint : <em>What the shell!</em><br><a id='1.4'></a>
>> <strong><code>Critical Data TECH THM, Exfiltration Plan</code></strong><br>
<p></p>

<br>

<p>Navigate to <code>/img_dis.E01/vol_vol3/Users/Administrator/AppData/Roaming/Microsoft/Windows/Recent/AutomaticDestinations/f01b4d95cf55d32a.automaticDestinations-ms/Critical Data TECH THM.lnk	</code></p>

<br>

![image](https://github.com/user-attachments/assets/db428365-c19a-4a8a-810c-0eff544c65b5)

<br>

<p>Navigate to <code>/img_dis.E01/vol_vol3/Users/Administrator/AppData/Roaming/Microsoft/Windows/Recent/AutomaticDestinations/f01b4d95cf55d32a.automaticDestinations-ms/Exfiltration Plan.lnk</code></p>

![image](https://github.com/user-attachments/assets/61443edc-4180-413c-bbf5-a0356370cd8a)

<br>

<p>After I generated the Autopsy report, I just clicked <code>Recent Documents</code> and could easily visualized the documents in <code>E:\</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/3eaffc0b-89a5-497b-8445-d92f1c4424fa)

<br>

> 1.9. <em>The external entity didn't fully trust Liam for the exfiltration so they asked him to execute file_uploader.exe, through the instructions in PDF. When was this file last executed and how many times was it executed? (YYYY-MM-DD HH:MM:SS, number of execution times)</em><br><a id='1.4'></a>
>> <strong><code>2025-01-29 11:26:09, 2</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/5ce51ccf-b57c-453d-927a-bb774754a6cb)


<br>

> 1.10. <em>Liam received a hidden flag inside a file (in the zip folder) from the external entity helping him. What was that?</em>Hint : <em>Ask meta where is your data?</em><br><a id='1.10'></a>
>> <strong><code>FLAGT{THM_TECH_DATA}</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/78d74893-d89a-4031-bbd9-94c89cac3a6d)


<br>

> 1.11. <em>It seems like Liam caused one last damage before leaving. When did Liam delete "Tax Records.docx"? (YYYY-MM-DD HH:MM:SS)</em><br><a id='1.11'></a>
>> <strong><code>2025-01-29 11:29:02</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/a3b0eed7-a66d-48e7-a33c-5816d1a117ff)

<br>

![image](https://github.com/user-attachments/assets/93da41ea-a94e-4104-abf3-8e308d7f5ad9)

<br>

![image](https://github.com/user-attachments/assets/dca60083-e63a-4e57-87ef-2c4bbbc3f643)

<br>

![image](https://github.com/user-attachments/assets/6025bc65-84e3-47f6-888d-8af5b2b6f7d0)

<br>





> 1.12. <em>Which social media site did Liam search for using his web browser? Likely to avoid suspicion, thinking somebody was watching him. (Full URL)</em><br><a id='1.12'></a>
>> <strong><code>https://www.facebook.com/</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/103e43f2-dd1d-4b51-b61e-34d54bfe882c)

<br>

> 1.13. <em>What is the PowerShell command Liam executed as per the plan?</em><br><a id='1.13'></a>
>> <strong><code>Get-WmiObject -Class Win32_Share | Select-Object Name, Path</code></strong><br>
<p></p>

<br>


![image](https://github.com/user-attachments/assets/5496eb67-f7b6-48d1-8324-9d09872d5a85)

<br>
<br>

<h2>Here is how I generated the report in <code>Autopsy</code>.</h2>

<p>Clicked <code>Generate Report</code> in <code>Autopsy</code>.<br><br>
In 2 minutes the report was generated.</p>
<br>

![image](https://github.com/user-attachments/assets/9fb1d7cd-4b42-4fe0-aded-e69f6010fadb)


<br>

![image](https://github.com/user-attachments/assets/ee763ac9-d8a6-4996-a21f-4ba1e29ded5a)

<br>

![image](https://github.com/user-attachments/assets/e6939f5c-3470-4f73-9852-66e9552b3b6a)

<br>

![image](https://github.com/user-attachments/assets/5f8e56a2-138b-46a0-bb91-74296b8f8703)


<br><br><br>

<p>Identified the highlighted <code>change</code> in the system.</p>

<br>

![image](https://github.com/user-attachments/assets/adb77d8e-6061-4c2c-ae87-704a8fae5cbf)


<br>
<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center">
<img width="900px" src="https://github.com/user-attachments/assets/219e61ed-76ba-4a81-96ee-24ce4acf6693"><br>
<img width="900px" src="https://github.com/user-attachments/assets/45aa792b-92e4-4748-8843-986e86a3be57"></p>

<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>


<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |   Brazil     |    Global   |   Brazil   |          | Completed |           |
| April 17, 2025    |   346    |     272ⁿᵈ    |     6ᵗʰ      |      51ˢᵗ    |     2ⁿᵈ    |  95,433  |    671    |    59     |

</div>


<br>

<p align="center"> Global All Time:  272ⁿᵈ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/bd95ecd0-0dee-4984-9b84-bba08439abbd"> </p>

<p align="center"> Brazil All Time:    6ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/fa7cf89e-6102-4e48-8117-fb8f9d969ca4"> </p>

<p align="center"> Global monthly:     51ˢᵗ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/8109a277-13f9-4694-b90f-ffa51a553c61"> </p>

<p align="center"> Brazil monthly:      2ⁿᵈ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/3e799729-405f-4e7c-8a34-ce922f53510e"> </p>


<br>

<p align="center">Weekly League: Silver 3ʳᵈ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/49f08f11-8419-4156-bf58-24d3f6924248"> </p>

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/tryhackme">tryhackme</a> and <a href="https://tryhackme.com/p/Aashir.Masood">Aashir.Masood</a>  for investing your time and effort to develop this walkthrough so that I could sharpen my skills!</p> 

