<h1 align="center">Session Forensics</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/ca8fe3c0-88c9-4e35-8022-9359a3c1749f"><br>
2025, Spetember 2<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>484</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Analyse sessions and tokens for web application investigation</em>.<br>
Access it <a href="https://tryhackme.com/room/sessionforensics">here</a><br>
<img width="1200px" src="https://github.com/user-attachments/assets/ecfcf137-e005-4c13-822e-f71dc3956ba0"></p>



<br>
<h2>Task 1 . Introduction</h2>
<p>In this room, we'll dive into different session types and how to investigate several log types at the application level to identify compromise.</p>

<h3>Learning Prerequisites</h3>
<p>

- <a href="https://tryhackme.com/room/jwtsecurity">JWT Security</a><br>
- <a href="hhttps://tryhackme.com/room/sessionmanagement">Session Management</a></p>


<h3>Learning Objectives</h3>
<p>

- Understand log types to perform application-level forensics<br>
- Identify key behaviours that lead to session compromise<br>
- Build alerting and detection capabilities tailored to application-level logs</p>

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
<br>

<img width="525" height="375" alt="image" src="https://github.com/user-attachments/assets/22b7e74c-2d2c-484c-9470-9307044352d6" />

<br>
<br>

<img width="1328" height="101" alt="image" src="https://github.com/user-attachments/assets/ff61eb05-d0af-4735-b6c2-10e5e91c97c1" />

<br>
<br>
<p>3.7. What algorithm did the malicious token use?<br>
<code>none</code></p>


<br>
<br>
<p>3.8. What was the previous legitimate token?<br>
<code>eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IkZsdWZmeUNhdCIsInJvbGUiOiJ1c2VyIiwiZXhwIjoxNzIxNDM1NDAwfQ.WMKctz1p5KLwNP_C7XXcWbP8uEpbwSeEY_hU_dhG6Rk</code></p>

<img width="1322" height="229" alt="image" src="https://github.com/user-attachments/assets/974275ab-551d-4fbb-8f05-e81805edef88" />

<br>
<br>
<p>3.9. What algorithm did the legitimate token use?<br>
<code>HS256</code></p>

<img width="539" height="360" alt="image" src="https://github.com/user-attachments/assets/5b0f493a-709b-4930-a7b6-5c3972061e70" />

<br>
<br>
<h2>Task 5. </h2>


<p><em>Answer the question below</em></p>

<p>5.1. Where would you find logs useful for investigating privilege escalation?.<br>
<code>Token Verification</code></p>

<img width="687" height="142" alt="image" src="https://github.com/user-attachments/assets/3aa6ae8c-ff63-4785-91ca-d5154bbc1063" />


<br>
<br>
<h2>Task 6 . Conclusion</h2>
<h3>Conclusion</h3>
<p>In this lab, you learned how to decode and inspect JWTs, identify tampered tokens, and trace malicious activity through layered logs using a real-world scenario involving FluffyCat. Forged tokens can bypass weak validation, and role escalation might slip by if proper checks aren’t in place. Thanks to your AppSec knowledge, you saw how linking activity across web, app, and IdP logs can build a timeline and uncover the root cause. Thinking like a forensic analyst during a session hijack or token forgery incident is very powerful, and the collaboration of skills between AppSec and SecOps can be really powerful. </p>

<p><em>Answer the question below</em></p>

<p>6.1. I´m ready for the next room!<br>
<code>No answer needed</code></p>

<img width="1896" height="897" alt="image" src="https://github.com/user-attachments/assets/4129980c-b1c2-4e31-a881-f3e4ec94a08f" />

<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/dcfff541-0417-4e14-82bd-25e628c434d7"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/4129980c-b1c2-4e31-a881-f3e4ec94a08f"></p>


<br>
<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, September 1 | 483      |     111ˢᵗ    |      5ᵗʰ     |     849ᵗʰ   |    15ᵗʰ    | 123,636  |    937    |    73     |

</div>


<p align="center">Global All Time:   111ˢᵗ<br><img width="250px" src="https://github.com/user-attachments/assets/87d4d449-43d0-42d9-b8a5-1ad6e6672963"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/a871adaa-f233-4df4-a6f0-43b060277aa9"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/d540e5de-8a3a-47f4-bfae-0b99755bbb0f"><br>
                  Global monthly:    849ʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/95a24424-5106-404f-9643-b555a1705957"><br>
                  Brazil monthly:     15ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/d7d7d0a3-6733-4eff-9422-2469b316a6fc"><br>

<br>
<br>

<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>

