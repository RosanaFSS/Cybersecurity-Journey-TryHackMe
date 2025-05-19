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

<p>book chosen --> https://learning.oreilly.com/library/view/mastering-linux-security/9781788620307/</p>

<h3>Disclaimer</h3>
<p>All tasks for this room were completed using Ubuntu 18.04 LTS. That being said, pretty much everything that applies to 18.04 can apply to 20.04 as well. If you take what you learn out of this room and try to apply it in the real world for practice and fun and something does not work, be sure to check the documentation for what you are trying to do. </p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 1.1. <em>Deploy the VM if necessary and let's go!</em><br><a id='1.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>

<p>Used <code>ssh</code> with the credentials <code>spooky</code>:<code>tryhackme</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/fe97603d-1ed2-47e6-b66c-9e67523a223d)


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
<h3>GNU Privacy Guard</h3>
<p>To understand what GNU Privacy Guard (GPG) is and does, we need to start with the original encryption system it's based off of; Pretty Good Privacy.</p>
<h4>Overview of Pretty Good Privacy</h4>
<p>Pretty Good Privacy (PGP) is used widely to encrypt and decrypt email by using asymmetrical and symmetrical systems. When you first send your email, it is encrypted with your own public key, as well as a session key, which is a one-time use random number called a nonce. The session key is then encrypted into the public key and sent with the cipher text. To decrypt your email, the receiving end must use their private key in order to discover the session key. The session key combined with the private key are then used to decrypt the cipher text back into the original document.</p>
<p>This is where GPG comes in. GPG is actually directly based off of the OpenPGP standard. GPG comes pre-installed on Ubuntu and comes with several advantages:<br>

- Easy encryption for email and files<br>
- Even the NSA can't crack PGP (https://twitter.com/Snowden/status/878686842631139334?s=20)<br>
- Asymmetric encryption removes the need to provide a password for decrypting or unlocking files thus improving security overall</p>
<br>
<h3>Using GPG</h3>
<h4>Creating GPG Keys</h4>
<p>When you first want to use GPG, it requires you to create your own keys. To do that we use <code>gpg --gen-key</code>.</p>
<p>This process is extremely simple. Once you press Enter after inputting the above command, it will create some files and directories as well as ask for some information:</p>

<br>

![image](https://github.com/user-attachments/assets/8624a276-d56b-4adc-9950-2157354c9653)

<p>I've just entered fake information for this user (the key generation process will still work).<br><br>

Following that, the program will proceed to generate random bytes for the key. It informs the user that</p>

<br>

![image](https://github.com/user-attachments/assets/057270a2-b0bd-4d8e-a8d6-c66308819dc5)

<br>

<p>So go ahead and move your mouse, type some stuff out or engage the disks. I just moved the mouse around...a lot. After quite some time, the process will complete and create another directory in your home directory called <code>.gnugpg</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/645f8e09-805e-4649-bfb5-7a2044c078da)

<br>

<p>You can verify the keys were created with <code>gpg --list-keys</code>.</p>

<br>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 3.1. <em>No questions</em><br><a id='3.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>

<p>Used <code>gpg --gen-key</code><br>
- <code>Real name</code>: <code>Nobody</code><br>
- <code>Email address</gpg></code>:</gpg><code>fake@mail.com</code><br>
- confirmed typing <code>O</code>:<code>Okay</code> and hit <code>ENTER</code>.<BR>
- <code>Passphrase</code>:<code>************</code><br>
- again <code>Passphrase</code>:<code>************</code><br></p>

<br>

![image](https://github.com/user-attachments/assets/e9f2febf-6b96-4377-bc2c-622fe91efb29)

<br>

<p>Used <code>gpg --list-keys</code></p>

<br>

![image](https://github.com/user-attachments/assets/fffc01ef-6db2-4687-b410-79b941da4f9e)


<br>


<h2>Task 4 . Encrypting Your Files</h2>
<h3>Encrypting Your Files with GPG</h3>
<h4>.Symmetric</h4>
<p>[ ... ]</p>
<br>
<h4>Asymmetric</h4>
<p>[ ... ]</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 4.1. <em>No questions</em><br><a id='4.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>

<p>Created a <code>Task4-File.txt</code> and run <code>gpg -c</code> against it to encrypt it.<br>
Typed and confirmed a passphrase.</p>

<br>

![image](https://github.com/user-attachments/assets/ef518214-9f49-41ab-b432-71982ace1acb)


<br>

<p>A <code>Task4-File.gpg</code> was generated.</p>

<br>

![image](https://github.com/user-attachments/assets/ba007259-5510-41e0-aed8-55f2abd78127)

<br>

<p>Used <code>gpg -d </code> against the <code>.gpg</code> file to decrypt the file and visualize what´s inside.</p>

<br>

![image](https://github.com/user-attachments/assets/6440dd17-84cf-4fa0-941d-92d6dfc3a55a)

<br>


<h2>Task 5 . SSh Protocol 1</h2>
<h3>SSH Protocol 1</h3>
<p>In your <code>/etc/ssh/sshd_config</code> file, if you see <br><br>

<code>Protocol 1</code><br>

or <br>

<code>Protocol 1, 2</code><br><br>

you should run far, far away. Just kidding! But really, you'll want to disable Protocol version 1 as soon as possible. It's available to run on Legacy machines but has been compromised and is no longer considered secure. SSH Protocol Version 2 is the current, more secure version of SSH.</p>
<br>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 5.1. <em>No questions</em><br><a id='5.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>
<br>

<h2>Task 6 . Creating an SSH Key Set</h2>
<h3>Creating SSH Keys</h3>
<p>Are you always logging in to SSH with a password? Well, I'm here to tell you to stop. By far, <code>the most secure way to login to SSH is with the use of secure keys</code>. These can be generated by any user and the command will generate their own set of public and private keys to be used with SSH.<br><br>

Like I said - any user can do this. Typically in the user's home directory, they can use the command <code>ssh-keygen</code> to generate their own pair of public and private keys.<br><br>

I've gone ahead and done this as the user nick so you can see what the process looks like if you don't know already.</p>

<br>

![image](https://github.com/user-attachments/assets/94eaeb08-211c-4cce-9266-934af1f71455)

<br>

<p>You can see that the prompts default to creating the keys in a hidden directory called <code>.ssh</code> in nick's home directory. Awesome! But we still can't login to SSH just yet.<br><br>

Remember from our discussion earlier on public and private keys. Well, this command generates them as well. Your public key is for everyone while your private key is for your eyes only. In order to login to the SSH server, we need to share our public key with the remote SSH server. There are a few ways to do this</p>

<h3>Copying Using ssh-copy-id</h3>
<p>The easiest way to copy your ssh keys is by using the simple command <code>ssh-copy-id</code>. All you need to do is do <code>ssh-copy-id username@remote-host</code> and answer the questions and you're done. It's really as easy as that. I don't have a remote server to test this on so I unfortunately cannot demonstrate. To learn more, see Digital Ocean's article for Ubuntu 16.04. It's an older Ubuntu version but the commands are the same.<br><br>
Article link --> https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys-on-ubuntu-1604</p>
<br>
<h3>Copying Manually</h3>
<p>You can copy the keys manually as well. If you still have password access to your remote host, you can perform the following (this should be done as root and after keys have been generated):<br><br>

<code>mkdir -p ~/.ssh</code><br><br>

From here, you'll want to create or modify an <code>authorized_keys</code> file in which you'll place your public key string into in a minute. Once this file is created you can <code>cat /home/user/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys</code> and that will copy the output of your public key into the <code>authorized_keys</code> file.<br><br>

Once that is done, be sure (still as root in this case) to run <code>chmod -R go= ~/.ssh</code> which will recursively (<code>-R</code>) remove group and other permissions on the <code>~/.ssh</code> directory.<br><br>

If, after doing all of this, your remote host is still prompting for a password, be sure to check your permissions. I found that this Stack Exchange article helped me the most. However, that being said, permissions should be set up correctly when using the <code>ssh-keygen</code> command and if you are logged in as root when making the <code>.ssh</code> and <code>authorized_keys</code> directory and file, those permissions should be okay as well.<br><br>
Stack Exchanged article --> https://unix.stackexchange.com/questions/36540/why-am-i-still-getting-a-password-prompt-with-ssh-with-public-key-authentication</p>
<br>
<h3>Creating Keys with Updated Encryption Algorithms</h3>
<p>In the previous task, we used ssh-keygen to create our keys. By default this uses RSA with a 2048 size key. Generally this is pretty okay and fine for day to day going abouts. However, you should be aware that there are other supported encryption algorithms and bit sizes. And this wouldn't be a room about hardening without discussing at least how to create these keys.<br><br>

The U.S. National Institute of Standards and Technology (NIST) are now recommending RSA of at least 3072 bits or an Elliptic Curve Digital Signature Algorithm (ECDSA) key of at least 384 bits.</p>
<br>
<h3>RSA</h3>
<p>To create that modified RSA key, we can use the following command during key generation<br><br>

<code>ssh-keygen -t rsa -b 3072</code><br><br>

The <code>-t</code> option specifies the encryption type and the <code>-b</code> option specifies the bit size.  </p>
<br>
<h3>ECDSA</h3>
<p>By now you probably can guess how you'd go about creating your ECDSA key.<br><br>

<code>ssh-keygen -t ecdsa -b 384</code>

The max key size with ECDSA is 521 bits. However, NIST does not recommend this key size as they could be susceptible to padding attacks. 384 bits is quite strong and although the key size is smaller than RSA's 3072 key size, it's just as strong as RSA while also requiring less computing power, which is a plus.</p>
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
- FATAL<br>
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
<h3>AppArmor</h3>
<p>﻿AppArmor comes preinstalled with Ubuntu so that means no additional tools to install (yay!). Both, AppArmor and SELinux can be used to implement MAC on a Linux system but since we're going over AppArmor in this walkthrough, let's look at some of the benefits of AppArmor.<br><br>

- It can prevent malicious actors from accessing the data on your systems. As a system administrator, this is extremely important; protecting the confidentiality of your data<br>
- Applications have their own profiles thus making it a little easier<br>
- SELinux and AppArmor have the capability to create your own custom profiles but the scripting in AppArmor is a little easier to understand and reduces the learning curve</p>

<h3>AppArmor Configuratuin</h3>
<p>The AppArmor directory is located at <code>/etc/apparmor.d</code>. This directory contains all of the AppArmor profiles. The <code>sbin.dhclient</code> and <code>usr.*</code> files are AppArmor profiles.</p>

<br>

![image](https://github.com/user-attachments/assets/8ed7e581-1d88-4e0b-bdea-f8415ca9c7ae)

<br>

The <code>abstractions</code> directory is a sort of "includes" folder that has partially written profiles that can be used and included in your own profiles. Part of the work has already been done for you. Here is a listing of the <code>abstractions</code> directory

<br>

![image](https://github.com/user-attachments/assets/170ab18d-2e0e-4cf9-b11b-e7b4c66a68eb)

<br>

<p>Lots of things here for you to use in your custom profiles! Let's take a look at one. I've already gone through and checked a lot of these out and I picked one that I think goes over quite a bit. For this example, let's look at the gnupg file.

</p>

![image](https://github.com/user-attachments/assets/dd7f2e52-0110-4ce0-af5a-e0b48f69dfc4)

<br>

<p>You'll notice that each line/rule ends in a comma. This is required syntax (even for the last rule). You'll also notice that each rule has an <code>owner @{HOME}</code> portion for each listing. The <code>@{HOME}</code> is an AppArmor variable that allows the rule to work with any user's home directory. The access methods before the end of the rule are what you'd expect <code>-r</code> for reading, <code>w</code> for writing. These indicate that the AppArmor daemon have those permissions to read and write to that location preceding it. Easy, right? The only one that you may not know is <code>m</code> which indicates that the file can be used for executable mapping - the file can be mapped into memory using <code>nmap</code>. Remember, these are not configured profiles. They are partials meant to be included in custom profiles. The only two profiles upon a fresh install of Ubuntu are the few mentioned earlier, <code>sbin.dhclient</code> and <code>usr.*</code>. There are a few in the <code>lxc</code>  directory and <code>lxc-containers</code>  file but not much.<br><br>

Additional profiles can be installed with <code>sudo apt install apparmor-profiles apparmor-profiles-extra</code>.</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 11.1. <em>Have fun!</em><br><a id='11.1'></a>
>> <code><strong>No answer needed</strong></code>


<br>
<br>

<h2>Task 12 . <code>AppArmor</code> Command Line Utilities</h2>
<h3>AppArmor Command-Line Utilities</h3>
<p>﻿When working with AppArmor, you're going to undoubtedly need to know the commands to interact with it. But before you do that, you should probably know the different modes of AppArmor. A few have direct comparisons to SELinux if you know them already but to make things less confusing, I won't mention the comparisons.<br><br>

To get the AppArmor status, we can enter <code>aa-status</code>. This gives us quite a long output.</p>

<br>

![image](https://github.com/user-attachments/assets/73adcdd1-d950-409f-af4c-d08edd3765c1)

<br>

<p>We can see that AppArmor is indeed loaded and it is currently set to enforce mode. There are 19 profiles loaded. This segues nicely into the different AppArmor modes.<br><br>

- Enforce - Enforces the active profiles<br>
- Complain - Allows processes to perform disallowed actions by the profile and are logged<br>
- Audit - The same as Enforce mode but allowed and disallowed actions get logged to <code>/var/log/audit/audit.log</code> or system log (depending on if <code>auditd</code> is installed)<br><br>
In order to use any of the command-line utilities I'm about to show, you'll need to perform the following, <code>sudo apt install apparmor-utils</code>. This will enable the following commands, <code>aa-enforce</code>, <code>aa-disable</code>, <code>aa-audit</code>, <code<aa-complain</code>.  Let's set the <code>usr.sbin.rsyslogd</code> profile to enforce mode and then check the status</p>

<br>

![image](https://github.com/user-attachments/assets/3bb5d9db-596e-4ab9-b742-9205acbd2bd3)

<br>

<p>From the output you can see that 20 profiles are now loaded which is 1 more than from the previous status we ran.</p>


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
<h3>Chapter 3: SSH and Encryption</h3>
<p>Encryption is a super important topic. Everything needs encryption! Whether its that super secret puppy gif collection, corporate documents, personal documents, even entire hard drives; it can all be encrypted! Understanding how to put encryption into effect and in place at home and work is a vital piece of information to have. It could save your personal files from being compromised or work documents from being stolen.<br><br>

Encryption covers a lot of different things. Just in the Sec+ alone, you cover symmetric and asymmetric encryption, private and public keys, various ciphers, hashing...it's a lot. This is going to be less than that and more focused on encryption as it pertains to Ubuntu and hardening your system/server. So sit back and let's get ready. We're going to cover a lot of things here.  Topics will include:<br>

- GNU Privacy Guard<br>
  - Encrypting files with GPG<br>
- SSH<br>
  - Disabling SSH Protocol 1<br>
  - Creating Keys<br>
  - Disabling username/password logins<br>
  - Configuring SSH encryption<br>
  - More detailed logging<br>
  - Disabling SSH Tunneling<br>
  - Disabling X11 Forwarding<br><br>
  
Let's get started!</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 14.1. <em>No questions</em><br><a id='14.1'></a>
>> <code><strong>No answer needed</strong></code>


<br>
<br>

<h2>Task 15 . Conclusion & Optional Challenges</h2>
<h3>Closing Thoughts﻿</h3>
<p>Well, you made it.  Thanks for sticking around and congratulations on completing this room.  We've gone through a lot and I hope you've learned something that you can take away and implement in your corporate/work environment or home environment or labs.<br><br>

Really, there's so much to cover in terms of hardening.  It was really hard to pick which topics to go over but after a lot of thought, the ones I chose were ultimately the ones I felt that would have the most benefit for the users here on TryHackMe.  We could have an entire room on Firewall hardening and rules and logging and testing (and maybe someone will do that), but I wanted to give a good overview of hardening concepts and best practices.<br><br>

If you're interested in learning more, I highly recommend the book, Mastering Linux Security and Hardening by Donald A. Tevault.  There's just so much I couldn't cover that is explained in great detail in this book.  A lot of the material in this room came from this book.  Check it out.<br><br>

And lastly, it took a lot of research and effort to make this room.  I didn't know about all of the topics covered when I first started.  And I definitely didn't know about all of the secure practices covered.  That being said, I'm only human and if I missed something or if some information here is wrong or misleading, let me know in the Discord or a DM on the site and I'll do my best to fix it.</p>

<h3>Resources﻿</h3>
- https://www.tecmint.com/configure-pam-in-centos-ubuntu-linux/<br>
- https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/4/html/security_guide/s2-wstation-privileges-noroot<br>
- https://help.ubuntu.com/community/IptablesHowTo#Saving_iptables<br>
- https://help.ubuntu.com/community/UFW<br>
- https://manpages.ubuntu.com/manpages/xenial/man5/apparmor.d.5.html<br>
- http://manpages.ubuntu.com/manpages/bionic/man7/PAM.7.html<br>
- https://www.digitalocean.com/community/tutorials/how-to-use-pam-to-configure-authentication-on-an-ubuntu-12-04-vps<br>
- https://linux.die.net/man/8/pam_pwhistory<br>
- https://www.amazon.com/Mastering-Linux-Security-Hardening-intruders/dp/1788620305</p>

<h3>Challenges</h3>
<p>I've set up some challenges for you to try to figure out while you play with the machine. You do not have to do these. They are entirely optional but will help cement the material and commands that you have learned. Enjoy!</p>

<h4>Challenge List</h4>
<p><code>[Easy]</code> Make a User Alias called "ADMINS". Then make a Command Alias called "ADMIN COMMANDS" and assign it some commands. Practice what you learned. Assign it to someone other than spooky. You can test the configuration by trying commands that are not assigned to the alias. You can enter visudo as spooky with sudo.<br><br>

<code>[Medium]</code> Spooky has a group that we talked about that should not be left on. Exploit it (research will be needed for this).<br><br>

<code>[Easy]</code> Spooky has gone and mucked up the firewall. Users outside the organization are reporting that they cannot reach the webpage on port 80. Figure out what he did and make it right! (<code>spooky:tryhackme</code>)<br><br>

<code>[Medium]</code> James has been notified that he needs to change his password as it is too simple. Login as James and change his password. You will need to conform to the following requirements. (<code>james:easy</code>)<br>
- minlen=8<br>
- difok=3<br>
- lcredit=-1<br>
- dcredit=-1<br>
- ucredit=-1<br>
- ocredit=-1<br><br>

<code>[Easy]</code> Using James and Spooky, play around with Gnu Privacy Guard and encrypt and decrypt a file. Try using both, symmetric and asymmetric encryption types. <code>If you did the challenge above and reset James's password, don't forget to write it down and use the new password</code>!<br><br>

<code>[Easy]</code> Configure SSH for Public Key Encryption. You do not need to change or modify anything in <code>/etc/ssh/sshd_config</code>. Test it with spooky. You should not need root login for this. If you need a hint, look in Task 21.</p>


<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 15.1. <em>Have fun!</em><br><a id='15.1'></a>
>> <code><strong>No answer needed</strong></code>


<br>
<br>
