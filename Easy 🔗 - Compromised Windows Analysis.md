<p align="center">April 9, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{338}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br></p>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Compromised Windows Analysis}}$$</h1>


<p align="center">"Learn about some key forensic artifacts and solve an interesting case of a compromised Windows workstation." <br>
It is classified as an easy-level walkthrough room, and you can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br> Can be accessed clicking  <a href="https://tryhackme.com/room/compromisedwindowsanalysis">here</a>.</p>

<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/92cac26d-8c7c-41d0-826c-c8aef3fbbcbc"> </p>

<br>
<br>

<h2>Task 1 . Introduction</h2>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 1.1. <em>What is the user's name whose system generated suspicious SSH traffic to a malicious IP?</em><br><a id='1.1'></a>
>> <strong><code>Aashir</code></strong><br>
<p></p>

<br><br>

<h2>Task 2 . Lab Setup</h2>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 2.1. <em>You are good to go!</em><br><a id='2.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br><br>

<h2>Task 3 . Time Explorer for Visualization</h2>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 3.1. <em>Which tool makes it easier to analyze CSV files?</em><br><a id='3.1'></a>
>> <strong><code>Timeline Explorer</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/6d88e970-d12f-4c97-a92d-6c7e414e243c)

<br><br>

<h2>Task 4 . Investigating Persistance</h2>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 4.1. <em>What is the name of the scheduled task created by the attacker?</em><br><a id='4.1'></a>
>> <strong><code>CnC</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/76886ba4-09c9-4973-b2a7-47e02dc1b15a)

<br>

![image](https://github.com/user-attachments/assets/c82d2364-bd0a-47e3-a053-6e5f793f1a4f)

<br>

![image](https://github.com/user-attachments/assets/950f58e3-e217-4a45-9d06-25285f7bc2a3)

<br>


> 4.2. <em>What is the IP of the malicious server to which SSH requests are made?</em><br><a id='4.2'></a>
>> <strong><code>101.55.125.10</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/099ce87c-0b6e-4b21-8c6b-bffd27396758)

<br>

![image](https://github.com/user-attachments/assets/71d59ed7-c221-4c16-bfd7-67c0591e42de)

<br><br>



<h2>Task 5 . Investigating Recently Accessed Files</h2>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 5.1. <em>What is the name of the RAR file created during the attack?</em><br><a id='5.1'></a>
>> <strong><code>Cursed.rar</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/4d816c4c-9705-46a4-91c7-67b84971be02)

<br>

> 5.2. <em>When was the RAR file created in the system? Format YYYY-MM-DD HH:MM:SS</em><br><a id='5.2'></a>
>> <strong><code>2025-03-29 10:26:07</code></strong><br>
<p></p>

<br>

```bash
C:\Users\Administrator\Desktop\Forensics Tools\LECmd>.\LECmd.exe -d C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Recent --csvf Parsed-LNK.csv --csv C:\Users\Administrator\Desktop
LECmd version 1.5.0.0

Author: Eric Zimmerman (saericzimmerman@gmail.com)
https://github.com/EricZimmerman/LECmd

Command line: -d C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Recent --csvf Parsed-LNK.csv --csv C:\Users\Administrator\Desktop

Looking for lnk files in C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Recent

Found 4 files

Processing C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Recent\Amazon Ec2 Launch - Instance Initialization.lnk

```

<br><br>

![image](https://github.com/user-attachments/assets/821b420c-0ec0-4a27-ac53-53696018b9ef)

<br>

![image](https://github.com/user-attachments/assets/187310bf-5369-4ec1-a423-660dd80d06f1)

<br>


<h2>Task 6 . Investigating File Execution</h2>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 6.1. <em>What is the name of the malicious executable file?</em><br><a id='6.1'></a>
>> <strong><code>Cursed.rar</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/736b8ca8-2829-4038-83fb-59babc3593d9)

<br>

![image](https://github.com/user-attachments/assets/4af9c739-468d-4845-bd86-4322bdbc4cae)


<br>

> 6.2. <em>How many times was this file executed?</em><br><a id='6.2'></a>
>> <strong><code>C2</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/9e4af17d-9f21-4fe6-b449-c2d111f90a05)


<br>

> 6.3. <em>When was the last time that this file was executed? Format YYYY-MM-DD HH:MM:SS</em><br><a id='6.3'></a>
>> <strong><code>2025-03-29 10:29:12</code></strong><br>
<p></p>

<br>


![image](https://github.com/user-attachments/assets/9384cd5f-dd11-4299-b6aa-00de493ec9b5)

<br>


<h2>Task 7 . The Dig of Executable</h2>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 7.1. <em>What is the full path of the malicious file?</em><br><a id='7.1'></a>
>> <strong><code>c:\users\administrator\desktop\cursed\cipher.exe</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/ef2c3a55-0fed-4fce-aced-f7c23080d6a1)

<br>

> 7.2. <em>What is the SHA1 hash of this file?</em><br><a id='7.2'></a>
>> <strong><code>5b15c9d9ef36cae9f24ce63eebd190ac381bb734</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/b5719313-4220-4ce6-bf3c-26fa0d087553)

<br>


<h2>Task 8 . Windows Event Log Analysis</h2>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 8.1. <em>When was Defender disabled? Answer in 12 hour clock format. e.g. hours:minutes:seconds AM/PM</em><br><a id='8.1'></a>
>> <strong><code>10:25:14 AM</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/4d1cca40-8018-4168-8d07-027488706faf)


<br>

<br>

> 8.2. <em>What is the IP address of the attacker's system?</em><br><a id='8.2'></a>
>> <strong><code>10.11.90.211</code></strong><br>
<p></p>



<br>

![image](https://github.com/user-attachments/assets/7ad31548-b1ea-4771-8857-8c552163fcbd)

<br>

<h2>Task 9 . Chronological Order of Attack</h2>

<br>

![image](https://github.com/user-attachments/assets/a5098265-8815-47b1-8e59-7c5266ff31f9)

<br>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 9.1. <em>Complete the room!</em><br><a id='9.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

<br><br>

<br>
<br>


<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center"><img width="900px" src="https://github.com/user-attachments/assets/9f7aa2cc-899c-4c4c-ab77-7f9a86d8de77">
<br><img width="900px" src="https://github.com/user-attachments/assets/f6321872-5caf-4976-9ac6-3a589a700e61"></p>

<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>


<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |Global        | Brazil       | Global      | Brazil     |          | Completed |           |
| April 9, 2025     | 338      |     297ᵗʰ    |        8ᵗʰ   |    272ⁿᵈ    |     2ⁿᵈ    |  92,142  |       651 |   59      |

</div>

<br>

<p align="center">Bronze League 7ᵗʰ<br><br><img width="300px" src="https://github.com/user-attachments/assets/16033216-661b-4505-9b89-d15d4176cee4"> </p>

<br>

<p align="center"> Global All Time: 297ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/a6f4ecb1-2159-43da-8951-80fc12a113d6"> </p>

<p align="center"> Brazil All Time: 8ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/b8af675b-c7b8-4b59-87e9-d49b8fbb989d"> </p>

<p align="center"> Global monthly: 272ⁿᵈ<br><br><img width="900px" src="https://github.com/user-attachments/assets/e7629a3f-197f-413e-a072-636c0ec9bd955"> </p>

<p align="center"> Brazil monthly: 2ⁿᵈ<br><br><img width="900px" src="https://github.com/user-attachments/assets/87dd5dec-7e70-463e-84f2-b0f718672f00"> </p>


<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/tryhackme">tryhackme</a>, <a href="https://tryhackme.com/p/aashirmasood">aashirmasood</a> and  <a href="https://tryhackme.com/p/Aashir.Masood">Aashir.Masood</a> for investing your time and effort to develop this walkthrough so that I could sharpen my skills!</p> 
