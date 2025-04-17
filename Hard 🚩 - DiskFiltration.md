<p align="center">April 16, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{345}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="" alt="Your Image Badge"><br>
<img width="300px" src="https://github.com/user-attachments/assets/dbaabd6d-47b5-4cd6-9800-eb50114e599d" alt="streak"></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{DiskFiltration}}$$</h1>
<p align="center"><em>Stay out of my server!</em>.<br>
It is classified as a hard-evel CTF.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/biteme">here</a>.</p>

<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/0356038c-47eb-454e-8a0e-a259e5da0a15"> </p>


![image](https://github.com/user-attachments/assets/dbaabd6d-47b5-4cd6-9800-eb50114e599d)


<h2>Task 2 . The Exfiltratopm Hunt </h2>

<p>[  Start Machine  ]</p>

<p>...</p>


<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 1.1. <em>What is the serial number of the USB device Liam used for exfiltration? </em>Hint : <em>If anywhere you get "&0" at the end of the serial number, ignore it, as it is just an instance identifier.</em><br><a id='1.1'></a>
>> <strong><code>2651931097993496666	</code></strong><br>
<p></p>

<br>

<p>Launched <code>Autopsy</code>.</p>

![image](https://github.com/user-attachments/assets/533ac813-78e5-4832-afd6-baf7e16e7195)

<br>

<p>Double-clicked <code>Open a Recent Case</code>.</p>

![image](https://github.com/user-attachments/assets/919eaa3f-0000-450b-9e2d-b2b9b8853bf1)

<br>


<p>Clicked <code>Open</code>.</p>

![image](https://github.com/user-attachments/assets/da45f725-1563-4b60-9ecc-7d0d693534ce)

<br>

<p>Clicked <code>Artifacts</code>.</p>

![image](https://github.com/user-attachments/assets/3ad77b06-ee4b-4e3e-abb1-cca2dd1a9040)


<br>

<p>Clicked <code>USB Device Attached</code>.</p>

![image](https://github.com/user-attachments/assets/df8fb5c0-b56f-4b9e-94e1-57d4b64bf887)

<br>

<p>Analyzed the <code>Device ID</code> field following the guidance provided in the hint.</p>

![image](https://github.com/user-attachments/assets/618d5e99-6e5b-4451-b653-11e459849aaa)

<br>

>1.2. <em>What is the profile name of the personal hotspot Liam used to evade network-level detection?</em><br><a id='1.2'></a>
>> <strong><code>Liam's Iphone</code></strong><br>
<p></p>

<br>

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


<br>

<p>Identified the highlighted <code>change</code> in the system.</p>

<br>

![image](https://github.com/user-attachments/assets/adb77d8e-6061-4c2c-ae87-704a8fae5cbf)

<br>

![image](https://github.com/user-attachments/assets/5ef140fb-43fa-4046-8a51-3e627da34502)

ProfileName	REG_SZ	Liam's Iphone

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

<p>I practiced another way to discover the answer.<br><br>
Launched <code>Exiftool</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/b341b1b5-bca4-4c7d-b6bc-067e8294cdc1)


<br>

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

> 1.9. <em>The external entity didn't fully trust Liam for the exfiltration so they asked him to execute file_uploader.exe, through the instructions in PDF. When was this file last executed and how many times was it executed? (YYYY-MM-DD HH:MM:SS, number of execution times)<br><a id='1.4'></a>
>> <strong><code>2025-01-29 11:26:09, 2</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/5ce51ccf-b57c-453d-927a-bb774754a6cb)


<br>

> 1.10. <em>Liam received a hidden flag inside a file (in the zip folder) from the external entity helping him. What was that?<br><a id='1.10'></a>
>> <strong><code>______</code></strong><br>
<p></p>

<br>

<br>

> 1.11. <em>It seems like Liam caused one last damage before leaving. When did Liam delete "Tax Records.docx"? (YYYY-MM-DD HH:MM:SS)<br><a id='1.11'></a>
>> <strong><code>______</code></strong><br>
<p></p>

<br>

> 1.12. <em>Which social media site did Liam search for using his web browser? Likely to avoid suspicion, thinking somebody was watching him. (Full URL)<br><a id='1.12'></a>
>> <strong><code>https://www.facebook.com/</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/103e43f2-dd1d-4b51-b61e-34d54bfe882c)

<br>

> 1.13. <em>What is the PowerShell command Liam executed as per the plan?<br><a id='1.13'></a>
>> <strong><code>Get-WmiObject -Class Win32_Share | Select-Object Name, Path</code></strong><br>
<p></p>

<br>


![image](https://github.com/user-attachments/assets/5496eb67-f7b6-48d1-8324-9d09872d5a85)

<br>




