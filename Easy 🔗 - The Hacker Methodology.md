
<p align="center">March 30, 2025</p>
<p align="center">Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{328}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.</p>

<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{The Hacker Methodology}}$$
</h1>
<p align="center">Introduction to the Hacker Methodology.</p>
<p align="center">It is classified as an easy-level walkthrough, and you can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed. Can be accessed clicking <a href=https://tryhackme.com/room/hackermethodology">here</a>.</p> 
                                                              
<p align="center">
  <img width="900px" src="https://github.com/user-attachments/assets/2c0e6a01-afdb-4ce3-9ca2-72b326dc06e2">
</p>

<br>

<h2>Task 1 . Methodology Outline</h2>
<h3>What process does a Hacker follow?</h3>

<p>While you might think that a hacker does whatever he/she wants, it is actually true that professional hackers/penetration tester generally follow an established process to understand and exploit their targets. This ensures that there is consistency between how assessments are performed throughout the industry, and is the methodology that drives assessments.<br>


<h3>The Process that pentesters follow is summarized in the following steps:</h3>

- Reconnaissance<br>
- Enumeration/Scanning<br>
- Gaining Access<br>
- Privilege Escalation<br>
- Covering Tracks<br>
- Reporting<br><br>

<p>In the next sections we will go through each aspect of this process in more detail.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> 1.1. <em>What is the first phase of the Hacker Methodology?</em><a id='1.1'></a>
>> <code><strong>Reconnaissance</strong></code><br>

<br>

<h2>Task 2 . Reconnaissance Overview</h2>
<p>The first phase of the Ethical Hacker Methodology is Reconnaissance.<br>

Reconnaissance is all about collecting information about your target.<br>

Generally speaking, reconnaissance usually involves no interaction with the target(s) or system(s). <br>

Reconnaissance is a pretty simple concept, think about what tools we can use on the internet to gather information about people.<br>

What websites and technology come to mind to gather information about a target organization, technology, or set of individuals?</p>

<p><strong>In this case, lets use the company: SpaceX. Stop here and take 2 minutes to do some research on SpaceX and note down any websites you used to conduct research.</strong></p>

<p align="center"><img width="160px" src="https://github.com/user-attachments/assets/c15eab02-4d84-4186-aa17-a92aa9c0da3d"></p>

<p>Where is the place that you started your research about SpaceX?</p>

<p>Most likely, you started at one of the most useful tools in a Hacker's possession:<br>

- Google<br><br>


Google is an incredibly useful tool, and there is an entire room (Google Dorking Room) to use it effectively to conduct research.<br>

You might have also used websites such as Wikipedia to understand the history of SpaceX, used the company's Twitter/YouTube to see their latest news releases or "sizzle-reels", or even LinkedIn profile to research open company positions and/or the company's organizational structure.<br>

The cool thing is, all of these very simple tools are all valid reconnaissance tools.<br>

<em>You might think hackers use special tools to conduct research (and in some cases that is true), but overall they use simple tools like these to conduct research</em>.<br>

Reconnaissance usually involves using publicly available tools like Google to conduct research about your target.<br>

Even though it may seem simple, reconnaissance is the single most important phase of a penetration test.<br>

There are some specialized tools that we can utilize but for this introduction, it is good to know the following tools. <br>

- Google (specifically Google Dorking)<br>
- Wikipedia<br>
- PeopleFinder.com<br>
- who.is<br>
- sublist3r<br>
- hunter.io<br>
- builtwith.com<br>
- wappalyzer</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 2.1. <em>Who is the CEO of SpaceX?</em><a id='2.1'></a>
>> <code><strong>Elon Musk</strong></code><br>

<br>

> 2.2. <em>Do some research into the tool: sublist3r, what does it list?</em><a id='2.2'></a>
>> <code><strong>subdomains</strong></code><br>

<br>

> 2.3. <em>What is it called when you use Google to look for specific vulnerabilities or to research a specific topic of interest?</em><a id='2.3'></a>
>> <code><strong>Google Dorking</strong></code><br>

<br>

<h2>Task 3 . Enumeration and Scanning Overview</h2>

<p>[ ... ]</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 3.1. <em>What does enumeration help to determine about the target?</em><a id='3.1'></a>
>> <code><strong>Attack Surface</strong></code><br>

<br>

> 3.2. <em>Do some reconnaissance about the tool: Metasploit, what company developed it?</em><a id='3.2'></a>
>> <code><strong>Rapid7</strong></code><br>

<br>

> 3.3. <em>What company developed the technology behind the tool Burp Suite?</em><a id='3.3'></a>
>> <code><strong>portswigger</strong></code><br>

<br>


<h2>Task 4 . Exploitation</h2>


<p>[ ... ]</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> 4.1. <em>What is one of the primary exploitation tools that pentester(s) use?</em><a id='4.1'></a>
>> <code><strong>Metasploit</strong></code><br>

<br>

<h2>Task 5 . Privilege Escalation</h2>

<p>After we have gained access to a victim machine via the exploitation phase, the next step is to escalate privileges to a higher user account. The following accounts are what we try to reach as a pentester:<br>

- In the Windows world, the target account is usually: Administrator or System.<br>
- In the Linux world, the target account is usually: root<br><br>

As you can tell, discovering what Operating System a device is running on is very important to determine how we will escalate our privileges later. Once we gain access as a lower level user, we will try to run another exploit or find a way to become root or administrator.<br>

<code>Privilege escalation can take many, many forms, some examples are</code>:<br>

- Cracking password hashes found on the target<br>
- Finding a vulnerable service or version of a service which will allow you to escalate privilege THROUGH the service<br>
- Password spraying of previously discovered credentials (password re-use)<br>
- Using default credentials<br>
- Finding secret keys or SSH keys stored on a device which will allow pivoting to another machine<br>
- Running scripts or commands to enumerate system settings like 'ifconfig' to find network settings, or the command 'find / -perm
-4000 -type f 2>/dev/null' to see if the user has access to any commands they can run as root<br><br>

These are just some examples of how privilege escalation could work and there are many more ways in which a privilege escalation could take place. Just think of this section of the methodology as getting to a higher-level user account or pivoting to another machine with the ultimate goal to "own" the machine.</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 5.1. <em>In Windows what is usually the other target account besides Administrator?</em><a id='5.1'></a>
>> <code><strong>System</strong></code><br>

<br>

> 5.2. <em>What thing related to SSH could allow you to login to another machine (even without knowing the username or password)?</em><a id='5.2'></a>
>> <code><strong>Keys</strong></code><br>

<br>

<h2>Task 6 . Covering Tracks</h2>
<p>Most professional/ethical penetration testers never have the need to "cover their tracks". However, this is still a phase in the methodology.<br>

You should always have explicit permission from the system owner regarding when the test is happening, how its occurring, and the scope of targets in any penetration test.<br>

Since the rules of engagement for a penetration test should be agreed to before the test occurs, the penetration tester should stop IMMEDIATELY when they have achieved privilege escalation and report the finding to the client. <br>

As such, a professional will never cover their tracks because the assessment was planned to and agreed to beforehand. Although there are multiple tools for covering tracks, I will not talk about any of them in this room. If you are truly curious you may research them yourself.<br>

However, even though you do not cover your tracks, this does not resolve you of liability for your exploitation. Often you will need to assist the IT Administrator or system owner in cleaning up the exploit code that you utilized, and also recommending HOW to prevent the attack in the future.<br>

While ethical hackers rarely have a need to cover their tracks, you still must carefully track and notate all of the tasks that you performed as part of the penetration test to assist in fixing the vulnerabilities and recommending changes to the system owner.</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> 6.1. <em>I read this section!</em><a id='6.1'></a>
>> <code><strong>No answer needed</strong></code><br>

<br>

<h2>Task 7 . Reporting</h2>
<p>The final phase of the pentest methodology is the reporting phase.<br>

This is one of the most important phases where you will outline everything that you found. The reporting phase often includes the following things:<br>

- The Finding(s) or Vulnerabilities<br>
- The CRITICALITY of the Finding<br>
- A description or brief overview of how the finding was discovered<br>
- Remediation recommendations to resolve the finding<br><br>

The amount of reporting documentation varies widely by the type of engagement that the pentester is involved in. A findings report generally goes in three formats:<br>

-Vulnerability scan results (a simple listing of vulnerabilities)<br>
-Findings summary (list of the findings as outlined above)<br>
-Full formal report.<br><br>

As stated before there are many varying levels of documentation for a final written report. Here is how each type of reporting would look in practice. A vulnerability report usually looks like this:</p>

![image](https://github.com/user-attachments/assets/d8d9dd58-adb0-4f3b-8683-1b747302c785)

<br>

<p>A findings summary is usually something like this:<br>
- Finding: SQL Injection in ID Parameter of Cats Page<br>
- Criticality: Critical<br>
- Description: Placing a payload of 1' OR '1'='1 into the ID parameter of the website allowed the viewing of all cat names in the cat Table of the database. Furthermore, a UNION SELECT SQL statement allowed the attacker to view all usernames and passwords stored in the Accounts table.<br>
- Remediation Recommendation: Utilize a Prepared SQL statement to prevent SQL injection attacks<br><br>

A full formal report sample can be found here: https://github.com/hmaverickadams/TCM-Security-Sample-Pentest-Report for your learning convenience. Take a look at this report and use it as a baseline for your own activity!</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> 7.1. <em>What would be the type of reporting that involves a full documentation of all findings within a formal document?</em><a id='7.1'></a>
>> <code><strong>full formal report</strong></code><br>

<br>

> 7.2. <em>What is the other thing that a pentester should provide in a report beyond: the finding name, the finding description, the finding criticality</em><a id='7.2'></a>
>> <code><strong>remediation recommendation</strong></code><br>

<br>
<br>
<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>

<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/f2466fc4-fee4-49e5-984e-f356aa679cd6"> </p>

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>> for investing your time and effort to develop this walkthrough so that I can sharpen my skills!</h1> 


