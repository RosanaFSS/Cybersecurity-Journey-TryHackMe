<p align="center">October 2, 2024</p>
<p align="center">Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{149}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.</p>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Ignite}}$$</h1>
<p align="center">It is classified as an easy-level challenge.
<br>You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.
<br>Can be accessed clicking <a href="https://tryhackme.com/room/ignite">here</a>.</p> 
                                                              
<p align="center"><img width="900px" src="https://github.com/user-attachments/assets/01001d55-7298-47cb-9154-5ac736bdb695"></p>

<br>


<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{CMS}}$$</h1>

<br>
<br>

<p><code>nmap -sV -sC -oA initial</code> TargetIP<br>
Discovered port 80 open running <code>FUEL CMS</code>.</p>

<br>

![October-02-2024 - TryHackMe - Ignite - CTF - Easy - Image  2 - nmap](https://github.com/user-attachments/assets/cb66d72a-9585-44b8-8330-778428ce141c)


<br>

<p>Navigated to <code>http://TargetIP</code>.<br>
Discovered the version = 1.4.</p>

<br>

![October-02-2024 - TryHackMe - Ignite - CTF - Easy - Image 5 - let´s investigate about Fuel CMS Version 1 4](https://github.com/user-attachments/assets/5c8787be-ab0a-43bf-9218-0be73f7af1b0)

<br>

![October-02-2024 - TryHackMe - Ignite - CTF - Easy - Image  3 - accessed the webpage](https://github.com/user-attachments/assets/22340076-6198-4780-b6f1-0c9440178d72)

<br>

![October-02-2024 - TryHackMe - Ignite - CTF - Easy - Image 4 - visualized the other part of the page and found something interesting](https://github.com/user-attachments/assets/74ea708f-f5a1-457f-82ff-b46e2050e4b3)


<br>

<p>Searched for a exploit in <code>ExploitDB</code>.</p>

<br>

![October-02-2024 - TryHackMe - Ignite - CTF - Easy - Image 7 - foud fours typed of Fuel CMS 1 4 1](https://github.com/user-attachments/assets/43b67d6f-0bd4-4856-9fde-838a2c9a7811)


<br>

<p>Donwloaded exploit related to <code>CVE-2018-16763</code>.</p>

<br>

![October-02-2024 - TryHackMe - Ignite - CTF - Easy - Image 8 - CVE 2018-18763 might be the one](https://github.com/user-attachments/assets/b2c54948-e124-4761-99fa-fa2607dfbc8a)


<br>

<p>Updated the exploit file with the AttackIP and to the Python3 syntax.</p>
<br>

![October-02-2024 - TryHackMe - Ignite - CTF - Easy - Image 10 - INspecting and updating code](https://github.com/user-attachments/assets/07398d3a-fc79-478a-b417-10f58397dd7b)

<br>

![October-02-2024 - TryHackMe - Ignite - CTF - Easy - Image 11 - updated the code to Python3](https://github.com/user-attachments/assets/894ded96-4e80-4d9d-830a-bdcabedf1bd4)

<br>

![October-02-2024 - TryHackMe - Ignite - CTF - Easy - Image 12 - updated the code to Python3 again again](https://github.com/user-attachments/assets/0bba12c6-6c18-434d-bbb5-e2eed5294db6)


<br>

<p>Ran the script.</p>

<br>

![October-02-2024 - TryHackMe - Ignite - CTF - Easy - Image 13 - code output after running whoami](https://github.com/user-attachments/assets/9a62f759-4cd5-4d72-86ea-5f6540f4c71c)

<br>

<p>Achieved Remote Execution.</p>

![October-02-2024 - TryHackMe - Ignite - CTF - Easy - Image 14 - the highlighted part shows that we achieved remote execution](https://github.com/user-attachments/assets/19c3c37e-9c86-4c1e-868a-2e1ce9312b29)


<br>

<p>Started a listener.<br>
<br>
8:-)<br>
<br>
I am laughing becuse by the time I am writing know how to do it effectively.<br>
...<br>
We got the shell!!!</p>

<br>

![October-02-2024 - TryHackMe - Ignite - CTF - Easy - Image 19 - Listenong worked](https://github.com/user-attachments/assets/e7823373-4b5b-461d-936d-0e1a0aafe179)

<br>

<br>

<p>Estabilised the shell.</p>

<br>

![image](https://github.com/user-attachments/assets/96ec7ca7-cb54-4fed-80cd-dbdd1823fb79)

<br>

<p>Now we have an interative prompt.</p>

<br>

![image](https://github.com/user-attachments/assets/e22d1ecd-6fd8-4237-9d9a-9b166a5f8926)

<br>

<p>Discovered the flag in <code>/home/www-data</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/b2855179-6196-4645-b5e3-bed85c592694)


<br>

![image](https://github.com/user-attachments/assets/94e4db85-de87-4afb-ac3a-9a3042651023)

<br>


<p>Navigated through the directories and discovered <code>fuel</code> and <code>application</code>.<br>
In there discovered <code>database.php</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/57caf67a-f151-4416-af02-4279d72f32db)



<br>


<p>Discovered important information about the database...<br>
some credentials.<br><br>
Used <code>su -</code>, typed the password just discovered and got root access.</p>

<br>

![October-02-2024 - TryHackMe - Ignite - CTF - Easy - Image 32 - got privileged access using    sudo -](https://github.com/user-attachments/assets/bb041f8e-dfa8-4add-98d5-d64d31bc952c)


<br>

![image](https://github.com/user-attachments/assets/d2e489ca-a5cf-4c8b-a0bc-0dc2a1543b49)

<br><br>

<br>

![October-02-2024 - TryHackMe - Ignite - CTF - Easy - Image 34 - room completed](https://github.com/user-attachments/assets/d08e1ecd-f40a-4bd8-8784-652bf7d7a6c3)

<br>

![October-02-2024 - TryHackMe - Ignite - CTF - Easy - Image 35 - room complete - another view](https://github.com/user-attachments/assets/bee60a29-4bb2-4eae-b80c-4a355c0f8c33)




