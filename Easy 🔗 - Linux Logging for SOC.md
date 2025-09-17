<h1 align="center">Linux Logging for SOC</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/88f79fae-a313-469e-a79d-10032cfb6165"><br>
2025, September 17<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>499</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Explore key Linux log sources and learn how to use them in your SOC triage</em>.<br>
Access it <a href="https://tryhackme.com/room/linuxloggingforsoc">here</a>.<br>
<img width="1200px" src=""></p>


<h2>Task 1 . Introduction</h2>

<p>Linux has long been a leader in servers and embedded systems, and now its use is even more widespread with the growth of cloud adoption. As a SOC analyst, you are now very likely to investigate Linux alerts and incidents, either from traditional on-premises servers or from cloud-native containerized workloads. In this room, you will explore the most common Linux logs sent to SIEM and learn how to view them directly on-host.</p>
<br>

<p><em>Answer the question below</em></p>

<p>1.1.Let´s start!<br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 . Working With Text Logs</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>2.1. Use the /var/log/syslog file on the VM to answer the questions.
Which time server domain did the VM contact to sync its time?<br>
<code>ntp.ubuntu.com</code></p>

```bash
ubuntu@thm-vm:/var/log$ cat /var/log/syslog | grep 'time server'
```
<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/94443bba-6669-4295-a070-f2e437b73714"><br><br>
                   <img width="900px" src="https://github.com/user-attachments/assets/e70d92ef-0d4d-4e91-a5b9-d92c431e3cca"><br>Rosana´s hands-on<br></h6>

<br>
<p>2.2. What is the kernel message from Yama in /var/log/syslog?<br>
<code>Becoming mindful.</code></p>

```bash
ubuntu@thm-vm:/var/log$ cat /var/log/syslog | grep Yama
```

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/49b99887-cdcb-4f63-bbd5-9f0ed2b39e0c"><br>Rosana´s hands-on<br></h6>

<br>
<h2>Task 3 . Authentication Logs</h2>
<h3>Authentication Logs</h3>




<h3>Login and Logout Events</h3>



<h3>Miscellaneous Events</h3>


<p><em>Answer the questions below</em></p>

<p>3.1.Continue with the VM and use the /var/log/auth.log file. Which IP address failed to log in on multiple users via SSH?<br>
<code>10.14.94.82</code></p>

```bash
ubuntu@thm-vm:/var/log$ cat auth.log | grep -E 'Failed'
```

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/ab70b6cd-2c51-4d7e-b760-7a341d7c6ba7"><br>Rosana´s hands-on<br></h6>

<br>
<p>3.2. Which user was created and added to the "sudo" group?<br>
<code>xerxes</code></p>

```bash
ubuntu@thm-vm:/var/log$ cat auth.log | grep -E 'useradd'
```

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/e90c4451-1d1c-4a1d-b35a-6e68fac54fd4"><br>Rosana´s hands-on<br></h6>

<br>
<h2>Task 4 . Common Linux Logs</h2>
<h3>Generic System Logs</h3>



<h3>App-Specific Logs</h3>


<h3>Bash History</h3>



<p><em>Answer the questions below</em></p>

<p>4.1. According to the VM's package manager logs, which version of unzip was installed on the system?<br>
<code>6.0-28ubuntu4.1</code></p>

<img width="1248" height="67" alt="image" src="https://github.com/user-attachments/assets/00981137-8624-4395-af41-c3c337f2f66d" />


<p>4.2. What is the flag you see in one of the users' bash history?<br>
<code>THM{****************}</code></p>

<img width="1360" height="825" alt="image" src="https://github.com/user-attachments/assets/7e40702c-df51-4bc5-bd9b-317f92863fa4" />

<br>
<h2>Task 5 . Runtime Monitoring</h2>
<h3>Runtime Monitoring</h3>



<h3>System Calls</h3>


<p><em>Answer the questions below</em></p>

<p>5.1. Which Linux system call is commonly used to execute a program?<br>
<code>execve</code></p>

<p>5.2. Can a typical program open a file or create a process bypassing system calls? (Yea/Nay)<br>
<code>Nay</code></p>

<br>
<h2 align="center">Task 6 . Using Auditd</h2>
<h3 align="center">Audit Daemon</h3>
<p>Auditd (Audit Daemon) is a built-in auditing solution often used by the SOC team for runtime monitoring. In this task, we will skip the configuration part and focus on how to read auditd rules and how to interpret the results. Let's start from the rules - instructions located in <code>/etc/audit/rules.d/</code> that define which system calls to monitor and which filters to apply:</p>

<h6 align="center"><img width="500px" src="https://github.com/user-attachments/assets/566f0914-e725-4b1d-8622-fc488a31ced4"><br>This image and all the theoretical content of the present article is TryHackMe´s property.<br></h6>

<p>Monitoring every process, file, and network event can quickly produce gigabytes of logs each day. But more logs don't always mean better detection since an attack buried in a terabyte of noise is still invisible. That's why SOC teams often focus on the highest-risk events and build balanced rulesets, like <a href="https://github.com/Neo23x0/auditd/blob/master/audit.rules">this one</a> or the example you saw above.</p>

<h3 align="center">Using Auditd</h3>
<p>You can view the generated logs in real time in <code>/var/log/audit/audit.log</code>, but it is easier to use the <code>ausearch</code> command, as it formats the output for better readability and supports filtering options. Let's see an example based on the rules from the example above by searching events matching the "proc_wget" key:</p>

<p align="center"><em>Looking for "Wget" Execution</em></p>

```bash
root@thm-vm:~$ ausearch -i -k proc_wget
----
type=PROCTITLE msg=audit(08/12/25 12:48:19.093:2219) : proctitle=wget https://files.tryhackme.thm/report.zip
type=CWD msg=audit(08/12/25 12:48:19.093:2219) : cwd=/root
type=EXECVE msg=audit(08/12/25 12:48:19.093:2219) : argc=2 a0=wget a1=https://files.tryhackme.thm/report.zip
type=SYSCALL msg=audit(08/12/25 12:48:19.093:2219) : arch=x86_64 syscall=execve [...] ppid=3752 pid=3888 auid=ubuntu uid=root tty=pts1 exe=/usr/bin/wget key=proc_wget
```

<p>The terminal above shows a log of a single "wget" command. Here, auditd splits the event into four lines: the PROCTITLE shows the process command line, CWD reports the current working directory, and the remaining two lines show the system call details, like:<br>

- <code>pid=3888, ppid=3752</code>: Process ID and Parent Process ID. Helpful in linking events and building a process tree<br>
- <code>auid=ubuntu</code>: Audit user. The account originally used to log in, whether locally (keyboard) or remotely (SSH)<br>
- <code>uid=root</code>: The user who ran the command. The field can differ from auid if you switched users with sudo or su<br>
- <code>tty=pts1</code>: Session identifier. Helps distinguish events when multiple people work on the same Linux server<br>
- <code>exe=/usr/bin/wget</code>: Absolute path to the executed binary, often used to build SOC detection rules<br>
- <code>key=proc_wget</code>: Optional tag specified by engineers in auditd rules that is useful to filter the events</p>

<h4 align="center">File Events</h4>
<p>Now, let's look at the file events matching the "file_sshconf" key. As you may see from the terminal below, auditd tracked the change to the <code>/etc/ssh/sshd_config</code> file via the "nano" command. SOC teams often set up rules to monitor changes in critical files and directories (e.g., SSH configuration files, cronjob definitions, or system settings)</p>

<p align="center"><em>Looking for SSH Configuration Changes</em></p>

```bash
root@thm-vm:~$ ausearch -i -k file_sshconf
----
type=PROCTITLE msg=audit(08/12/25 13:06:47.656:2240) : proctitle=nano /etc/ssh/sshd_config
type=CWD msg=audit(08/12/25 13:06:47.656:2240) : cwd=/
type=PATH msg=audit(08/12/25 13:06:47.656:2240) : item=0 name=/etc/ssh/sshd_config [...]
type=SYSCALL msg=audit(08/12/25 13:06:47.656:2240) : arch=x86_64 syscall=openat [...] ppid=3752 pid=3899 auid=ubuntu uid=root tty=pts1 exe=/usr/bin/nano key=file_sshconf
```

<h3 align="center">Audit Alternatives</h3>
<p>You might have noticed an inconvenient output of auditd - although it provides a verbose logging, it is hard to read and ingest into SIEM. That's why many SOC teams resort to the alternative runtime logging solutions, for example:<br>

- <a href="https://github.com/microsoft/SysmonForLinux">Sysmon for Linux</a>: A perfect choice if you already work with Sysmon and love XML<br>
- <a href="https://falco.org/">Falco</a>: A modern, open-source solution, ideal for monitoring containerized systems<br>
- <a href="https://osquery.io/">Osquery</a>: An interesting tool that can be broadly used for various security purposes<br>
- <a href="https://tryhackme.com/room/introductiontoedr">EDRs</a>: Most EDR solutions can track and monitor various Linux runtime events<br>

The key to remember is that all listed tools work on the same principle - monitoring system calls. Once you've understood system calls, you will easily learn all the mentioned tools. This knowledge also helps you to handle advanced scenarios, like understanding why certain actions were logged in a specific way or not logged at all.<br>

Now, try to uncover a threat actor with process creation logs! For this task, continue with the VM and use auditd logs to answer the questions.
You may need to use <code>ausearch -i</code> and <code>grep</code> commands for this task.</p>

<p><em>Answer the questions below</em></p>

<p>6.1. When was the secret.thm file opened for the first time? (MM/DD/YY HH:MM:SS). Note: Access to this file is logged with the "file_thmsecret" key.<br>
<code>naabu_2.3.5_linux_amd64.zip</code></p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/8fd5566c-a1c5-412b-b0e7-18e0334cfd1f"><br>Rosana´s hands-on<br></h6>

<p>6.2. What is the original file name downloaded from GitHub via wget?Note: Wget process creation is logged with the "proc_wget" key.<br>
<code>naabu_2.3.5_linux_amd64.zip</code></p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/973ffa60-dadd-413f-be3d-8cccf5cce91c"><br>Rosana´s hands-on<br></h6>

<p>6.3.Which network range was scanned using the downloaded tool? Note: There is no dedicated key for this event, but it's still in auditd logs.<br>
<code>naabu_2.3.5_linux_amd64.zip</code></p>

```bash
$ ausearch -m connect,sendto -c naadbu --raw | grep 'syscall=connect operation=connect' | grep 'saddr=' | grep 'dest=' | grep 'addr='
```


<br>
<br>



