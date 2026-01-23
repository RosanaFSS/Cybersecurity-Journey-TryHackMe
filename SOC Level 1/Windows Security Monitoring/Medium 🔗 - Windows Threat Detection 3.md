<h1 align="center">Windows Threat Detection 3</h1>
<p align="center">July 24, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>444</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Learn how threat actors manage to maintain access to the breached Windows hosts.</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/fda99b35-131e-4d35-ab55-e4bb8639f122"><br>
Click <a href="https://tryhackme.com/room/windowsthreatdetection3">here </a>to access the TryHackMe walkthrough.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/607fa12b-f404-4e9e-a673-a4f3f0c1b522"></p>

<br>

<h2>Task 1 . Introduction</h2>
<p>What if attackers aren't satisfied with just breaching the host but aim to stay, establish control, and use the system as a starting point for future operations? This room completes your Windows threat detection journey and explores how a compromised host can become part of a larger attack, focusing on three tactics: Command and Control, Persistence, and Impact.</p>

<h3>Learning Objectives</h3>
<p>

- Remind the concept of Command and Control (C2)<br>
- Learn why and how threat actors maintain control of their victims<br>
- Use Windows event logs to uncover various persistence methods<br>
- See how the learned techniques work in a hands-on environment</p>

<h3>Prerequisites</h3>

<p>

- Recall the basics of MITRE tactics and Windows logs<br>
- Complete Windows Threat Detection 1 and 2 rooms<br>
- Be ready to dive deeper into the last stages of Windows attacks</p>

<h3>Lab Access</h3>
<p>Before moving forward, start the lab by clicking the Start Machine button below. The VM will open in split view and will need about 2 minutes to fully load. In case the VM is not visible, you can click the Show Split View button at the top of the page.

<h4>Set up your virtual environment</h4>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting the Target Machine, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.</p>
<p>[ ... ]</p>

<h4>Credentials</h4>
<p>Alternatively, you can access the VM from your own VPN-connected machine with the credentials below:<br>
[ ... ]</p>

 </p>

<br>

<p><em>Answer the question below</em></p>

<p>1.1. Let´s go!<br>
<code>No answer needed</code></p>

<br>

<h2>Task 2 . Command and Control</h2>
<h3>Command and Controle</h3>
<p>You already learned that USB worms and phishing attachments can "infect" the machine. But how do they do it exactly? How do threat actors send the commands and keep control of the victim's host? This task will shed light on this topic and explore the Command and Control (C2) MITRE tactic.</p>

<h3>Attacks Without C2</h3>
<p>In some cases, C2 is not needed at all. For example, threat actors can type their commands directly in the RDP session after an RDP breach. Since this method becomes unavailable as soon as RDP is closed or secured, most threat actors choose to still set up a C2 immediately after the breach.</p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/9647c6bd-9b28-4465-af02-6cadeecc37f0"></p>

<h3>Simplest C2</h3>
<p>For other Initial Access methods, threat actors can't simply use RDP every time they need to run a command, so they need some process that connects back to the attackers and waits for their commands 24/7. In the simplest case, the phishing attachment will be that process and establish the Command and Control channel, like on the CobaltStrike C2 screenshot below.<br>

In more advanced cases, the attachment won't immediately connect back, but rather download an additional C2 malware, hide it in a folder like C:\Temp, and run it as a new stealthy process. This method is beneficial to keep the attack going if the victim decides to delete the original attachment. See how it worked in the recent ransomware cases and during the APT29 phishing campaign.</p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/5fb115c4-4f76-47a6-89f8-39a128031312"></p>

<p>For this task, access the attached VM and detect the C2 setup using Sysmon logs:<br>
C:\Users\Administrator\Desktop\Practice\Task 2\Sysmon.evtx</p>

<p><em>Answer the questions below</em></p>

<p>2.1. Which suspicious archive did the user download?<br>
<code>URGENT!.zip</code></p>

<img width="743" height="150" alt="image" src="https://github.com/user-attachments/assets/6e91833c-f415-47b3-9258-2b934a89671a" />

<br>

<p>2.2. Where did the attackers hide the C2 malware file?<br>
<code>C:\Users\Administrator\AppData\Roaming\update.exe</code></p>

<img width="1276" height="539" alt="image" src="https://github.com/user-attachments/assets/c4d805ba-27fe-4428-aa29-712e74604e24" />

<br>

<p>2.3. What is the domain of the Command and Control server?<br>
<code>route.m365officesync.workers.dev</code></p>

<img width="1266" height="515" alt="image" src="https://github.com/user-attachments/assets/5f4d1bd8-eaeb-4726-894d-d59c45da95f5" />

<br>

<h2>Task 3 . Persistence Overview</h2>
<h3>Persistence Overview</h3>
<p>Data stealer infections usually have a very short lifespan: they breach the victim, collect the data, exfiltrate it, and exit - all within minutes. However, for most other attacks, maintaining access to the victim for days or even months after the Initial Access is vital. The tactic of maintaining reliable, long-term access to the target that can survive reboots and password changes is called Persistence - a big and interesting topic that you will discover soon.</p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/5ca8a7de-3506-40d5-ac2f-e3a0001398bc"></p>

<h3>Persisting via RDP</h3>
<p>Many Windows breaches happen because of the exposed service: RDP with a weak password, a vulnerable mail server, or a misconfigured web app. For such scenarios, the threat actors can access the machine via the same exposed service over and over again until the vulnerability is fixed. Still, threat actors often deploy an additional Persistence method, for example:<br>

- Create an additional hidden vulnerability in the breached service (e.g. a backdoor or a web shell)<br>
-Create a new user (T1136), make it an administrator (T1098), and use it for further RDP logins<br><br>
Let's focus on the second method now and see how you or threat actors can manage users on Windows. The first option is to use the graphical utility by searching for "Computer Management" or by launching lusrmgr.msc. The second option is to use a command line, like in the example below:</p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/87bc9b09-d265-4c8d-8b3a-524b778dc863"></p>

<h3>Detecting Backdoored Users</h3>
<p>It's time to go back to the Security event logs! Every user creation event is logged as Security event ID 4720, which you explored in the Windows Logging for SOC room. Since threat actors can be very creative with naming the backdoored accounts, you should not rely just on detecting suspicious names like "hacker" but rather investigate:<br>

- Who created the account? Can the person confirm the account creation?<br>
- What is the source IP and time of the creator's login? Is it expected?<br>
- Which other suspicious events can you see in the creator's session?</p>

<h4>Making Users Privileged</h4>
<p>Next, a new user by itself won't give the attacker much, as the default user permissions do not allow remote (RDP) logins or grant administrative privileges on the machine. To overcome this, threat actors will add their backdoored account to one of the privileged groups, which is tracked by Security event ID 4732. The most commonly exploited groups are Administrators and Remote Desktop Users.</p>

<h4>Resetting Passwords</h4>
<p>Lastly, in more advanced cases, threat actors may simply reset the password of some old or unused account and use it instead of creating a new one. You can detect it with Security event ID 4724. In summary, below you can see how the described event IDs look like:</p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/cc7f983d-05f3-445b-b87f-94a2c952b219"></p>

<p>For this task, try to detect a persistence via the backdoored user account:<br>
C:\Users\Administrator\Desktop\Practice\Task 3\Security.evtx</p>

<br>

<p><em>Answer the questions below</em></p>

<p>3.1. How many times did the threat actor fail to log in to the Administrator?<br>
<code>6</code></p>

<p>

- Double-clcicked <code>~\Task3\Security.evtx</code> launching <code>Event Viewer</code><br></p>

<img width="1257" height="218" alt="image" src="https://github.com/user-attachments/assets/1c382404-8dd5-4c70-b895-969988322c1e" />

<br>

<p>3.2. After the successful login, which backdoor user did the attacker create?<br>
<code>support</code></p>

<br>

<p>3.3. Which privileged group was the backdoor user added to?<br>
<code>Administrators</code></p>
  
<img width="1242" height="606" alt="image" src="https://github.com/user-attachments/assets/1c2d0cbd-d1cc-4d17-9cd9-481bb47cec46" />

<img width="1254" height="606" alt="image" src="https://github.com/user-attachments/assets/dac58fd3-ed29-4cfb-9c63-ff476f73ee6d" />

<br>

<h2>Task 4 . Persistence: Tasks and Services</h2>
<h3>Malware Persistence</h3>
<p>Persistence via a backdoored user works well if you can remotely log in to it via RDP, but if the attack started through a phishing attack or USB infection, that's not an option. For these scenarios, threat actors need an actively running malware that maintains a connection with their C2 server even after a system reboot. How could they achieve malware persistence?</p>

<h3>Services and Tasks</h3>
<p>Unfortunately for defenders, there are literally a hundred or more methods to persist on a Windows machine. As a SOC L1 or L2 analyst, you don't need to know all of them, but let's start with the two common ones:</p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/b3d36250-1a2e-42fb-9afa-57555de264c4"></p>

<h3>Detecting Services</h3>
<p>Many critical Windows components like DNS client or Security Center are services. You can view services by launching services.msc or searching for "Services", but you need administrative privileges and the sc.exe command to create or modify one.<br>

Threat actors can create their own malicious services that will run the specified program on startup, and they do it very often, as you can read in the MITRE examples. In logs, you can detect malicious services in three ways:<br>

- Detect the launch of the sc.exe create command via Sysmon event ID 1<br>
- Detect service creation via Security event ID 4697 or System event ID 7045<br>
- Detect suspicious processes with a services.exe parent process</p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/c0163bd5-b6ac-4cad-b41f-0afd3aa93e29"></p>

<h3>Detecting Tasks</h3>
<p>Scheduled tasks are another Windows feature heavily used by both the OS and external apps (e.g. to check for updates or make a backup every hour). From GUI, you can manage tasks by launching taskschd.msc or searching for "Task Scheduler". From the command line, you can use the schtasks.exe command.<br>

Unlike services, scheduled tasks are very easy to configure and hide, which is why they are the most common persistence method by threat actors, like in these APT28 and APT41 attacks. Similar to services, you can detect scheduled tasks in three ways:<br>

- Detect the launch of the schtasks.exe /create command via Sysmon event ID 1<br>
- Detect and analyze scheduled task creation events via Security event ID 4698<br>
- Detect suspicious processes with a svchost.exe [...] -s Schedule parent</p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/30c9b9ad-eb52-4c0f-92bd-c62b1436608a"></p>

<p>The attackers left two backdoors and restarted the system.<br>
Can you uncover them all using Security and Sysmon logs?<br>
C:\Users\Administrator\Desktop\Practice\Task 4\</p>

<br>

<p><em>Answer the questions below</em></p>

<p>4.1. Which Windows service was created to persist the Nessie malware?<br>
<code>Data Protection Service</code></p>

<img width="1255" height="674" alt="image" src="https://github.com/user-attachments/assets/4c1253e7-0c51-46e7-be6f-577075b9b690" />

<img width="1078" height="222" alt="image" src="https://github.com/user-attachments/assets/5285caf2-0f20-4058-9494-70597e6e6ccb" />


<br>

<p>4.2. Which scheduled task was created to persist the Troy malware?<br>
<code>AmazonSync</code></p>

<p><code>CommandLine: "C:\Program Files\Common Files\troy.exe" -d</code></p>

<p><code>ParentCommandLine: C:\Windows\system32\svchost.exe -k netsvcs -p -s Schedule</code></p>

<img width="1250" height="664" alt="image" src="https://github.com/user-attachments/assets/93ed5ad3-2683-4661-bc79-c5372152840b" />

<img width="1254" height="652" alt="image" src="https://github.com/user-attachments/assets/579c0b02-7824-4a74-bd36-ec290dca09c4" />

<img width="1908" height="397" alt="image" src="https://github.com/user-attachments/assets/4152f57b-6e1a-4a37-a4a7-0b3e0ecd7563" />

<br>

<p>4.3. What flag do you get after finding and running the Troy malware?<br>
<code>THM{c2_is_on_schedule!}</code></p>

<img width="1496" height="573" alt="image" src="https://github.com/user-attachments/assets/34e62d9f-bef9-4832-8126-558459be1d3c" />

<br>

<h2>Task 5 . Persistence: Run Keys and Startup</h2>
<h3>Run Keys and Startup</h3>
<p>Services and scheduled tasks are typically run on system boot and require administrative privileges to configure. However, what if a program has to run only when a specific user logs in? For such cases, Windows provides a few per-user persistence methods that are actively used by both legitimate tools and malware:</p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/bf5ecc87-b9c9-4de1-994a-6120afb8c48c"></p>

<h3>Detecting Startup</h3>
<p>The startup folder was meant to be an easy way for inexperienced users to configure programs to run on login. You simply open the startup folder, move your program or program shortcut there, and see how it automatically starts upon your future logins. You can access your startup folder via the path below:</p>

```bash
C:\Users\<USER>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\
Or for all users: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp
```

<p>The startup folder is not a common choice for legitimate programs, so usually, the folder is empty. Still, threat actors often put their malware there (Lumma Stealer example), and you can detect it by monitoring file creation events (Sysmon Event ID 11) inside the Startup Folder. Also, note that the programs launched via startup will have an explorer.exe parent, so it may be hard to differentiate them from legitimate user activity or attacks you learned in Windows Threat Detection 1:</p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/78bd510b-ffb5-4ced-80f6-906f7f1f2e4b"></p>

<h3>Detecting Run Keys</h3>
<p>Run key persistence is very similar to the startup folder; they even share a single MITRE technique! The only major difference is how the entries are added there. Instead of just copying the program to the startup folder, you need to create a new value in the "Run" Windows registry and put the path to your program there:</p>

```bash
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
Or for all users: HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run
```

<p>To view the "Run" entries, you can launch the regedit.exe or search for "Registry Editor" and go to the path shown above. To detect the malicious entry from logs, you can monitor registry change events (Sysmon Event ID 13) affecting the Run keys:</p>
  
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/fbe23195-de0e-4836-b9c1-5ffc986301b4"></p>

<p>Use all the tools you know to uncover the newly learned backdoors!<br>
C:\Users\Administrator\Desktop\Practice\Task 5\</p>

<br>

<p><em>Answer the questions below</em></p>

<p>5.1. What is the parent process image of the "Odin" malware?<br>
<code>C:\Windows\explorer.exe</code>

<img width="1251" height="633" alt="image" src="https://github.com/user-attachments/assets/b7a6e0a2-e2c3-43a7-9822-5fb6e94b9900" />

<br>

<p>5.2. What is the last line that the "Odin" malware outputs?<br>
<code>Done doing bad stuff!</code>

<img width="1252" height="671" alt="image" src="https://github.com/user-attachments/assets/8d4e6d8b-44ad-4320-8d4d-c3afbd7d3248" />


<br>

<p>5.3. What flag do you get after finding and running the "Kitten" malware?<br>
<code>THM{persisting_in_basket!}</code>

<img width="1260" height="657" alt="image" src="https://github.com/user-attachments/assets/2794990b-ddcd-456d-9802-15f39f2e9bd4" />

<img width="1826" height="602" alt="image" src="https://github.com/user-attachments/assets/b860fb5a-e22c-4629-9add-8dca5f190584" />

<img width="1839" height="583" alt="image" src="https://github.com/user-attachments/assets/003e5c20-d743-42d4-87fd-0fae6dd39176" />


<br>

<h2>Task 6 . Impact and Threat Detection Recap</h2>
<h3>Need for Persistance</h3>

<p>In the previous tasks, you have learned how threat actors can remain active on the systems. But why would they need it? Why not just steal the data and exit the system before detection? There can be multiple reasons, but the main ones are:<br>

- <strong>Add the host to a botnet and use it for further attacks</strong><br>Like how the Kraken Botnet combines crypto miner, data stealer, and C2 capabilities<br>
- <strong>Spy on the victim as a part of a state-sponsored campaign</strong><br>Like how Volt Typhoon stayed undetected in the US electric grid for nearly a year<br>
- <strong>Use the victim as an entry point to the network, breaching which could take months</strong><br>Like in the case where threat actors spent 29 days breaching a full network
</p>

<h3>Active Directory and Ransomware</h3>
<p>Let's take a closer look at the third point. In most cases, a Windows network means a large Active Directory that brings its own attacks, detections, and threats - the main one being ransomware. Ransomware scares businesses the most. Why? Because it can bring entire companies to a halt, as it did for McLaren hospitals, affecting 743,000 patients. Just imagine seeing your servers encrypted, data stolen, and ransom notes automatically printed on all office printers:</p>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/d4341736-3671-400e-a822-79b7f7cd22b4"></p>

<h3>Threat Detection Recap</h3>
<p>Active Directory and ransomware are complex topics, but all complex attacks start from a simple single breach. In the Windows Threat Detection rooms, you explored how breaches begin, how the attackers steal data, and how they remain undetected for years. You are now ready to use the acquired knowledge to detect and stop the attacks before ransomware causes a disastrous Impact, preferably right after Initial Access. Here is a quick recap of what you've learned so far (highlighted in yellow):</p>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/311da65c-248f-44d9-9f5d-b14a027a410a"></p>


<p><em>Answer the questions below</em></p>

<p>6.1. What is the biggest threat to most corporate Windows networks?<br>
<code>Ransomware</code>

<br>

<p>6.2. At which stage is it best to detect and stop the attack (e.g. Exfiltration)?<br>
<code>Initial Access</code>

<br>

<h2>Task 7. Conclusion</h2>
<p>In this room, you explored Command and Control, Persistence, and Impact - three tactics observed during advanced attack campaigns. You learned why attackers establish C2 channels, how they maintain long-term access using scheduled tasks, startup folders, services, and run keys, and how to detect these actions through Windows event logs.<br>

You are now better equipped to recognize the signs of compromise and are prepared to detect complete attack chains in SIEM or directly on the host. We hope you enjoyed the Windows Threat Detection journey!</p>

<p><em>Answer the question below</em></p>

<p>7.1. Complete the room!<br>
<code>No answer needed</code>

<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/2fc1743b-a841-4dfc-a788-58f379a899f3"><br>
                 <img width="1200px" src="https://github.com/user-attachments/assets/111be419-53c2-40ee-9433-b924ab8bd1cd"></p>

<br>

<h1 align="center">My TryHackMe Journey</h1>
<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 24, 2025     | 444      |     151ˢᵗ    |      5ᵗʰ     |    179ᵗʰ    |     8ᵗʰ    | 116,329  |    873    |    72     |

</div>

<p align="center">Global All Time:   151ˢᵗ<br><img width="400px" src="https://github.com/user-attachments/assets/f3cb3f9e-d24e-4771-9429-b35ccfa18797"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/d6c9e3aa-66b1-4bed-bb60-6a6d16d1aa94"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/873dab1c-6f43-493b-a079-4aa7af8f3abb"><br>
                  Global monthly:    179ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/07f43a1b-c780-49c9-a76f-dfc686155b0f"><br>
                  Brazil monthly:      8ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/650362ec-3832-4ac4-9af0-32fe39f47249"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
<br>
<h1 align="center">Thank you very much ...</h1>
<p><a href="https://tryhackme.com/p/tryhackme">TryHackMe</a> and <a href="https://tryhackme.com/p/TactfulTurtle">TactfulTurtle</a><br>for developinng this experience so that I could sharpen my skills!</p>
