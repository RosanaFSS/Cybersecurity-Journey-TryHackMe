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
    <li>There is just 1 <code>HTTP</code> packet. Related to<br> - <code>Source IP</code> : <code>10.0.2.15</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp; <code>Source Port</code> : <code>42312</code><br>- <code>Destination IP</code> : <code>192.168.1.100</code> &nbsp; | &nbsp; <code>Destination Port</code> : <code>8081</code>.<br><br></li>
    <li>TCP &nbsp; | &nbsp; Righed-clicked the 1st TCP packet, selected <code>Follow</code> and <code>TCP stream</code>.<br><br></li>
    <li>chunked &nbsp; | &nbsp; <code>jpeg</code> images were set to be sent in chunks.<br><br></li>
    <li>Boundary &nbsp; | &nbsp; <code>--BoundaryString</code> was used to separate the images´s frames.<br>
        Identified the header <code>JFIF</code>.<br><br></li>
    <li>jpeg header and footer &nbsp; | &nbsp; learned in <a href="https://tryhackme.com/room/filecarving">File Carving</a> challenge the signatures for a jpeg file.<br><br></li>
</ol></p>

flag{5ebf457ea66b2877fdbca2de9ec86f31}

<p>2</p>

![image](https://github.com/user-attachments/assets/d4a353f5-5f82-4978-a144-2aa081a702ca)

<br>

<p>3</p>

![image](https://github.com/user-attachments/assets/31c4b598-e588-405b-8875-9d3c6393d9aa)

<br>

<p>4</p>

![image](https://github.com/user-attachments/assets/5586fb7a-9770-4730-8503-c8b41d51163e)

<br>

<p>5</p>

![image](https://github.com/user-attachments/assets/a99ace5d-420f-4ad3-80b3-42749a1866a0)

<br>

![image](https://github.com/user-attachments/assets/f027ff99-c3e6-42d7-b8e2-af2c9ae47a50)


<br>

<p>6</p>

![image](https://github.com/user-attachments/assets/9b5b9f01-e306-46d2-965a-fced1f88261d)


<br>

<p>7</p>

![image](https://github.com/user-attachments/assets/22482162-0fae-45ac-9755-ae764b2a5362)


<br>


<p><code>(tcp.flags.ack == True && tcp.flags.push == True && frame contains "Boundar" && frame.number != 1108)</code></p>

<br>

![image](https://github.com/user-attachments/assets/513b8c01-4a66-4b6f-bab2-84ccaf608f29)

<br>






![image](https://github.com/user-attachments/assets/6212e09c-3c0d-4ae5-ac1d-5e520f1813cc)





