<h1 align="center">Linux Logging for SOC</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/88f79fae-a313-469e-a79d-10032cfb6165"><br>
2025, September 17<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>499</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Explore key Linux log sources and learn how to use them in your SOC triage</em>.<br>
Access it <a href="https://tryhackme.com/room/linuxloggingforsoc">here</a>.<br>
<img width="1200px" src=""></p>


<h2>Task 1 . Introduction</h2>

<p>Linux has long been a leader in servers and embedded systems, and now its use is even more widespread with the growth of cloud adoption. As a SOC analyst, you are now very likely to investigate Linux alerts and incidents, either from traditional on-premises servers or from cloud-native containerized workloads. In this room, you will explore the most common Linux logs sent to SIEM and learn how to view them directly on-host.</p>
<br>

<p><em>Answer the question below</em></p>

<p>1.1.Let´s start!<br>
<code>No answer needed</code></p>

<h2>Task 2 . Working With Text Logs</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>2.1. Use the /var/log/syslog file on the VM to answer the questions.
Which time server domain did the VM contact to sync its time?<br>
<code>ntp.ubuntu.com</code></p>

<img width="1237" height="114" alt="image" src="https://github.com/user-attachments/assets/e70d92ef-0d4d-4e91-a5b9-d92c431e3cca" />

<p>2.2. What is the kernel message from Yama in /var/log/syslog?<br>
<code>Becoming mindful.</code></p>

<img width="989" height="93" alt="image" src="https://github.com/user-attachments/assets/49b99887-cdcb-4f63-bbd5-9f0ed2b39e0c" />


<br>
<h2>Task 3 . Authentication Logs</h2>
<h3>Authentication Logs</h3>




<h3>Login and Logout Events</h3>



<h3>Miscellaneous Events</h3>


<p><em>Answer the questions below</em></p>

<p>3.1.Continue with the VM and use the /var/log/auth.log file. Which IP address failed to log in on multiple users via SSH?<br>
<code>10.14.94.82</code></p>

<img width="1352" height="628" alt="image" src="https://github.com/user-attachments/assets/94443bba-6669-4295-a070-f2e437b73714" />


<br>
<br>


<img width="1260" height="139" alt="image" src="https://github.com/user-attachments/assets/ab70b6cd-2c51-4d7e-b760-7a341d7c6ba7" />


<p>3.2. Which user was created and added to the "sudo" group?<br>
<code>xerxes</code></p>

<img width="1345" height="110" alt="image" src="https://github.com/user-attachments/assets/e90c4451-1d1c-4a1d-b35a-6e68fac54fd4" />

<br>
<h2>Task 4 . Common Linux Logs</h2>
<h3>Generic System Logs</h3>



<h3>App-Specific Logs</h3>


<h3>Bash History</h3>



<p><em>Answer the questions below</em></p>

<p>4.1. According to the VM's package manager logs, which version of unzip was installed on the system?<br>
<code>6.0-28ubuntu4.1</code></p>

<img width="1248" height="67" alt="image" src="https://github.com/user-attachments/assets/00981137-8624-4395-af41-c3c337f2f66d" />


<p>4.2. What is the flag you see in one of the users' bash history?<br>
<code>THM{****************}</code></p>

<img width="1360" height="825" alt="image" src="https://github.com/user-attachments/assets/7e40702c-df51-4bc5-bd9b-317f92863fa4" />

<br>
<h2>Task 5 . Runtime Monitoring</h2>
<h3>Runtime Monitoring</h3>



<h3>System Calls</h3>


<p><em>Answer the questions below</em></p>

<p>5.1. Which Linux system call is commonly used to execute a program?<br>
<code>execve</code></p>

<p>5.2. Can a typical program open a file or create a process bypassing system calls? (Yea/Nay)<br>
<code>Nay</code></p>

<br>
<h2>Task 6 . Using Auditd</h2>
<h3>Audit Daemon</h3>


<h3>Using Auditd</h3>




<p>6.1. When was the secret.thm file opened for the first time? (MM/DD/YY HH:MM:SS). Note: Access to this file is logged with the "file_thmsecret" key.<br>
<code>naabu_2.3.5_linux_amd64.zip</code></p>

<img width="1350" height="155" alt="image" src="https://github.com/user-attachments/assets/8fd5566c-a1c5-412b-b0e7-18e0334cfd1f" />

<p>6.2. What is the original file name downloaded from GitHub via wget?Note: Wget process creation is logged with the "proc_wget" key.<br>
<code>naabu_2.3.5_linux_amd64.zip</code></p>

<img width="1350" height="508" alt="image" src="https://github.com/user-attachments/assets/973ffa60-dadd-413f-be3d-8cccf5cce91c" />

<p>6.3.Which network range was scanned using the downloaded tool? Note: There is no dedicated key for this event, but it's still in auditd logs.<br>
<code>naabu_2.3.5_linux_amd64.zip</code></p>


```bash
user@tryhackme:~$ python3 -m http.server 8000
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
MACHINE_IP - - [06/Jul/2025 20:14:05] "GET /script.js HTTP/1.1" 200 -
```

