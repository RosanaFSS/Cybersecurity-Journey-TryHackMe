<p align="center">May 12, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{370}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/62cf4572-71af-43ed-898e-31c0887632ce" alt="streak"></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Security Footage}}$$</h1>
<p align="center"><em>Perform digital forensics on a network capture to recover footage from a camera.</em>.<br>
It is classified as an easy-level CTF.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/securityfootage"</a>.</p>

<p align="center"> <img width="1000px" src=""> </p>


<br>
<br>

<h2>Task 1 . Security Footgae</h2>

<p>[  Download Task Files  ]</p>

<p>Someone broke into our office last night, but they destroyed the hard drives with the security footage. Can you recover the footage?<br><br>

Note: If you are using the AttackBox, you can find the task files inside the /root/Rooms/securityfootage/ directory.</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> 1.1. <em>What is the flag?</em><a id='1.1'></a>
>> <code><strong></strong></code><br>

<br>

<p><ol type="1. ">
    <li>Downloaded Task File | &nbsp; security-footage-1648933966395.pcap.<br><br></li>
    <li>Protocol hierarchy &nbsp; | &nbsp; analyzed it clicking <code>Statistics</code> --> <code>Protocol Hierarchy</code>.<br>
        There are protocols <code>TCP</code> and <code>HTTP</code>.<br><br></li>
    <li>xx &nbsp; | &nbsp; Tehere is just 1 <code>HTTP</code> packet.<br>
           Related to <code>Source IP</code> : <code>10.0.2.15</code><br><code>Source Port</code> : <code>42312</code><br><code>Destination IP</code> : <code>192.168.1.100</code><br><code>Destination Port</code> : <code>8081</code>.<br><br></li>
    <li>xx &nbsp; | &nbsp; xx.<br><br></li>
    <li>xx &nbsp; | &nbsp; xx.<br><br></li>
    <li>xx &nbsp; | &nbsp; xx.<br><br></li>
</ol></p>

<p>2</p>

![image](https://github.com/user-attachments/assets/d4a353f5-5f82-4978-a144-2aa081a702ca)

<br>

<p>3</p>

![image](https://github.com/user-attachments/assets/31c4b598-e588-405b-8875-9d3c6393d9aa)

<br>






