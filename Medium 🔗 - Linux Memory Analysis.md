<h1 align="center">Linux Memory & Network<br><img width="1200px" src="https://github.com/user-attachments/assets/3c611801-4d91-40e8-b35b-a2395cf04ada"></h1>

<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/cd4e5dca-28bb-4fdb-972b-8ebd508fbf9b"><br>
June 12, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure,<br>
part of my <code>402</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br>
Identify C2 traffic & post-exploit activity in Windows memory.<a href="https://tryhackme.com/room/windowsmemoryandnetwork"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/2179ec73-213f-4b57-9115-4ae96682c9b9"></p>

<h2> Task 1 . Introduction</h2>

<p>When investigating a cyber incident, a system's memory is one of the most volatile and revealing sources of evidence. Memory forensics helps uncover valuable information about what was happening on a machine at a specific time, such as running processes, open files, network connections, credentials, and more.<br><br><br>

In this room, we will continue our investigation of the APT attack on the TryHatMe company and look at the footprints that the adversary left behind in the memory of the Linux machine. It is suspected that the adversary got access to the Linux server via lateral movement.</p>

<h3>Prerequisites</h3>

<p>To understand the concepts and technicalities covered in this room, it is expected that the user is well-versed with Volatility and has covered the following rooms:</p>

- Volatility<br>
- Linux Live Analysis<br>
- Windows Memory & User Activity<br>
- Windows Memory & Processes</p>

<h3>Learning Objectives</h3>
<p> In this room, we will examine the footprints of the adversary's actions in the compromised Linux server. Some of the key topics that we will cover are:<br>

- Overview of the Linux and Windows memory layout.<br>
- Learn how to utilize Volatility to investigate Linux memory.<br>
- Learn how to investigate the running processes and network connections and identify the odd ones.</p>

<p>Let's dive in.</p>

<h3 align="left"> Answer the question below</h3>

> 1.1. <em>Continue to the next task.</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

<h2> Task 2 . Scenario Information</h2>
<p>This is the continuation of the scenario covered in the previous rooms. We will focus on the Linux Server compromised via lateral movement in this room. </p>

<h3>Recapping the Scenario</h3>
<p></p>You are part of the incident response team handling an incident at TryHatMe - a company that exclusively sells hats online. You are tasked with analyzing a full memory dump of a potentially compromised Linux host. Before you, another analyst had already taken a full memory dump and gathered all the necessary information from the TryHatMe IT support team. Since this is your first case, you are a bit nervous, but don't worry; a senior analyst will guide you.</p>

<h3>Information Incident THM-0001</h3>

<p>

- On May 5th, 2025, at 07:30 CET, TryHatMe initiated its incident response plan and escalated the incident to us. After an initial triage, our team found a Windows host that was potentially compromised. This led to a full-scale investigation and discovered that the Linux server FS-01 was also compromised along with the Windows machines.<br>
- The details of the host are as follows:<br>
--- Hostname: FS-01<br>
--- OS: Linux 5.15.0-1066<br>
-At 07:45 CET, our analyst Steve Stevenson took a full memory dump of the Windows host and made a hash to ensure its integrity. The memory dump details are:<br>
--- Name: FS-01.mem<br>
--- MD5-hash: c0fbf40989bda765b8edaa41f72d3ee9<br>

<h3>Company Information TryHatMe</h3>
<p>Network Map</p>

![image](https://github.com/user-attachments/assets/618c3a46-443b-4407-bc46-c9439127f4fd)

<p>Let's move on to the next task: Connect to our analysis lab and start to investigate the adversary's footprints in the Linux server's memory.</p>

<h3 align="left"> Answer the question below</h3>

> 2.1. <em>Continue to the next task.</em><br><a id='2.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

<h2> Task 3 . Lab Connection</h2>
<h3>Start Machine</h3>
<p>[ Start Machine ]</p>

<p>Before moving forward, start the lab by clicking the <code>Start Machine</code> button. It will take 3 minutes to load properly. The VM will be accessible on the right side of the split screen. If the VM is not visible, use the blue Show Split View button at the top of the page.<br><br>

Note: The memory image <code>FS-01.mem</code> used in this room is in the <code>/home/ubuntu/Desktop/artifacts/ directory</code>.</p>

<h3 align="left"> Answer the question below</h3>

> 3.1. <em>Continue to the next task.</em><br><a id='3.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

<h2> Task 4 . Memory Overview: Linux vs Windows</h2>
<p>It is important to understand how memory works in Linux before starting to analyze the memory dump. While Linux and Windows utilize RAM for process execution, system caching, and runtime operations, their memory architectures, management, and artifacts differ substantially.<br><br>

This task provides an overview of Linux memory and how it contrasts with Windows memory systems. You’ll learn key concepts such as virtual memory, page tables, memory regions, and how memory appears in forensic dumps.</p>

<h3>Memory</h3>
<p>Memory (RAM) is where active processes and kernel operations are stored during system operation. Both operating systems use virtual memory to give each process the illusion of having its own isolated memory space.<br><br>

However, their memory management models diverge in key areas:</p>

![image](https://github.com/user-attachments/assets/3beadea9-4d83-4f54-bbc0-fd50653ea271)

<h3>How Linux Manages Memory</h3>
<p>

- Physical vs Virtual Memory: Every process is given a virtual address space. Using page tables, the MMU (Memory Management Unit) translates these to physical addresses.<br>
- Memory-mapped Files: Shared libraries and files are loaded into memory using <code>mmap()</code>. This helps in efficient sharing across processes.<br>
- Kernel Memory: Managed separately from normal programs. <br>
- Swap: When RAM is exhausted, less-used memory pages are moved to swap, freeing space.<br><br>

Linux and Windows both use virtual memory, but their internal structures and exposure to forensics tools differ. Linux provides more direct access to live memory views through the <code>/proc</code> filesystem, while Windows relies on kernel-level structures like Virtual Address Descriptors (VADs) to manage memory.
</p>

<h3>Recapping the Process</h3>
<p>A process is a fundamental unit of execution in an operating system. It represents a running instance of a program, including its memory, CPU context, and system resources. While both Linux and Windows support multitasking through processes, they differ significantly in how they structure, manage, and expose process data. Understanding these differences is vital in memory forensics and threat detection. At its core, a process includes a unique process ID (PID), a dedicated memory space, an execution context (like CPU registers and scheduling data), and a set of resources such as open files and network connections. A process consists of:</p>

<p>

- A PID (Process ID): A process ID (PID) is a unique identifier the operating system assigns to every active process. It enables tracking, managing, and referencing a process during its lifecycle.<br><br>
- Memory space: Each process gets its own virtual address space, broken into key regions:<br>
---Code segment: Contains executable instructions.<br>
---Heap: Dynamically allocated memory (e.g., via malloc()).<br>
----Stack: Manages function calls and local variables.<br>
----Memory-mapped files: Files mapped into memory (e.g., shared libraries, config files).<br>
- Execution context (registers, scheduling info): The execution context of a process or thread includes:<br><br>
---Register values: EIP/RIP for instruction pointer and ESP/RSP for stack pointer.<br>
---Program counter: Tracks instruction execution.<br>
---Scheduler metadata: Priority, CPU time, and state (running, sleeping, etc.).<br>
- Open File Descriptors: File descriptors (FDs) are integer handles pointing to open files, sockets, or pipes used by a process. On UNIX-like systems, this includes everything from log files to /dev/null to TCP ports.<br><br>
- Parent/Child Relationships (Process Tree): Processes are organized hierarchically. A parent spawns a child using system calls like fork() (Unix) or CreateProcess() (Windows). This forms a process tree, which is useful for tracing activity lineage.</p>


<p>Processes may spawn other processes, forming parent-child relationships that define process trees. In forensic terms, a process also leaves behind runtime artifacts that help analysts determine what was executed, how it behaved, and what resources it accessed.</p>

<h3>Linux vs Windows: Process Models</h3>
<p>In Linux, each process is internally represented by a structure called task_struct. This kernel-level data structure holds PID, state, memory pointers, CPU usage, and more information. Linux also treats threads as lightweight processes, meaning every thread has its own PID. It is managed similarly to full processes, with specific flags (via the clone() system call) differentiating thread behavior.<br><br>

On Windows, the equivalent structure is EPROCESS, which resides in kernel memory. Unlike Linux, threads in Windows exist as entities within a process; they do not have standalone identifiers visible like Linux threads do.</p>

![image](https://github.com/user-attachments/assets/333ce8ba-0915-4a54-bc2b-a09b66fd8434)

  
<h3>Anatomy of a Linux Process</h3>
<p>Linux offers transparent access to live process information through the /proc pseudo-filesystem. For example:</p>
<p>

- /proc/<pid>/cmdline provides command-line arguments.<br>

- /proc/<pid>/status shows metadata like UID, memory usage, and thread count.<br>

- /proc/<pid>/exe is a symlink to the binary executed.<br>

- /proc/<pid>/maps reveals memory layout.<br>

- /proc/<pid>/fd/ lists open file descriptors.</p>

<p>From a forensic perspective, Linux gives direct access to live process artifacts through the /proc filesystem. Analysts can check memory maps, open files, load libraries, and even inspect a running binary via symbolic links. This transparency is a powerful feature in Linux for live system analysis.</p>

<h3 align="left"> Answer the question below</h3>

> 4.1. <em>Continue to the next task.</em><br><a id='4.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

<h2> Task 5 . Hunting for Suspicious Process</h2>

<h3 align="left"> Answer the questions below</h3>

> 5.1. <em>What is the MD5 hash of the image we are investigating?</em><br><a id='5.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

> 5.2. <em>What is the PID of the suspicious Netcat process?</em><br><a id='5.2'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

> 5.3. <em>What is the name of the suspicious process running from the hidden tmp directory?</em><br><a id='5.3'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

> 5.4. <em>What port number was used while setting up a Python server to transfer files?</em><br><a id='5.4'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

> 5.5. <em>A suspicious process with PID 821 was found running on the system. What is the full path of the process?</em><br><a id='5.4'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>


<br>

<h2> Task 6 . Hunting for Suspicious Network Activities</h2>

<br>

<h2> Task 7 . Hunting for User Activities</h2>

<br>

<h2> Task 8 . Conclusion</h2>


