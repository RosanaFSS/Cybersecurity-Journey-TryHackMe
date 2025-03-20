<h2>Advent of Cyber 3 (2021)
<h2>Day 8, Santa´s Bag of Toys</h2>

<p>McSkidy was notified of some terrible news! Santa's laptop, which he uses to prepare his bag of toys for Christmas, is missing! We believe a minion at the Grinch Enterprise stole it, but we need to find out for sure. It is up to us to determine what actor compromised the laptop and recover Santa's bag of toys!<br>

Unfortunately, The Best Festival Company had minimal monitoring tools on Santa's laptop (he is the boss, after all)! All we have to work with are some PowerShell Transcription Logs we were able to remotely recover just after it went missing. You can find the transcription logs within the SantasLaptopLogs folder on the Desktop of the attached Windows virtual machine.<br>

If you aren't familiar, PowerShell Transcription Logs capture the input and output of Windows PowerShell commands, allowing an analyst to review what happened when. Typically, PowerShell Transcription can be enabled by Group Policy, but another method to turn on this logging is by configuring the Windows Registry.</p>

<p>While you do not have to use these commands for this task, these will turn on PowerShell Transcription Logging for a local host if entered in an Administrator command prompt:<br>

reg add HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\PowerShell\Transcription /v EnableTranscripting /t REG_DWORD /d 0x1 /f<br>
reg add HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\PowerShell\Transcription /v OutputDirectory /t REG_SZ /d C:/ /f<br>
reg add HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\PowerShell\Transcription /v EnableInvocationHeader /t REG_DWORD /d 0x1 /f<br>
The Windows Registry is a large database of operating system settings and configurations. It is organized by "hives", with each hive containing "keys" and their corresponding "values." PowerShell Transcription Logging can be enabled in this way "per-user" via the HKEY_CURRENT_USER registry hive, or across the entire host via the HKEY_LOCAL_MACHINE registry hive. Thankfully, Santa's laptop had this enabled machine-wide!<br>

Note that for this task, you will interact with a Windows virtual machine to perform your analysis. For the sake of storyline, this is not Santa's laptop... rather, you have sample files that were recovered before the laptop was stolen.

<h3>Additional Resources</h3>
<p></p>If you are interested in learning more about the Windows Fundamentals, check out the Windows Fundamentals module on TryHackMe.</p>

<br>

![image](https://github.com/user-attachments/assets/67d84414-d9e4-4068-be03-f10e812305dd)

<br>
<br>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>


> 1.1. <em>Read the premise above, start the attached Windows analysis machine and find the transcription logs in the SantasLaptopLogs folder on the Desktop.</em><br><a id='1.1'></a>
> <em>If you want to RDP into the machine, start the AttackBox and enter the following into a terminal: xfreerdp /u:Administrator /p:grinch123! /v:Target_IP - The credentials for the machine are Administrator as the username, and grinch123! as the password.</em>
>> <code><strong>No answer needed</strong></code><br><br>


<p>Used Remmina.  Entered the credentials provided for this task.</p>

![image](https://github.com/user-attachments/assets/5f293f85-6956-4a96-b019-47173b1830be)

<p>Clicked OK.</p>

![image](https://github.com/user-attachments/assets/039d33d0-04e8-46c7-adc7-b3ff3791d3a3)

<br>

<p>Each transcription log is a simple plain text file that you can open in any editor of your choice. While the filenames are random, you can get an idea as to which log "comes first" by looking at the Date Modified or Date Created attributes, or the timestamps just before the file extension!<br>

Open the first transcription log. You can see the commands and output for everything that ran within PowerShell, like whoami and systeminfo!
</p>

> 1.2. <em>What operating system is Santa's laptop running ("OS Name")?</em><br><a id='1.2'></a>
>> <code><strong>Microsoft Windows Pro</strong></code><br><br>



<p>clicked on <code>SantasLaptopLogs</code></p>

![image](https://github.com/user-attachments/assets/136aa022-49db-4244-8227-1c1c974c12de)

<br>

<p>double-clicked the first file.</p>

![image](https://github.com/user-attachments/assets/3da6119a-00fd-47fb-bb23-e95403c10f6e)

<p>Review each transcription log to get an idea for what activity was performed on the laptop just after it went missing. In the "second" transcription log, it seems as if the perpetrator created a backdoor user account!</p>

> 1.3. <em>What was the password set for the new "backdoor" account?</em><br><a id='1.2'></a>
>> <code><strong>grinchstolechristmas</strong></code><br><br>


![image](https://github.com/user-attachments/assets/a831cd5d-6a0c-4173-a308-ed7e5c858f86)


<p>In one of the transcription logs,  the bad actor interacts with the target under the new backdoor user account, and copies a unique file to the Desktop. Before it is copied to the Desktop,</p>



