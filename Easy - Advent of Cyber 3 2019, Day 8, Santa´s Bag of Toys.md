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


> 1.1. <em>Read the premise above, start the attached Windows analysis machine and find the transcription logs in the SantasLaptopLogs folder on the Desktop.
> If you want to RDP into the machine, start the AttackBox and enter the following into a terminal: xfreerdp /u:Administrator /p:grinch123! /v:Target_IP - The credentials for the machine are Administrator as the username, and grinch123! as the password.</em><a id='1.1'></a>
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

> 1.3. <em>What was the password set for the new "backdoor" account?</em><br><a id='1.3'></a>
>> <code><strong>grinchstolechristmas</strong></code><br><br>


<p>Double-clicked on the third file in the <code>SantasLaptopLogs</code>, and discovered the answer.</p>

![image](https://github.com/user-attachments/assets/a831cd5d-6a0c-4173-a308-ed7e5c858f86)


<p>In one of the transcription logs,  the bad actor interacts with the target under the new backdoor user account, and copies a unique file to the Desktop. Before it is copied to the Desktop,</p>

> 1.4. <em>In one of the transcription logs,  the bad actor interacts with the target under the new backdoor user account, and copies a unique file to the Desktop. Before it is copied to the Desktop, what is the full path of the original file? </em><br><a id='1.4'></a>
>> <code><strong>C:\Users\santa\AppData\Local\Microsoft\Windows\UsrClass.dat</strong></code><br><br>


<p>Double-clicked on the last file in the <code>SantasLaptopLogs</code>, and discovered the answer.</p>

![image](https://github.com/user-attachments/assets/5e7e042e-be37-4dd2-8ec0-ad0ecc63319a)

<br>

> 1.5. <em>The actor uses a Living Off The Land binary (LOLbin) to encode this file, and then verifies it succeeded by viewing the output file. What is the name of this LOLbin?</em><br><a id='1.5'></a>
>> <code><strong>certutil.exe</strong></code><br><br>

<p>Discovered the answer in the same file analyzed in the 1.4.</p>

![image](https://github.com/user-attachments/assets/595af745-6996-4584-bf1f-0fe7c3324aa5)

<br>

<p>[ ... ]</p>

> 1.6. <em>Drill down into the folders and see if you can find anything that might indicate how we could better track down what this SantaRat really is. What specific folder name clues us in that this might be publicly accessible software hosted on a code-sharing platform?</em><br><a id='1.6'></a>
>> <code><strong>No answer needed</strong></code><br><br>

<p>Opened <code>ShellBagsExplorer.exe</code> directory which in located in the Desktop.<br>
Double-clicked <code>ShellBagsExplorer</code>.</p>

![image](https://github.com/user-attachments/assets/b42aa7ce-f56c-4bb3-aff0-38e2e2b179a0)

<br>


> 1.7. <em>Read the above and open the ShellBagsExplorer.exe application found in the folder on your Desktop.</em><br><a id='1.7'></a>
>> <code><strong>No answer needed</strong></code><br><br>

<p>Opened <code>ShellBagsExplorer.exe</code> directory which in located in the Desktop.<br>
Right-clicked <code>ShellBagsExplorer</code>.<br>
Clicked <code>Run as Administrator</code>.</p>

![image](https://github.com/user-attachments/assets/de717f4a-9d2c-417c-a4bf-457b9419e74d)


> 1.8. <em>Drill down into the folders and see if you can find anything that might indicate how we could better track down what this SantaRat really is. What specific folder name clues us in that this might be publicly accessible software hosted on a code-sharing platform?</em><br><a id='1.8'></a>
>> <code><strong>github</strong></code><br><br>

<p>Copied the content <code>santa.data</code> in <code>PowerShell_transcript.LAPTOP.Zw6PA+c4.20211128153734</code> file between <code>----BEGIN CERTIFICATE-----</code> and <code>-----END CERTIFICATE-----</code>.</p>

![image](https://github.com/user-attachments/assets/304f4c29-52fc-41de-b93c-41d8cbd28215)

<br>

![image](https://github.com/user-attachments/assets/6e9a0da8-b129-497b-9235-97197f5089b8)


<br>

<p>Chose <code>Download</code>, type a name for the file, clicked <code>OK</code>, selected <code>Open with</code>, clicked <code>Browse</code>, selected the <code>ShellBagsExplorer.exe</code>.</p>

![image](https://github.com/user-attachments/assets/d463143d-4027-405c-a171-256986e5691b)


<br>


> 1.9. <em>Drill down into the folders and see if you can find anything that might indicate how we could better track down what this SantaRat really is. What specific folder name clues us in that this might be publicly accessible software hosted on a code-sharing platform?</em><br><a id='1.9'></a>
>> <code><strong>github</strong></code><br><br>

![image](https://github.com/user-attachments/assets/9ba25aa6-432c-4ec4-abb2-a470fd7ab01b)

<br>

> 1.10. <em>Additionally, there is a unique folder named "Bag of Toys" on the Desktop! This must be where Santa prepares his collection of toys, and this is certainly sensitive data that the actor could have compromised. What is the name of the file found in this folder? </em><br><a id='1.10'></a>
>> <code><strong>bag_of_toys.zip</strong></code><br><br>

![image](https://github.com/user-attachments/assets/bb25d544-8dcf-4e73-845d-6ceb0649ff30)


<br>

Track down this SantaRat software online. It may be just as simple as searching for the name of the software on the suggested website (Github).

Note that the TryHackMe Windows analysis machine does not have Internet access, so you will need to explore in your own web browser.

> 1.11. <em>What is the name of the user that owns the SantaRat repository? </em><br><a id='1.11'></a>
>> <code><strong>Grinchies</strong></code><br><br>

<p>Used <code>Search</code> in <code>GitHub</code>.</p>

![image](https://github.com/user-attachments/assets/304f8f6d-7f7f-49db-815e-894256ec82b1)

> 1.12. <em>Explore the other repositories that this user owns. What is the name of the repository that seems especially pertinent to our investigation? </em><br><a id='1.12'></a>
>> <code><strong>operation-bag-of-toys</strong></code><br><br>

<p>Used 1.11. to dicover the answer.</p>

![image](https://github.com/user-attachments/assets/1d434f85-e640-44b5-8a5c-ddad5bcb77d5)

<br>

> 1.13. <em>Explore the other repositories that this user owns. What is the name of the repository that seems especially pertinent to our investigation? </em><br><a id='1.13'</a>
>> <code><strong>uharc-cmd-install.exe</strong></code><br><br>

<p>Clicked <code>SantaRat</code>.</p>

![image](https://github.com/user-attachments/assets/b2b02061-f806-46a3-9c6c-476a904a1264)

<br>

<p>Opened one of the <code>SantasLaptopLogs</code>, and discovered about this: <code>PS C:\Users\s4nta\Desktop> C:\Program` Files` `(x86`)\UHARC` CMD\bin\uharc.exe</code></p>

![image](https://github.com/user-attachments/assets/9b1c42dc-8ae0-4c80-b403-62d260d6cc33)

<br>

<p>[ ... ]</p>

> 1.14. <em>Following this, the actor looks to have removed everything from the bag of toys, and added in new things like coal, mold, worms, and more!  What are the contents of these "malicious" files (coal, mold, and all the others)? </em><br><a id='1.14'></a>
>> <code><strong>GRINCHMAS</strong></code><br><br>


<br>


> 1.15. <em>We know that the actor seemingly collected the original bag of toys. Maybe there was a slight OPSEC mistake, and we might be able to recover Santa's Bag of Toys! Review the actor's repository for its planned operations... maybe in the commit messages, we could find the original archive and the password! </em><br><a id='1.15'></a>
>> <code><strong>No answer neeeded</strong></code><br><br>

> 1.16. <em>We know that the actor seemingly collected the original bag of toys. Maybe there was a slight OPSEC mistake, and we might be able to recover Santa's Bag of Toys! Review the actor's repository for its planned operations... maybe in the commit messages, we could find the original archive and the password! </em><br><a id='1.16'></a>
>> <code><strong>TheGrinchiestGrinchmasOfAll</strong></code><br><br>


> 1.17. <em>How many original files were present in Santa's Bag of Toys?</em><br><a id='1.17'></a>
>> <code><strong>228</strong></code><br><br>








