
<p align="center">March 18, 2025</p>
<p align="center">Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{328}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.</p>

<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{Registry Persistance Detection.}}$$
</h1>
<p align="center">Learn to use the AutoRuns PowerShell module to detect persistence mechanisms that use the Registry.</p>
<p align="center">It is classified as an easy-level walkthrough, and you can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed. Can be accessed clicking <a href="https://tryhackme.com/room/registrypersistencedetection">here</a>.</p> 
                                                              
<p align="center">
  <img width="900px" src="">
</p>


<br>

<h2>Task 1 . Intro</h2>

<p>One crucial step that malware does upon successful execution on a target machine is to ensure that it can stay there even after a reboot or removal attempt. This is possible using various techniques, collectively called "malware persistence mechanisms".<br>

This room will give you an overview of these techniques and introduce a tool that can help detect them and aid in removal.</p>

<h3>Learning Objectives</h3>

- Learn how malware persists in a machine<br>
- Learn how malware uses the Registry as a persistence mechanism<br>
- Learn how to use the AutoRuns PowerShell module to detect and remediate persistence mechanisms<br>
- Connecting to the Machine<br>

<p>We will use the Virtual Machine provided to complete the tasks in this room. You can start it in split-screen view by clicking on the green "Start Machine" button on the upper right section of this task. If the VM is not visible, use the blue "Show Split View" button at the top-right of the page. Alternatively, you can connect to</p>
<p>[ Credentials provided by TryHackMe</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> 1.1. <em>Read the above, start the machine, and log in.</em>.<a id='1.1'></a>
>> <code><strong>No answer needed</strong></code><br>


<h2>Task 2 . Intro to Malware Persistance Mechanisms</h2>

<p>The term "malware persistence" can be defined as:<br>

"Behaviors that enable malware to remain on a system regardless of system events, such as reboots."<br>

There are multiple ways malware can gain persistence. The technique/s used vary depending on the targeted operating system, ease of implementation, level of stealthiness, or, sometimes, based on the preference of the malware author. Examples of these techniques would be modifying an operating system's boot sector, installing malicious configurations, or hijacking execution flow.<br>

<code><em>In Windows, the most common and easiest-to-implement technique is the abuse of Windows Registry Run keys.</em></code><br>

The Windows Registry is a database of low-level operating systems and application settings. The Run keys are specific keys within the Registry that contain a path that runs every time a user logs on, and they are listed below:<br>

- HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run - Run path when the current user logs in<br>
- HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run - Run path when any user logs in<br>
- HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce - Run path when the current user logs in, then delete<br>
- HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce - Run path when any user logs in, then delete<br>
To view these keys, open the Registry Editor by searching for "Regedit" on Windows Search or double-clicking on the Regedit icon pinned on the Windows taskbar.<br><br>

This is what the Registry Editor window looks like:</p>

![image](https://github.com/user-attachments/assets/bf98e499-9de0-4812-874f-62ad9f1a79b1)

<br>

<p>If you want to view the value for one of the Run keys, expand the folders and their subfolders until you reach the key you are looking for. For example:<br>

- HKEY_LOCAL_MACHINE > Software > Microsoft > Windows > CurrentVersion > Run</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 2.1. <em>What is the value "Name" of the suspicious registry entry that runs during startup? Include the parenthesis.</em>.<a id='2.1'></a>
>> <code><strong>Default</strong></code><br><br>

![image](https://github.com/user-attachments/assets/256d3491-4dfe-43c7-adec-996483052c03)

<br>

![image](https://github.com/user-attachments/assets/b9df387f-16e5-4ec0-81cc-bbf21f96f113)

<br>


> 2.2. <em>What is the value "Data" of the suspicious registry entry that runs during startup?</em>.<a id='2.2'></a>
>> <code><strong>C:\Users\Administrator\AppData\Local\bd84\24d9.bat</strong></code><br><br>

![image](https://github.com/user-attachments/assets/1f987e7f-480e-458e-be0c-1bc1ce276181)

<br>

![image](https://github.com/user-attachments/assets/e1249e49-e75a-41e4-88ba-f51aa021eb01)



> 2.3. <em>What string is displayed on the console when the suspicious file runs?</em>.<a id='2.3'></a>
>> <code><strong>pleaseletmepersist</strong></code><br><br>

![image](https://github.com/user-attachments/assets/c8ef8c75-2217-49d9-9423-f0b5947312aa)

<br>


<h2>Task 3 . Intro to the AutoRuns PowerShell Module</h2>

<p>As you've seen in the previous task, it is possible to detect the existence of persistence mechanisms in the Registry by manually checking keys. However, other registry keys can be used to establish persistence, and they are not as obvious, making them harder to find. Fortunately, some tools can help us with this problem.<br>

A widely-used tool from Microsoft called AutoRuns checks all possible locations where a program can automatically run on start-up or when a user logs in. This tool does what we need, but it is not the one we'll be using for this room (If you still want to check it out, try the SysInternals room).</p>

![image](https://github.com/user-attachments/assets/0d079083-0eb9-456d-9351-b8d6e16eb9b8)

<p>For this room, we'll use the AutoRuns PowerShell module. It does the same thing as the original AutoRuns tool. Still, it allows us to leverage the benefits of PowerShell scripting and has a baseline feature for comparing current snapshots to previous ones. You'll see why these features are essential later on.<br>

The Windows machine already has the AutoRuns PowerShell module installed. To use it, open PowerShell in Administrator mode by clicking on the PowerShell icon on the Windows Taskbar at the bottom of the screen. Once the PowerShell window appears, type the following to view the available commands:</p>

![image](https://github.com/user-attachments/assets/8e9a561b-35bf-4d8a-ac3f-105c4188b304)

<br>

<p>To learn more about each AutoRuns command, we can use the Get-help cmdlet along with each AutoRun command name as shown below:</p>

![image](https://github.com/user-attachments/assets/9018dbe2-6b8f-4c46-af7a-f6c713d73e68)






<h2>Task 4 . Filtering AutoRuns Entries</h2>

<h2>Task 5 . Comparing to a Baseline</h2>


<h2>Task 6 . Connclusion</h2>

