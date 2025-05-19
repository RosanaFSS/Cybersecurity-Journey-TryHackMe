<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Hardening Basics Part 2}}$$</h1>
<p align="center">May 19, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my $$\textcolor{#FF69B4}{\textbf{378}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a><br>
Continue learning about hardening: an easy-level walkthrough. It is Premium: only for subscribers.  Access it clicking <a href="https://tryhackme.com/room/hardeningbasicspart2"</a>here.<br><br>
<img width="1000px" src=""></p>

<br>

<h2>Task 1 . Introduction</h2>
<h3>Introduction</h3>
<p>Welcome to Part 2 of Hardening Basics! While this room can be enjoyed on its own, it is meant to be done in conjunction with Part 1. If you have not done Part 1 yet, I highly recommend you do so.<br><br>

In this room, we will cover the following:<br>

1. SSH and Encryption (Chapter 3)<br>
2. Mandatory Access Control (Chapter 4)
<br>
This was mentioned in Part 1 but in case you did not do that room:
<br>
<br>

There are no questions related to performing tasks on a virtual machine. However, I have provided a semi-configured Ubuntu 18.04 environment for you to play around with while you go through the different tasks. Things that have been configured at a basic level will be:<br>

- Users<br>
- PAM<br>
- Permissions<br>
- Passwords<br><br>

And that's it! I'll leave you to play around as you wish. You may access the machine with the following credentials (if you're coming from Part 1, you do not need to deploy the VM):<br>
<code>spooky:tryhackme</code><br><br>
These will be global credentials that should give you access to do everything you need to.  I will provide other credentials for tasks where I feel it's possible to lock yourself out from a mistake. You can find some optional challenges in Task 15. <br><br>

The hope is that by the end of this room, you'll be able to clearly explain and understand the above topics and apply them to your daily life, or life at work. Whether you're a senior systems administrator or just starting out as a junior, these topics will help you understand what it takes to harden a Linux system.<br><br>

Topics have been chosen from this book. I looked through the table of contents and picked out the ones that would be the most important and allow the room to have the best content while still keeping it within the proper limits. I think the above 4 topics are the best and will give you the most knowledge on how to harden a system. If you have a subscription to O'Reilly through work or school, I suggest checking the book out.</p>

<h3>Disclaimer</h3>
<p>All tasks for this room were completed using Ubuntu 18.04 LTS. That being said, pretty much everything that applies to 18.04 can apply to 20.04 as well. If you take what you learn out of this room and try to apply it in the real world for practice and fun and something does not work, be sure to check the documentation for what you are trying to do. </p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 1.1. <em>Deploy the VM if necessary and let's go!</em><br><a id='1.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>
<br>

<h2>Task 2 . ~~~~~ Chapter 3 Quiz ~~~~~</h2>
<h3>Summary</h3>

<p>I hope you're continuing to learn something new with each chapter. Even if some of this is re-hashing old concepts, maybe there has been some things you've forgotten. We've gone through GPG and encryption, creating SSH keys, and some methods to harden SSH further.<br><br>

Now it's time to complete a little skills check and see how well you understand the material.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>
<br>

> 2.1. <em>Which SSH Protocol version is the most secure?</em><br><a id='2.1'></a>
>> <code><strong>2</strong></code>

<br>

> 2.2. <em>This is a random, arbitrary number, used as the session key, that is used to encrypt GPG.</em><br><a id='2.2'></a>
>> <code><strong>nonce</strong></code>

<br>

> 2.3. <em>Yey/Ney - GPG is based on the OpenPGP standard.</em><br><a id='2.3'></a>
>> <code><strong>Yey</strong></code>

<br>

> 2.4. <em>What is the command to generate your GPG keys?</em><br><a id='2.4'></a>
>> <code><strong>gpg --gen-key</strong></code>

<br>

> 2.5. <em>What is the command to symmetrically encrypt a file with GPG?</em><br><a id='2.5'></a>
>> <code><strong>gpg -c</strong></code>

<br>

> 2.6. <em>What is the command to asymmetrically encrypt a file with GPG?</em><br><a id='2.6'></a>
>> <code><strong>gpg -e</strong></code>

<br>

> 2.7. <em>What is the command to create SSH keys?</em><br><a id='2.7'></a>
>> <code><strong>ssh-keygen</strong></code>

<br>

> 2.8. <em>Where are ssh keys stored in a user's home directory?</em><br><a id='2.8'></a>
>> <code><strong>.ssh</strong></code>

<br>

> 2.9. <em>What option needs to be set to select the type of key to generate for SSH?</em><br><a id='2.9'></a>
>> <code><strong>-t</strong></code>

<br>

> 2.10. <em>The SSH configuration options presented in this chapter were found in what file (full path)?</em><br><a id='2.10'></a>
>> <code><strong>/etc/ssh/sshd_config</strong></code>

<br>
<br>

<h2>Task 3 . GNU Privacy Guard</h2>
<h3> GNU Privacy Guard</h3>
<p>[ ... ]</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>
<br>

> 3.1. <em>No questions</em><br><a id='3.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>
<br>

<h2>Task 4 . Encrypting Your Files</h2>
<h3>Encrypting Your Files with GPG</h3>
<h4>/h4>.Symmetric</h4>
<p>[ ... ]</p>
<br>
<h4>Asymmetric</h4>
<p>[ ... ]</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 4.1. <em>No questions</em><br><a id='4.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>
<br>

<h2>Task 5 . SSh Protocol 1</h2>
<h3>SSH Protocol 1</h3>
<p>[ ... ]</p>
<br>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 5.1. <em>No questions</em><br><a id='5.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>
<br>

<h2>Task 6 . Creating an SSH Key Set</h2>
<h3>Creating SSH Keys</h3>
<p>[ ... ]</p>
<br>
<h3>Copying Using ssh-copy-id</h3>
<p>[ ... ]</p>
<br>
<h3>Copying Manually</h3>
<p>[ ... ]</p>
<h3>Creating Keys with Updated Encryption Algorithms</h3>
<p>[ ... ]</p>
<br>
<h3>RSA</h3>
<p>[ ... ]</p>
<br>
<h3>ECDSA</h3>
<p>[ ... ]</p>
<br>
<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 6.1. <em>No questions</em><br><a id='6.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>
<br>

<h2>Task 7 . Disable Username & Password SSH Login</h2>
<h3>How to Disable Username & Password SSH Login</h3>
<p>[ ... ]</p>
<br>

<br>
<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 7.1. <em>No questions</em><br><a id='7.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>
<br>

<h2>Task 8 . X11 Forwarding & SSH Tunneling</h2>
<h3>﻿X11 Forwarding</h3>
<p>[ ... ]</p>
<br>
<h3>﻿SSH Tunneling</h3>
<p>[ ... ]</p>
<br>
<br>
<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 8.1. <em>No questions</em><br><a id='8.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>
<br>

<h2>Task 9 . Improving SSH Logging</h2>
<h3>Configuring Improved SSH Logging﻿</h3>
<p>A log file is created any time someone logs in with a Protocol that uses SSH. So that would be SSH, SCP, or SFTP.  By default, Ubuntu stores this log file in /var/log/auth.log. It looks something like this</p>
<br>

![image](https://github.com/user-attachments/assets/e6152992-b407-435a-823e-65da518402bf)


<br>

<p>Neat. There's a few different levels of logging that you can find in the man pages of <code>sshd_config</code>.  They are<br>

- QUIET<br>
-FATAL<br>
- ERROR<br>
- INFO<br>
- VERBOSE<br>
- DEBUG1<br>
- DEBUG2<br>
- DEBUG3<br><br>
INFO is the default setting. This is one of the two we would normally care about. The other would be VERBOSE. To change the logging level is actually very simple and is an easy config change. Navigate to <code>/etc/ssh/sshd_config</code> and look for the line that says<br><br>
<code>#LogLevel INFO</code><br><br>
We can uncomment that line and change it to any of the available levels above. And just like that, you'll now see more detailed logs in the /var/log/auth.log file.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 9.1. <em>No questions</em><br><a id='9.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>
<br>

<h2>Task 10 . ~~~~~ Chapter 4: Mandatory Access Control ~~~~~</h2>
<h3>﻿Mandatory Access Control</h3>
<p>﻿Mandatory Access Control (MAC) is a type of Access Control. It goes along with Discretionary Access Control, Role Based Access Control, and Rule Based Access Control. MAC is considered the strongest form of access control due to allowing more control over who has access over what. In a Linux system, there are multiple ways to implement MAC. Two of which being SELinux and AppArmor.  We're going to take a look at AppArmor in this chapter and see how a system administrator or security enthusiast could harden their systems using MAC. </p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 10.1. <em>Have fun!</em><br><a id='10.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>
<br>

<h2>Task 11 . Introduction to <code>AppArmor</code></h2>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 11.1. <em>Have fun!</em><br><a id='11.1'></a>
>> <code><strong>No answer needed</strong></code>


<br>
<br>

<h2>Task 12 . <code>AppArmor</code> Command Line Utilities</h2>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 12.1. <em>Have fun!</em><br><a id='12.1'></a>
>> <code><strong>No answer needed</strong></code>


<br>
<br>

<h2>Task 13 . ~~~~~ Chapter 4 Quiz ~~~~~</h2>
<h3>Summary</h3>
<p>You did it! You've completed every chapter in the room and are now ready for the final quiz. This was a short chapter on AppArmor and Mandatory Access Control. Remember what you've learned and answer the questions!</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 13.1. <em>Where are the AppArmor profiles located?</em><br><a id='13.1'></a>
>> <code><strong>/etc/apparmor.d</strong></code>

<br>

> 13.2. <em>This directory includes partial profiles to be used in your own custom profiles</em><br><a id='13.2'></a>
>> <code><strong>abstractions</strong></code>

<br>

> 13.3. <em>This punctuation mark is REQUIRED at the end of every rule in a profile</em><br><a id='13.3'></a>
>> <code><strong>,</strong></code>

<br>

> 13.4. <em>This AppArmor mode enforces the profiles but also logs them</em><br><a id='13.4'></a>
>> <code><strong>audit</strong></code>

<br>

> 13.5. <em>This command checks the status of AppArmor</em><br><a id='13.5'></a>
>> <code><strong>aa-status</strong></code>

<br>
<br>

<h2>Task 14 . ~~~~~ Chapter 3: SSH and Encryption ~~~~~</h2>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 14.1. <em>No questions</em><br><a id='14.1'></a>
>> <code><strong>No answer needed</strong></code>


<br>
<br>

<h2>Task 15 . Conclusion & Optional Challenges</h2>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 15.1. <em>Have fun!</em><br><a id='15.1'></a>
>> <code><strong>No answer needed</strong></code>


<br>
<br>
