<h1 align="center">OWASP Top 10 2025: IAAA Failures</h1>
<p align="center">2025, November 18  &nbsp; .  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure on my <code>1</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>Learn about A01, A07, and A09 in how they related to failures in the applied IAAA model. &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/owasptopten2025one">here</a>.<br><br><img width="1200px" src="https://github.com/user-attachments/assets/7a11cb25-6345-443b-ab5f-3c1bb4e6cafc"></p>

<h2>Task 1 . Introduction</h2>
<p>This room breaks down 3 of the OWASP Top 10 2025 categories. In this room, you will learn about the categories that are related to failures in how Identity, Authentication, Authorisation, and Accountability (IAAA) is implemented in the application. You will put the theory into practice by completing supporting challenges. The following categories are covered in this room:<br>

- A01: Broken Access Control<br>
- A07: Authentication Failures<br>
- A09: Logging & Alerting Failures<br>

The room has been designed for beginners and assumes no previous security knowledge.</p>

<p><em>Answer the question below</em></p>

<p>1.1. <em>I am ready to learn about IAAA failures!</em><br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 . What is IAAA</h2>
<p>IAAA is a simple way to think about how users and their actions are verified on applications. Each item plays a crucial role and it isn't possible to skip a level. That means, if a previous item isn't being performed, you cannot perform the later itmes. The four items are:<br>

- <strong>Identity</strong> - the unique account (e.g., user ID/email) that represents a person or service.<br>
- <strong>Authentication</strong> - proving that identity (passwords, OTP, passkeys).
- <strong>Authorisation</strong> - what that identity is allowed to do.
- <strong>Accountability</strong> - recording and alerting on who did what, when, and from where.<br>

The three categories of OWASP Top 10:2025 discussed in this room relates to failures in how IAAA was implemented. Weaknesses here can be incredibly detrimental, as it can allow threat actors to either access the data of other users or gain more privileges than they are suppose to have.<br>

If you want a deeper dive on IAAA first, work through <a href="https://tryhackme.com/room/iaaaidm">this room</a>.</p>

<p><em>Answer the question below</em></p>

<p>2.1. <em>What does IAAA stand for?</em><br>
<code>Identity, Authentication, Authorisation, Accountability</code></p>

<br>
<h2>Task 3 . A01: Broken Access Controle</h2>
<p>Broken Access Control happens when the server doesn’t properly enforce <strong></strong>who can access what</strong> on every request. A common occurence of this is IDOR (Insecure Direct Object Reference): if changing an ID (like <code></code>?id=7</code> → <code></code>?id=6</code>) lets you see or edit someone else’s data, access control is broken.<br>

In practice this shows up as horizontal privilege escalation (same role, other user’s stuff) or vertical privilege escalation (jumping to admin-only actions) because the application trusts the client too much.<br>

Start the static site attached to this task and play with the <code>accountID</code> value in the URL. So if you can identify which user has more than $ 1 million in their account!

If you want a deeper dive or more variations on the theme (encoded IDs, hashed IDs, etc.), work through these rooms afterwards:

- <a href="https://tryhackme.com/room/owaspbrokenaccesscontrol">Broken Access Control</a><br>
- <a href="https://tryhackme.com/room/idor">Insecure Direct Object References</a></p>

<p><em>Answer the questions below</em></p>

<p>3.1. <em>If you don't get access to more roles but can view the data of another users, what type of privilege escalation is this?</em><br>
<code>Horizontal</code></p>

<p>3.2. <em>What is the note you found when viewing the user's account who had more than $ 1 million?</em><br>
<code>THM{••••••••••••••••••••••}</code></p>

<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/31770db2-1596-4588-ba17-6db8105baf50"><br><img width="700px" src="https://github.com/user-attachments/assets/75d7a07e-45f7-49d4-b2e5-8fce6e073cad"></h6>

<br>
<h2>Task 4 . A07: Authentication Failures</h2>
<p>Authentication Failures happen when an application can’t reliably verify or bind a user’s identity. Common issues include:<br>

- username enumeration<br>
- weak/guessable passwords (no lockout/rate limits)<br>
- logic flaws in the login/registration flow<br>
- insecure session or cookie handling<br>

If any of these are present, an attacker can often log in as someone else or bind a session to the wrong account.<br>

Let's try to break into the <code>admin</code> user's account. We know that their username is <code>admin</code>, so let's try to fool the application by registering a user with the name of <code>aDmiN</code>. Start the static site attached to this task. register your account and log into the admin user's account to get your next flag!<br>

If you want more depth or broader techniques (e.g., brute force, session handling, cookies/JWT/OAuth, and MFA specifics), work through these after this room:<br>

- <a href="https://tryhackme.com/room/authenticationbypass">Authentication Bypass Room</a><br>
- <a href="https://tryhackme.com/room/multifactorauthentications">Multi-Factor Authentication</a><br>
- <a href="https://tryhackme.com/module/authentication">Authentication Module</a><br>

<p><em>Answer the question below</em></p>

<p>4.1. <em>What is the flag on the <code>admin</code> user's dashboard?</em><br>
<code>THM{••••••••••••••••••••••}</code></p>

<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/20094549-124c-4ab1-8fbb-aeb6f337927b"><br><img width="700px" src="https://github.com/user-attachments/assets/13adeb89-f9de-4482-ab6b-660f4daaf1d1"><br><img width="700px" src="https://github.com/user-attachments/assets/feecd2aa-6830-4cb8-8c15-c38e36b5d3d9"></h6>

<br>
<h2>Task 5 . A09: Logging & Alerting Failures</h2>
<p>When applications don’t record or alert on security-relevant events, defenders can’t detect or investigate attacks. Good logging underpins accountability (being able to prove who did what, when, and from where). In practice, failures look like missing authentication events, vague error logs, no alerting on brute-force or privilege changes, short retention, or logs stored where attackers can tamper with them.<br>

Let's take a look at what is required to perform an investigation of a application under attack. Start the static site attached to this task, perform your investigation, and answer the questions below. Then, think about how hard it would be to understand what happened during this attack if key pieces of this log information as missing.<br> 

If you want a deeper dive into logging for accountability, take a look at <a href="https://tryhackme.com/room/loggingforaccountability">this room</a>.</p>

<p><em>Answer the questions below</em></p>

<p align="left">5.1. <em>It looks like an attacker tried to perform a brute-force attack, what is the IP of the attacker?</em><br>
<code>203.0.113.45</code></p>

<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/92f796d3-9657-4081-bcee-4b3cba014f83"><br><img width="700px" src="https://github.com/user-attachments/assets/b95c85b4-c479-47af-9589-b28cc2ba92ed"></h6>

<br>
<p align="left">5.2. <em>Looks like they were able to gain access to an account! What is the username associated with that account?</em><br>
<code>admin</code></p>

<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/fbbe81b9-e5a9-454f-b8f7-4e8dba7a12e4"></h6>

<br>
<p>5.3. <em>What action did the attacker try to do with the account? List the endpoint the accessed.</em><br>
<code>/supersecretadminstuff</code></p>

<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/2f28ff07-4db2-4e74-bade-4c285e49cfce"><br>
                   <img width="700px" src="https://github.com/user-attachments/assets/bcf7d1cb-9397-4c7a-ae08-28254f8bc2cf"></h6>

<br>
<h2>Task 6 . Conclusion</h2>

<p>You’ve just worked through the essentials of Identity, Authentication, Authorisation, and Accountability in web applications and how it can cause several of the categories of vulnerabilities discussed in OWASP Top 10:2025. The big ideas to keep:<br>

- <strong>A01 Broken Access Control</strong>: Enforce server-side checks on every request
- <strong>A07 Authentication Failures</strong>: Enforce unique indexes on the canonical form, rate-limit/lock out brute force, and rotate sessions on password/privilege changes.
- <strong>A09 Logging & Alerting Failures</strong>: Log the full auth lifecycle (fail/success, password/2FA/role changes, admin actions), centralise logs off-host with retention, and alert on anomalies (e.g., brute-force bursts, privilege elevation).<br>

Continue the journey with <strong>Room 2 in this module</strong>: <a href="https://tryhackme.com/jr/owasptopten2025two">Application Design Flaws</a>.</p>

<p><em>Answer the question below</em></p>

<p>6.1. <em>I understand the importance of a secure IAAA implementation in my application!</em><br>
<code>No answer needed</code></p>

<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/37e87214-b02e-48bf-853e-3978a3a76991"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/14bbc945-4d73-4377-984e-8df95425cf92"></p>


<h1 align="center">My TryHackMe Journey ・ 2025, November</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|18      |Easy 🔗 - OWASP Top 10 2025: IAAA Failures| 1   |      93ʳᵈ    |     3ʳᵈ    |     971ˢᵗ   |      8ᵗʰ     |    132,151  |    1,022    |    80     |
|14      |Hard 🚩 - Shock and Silence            |   1    |      94ᵗʰ    |     4ᵗʰ    |     749ᵗʰ   |      7ᵗʰ     |    133,095  |    1,021    |    80     |
|14      |Easy 🔗 - Input Manipulation & Prompt Injection| 1 |   95ᵗʰ    |     4ᵗʰ    |   1,290ᵗʰ   |     12ⁿᵈ     |    132,822  |    1,020    |    80     |
|14      |Hard 🚩 - CRM Snatch                   |   1    |      95ᵗʰ    |     4ᵗʰ    |   1,526ᵗʰ   |     12ⁿᵈ     |          -  |    1,019    |    80     |
|8       |Easy 🔗 - Living of the Land Attacks   |   1    |      91ˢᵗ    |     4ᵗʰ    |   1,759ᵗʰ   |     17ᵗʰ     |    132,642  |    1,018    |    80     |
|8       |Hard 🚩 - Lost in RAMslation           |   1    |      91ˢᵗ    |     4ᵗʰ    |   2,547ᵗʰ   |     25ᵗʰ     |    132,580  |    1,017    |    80     |
|8       |Easy 🔗 - MITRE                        |   1    |       -      |     4ᵗʰ    |      -      |      -       |          -  |       -     |    80     |

</h6></div><br>

<p align="center">Global All Time:     93ʳᵈ<br><img width="250px" src="https://github.com/user-attachments/assets/f21b7df7-8f11-4cb4-9c6d-2a1e578a366f"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/0ae19a6e-f5d6-4ad9-8bde-d53d33df5d7f"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/dbf4fde7-3fc2-4beb-b9ed-ec09ed68a3ec"><br><br>
                  Global monthly:     971ˢᵗ<br><img width="1200px" src="https://github.com/user-attachments/assets/f89e083e-5bb2-4b76-b9f0-c6364a32df12"><br><br>
                  Brazil monthly:       8ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/1340de07-ea3d-4912-86bb-f54bb2413dd8"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
