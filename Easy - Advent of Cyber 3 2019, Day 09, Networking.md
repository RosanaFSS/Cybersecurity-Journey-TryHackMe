<p align="center">March 20, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{318}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
  <img width="160px" src="https://github.com/user-attachments/assets/67d84414-d9e4-4068-be03-f10e812305dd"></p>


<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{[ Day 9 ] - Advent of Cyber 3 (2021)}}$$
</h1>
<p align="center">Get started with Cyber Security in 25 Days - Learn the basics by doing a new, beginner friendly security challenge every day leading up to Christmas. It is classified as an easy-level walkthrough, and you can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed. <a href="https://tryhackme.com/room/adventofcyber3">[ Day 8 ] - Advent of Cyber 3 (2021)</a>.</p>
                                                              
<p align="center"> <img width="900px" src=""> </p>

<br>

<p align="center"> <img width="900px" src=""> </p>

<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{Networking | Where is All This Data Going}}$$
</h1>

<br>
<p><p align="center">March 20, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{318}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
  <img width="160px" src="https://github.com/user-attachments/assets/67d84414-d9e4-4068-be03-f10e812305dd"></p>


<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{[ Day 9 ] - Networking - Advent of Cyber 3 (2021)}}$$
</h1>
<p align="center">Get started with Cyber Security in 25 Days - Learn the basics by doing a new, beginner friendly security challenge every day leading up to Christmas. It is classified as an easy-level walkthrough, and you can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed. <a href="https://tryhackme.com/room/adventofcyber3">[ Day 8 ] - Advent of Cyber 3 (2021)</a>.</p>
                                                              
<p align="center"> <img width="900px" src=""> </p>

<br>

<p align="center"> <img width="900px" src=""> </p>

<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{[ Day 9 ] - Networking - Advent of Cyber 3 (2021)}}$$
</h1>

<br>

<p>McSkidy recently found out that a large amount of traffic is entering one system on the network. Use your traffic analysis skills to determine what kind of activities Grinch Enterprises are performing.</p>

<p>In this task, we will walk you through the required skills and knowledge to perform a basic packet analysis using Wireshark.<br>

Packet analysis is a technique used to capture and intercept network traffic that passes the computer’s network interfaces. Packet analysis may also be called with different terms such as packet sniffer, packet analyzer, protocol analyzer, or network analyzer. As a cybersecurity individual, gaining packet analysis skills is an important requirement for network troubleshooting and communication protocol analysis. Using network analysis tools such as Wireshark, it captures network packets in real-time and displays them in a human-readable format. It provides many advanced features, including the live capture and offline analysis. This task covers the packet analysis steps in detail using Wireshark to analyze various protocols (unencrypted protocols) such as HTTP, DNS, and FTP.</p>

<h3>Required Skills and Knowledge</h3>h3>

<p>We’re assuming that the user has basic background skills to complete this task, requires theoretical and practical knowledge, including basic networking concepts, TCP/IP Stack, OSI Model, and TCP handshake. This applies not only to packet analysis but also to most other topics we will deal with in cybersecurity.</p>

<h3>Packet Analysis Tools</h3>

<p>There are many tools that are used in network traffic analysis and network sniffing. Each of these tools provides a different way to capture or dissect traffic. Some offer ways to copy and capture, while others read and ingest using different interfaces. In this room, we will explore Wireshark. Keep in mind that these tools require administrator privileges.</p>

<h3>What is Wireshark?</h3>

<p>Wireshark is pre-installed on the THM AttackBox, and you can just launch the THM AttackBox by using the Start AttackBox button and opening Wireshark.</p>

<p>If you want to do this challenge on your own computer, Wireshark can be downloaded from here: Download Wireshark.<br>

For this task, we have prepared a PCAP file to download and follow the instructions and apply the required packet analysis skills using different scenarios. If you're using the AttackBox you don't need to download the file as it's already on the machine; the AoC3.pcap file is in the following location: /root/Rooms/AoC3/Day9/AoC3.pcap.<br>

We can run Wireshark and import the provided PCAP file as follows,</p>


<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>


> 1.1. <em>Read the premise above, start the attached Windows analysis machine and find the transcription logs in the SantasLaptopLogs folder on the Desktop.
> If you want to RDP into the machine, start the AttackBox and enter the following into a terminal: xfreerdp /u:Administrator /p:grinch123! /v:Target_IP - The credentials for the machine are Administrator as the username, and grinch123! as the password.</em><a id='1.1'></a>
>> <code><strong>No answer needed</strong></code><br><br>


<p>Used Remmina.  Entered the credentials provided for this task.</p>



r account, and copies a unique file to the Desktop. Before it is copied to the Desktop, what is the full path of the original file? </em><br><a id='1.4'></a>
>> <code><strong>C:\Users\santa\AppData\Local\Microsoft\Windows\UsrClass.dat</strong></code><br><br>


<p>Double-clicked on the last file in the <code>SantasLaptopLogs</code>, and discovered the answer.</p>

![image](https://github.com/user-attachments/assets/5e7e042e-be37-4dd2-8ec0-ad0ecc63319a)

<br>

> 1.5. <em>The actor uses a Living Off The Land binary (LOLbin) to encode this file, and then verifies it succeeded by viewing the output file. What is the name of this LOLbin?</em><br><a id='1.5'></a>
>> <code><strong>certutil.exe</strong></code><br><br>

<p>Discovered the answer in the same file analyzed in the 1.4.</p>

![image](https://github.com/user-attachments/assets/595af745-6996-4584-bf1f-0fe7c3324aa5)

<br>

<p>[ ... ]</p>

> 1.6. <em>Drill down into the folders and see if you can find anything that might indicate how we could better track down what this SantaRat really is. What specific folder name clues us in that this might be publicly accessible software hosted on a code-sharing platform?</em><br><a id='1.6'></a>
>> <code><strong>No answer needed</strong></code><br><br>

<p>Opened <code>ShellBagsExplorer.exe</code> directory which in located in the Desktop.<br>
Double-clicked <code>ShellBagsExplorer</code>.</p>

![image](https://github.com/user-attachments/assets/b42aa7ce-f56c-4bb3-aff0-38e2e2b179a0)

<br>


> 1.7. <em>Read the above and open the ShellBagsExplorer.exe application found in the folder on your Desktop.</em><br><a id='1.7'></a>
>> <code><strong>No answer needed</strong></code><br><br>

<p>Opened <code>ShellBagsExplorer.exe</code> directory which in located in the Desktop.<br>
Right-clicked <code>ShellBagsExplorer</code>.<br>
Clicked <code>Run as Administrator</code>.</p>

![image](https://github.com/user-attachments/assets/de717f4a-9d2c-417c-a4bf-457b9419e74d)


> 1.8. <em>Drill down into the folders and see if you can find anything that might indicate how we could better track down what this SantaRat really is. What specific folder name clues us in that this might be publicly accessible software hosted on a code-sharing platform?</em><br><a id='1.8'></a>
>> <code><strong>github</strong></code><br><br>

<p>Copied the content <code>santa.data</code> in <code>PowerShell_transcript.LAPTOP.Zw6PA+c4.20211128153734</code> file between <code>----BEGIN CERTIFICATE-----</code> and <code>-----END CERTIFICATE-----</code>.</p>

![image](https://github.com/user-attachments/assets/304f4c29-52fc-41de-b93c-41d8cbd28215)








<br>

<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$
</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          | WorldWide    | Brazil       | WorldWide   | Brazil     |          | Completed |           |
| March 20, 2025    | 318      |     354ᵗʰ    |        8ᵗʰ   |    835ᵗʰ    |      11ˢᵗ  |  87,001  |       621 |   59      |

</div>

<p align="center"> Global All Time: 354ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/ab1fa808-049c-4dad-a848-b609307283dc"> </p>

<p align="center"> Brazil All Time: 8ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/6d0501d4-836c-4397-90c3-f4fde161ae38"> </p>

<p align="center"> Global monthly: 835ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/edff857b-d678-4f7b-8d9f-183195ef936e)"> </p>

<p align="center"> Brazil monthly: 11ˢᵗ<br><br><img width="900px" src="https://github.com/user-attachments/assets/497d78b1-bef4-49d2-87db-c24261416a87"> </p></p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>


> 1.1. <em>Read the premise above, start the attached Windows analysis machine and find the transcription logs in the SantasLaptopLogs folder on the Desktop.
> If you want to RDP into the machine, start the AttackBox and enter the following into a terminal: xfreerdp /u:Administrator /p:grinch123! /v:Target_IP - The credentials for the machine are Administrator as the username, and grinch123! as the password.</em><a id='1.1'></a>
>> <code><strong>No answer needed</strong></code><br><br>


<p>Used Remmina.  Entered the credentials provided for this task.</p>



<br>

<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$
</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          | WorldWide    | Brazil       | WorldWide   | Brazil     |          | Completed |           |
| March 20, 2025    | 318      |     354ᵗʰ    |        8ᵗʰ   |    835ᵗʰ    |      11ˢᵗ  |  87,001  |       621 |   59      |

</div>

<p align="center"> Global All Time: 354ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/ab1fa808-049c-4dad-a848-b609307283dc"> </p>

<p align="center"> Brazil All Time: 8ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/6d0501d4-836c-4397-90c3-f4fde161ae38"> </p>

<p align="center"> Global monthly: 835ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/edff857b-d678-4f7b-8d9f-183195ef936e)"> </p>

<p align="center"> Brazil monthly: 11ˢᵗ<br><br><img width="900px" src="https://github.com/user-attachments/assets/497d78b1-bef4-49d2-87db-c24261416a87"> </p>
