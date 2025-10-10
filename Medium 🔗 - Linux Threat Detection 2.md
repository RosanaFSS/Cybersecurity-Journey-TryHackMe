<h1 align="center">Linux Threat Detection 2</h1>
<p align="center">2025, October 9<br>Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>521</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Hack the island of Motunui</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/58b2d9ef-f234-4716-b272-418055a02032"><br>
Access it <a href="https://tryhackme.com/room/linuxthreatdetection2">here</a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/ab286ff8-4316-4d95-9046-336440cac4d5"></p>


<h2>Task 1 . Introduction</h2>
<p>What happens next after threat actors enter the Linux system? What commands do they run, and what goals do they aim to achieve? In this room, you'll find out by exploring common attack techniques, detecting them in logs, and analyzing a real-world cryptominer infection from start to finish.</p>

<h3>Learning Objectives</h3>
<p></p>

- Explore how to identify Discovery commands in logs<br>
- Learn common threats endangering Linux servers<br>
- Know how attackers upload malware onto their victims<br>
- Practice your skills by uncovering a real cryptominer attack</p>

<h3>Prerequisites</h3>
<p>

- Complete the <a href="https://tryhackme.com/room/linuxthreatdetection1">Linux Threat Detection 1</a> room<br>
- Remind yourself of <a href="https://tryhackme.com/room/mitre">MITRE</a> tactics and techniques<br>
- Know basic Linux commands like wget or grep</p>
  
<h3>Lab Access</h3>
<p>Before moving forward, start the lab by clicking the Start Machine button below. The machine will start in split view and will take about two minutes to load. In case the machine is not visible, you can click the Show Split View button at the top of the task. You may need to work as the root user for some tasks. To switch to root on the VM, please run <code>sudo su</code>.</p>

<h3>Set up your virtuala environment</h3>
<p>All machine details can be found at the top of the page.</p>

<h3>Credentials</h3>
<p>Alternatively, you can access the VM from your own VPN-connected machine with the credentials below:<br>

- Username<br>
- Password<br>
- IP address<br>
- Connection via: SSh</p>

<p><em>Answer the question below</em></p>

<p>1.1. I´m ready to learn!<br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 . Discovery Overview</h2>
<h3>Discovery</h3>
<p>Imagine suddenly appearing in a Linux system, and all you see is a command-line interface. Your first question would be about where you are and how you appeared there, right? Interestingly, this is how most Linux breaches start for attackers. This is because botnets usually automate the Initial Access, and human attackers join only when an entry point is ready.</p>

<h3>First Actions</h3>
<p>The first discovery commands threat actors run on the Linux systems are usually the same, no matter which entry point they used and the goal they pursue. The only exception when Discovery is skipped is when the attackers already know their target or simply want to install a cryptominer and exit, no matter who the victim is. Let's see some basic Discovery examples:</p>

<p>As you can see, attackers rely on the same commands you would use. In the next task, you will learn how to tell bad from good, but one specific command should have your attention - whoami. While legitimate applications rarely need this command, adversaries almost always run it first after breaching a service. In fact, your SOC team can even consider creating a detection rule for any whoami execution - there is a high chance you'll catch the attackers!</p>

<p>Open the VM and test some Discovery commands yourself. Follow the instructions below to answer the questions.</p>

<p><em>Answer the questions below</em></p>

<p>2.1. Run <code>systemd-detect-virt</code>code> to detect the system's cloud. What is the command's output you discovered?<br>
<code>amazon</code></p>

```bash
root@thm-vm:/home/ubuntu$ systemd-detect-virt
amazon
```

<p>2.2. Now run <code>ps aux</code>code> and look for EDR or antivirus processes.What is the full path to the detected antimalware binary? Hint: <em>Look for the related keywords like "security", "scan", "edr", "malware".</em><br>
<code>/var/lib/ultrasec/malscan</code></p>

```bash
ubuntu@thm-vm:/home/ubuntu$ ps aux
...
root         620  0.2  2.1 1830368 20244 ?       Ssl  16:35   0:01 /snap/amazon-ssm-agent/11797/amazon-ssm-agent
root         624  0.3  4.0 1849124 38424 ?       Ssl  16:35   0:02 /usr/lib/snapd/snapd
root         627  0.0  0.9  17988  8664 ?        Ss   16:35   0:00 /usr/lib/systemd/systemd-logind
root         629 60.5  0.3   7744  3556 ?        Rs   16:35   7:26 /bin/bash /var/lib/ultrasec/malscan
root         640  0.0  0.2   6148  2072 ttyS0    Ss+  16:35   0:00 /sbin/agetty -o -p -- \u --keep-baud 115200,57600,38400,9600 - vt220
root         647  0.0  0.2   6104  2024 tty1     Ss+  16:35   0:00 /sbin/agetty -o -p -- \u --noclear - linux
...
```

<br>
<br>
<h2>Task 3 . Detection Discovery</h2>
<h3>Specialized Discovery</h3>
<p>After the initial Discovery, threat actors might also utilize more focused commands to achieve their goals: Data stealers look for passwords and secrets to collect, cryptocurrency miners query CPU and GPU information to optimize the mining, and botnet scripts scan the network for new victims. Some malware can also combine all three objectives. For example:</p>

<img width="447" height="258" alt="image" src="https://github.com/user-attachments/assets/fee5ebc0-46ab-4f9d-82f2-cc740e6aefc7" />

<h3>Detecting Discovery</h3>
<p>Detecting Discovery commands is straightforward with auditd or other runtime monitoring tools. First, configure auditd to log the right commands, like those shown in this room. Then, hunt for Discovery using a SIEM or ausearch. But the real challenge is deciding if the commands came from an attacker, a legitimate service, or an IT administrator.</p>

<p>It is very important to get the context of the Discovery commands. For example, it's a red flag when a web server suddenly spawns whoami or when your IT member starts looking for secrets with find and grep. On the other hand, a network monitoring tool is often expected to periodically ping the local network. You can get that context by building a process tree, for example:</p>


```bash
ubuntu@thm-vm:~$ ausearch -i -x whoami # Look for a Discovery command like whoami
type=PROCTITLE msg=audit(08/25/25 16:28:18.107:985) : proctitle=whoami
type=SYSCALL msg=audit(08/25/25 16:28:18.107:985) : arch=x86_64 syscall=execve success=yes exit=0 items=2 ppid=3898 pid=3907 auid=ubuntu uid=ubuntu exe=/usr/bin/whoami

ubuntu@thm-vm:~$ ausearch -i --pid 3898 # Identify its parent process, a lp.sh script
type=PROCTITLE msg=audit(08/25/25 16:28:11.727:982) : proctitle=/usr/bin/bash /tmp/lp.sh
type=SYSCALL msg=audit(08/25/25 16:28:11.727:982) : arch=x86_64 syscall=execve success=yes exit=0 items=2 ppid=3840 pid=3898 auid=ubuntu uid=ubuntu exe=/usr/bin/bash

ubuntu@thm-vm:~$ ausearch -i --ppid 3898 # Look for other processes created by the lp.sh
[Five more commands like "find /home -name *secret*" confirming the script is malicious ]
```

<p>For this task, imagine you received a SIEM alert about a spike in Discovery commands.<br>
The first thing you see is that the itsupport user launched the hostname command.<br>
Can you continue the investigation on the VM and find out what really happened?</p>

<p><em>Answer the questions below</em></p>

<p>3.1. What is the path of the script that initiated the "hostname" command? Hint : <em>Filter the results by "--pid" to identify the parent process</em>.<br>
<code>/home/itsupport/debug.sh</code></p>

```bash
ausearch -i -x hostname
```

```bash
ausearch -i --pid 3772
```

```bash
ausearch -i --pid 3771
```

```bash
root@thm-vm:/home/itsupport$ ls
debugh.sh ...
```

<p>3.2. What was the last Discovery command launched by the script? Hint : <em>Filter the results by "--ppid" to identify all processes spawned by the script</em>.<br>
<code>ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%cpu</code></p>

<img width="1102" height="341" alt="image" src="https://github.com/user-attachments/assets/0c293af4-3001-4eb3-adb0-027c1acb9d6e" />

<br>
<br>
<br>
<p>3.3. Looking at the script content, what's the email of the script author?<br>
<code>greg@tryhackme.thm</code></p>

<img width="1102" height="341" alt="image" src="https://github.com/user-attachments/assets/89a9f9c9-61e6-443d-b6db-ddcf2596c456" />

<br>
<br>
<br>
<h2>Task 4 . Motivation for Attacks</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>4.1. From which domain was the Elastic agent downloaded?<br>
<code>artifacts.elastic.co</code></p>


<br>
<p>4.2. What is the full path to the downloaded "helper.sh" script?<br>
<code>/var/tmp/helper.sh</code></p>

<br>
<p>4.3. Which of the downloaded files is more likely to be malicious: The one downloaded with curl or wget?<br>
<code>curl</code></p>

<img width="1102" height="232" alt="image" src="https://github.com/user-attachments/assets/643cea2c-c238-489c-8903-31e768ea8435" />

<br>
<br>
<br>
<h2>Task 5 . Dota3: First Actions</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>5.1. Which IP address managed to brute-force the exposed SSH? Hint: <em>Look for SSH authentication events as shown in the task content.</em><br>
<code>45.9.148.125</code></p>

<img width="1082" height="82" alt="image" src="https://github.com/user-attachments/assets/86c040f4-e7ab-4562-a239-64d3a292a17e" />

<br>
<br>
<br>
<p>5.2. Which command did the attacker use to list the last logged-in users? Hint: <em>Use auditd and build process tree to list all entered command.</em><br>
<code>last</code></p>

<img width="639" height="28" alt="image" src="https://github.com/user-attachments/assets/39e6d6fa-dc63-4b36-b087-c489b0202585" />

<br>
<br>
<br>
<p>5.3. Which three EDR processes did the attacker look for with "egrep"? Answer Format: Separated by a comma, in alphabetical order.<br>
<code>ds_agent,falcon,sentinel</code></p>

<img width="1099" height="309" alt="image" src="https://github.com/user-attachments/assets/9cf01a3e-6a60-4e98-92db-088bba22b2d8" />

<br>
<br>
<br>
<h2>Task 6 . Dota3: Miner Setup</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>6.1. What is the name of the malicious archive that was transferred via SCP? Hint : <em>Try the "ausearch -i -if [...] | grep proctitle=" command to simplify the output.</em><br>
<code>kernupd.tar.gz</code></p>

<img width="903" height="78" alt="image" src="https://github.com/user-attachments/assets/2d48e9bb-8533-4d29-bf54-efb14b5e7429" />

<br>
<br>
<br>
<p>6.2. What was the full command line of the cryptominer launch? Hint : <em>include the "nohup" command in your answer</em>.<br>
<code>nohup /tmp/.apt/kernupd/kernupd</code></p>

```bash
ausearch i -if audit.log | grep proctitle=nohup
```

<img width="1052" height="127" alt="image" src="https://github.com/user-attachments/assets/98163edc-6fa4-4022-bd6f-a7096b551662" />

<br>
<br>
<br>
<p>6.3. Which IP address range did the attacker scan for an exposed SSH? Answer Example: 10.0.0.1-10.0.0.126. Hint: <em>Closely review the auditd logs. You should see the network scan there!</em><br>
<code>10.10.12.1-10.10.12.10</code></p>

```bash
ausearch i -if audit.log | grep proctitle=nohup
```

<img width="1052" height="127" alt="image" src="https://github.com/user-attachments/assets/98163edc-6fa4-4022-bd6f-a7096b551662" />

<br>
<br>
<h2>Task 7 . Conclusion</h2>
<p>In this room, you learned a lot about "Hack and Forget" attacks on Linux, from the first Discovery commands to the final Impact. You also explored how to detect the attack stages using auditd and authentication logs, and even practiced your skills by uncovering a cryptominer attack!</p>

<h3>Key Takeaways</h3>

<p>

- "Hack and Forget" attacks are usually automated and performed at scale by botnets<br>
- In Linux, all attack stages mostly rely on prebuilt commands like ls, cat, wget, and ssh<br>
- Your best approach in detecting malicious commands is auditd and process tree analysis</p>
<br>

<p><em>Answer the question below</em></p>

<p>7.1. Let´s move on!<br>
<code>No answer needed</code></p>

<br>
<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/fe714ab2-0ab4-4168-8430-26f9175ed824"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/db1c55d1-bf95-4b81-b4d3-508876a27908"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, October</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|9       |Medium 🔗 - Linux Threat Detection 2   | 521    |     103ʳᵈ    |      4ᵗʰ     |     326ᵗʰ    |     3ʳᵈ    | 129,373  |    996    |    76     |
|9       |Medium 🚩 - WWBuddy                    | 521    |     103ʳᵈ    |      4ᵗʰ     |     390ᵗʰ    |     4ᵗʰ    | 129,293  |    995    |    76     |
|8       |Hard 🚩 - Motunui                      | 520    |     103ʳᵈ    |      4ᵗʰ     |     383ʳᵈ    |     4ᵗʰ    | 129,201  |    994    |    76     |
|8       |Easy 🔗 - Man-in-the-Middle            | 520    |     103ʳᵈ    |      4ᵗʰ     |     390ᵗʰ    |     4ᵗʰ    | 129,141  |    993    |    76     |
|7       |Medium 🚩 - Profiles, in progress      | 519    |              |              |              |            | 129,021  |    992    |    76     |
|6       |Medium 🚩 - VulnNet                    | 518    |     105ᵗʰ    |      4ᵗʰ     |     348ᵗʰ    |     5ᵗʰ    | 129,021  |    992    |    76     |
|6       |Easy 🚩 - DearQA                       | 518    |     105ᵗʰ    |      4ᵗʰ     |     333ʳᵈ    |     6ᵗʰ    | 128,991  |    991    |    76     |
|5       |Medium 🚩 - Frank & Herby try again.....| 517   |     106ᵗʰ    |      4ᵗʰ     |     300ᵗʰ    |     5ᵗʰ    | 128,931  |    990    |    76     |
|4       |Medium 🚩 - Frank & Herby make an app  | 516    |     105ᵗʰ    |      4ᵗʰ     |     233ʳᵈ    |     3ʳᵈ    | 128,871  |    989    |    76     |
|4       |Info ℹ️ - OverlayFS - CVE-2021-3493    | 516    |     105ᵗʰ    |      4ᵗʰ     |     235ᵗʰ    |     3ʳᵈ    | 128,841  |    988    |    76     |
|3       |Medium 🚩 - XDR: Operation Global Dagger2| 515  |     104ᵗʰ    |      4ᵗʰ     |     149ᵗʰ    |     3ʳᵈ    | 128,833  |    987    |    76     |
|3       |Medium 🚩 - VulnNet: dotpy             | 515    |     108ᵗʰ    |      4ᵗʰ     |     741ˢᵗ    |    11ˢᵗ    | 128,563  |    986    |    76     |
|2       |Medium 🔗 - Data Exfiltration Detection| 514    |     108ᵗʰ    |      4ᵗʰ     |     521ˢᵗ    |     8ᵗʰ    | 128,503  |    985    |    76     |
|1       |Medium 🔗 - Network Discovery Detection| 513    |     108ᵗʰ    |      4ᵗʰ     |     875ᵗʰ    |     7ᵗʰ    | 128,407  |    984    |    76     |
|1       |Medium 🚩 - Intranet                   | 513    |     108ᵗʰ    |      4ᵗʰ     |    3,357ᵗʰ   |    57ᵗʰ    | 128,335  |    983    |    76     |

</h6></div>

<br>

<p align="center">Global All Time:   103ʳᵈ<br><img width="250px" src="https://github.com/user-attachments/assets/dfd98250-24d7-4999-b07e-5081a30c6dee"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/197e01fd-a40b-414d-9321-6b829f8f8244"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/45d59c58-6a89-4c1b-97dd-a646b89af6e2"><br>
                  Global monthly:     326ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/71bc1758-827c-4b2a-af69-63506e4f2713"><br>
                  Brazil monthly:       3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/db378249-b379-4ece-806b-afa7a27facd1"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
