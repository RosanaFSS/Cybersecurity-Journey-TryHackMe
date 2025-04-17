<p align="center">April 16, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{345}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="" alt="Your Image Badge"><br></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{DiskFiltration}}$$</h1>
<p align="center"><em>Stay out of my server!</em>.<br>
It is classified as a hard-evel CTF.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/biteme">here</a>.</p>

<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/0356038c-47eb-454e-8a0e-a259e5da0a15"> </p>


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

[image](https://github.com/user-attachments/assets/df8fb5c0-b56f-4b9e-94e1-57d4b64bf887)

<br>

<p>Analyzed the <code>Device ID</code> field following the guidance provided in the hint.</p>


![image](https://github.com/user-attachments/assets/618d5e99-6e5b-4451-b653-11e459849aaa)



<br>

>1.2. <em>What is the profile name of the personal hotspot Liam used to evade network-level detection?<br><a id='1.1'></a>
>> <strong><code>2651931097993496666	</code></strong><br>
<p></p>

<br>

> 1.3. <em>What is the name of the zip file Liam copied from the USB to the machine for exfiltration instructions?</em><br><a id='1.3'></a>
>> <strong><code>Shadow_Plan.zip</code></strong><br>
<p></p>

<br>


![image](https://github.com/user-attachments/assets/9836f23f-f259-483d-a107-358b4425d789)

<br>

> 1.4. <em>What is the password for this zip file?</em>Hint : <em>Liam did open a text file containing this pass.</em><br><a id='1.4'></a>
>> <strong><code>Qwerty@123</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/21dd4c0b-248f-49a5-b606-2cdb36797b16)



<br>




