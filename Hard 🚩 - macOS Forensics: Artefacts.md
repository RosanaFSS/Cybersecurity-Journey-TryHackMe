<p align="center">April 18, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{346}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/515f9049-42dc-4683-80a3-f51908ea1361" alt="streak"></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{macOS Forensics: Artefacts}}$$</h1>
<p align="center"><em>Understand the forensic artefacts in macOS and learn to leverage them for forensic analysis.</em>.<br>
It is classified as a hard-level CTF.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/macosforensicsartefacts">here</a>.</p>

<p align="center"> <img width="1000px" src=""> </p>

<br>


<h2>Task 1 . Introduction </h2>
<p>...</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 1.1. <em>What command can be used to mount the image named mac-disk.img to the directory ~/mac in the attached VM, making sure the Data volume is mounted?</em><br><a id='1.1'></a>
>> <strong><code>apfs-fuse -v 4 mac-disk.img ~/mac</code></strong><br>
<p></p>

<br>

<p align="center"><img width="1000px" src="https://github.com/user-attachments/assets/c51c7320-6265-4dea-8ba1-4be1abe78ec8">https://github.com/sgan81/apfs-fuse<br> </p>

<br>
<br>


<h2>Task 2 . Before We Begin </h2>
<p>...</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 2.1. <em>What command can be used to mount the image named mac-disk.img to the directory ~/mac in the attached VM, making sure the Data volume is mounted?</em><br><a id='2.1'></a>
>> <strong><code>plistutil</code></strong><br>
<p></p>

<br>

<p align="center"><img width="1000px" src="https://github.com/user-attachments/assets/346588ce-1889-4f6f-960f-f29b4f6b9282">https://man.archlinux.org/<br> </p>


<br>
<br>


<h2>Task 3 . System Information </h2>
<p>...</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 3.1. <em>When was the OS installed on the disk image present in the attached VM? Write your answer as GMT in the format: YYYY-MM-DD hh:mm:ss </em><br><a id='3.1'></a>
>> <strong><code>2024-12-08 17:42:28</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/c667267f-5f85-4c57-943f-c64a09485f5d)

<br>

![image](https://github.com/user-attachments/assets/67eb08d1-b0f3-4793-8007-f61559382c30)

<br>

<p><code>thm</code>:<code>12345</code><br><br>
<code>ubuntu</code>:<code>TryHackMe!</code></p>

![image](https://github.com/user-attachments/assets/8f722bbf-ce47-40ba-87c9-6b1f0b0ac7cc)

<br>

<p>Localtime:</p>

<br>

![image](https://github.com/user-attachments/assets/56fe91c7-fa91-42f9-8912-d5c78648d1f0)

<br>

<p>The default is <code>UTC</code>.<br><br>
<code>UTC</code> = <code>GMT</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/07f1e324-b76d-4a1d-8ce2-8d3e5e1128ac)

<br>

> 3.2. <em>What is the country code for this machine?</em>Hint : Which artefact gives you the country locale?<br><a id='3.2'></a>
>> <strong><code>AE</code></strong><br>
<p></p>


<br>

![image](https://github.com/user-attachments/assets/9a8c20e8-2d76-46f3-8d63-f194cf213b1a)

<br>

![image](https://github.com/user-attachments/assets/60d434f3-0d4e-4f4a-9f19-ae6dde3c1753)


<br>

![image](https://github.com/user-attachments/assets/bed4564a-b97f-48ba-8824-f00e80e58118)

<br>


> 3.3. <em>When was the last time this machine booted up? Write your answer as GMT in the format: YYYY-MM-DD hh:mm:ss</em>Hint : <em>You will need to convert the time from Unix epoch to human-readable format</em><br><a id='3.3'></a>
>> <strong><code>2025-01-19 15:47:05</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/7fbf999e-567a-4f21-a2f9-6be85aca1411)

<br>

<p>Used <code>unixtimestamp.com</code></p>

<br>

![image](https://github.com/user-attachments/assets/2066a6c9-0282-4bf4-a654-4a4bd773d0f9)

<br><br>


<h2>Task 4 . Network Information </h2>
<p>...</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 4.1. <em>What is the name of the machine's built-in network interface? </em><br><a id='4.1'></a>
>> <strong><code>en0</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/9586b01c-b6c2-4480-9b63-a37752d8e31a)


<br>




> 4.2. <em>What is the IP address of the router this machine was last connected to?<br><a id='4.2'></a>
>> <strong><code>192.168.64.1</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/5355783d-91ca-401b-9c53-c3bba4d14e9b)

<br><br>


<h2>Task 5 . Account Activity </h2>
<p>...</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 5.1. <em>What is the name of the last logged in user? </em><br><a id='5.1'></a>
>> <strong><code>thm</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/e05402a8-aa2b-4a92-ab9e-84812942057c)


<br>

![image](https://github.com/user-attachments/assets/ded961b1-602d-4ffe-aacc-31add68a8512)

<br>




> 5.2. <em>What is the password hint for the user?<br><a id='5.2'></a>
>> <strong><code>__________</code></strong><br>
<p></p>

<br>

> 5.3. <em>When was the last time a user logged out of the machine? Format MMM DD hh:mm:ss?<br><a id='5.2'></a>
>> <strong><code>__________</code></strong><br>
<p></p>

<br>


<br>



