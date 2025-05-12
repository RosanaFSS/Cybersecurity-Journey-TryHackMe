<p align="center">May 12, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{371}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/51810771-2c6a-4810-b8ae-f276f9525f6f" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/5c310a08-6e8d-4bc7-bbe4-7d1b5189f24b" alt="streak"></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Security Footage}}$$</h1>
<p align="center"><em>Perform digital forensics on a network capture to recover footage from a camera.</em>.<br>
It is classified as an easy-level CTF.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/securityfootage"</a>.</p>

<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/49f59741-e668-4f92-804b-8cd2cf54eeca"> </p>




<br>
<br>

<h2>Task 1 . Security Footgae</h2>

<p>[  Download Task Files  ]</p>

<p>Someone broke into our office last night, but they destroyed the hard drives with the security footage. Can you recover the footage?<br><br>

Note: If you are using the AttackBox, you can find the task files inside the /root/Rooms/securityfootage/ directory.</p>


<p><ol type="1. ">
    <li>Downloaded Task File | &nbsp; security-footage-1648933966395.pcap.<br><br></li>
    <li>Protocol hierarchy &nbsp; | &nbsp; analyzed it clicking <code>Statistics</code> --> <code>Protocol Hierarchy</code>.<br>
        There are protocols <code>TCP</code> and <code>HTTP</code>.<br><br></li>
    <li>There is just 1 <code>HTTP</code> packet. Related to<br> - <code>Source IP</code> : <code>10.0.2.15</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp; <code>Source Port</code> : <code>42312</code><br>- <code>Destination IP</code> : <code>192.168.1.100</code> &nbsp; | &nbsp; <code>Destination Port</code> : <code>8081</code>.<br><br></li>
    <li>TCP &nbsp; | &nbsp; Used <code>tcp</code> to filter the packaged.<br>Right-clicked the 1st TCP packet.<br>Selected <code>Follow</code> and <code>TCP stream</code>.<br>Selected <code>Raw</code> for the <code>Show as</code> field.<br>Defined the filename <code>tcpstream</code>code> clicking <code>Save as...</code>, typing the name and clicking <code>Save</code>.<br><br></li>
    <li>Chunks &nbsp; | &nbsp; <code>jpeg</code> images were sent in chunks.<br><br></li>
    <li>Boundary &nbsp; | &nbsp; <code>--BoundaryString</code> was used to separate the images´s frames.<br>
        Identified the header <code>JFIF</code>.<br><br></li>
    <li>Signature &nbsp; | &nbsp; learned in <a href="https://tryhackme.com/room/filecarving">File Carving</a> challenge the signatures for a jpeg file.<br><br></li>
</ol></p>


<p align="center">2 . Protocol hierarchy<br><br><img width="1000px" src="https://github.com/user-attachments/assets/d4a353f5-5f82-4978-a144-2aa081a702ca"></p>

<br>

<p align="center">3 . HTTP<br><br><img width="1000px" src="https://github.com/user-attachments/assets/31c4b598-e588-405b-8875-9d3c6393d9aa"></p>

<br>

<p align="center">4 . TCP<br><br><img width="1000px" src="https://github.com/user-attachments/assets/d43de789-a12d-415f-b609-55ecad5fae4a"><br>
                                <img width="1000px" src="https://github.com/user-attachments/assets/5586fb7a-9770-4730-8503-c8b41d51163e"><br>
                                <img width="1000px" src=""><br>
                                <img width="1000px" src=""></p>


<br>

<p align="center">5 . Chunks<br><br><img width="1000px" src="https://github.com/user-attachments/assets/a99ace5d-420f-4ad3-80b3-42749a1866a0"></p>

<br>

<p align="center"><img width="1000px" src="https://github.com/user-attachments/assets/f027ff99-c3e6-42d7-b8e2-af2c9ae47a50"></p>

<br>

<p align="center">6 . Boundary<br><br><img width="1000px" src="https://github.com/user-attachments/assets/9b5b9f01-e306-46d2-965a-fced1f88261d"></p>

<br>

<p align="center">7 . Signature<br><br><img width="1000px" src="https://github.com/user-attachments/assets/22482162-0fae-45ac-9755-ae764b2a5362"></p>

<br>


<br>


<p><code>(tcp.flags.ack == True && tcp.flags.push == True && frame contains "Boundar" && frame.number != 1108)</code></p>

<br>

![image](https://github.com/user-attachments/assets/513b8c01-4a66-4b6f-bab2-84ccaf608f29)

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> 1.1. <em>What is the flag?</em><a id='1.1'></a>
>> <code><strong>flag{5ebf457ea66b2877fdbca2de9ec86f31}</strong></code><br>

<br>


<br>
<br>
<br>


<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>

<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/2e18ef45-210d-4c27-a73d-24fbba7293de"> </p>

<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/705a8751-d04d-470d-a62a-4208f834d249"> </p>


<br>
<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |   Global     |   Brazil     |   Global    |   Brazil   |          | Completed |           |
| May 12, 2025      | 371      |    230ᵗʰ     |        5ᵗʰ   |   414ᵗʰ     |    6ᵗʰ     |  101,203 |       725 |   62      |

</div>

<p align="center"> Global All Time:  230ᵗʰ <br><br><img width="1000px" src="https://github.com/user-attachments/assets/e6e8e91d-2071-4c53-aa0e-46623986afd0"> </p>

<p align="center"> Brazil All Time: 5ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/a48b7538-0417-4292-bb1c-fc3b98eeebf0"> </p>

<p align="center"> Global monthly: 414ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/293652b3-3a72-4b51-ad96-557cc17f8071"> </p>

<p align="center"> Brazil monthly: 6ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/a48b7538-0417-4292-bb1c-fc3b98eeebf0"> </p>


<br>
<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>


<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/ben">ben</a>, <a href="https://tryhackme.com/p/tryhackme">tryhackme</a>, <a href="https://tryhackme.com/p/timtaylor">timtaylor</a> and <a href="https://tryhackme.com/p/congon4tor">congon4tor</a> for investing your time and effort to develop this walkthrough so that I could sharpen my skills!</p>
