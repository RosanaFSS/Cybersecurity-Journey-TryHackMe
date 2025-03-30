
<p align="center">March 30, 2025</p>
<p align="center">Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{328}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.</p>

<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{Registry Persistance Detection}}$$
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
<p>[ Credentials provided by TryHackMe ]</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> 1.1. <em>Read the above, start the machine, and log in.</em>.<a id='1.1'></a>
>> <code><strong>No answer needed</strong></code><br>

<br>


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

<p>To view these keys, open the Registry Editor by searching for "Regedit" on Windows Search or double-clicking on the Regedit icon pinned on the Windows taskbar.<br>

This is what the Registry Editor window looks like:</p>

![image](https://github.com/user-attachments/assets/bf98e499-9de0-4812-874f-62ad9f1a79b1)

<br>

<p>If you want to view the value for one of the Run keys, expand the folders and their subfolders until you reach the key you are looking for. For example:<br>

- HKEY_LOCAL_MACHINE > Software > Microsoft > Windows > CurrentVersion > Run</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 2.1. <em>What is the value "Name" of the suspicious registry entry that runs during startup? Include the parenthesis.</em>.<a id='2.1'></a>
>> <code><strong>Default</strong></code><br>

<br>

![image](https://github.com/user-attachments/assets/256d3491-4dfe-43c7-adec-996483052c03)

<br>

![image](https://github.com/user-attachments/assets/b9df387f-16e5-4ec0-81cc-bbf21f96f113)

<br>


> 2.2. <em>What is the value "Data" of the suspicious registry entry that runs during startup?</em>.<a id='2.2'></a>
>> <code><strong>C:\Users\Administrator\AppData\Local\bd84\24d9.bat</strong></code><br>

<br>

![image](https://github.com/user-attachments/assets/1f987e7f-480e-458e-be0c-1bc1ce276181)

<br>

![image](https://github.com/user-attachments/assets/e1249e49-e75a-41e4-88ba-f51aa021eb01)

<br>

> 2.3. <em>What string is displayed on the console when the suspicious file runs?</em>.<a id='2.3'></a>
>> <code><strong>pleaseletmepersist</strong></code><br>

<br>

![image](https://github.com/user-attachments/assets/c8ef8c75-2217-49d9-9423-f0b5947312aa)

<br>


<h2>Task 3 . Intro to the AutoRuns PowerShell Module</h2>

<p>As you've seen in the previous task, it is possible to detect the existence of persistence mechanisms in the Registry by manually checking keys. However, other registry keys can be used to establish persistence, and they are not as obvious, making them harder to find. Fortunately, some tools can help us with this problem.<br>

A widely-used tool from Microsoft called AutoRuns checks all possible locations where a program can automatically run on start-up or when a user logs in. This tool does what we need, but it is not the one we'll be using for this room (If you still want to check it out, try the SysInternals room).</p>


<p align="center">
  <img width="160px" src="https://github.com/user-attachments/assets/0d079083-0eb9-456d-9351-b8d6e16eb9b8">
</p>


<p>For this room, we'll use the AutoRuns PowerShell module. It does the same thing as the original AutoRuns tool. Still, it allows us to leverage the benefits of PowerShell scripting and has a baseline feature for comparing current snapshots to previous ones. You'll see why these features are essential later on.<br>

The Windows machine already has the AutoRuns PowerShell module installed. To use it, open PowerShell in Administrator mode by clicking on the PowerShell icon on the Windows Taskbar at the bottom of the screen. Once the PowerShell window appears, type the following to view the available commands:</p>

![image](https://github.com/user-attachments/assets/8e9a561b-35bf-4d8a-ac3f-105c4188b304)

<br>

<p>To learn more about each AutoRuns command, we can use the Get-help cmdlet along with each AutoRun command name as shown below:</p>

![image](https://github.com/user-attachments/assets/0f612d1a-5da7-4dec-ab30-c44b449898c9)

<br>

<p>You can also check out the tool's ReadMe page for more information.<br>
https://github.com/user-attachments/assets/0d079083-0eb9-456d-9351-b8d6e16eb9b8</p>

<br>
<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 3.1. <em>What AutoRun function is used for getting and displaying the auto-run entries?</em>.<a id='3.1'></a>
>> <code><strong>Get-PSAutorun</strong></code><br>

<br>

> 3.2. <em>What AutoRun function is used for creating a baseline file from Autoruns artifact(s)?</em>.<a id='3.2'></a>
>> <code><strong>New-AutoRunsBaseLine</strong></code><br>

<br>

> 3.3. <em>What AutoRun function is used for creating a baseline file from Autoruns artifact(s)?</em>.<a id='3.3'>/a>
>> <code><strong>Compare-AutoRunsBaseLine</strong></code><br>

<br>


<h2>Task 4 . Filtering AutoRuns Entries</h2>
<p>AutoRuns PowerShell has a function called Get-PSAutorun that will list all possible auto-start mechanisms available on the machine. It makes this list by looking at categories like the Registry, Windows services, WMI entries, DLL hijacking, and more. Because of this, the output of the command will return many results that might be challenging if not adequately filtered.</p>

![image](https://github.com/user-attachments/assets/017b3c1a-181a-4ff4-aa17-8286bac08f1a)


<p>Piping the result of the command above to the Out-GridView cmdlet can make the output more readable.</p>

![image](https://github.com/user-attachments/assets/3e9b22b4-4c00-4ab2-93ff-fed2427d05ab)

<br>

<p>The above command will open a new window showing the following output:</p>

![image](https://github.com/user-attachments/assets/0e0f4d45-0c92-4647-a277-c36ef741758b)

<p><em>Note: Wait for a couple of minutes for the tool to finish populating the results</em></p>

<p>The results above list all possible places a program can run on start-up. You can filter the results by specifying keywords in the "Filter" bar at the top of the window. You can also sort the results by clicking on the column headers.<br>

We can specify parameter switches when calling the function to filter the result according to the previously mentioned categories. Open a new PowerShell window, and use the Get-Help command to list the available parameters.</p>

![image](https://github.com/user-attachments/assets/26d38562-0344-4f7a-9556-ec7213f893d7)

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 4.1. <em>What parameter switch is used for filtering for artifacts related to boot execution of images? </em>.<a id='4.1'></a>
>> <code><strong>BootExecute</strong></code><br>

<br>

![image](https://github.com/user-attachments/assets/970a2a60-59c0-4e21-b1e1-50f5c438a8e0)


<br>


> 4.2. <em>How many entries are outputted using the parameter switch from the previous question?</em>.<a id='4.2'></a>
>> <code><strong>1</strong></code><br>

<br>

![image](https://github.com/user-attachments/assets/75e009ca-234f-4a3e-83d3-b24c2d7e4f26)

<br>


> 4.3. <em>What parameter switch is used for filtering for artifacts related to printer driver and status monitors?</em>.<a id='4.3'>/a>
>> <code><strong>PrintMonitorDLLS</strong></code><br>

<br>

![image](https://github.com/user-attachments/assets/6bd2a767-13ed-4c1e-af44-e47a504dd29b)


<br>


> 4.4. <em>How many entries are listed in the output using the parameter switch from the previous question?</em>.<a id='4.4'>/a>
>> <code><strong>5</strong></code><br>

<p>Discovered the answer in 4.3.</p>

<br>

> 4.5. <em>What parameter is used to add a new column to show whether a file is digitally signed?</em>.<a id='4.5'>/a>
>> <code><strong>VerifyDigitalSignature</strong></code><br>

<br>

![image](https://github.com/user-attachments/assets/f586d662-7039-47e2-989e-71db7b0e4fa0)

<br>


> 4.6. <em>Searching all categories, how many entries have the "Signed" column set to "false"?</em>. Hint : Specify the "VerifyDigitalSignature" parameter when calling Get-PSAutorun to get the "Signed" column.<a id='4.6'>/a>
>> <code><strong>3</strong></code><br>

<br>

![image](https://github.com/user-attachments/assets/ca1a3ab1-72a2-4a04-b9f6-1c34ec3cd3b6)

<br>

> 4.7. <em>Try to answer the previous question with just Powershell and without using Out-GridView.</em>.<a id='4.7'>/a>
>> <code><strong>No answer needed</strong></code><br>

<br>

<h2>Task 5 . Comparing to a Baseline</h2>

<p>While filtering via parameter switches helps reduce the output, there is still a lot to go through. This is where the baseline creation and comparison feature of the AutoRuns PowerShell module is helpful, as only the entries that differ from the baseline are shown in the results.<br>

After creating this room's machine, a baseline file was generated and saved in the ~/Documents folder. This file serves as a snapshot of the Registry before the malware ran.</p>

![image](https://github.com/user-attachments/assets/19089202-d2f8-4ab2-b114-8bffc9f69d89)


<p>To check what Registry keys were changed, a new baseline file needs to be created using the New-AutoRunsBaseLine function.</p>

![image](https://github.com/user-attachments/assets/c5605de6-1b86-4633-9f69-5362578569b9)



<p><em>Note: Generating a new baseline file using the code above will take a few minutes. So please be patient.</em><br>
When done, the new baseline file is added to the ~/Documents folder.</p>

![image](https://github.com/user-attachments/assets/5202f5b7-0b83-4022-88c0-39081bc3993c)



<p>The two baseline files can now be compared using the following command:</p>

![image](https://github.com/user-attachments/assets/abfdf3e9-06ed-4d83-8e40-d928d7cc137d)


<p><em>Note:  Make sure there are always two baseline files in the ~/Documents folder when comparing. Delete the other files you do not need to avoid confusion.</em></p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 5.1. <em>There is another suspicious logon Registry entry. What is the full path of this key? </em>.<a id='5.1'></a>
>> <code><strong>______________</strong></code><br>

<br>

![image](https://github.com/user-attachments/assets/8095124d-42ef-4b22-ba10-9ac0990af69b)

<br>

```bash
PS C:\Users\Administrator> Get-PsAutorun -VerifyDigitalSignature |
>> Where { -not($_.isOSbinary)} |
>> New-AutoRunsBaseLine -Verbose
```

<br>

![image](https://github.com/user-attachments/assets/e7fec6ef-c9a6-4b1a-a929-c97157201dd6)



<br>


> 5.2. <em>What is the value item name of the suspicious Registry entry from question #1?</em>.<a id='5.2'></a>
>> <code><strong>_______________</strong></code><br>

<br>

![image](https://github.com/user-attachments/assets/75e009ca-234f-4a3e-83d3-b24c2d7e4f26)

<br>


> 5.3. <em>What is the value data of the suspicious Registry entry from question #1?</em>.<a id='5.3'>/a>
>> <code><strong>____________________</strong></code><br>

<br>




<br>


> 5.4. <em>What is the category that AutoRuns assigned to the entry from question #1?</em>.<a id='5.4'>/a>
>> <code><strong>_______________</strong></code><br>



<br>

> 5.5. <em>What string is displayed on the console when the suspicious file ran?</em>.<a id='5.5'>/a>
>> <code><strong>_______________</strong></code><br>

<br>


<br>



<h2>Task 6 . Connclusion</h2>



