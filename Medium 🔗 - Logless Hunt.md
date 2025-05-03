<p align="center">May 3, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{362}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/93512cf9-8443-4639-8359-18137e0dd1c3"><br></p>


<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Logless Hunt}}$$</h1>
<p align="center">Detect every attack step on a Windows machine even after threat actors cleared Security logs.<br>
It is classified a medium-level walkthrough, , and you can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed. Can be accessed clicking <a href="https://tryhackme.com/room/loglesshunt">here</a>.</p>


<p align="center"> <img width="900px" src=""> </p>

<br>

<h2>Task 1 . Introduction</h2>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> 1.1. <em>Let´s begin</em>.<a id='1.1'></a>
>> <code><strong>No answer needed</strong></code><br><br>

<br>
<br>

<h2>Task 2 . Scenario</h2>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> 2.1. <em>After launching the VM, open Event Viewer. What is the earliest Event ID you see in the Security logs?</em>.<a id='2.1'></a>
>> <code><strong>1102</strong></code><br><br>


<br>

![image](https://github.com/user-attachments/assets/1d4c3a1d-b556-49ba-afd1-4dcc399a0756)


<br>

![image](https://github.com/user-attachments/assets/92013c6e-76b4-4931-96ca-99078596e692)

<br>

![image](https://github.com/user-attachments/assets/8a3a7056-d54c-4540-b883-ce05d38db537)


<br>
<br>



<h2>Task 3 . Scenario</h2>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 3.1. <em>What is the title of the HR01-SRV web app hosted on 80 port?</em>.<a id='3.1'></a>
>> <code><strong>Salary Raise Approver v0.1</strong></code><br><br>


<br>

![image](https://github.com/user-attachments/assets/8911d2e4-bac0-4528-afd1-9a56f54fdfd4)


<br>

> 3.2. <em>Which IP performed an extensive web scan on the HR01-SRV web app?</em>.<a id='3.2'></a>
>> <code><strong>10.10.23.190</strong></code><br><br>


<br>

![image](https://github.com/user-attachments/assets/a7fade1d-c0a1-4d97-9605-057ad3a5bd5f)



<br>

> 3.3. <em>What is the absolute path to the file that the suspicious IP uploaded?</em>.<a id='3.3'></a>
>> <code><strong>C:\Apache24\htdocs\uploads\search.php</strong></code><br><br>

<br>

![image](https://github.com/user-attachments/assets/afdd8fb6-1fed-43a3-9119-ae939c23108e)

<br>

> 3.4. <em>Clearly, that's suspicious! What would you call the uploaded malware / backdoor?</em> Hint : <em>Note how the file is then repeatedly used by the attacker to achieve code execution.</em><br><a id='3.3'></a>
>> <code><strong>Web Shell</code><br><br>

<br>

![image](https://github.com/user-attachments/assets/414d7bdd-2e0d-442f-b62d-5c59776599c2)

<br>
<br>



<h2>Task 4 . From Web to RDP | PowerShell Logs</h2>

<h2>Task 5 . Breached Admin | RDP Session Logs</h2>

<h2>Task 6 . Persistance Traces | Scheduled Tools</h2>

<h2>Task 7 . Credentials Access | Windows Defender</h2>

<h2>Task 8 . Conclusion</h2>


