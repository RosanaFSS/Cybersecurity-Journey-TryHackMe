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
<h2>Methodology<a id='3'></a></h2>
<p>
  
- Step 1<br><strong>...</strong><br>...<br><br>
- Step 2<br><strong>...</strong><br>...<br><br>
- Step 3<br><strong>...</strong><br>....</p>

<br>
<br>
<h2>Documentation<a id='4'></a></h2>
<h3>Company Information</h3>

<img width="1900" height="880" alt="image" src="https://github.com/user-attachments/assets/6d491a39-a313-403e-b41d-42d349549f74" />

<br>
<h3>Asset Inventory</h3>

<img width="1899" height="892" alt="image" src="https://github.com/user-attachments/assets/53b8e1dc-8c04-481e-812a-c74aca575415" />


<br>
<br>
<br>
<h2>Practice<a id='5'></a></h2>

<h3>Summary: Attack Chain</h3>

<div align="left"><h6>

|Stage<br><br><br>                                    |Adversary<br>Step<br>Description<br>                                                                                               |Timestamp<br><br><br>          |Tatic<br><br><br>                        |Technique<br><br><br>    |User<br><br><br>                    |Asset<br><br><br>           |List<br>of<br>IOC´s<br>                       |SIEM<br>URL<br>link<br>|________<br><br><br>|________<br><br><br>|
|:----------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------|:------------------------------|:----------------------------------------|:------------------------|:-----------------------------------|:---------------------------|:---------------------------------------------|:----------------------|:----------------|:----------------|
|&nbsp;&nbsp;&nbsp;&nbsp;<strong>1</strong> . Initial Access<br><br>&nbsp;&nbsp;&nbsp;&nbsp;<strong>2</strong> . Execution<br><br>&nbsp;&nbsp;&nbsp;&nbsp;<strong>3</strong> . Persistence<br><br>____________________|-<br><br>-<br><br>-<br><br>___________|-<br><br>-<br><br>-<br><br>_________|Initial Access<br><br>Execution<br><br>Persistence<br><br>__________________|T1195<br><br>T1095<br><br>T1547<br><br>______________|tom@pawpress.me<br><br>tom@pawpress.me<br><br>tom@pawpress.me<br><br>_____________________|paw tom<br><br>paw tom<br><br>paw tom<br><br>__________|_____________________________________________ <br> _____________________________________________ <br>_____________________________________________ <br> _____________________________________________ <br> _____________________________________________<br> _____________________________________________ <br> _____________________________________________<br>|-<br><br>-<br><br>-<br><br>___________|-<br><br>-<br><br>-<br><br>___________|-<br><br>-<br><br>-<br><br>___________|-<br><br>-<br><br>-<br><br>___________|

</h6></div>

<h3>Summary Analysis of Hypothesis & Attack Chain</h3>

<div align="left"><h6>

|Stage<br><br><br>                                  |Adversary<br>Step<br>Description<br>                           |Timestamp<br><br><br>|Tatic<br><br><br>    |Technique<br><br><br>                       |User<br><br><br>                                   |Asset<br><br><br>                             |List<br>of<br>IOC´s<br>              |SIEM<br>URL<br>link<br>|Score<br><br>+<code>320</code><br>|Value<br><br>360<br>|
|:--------------------------------------------------|:--------------------------------------------------------------|:--------------------|:--------------------|:-------------------------------------------|:--------------------------------------------------|:---------------------------------------------|:--------------------------------------------|:----------------------|--------:|--------:|
|<strong>Hypothesis</strong><br><br>Attack Chain<br><br>&nbsp;&nbsp;&nbsp;&nbsp;<strong>1</strong> . Initial Access<br><br>&nbsp;&nbsp;&nbsp;&nbsp;<strong>2</strong> . Execution<br><br>&nbsp;&nbsp;&nbsp;&nbsp;<strong>3</strong> . Persistence<br>____________________|-<br><br>+ &nbsp;<code>20</code><br><br>+ &nbsp;10<br><br>+ &nbsp;&nbsp;5<br><br>+ &nbsp;&nbsp;5<br>___________|-<br><br>+ &nbsp;<code>40</code><br><br>+ &nbsp;20<br><br>+ &nbsp;20<br><br>Incorrect<br>_________|-<br><br>+ &nbsp;<code>60</code><br><br>+ &nbsp;20<br><br>+ &nbsp;20<br><br>+ &nbsp;20<br>__________________|-<br><br>+ &nbsp;<code>60</code><br><br>+ &nbsp;20<br><br>+ &nbsp;20<br><br>+ &nbsp;20<br>______________|-<br><br>+ &nbsp;<code>30</code><br><br>+ &nbsp;10<br><br>+ &nbsp;10<br><br>+ &nbsp;10<br>_____________________|-<br><br>+ &nbsp;<code>30</code><br><br>+ &nbsp;10<br><br>+ &nbsp;10<br><br>+ &nbsp;10<br>__________|-<br><br>+ &nbsp;<code>20</code><br><br>+ &nbsp;10<br><br>+ &nbsp;&nbsp;5<br><br>+ &nbsp;&nbsp;5<br>_____________________________________________|-<br><br>-<br><br>-<br><br>-<br><br>-<br>___________|+<code>60</code><br><br>+<code>260</code><br><br>+100<br><br>+90<br><br>+70<br>___________|+60<br><br>+260<br><br>+100<br><br>+100<br><br>+100<br>___________|

</h6></div>




<p align="center"><img width="450px" src=""><br>
                  <img width="450px" src=""><br>
                  <img width="450px" src=""></p>



<img width="1252" height="299" alt="image" src="https://github.com/user-attachments/assets/c7055625-ea60-47af-873c-2a144d1ada4b" />


<img width="1116" height="902" alt="image" src="https://github.com/user-attachments/assets/7f1264e1-b7b1-4bfb-8cd4-acd76dcbaa54" />



<img width="1127" height="419" alt="image" src="https://github.com/user-attachments/assets/36c38f0f-a6b5-42cd-a071-d928347c804e" />


<img width="266" height="174" alt="image" src="https://github.com/user-attachments/assets/05ffa54a-7df2-4e28-aa57-7f26d55329cd" />


<img width="266" height="259" alt="image" src="https://github.com/user-attachments/assets/896ed237-607d-479f-bc83-6f830a6ca4cc" />

<img width="262" height="277" alt="image" src="https://github.com/user-attachments/assets/595dbc58-7ce6-41fb-bbeb-0076b03b706b" />










