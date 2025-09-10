<h1 align="center">SOC Role in Blue Team</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/41a37fcf-1794-4eea-b36d-9b29558c3e8c"><br>
2025, September 10<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>492</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Discover security roles and learn how to advance your SOC career, starting from the L1 analyst</em>.<br>
Access it <a href="https://tryhackme.com/room/pythonplayground"</a>here.<br>
<img width="1200px" src=""></p>

<h2>Task 1 . Introduction</h2>

<h3>Introduction</h3>
<p>You've learned about a SOC L1 analyst role in the Junior Security Analyst Intro room. But where is it placed in a company structure? Who is overseeing your team? What other security departments exist? Which skills do you need to advance through your career ladder? Let's find out!</p>

<h3>Learning Objectives</h3>
<p>

- Understand the concept and purpose of the Blue Team<br>
- Explore a place of the SOC within the company structure<br>
- Find out about your career path as a SOC L1 analyst.</p>

<h3>Prerequisites</h3>
<p>

- Complete the <a href="https://tryhackme.com/room/jrsecanalystintrouxo">Intro to Cyber Threat Intel</a> room<br>
- Remind yourself of <a href="https://tryhackme.com/room/socfundamentals">Intro to Cyber Threat Intel</a></p>

<p><em>Answer the question below</em></p>

<p>1.1. Let´s find out!<br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 . Security Hierarchy</h2>
<h3>Security Hierarchy</h3>
<p>Cyber security priorities are different for every company.<br>
  
- For law firms, the goal is the privacy of the legal documents.<br>
- For factories, the availability of production lines.<br>
- For hospitals, patient safety.<br>

That's why every company has a unique security approach and security team structure.<br>
Let's take a look at the high-level example of it:</p>

<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/4e5b0bab-9a4f-4298-8888-90c988612b96"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Looking at the diagram above, top executives like the CEO usually focus on global business objectives and don't manage technical aspects. That's why they hire a Chief Information Security Officer (CISO) or a similar role who knows the business needs and can create the most suitable security departments.</p>

<h3>Security Departments</h3>
<p>In tiny companies, the IT department takes the role of securing the company. Small to medium-sized companies may have a generic "Information Security" team that does all sorts of tasks. For this room, we will focus on bigger companies with a CISO overseeing multiple security teams, each handling a specific task. For example:<br>

- <strong>Red Team</strong>: Offensive security experts, pentesters, or ethical hackers who look for security issues<br>
- <strong>GRC Team</strong>: Specialists managing policies and ensuring compliance with regulations like <a href="https://tryhackme.com/room/socfundamentals">PCI DSS</a><br>
- <strong>Blue Team</strong>: Defensive security experts like SOC analysts, engineers, or incident responders</p>

<p><em>Answer the questions below</em></p>

<p>1.1. Let´s find out!<br>
<code>No answer needed</code></p>

<br>
<h2>Task 3 . Meet the Blue Team</h2>



<h2>Task 4 . Advancing SOC Career</h2>



<h2>Task 5 . Final Challenge</h2>



<h2>Task 6 . COnclusion</h2>



<p>Jump in and grab those flags! They can all be found in the usual places (<code>/home/someuser</code> and <code>/root</code>).</p>


<p><em>Answer the questions below</em></p>


<br>
<br>
<h2 align="center">nmap</h2>

```bash
:~/PythonPlayground# nmap -sC -sV -Pn -p- -T4 xx.xxx.xx.xx
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
...
80/tcp open  http    Node.js Express framework
|_http-title: Python Playground!
```

```bash
:~/PythonPlayground# nmap -sC -sV -A -p- -T4 xx.xxx.xx.xx
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp open  http    Node.js Express framework
|_http-title: Python Playground!
```

<p>
