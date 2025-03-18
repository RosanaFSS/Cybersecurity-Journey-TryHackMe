<p align="center">December 2, 2024</p>
<p align="center">Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{210}}$$-day-streak in  <a href="https://tryhackme.com/r/p/Rosana">TryHackMe</a>.</p>

<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{Windows User Account Forensics}}$$
</h1>
<p align="center">Learn where to search for artefacts associated with users and accounts.</p>
<p align="center">Access this TryHackMe Room clicking <a href="https://tryhackme.com/r/room/windowsuseraccountforensics">Windows User Account Forensics</a>. Note that only subscribers can deploy virtual machines in this room.</p><br>
<p align="center">
  <img height="150px" hspace="20" src="https://github.com/user-attachments/assets/3773d729-f20d-4e8b-8c6f-fbd982d22bed">
  <img height="150px" src="https://github.com/user-attachments/assets/fa4c8493-b891-4974-b82d-8417129a9e05">
</p>


<br>
<h2>Task 1. Introduction<a id='1'></a></h2>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> 1.1. <em>I have started the machine!</em>.<a id='1.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>
<h2>Task 2. Windows Account Types<a id='2'></a></h2>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 2.1. <em>What type of accounts are used by the Windows operating system and various apps?</em>.<a id='2.1'></a>
>> <code><strong>System and Service Accounts</strong></code>

<br>

> 2.2. <em>What centrally manages local user accounts and domain accounts?</em>.<a id='2.2'></a>
>> <code><strong>Domain Controller</strong></code>

<br>
<h2>Task 3. Account Lifecycle Artifacts<a id='3'></a></h2>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 3.1. <em>How many users were found using the DSInternals command?</em>.<a id='3.1'></a>
>> <code><strong>5</strong></code>

<br>

> 3.2. <em>What is the value of the "bootKey" variable?</em>.<a id='3.2'></a>
>> <code><strong>36c8d26ec0df8b23ce63bcefa6e2d821</strong></code>

<br>

> 3.3. <em>What is the SID of the domain user, m.ascot?</em>.<a id='3.3'></a>
>> <code><strong>S-1-5-21-1966530601-3185510712-10604624-1111</strong></code>

<br>

![image](https://github.com/user-attachments/assets/9097704f-20db-40d5-b891-6e315d6f7452)

<br>

![image](https://github.com/user-attachments/assets/c4afb3a0-b4e2-4f05-a63f-880f94c40d7c)

<br>
<p>There are 5 different <code></code>DistinguishedName</code></p>
![image](https://github.com/user-attachments/assets/e03caf18-b910-4584-8a20-9e77483c1ac5)

<br>

![image](https://github.com/user-attachments/assets/68462d0d-bded-4147-9965-cee72ef8d973)

<p>I also tested the following command line, and got user´s SID.</p>

![image](https://github.com/user-attachments/assets/a9456312-2581-4ab0-8427-4ca06de2517e)


<br>
<h2>Task 4. Account Authentication Artefacts<a id='4'></a></h2>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 4.1. <em>What is the user name used for the NTLM authentication?</em>.<a id='4.1'></a>
>> <code><strong>admin</strong></code>

<br>

> 4.2. <em>What was the Server Challenge sent to the client during the Challenge stage of the NTLM handshake?</em>.<a id='4.2'></a>
>> <code><strong>____________________</strong></code>

<br>

> 4.3. <em>What is the Dns Name of the other result from the the DsGetDomainControllerInfo response?</em>.<a id='4.3'></a>
>> <code><strong>____________________</strong></code>

<br>

![image](https://github.com/user-attachments/assets/cb2e69f7-3471-46f9-9cc2-2c96cefcd3e1)

<br>

![image](https://github.com/user-attachments/assets/2498dff8-0715-48ba-b3c2-6da525cf2ee2)

<br>

![image](https://github.com/user-attachments/assets/274771e1-ddb6-404d-9df7-df9795c5b98b)

<br>

![image](https://github.com/user-attachments/assets/a5c34047-d189-47f5-83da-749a146383a0)

<br>

![image](https://github.com/user-attachments/assets/3620d3a3-b732-4970-9fc8-3aaaf6817967)


<br>

![December 2, 2024  - TryHackMe - Windows User Account Forensics - Room Complete 2](https://github.com/user-attachments/assets/341cd4f9-3409-4b02-9492-17de2ca33fc8)




















