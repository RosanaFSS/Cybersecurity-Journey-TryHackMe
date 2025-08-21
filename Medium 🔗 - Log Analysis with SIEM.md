<h1 align="center">Log Analysis with SIEM</h1>
<p align="center">2025, August 21<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>472</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Learn how SIEM solutions can be used to detect and analyse different types of malicious behaviour.</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/ea97b004-3844-459e-9d17-021c2523a7bc"><br>
Access this TryHackMe´s walkthrough <a href="https://tryhackme.com/room/loganalysiswithsiem">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/dae64b77-18e1-4b0e-93a7-8cccf1328d32"></p>


<br>
<h2>Task 1 . Introduction</h2>
<br>

<p><em>Answer the question below</em></p>

<p>1.1. Let´s go!<br>
<code>No answer needed</code></p>

<br>
<br>
<h2>Task 2 . Benefits of SIEM for Analysts</h2>

<br>

<p>2.1. What is the process of linking data from multiple sources to identify relationships between individual events called?<br>
<code>Correlation</code></p>

<br>

<p><em>Answer the questions below</em></p>

<p>2.2. What is the process of collecting and storing log data from multiple systems and sources into a single, unified location for easier analysis called?<br>
<code>Centralisation</code></p>

<br>
<br>
<h2>Task 3 . Log sources overview</h2>

<br>

<p><em>Answer the questions below</em></p>

<p>3.1. What is the process of converting logs from different formats into a single format for easier analysis in a SIEM?<br>
<code>Normalisation</code></p>

<br>

<p>3.2. Which log source type can be used to detect the execution of a malicious script?<br>
<code>Host0based</code></p>

<br>
<br>
<h2>Task 4 . Windows Logs</h2>

<br>

<p><em>Answer the questions below</em></p>

<p>4.1. Which IP address was the connection established with?<br>
<code>10.10.114.80</code></p>

<p>

- select <code>All time</code></p>

<br>

```bash
index=task4  DestinationPort=5678
| sort +_time
```

<br>

<img width="1062" height="456" alt="image" src="https://github.com/user-attachments/assets/485fa3ec-f07b-430e-b0ef-dc938dd108be" />

<br>
<br>
<p>4.2. Which process initiated this suspicious connection?<br>
<code>SharePoInt.exe</code></p>

<br>

<img width="1278" height="388" alt="image" src="https://github.com/user-attachments/assets/d857b230-33b1-4f1f-a4f1-b03133229713" />

<br>
<br>

<img width="1060" height="156" alt="image" src="https://github.com/user-attachments/assets/d4bff627-ce83-4161-9486-82abf56ebf34" />

<br>
<br>
<p>4.3. What is the MD5 hash of the malicious process from the previous question?<br>
<code>770D14FFA142F09730B415506249E7D1</code></p>

<p>

- click <code>Event Actions</code><br>
- click <code>Show Source</code></p>

<br>

<img width="1274" height="399" alt="image" src="https://github.com/user-attachments/assets/2ce6dfee-4c7d-4dc1-9405-ba61893bab0f" />

<br>
<br>
<p>4.4. What is the name of the scheduled task that was created on the system?<br>
<code>Office365 Install</code></p>

<br>

```bash
index=task4 Description="*Sched*"
| sort +_time
```

<br>

<img width="1273" height="417" alt="image" src="https://github.com/user-attachments/assets/d51a3943-b9d1-49e6-bbda-87ace5d0278c" />

<br>
<br>
<h2>Task 5 . Linux Logs</h2>
<br>

<p><em>Answer the questions below</em></p>


<p>5.1. What was the timestamp of the remote-ssh account creation? Answer Format Example: 2025-01-15 12:30:45<br>
<code>2025-08-12 09:52:57</code>
<br>

```bash
index=task5 process=useradd
| sort +_time
```

<br>

<img width="1271" height="376" alt="image" src="https://github.com/user-attachments/assets/fcee9abc-9b6e-42fe-9f7d-cd0e371ffe12" />

<br>
<br>

<img width="1337" height="413" alt="image" src="https://github.com/user-attachments/assets/0304d7ed-5bdb-4f39-be60-d8d87a22add7" />

<br>
<br>

<p>5.2. Which user successfully escalated their privileges to root prior to the action from the first question?<br>
<code>jack-brown</code>
<br>

```bash
index=task5 (process=sudo OR process=su)
| sort +_time
```

<br>


<img width="484" height="227" alt="image" src="https://github.com/user-attachments/assets/e752ee91-ede6-4b4d-894b-fb320b93cc1c" />


<br>
<br>

<img width="1267" height="712" alt="image" src="https://github.com/user-attachments/assets/3ce2c702-f426-4c21-9bed-e8733f4b3293" />


<br>
<br>

<p>5.3. From which IP address did the user from the previous question successfully log in to the system?<br>
<code>10.14.94.82</code>
<br>

```bash
index=task5
| sort +_time
```

<br>

<img width="486" height="225" alt="image" src="https://github.com/user-attachments/assets/a0bb0d40-977c-4c8f-be5a-45e4735228f0" />

<br>
<br>

<img width="1261" height="449" alt="image" src="https://github.com/user-attachments/assets/387656e4-b073-4ee6-8f41-d94225246e4d" />


<br>
<br>
<p>5.4. How many failed login attempts occurred prior to this successful login?<br>
<code>4</code>

<br>

```bash
index=task5 source=auth.log *status 22*
| sort +_time
```

<br>

<img width="483" height="230" alt="image" src="https://github.com/user-attachments/assets/7793ba0e-f679-4005-9707-54624c308ff1" />

<br>
<br>

<img width="1268" height="533" alt="image" src="https://github.com/user-attachments/assets/19332f9d-f440-4843-b528-29ede96e3960" />

<br>
<br>
<p>5.5. Which port is the persistence mechanism configured to connect to?<br>
<code>7654</code>

<br>

```bash
index=task5 (process=CRON OR process=crontab) *connect*
| sort +_time
```

<br>

<img width="1376" height="327" alt="image" src="https://github.com/user-attachments/assets/22aa2b33-87f2-4994-b9db-e692178bba6c" />

<br>
<br>
<h3>Task 6 . Web Application Logs</h3>
<br>

<p><em>Answer the questions below</em></p>


<p>6.1. Which URI path had the highest number of requests?<br>
<code>/wp-login.php</code>
<br>

```bash
index=task6
| stats count by uri_path
| sort -count
```

<br>

<img width="935" height="646" alt="image" src="https://github.com/user-attachments/assets/d65337b4-b9eb-44d0-8973-047c3901ae8c" />

<br>
<br>
<p>6.2. Which IP address was the source of the activity?<br>
<code>10.10.243.134</code>
<br>

```bash
index=task6 *wp-login.php*
| table _time, uri_path, clientip
| sort +_time
```

<br>

<img width="1175" height="360" alt="image" src="https://github.com/user-attachments/assets/7b09ba79-5d60-498d-9045-8b6e0810fa46" />

<br>
<br>
<p>6.3. How can this activity be classified?<br>
<code>Brute Force</code>
  
  
<br>
<br>
<p>6.3. Which tool did the threat actor use?<br>
<code>WPScan</code>

<br>

```bash
index=task6 *wp-login.php* *post*
| stats count by uri_path, clientip
```

<br>
<br>

<img width="1176" height="338" alt="image" src="https://github.com/user-attachments/assets/5eefc728-9fb4-45c8-87e6-8bd2812f881a" />

<br>
<br>

```bash
index=task6 uri_path="/wp-login.php" clientip="10.10.243.134" method=POST
| sort +_time
```
<br>
<br>

<img width="1175" height="351" alt="image" src="https://github.com/user-attachments/assets/b0223cd6-5768-4e44-a2ca-1b8264768d50" />

<br>
<br>

<img width="1183" height="685" alt="image" src="https://github.com/user-attachments/assets/42440ea5-c225-41fa-bd49-df7f6682b5f7" />

<br>
<br>
<br>






