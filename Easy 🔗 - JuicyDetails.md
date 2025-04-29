<p align="center">April 29, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{358}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/0ad6d78e-0e08-4d29-a43e-96d980b519d8" alt="Your Image Badge"><br>
<img width="300px" src="https://github.com/user-attachments/assets/9050e33f-101f-4a0f-bb58-9640a7b72eff" alt="streak"><br></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Juicy Details}}$$</h1>
<p align="center"><em>A popular juice shop has been breached! Analyze the logs to see what had happened.</em>.<br>
It is classified as an easy-level walkthrough.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/juicydetails">here</a>.</p>

<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/eaf189e0-2c85-47e3-8423-07d1df447c3f"> </p>

<br>
<br>


<h2>Task 1 . Introduction </h2>
<h3>Introduction</h3>

<p>[ Download Task Files ]</p>

                                      

<p>You were hired as a SOC Analyst for one of the biggest Juice Shops in the world and an attacker has made their way into your network. <br><br>

Your tasks are:<br>

- Figure out what techniques and tools the attacker used<br>
- What endpoints were vulnerable<br>
- What sensitive data was accessed and stolen from the environment<br>
- An IT team has sent you a zip file containing logs from the server. Download the attached file, type in "I am ready!" and get to work! There's no time to lose!</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 1.1. <em>Are you ready?</em><br><a id='1.1'></a>
>> <strong><code>I am ready!</code></strong><br>
<p></p>

<br>
<br>


<h2>Task 2 . Reconnaissance</h2>
<h3>Reconnaissance</h3>

                                      

<p>Analyze the provided log files.<br><br>

Look carefully at:<br>

- What tools the attacker used<br>
- What endpoints the attacker tried to exploit<br>
- What endpoints were vulnerable</h3>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 2.1. <em>What tools did the attacker use? (Order by the occurrence in the log)</em><br><a id='2.1'></a>
>> <strong><code>nmap, hydra, sqlmap, curl, feroxbuster</code></strong><br>
<p></p>

<br>

```bash
awk '{ cmd = $12 " " $13 " " $14; if (!seen[cmd]++) print $0, cmd }' access.log | sort -u
```

<br>

![image](https://github.com/user-attachments/assets/2b76f8db-997e-4256-b44d-9689ac4cd866)

<br>

> 2.2. <em>What endpoint was vulnerable to a brute-force attack?</em><br><a id='2.2'></a>
>> <strong><code>/rest/user/login</code></strong><br>
<p></p>

<br>

```bash
awk '{ cmd = $12 " " $13 " " $14; if (!seen[cmd]++) print $0, cmd }' access.log | sort -u
```

<br>

![image](https://github.com/user-attachments/assets/f1e0ab90-d938-4a0b-bbed-6fd17e840da7)


<br>

> 2.3. <em>What endpoint was vulnerable to SQL injection?</em><br><a id='2.3'></a>
>> <strong><code>/rest/products/search</code></strong><br>
<p></p>

<br>

```bash
awk '{ cmd = $12 " " $13 " " $14; if (!seen[cmd]++) print $0, cmd }' access.log | sort -u
```

<br>

![image](https://github.com/user-attachments/assets/a6456a77-8118-4aa6-8de5-eba32ef05454)


<br>

> 2.4. <em>What parameter was used for the SQL injection?</em><br><a id='2.4'></a>
>> <strong><code>q</code></strong><br>
<p></p>

<br>

```bash
awk '{ cmd = $12 " " $13 " " $14; if (!seen[cmd]++) print $0, cmd }' access.log | sort -u
```

<br>

![image](https://github.com/user-attachments/assets/299c8df0-97ae-4309-b18f-37559de17968)

<br>


> 2.5. <em>What endpoint did the attacker try to use to retrieve files? (Include the /)</em><br><a id='2.5'></a>
>> <strong><code>/ftp</code></strong><br>
<p></p>

<br>

```bash
awk '{ cmd = $12 " " $13 " " $14; if (!seen[cmd]++) print $0, cmd }' access.log | sort -u
```

<br>

![image](https://github.com/user-attachments/assets/5e381749-de4a-417f-bc1b-3a7a11aca781)


<br>

<h2>Task 3 . Stole Data </h2>
<h3>Stolen data</h3>

                                      

<p>Analyze the provided log files.<br><br>

Look carefully at:<br>

- The attacker's movement on the website<br>
- Response codes<br>
- Abnormal query strings</h3>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 3.1. <em>What section of the website did the attacker use to scrape user email addresses?</em>Hint : <em>Where can customers usually comment on a shopping website?</em><br><a id='3.1'></a>
>> <strong><code>product reviews</code></strong><br>
<p></p>

<br>

```bash
cat access.log | grep "review" | sort -u
```

<br>

<br>

![image](https://github.com/user-attachments/assets/90e52fa9-ff39-4013-a9b4-e876c9703303)

<br>



> 3.2. <em>Was their brute-force attack successful? If so, what is the timestamp of the successful login? (Yay/Nay, 11/Apr/2021:09:xx:xx +0000)</em><br><a id='3.2'></a>
>> <strong><code>Yay, 11/Apr/2021:09:16:31 +0000</code></strong><br>
<p></p>

<br>

```bash
grep "Hydra" access.log | grep "200"
```

<br>

![image](https://github.com/user-attachments/assets/bb6f7d10-1d4f-497f-838e-0c372a97689c)

<br>

> 3.3. <em>What user information was the attacker able to retrieve from the endpoint vulnerable to SQL injection?</em><br><a id='3.2'></a>
>> <strong><code>Yay, 11/Apr/2021:09:16:31 +0000</code></strong><br>
<p></p>

<br>

```bash
grep "/rest/products/search" access.log | grep "200" > analysis
```

<br>


<p>Opened <code>analysis</code> in </code>CyberChef</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/4cdbb0c6-c71c-47fb-9538-671b5a4f0e53)

<br>

> 3.4. <em>What files did they try to download from the vulnerable endpoint? (endpoint from the previous task, question #5)</em><br><a id='3.4'></a>
>> <strong><code>coupons_2013.md.bak, www-data.bak</code></strong><br>
<p></p>

<br>

```bash
grep "GET /ftp/" access.log
```

<br>


![image](https://github.com/user-attachments/assets/10b8fb8b-d09c-4170-a120-60877596d1ad)


<br>

> 3.5. <em>What service and account name were used to retrieve files from the previous question? (service, username)</em>Hint : <em>What other log files do you have?</em><br><a id='3.5'></a>
>> <strong><code>ftp, anonymous</code></strong><br>
<p></p>

<br>

```bash
cat vsftpd.log
```

<br>


![image](https://github.com/user-attachments/assets/47ea3f84-3646-4a5b-90c2-34fd593591ae)

> 3.6. <em>What service and username were used to gain shell access to the server? (service, username)</em><br><a id='3.6'></a>
>> <strong><code>ftp, anonymous</code></strong><br>
<p></p>

<br>

<br>

```bash
cat auth.log | grep "Accepted password"
```

<br>



![image](https://github.com/user-attachments/assets/63e2c8dd-7182-4e66-8874-c55ca3d62d39)



<br>
<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center">
<img width="1000px" src="https://github.com/user-attachments/assets/2b1a5df6-ed2e-4602-91cc-d450df62d0e2"><br>
<img width="1000px" src="https://github.com/user-attachments/assets/79778ae4-f43e-416b-a6de-729c5eef360a"></p>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| April 29, 2025    | 358      |     246ᵗʰ    |      6ᵗʰ     |     52ⁿᵈ    |     2ⁿᵈ    |  98,435  |    696    |     60    |

</div>

<br>

<p align="center"> Global All Time:  246ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/3714de89-7508-45b0-9b43-ee6d0229d726"> </p>

<p align="center"> Brazil All Time:    6ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/dc860106-35b3-47c5-8cb0-0075654c418f"> </p>

<p align="center"> Global monthly:    52ⁿᵈ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/7eb36126-2d8f-4fab-ba74-9c35cbeca501"> </p>

<p align="center"> Brazil monthly:    2ⁿᵈ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/0d436687-94a7-495a-98a0-19d3aca99fd5"> </p>

<br>
<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Skills Matrix}}$$</h1>

<br>

<p align="center"> Security Analyst <br><br><img width="1000px" src="https://github.com/user-attachments/assets/91644f6f-0b79-457f-9ed7-d0511bad08c2"> </p>





<br>
<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/GEEZET1">GEEZET1</a> for investing your time and effort to develop this challenge so that I could sharpen my skills!</p> 
