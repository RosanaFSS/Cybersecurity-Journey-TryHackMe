<h1 align="center">Session Forensics</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/ca8fe3c0-88c9-4e35-8022-9359a3c1749f"><br>
2025, Spetember 2<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>484</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Analyse sessions and tokens for web application investigation</em>.<br>
Access it <a href="https://tryhackme.com/room/voyage"</a>here.<br>
<img width="1200px" src=""></p>



<br>
<h2>Task 1 . Introduction</h2>

<p><em>Answer the question below</em></p>

<p>1.1. I´m ready!<br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 . Recap: Session & JWT</h2>

<p><em>Answer the questions below</em></p>

<p>2.1. Analyse sessions and tokens for web application investigation.<br>
<code>revocation</code></p>

<p>2.2. What is the attack called when an attacker steals your session ID?<br>
<code>session hijacking</code></p>

<br>
<h2>Task 3 . Decoding and Inspecting Tokens</h2>

<p><em>Answer the questions below</em></p>

<p>3.1. Where would you find logs useful for investigating privilege escalation?.<br>
<code>application logs</code></p>

<p>3.2. Where would you find logs useful for mapping user-agent and IP addresses?<br>
<code>web server logs</code></p>

<p>3.3. Which logs would you check if a JWT token has been forged?<br>
<code>identity provider logs</code></p>

<br>
<h2>Task 4 . Session Forensics, Log Investigation</h2>


<p><em>Answer the questions below</em></p>

<p>3.1. What user-agent can be seen in the logs?<br>
<code>Mozilla/5.0</code></p>

<img width="1325" height="74" alt="image" src="https://github.com/user-attachments/assets/7b7d1ed7-7fcb-49f9-beb6-0c918dd5cc9d" />

<br>
<br>
<p>3.2. Based on the logs, what kind of tokens are we dealing with?<br>
<code>JWT</code></p>

<img width="1290" height="167" alt="image" src="https://github.com/user-attachments/assets/261680ec-c749-4b15-8990-e3b9d8d312a3" />

<br>

<img width="523" height="357" alt="image" src="https://github.com/user-attachments/assets/6cd8db92-2055-42dc-b400-a616befa38d1" />

<br>
<br>
<p>3.3. What is the IdP server that issued the tokens?<br>
<code>auth.catportal.internal</code></p>

<img width="1055" height="102" alt="image" src="https://github.com/user-attachments/assets/ebde3d48-1d8a-4dcb-9092-881c14cde6b9" />

<br>
<br>
<p>3.4. Which user has requested the tokens?<br>
<code>FluffyCat</code>

<img width="1055" height="102" alt="image" src="https://github.com/user-attachments/assets/a5392710-caeb-42b0-80dd-199ab7e43cd1" />

<br>

<img width="1279" height="128" alt="image" src="https://github.com/user-attachments/assets/5c1deceb-6411-4917-9220-1965c4f20cf0" />

<br>
<br>
<p>3.5. Which role change triggered the warning?<br>
<code>admin</code>

<img width="1312" height="193" alt="image" src="https://github.com/user-attachments/assets/f63581ce-5c32-442e-8aef-10d37ef89b5b" />

<br>
<br>
<p>3.6. What was the malicious token used?<br>
<code>eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJ1c2VybmFtZSI6IkZsdWZmeUNhdCIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTcyMTQzMTgwMCwiZXhwIjoxNzIxNDM1NDAwfQ</code>

<img width="1339" height="111" alt="image" src="https://github.com/user-attachments/assets/f32e3d2a-ea01-4753-b67c-8dd531ff1fc1" />

<br>

<img width="525" height="375" alt="image" src="https://github.com/user-attachments/assets/22b7e74c-2d2c-484c-9470-9307044352d6" />

<br>

<img width="1328" height="101" alt="image" src="https://github.com/user-attachments/assets/ff61eb05-d0af-4735-b6c2-10e5e91c97c1" />


<br>
<h2>Task 5. </h2>







