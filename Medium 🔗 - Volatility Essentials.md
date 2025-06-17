<h1 align="center">Volatility Essentials<br><img width="1200px" src="https://github.com/user-attachments/assets/3c611801-4d91-40e8-b35b-a2395cf04ada"></h1>

<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/b3c3953c-b8ca-431d-a83f-83d1adc6dd99"><br>
June 17, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure,<br>
part of my <code>407</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br>
Learn how to perform memory forensics with Volatility!<br>Click <a href="https://tryhackme.com/room/volatilityessentials"</a>here to acces this walkthrough.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/c413eacf-dd51-470b-a064-639f4a5f354b"></p>

<h2> Task 1 . Introduction</h2>

<h3>Set up your virtual environment</h3>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting the Task Machine, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.</p>

<p>[  Target machine  ]</p>

<p>In the previous room, Memory Analysis Introduction, we learnt about the vital nature of memory forensics in cyber security. We explored the structure of memory dumps, differentiated between RAM and disk forensics, and saw scenarios where memory analysis is essential.<br>
Here, we shall begin looking at the practical aspects of memory forensics through tools, specifically Volatility.</p>

<h3>Learning Objectives</h3>
<p>

- Getting familiar with the Volatility Framework<br>
- Navigate and utilise basic Volatility commands and plugins<br>
- Conduct forensic analysis to identify key artefacts such as running processes and loaded DLLs using Volatility.</p>

<h3>Prerequisites</h3>

<p>

- <a href="https://tryhackme.com/room/memoryanalysisintroduction">Memory Analysis Introduction</a><br>
- <a href="https://tryhackme.com/room/btwindowsinternals">Core Windows Processes</a></p>

<h3 align="left"> Answer the question below</h3>

> 1.1. <em>Ready to learn about Volatility and memory analysis.</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

<h2>Task 2 . Volatility Overview</h2>

<p><a href="https://volatilityfoundation.org/the-volatility-framework/">Volatility</a> is an open-source memory forensics framework that is cross-platform, modular, and extensible. The framework has undergone various iterations over the years, with the current version being Volatility 3. This version is superior to its predecessors as it abandoned static OS profiling in favour of dynamic symbol resolution, supporting newer operating systems, memory layouts, and complete insight into the runtime state of the system.</p>

<h3>Architectural Overview</h3>

<p>Volatility 3 is made up of several key layers:<br>

- <code>Memory layers</code>: These layers represent the hierarchy of address spaces, from raw memory to virtual address translations.<br>
- <code>Symbol tables</code>: The tables enable kernel and process structures to be interpreted through OS-specific debugging symbols.<br>
- <code>Plugins</code>: These are modular routines that leverage the underlying memory layers and symbol tables to extract artefacts of forensic interest. Later in the room, we shall look at some key plugins used.</p>

<h3>System Requirements and Installation</h3>
<p>Volatility 3 requires Python 3.6 or later to run. Additionally, it benefits from various libraries such as <code>pefile</code>, <code>capstone</code>, and <code>yata-python</code> that allow us to process portable executables, perform memory disassembly, and use YARA rules in our analysis, respectively. The terminal output below shows how to install Volatility by cloning the <a href="https://github.com/volatilityfoundation/volatility3.git">GitHub Repository</a> and running it directly from the source.<br>
Volatility has already been installed on the machine attached to this room and can be accessed under the <code>Desktop/volatility3</code> directory.</p>

<p><em>Volatility Installation</em></p>

```bash
ubuntu@tryhackme:~/Desktop$ git clone https://github.com/volatilityfoundation/volatility3.git
ubuntu@tryhackme:~/Desktop$ cd volatility3
ubuntu@tryhackme:~/Desktop/volatility3$ python3 vol.py -h
Volatility 3 Framework 2.26.2
usage: vol.py [-h] [-c CONFIG] [--parallelism [{processes,threads,off}]] [-e EXTEND] [-p PLUGIN_DIRS] [-s SYMBOL_DIRS] [-v] [-l LOG] [-o OUTPUT_DIR] [-q]
              [-r RENDERER] [-f FILE] [--write-config] [--save-config SAVE_CONFIG] [--clear-cache] [--cache-path CACHE_PATH] [--offline | -u URL]
              [--filters FILTERS] [--hide-columns [HIDE_COLUMNS ...]] [--single-location SINGLE_LOCATION] [--stackers [STACKERS ...]]
              [--single-swap-locations [SINGLE_SWAP_LOCATIONS ...]]
              PLUGIN ...

An open-source memory forensics framework

options:
  -h, --help            Show this help message and exit, for specific plugin options use 'vol.py  --help'
  -c CONFIG, --config CONFIG
                        Load the configuration from a json file
------TRUNCATED--------
```

<h3 align="left"> Answer the question below</h3>

> 2.1. <em>Read the above and navigate to the Volatility directory.</em><br><a id='2.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

<h2>Task 3 . Memory Acquisition and Analysis</h2>
<h3>Memory Acquisition Methodologies</h3>
<p>Memory acquisition is a foundational step in forensics that must be performed in a manner that ensures we maintain the integrity of evidence. The process and the deployment environment used vary from one OS to another.</p>

<p>For Windows systems, the following tools can be used to conduct memory acquisition:<br>

- <code>DumpIt</code>: captures a full physical memory image on 32/64‑bit Windows and automatically hashes the output.<br>
- <code>WinPmem</code>: Open‑source driver‑based tool that acquires RAM in RAW/ELF formats and embeds acquisition metadata for chain‑of‑custody.<br>
- <code>Magnet RAM Capture</code>: GUI‑driven collector that snapshots volatile memory on live Windows hosts while minimising footprint.<br>
- <code>FTK Imager</code>: The most common commercial tool that acquires memory and selected logical artefacts alongside disk imaging functions. </p>

<p>For Linux and macOS systems,  we can employ the services of the following tools:<br>

- <code>AVML</code>: Lightweight Microsoft CLI utility that dumps Linux memory to a compressed ELF file without requiring a kernel module.<br>
- <code>LiME</code>: Loadable Kernel Module for Linux that captures full volatile memory over disk or network and supports ARM/x86 architectures.<br>
- <code>OSXPmem</code>: macOS‑specific fork of Pmem that creates raw memory images on Intel‑based Macs for subsequent Volatility analysis.</p>

<h5 align="center"><img width="600px" src="https://github.com/user-attachments/assets/5aa0c2b1-b716-45aa-9f64-e6d6898a7187"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h5>

<p>Extracting memory from virtual environments can be done by collecting the virtual memory file from the host machine's drive. Depending on the hypervisor in use, the output file will likely differ, and you would likely encounter the following examples:<br>

- VMware - <code>.vmem</code><br>
- Hyper-V - <code>.bin</code><br>
- Parallels - <code>.mem</code><br>
- VirtualBox - <code>.sav</code> It is worth noting that this is a partial memory file. </p>

<h3>Memory Analysis</h3>
<p>To have a holistic and hands-on understanding of Volatility, we shall investigate a forensic case and use it to learn about the tool's inner workings. The files for the analysis are found under the <code>Desktop/Investigations</code>code> directory.</p>

<h4>Case 001</h4>
<p>Your SOC has informed you that they have gathered a memory dump from a quarantined endpoint thought to have been compromised by a banking trojan masquerading as an Adobe document. Your job is to use your knowledge of threat intelligence and reverse engineering to perform memory forensics on the infected host.<br>
You have been informed of a suspicious IP in connection with the file that could be helpful:  <code>41.168.5.140</code>.</p>

<h4>Plugins</h4>
<p>Volatility uses plugins to request data to carry out analysis. Some of the most commonly used plugins include:<br>

- <code>windows.info</code><br>
- <code>linux.info</code><br>
- <code>pslist</code><br>
- <code>.pstree</code> </p>

<p>Let us look at these plugins, extracting information from our memory file. First, we can begin by obtaining operating system details from the image. In previous versions of Volatility, this information was identified as OS profiles and was extracted using the plugin <code>imageinfo</code>. However, OS profiles have been deprecated in the new version, and now we have the individual information plugins.<br>
Given that our memory file was obtained from a Windows VM running on VMware, we can extract details about its profile with the command below:</p>


<p><em>Volatility Windows Info</em></p>

```bash
ubuntu@tryhackme:~/Desktop/volatility3$ python3 vol.py -f ~/Desktop/Investigations/Investigation-1.vmem windows.info
Volatility 3 Framework 2.26.2
WARNING  volatility3.framework.layers.vmware: No metadata file found alongside VMEM file. A VMSS or VMSN file may be required to correctly process a VMEM file. These should be placed in the same directory with the same file name, e.g. Investigation-1.vmem and Investigation-1.vmss.
Progress:  100.00               PDB scanning finished                                                                                              
Variable        Value

Kernel Base     0x804d7000
DTB     0x2fe000
Symbols file:///home/ubuntu/Desktop/volatility3/volatility3/symbols/windows/ntkrnlpa.pdb/30B5FB31AE7E4ACAABA750AA241FF331-1.json.xz
```

<p>We can extract the system version, architecture, symbol tables, and available memory layers from the details.</p>


<h3 align="left"> Answer the questions below</h3>

> 3.1. <em>What is the build version of the host machine in Case 001?</em> Hint : <em>Utilise the windows.info plugin to uncover information.</em><br><a id='3.1'></a>
>> <strong><code>2600.xpsp.080413-2111</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/96ba9d1d-f538-40d1-877c-2b43e6923b64)

```bash
ubuntu@tryhackme:~/Desktop/volatility3$ python3 vol.py -f ~/Desktop/Investigations/Investigation-1.vmem windows.info
```

![image](https://github.com/user-attachments/assets/af110d3a-b399-42ce-8de1-2f86687d2cc8)

<br>

> 3.2. <em>At what time was the memory file acquired in Case 001?</em> Hint: <em>Utilise the windows.info plugin to uncover information.</em><br><a id='3.2'></a>
>> <strong><code>2012-07-22 02:45:08</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/4cc7cbb2-d908-431a-97f6-0e457eaafde2)

<br>

<h2>Task 4 . Listing Processs and Connections</h2>
<p>When we want to analyse details on processes and network connections from our memory file, Volatility supports different plugins, each with varying techniques used. Not all plugins mentioned here will produce a result from the memory file, as the capture may not have included processes or services that the plugins would enumerate.</p>

<h3>Active Process Enumeration</h3>
<p>The most basic way of listing processes is by using <code>pslist</code>. This plugin enumerates active processes from the doubly-linked list that keeps track of processes in memory, equivalent to the process list in the task manager. The output from this plugin will include all current and terminated processes and their exit times.</p>

<p><em>Volatility Process Enumeration</em></p>

```bash
ubuntu@tryhackme:~/Desktop/volatility3$ python3 vol.py -f ~/Desktop/Investigations/Investigation-1.vmem windows.pslist
```

<h3>Hidden Process Enumeration</h3>
<p>Some malware, typically rootkits, will, in an attempt to hide their processes, unlink themselves from the list. By unlinking themselves from the list, you will no longer see their processes when using pslist. To combat this evasion technique, we can use psscan. This technique of listing processes will locate processes by finding data structures that match _EPROCESS. While this technique can help with evasion countermeasures, it can also result in false positives; therefore, we must be careful.</p>

<p><em>Volatility Process Enumeration</em></p>

```bash
ubuntu@tryhackme:~/Desktop/volatility3$ python3 vol.py -f ~/Desktop/Investigations/Investigation-1.vmem windows.psscan
```

<h3>Process Hierarchy Enumeration</h3>
<p>The third process plugin, pstree, does not offer any other kind of special techniques to help identify evasion like the last two plugins. However, this plugin will list all processes based on their parent process ID, using the same methods as pslist. This can be useful for an analyst to get a complete story of the processes and what may have occurred at the extraction time..</p>

<p><em>Volatility Files Inspecting</em></p>

```bash
ubuntu@tryhackme:~/Desktop/volatility3$ python3 vol.py -f ~/Desktop/Investigations/Investigation-1.vmem windows.pstree
```

<h3>File, Registry, and Thread Enumeration</h3>

<p><em>Volatility File Inspecting</em></p>

```bash
ubuntu@tryhackme:~/Desktop/volatility3$ python3 vol.py -f ~/Desktop/Investigations/Investigation-1.vmem windows.handles
```

<h3>Network Connection Enumeration</h3>

<p><em>Volatility Network Enumeration</em></p>

```bash
ubuntu@tryhackme:~/Desktop/volatility3$ python3 vol.py -f ~/Desktop/Investigations/Investigation-1.vmem windows.netstat
```

<h3>TCP/UDP Enumeration</h3>

<p><em>Volatility TCP/UDP Enumeration</em></p>

```bash
ubuntu@tryhackme:~/Desktop/volatility3$ python3 vol.py -f ~/Desktop/Investigations/Investigation-1.vmem windows.netscan
```

<h3>DLL Enumeration</h3>

<p><em>Volatility DLL Enumeration</em></p>

```bash
ubuntu@tryhackme:~/Desktop/volatility3$ python3 vol.py -f ~/Desktop/Investigations/Investigation-1.vmem windows.dlllist
```

<h3 align="left"> Answer the questions below</h3>

> 4.1. <em>What is the absolute path to the active Adobe process?</em><br><a id='4.1'></a>
>> <strong><code>C:\Program Files\Adobe\Reader 9.0\Reader\Reader_sl.exe</code></strong><br>
<p></p>

<p>In Task 3 --> banking trojan masquerading as an <code>Adobre</code>document.</p>

```bash
ubuntu@tryhackme:~/Desktop/volatility3$ python3 vol.py -f ~/Desktop/Investigations/Investigation-1.vmem windows.pstree | grep -i adobe
```

![image](https://github.com/user-attachments/assets/8645b945-2923-47d6-b5e6-5d88ff69c403)

<br>

> 4.2. <em>What is the parent process of this process in Case 001?</em><br><a id='4.2'></a>
>> <strong><code>____</code></strong><br>
<p></p>

```bash
ubuntu@tryhackme:~/Desktop/volatility3$ python3 vol.py -f ~/Desktop/Investigations/Investigation-1.vmem windows.psscan
```

![image](https://github.com/user-attachments/assets/5def0f7d-e153-4296-b593-60ec76ad21bb)

<br>

> 4.3. <em>What is the PID of the parent process?</em><br><a id='4.3'></a>
>> <strong><code>1484</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/5043244c-90c0-4509-82f5-37ac84b8fef4)

<br>

> 4.4. <em>How many DLL files are used by the Adobe process that are outside the <code>system32</code> directory?</em><br><a id='4.4'></a>
>> <strong><code>3</code></strong><br>
<p></p>

```bash
ubuntu@tryhackme:~/Desktop/volatility3$ python3 vol.py -f ~/Desktop/Investigations/Investigation-1.vmem windows.dlllist --pid 1484 > dlllist_1484
WARNING  volatility3.framework.layers.vmware: No metadata file found alongside VMEM file. A VMSS or VMSN file may be required to correctly process a VMEM file. These should be placed in the same directory with the same file name, e.g. Investigation-1.vmem and Investigation-1.vmss.
ubuntu@tryhackme:~/Desktop/volatility3$ cat dllist_1484 | grep -i -v system32
Volatility 3 Framework 2.26.2

PID	Process	Base	Size	Name	Path	LoadTime	File output

1484	explorer.exe	0x1000000	0xff000	Explorer.EXE	C:\WINDOWS\Explorer.EXE	N/A	Disabled
1484	explorer.exe	0x6f880000	0x1ca000	AcGenral.DLL	C:\WINDOWS\AppPatch\AcGenral.DLL	N/A	Disabled
1484	explorer.exe	0x773d0000	0x103000	comctl32.dll	C:\WINDOWS\WinSxS\x86_Microsoft.Windows.Common-Controls_6595b64144ccf1df_6.0.2600.5512_x-ww_35d4ce83\comctl32.dll	N/A	Disabled
ubuntu@tryhackme:~/Desktop/volatility3$ 
```

<br>

> 4.5. <em>What is the name of the one KeyedEvent associated with the process's handles?</em><br><a id='4.5'></a>
>> <strong><code>CritSecOutOfMemoryEvent</code></strong><br>
<p></p>

```bash
ubuntu@tryhackme:~/Desktop/volatility3$ python3 vol.py -f ~/Desktop/Investigations/Investigation-1.vmem windows.handles --pid 1484 | grep -i keyedevent
```

![image](https://github.com/user-attachments/assets/b1583e51-4b97-4a05-b738-399027d2eefe)

<br>

<h2>Task 5 . Volatility Hunting and Detection Capacbilities</h2>
<h3>Malware Analysis</h3>
<p>The first plugin we will discuss, which is one of the most useful when hunting for code injection, is <code>malfind</code>. This plugin will attempt to detect injected processes and their PIDs along with the offset address and the infected area's Hex, Ascii, and Disassembly views. The plugin works by scanning the heap and identifying processes that have the executable bit set RWE or RX and/or no memory-mapped file on disk (file-less malware).<br>

Based on what <code>malfind</code> identifies, the injected area will change. An MZ header is an indicator of a Windows executable file. The injected area could also be directed towards shellcode, which requires further analysis.</p>

<h5 align="center"><img width="600px" src="https://github.com/user-attachments/assets/34c92e78-b695-4396-9e07-67dc2baae55f"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h5>

<p><em>Volatility Malare Enumeration</em></p>

```bash
ubuntu@tryhackme:~/Desktop/volatility3$ python3 vol.py -f ~/Desktop/Investigations/Investigation-1.vmem windows.malfind
```

<p>Another helpful plugin is <code>vadinfo</code>. This displays detailed information about virtual memory descriptors, which is useful when manually investigating suspicious memory regions and heap allocations.</p>

<p><em>Volatility Malare Enumeration</em></p>

```bash
ubuntu@tryhackme:~/Desktop/volatility3$ python3 vol.py -f ~/Desktop/Investigations/Investigation-1.vmem windows.vadinfo
```

<h3 align="left"> Answer the question below</h3>

> 5.1. <em>What processes in the Case 001 memory file contain a header that points to a Windows executable file? (Answer: process1,process2)</em><br><a id='5.1'></a>
>> <strong><code>explorer.exe,reader_sl.exe</code></strong><br>
<p></p>

```bash
ubuntu@tryhackme:~/Desktop/volatility3$ python3 vol.py -f ~/Desktop/Investigations/Investigation-1.vmem windows.malfind | grep -i 'mz header'
```

![image](https://github.com/user-attachments/assets/2483ded0-4e57-4a5b-be80-98bf7634c6c4)

<br>

<h2>Task 6 . Advanced Memory Forensics</h2>
<p>Forensic analysts must be equipped to detect manipulation deep within the operating system when dealing with sophisticated threats such as kernel-mode rootkits. Rootkits are designed to conceal processes, files, drivers, and their presence by modifying kernel structures. This section focuses on a structured and practical exploration of these advanced evasion techniques, particularly within the Windows operating system, using Volatility 3.<br>

Advanced adversaries often employ <code>hooking</code> — a technique that allows malicious software to intercept and potentially redirect system-level functions for evasion or persistence. Hooks are not inherently malicious; antivirus and debugging tools also use them legitimately. The analyst’s responsibility is to identify whether the presence of a hook aligns with expected system behaviour or represents malicious interference.<br>

One of the most common hooking strategies is the <code>System Service Descriptor Table (SSDT)</code> hooks. These hooks are used to modify kernel system call table entries. They are prevalent in kernel-mode malware, with Volatility providing a corresponding plugin for analysis.</p>

<h3>SSDT Hook Detection</h3>
<p>The Windows kernel uses the System Service Descriptor Table (SSDT) to resolve addresses for system calls. Rootkits often overwrite SSDT entries to redirect legitimate system calls (e.g., NtCreateFile) to their malicious counterparts.<br>

Volatility 3’s windows.ssdt plugin enables analysts to inspect this table for any irregularities.</p>

<p><em>Volatility SSDT Hook Enumeration</em></p>

```bash
ubuntu@tryhackme:~/Desktop/volatility3$ python3 vol.py -f ~/Desktop/Investigations/Investigation-1.vmem windows.ssdt
```

<p><code>Recommendation</code>: Perform SSDT inspection <code>after</code> discovering suspicious kernel modules or abnormal process behaviour.

<h3>Kernel Module Enumeration</h3>
<p>The <code>windows.modules</code> plugin lists drivers and kernel modules currently loaded into memory. Each entry includes metadata such as base address, size, and file path.</p>
<p><em>Volatility Kernel Module Enumeration</em></p>

```bash
ubuntu@tryhackme:~/Desktop/volatility3$ python3 vol.py -f ~/Desktop/Investigations/Investigation-1.vmem windows.modules
```

<h3>Driver Scanning</h3>
<p>While <code>windows.modules</code> lists known drivers, it can miss hidden or unlinked ones. The <code>windows.driverscan</code> plugin scans raw memory for DRIVER_OBJECT structures that may have been unlinked from standard lists.</p>

<p><em>Volatility Kernel Module Enumeration</em></p>

```bash
ubuntu@tryhackme:~/Desktop/volatility3$ python3 vol.py -f ~/Desktop/Investigations/Investigation-1.vmem windows.driverscan
```

<h3 align="left"> Answer the question below</h3>

> 6.1. <em>What is the address for the <code>NtCreateFile</code> system call?</em><br><a id='6.1'></a>
>> <strong><code>0x8056e27c</code></strong><br>
<p></p>

```bash
ubuntu@tryhackme:~/Desktop/volatility3$ python3 vol.py -f ~/Desktop/Investigations/Investigation-1.vmem windows.ssdt | grep -i NtCreateFile
```

![image](https://github.com/user-attachments/assets/21afd732-64f7-412d-93d8-77a8baf9bf2b)

<br>

<h2>Task 7 . Practical Investigations</h2>
<h3>Case 002</h3>
<p>You have been informed that your corporation has been hit with a chain of ransomware that has been affecting corporations internationally. Your team has already recovered from the attack through backups. Your job is to perform post-incident analysis and identify which actors were at play and what occurred on your systems. You have received a raw memory dump from your team to begin your analysis.<br>

The memory file is located in <code>~/Desktop/Investigations/Investigation-2.raw</code>.</p>

Investigation-2.raw

<h3 align="left"> Answer the questionw below</h3>

> 7.1. <em>What suspicious process is running at PID 740?</em><br><a id='7.1'></a>

![image](https://github.com/user-attachments/assets/56b365f8-390f-4bce-96cc-1b8ffa4e8c3e)


```bash
ubuntu@tryhackme:~/Desktop/volatility3$ python3 vol.py -f ~/Desktop/Investigations/Investigation-2.raw windows.psscan --pid 740
```

![image](https://github.com/user-attachments/assets/2a66ea1f-8109-4374-a95c-517bd6c33e14)

<br>

> 7.2. <em>What is the full path of the suspicious binary in PID 740?</em><br><a id='7.2'></a>

![image](https://github.com/user-attachments/assets/bb8f50f2-8d8f-4c78-8282-06e4be69abb4)


```bash
ubuntu@tryhackme:~/Desktop/volatility3$ python3 vol.py -f ~/Desktop/Investigations/Investigation-2.raw windows.dlllist --pid 740
```

![image](https://github.com/user-attachments/assets/7feb4ab9-4e47-41c2-92be-1cccddefde8a)

<br>

> 7.3. <em>What is the parent process of PID 740?</em><br><a id='7.3'></a>
>> <strong><code>tasksche.exe</code></strong><br>
<p></p>

```bash
ubuntu@tryhackme:~/Desktop/volatility3$ python3 vol.py -f ~/Desktop/Investigations/Investigation-2.raw windows.psstree --pid 740
```

![image](https://github.com/user-attachments/assets/60af533f-c77b-421a-9be5-9076e645bc79)

<br>

> 7.4. <em>From our current information, what malware is present on the system?</em><br><a id='7.4'></a>

![image](https://github.com/user-attachments/assets/57678bfa-0dfa-44a3-bf4b-d6d5d0bd3ced)


![image](https://github.com/user-attachments/assets/8b6c998d-58a5-4c91-9029-a1a584954569)

<p>https://www.secureworks.com/research/wcry-ransomware-analysis</p>

![image](https://github.com/user-attachments/assets/346d1262-0b9d-4704-b822-6a0e5f91ec87)

![image](https://github.com/user-attachments/assets/2f1891d0-ec65-40c1-b265-c74c62b78d26)

<br>

> 7.5. <em>What plugin could be used to identify all files loaded from the malware working directory?</em><br><a id='7.5'></a>
>> <strong><code>windows.filescan</code></strong><br>
<p></p>

```bash
ubuntu@tryhackme:~/Desktop/volatility3$ python3 vol.py -f ~/Desktop/Investigations/Investigation-2.raw windows.psstree --pid 740
ubuntu@tryhackme:~/Desktop/volatility3$ python3 vol.py -h | grep -i scan
    linux.psscan.PsScan
                        Scans for processes present in a particular linux
    linux.vmaregexscan.VmaRegExScan
                        Scans all virtual memory areas for tasks using RegEx.
    linux.vmayarascan.VmaYaraScan
                        Scans all virtual memory areas for tasks using yara.
    regexscan.RegExScan
                        Scans kernel memory using RegEx patterns.
    vmscan.Vmscan       Scans for Intel VT-d structues and generates VM
    windows.cmdscan.CmdScan
    windows.deskscan.DeskScan
                        Scans for the Desktop instances of each Window Station
    windows.driverscan.DriverScan
                        Scans for drivers present in a particular windows
    windows.filescan.FileScan
                        Scans for file objects present in a particular windows
    windows.mbrscan.MBRScan
                        Scans for and parses potential Master Boot Records
    windows.mftscan.ADS
                        Scans for Alternate Data Stream
    windows.mftscan.MFTScan
                        Scans for MFT FILE objects present in a particular
    windows.mftscan.ResidentData
                        Scans for MFT Records with Resident Data
    windows.modscan.ModScan
                        Scans for modules present in a particular windows
    windows.mutantscan.MutantScan
                        Scans for mutexes present in a particular windows
    windows.netscan.NetScan
                        Scans for network objects present in a particular
    windows.poolscanner.PoolScanner
                        A generic pool scanner plugin.
    windows.psscan.PsScan
                        Scans for processes present in a particular windows
    windows.registry.hivescan.HiveScan
                        Scans for registry hives present in a particular
                        scanning to find rootkits
    windows.svcscan.SvcScan
                        Scans for windows services.
    windows.symlinkscan.SymlinkScan
                        Scans for links present in a particular windows memory
    windows.thrdscan.ThrdScan
                        Scans for windows threads.
    windows.vadregexscan.VadRegExScan
                        Scans all virtual memory areas for tasks using RegEx.
    windows.vadyarascan.VadYaraScan
                        Scans all the Virtual Address Descriptor memory maps
                        Scans for top level Windows Stations
    yarascan.YaraScan   Scans kernel memory using yara rules (string or fil
```

<br>

<h2>Task 8 . Conclusion</h2>

<p>We have only covered a very thin layer of memory forensics with Volatility, which can go much deeper when analysing the Windows, Mac, and Linux architectures. If you're looking for a deep dive into memory forensics, I suggest reading The Art of Memory Forensics.<br>

Additionally, the following is a list of worthy plugin mentions that you can be aware of and read more on:<br>

- <code>windows.callbacks</code>: Malware may register malicious callbacks for process creation, image loading, or thread creation. We can use this plugin to inspect callback functions for unknown driver associations or non-standard modules.<br>
- windows.driverirp: This plugin examines IRP (I/O Request Packet) dispatch tables of drivers. Suspicious drivers may register no IRP functions or point to non-driver memory.<br>
- windows.modscan: This plugin scans for loaded kernel modules without relying on linked lists. It can be used to uncover stealth drivers that evade both modules and driverscan.<br>
- windows.moddump: This plugin allows analysts to extract suspicious drivers or modules from memory for static analysis. Further investigation with tools such as Ghidra or IDA can be done to reverse engineer dumped modules.<br>
- windows.memmap: This plugin can perform deeper analysis of injected code or memory artefacts, to extract memory regions from specific processes.<br>
- yarascan: This plugin will search for strings, patterns, and compound rules against a rule set by using a YARA file as an argument or listing rules within the command line.<br>
In the next room, Memory Acquisition, we will cover memory acquisition in detail, covering all the necessary techniques and approaches.</p>


<h3 align="left"> Answer the question below</h3>

> 8.1. <em>Ready the above and continue learning!</em><br><a id='8.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>


<br>
<br>

![image](https://github.com/user-attachments/assets/d3f3a3e4-4040-41bd-a93c-247d713fa257)

![image](https://github.com/user-attachments/assets/aaa9b9f2-5fc7-4ff3-b669-6933e976357f)

<br>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| June 17 2025      | 407      |     199ᵗʰ    |      5ᵗʰ     |     301ˢᵗ   |     6ᵗʰ    |  108,485 |    784    |     63    |

</div>

![image](https://github.com/user-attachments/assets/34e894c8-1d3d-4c3a-9c2c-5d39f36b1010)

![image](https://github.com/user-attachments/assets/a6fbc023-e199-489b-8f5c-d29e9ba976ba)

![image](https://github.com/user-attachments/assets/4c4a2a57-dc51-4a16-8b2f-e365fd4c78da)

![image](https://github.com/user-attachments/assets/e1363df8-1565-4276-ae28-789b9cf27db5)

![image](https://github.com/user-attachments/assets/27792a90-fec0-4a95-950c-2405a1d91b9c)

