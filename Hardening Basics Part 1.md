<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Hardening Basics Part 1}}$$</h1>
<p align="center">May 19, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my $$\textcolor{#FF69B4}{\textbf{378}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a><br>
Learn how to harden an Ubuntu Server! Covers a wide range of topics (Part 1): an easy-level walkthrough. You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.  Access it clicking <a href="https://tryhackme.com/room/hardeningbasicspart1"</a>here.<br><br>
<img width="1000px" src="https://github.com/user-attachments/assets/69200fb4-5976-4433-a063-1862037c68c0"></p>

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

<h3>Disclaimer</h3>

<p>All tasks for this room were completed using Ubuntu 18.04 LTS. That being said, pretty much everything that applies to 18.04 can apply to 20.04 as well. If you take what you learn out of this room and try to apply it in the real world for practice and fun and something does not work, be sure to check the documentation for what you are trying to do. </p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 1.1. <em>Deploy the VM and let's get started!!</em><br><a id='1.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>

![image](https://github.com/user-attachments/assets/a2e114f2-2620-48ee-9b3b-8aeffe3b61c3)

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
<br>

<h2>Task 4 . Sudo (Part 1)</h2>
<h3>What is sudo?</h3>
<p><code>sudo</code> stands for "super-user do". Sudo allows any non-root user to run applications as root. It's as simple as that.</p>

<h3>Why is sudo Important?</h3>
<p><code>sudo</code> is important to system administrators because it means they can allow certain users to perform actions with sudo while still having that user keep his/her privileges.<br><br>
Let's say Nick is a Junior System Administrator and he's asked by his senior to perform some tasks. He's asked to:<br>

1. Install a package that the team will need (<code>apt install</code>)<br>
2. Reload the Apache web server after the senior made some configuration changes (<code>systemctl reload apache2</code>)<br><br>
Each of these tasks will require Nick to use sudo before being able to perform them. Doing so will grant him root user privileges for the duration of that program and then returns back to Nick's default privileges.</p>

<h3>Advantages of sudo</h3>
<p>It was touched on above but when sudo is configured correctly, it greatly increases the security of your Linux environment. There are a few advantages it has such as:<br>

- Slowing hackers down. Since the root login will most likely be disabled and your users are properly granted sudo, any attacker will not know which account to go after, thus slowing them down. If they are slowed down enough, they may stop the attack and give up<br>
- Allow non-privileged users to perform privileged tasks by entering their own passwords<br>
- Keeps in line with the principle of least privilege by allowing administrators to assign certain users full privileges, while assigning other users only the privileges they need to complete their daily tasks</p>

<h3>﻿Adding Users to a Predefined Admin Group</h3>
<h4>Method 1</h4>
<p>This is the first way to add users to the sudo group. Generally, this is considered the easiest method to allow users to use the sudo command. On Ubuntu 18.04, unless otherwise specified upon account creation, the user is automatically added to the sudo group. Let's take a look at nick's groups with the <code>groups</code> command.</p>

<br>

![image](https://github.com/user-attachments/assets/6b0c9b8d-b9e0-4d92-8894-b72c5ec8922c)

<br>

<p>We can see that Nick is a part of the sudo group (as well as a few others). If Nick was not part of the sudo group already, we could easily add him with one simple command: <code>usermod -aG</code>. The <code>-aG</code> options here will add Nick to the group sudo. Using the -a option helps Nick retain any previously existing groups. You can also directly add a user to the sudo group upon creation with the command, <code>useradd -G sudo james</code>.<br><br>

But what does adding a user to the sudo group in Ubuntu mean? By default, Ubuntu allows sudo users to execute any program as root with their password. There are a few ways we can check this information. The first way is as Nick with <code>sudo -l</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/d84546f7-e875-4d7c-9c9d-ddc4e8d8b2b7)

<br>

<p>The important information are in the last lines. This is saying that Nick (as part of the sudo group) may run all commands as any user on any machine. <br><br> 

There's another way to view this information and that's with <code>visudo</code>. This opens the sudo policy file. The sudo policy file is stored in /etc/sudoers. We can do it here as Nick, but we would need to use sudo if we want to edit it since it can only be edited by the root user (using just visudo as Nick actually gives a permission denied).</p>

<br>

![image](https://github.com/user-attachments/assets/73b58b68-dcef-426e-ab97-605a87066679)

<br>

<p>This gives the same information as <code>sudo -l</code> but it has one difference; the <code>%sudo</code> indicates that it's for the group, sudo. There are other groups in this file such as "admin". This is where administrators can set what programs a user in a certain group can perform and whether or not they need a password. You may have seen sometimes <code>%sudo ALL=(ALL:ALL) ALL NOPASSWD: ALL</code>. That NOPASSWD part says that the user that is part of the sudo group does not need to enter their local password to use sudo privileges. Generally, this is not recommended - even for home use.</p>


<br>

<h4>Method 2</h4>
<p>This next method utilizes the sudo policy file mentioned in Method 1. It's nice to be able to modify what an entire group can do, but that's just for Ubuntu.  If you're managing users in a network across multiple flavors of Linux (CentOS, Red Hat, etc.), where the sudo group may be called something different, this method may be more preferable.<br><br>

What you can do is add a User Alias to the policy file and add users to that alias (below), or add lines for individual users.  The first image below creates the ADMIN User Alias and assigns 3 users to it and then says that this Alias has full sudo powers.</p>

<br>

![image](https://github.com/user-attachments/assets/c2d22b16-43fc-43bd-a6b8-6d944de5f0fc)

<br>

![image](https://github.com/user-attachments/assets/d479d27f-79e4-498c-b84a-172842578c2d)

<br>


<p>I would not recommend the second option (individual user aliases) in a large network since this can become unwieldy very quickly.﻿ The first option is going to be your best bet as you'll see in the next Task that we can simply add users to this alias and control which commands they have access to with sudo very easily.</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 4.1. <em>No questions</em><br><a id='4.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>

![image](https://github.com/user-attachments/assets/cc475201-4b59-44a3-a26b-7ce6bbab56df)

<br>

<p>Used <code>sudo -l</code> to identify which commands <code>spooky</code> can execute as a <code>sudo user</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/c42e1893-102e-4521-9f15-eb9c7e3f10fa)

<br><br>

<h2>Task 5 . Sudo (Part 2)</h2>
<h3>Setting Up sudo for Only Certain Delegated Privileges</h3>
<h4>Assigning Command Aliases</h4>

<p>﻿In the previous task, we saw how we can add users to the sudo group, and set up a User Alias in the sudo policy file, visudo.<br><br>

I know I've hammered this point a lot in these two tasks, but the next method that we'll talk about here will ensure that users are assigned to the groups they belong to and only are allowed access to the programs they need to complete their daily tasks. This is how sudo aligns with the principle of least privilege.<br><br>

It does this by allowing the root user to set what are called Command Aliases in the sudo policy file. Just as we set a User Alias in this file in the last task, we'll set a Command Alias now in the same file. Since we've already gone over it, I'm going to create another User Alias with the name of SYSTEMADMINS and assign some users to it. So again, using sudo visudo, we'll edit the line under the comment # Cmnd alias specification.<br><br>

We'll just add a few commands to the list. These don't mean anything in the actual context of what a System Admin would need. In reality, a System Admin would probably have sudo access to most things, but for brevity, let's only include a few.</p>

<br>

![image](https://github.com/user-attachments/assets/0602545d-aa11-424f-b914-df20635b00b6)

<br>

![image](https://github.com/user-attachments/assets/5f9fd318-fcb7-494d-9eb5-22f3e589c947)

<br>

<p>The SYSTEM Command Alias allows the user to run systemctl restart, systemctl restart ssh and chmod . What do you think will happen if someone in the SYSTEMADMINS User Alias tried to run systemctl restart apache2? It would fail because that specific service has not been specified in the Alias. However, they are able to restart the ssh service because this is specified. And lastly, they can use chmod with all options.<br><br>

If we wanted to allow the SYSTEMADMINS User Alias to be able to restart all services, we can use a wildcard character at the end so the new Alias would look like /usr/bin/systemctl restart *.</p>

<h4>Different Ways to Assign Commands</h4>
<p>We can also assign Command Aliases to individual users, specific commands to individual users, and Command Aliases to groups:</p>

<br>

![image](https://github.com/user-attachments/assets/36ac50b0-d523-46a8-853d-c93c9d6fa7b2)

<br>

<p>So dark is assigned specifically to the WEBDEV Command Alias, the user paradox is assigned only the cd command (poor Paradox) and the HR User Alias can only perform tasks in the HR Command Alias. See how useful the sudo policy can be in allowing you to separate privileges?</p>

<h4>A Mention of Host Aliases</h4>

<p>Host Aliases exist. They are a way to trickle down a sudo policy across the network and different servers. For example, you may have a MAILSERVERS Host Alias which contains servers mail1 and mail2. This Host Alias has certain users or groups assigned to it like we've demonstrated in these last two tasks and that Host Alias has a Command Alias assigned to it stating which commands those users are able to run.<br><br>

When those users run a command on mail1 or mail2, the server will check the sudo policy file to see if they can do what they're trying to do.<br><br>

I don't want to go into too much detail about it here because in a home environment and small-medium business environments, it probably is just easier to copy the sudo policy file to each server in the network.  This will really only come into play with large enterprise networks and even then they will probably be using one centralized Ansible or other automation in effect.</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 5.1. <em>No questions</em><br><a id='5.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>
<br>

<h2>Task 6 . Disabling Root Access</h2>

<p>[ ... ]</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 6.1. <em>No questions</em><br><a id='6.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>
<br>

<br>
<br>

<h2>Task 7 . Locking Home Directories</h2>
<h3>Quick Note on Locking a User's Home Directory in Ubuntu</h3>
<p>Ubuntu by default sets a new user's home directory permissions to 755 (UMASK of 022). This means that any other user and group can read and write in that user's directory. This is generally not good practice and it's up to the system admin to change this. The UMASK is set in /etc/login.defs so let's take a look at that file real quick.</p>

<br>

![image](https://github.com/user-attachments/assets/e1f0c4ee-ce3c-42e3-ab30-b247086c81a2)

<br>

<p>Specifically, we're looking at the boxed UMASK in this screenshot, but pay attention to the long note that Ubuntu gives. They even state that 077 would be more secure. So changing that here will automatically make any new user's home directory more secure.  Awesome stuff.<br><br>

Note: The resulting permissions that get set are just 777 - UMASK so in this case:<br><br>

777<br><br>

022<br><br>

-------<br><br>

755<br><br>

Since 777 is the numerical equivalent of rwxrwxrwx in Linux, subtracting that from the UMASK, you get the resulting permissions that will be set on a user's home directory and files.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 7.1. <em>No questions</em><br><a id='7.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>

![image](https://github.com/user-attachments/assets/f455a57c-7e18-48d5-bc1a-8f0a2a9e2c12)

<br>
<br>

<h2>Task 8 . Configuring Password Complexity</h2>
<h3>Pwquality</h3>
<p>﻿Pwquality is a PAM module that allows you to configure password complexity requirements for your users. It's fairly easy to install on Ubuntu. You'll do sudo apt-get install libpam-pwquality. Once installed, it automatically adds an entry into the /etc/pam.d/common-password file. The pam.d directory is just another location where PAM adds files for basic services like ssh, basic login, etc.</p>

<br>

![image](https://github.com/user-attachments/assets/6899cb2c-73cc-4dde-9e7b-4bd01dc835aa)

<br>

<p>Remember from before how to read this?  There's a few differences but let's take a look:<br>

- password: module<br>
- requisite: module; states that if the the module fails, the operation is immediately terminated with a failure without invoking other modules<br>
- pam_pwquality.so: checks the pwquality.conf file for the requirements<br>
- retry=3: allows the user to retry their password 3 times before returning with an error<br><br>
If we look at a few lines from the pwquality.conf file found in /etc/security, we can see that there are many options the administrator can set for the password quality.  The lines just need to be uncommented and modified</p>

<br>

![image](https://github.com/user-attachments/assets/bfc12eda-2c65-46b0-a500-e488659b23a7)

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 8.1. <em>No questions</em><br><a id='8.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>
<br>

<h2>Task 9 . Configuring Other Password Requirements</h2>
<h3>Configuring Other Password Requirements</h3>
<p>﻿﻿In the Security world, when we talk about passwords, there's 4 important concepts that relate to passwords. They are:<br>

- Password complexity<br>
- Password length<br>
- Password expiration<br>
- Password history<br><br>
We already covered the first 2 in previous tasks by configuring pwquality for our server. Now let's cover the last 2.</p>

<h4>Password Expiration</h4>
<p>When we open /etc/login.defs, and scroll down to the "Password aging controls" section, we can set password expiration here.  There are a few options:</p>

<br>

![image](https://github.com/user-attachments/assets/9842a8b8-50a0-4723-a42a-268a49e2c90b)

<br>

<p>- <code>PASS_MAX_DAYS</code>: Default 99999; Sets the maximum number of days a password may be used <br>
- <code>PASS_MIN_DAYS</code>: Default 0; Sets the minimum number of days a user must keep their password before changing it<br>
- <code>PASS_WARN_AGE</code>code>: Default 7; Sets the number of days out from expiration that the system will warn the user<br><br>
It is generally considered good practice to have a user's password expire after 90 days with a minimum age of at least 1. We'll get into why when we get to Password History next.</p>

<h4>Password History</h4>
<p>When configuring the password history of any system, it is generally considered best practice to remember the previous 10 passwords. This will ensure that the user's passwords stay different and are not reused. As we talked about above, setting a minimum age of 1 and a password history of 10 means that somebody would need to wait at least 11 days before they're able to get back to their original password. Usually this is enough to dissuade anyone from trying.<br><br>

To configure password history in Ubuntu, we're once again going to look at /etc/pam.d/common-password. Take a look at the screenshot below for a sample configuration</p>

<br>

![image](https://github.com/user-attachments/assets/83a7eaf1-21a5-4823-b94a-1f863880b13d)

<br>

<p>The pwquality line from before has been removed for simplicity. Let's focus on the top line. Again, I'll go through the PAM settings.  <br><br>

Disclaimer: The PAM is not easy to understand. I did a lot of research and reading for any of these tasks where PAM was used.  Some of these explanations are from the documentation of pam.d found here.<br><br>

- <code>password</code>: module type we are referencing<br>
- <code>required</code>: module where failure returns a failure to the PAM-API<br>
- <code>pam_pwhistory.so</code>: module that configures the password history requirements<br>
- <code>remember=2</code>: option for the pam_pwhistory.so module to remember the last n passwords (n = 2). These passwords are saved in /etc/security/opasswd<br>
- <code>retry=3</code>: option for the pam_pwhistory.so module to prompt the user 3 times before returning a failure<br><br>
You may notice a change to the pam_unix.so line below the top one. We make use of use_authtok here and we tell the module to use shadow which will create shadow passwords when updating a user's password.</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 9.1. <em>No questions</em><br><a id='9.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>
<br>

<h2>Task 10 . Dangers of the <code>lxd</code> Group</h2>
<h4>The lxd Group in Ubuntu</h4>
<p>I figure this wouldn't be a room about hardening if I ignore the fact that for whatever reason, Ubuntu places users (unless otherwise specified) into the lxd group. This group is known to be a point of privilege escalation and should be removed from any user that is a part of it.  <br><br>

It's so prevalent that Linux-Smart-Enumeration even checks for it. So, just remove it from any user that has it assigned. Using <code>adduser</code> does not add the user to any predefined groups and should probably be used when adding new users.</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 10.1. <em>No questions</em><br><a id='10.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>
<br>

<h2>Task 11 . ~~~~~ Chapter 1 Quiz ~~~~~</h2>
<h3>Summary</h3>
<p>We've gone through quite a bit of material. And to be honest, I could have included more. There's a lot to securing user accounts in Linux. There's lots of ways to do so and lots of things to think of when preparing to secure user accounts. The material included here only accounts for some of the things you can do. But, overall I feel these are the most important things and the things you'd see on a regular basis if you were a system admin that handles Linux machines.  <br><br>

So take some time to grab a drink, stretch, and re-read some Tasks if you have to. Then let's dive into the questions.</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 11.1. <em>What group are users automatically added to in Ubuntu?</em><br><a id='11.1'></a>
>> <code><strong>sudo</strong></code>

<br>

> 11.2. <em>What would be the command to add an existing user, nick, to the sudo group? You're running as root</em><br><a id='11.2'></a>
>> <code><strong>usermod -aG sudo nick</strong></code>

<br>

> 11.3. <em>What command as a user can we enter to see what we are allowed to execute with sudo?</em><br><a id='11.3'></a>
>> <code><strong>sudo -l</strong></code>

<br>

> 11.4. <em>Where is the sudo policy file stored?</em><br><a id='11.4'></a>
>> <code><strong>/etc/sudoers</strong></code>

<br>

> 11.5. <em>When in visudo and you see %____, what does the % sign indicate that you are dealing with?</em><br><a id='11.5></a>
>> <code><strong>group</strong></code>

<br>

> 11.6. <em>This Alias lets the user assign a name, like "ADMINS" to a group of people </em><br><a id='11.6></a>
>> <code><strong>user</strong></code>

<br>

> 11.7. <em>Which Alias allows you to create a set of commands that you can then assign to a User Alias?</em> Hint : <em>It's abbreviated in visudo, but spell out the whole word</em><br><a id='11.7></a>
>> <code><strong>command</strong></code>

<br>

> 11.8. <em>Yey/Ney - emacs has a shell escape</em><br><a id='11.8></a>
>> <code><strong>Yey</strong></code>

<br>

> 11.9. <em>What is the minimum recommended password length set by NIST?</em><br><a id='11.9></a>
>> <code><strong>8</strong></code>

<br>

> 11.10. <em>When using the pwhistory module, which file will contain the previous passwords for the user?</em><br><a id='11.10></a>
>> <code><strong>opasswd</strong></code>

<br>

> 11.11. <em>What principle states that every user only has enough access to do their daily duties and tasks</em><br><a id='11.11></a>
>> <code><strong>principle of least privilege</strong></code>

<br>
<br>

<h2>Task 12 . ~~~~~ Chapter 1: Firewall Basics ~~~~~</h2>
<h3>Chapter 2: Firewall Basics</h3>
<p>We've covered user account security which is really important. But now let's move into more of the networking side of things with Firewalls.<br><br>

A Firewall by Cisco's definition is a "network security device that monitors incoming and outgoing network traffic and decides whether to allow or block specific traffic based on a defined set of security rules" (Cisco). After reading that, you may think that a Firewall can only be a network device. But, a Firewall actually comes in two different flavors:<br>

1. Host Based<br>
2. Network Based</p>

<br>
<h4>Host-Based</h4>
<p>Host-based Firewalls are just what they sound like - host-based. They are installed on host machines and monitor traffic from that host. Microsoft Windows includes Windows Firewall by default on all of its operating systems.</p>

<br>

![image](https://github.com/user-attachments/assets/7f089657-fae9-409f-9dcc-62043ce0fd02)

<br>

![image](https://github.com/user-attachments/assets/b608291d-50cd-4af5-8fcd-3925f5a3ca75)

<br>

<p>Rules can be configured on the Windows Firewall just like any other. If using a host-based Firewall, system administrators typically will configure the Firewall on the Windows Server which can then act as the Firewall for the entire network.</p>

<br>
<h4>Network Based</h4>

<p>A network based Firewall is more likely the type of Firewall that Cisco was referring to in their definition above. This type of Firewall is commonly a piece of hardware that may have two or more network interface cards.<br><br>

The network based Firewall is placed on the border of the internal network and the open Internet and all traffic will pass through the Firewall before either entering the private network or leaving to the public Internet. Cisco has model lines such as Firepower that are network-based Firewalls and help protect a company from outside (and inside) threats.</p>

<br>

![image](https://github.com/user-attachments/assets/027aeacb-6858-4dc6-9afd-ec764aa32d98)

<h6>A Cisco Firepower Firewall from cisco.com</h6>

<br>

<br>
<h4>A Note on Web Application Firewalls</h4>
<p>You may have heard of the term, "Web Application Firewall" (WAF). This type of device is not to be confused with a network-based Firewall. WAFs are commonly placed in the Demilitarized Zone (DMZ) of a network and help protect the web-server from outside and inside threats. However, you should not only rely on a web-application firewall to protect your entire network. Instead, a network-based Firewall should be added on the border of the network as discussed above to add an additional layer of security.</p>

<br>

<h4>Summary</h4>
<p>We've briefly gone over the two types of Firewalls.  Since this room is focused on Ubuntu and Linux, we're going to cover Linux's host-based Firewall utility called <code>iptables</code>.</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 12.1. <em>No questions</em><br><a id='12.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>
<br>

<h2>Task 13 . iptables</h2>
<h3>iptables</h3>
<p>As hackers, you're probably around Linux a lot, right? So you've probably heard of iptables. But did you know that iptables is not actually the name of Linux's Firewall? In fact, iptables is just one way of interacting with netfilter which every Linux distribution comes with.<br><br>

Ubuntu actually comes with the Uncomplicated Firewall (ufw), which is an easy to use frontend for iptables. We will go over its uses later on in the room.</p>

<br>

<h3>﻿The Four Components of iptables</h3>
<p>iptables actually has 4 different components to it that all come together to give the utility its overall functionality. They are:<br>

- <code>Filter table</code> - offers the basic protection that you'd expect a firewall to provide<br>
- <code>Network Address Translation table</code> - connects the public interwebs to the private networks<br>
- <code>Mangle table</code> - for mangling them packets as they go through the firewall<br>
- <code>Security table</code> - only used by SELinux</p>

<br>

<h3>Getting Familiar with iptables Commands</h3>
<p>To start, let's look at what our iptables look like on Ubuntu. We can do this by doing a <code>sudo iptables -L</code> (iptables must be called as root, so sudo is needed here).</p>

<br>

![image](https://github.com/user-attachments/assets/d56ebd54-180b-4b49-a20f-0e2a04a4a496)

<br>

<p>As you can see from the image, we have no rules! Yikes! This means, that all traffic is allowed in and out of this system. Not good. We'll go over how someone would go about fixing that. Let's briefly explain the Chains that we have here.<br>

- <code>INPUT</code> - packets coming into the firewall<br>
- <code>FORWARD</code> - packets routed to another NIC on the network; for packets on the local network that are being forwarded on.<br>
- <code>OUTPUT</code> - packets going out of the firewall<br><br>
With that out of the way, and without wanting to overwhelm you, let's jump into the next task and go over some ways to correct this iptable.</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 13.1. <em>No questions</em><br><a id='13.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>
<br>

<h2>Task 14 . iptables Configuration</h2>

<p>[ ... ]</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 14.1. <em>No questions</em><br><a id='14.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>
<br>

<h2>Task 15 . Basic Uncomplicated Firequall for Ubuntu & Chapter 2 Quiz</h2>
<h3>Uncomplicated Firewall</h3>
<p>The Uncomplicated Firewall (UFW) is meant to make creating Firewall rules less complicated. It provides a friendly way to create an IPv4 (or v6) based Firewall. By default, UFW is disabled. You can check the status of UFW with sudo ufw status (UFW must be run as root).  To enable UFW, you simply do sudo ufw enable. And to disable you do sudo ufw disable.  Ez-pz.</p>

<h4>Allowing and Denying Ports</h4>
<p>It's actually really easy to allow and deny things with UFW. The basic format is as follows<br><br>

<code>sudo ufw <allow/deny> <port>/<optional: protocol></code><br><br>

So to allow TCP connections on port 9000 we do sudo ufw allow 9000/tcp. Denying something would be just as easy. Let's say we want to deny telnet traffic on port 23.  We'd do sudo ufw deny 23.</p>

<h4>Allowing and Denying Services</h4>
<p>UFW also allows for entering of services instead of ports with sudo ufw <allow/deny> <service name>. For example, allowing SSH would be done with sudo ufw allow ssh. It's really that easy. You can do the same with deny in order to deny a service that you don't to pass through the Firewall.</p>

<h4>Advanced Syntax</h4>
<p>There's more advanced syntax to allow or deny specific IP addresses, ranges or subnets.  We won't cover this here, but if you want to learn more about how to configure UFW, check out https://help.ubuntu.com/community/UFW.</p>

<h3>Chapter 2 Symmary</h3>
<p>I hope you've learned something going through this chapter. We've gone through iptables and ufw, which are the two most common ways to configure a Firewall on an Ubuntu server.<br><br>

Now it's time to complete a little skills check and see how well you understand the material.</p>

<h3>Room Symmary</h3>
<p>This ends Part 1 of this series. Please head to Part 2 to finish the last 2 chapters!</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 15.1. <em>This type of Firewall typically has two NIC cards</em><br><a id='15.1'></a>
>> <code><strong>Network-Based</strong></code>

<br>

> 15.2. <em>This type of Firewall is typically installed on a host computer and rules apply to that specific host only</em><br><a id='15.2'></a>
>> <code><strong>Host-Based</strong></code>

<br>

> 15.3. <em>Web Application Firewalls help add an extra layer of security to your web servers.  Where should these be installed?</em><br><a id='15.3'></a>
>> <code><strong>demilitarized zone</strong></code>

<br>

> 15.4. <em>iptables is not the name of the Linux Firewall.  What is the framework that iptables allows us to interact with?</em><br><a id='15.4'></a>
>> <code><strong>netfilter</strong></code>

<br>

> 15.5. <em>This 3 letter acronym is a set of rules that defines what the Firewall should allow and what it should deny</em><br><a id='15.5'></a>
>> <code><strong>ACL</strong></code>

<br>

> 15.6. <em>Which iptables option allows us to keep track of the connection state?</em><br><a id='15.6'></a>
>> <code><strong>--ctstate</strong></code>

<br>

> 15.7. <em>Which iptable Chain is responsible for packets on the local network that are being carried onwards?</em><br><a id='15.7'></a>
>> <code><strong>Forward</strong></code>

<br>

> 15.8. <em>Which table mashes up the packets as they go through the Firewall?</em><br><a id='15.8'></a>
>> <code><strong>mangle</strong></code>

<br>

> 15.9. <em>What is the last rule that should be added to an access control list?</em><br><a id='15.9'></a>
>> <code><strong>implicit deny</strong></code>

<br>
<br>


<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/77a39478-53bd-4a2f-a9bf-645fa395e1c9"><br>
                   <img width="1000px" src="https://github.com/user-attachments/assets/dff63490-1dfb-487a-9b6b-ed8e09f20392"><br>
                   <img width="1000px" src="https://github.com/user-attachments/assets/dbc97f40-e2cb-4399-880d-57ccc2368029"><br>
                   <img width="1000px" src="https://github.com/user-attachments/assets/5177ef22-c328-4e9a-ad73-d74c8493f0b9"></p>

<br>
<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$</h1>


<div align="center">

| Date<br>          |  Streak<br>|   All Time<br>Global   |   All Time<br>Brazil |  Monthly<br>Global   |  Monthly<br>Brazil   |  SHOGUN<br>points  |   Rooms<br>completed  |  Badges<br> |
| :---------------: | :--------: | :--------------------: | :------------------: | :------------------: | :------------------: | :----------------: | :-------------------: | :---------: |
| May 19, 2025      |     378    |          218ᵗʰ         |            5ᵗʰ       |        169ᵗʰ         |           4ᵗʰ        |       103,349      |             737      |    62       |

</div>

<p align="center"> Global All Time: 218ᵗʰ <br><img width="300px" src="https://github.com/user-attachments/assets/4c073b5f-d3bd-4b5c-9025-5502560ba5a7" alt="Your Image Badge"><br>
                                              <img width="1000px" src="https://github.com/user-attachments/assets/f0b2e8d2-08cd-4bbf-b9c6-d3247efbc034"><br><br>
                   Brazil All Time:   5ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/a274999e-5d84-4532-a58e-e4adb20bb163"><br><br>
                   Global monthly:   169ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/e6c617dc-7804-43c8-9780-c6b69885b530"><br><br>
                   Brazil monthly:    4ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/5142e2e7-7ce2-4f77-8ec7-cc352a4fcb94"><br><br></p>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Thanks for coming!}}$$</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
<br>
<h1 align="center">Thank you very much <a href="https://tryhackme.com/p/Nameless0ne">Nameless0ne</a> <br>for developinng this experience so that I could sharpen my skills!</h1>

