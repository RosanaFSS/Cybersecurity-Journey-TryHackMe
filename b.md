



<br>

<h2>Task 1 . Hardening Basics</h2>
<p>Welcome to the walkthrough for Harden. In this room, we will explore the different ways to protect an Ubuntu 18.04 Server. Tasks will cover a wide range of hardening topics with challenges along the way to prove your mettle and test your knowledge. You can look forward to the following topics:<br>

1. User Accounts<br>
2. Firewall Security<br>
3. SSH and Encryption<br>
4. Mandatory Access Control</p>

<p>There are no questions related to performing tasks on a virtual machine. However, I have provided a semi-configured Ubuntu 18.04 environment for you to play around with while you go through the different tasks. Things that have been configured at a basic level will be:<br>

- Users<br>
- PAM<br>
- Permissions<br>
- Passwords</p>

<p>And that's it! I'll leave you to play around as you wish. You may access the machine with the following credentials:<br><br>
spooky:tryhackme<br><br>
These will be global credentials that should give you access to do everything you need to.  I will provide other credentials for tasks where I feel it's possible to lock yourself out from a mistake. You can find some optional challenges in Part 2 of this room series. <br><br>

The hope is that by the end of this room, you'll be able to clearly explain and understand the above topics and apply them to your daily life, or life at work. Whether you're a senior systems administrator or just starting out as a junior, these topics will help you understand what it takes to harden a Linux system.<br><br>

Topics have been chosen from this book. I looked through the table of contents and picked out the ones that would be the most important and allow the room to have the best content while still keeping it within the proper limits. I think the above 4 topics are the best and will give you the most knowledge on how to harden a system. If you have a subscription to O'Reilly through work or school, I suggest checking the book out.</p>

<h3>Disclaimer</h3>h3>

<p>All tasks for this room were completed using Ubuntu 18.04 LTS. That being said, pretty much everything that applies to 18.04 can apply to 20.04 as well. If you take what you learn out of this room and try to apply it in the real world for practice and fun and something does not work, be sure to check the documentation for what you are trying to do. </p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 1.1. <em>Deploy the VM and let's get started!!</em><br><a id='1.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>

<h2>Task 2 . ~~~~~ Chapter 1: Securing User Accounts ~~~~~</h2>
<h3>Chapter 1: Securing User Accounts</h3>
<p>Managing the users of any system is no small task. The principle of least privilege states that each user should only have enough access to perform their daily tasks. This means that an HR Admin should not have access to the system log files. However, this may mean that an IT Administrator does have access to the HR drive but not necessarily employee information. This chapter will focus on securing your user accounts through the smart configuration of sudo, using complex passwords, disabling root access and locking down home directories.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 2.1. <em>No questions</em><br><a id='2.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>

<h2>Task 3 . The Dangers of Root</h2>
<h3>The Dangers of Root</h3>
<p>The root user is the highest user in a Linux system. They are able to do anything, including modifying system and boot files.  Knowing that, you can see why logging in as root is probably not ideal in most situations.<br><br>

Being on a site like this, you probably use root to utilize the features of your Kali, Parrot, or other hacking Operating System.  In an environment like this, it's completely fine. But in the real world, using root can be and should be viewed as a danger to your system and company.<br><br>

There is a tool in Linux that allows users to use their standard user accounts but still access programs and binaries as if they were root with their standard user passwords. That tool is sudo.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 3.1. <em>No questions</em><br><a id='3.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>

<h2>Task 4 . Sudo (Part 1)</h2>
<h3>What is sudo?</h3>
<p>sudo stands for "super-user do". Sudo allows any non-root user to run applications as root. It's as simple as that.</p>

<h3>Why is sudo Important?</h3>
<p>sudo is important to system administrators because it means they can allow certain users to perform actions with sudo while still having that user keep his/her privileges.<br><br>
Let's say Nick is a Junior System Administrator and he's asked by his senior to perform some tasks. He's asked to:<br>

1. Install a package that the team will need (apt install)<br>
2. Reload the Apache web server after the senior made some configuration changes (systemctl reload apache2)<br><br>
Each of these tasks will require Nick to use sudo before being able to perform them. Doing so will grant him root user privileges for the duration of that program and then returns back to Nick's default privileges.</p>

<h3>Advantages of sudo</h3>
<p>It was touched on above but when sudo is configured correctly, it greatly increases the security of your Linux environment. There are a few advantages it has such as:<br>

- Slowing hackers down. Since the root login will most likely be disabled and your users are properly granted sudo, any attacker will not know which account to go after, thus slowing them down. If they are slowed down enough, they may stop the attack and give up<br>
- Allow non-privileged users to perform privileged tasks by entering their own passwords<br>
- Keeps in line with the principle of least privilege by allowing administrators to assign certain users full privileges, while assigning other users only the privileges they need to complete their daily tasks</p>

<h3>﻿Adding Users to a Predefined Admin Group</h3>
<h4>Method 1</h4>
<p>...</p>

<h4>Method 2</h4>
<p>...</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 4.1. <em>No questions</em><br><a id='4.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>
