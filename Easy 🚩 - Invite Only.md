<h1 align="center">Invite Only</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/888cff96-ae5f-4b99-8cfd-1b38f84648a3"><br>
2025, September 12<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>494</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Extract insight from a set of flagged artefacts, and distil the information into usable threat intelligence</em>.<br>
Access it <a href="https://tryhackme.com/room/invite-only"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/b2c7a3a9-3cf3-489c-ae71-940926f1ca83"></p>

<h2>Task 1 . Invite Only</h2>
<p>You are an SOC analyst on the SOC team at Managed Server Provider TrySecureMe. Today, you are supporting an L3 analyst in investigating flagged IPs, hashes, URLs, or domains as part of IR activities. One of the L1 analysts flagged two suspicious findings early in the morning and escalated them. Your task is to analyse these findings further and distil the information into usable threat intelligence.<br>

Flagged IP: <strong>xxx[.]xx[.]xx[.]xxx </strong><br>
Flagged SHA256 hash:  <strong>5d0509f68a9b7c415a726be75a078180e3f02e59866f193b0a99eee8e39c874f </strong><br>

We recently purchased a new threat intelligence search application called TryDetectThis2.0. You can use this application to gather information on the indicators above.

<h3>Connecting To The Machine</h3>
<p>Just start the Virtual Machine by clicking “ <strong>Start Virtual Machine </strong>.” Once the VM is booted up, double-click the launcher on the desktop to start the TryDetectThis2.0 application.</p>

<h3>Virtual environement</h3>
<p></p><p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting the Target Machine, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.<br>
<p>[ Start Machine ]</p>

<p><em>Answer the questions below</em></p>

<p>1.1. What is the name of the file identified with the flagged SHA256 hash?<br>
<code>syshelpers.exe</code></p>

<img width="1348" height="470" alt="image" src="https://github.com/user-attachments/assets/92b70128-800c-40ca-8ae9-12ccf3ff1e22" />

<br>
<br>

<img width="1015" height="428" alt="image" src="https://github.com/user-attachments/assets/f508fea9-b781-4dba-9cbc-7c715a1b5bb7" />

<br>
<br>
<p>1.2. What is the file type associated with the flagged SHA256 hash?<br>
<code>WIN32 EXE</code></p>

<img width="1659" height="695" alt="image" src="https://github.com/user-attachments/assets/0a2e82f2-6284-4d31-8912-8ffe8680c44e" />

<br>
<br>

<img width="1015" height="428" alt="image" src="https://github.com/user-attachments/assets/f508fea9-b781-4dba-9cbc-7c715a1b5bb7" />

<br>
<br>
<p>1.3. What are the execution parents of the flagged hash? List the names chronologically, using a comma as a separator. Note down the hashes for later use.<br>
<code>361GJX7J,installer.exe</code></p>

<img width="824" height="177" alt="image" src="https://github.com/user-attachments/assets/417e2ff3-5bf3-453c-9f00-2a949e0355cb" />

<br>
<br>

<img width="1157" height="147" alt="image" src="https://github.com/user-attachments/assets/f4803584-d872-4f65-bf29-ac63220b8c9c" />

<br>
<br>
<p>1.4. What is the name of the file being dropped? Note down the hash value for later use.<br>
<code>Aclient.exe</code></p>

<img width="385" height="120" alt="image" src="https://github.com/user-attachments/assets/6927f831-8f49-48e2-89af-8290eecf0c5e" />

<br>
<br>

<img width="1174" height="109" alt="image" src="https://github.com/user-attachments/assets/cce517b5-40cf-4b5c-86b0-8f4dcfb0534b" />

<br>
<br>
<p>1.5. From the second hash in question 3, list the four detected dropped files in chronological order, separated by commas.<br>
<code>searchhost.exe,syshelpers.exe,nat.vbs,runsys.vbs</code></p>

<p>

- fa102d4e3cfbe85f5189da70a52c1d266925f3efd122091cdc8fe0fc39033942</p>

<img width="1270" height="471" alt="image" src="https://github.com/user-attachments/assets/08d6c337-c98a-46e0-a25c-055771a88380" />

<br>
<br>
<p>1.6. Analyse the files related to the flagged IP. What is the malware family that links these files?<br>
<code>WIN32 EXE</code></p>

<img width="806" height="390" alt="image" src="https://github.com/user-attachments/assets/2bce324a-004d-4d7b-b50e-86b7a43691ea" />

<br>
<br>
<p>1.7. What is the title of the original report where these flagged indicators are mentioned? Use Google to find the report.<br>
<code>From Trust to Threat: Hijacked Discord Invites Used for Multi-Stage Malware Delivery</code></p>

<p>

- https://research.checkpoint.com/2025/from-trust-to-threat-hijacked-discord-invites-used-for-multi-stage-malware-delivery</p>

<img width="835" height="578" alt="image" src="https://github.com/user-attachments/assets/01a448cb-946c-4072-ad96-5abdee2353e4" />


<br>
<br>
<p>1.8. Which tool did the attackers use to steal cookies from the Google Chrome browser?<br>
<code>ChromeKatz</code></p>

<img width="833" height="421" alt="image" src="https://github.com/user-attachments/assets/a9336185-835b-44f3-92ce-e41854002b9e" />

<br>
<br>
<p>1.9 Which phishing technique did the attackers use? Use the report to answer the question.<br>
<code>ClickFix</code></p>

<img width="822" height="424" alt="image" src="https://github.com/user-attachments/assets/def843e0-52a9-4a83-90a7-92fea0f098a5" />

<br>
<br>

<p>1.9 What is the name of the platform that was used to redirect a user to malicious servers?<br>
<code>Discord</code></p>

<br>
<br>
<h2 align="center">Completed</h2>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/59c934e5-575f-4aeb-a28a-01cd899b791d"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/2c18a5fd-3735-4610-bf9f-964991f2df1e"></p>

<h2 align="center">My TryHackMe Journey ・ 2025, September</h2>

<div align="center"><h6>

| Date              | Room                                  |Streak   |   All Time<br>Global   |   All Time<br>Brazil   |   Monthly<br>Global   |   Monthly<br>Brazil  | Points   | Rooms<br>Completed     | Badges    |
|:------------------|:--------------------------------------|--------:|:-----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
| 2025, Sep 10      |Easy 🚩 - <code><strong>Invite Only</strong></code>                  | 494    |     110ᵗʰ    |      5ᵗʰ     |     352ⁿᵈ    |     6ᵗʰ    | 126,056  |    960    |    73     |
| 2025, Sep 10      |Easy 🚩 - Devie                        | 494    |     110ᵗʰ    |      5ᵗʰ     |     607ᵗʰ    |     9ᵗʰ    | 125,606  |    959    |    73     |
| 2025, Sep 10      |Medium 🚩 - Backtrack, in progress     | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ    |     9ᵗʰ    | 125,516  |    958    |    73     |
| 2025, Sep 10      |Easy 🔗 - Detecting Web Attacks        | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ    |     9ᵗʰ    | 125,516  |    958    |    73     |
| 2025, Sep 10      |Easy 🔗 - Attacking ICS Plant #1       | 492    |     110ᵗʰ    |      5ᵗʰ     |     675ᵗʰ    |     9ᵗʰ    | 125,428  |    957    |    73     |
| 2025, Sep 10      |Easy 🔗 - SOC Role in Blue Team        | 492    |     110ᵗʰ    |      5ᵗʰ     |     664ᵗʰ    |     9ᵗʰ    | 125,292  |    956    |    73     |
| 2025, Sep 9       |Hard 🚩 - Python Playground            | 491    |     111ˢᵗ    |      5ᵗʰ     |     693ʳᵈ    |     9ᵗʰ    | 125,236  |    955    |    73     |
| 2025, Sep 9       |Hard 🚩 - Borderlands                  | 491    |     111ˢᵗ    |      5ᵗʰ     |     713ʳᵈ    |    10ᵗʰ    | 125,146  |    954    |    73     |
| 2025, Sep 9       |Medium 🚩 - Forgotten Implant          | 491    |     112ⁿᵈ    |      5ᵗʰ     |     660ᵗʰ    |    10ᵗʰ    | 125,016  |    953    |    73     |
| 2025, Sep 8       |Easy 🔗 - Web Enumeration              | 490    |     112ⁿᵈ    |      5ᵗʰ     |     663ʳᵈ    |    10ᵗʰ    | 124,986  |    952    |    73     |
| 2025, Sep 8       |Easy 🔗 - iOS: Forensics               | 490    |     113ʳᵈ    |      5ᵗʰ     |     548ᵗʰ    |     9ᵗʰ    | 124,850  |    951    |    73     |
| 2025, Sep 7       |Medium 🚩 - VulnNet: Active            | 489    |     114ᵗʰ    |      5ᵗʰ     |     542ⁿᵈ    |     9ᵗʰ    | 124,746  |    950    |    73     |
| 2025, Sep 7       |Medium 🚩 - pyLon                      | 489    |     114ᵗʰ    |      5ᵗʰ     |     535ᵗʰ    |     9ᵗʰ    | 124,716  |    949    |    73     |
| 2025, Sep 7       |Medium 🚩 - Pressed                    | 489    |     113ʳᵈ    |      5ᵗʰ     |     508ᵗʰ    |     9ᵗʰ    | 124,886  |    948    |    73     |
| 2025, Sep 6       |Easy 🚩 - Classic Passwd               | 488    |     114ᵗʰ    |      5ᵗʰ     |     683ʳᵈ    |    12ⁿᵈ    | 124,476  |    947    |    73     |
| 2025, Sep 6       |Medium 🚩 - toc2                       | 488    |     114ᵗʰ    |      5ᵗʰ     |     695ᵗʰ    |    12ⁿᵈ    | 124,446  |    946    |    73     |
| 2025, Sep 6       |Hard 🚩 - Extract                      | 488    |     114ᵗʰ    |      5ᵗʰ     |     716ᵗʰ    |    13ʳᵈ    | 124,386  |    945    |    73     |
| 2025, Sep 6       |Medium 🚩 - Plotted-EMR                | 488    |     114ᵗʰ    |      5ᵗʰ     |     844ᵗʰ    |    12ⁿᵈ    | 124,326  |    944    |    73     |
| 2025, Sep 5       |Medium 🚩 - Inferno                    | 487    |     114ᵗʰ    |      5ᵗʰ     |     758ᵗʰ    |    12ⁿᵈ    | 124,236  |    943    |    73     |
| 2025, Sep 5       |Easy 🔗 - Psycho Break                 | 487    |     115ᵗʰ    |      5ᵗʰ     |     724ᵗʰ    |    10ᵗʰ    | 124,152  |    942    |    73     |
| 2025, Sep 4       |Medium 🚩 - Cold VVars                 | 486    |     113ʳᵈ    |      5ᵗʰ     |     579ᵗʰ    |    10ᵗʰ    | 124,048  |    941    |    73     |
| 2025, Sep 4       |Medium 🔗 - IP and Domain Threat Intel | 486    |     113ʳᵈ    |	    5ᵗʰ     |     579ᵗʰ    |    10ᵗʰ    | 124,018  |   940   |    73     |
| 2025, Sep 3       |Easy 🔗 - Malware Classification       | 485    |     112ⁿᵈ    |      5ᵗʰ     |     714ᵗʰ    |    13ʳᵈ    | 123,882  |    939    |    73     |
| 2025, Sep 2       |Medium 🔗 - Session Forencics          | 484    |     111ˢᵗ    |      5ᵗʰ     |     706ᵗʰ    |    14ᵗʰ    | 123,786  |    938    |    73     |
| 2025, Sep 1       |Medium 🚩 - Voyage                     | 483    |     111ˢᵗ    |      5ᵗʰ     |     849ᵗʰ    |    15ᵗʰ    | 123,636  |    937    |    73     |

</h6></div><br>


<br>

<p align="center">Global All Time:   110ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/0ef3dcf4-eef0-473d-ad58-ed6a142144e7"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/94d953ea-65c1-46d0-afc9-ff690fd8c6a7"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/d5175f19-b218-4134-8011-47953fc96448"><br>
                  Global monthly:    352ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/8c84c995-39a1-4d25-a360-dcb198a44ac1"><br>
                  Brazil monthly:      6ᵗʰ<br><img width="1200px" src="image" src="https://github.com/user-attachments/assets/42b42fdf-d145-4175-9daf-8897d40ff00d"><br>

<h2 align="center">Thanks for coming!</h2>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>  
