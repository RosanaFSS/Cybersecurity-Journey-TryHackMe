<p align="center">November 10, 2024</p>
<p align="center">Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{188}}$$-day-streak in  <a href="https://tryhackme.com/r/hacktivities">TryHackMe</a>.</p>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{ Scripting }}$$ </h1>
<p align="center">Learn basic scripting by solving some challenges!</p>
<p align="center">Access this TryHackMe CTF Room clicking <a href="https://tryhackme.com/r/room/scripting">Scripting</a>.</p>
<p align="center">
  <img height="150px" hspace="20" src="https://github.com/user-attachments/assets/5061cdbe-980e-4ba0-ae69-60d5a10fdbf2"><br>
  <img width="900px" src="https://github.com/user-attachments/assets/098e7cb5-22c6-48ea-a660-c3df66b77042">
</p>


<br>
<br>
<br>
<h2 align="center">Task 1. [Easy] Base64<a id='1'></a></h2>
<p>This file has been base64 encoded 50 times - write a script to retrieve the flag. Here is the general process to do this:</p>p>

<ol type="1. ">
  <li>read input from the file</li>
  <li>use function to decode the file</li>
  <li>Run Nmap’s traceroute</li>
  <li>Run select Nmap scripts</li>
  <li>Save the scan results in various formats</li>
</ol></p>

<p>Try do this in both Bash and Python!</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> 1.1. <em>What is the final string?</em><br><a id='1.1'></a>
>> <code><strong>HackBack2019=</strong></code>

<br>
<p>I downloaded room´s file and renamed it to <code>THMscripting.txt</code>.</p>


<p>Called the following file <code>THMctf.py</code>.</p>

<pre><code>$ nano THMctf.py
</code></pre>
  
<pre><code>import base64

#Open file
with open('THMscripting.txt') as f:
    msg = f.read()

#Decode 50 times
for _ in range(50):
    msg = base64.b64decode(msg)

print(f"The flag is: {msg.decode('utf8')}")
</code></pre>

<p>After running the file with Python3 I got the flag.</p>
<pre><code>$ python3 THMctf.py                
The flag is: HackBack2019=
</code></pre>

<br>


<br>
<h2 align="center">Task 2. [Medium] Gotta Catch em All<a id='2'></a></h2>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> 2.1. <em>Once you have done all operations, what number do you get (rounded to 2 decimal places at the end of your calculation)?</em><br><a id='2.1'></a>
>> <code><strong>344769.12</strong></code>

<br>
<h2 align="center">Task 3. [Hard] Encrypted Server Chita Chat<a id='3'></a></h2>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> 3.1. <em>What is the flag?</em><br><a id='3.1'></a>
>> <code><strong>THM{eW-sCrIpTiNg-AnD-cRyPtO}</strong></code>


<br>
<h2>Room Complete<a id='4'></a></h2>
<p>Keep learning, keep growing!</p>

<p align="center"> <img width="750px" src="https://github.com/user-attachments/assets/5f354c71-ec20-408f-a672-8301c0291090"></p>

<h2>My Journey<a id='5'></a></h2>
<p>Following I share the status of my journey in TryHackMe.</p>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     |
| :---------------: | :------- | :----------- | :----------- | :---------- | :--------- | :------  | :-------- |
|                   |          | WorldWide    | Brazil       | WorldWide   | Brazil     |          | Completed |
| November 10, 2024 | 188      |       1,247ª |          25ª |      4,292ª |        60ª | 54,698   |       415 |

</div>


<p align="center"> <img width="750px" src="https://github.com/user-attachments/assets/1cc5b812-47ed-4f70-803a-fa73e9b6cdfd"></p>

<p style="text-align: center;">Thank you for coming. Hope to learn together again!!</p>
