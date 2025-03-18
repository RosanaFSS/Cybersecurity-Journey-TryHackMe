<p align="center">December 25, 2024</p>
<p align="center">Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{233}}$$-day-streak in  <a href="https://tryhackme.com/">TryHackMe</a>.</p>

<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{Retro}}$$

</h1>
<p align="center">New high score!</p>
<p align="center">Access this 🆓 TryHackMe CTF Room clicking <a href="https://tryhackme.com/r/room/overpass2hacked">Retro</a>.</p><br>
<p align="center">
  <img height="150px" hspace="20" src="https://github.com/user-attachments/assets/549ef432-b001-4fe3-8c8b-3d2e75c0349a">
  <img width="800px" src="https://github.com/user-attachments/assets/e3a9fad3-f316-424c-9434-f5f6c626111d">
</p>

<br>

<h2>Task 1. Pwn</h2>

<p align="center">
  <img width="150px" src="https://github.com/user-attachments/assets/a89030d4-3184-425d-8ae9-bf2a78830054">
</p>

<p align="center">Can you time travel? If not, you might want to think about the next best thing.<br>

Please note that this machine does not respond to ping (ICMP) and may take a few minutes to boot up.<br>

-------------------------------------</p>

<p align="center"><em></em>There are two distinct paths that can be taken on Retro. One requires significantly less trial and error, however, both will work. Please check writeups if you are curious regarding the two paths. An alternative version of this room is available in it's remixed version Blaster.</em></p>


<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 1.1. <em>A web server is running on the target. What is the hidden directory which the website lives on??</em><br><a id='1.1'></a>
>> <code><strong>/retro</strong></code>

<br>

> 1.2. <em>user.txt</em><br><a id='1.2'></a>
>> <code><strong>3b99fbdc6d430bfb51c72c651a261927</strong></code>

<br>

> 1.3. <em>user.txt</em><br><a id='1.3'></a>
>> <code><strong>___________________</strong></code>

<br>

<br>

<br>

<pre><code># nmap -Pn --script vuln [Target]</code></pre>

<br>

![image](https://github.com/user-attachments/assets/b0bc69a8-860c-48ca-a6a1-a50ea17cc153)

<br>

<pre><code># nmap -sC -sV -Pn [Target]</code></pre>

<br>

![image](https://github.com/user-attachments/assets/3a80b505-b292-4726-a10f-bba6db3acd01)

<br>

<pre><code>echo [Target] retro.thm >> /etc/hosts</code></pre>


<br>

![image](https://github.com/user-attachments/assets/4bb82a14-47d0-4866-bf86-e99c0d0d9b4b)

<br>

<pre><code>gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -u http:/[Target]</code></pre>

<br>

![image](https://github.com/user-attachments/assets/7e514192-db3e-4ea7-aa80-4f0164fa5600)

<br>

![image](https://github.com/user-attachments/assets/0f8f69c4-64ce-41d2-b692-9d0788986310)


<br>


<h3>/retro</h3>

<pre><code>gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -u http:/[Target]/retro</code></pre>

<br>

![image](https://github.com/user-attachments/assets/d6db8c7d-17b6-4fe2-a368-0c294753ee01)


<br>

![image](https://github.com/user-attachments/assets/9aaa8053-8fa5-4637-8a77-f38baed5a935)


<br>

![image](https://github.com/user-attachments/assets/b675d6e4-265d-4952-a19b-ec4e3388a723)

<br>

![image](https://github.com/user-attachments/assets/f098fbfd-a640-4a0e-9954-1ef5ec122fa6)

<br>

<pre><code>http://retro.thm/retro/index.php/2019/12/09/ready-player-one/#comment-2</code></pre>

![image](https://github.com/user-attachments/assets/8dccaa91-4360-4165-b6b2-becc1dbe292c)


<br>




<h3>/retro/wp-content</h3>


<pre><code>gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -u http:/[Target]/retro/wp-content</code></pre>

<br>

![image](https://github.com/user-attachments/assets/f9b327ac-b8d3-4548-87f7-47186c2d0297)

<br>

<h3>/retro/wp-includes</h3>

<pre><code>gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -u http:/[Target]/retro/wp-content</code></pre>

<br>

![image](https://github.com/user-attachments/assets/25d853dd-49f5-47ba-99f1-39df4ccb844e)

<br>

<h3>/retro/wp-admin</h3>

<pre><code>gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -u http:/[Target]/retro/wp-admin</code></pre>

<br>

![image](https://github.com/user-attachments/assets/1850328b-53de-4076-962e-50f5e26c6032)

<br>


<h2>Microsoft 2016  IIS 10.0</h2>

![image](https://github.com/user-attachments/assets/fe31359f-6d0d-4353-a5f2-70016747506a)

<br>

![image](https://github.com/user-attachments/assets/bc40a0fd-7ac3-4fd1-8275-fd80333144c8)


<br>

![image](https://github.com/user-attachments/assets/71e0448c-dd21-4f93-9de3-1b29b4e96376)

<br>

<pre><code>http://[Target]/retro/index.php/2019/12/09/ready-player-one/#comment-2</code></pre>

<br>

![image](https://github.com/user-attachments/assets/6278e361-7327-4c47-9bc8-e2c89ff7fa80)

<br>

![image](https://github.com/user-attachments/assets/9c883def-d310-4ee4-b9a5-c0a7a832296d)

<br>

![image](https://github.com/user-attachments/assets/e22edca8-8ba0-4a19-9334-d958868ceeba)


<br>

![image](https://github.com/user-attachments/assets/19bdcd7b-9788-468f-821b-b8c35aac4b74)


<br>

![image](https://github.com/user-attachments/assets/4c9ff2fc-6bd6-4fa9-9540-0a9399eb6637)


<br>

<br>

<br>

![image](https://github.com/user-attachments/assets/2d19f831-72fe-4631-acfe-fec90e512d7e)

<br>

![image](https://github.com/user-attachments/assets/4f269aea-b943-476b-b743-0d7a7e3b21db)

<br>

![image](https://github.com/user-attachments/assets/f0918613-7fff-4751-87b4-9b3a95da52be)

<br>

<br>

![image](https://github.com/user-attachments/assets/e44a4b6f-5ac5-44a2-88cf-3835add5598a)

<br>

![image](https://github.com/user-attachments/assets/f5666a7f-49a2-439f-a84c-7e0f7b85c21e)

<br>

![image](https://github.com/user-attachments/assets/0d23fe29-e3d8-40e8-96ed-609b1b996745)

<br>

<p>I restored the file.</p>


![image](https://github.com/user-attachments/assets/66327a5d-53be-4efb-8328-fbd571f8f314)


<p>I run it as Administrator.  Selected Show More Details. Then Show Inofrmation about the publisher´s certificate.  And I got this.</p>

<br>

![image](https://github.com/user-attachments/assets/ac6c7ec4-0ae9-4b3e-b7da-0dd501be17a6)

<br>

![image](https://github.com/user-attachments/assets/28cafa6b-9a6e-4d3f-bceb-d0f7cb6d8ae0)

<br>


![image](https://github.com/user-attachments/assets/df40315c-ad9e-46d1-9338-d94321ae3265)

<br>


<pre><code>https://www.verisign.com/repository/CPS</code></pre>

<br>

![image](https://github.com/user-attachments/assets/237eba3e-f5fe-49ae-92cd-336785198b0b)


<br>

![image](https://github.com/user-attachments/assets/e4a03410-86e1-48b6-a16b-5db38a289cc3)


<br>

![image](https://github.com/user-attachments/assets/d05bced2-0c9e-4933-8649-4d404ef1060e)

<br>

![image](https://github.com/user-attachments/assets/85b0e210-0d32-4b31-b7a8-0f8494a34644)

<br>

![image](https://github.com/user-attachments/assets/4f250caf-7a62-4531-82b0-73bf7ca0a41e)


<br>

![image](https://github.com/user-attachments/assets/dfb595b6-9a85-45f3-9d25-1309fb166bb8)

<br>
<br>

![December 25, 2024, TryHackMe, Retro - Room Completed](https://github.com/user-attachments/assets/a1c87263-0e29-401e-85d2-3bd6c7d92662)


<br>

![December 25, 2024, TryHackMe, Retro - Room Completed - Header and Tasks](https://github.com/user-attachments/assets/92d09524-4ce5-41e1-9a62-9685d1f42d60)

<br>

![December 25, 2024, TryHackMe, Retro - Room Completed - Yearly Activity](https://github.com/user-attachments/assets/8265eec4-9109-4dca-ab32-e2ee8da59688)






