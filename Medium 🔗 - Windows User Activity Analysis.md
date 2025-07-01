<h1 align="center">Windows Endpoint Investigation<br>Advanced Endpoint Investigation<img width="660px" src=""><br>Windows User Activity Analysis</h1>

<p align="center"July 1, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{421}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="" alt="Your Image Badge"><br></p>
<p align="center"><em>What happened in those 36 hours? A forensics case to solve.</em>.<br>
It is classified as a medium-level walkthrough.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/windowsuseractivity">here</a>.</p>


<p align="center"> <img width="1000px" src=""> </p>

<br>
<br>

<h2> Task 1 . Introduction</h2>

<h3 align="left"> Answer the question below</h3>

> 1.1. <em>Continue to the next task</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

<h2> Task 2 . Lab Connection Instructions</h2>

<h3 align="left"> Answer the question below</h3>

> 2.1. <em>Connect with the lab. How many tools / folders are in the EZ tools folder on the Desktop?</em><br><a id='2.1'></a>
>> <strong><code>12</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/1785b7c0-ecb4-435e-9745-46da7359ea9d)

<br>

<h2> Task 3 . Revisiting Registry</h2>

<h3 align="left"> Answer the questions below</h3>

> 3.1. <em>Which Hive stores information about installed software?</em><br><a id='3.1'></a>
>> <strong><code>SOFTWARE</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/1795eaa6-c88a-4dcf-9291-22e657d5c323)


<br>

> 3.2. <em>What is the current size of the SAM Hive in the attached lab? (In KB)</em><br><a id='3.2'></a>
>> <strong><code>128</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/a745006f-81cf-4111-9d93-ae8d9b0599e4)

<br>

<h2> Task 4 . Performing Registry Forensics</h2>

<h3 align="left"> Answer the questions below</h3>

> 4.1. <em>The suspect typed a suspicious path in the Windows Explorer, that points to a tmp directory in C drive. What is the full path?</em><br><a id='4.1'></a>
>> <strong><code>C:\system\home\tmp</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/6c808ae9-dfca-4deb-8e77-fdd8fc6e7219)

<br>

> 4.2. <em>In the WordWheelQuery search, what was the latest term searched by the user?</em><br><a id='4.2'></a>
>> <strong><code>wipe</code></strong><br>
<p></p>

<p><em></em>Registry Editor</em></p>

![image](https://github.com/user-attachments/assets/b0cadc9c-18f8-4a44-b81d-d0d1953363f0)

<p><em>Registry Explorer</em></p>

![image](https://github.com/user-attachments/assets/ebc04428-b2a5-4628-8372-957fc199eec7)

<br>

> 4.3. <em>Where was the last text file saved by the suspect?</em><br><a id='4.3'></a>
>> <strong><code>C:\system\home\tmp\code.txt</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/9a7cfb81-ade2-4e96-9524-6654351f92c8)

<br>

> 4.4. <em>From the Hacking-tools folder, which suspicious key logging tool was executed 5 times?</em><br><a id='4.4'></a>
>> <strong><code>keylogger.exe</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/073e79b0-d7ae-4aa9-b60e-f5790d89c624)

<br>

> 4.5. <em>Which Disk Wiping utility was executed on this host?</em><br><a id='4.5'></a>
>> <strong><code>DiskWipe.exe</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/f8d4a3cc-64c8-4d0c-8f15-360cd900b47f)


<br>

<h2> Task 5 . Shellbags: Navigating the Past</h2>

<h3 align="left"> Answer the questions below</h3>

> 5.1. <em>What is the IP address of the Network Share, where the user accessed three folders?</em><br><a id='5.1'></a>
>> <strong><code>10.10.17.228</code></strong><br>
<p></p>

<p><em>Shellbags Explorer</em></p>

![image](https://github.com/user-attachments/assets/9cc204f9-a7fa-4d6c-9960-6d3e1e647d37)

<br>

> 5.2. <em>What is the name of the second sub-folder within the Documents folder of the network share that the user accessed?</em><br><a id='5.2'></a>
>> <strong><code>secret-doc</code></strong><br>
<p></p>

<br>

<h2> Task 6 . LNK Files - Shortcut</h2>

<h3 align="left"> Answer the questions below</h3>

> 6.1. <em>What is the document that was last opened by the user on this machine?</em><br><a id='6.1'></a>
>> <strong><code>10_ways_to_Exfiltrate_Data.pdf</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/b879c225-34f4-42eb-b6d9-74f77ef8219a)

<br>

> 6.2. <em>Analyzing the code.lnk file shows that it was accessed from the network shared drive. What is the full path of the network directory?</em><br><a id='6.2'></a>
>> <strong><code>\\10.10.17.228\Users\Administrator\Documents\secret-documentsc</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/dd3b46ec-2eaf-4305-9845-d8e2ae79f75d)

![image](https://github.com/user-attachments/assets/45e99d2c-8ea1-4d52-91bb-3b9431fdd13d)

![image](https://github.com/user-attachments/assets/978e1eaa-4977-4c5c-9585-cf5871806864)




