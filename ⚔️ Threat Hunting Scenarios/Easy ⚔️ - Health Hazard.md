<h1 align="center">Threat Hunting Scenario &nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;&nbsp; <a href="   "> Health Hazard</a></h1>
<p align="center"><img width="630px" src="https://github.com/user-attachments/assets/2febfb71-1aa9-49e8-ae13-a922f76c32fc"><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20JAN%2024-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Briefing](#1) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Hypothesis](#2) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Objectives](#3)  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Methodology](#4) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Documentation](#5)  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Practice](#6)

<br>
<br>
<h2>Briefing<a id='1'></a></h2>
<p>After months of juggling content calendars and caffeine-fueled brainstorming, co-founder Tom Whiskers finally carved out time to build the company’s first website. It was supposed to be simple: follow a tutorial, install a few packages, and bring the brand to life with lightweight JavaScript magic.<br>
But between sleepless nights and copy-pasted code, Tom started feeling off. Not sick exactly, just off. The terminal scrolled with reassuring green text, the site loaded fine, and everything looked normal.<br>
But no one really knows what might have been hidden beneath it all…<br>
It just waited.</p>
<br>
<br>
<h2>Hypothesis<a id='2'></a></h2>
<p>An attacker may have leveraged a compromised third-party software package to gain initial access to the system and silently stage a payload for later execution. They likely established persistence to maintain access without immediate detection.</p>
<br>
<br>
<h2>Objectives<a id='3'></a></h2>
<p>

- Determine how a threat actor first gained a foothold on the system. Identify suspicious activity that may point to the initial compromise method.<br>
- Investigate signs of malicious execution following the initial access. Analyse the logs and system behaviour to uncover the attacker's actions.<br>
- Identify any mechanisms the attacker used to maintain access across system restarts or user sessions. Look for indicators of persistence that could allow long-term control.</p>

<br>
<br>
<h2>Methodology<a id='4'></a></h2>
<p>
  
- Step 1<br><strong>...</strong><br>...<br><br>
- Step 2<br><strong>...</strong><br>...<br><br>
- Step 3<br><strong>...</strong><br>....</p>

<br>
<br>
<h2>Documentation<a id='5'></a></h2>
<h3>Company Information</h3>

<img width="1900" height="880" alt="image" src="https://github.com/user-attachments/assets/6d491a39-a313-403e-b41d-42d349549f74" />

<br>
<h3>Asset Inventory</h3>

<img width="1899" height="892" alt="image" src="https://github.com/user-attachments/assets/53b8e1dc-8c04-481e-812a-c74aca575415" />


<br>
<br>
<br>
<h2>Practice<a id='6'></a></h2>

<br>
<h3>Summary: Attack Chain</h3>

<div align="left"><h6>

|Stage<br><br><br>                                    |Adversary<br>Step<br>Description<br>                                                                                               |Timestamp<br><br><br>          |Tatic<br><br><br>                        |Technique<br><br><br>    |User<br><br><br>                    |Asset<br><br><br>           |List<br>of<br>IOC´s<br>                       |SIEM<br>URL<br>link<br>|________<br><br><br>|________<br><br><br>|
|:----------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------|:------------------------------|:----------------------------------------|:------------------------|:-----------------------------------|:---------------------------|:---------------------------------------------|:----------------------|:----------------|:----------------|
|&nbsp;&nbsp;&nbsp;&nbsp;<strong>1</strong> . Initial Access<br><br>&nbsp;&nbsp;&nbsp;&nbsp;<strong>2</strong> . Execution<br><br>&nbsp;&nbsp;&nbsp;&nbsp;<strong>3</strong> . Persistence<br><br>____________________|-<br><br>-<br><br>-<br><br>___________|-<br><br>-<br><br>-<br><br>_________|Initial Access<br><br>Execution<br><br>Persistence<br><br>__________________|T1195<br><br>T1095<br><br>T1547<br><br>______________|tom@pawpress.me<br><br>tom@pawpress.me<br><br>tom@pawpress.me<br><br>_____________________|paw tom<br><br>paw tom<br><br>paw tom<br><br>__________|_____________________________________________ <br> _____________________________________________ <br>_____________________________________________ <br> _____________________________________________ <br> _____________________________________________<br> _____________________________________________ <br> _____________________________________________<br>|-<br><br>-<br><br>-<br><br>___________|-<br><br>-<br><br>-<br><br>___________|-<br><br>-<br><br>-<br><br>___________|-<br><br>-<br><br>-<br><br>___________|

</h6></div>

<br>
<h3>Summary Analysis of Hypothesis & Attack Chain</h3>

<div align="left"><h6>

|Stage<br><br><br>                                  |Adversary<br>Step<br>Description<br>                           |Timestamp<br><br><br>|Tatic<br><br><br>    |Technique<br><br><br>                       |User<br><br><br>                                   |Asset<br><br><br>                             |List<br>of<br>IOC´s<br>              |SIEM<br>URL<br>link<br>|Score<br><br>+<code>320</code><br>|Value<br><br>360<br>|
|:--------------------------------------------------|:--------------------------------------------------------------|:--------------------|:--------------------|:-------------------------------------------|:--------------------------------------------------|:---------------------------------------------|:--------------------------------------------|:----------------------|--------:|--------:|
|<strong>Hypothesis</strong><br><br>Attack Chain<br><br>&nbsp;&nbsp;&nbsp;&nbsp;<strong>1</strong> . Initial Access<br><br>&nbsp;&nbsp;&nbsp;&nbsp;<strong>2</strong> . Execution<br><br>&nbsp;&nbsp;&nbsp;&nbsp;<strong>3</strong> . Persistence<br>____________________|-<br><br>+ &nbsp;<code>20</code><br><br>+ &nbsp;10<br><br>+ &nbsp;&nbsp;5<br><br>+ &nbsp;&nbsp;5<br>___________|-<br><br>+ &nbsp;<code>40</code><br><br>+ &nbsp;20<br><br>+ &nbsp;20<br><br>Incorrect<br>_________|-<br><br>+ &nbsp;<code>60</code><br><br>+ &nbsp;20<br><br>+ &nbsp;20<br><br>+ &nbsp;20<br>__________________|-<br><br>+ &nbsp;<code>60</code><br><br>+ &nbsp;20<br><br>+ &nbsp;20<br><br>+ &nbsp;20<br>______________|-<br><br>+ &nbsp;<code>30</code><br><br>+ &nbsp;10<br><br>+ &nbsp;10<br><br>+ &nbsp;10<br>_____________________|-<br><br>+ &nbsp;<code>30</code><br><br>+ &nbsp;10<br><br>+ &nbsp;10<br><br>+ &nbsp;10<br>__________|-<br><br>+ &nbsp;<code>20</code><br><br>+ &nbsp;10<br><br>+ &nbsp;&nbsp;5<br><br>+ &nbsp;&nbsp;5<br>_____________________________________________|-<br><br>-<br><br>-<br><br>-<br><br>-<br>___________|+<code>60</code><br><br>+<code>260</code><br><br>+100<br><br>+90<br><br>+70<br>___________|+60<br><br>+260<br><br>+100<br><br>+100<br><br>+100<br>___________|

</h6></div>


<br>
<br>
<br>

<p align="center"><img width="450px" src=""><br>
                  <img width="450px" src=""><br>
                  <img width="450px" src=""></p>



<br>
<h1 align="center">Threat Hunting Scenario Completed</h1>


<p align="center"><img width="900px" src="https://github.com/user-attachments/assets/7f1264e1-b7b1-4bfb-8cd4-acd76dcbaa54"><br>
                  <img width="900px" src="https://github.com/user-attachments/assets/36c38f0f-a6b5-42cd-a071-d928347c804e"></p>

                  
<h1 align="center">My TryHackMe Journey ・ 2026, January</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|24     |Easy ⚔️ - Health Hazard               |23 |     78ᵗʰ  |     3ʳᵈ    |       94ᵗʰ   |        2ⁿᵈ     |    142,264  |    1,072    |    88     |
|23     |Medium ⚙️ - BlackCat                  |22 |     79ᵗʰ  |     3ʳᵈ    |      104ᵗʰ   |        2ⁿᵈ     |    142,189  |    1,072    |    88     |
|22     |Hard 🚩 - Azure: Tapper               |21 |     82ⁿᵈ  |     3ʳᵈ    |      176ᵗʰ   |        2ⁿᵈ     |    141,154  |    1,072    |    88     |
|22     |Easy ⚙️ - Hidden Hooks                |21 |     82ⁿᵈ  |     3ʳᵈ    |      189ᵗʰ   |        3ʳᵈ     |    141,059  |    1,071    |    88     |
|22     |Medium 🔗 - ret2libc                  |21 |     82ⁿᵈ  |     3ʳᵈ    |      193ʳᵈ   |        3ʳᵈ     |    140,979  |    1,071    |    88     |
|20     |Easy 🔗 - MS Entra ID: Hybrid Identities|19|    82ⁿᵈ  |     3ʳᵈ    |      184ᵗʰ   |        2ⁿᵈ     |    140,971  |    1,069    |    88     |
|19     |Easy ⚙️ - Upload and Conquer          |18 |     81ˢᵗ  |     3ʳᵈ    |      181ˢᵗ   |        2ⁿᵈ     |    140,859  |    1,068    |    88     |
|18     |Easy 🔗 - MS Entra ID: Identities     |17 |     83ʳᵈ  |     3ʳᵈ    |      341ˢᵗ   |        3ʳᵈ     |    139,864  |    1,068    |    88     |
|18     |Easy ⚙️ - APT28: Initial Access       |17 |     84ᵗʰ  |     3ʳᵈ    |      341ˢᵗ   |        3ʳᵈ     |    139,752  |    1,067    |    88     |
|18     |Easy ⚙️ - Hidden Hooks                |17 |           |     3ʳᵈ    |              |                |             |    1,067    |    88     |
|17     |Easy 🔗 - MS Entra ID: Introduction   |17 |     83ʳᵈ  |     3ʳᵈ    |      359ᵗʰ   |        3ʳᵈ     |    139,657  |    1,067    |    88     |
|17     |Easy ⚙️ - APT28: Credential Access    |17 |           |     3ʳᵈ    |              |                |             |    1,067    |    88     |
|17     |Medium ⚙️ - Open Door                 |17 |           |     3ʳᵈ    |              |                |             |     1,067   |    88     |
|17     |Easy 🔗 - Offensive Security Intro    |16 |     87ᵗʰ  |     3ʳᵈ    |      504ᵗʰ   |        5ᵗʰ     |    139,099  |    1,067    |    88     |
|16     |Hard 🚩 - Spring                      |15 |     87ᵗʰ  |     3ʳᵈ    |      540ᵗʰ   |        4ᵗʰ     |    138,942  |    1,066    |    87     |
|14     |Insane 🚩 - Scheme Catcher            |13 |     87ᵗʰ  |     3ʳᵈ    |      534ᵗʰ   |        5ᵗʰ     |    138,822  |    1,065    |    87     |
|13     |Hard 🚩 - Breachblocker Unlocker      |12 |     86ᵗʰ  |     3ʳᵈ    |      526ᵗʰ   |        5ᵗʰ     |    138,732  |    1,064    |    87     |
|11     |Medium 🚩 - Azure: Eyes Wide Shut     |10 |     86ᵗʰ  |     3ʳᵈ    |      558ᵗʰ   |        5ᵗʰ     |    138,450  |    1,063    |    86     |
|8      |Medium ⚙️ - Phishing Unfolding        | 7 |     86ᵗʰ  |     3ʳᵈ    |      508ᵗʰ   |        4ᵗʰ     |    138,372  |    1,062    |    84     |
|8      |Easy ⚙️ - Introduction to Phishing    | 7 |     96ᵗʰ  |     3ʳᵈ    |    2,479ᵗʰ   |       32ⁿᵈ     |    137,117  |    1,062    |    84     |
|8      |Medium 🔗 - KaffeeSec - SoMeSINT      | 7 |     98ᵗʰ  |     3ʳᵈ    |    2,847ᵗʰ   |       38ᵗʰ     |    137,052  |    1,062    |    84     |
|7      |Hard 🚩 - Hack Back                   | 6 |     98ᵗʰ  |     3ʳᵈ    |    2,798ᵗʰ   |       37ᵗʰ     |    136,908  |    1,061    |    84     |
|7      |Hard 🚩 - Dead End?                   | 6 |     99ᵗʰ  |     3ʳᵈ    |    2,924ᵗʰ   |       37ᵗʰ     |    136,788  |    1,060    |    84     |
|6      |Easy 🔗 - Linux Strength Training     | 5 |     98ᵗʰ  |     3ʳᵈ    |    3,172ⁿᵈ   |       47ᵗʰ     |    136,608  |    1,059    |    84     |
|4      |Medium 🚩 - JVM Reverse Engineering   | 3 |     96ᵗʰ  |     3ʳᵈ    |    3,031ˢᵗ   |       46ᵗʰ     |    136,450  |    1,058    |    84     |
|3      |Medium 🚩 - Carrotbane of My Existence| 2 |     96ᵗʰ  |     3ʳᵈ    |    3,468ᵗʰ   |       49ᵗʰ     |    136,150  |    1,057    |    84     |
|2      |Easy 🔗 - Learn Rust                  | 1 |     96ᵗʰ  |     3ʳᵈ    |    5,152ⁿᵈ   |       67ᵗʰ     |    136,030  |    1,056    |    84     |

</h6></div><br>


<p align="center">Global All Time:     78ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/b700a47e-62bb-445f-91ed-057b8e429946"<br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/cd61cf53-7565-4588-a27c-a35fe6d3b70e"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/03275e86-a744-4fc7-b83a-cc43cbebd4f0"><br><br>
                  Global monthly:      94ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/c9e42d86-b56c-47ca-b3a9-6a3df4a3e1df"><br><br>
                  Brazil monthly:       2ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/821956db-da14-488f-9a81-230553397707"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>


<img width="945" height="599" alt="image" src="https://github.com/user-attachments/assets/bef3aebe-75c6-43a3-8e59-64a48a71722c" />






