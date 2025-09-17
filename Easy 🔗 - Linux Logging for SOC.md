<h1 align="center">Linux Logging for SOC</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/88f79fae-a313-469e-a79d-10032cfb6165"><br>
2025, September 17<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>499</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Explore key Linux log sources and learn how to use them in your SOC triage</em>.<br>
Access it <a href="https://tryhackme.com/room/linuxloggingforsoc">here</a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/a9b94ce0-f3f4-4453-acab-d31116dd1803"></p>

<h2 align="center">Task 1 . Introduction</h2>
<p>Linux has long been a leader in servers and embedded systems, and now its use is even more widespread with the growth of cloud adoption. As a SOC analyst, you are now very likely to investigate Linux alerts and incidents, either from traditional on-premises servers or from cloud-native containerized workloads. In this room, you will explore the most common Linux logs sent to SIEM and learn how to view them directly on-host.</p>

<h3 align="center">Learning Objectives</h3>
<p>

- Explore authentication, runtime, and system logs on Linux<br>
- Learn the commands and pitfalls when working with logs<br>
- Uncover how tools like auditd monitor and report the events<br>
- Practice every learned log source in the attached VM</p>

<h3 align="center">Recommended Rooms</h3>
<p>Before starting this room, you should already be familiar with the fundamentals of web application security, including vulnerabilities like:<br>

- Complete the <a href="https://tryhackme.com/module/linux-fundamentals">Linux Fundamentals</a> module<br>
- Complete the <a href="https://tryhackme.com/room/linuxshells">Linux Shells</a> room<br>
- Learn the <a href="https://tryhackme.com/room/logsfundamentals">Logs Fundamentals</a></p>

<h3 align="center">Machine Access</h3>
<p>Before moving forward, start the lab by clicking the <strong>Start Machine</strong> button below. The machine will start in split view and will take about two minutes to load. In case the machine is not visible, you can click the <strong>Show Split</strong> View button at the top of the task. You may need to work as the root user for some tasks. To switch to root on the VM, please run <code>sudo su</code></p>

<h3 align="center">Set up virtual environment</h3>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting the Target Machine, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.<br>
[ Start Machine]</p>

<h3 align="center">Credentials</h3>
<p>Alternatively, you can access the VM from your own VPN-connected machine with the credentials below:

- Username: ******<br>
- Password: *******<br>
- IP address: MACHINE_IP<br>
- Connection via: SSH</p>

<p><em>Answer the question below</em></p>

<p>1.1. Let´s start!<br>
<code>No answer needed</code></p>

<br>
<h2 align="center">Task 2 . Working With Text Logs</h2>
<h3 align="center">Log Format</h3>
<p>Contrary to a common belief, Linux-based systems are not immune to malware. Moreover, Linux-targeted intrusions are a growing problem. Thus, as a SOC analyst, you will often need to investigate Linux alerts, and for this, you need to understand how its logging works. Now, let's clarify a couple of things and move on!<br>

- By Linux, the room refers to Linux distributions like Debian, Ubuntu, CentOS, or RHEL<br>
- The room focuses on Linux servers without a GUI and does not explain desktop logging</p>

<h3 align="center">Working With Logs</h3>
<p>Unlike in Windows, Linux logs most events into plain text files. This means you can read the logs via any text editor without the need for specialized tools like Event Viewer. On the other hand, default Linux logs are less structured as there are no event codes and strict log formatting rules. Most Linux logs are located in the <code>/var/log</code> folder, so let's start the journey by checking the <code>/var/log/syslog</code> file - an aggregated stream of various system events:</p>

<p align="center"><em>Syslog File Content</em></p>

```bash
root@thm-vm:~$ cat /var/log/syslog | head
[...]
2025-08-13T13:57:49.388941+00:00 thm-vm systemd-timesyncd[268]: Initial clock synchronization to Wed 2025-08-13 13:57:49.387835 UTC.
2025-08-13T13:59:39.970029+00:00 thm-vm systemd[888]: Starting dbus.socket - D-Bus User Message Bus Socket...
2025-08-13T14:02:22.606216+00:00 thm-vm dbus-daemon[564]: [system] Successfully activated service 'org.freedesktop.timedate1'
2025-08-13T14:05:01.999677+00:00 thm-vm CRON[1027]: (root) CMD (command -v debian-sa1 > /dev/null && debian-sa1 1 1)
[...]
```

<h4 align="center">Filtering Logs</h4>
<p>You will see thousands of events when reading the syslog file on the attached VM, but only a few are useful for SOC. That's why you must filter logs and narrow down your search as much as possible. For example, you can use the "grep" command to filter for the "CRON" keyword and see only the cronjob logs:</p>

<p align="center"><em>Syslog Filtering</em></p>

```bash
# Or "grep -v CRON" to exclude "CRON" from results
root@thm-vm:~$ cat /var/log/syslog | grep CRON
2025-08-13T14:17:01.025846+00:00 thm-vm CRON[1042]: (root) CMD (cd / && run-parts --report /etc/cron.hourly)
2025-08-13T14:25:01.043238+00:00 thm-vm CRON[1046]: (root) CMD (command -v debian-sa1 > /dev/null && debian-sa1 1 1)
2025-08-13T14:30:01.014532+00:00 thm-vm CRON[1048]: (root) CMD (date > mycrondebug.log)
```

<h4 align="center">Discovering Logs</h4>
<p>Lastly, let's say you hunt for all user logins, but don't know where to look for them. Linux system logs are stored in the <code>/var/log/</code> folder in plain text, so you can simply grep for related keywords like "login", "auth", or "session" in all log files there and narrow down your next searches:</p>

<p align="center"><em>Discovering Logs</em></p>

```bash
# List what's logged by your system (/var/log folder) 
root@thm-vm:~$ ls -l /var/log
drwxr-xr-x  2 root      root               4096 Aug 12 16:41 apt
drwxr-x---  2 root      adm                4096 Aug 12 12:40 audit
-rw-r-----  1 syslog    adm               45399 Aug 13 15:05 auth.log
-rw-r--r--  1 root      root            1361277 Aug 12 16:41 dpkg.log
drwxr-sr-x+ 3 root      systemd-journal    4096 Oct 22  2024 journal
-rw-r-----  1 syslog    adm              214772 Aug 13 13:57 kern.log
-rw-r-----  1 syslog    adm              315798 Aug 13 15:05 syslog
[...]

# Search for potential logins across all logs (/var/log)
root@thm-vm:~$ grep -R -E "auth|login|session" /var/log
[...]
```

<h3 align="center">Logging Caveats</h3>
<p>Unlike Windows, Linux allows you to easily change log format, verbosity, and storage location. With hundreds of Linux distributions, each known to slightly customize logging, be prepared that the logs in this room may look different on your system, or might not exist at all.</p>

<p><em>Answer the questions below</em></p>

<p>2.1. Use the <strong>/var/log/syslog</strong> file on the VM to answer the questions.
Which time server domain did the VM contact to sync its time?<br>
<code>ntp.ubuntu.com</code></p>

```bash
ubuntu@thm-vm:/var/log$ ll
```
<h6 align="center"><img width="1000px" src="https://github.com/user-attachments/assets/94443bba-6669-4295-a070-f2e437b73714"><br>Rosana´s hands-on<br></h6>

```bash
ubuntu@thm-vm:/var/log$ cat /var/log/syslog | grep 'time server'
```
<h6 align="center"><img width="1000px" src="https://github.com/user-attachments/assets/e70d92ef-0d4d-4e91-a5b9-d92c431e3cca"><br>Rosana´s hands-on<br></h6>

<br>
<p>2.2. What is the kernel message from Yama in  <strong>/var/log/syslog</strong>?<br>
<code>Becoming mindful.</code></p>

```bash
ubuntu@thm-vm:/var/log$ cat /var/log/syslog | grep Yama
```

<h6 align="center"><img width="1000px" src="https://github.com/user-attachments/assets/49b99887-cdcb-4f63-bbd5-9f0ed2b39e0c"><br>Rosana´s hands-on<br></h6>

<br>
<h2 align="center">Task 3 . Authentication Logs</h2>
<h3 align="center">Authentication Logs</h3>
<p>The first and often the most useful log file you want to monitor is <code>/var/log/auth.log</code>code> (or <code>/var/log/secure</code> on RHEL-based systems). Although its name suggests it contains authentication events, it can also store user management events, launched sudo commands, and much more! Let's start with the log file format:</p>

<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/0884762e-e3ff-464b-9e39-657a49f17628"><br>This image and all the theoretical content of the present article is TryHackMe´s property.<br></h6>

<h3 align="center">Login and Logout Events</h3>
<p>There are many ways users authenticate into a Linux machine: locally, via SSH, using "sudo" or "su" commands, or automatically to run a cron job. Each successful logon and logoff is logged, and you can see them by filtering the events containing the "session opened" or "session closed" keywords:</p>

<p align="center"><em>Local and Remote Logins</em></p>

```bash
root@thm-vm:~$ cat /var/log/auth.log | grep -E 'session opened|session closed'
# Local, on-keyboard login and logout of Bob (login:session)
2025-08-02T16:04:43 thm-vm login[1138]: pam_unix(login:session): session opened for user bob(uid=1001) by bob(uid=0)
2025-08-02T19:23:08 thm-vm login[1138]: pam_unix(login:session): session closed for user bob
# Remote login examples of Alice (via SSH and then SMB)
2025-08-04T09:09:06 thm-vm sshd[839]: pam_unix(sshd:session): session opened for user alice(uid=1002) by alice(uid=0)
2025-08-04T12:46:13 thm-vm smbd[1795]: pam_unix(samba:session): session opened for user alice(uid=1002) by alice(uid=0)
```

<p align="center"><em>Cron and Sudo Logins</em></p>

```bash
root@thm-vm:~$ cat /var/log/auth.log | grep -E 'session opened|session closed'
# Traces of some cron job launch running as root (cron:session)
2025-08-06T19:35:01 thm-vm CRON[41925]: pam_unix(cron:session): session opened for user root(uid=0) by root(uid=0)
2025-08-06T19:35:01 thm-vm CRON[3108]: pam_unix(cron:session): session closed for user root
# Carol running "sudo su" to access root (sudo:session)
2025-08-07T09:12:32 thm-vm sudo: pam_unix(sudo:session): session opened for user root(uid=0) by carol(uid=1003)
```

<p>In addition to the system logs, the SSH daemon stores its own log of successful and failed SSH logins. These logs are sent to the same auth.log file, but have a slightly different format. Let's see the example of two failed and one successful SSH logins:</p>

<p align="center"><em>SSH-Specific Events</em></p>

```bash
root@thm-vm:~$ cat /var/log/auth.log | grep "sshd" | grep -E 'Accepted|Failed'
# Common SSH log format: <is-successful> <auth-method> for <user> from <ip>
2025-08-07T11:21:25 thm-vm sshd[3139]: Failed password for root from 222.124.17.227 port 50293 ssh2
2025-08-07T14:17:40 thm-vm sshd[3139]: Failed password for admin from 138.204.127.54 port 52670 ssh2
2025-08-09T20:30:51 thm-vm sshd[1690]: Accepted publickey for bob from 10.19.92.18 port 55050 ssh2: <key>
```

<h3 align="center">Miscellaneous Events</h3>
<p>You can also use the same log file to detect user management events. This is easy if you know basic Linux commands: If <a href="https://www.man7.org/linux/man-pages/man8/useradd.8.html">useradd</a> is a command to add new users, just look for a "useradd" keyword to see user creation events! Below is an example of what you can see in the logs: password change, user deletion, and then privileged user creation.</p>

<p align="center"><em>User management events</em></p>

```bash
root@thm-vm:~$ cat /var/log/auth.log | grep -E '(passwd|useradd|usermod|userdel)\['
2023-02-01T11:09:55 thm-vm passwd[644]: password for 'ubuntu' changed by 'root'
2025-08-07T22:11:11 thm-vm userdel[1887]: delete user 'oldbackdoor'
2025-08-07T22:11:29 thm-vm useradd[1878]: new user: name=backdoor, UID=1002, GID=1002, shell=/bin/sh
2025-08-07T22:11:54 thm-vm usermod[1906]: add 'backdoor' to group 'sudo'
2025-08-07T22:11:54 thm-vm usermod[1906]: add 'backdoor' to shadow group 'sudo'
```

<p>Lastly, depending on system configuration and installed packages, you may encounter interesting or unexpected events. For example, you may find commands launched with sudo, which can help track malicious actions. In the example below, the "ubuntu" user used sudo to stop EDR, read firewall state, and finally access root via "sudo su":</p>

<p align="center"><em>Commands Run With Sudo</em></p>

```bash
root@thm-vm:~$ cat /var/log/auth.log | grep -E 'COMMAND='
2025-08-07T11:21:49 thm-vm sudo: ubuntu : TTY=pts/0 ; [...] COMMAND=/usr/bin/systemctl stop edr
2025-08-07T11:23:18 thm-vm sudo: ubuntu : TTY=pts/0 ; [...] COMMAND=/usr/bin/ufw status numbered
2025-08-07T11:23:33 thm-vm sudo: ubuntu : TTY=pts/0 ; [...] COMMAND=/usr/bin/su
```

<p><em>Answer the questions below</em></p>

<p>3.1. Continue with the VM and use the /var/log/auth.log file. Which IP address failed to log in on multiple users via SSH?<br>
<code>10.14.94.82</code></p>

```bash
ubuntu@thm-vm:/var/log$ cat auth.log | grep -E 'Failed'
```

<h6 align="center"><img width="1000px" src="https://github.com/user-attachments/assets/ab70b6cd-2c51-4d7e-b760-7a341d7c6ba7"><br>Rosana´s hands-on<br></h6>

<br>
<p>3.2. Which user was created and added to the "sudo" group?<br>
<code>xerxes</code></p>

```bash
ubuntu@thm-vm:/var/log$ cat auth.log | grep -E 'useradd'
```

<h6 align="center"><img width="1000px" src="https://github.com/user-attachments/assets/e90c4451-1d1c-4a1d-b35a-6e68fac54fd4"><br>Rosana´s hands-on<br></h6>

<br>
<h2 align="center">Task 4 . Common Linux Logs</h2>
<h3 align="center">Generic System Logs</h3>
<p>Linux keeps track of many other events scattered across files in <code>/var/log</code>: kernel logs, network changes, service or cron runs, package installation, and many more. Their content and format can differ depending on the OS, and the most common log files are:<br>

-  <code>/var/log/kern.log</code>: Kernel messages and errors, useful for more advanced investigations<br>
-  <code>/var/log/syslog (or /var/log/messages)</code>: A consolidated stream of various Linux events<br>
-  <code>/var/log/dpkg.log (or /var/log/apt)</code>: Package manager logs on Debian-based systems<br>
- <code>/var/log/dnf.log (or /var/log/yum.log)</code>: Package manager logs on RHEL-based systems<br>

The listed logs are valuable during DFIR, but are rarely seen in a daily SOC routine as they are often noisy and hard to parse. Still, if you want to dive deeper into how these logs work, check out the <a href="https://tryhackme.com/room/linuxlogsinvestigations">Linux Logs Investigations</a> DFIR room.</p>

<h3 align="center">App-Specific Logs</h3>
<p>In SOC, you might also monitor a specific program, and to do this effectively, you need to use its logs. For example, analyze database logs to see which queries were run, mail logs to investigate phishing, container logs to catch anomalies, and web server logs to know which pages were opened, when, and by whom. You will explore these logs in the upcoming modules, but to give an overview, here is an example from the typical Nginx web server logs:</p>

<p align="center"><em>Nginx Web Access Logs</em></p>

```bash
root@thm-vm:~$ cat /var/log/nginx/access.log
# Every log line corresponds to a web request to the web server
10.0.1.12 - - [11/08/2025:14:32:10 +0000] "GET / HTTP/1.1" 200 3022
10.0.1.12 - - [11/08/2025:14:32:14 +0000] "GET /login HTTP/1.1" 200 1056
10.0.1.12 - - [11/08/2025:14:33:09 +0000] "POST /login HTTP/1.1" 302 112
10.0.4.99 - - [11/08/2025:17:11:20 +0000] "GET /images/logo.png HTTP/1.1" 200 5432
10.0.5.21 - - [11/08/2025:17:56:23 +0000] "GET /admin HTTP/1.1" 403 104
```

<h3 align="center">Bash History</h3>
<p>Another valuable log source is Bash history - a feature that records each command you run after pressing Enter. By default, commands are first stored in memory during your session, and then written to the per-user <code>~/.bash_history</code> file when you log out. You can open the <code>~/.bash_history</code> file to review commands from previous sessions or use the <code>history</code> command to view commands from both your current and past sessions:</p>

<p align="center"><em>Bash History File and Command</em></p>

```bash
ubuntu@thm-vm:~$ cat /home/ubuntu/.bash_history
echo "hello" > world.txt
nano /etc/ssh/sshd_config
sudo su
ubuntu@thm-vm:~$ history
1 echo "hello" > world.txt
2 nano /etc/ssh/sshd_config
3 sudo su
4 ls -la /home/ubuntu
5 cat /home/ubuntu/.bash_history
6 history
```

<p>Although the Bash history file looks like a vital log source, it is rarely used by SOC teams in their daily routine. This is because it does not track non-interactive commands (like those initiated by your OS, cron jobs, or web servers) and has some other limitations. While you can <a href="https://datawookie.dev/blog/2023/04/configuring-bash-history/">configure it</a> to be more useful, there are still a few issues you should know about:</p>

<p align="center"><em>Bash History Limitations</em></p>

```bash
# Attackers can simply add a leading space to the command to avoid being logged
ubuntu@thm-vm:~$  echo "You will never see me in logs!"

# Attackers can paste their commands in a script to hide them from Bash history
ubuntu@thm-vm:~$ nano legit.sh && ./legit.sh
 
# Attackers can use other shells like /bin/sh that don't save the history like Bash
ubuntu@thm-vm:~$ sh
$ echo "I am no longer tracked by Bash!"
```

<p><em>Answer the questions below</em></p>

<p>4.1. According to the VM's package manager logs, which version of unzip was installed on the system?<br>
<code>6.0-28ubuntu4.1</code></p>

```bash
ubuntu@thm-vm:/var/log$ cat dpkg.log | grep ' installed ' | grep -E 'unzip'
```

<h6 align="center"><img width="1000px" src="https://github.com/user-attachments/assets/00981137-8624-4395-af41-c3c337f2f66d"><br>Rosana´s hands-on<br></h6>

<br>
<p>4.2. What is the flag you see in one of the users' bash history?<br>
<code>THM{****************}</code></p>

```bash
ubuntu@thm-vm:/$ sudo -l
...
ubuntu@thm-vm:/$ sudo su
...
ubuntu@thm-vm:/$ pwd
...
ubuntu@thm-vm:/$ cd /root
ubuntu@thm-vm:/$ ll
...
ubuntu@thm-vm:/$ cat .bash_history
```

<h6 align="center"><img width="1000px" src="https://github.com/user-attachments/assets/7e40702c-df51-4bc5-bd9b-317f92863fa4"><br>Rosana´s hands-on<br></h6>

<br>
<h2 align="center">Task 5 . Runtime Monitoring</h2>
<h3 align="center">Runtime Monitoring</h3>
<p>Up to this point, you have explored various Linux log sources, but none can reliably answer questions like "Which programs did Bob launch today?" or "Who deleted my home folder, and when?". That's because, by default, Linux doesn't log process creation, file changes, or network-related events, collectively known as runtime events. Interestingly, Windows faces the same limitation, which is why in the <a href="https://tryhackme.com/room/windowsloggingforsoc">Windows Logging for SOC</a> room we had to use an additional tool: Sysmon. In Linux, we'll take a similar approach.</p>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/ef535fcd-8f9c-4e21-856b-9db6d1d100e3"><br>This image and all the theoretical content of the present article is TryHackMe´s property.<br></h6>

<h3 align="center">System Calls</h3>
<p>Before moving on, let's explore a core OS concept that might help you understand many other topics: system calls. In short, whenever you need to open a file, create a process, access the camera, or request any other OS service, you make a specific system call. There are over <a href="https://man7.org/linux/man-pages/man2/syscalls.2.html">300</a> system calls in Linux, like <code>execve</code> to execute a program. Below is a high-level flowchart of how it works:</p>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/bb6a6147-c1d3-460c-9878-208d5812e085"><br>This image and all the theoretical content of the present article is TryHackMe´s property.<br></h6>

<p>Why do you need to know about system calls? Well, all modern EDRs and logging tools rely on them - they monitor the main system calls and log the details in a human-readable format. Since there is nearly no way for attackers to bypass system calls, all you have to do is choose the system calls you'd like to log and monitor. In the next task, you will try it in practice using auditd.</p>

<p><em>Answer the questions below</em></p>

<p>5.1. Which Linux system call is commonly used to execute a program?<br>
<code>execve</code></p>

<br>
<p>5.2. Can a typical program open a file or create a process bypassing system calls? (Yea/Nay)<br>
<code>Nay</code></p>

<br>
<h2 align="center">Task 6 . Using Auditd</h2>
<h3 align="center">Audit Daemon</h3>
<p>Auditd (Audit Daemon) is a built-in auditing solution often used by the SOC team for runtime monitoring. In this task, we will skip the configuration part and focus on how to read auditd rules and how to interpret the results. Let's start from the rules - instructions located in <code>/etc/audit/rules.d/</code> that define which system calls to monitor and which filters to apply:</p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/566f0914-e725-4b1d-8622-fc488a31ced4"><br>This image and all the theoretical content of the present article is TryHackMe´s property.<br></h6>

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

```bash
root@thm-vm:var/log/audit$ ausearch -i -k proc_wget | grep github
```

<h6 align="center"><img width="1000px" src="https://github.com/user-attachments/assets/8fd5566c-a1c5-412b-b0e7-18e0334cfd1f"><br>Rosana´s hands-on<br></h6>

<br>
<p>6.2. What is the original file name downloaded from GitHub via wget?Note: Wget process creation is logged with the "proc_wget" key.<br>
<code>naabu_2.3.5_linux_amd64.zip</code></p>

```bash
root@thm-vm:var/log/audit$ ausearch -i -k file_thmsecret
```

<h6 align="center"><img width="1000px" src="https://github.com/user-attachments/assets/973ffa60-dadd-413f-be3d-8cccf5cce91c"><br>Rosana´s hands-on<br></h6>

<p>6.3.Which network range was scanned using the downloaded tool? Note: There is no dedicated key for this event, but it's still in auditd logs.<br>
<code>192.168.50.0/24</code></p>

```bash
ubuntu@thm-vm:/var/log/audit$ cat audit.log | grep naabu
```

<h6 align="center"><img width="1000px" src="https://github.com/user-attachments/assets/e6fb474f-b15f-4155-85ac-d4894686c7f7"><br>Rosana´s hands-on<br></h6>

<br>
<h2 align="center">Task 7 . Conclusion</h2>
<p>Great job exploring the Linux log sources! In the upcoming rooms, you will put this knowledge into action to trace and investigate a variety of threats targeting Linux systems. From the Initial Access to the final attack steps, you may need all learned log sources to fully uncover the breaches.</p>p>

<h3 align="center">Key Takeaways</h3>h3>
<p>

- Linux logging can be chaotic, but it often stores enough details to detect the threat<br>
- Logs are kept in /var/log/ folder by default and are usually stored in plain text<br>
-  The top three log sources for SOC are auth.log, app-specific logs, and runtime logs<br>
-  Bash history is unreliable for SOC; better use auditd or an alternative solution</p>

<p><em>Answer the question below</em></p>

<p>7.1. Complete the room!<br>
<code>No answer needed</code></p>

<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/ca43a8f9-1d25-416e-bb5e-2a93be9af1eb"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/6ce795f3-0f90-4197-a753-f0b98d75235c"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, September</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|17      |Easy 🔗 - <code><strong>Linux Logging for SOC</strong></code>| 499| 108ᵗʰ| 5ᵗʰ|     365ᵗʰ    |     7ᵗʰ    | 126,420  |    965    |    74     |
|16      |Hard 🚩 - TryHack3M: TriCipher Summit  | 498    |     107ᵗʰ    |      4ᵗʰ     |     364ᵗʰ    |     7ᵗʰ    | 126,420  |    966    |    74     |
|16      |Easy 🔗 - Chaining Vulnerabilities     | 498    |     108ᵗʰ    |      5ᵗʰ     |     365ᵗʰ    |     7ᵗʰ    | 126,420  |    965    |    74     |
|15      |Medium 🔗 - AppSec IR                  | 497    |     108ᵗʰ    |      5ᵗʰ     |     352ⁿᵈ    |     7ᵗʰ    | 126,404  |    964    |    74     |
|14      |Hard 🚩 - Misguided Ghosts, in progress| 496    |     108ᵗʰ    |      5ᵗʰ     |     389ᵗʰ    |     6ᵗʰ    | 126,300  |    963    |    74     |
|14      |Hard 🚩 - VulnNet: Endgame             | 496    |     108ᵗʰ    |      5ᵗʰ     |     394ᵗʰ    |     6ᵗʰ    | 126,270  |    963    |    74     |
|13      |Hard 🚩 - Royal Router                 | 495    |     107ᵗʰ    |      5ᵗʰ     |     388ᵗʰ    |     6ᵗʰ    | 126,160  |    962    |    74     |
|13      |Medium 🚩 - Void Execution             | 495    |     107ᵗʰ    |      5ᵗʰ     |     383ʳᵈ    |     6ᵗʰ    | 126,120  |    961    |    73     |
|12      |Easy 🚩 - Invite Only                  | 494    |     110ᵗʰ    |      5ᵗʰ     |     352ⁿᵈ    |     6ᵗʰ    | 126,056  |    960    |    73     |
|12      |Medium 🚩 - Devie                      | 494    |     110ᵗʰ    |      5ᵗʰ     |     607ᵗʰ    |     9ᵗʰ    | 125,606  |    959    |    73     |
|11      |Medium 🚩 - Backtrack, in progress     | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ    |     9ᵗʰ    | 125,516  |    958    |    73     |
|11      |Easy 🔗 - Detecting Web Attacks        | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ    |     9ᵗʰ    | 125,516  |    958    |    73     |
|10      |Easy 🔗 - Attacking ICS Plant #1       | 492    |     110ᵗʰ    |      5ᵗʰ     |     675ᵗʰ    |     9ᵗʰ    | 125,428  |    957    |    73     |
|10      |Easy 🔗 - SOC Role in Blue Team        | 492    |     110ᵗʰ    |      5ᵗʰ     |     664ᵗʰ    |     9ᵗʰ    | 125,292  |    956    |    73     |
|9       |Hard 🚩 - Python Playground            | 491    |     111ˢᵗ    |      5ᵗʰ     |     693ʳᵈ    |     9ᵗʰ    | 125,236  |    955    |    73     |
|9       |Hard 🚩 - Borderlands                  | 491    |     111ˢᵗ    |      5ᵗʰ     |     713ʳᵈ    |    10ᵗʰ    | 125,146  |    954    |    73     |
|9       |Medium 🚩 - Forgotten Implant          | 491    |     112ⁿᵈ    |      5ᵗʰ     |     660ᵗʰ    |    10ᵗʰ    | 125,016  |    953    |    73     |
|8       |Easy 🔗 - Web Enumeration              | 490    |     112ⁿᵈ    |      5ᵗʰ     |     663ʳᵈ    |    10ᵗʰ    | 124,986  |    952    |    73     |
|8       |Easy 🔗 - iOS: Forensics               | 490    |     113ʳᵈ    |      5ᵗʰ     |     548ᵗʰ    |     9ᵗʰ    | 124,850  |    951    |    73     |
|7       |Medium 🚩 - VulnNet: Active            | 489    |     114ᵗʰ    |      5ᵗʰ     |     542ⁿᵈ    |     9ᵗʰ    | 124,746  |    950    |    73     |
|7       |Medium 🚩 - pyLon                      | 489    |     114ᵗʰ    |      5ᵗʰ     |     535ᵗʰ    |     9ᵗʰ    | 124,716  |    949    |    73     |
|7       |Medium 🚩 - Pressed                    | 489    |     113ʳᵈ    |      5ᵗʰ     |     508ᵗʰ    |     9ᵗʰ    | 124,886  |    948    |    73     |
|6       |Easy 🚩 - Classic Passwd               | 488    |     114ᵗʰ    |      5ᵗʰ     |     683ʳᵈ    |    12ⁿᵈ    | 124,476  |    947    |    73     |
|6       |Medium 🚩 - toc2                       | 488    |     114ᵗʰ    |      5ᵗʰ     |     695ᵗʰ    |    12ⁿᵈ    | 124,446  |    946    |    73     |
|6       |Hard 🚩 - Extract                      | 488    |     114ᵗʰ    |      5ᵗʰ     |     716ᵗʰ    |    13ʳᵈ    | 124,386  |    945    |    73     |
|6       |Medium 🚩 - Plotted-EMR                | 488    |     114ᵗʰ    |      5ᵗʰ     |     844ᵗʰ    |    12ⁿᵈ    | 124,326  |    944    |    73     |
|5       |Medium 🚩 - Inferno                    | 487    |     114ᵗʰ    |      5ᵗʰ     |     758ᵗʰ    |    12ⁿᵈ    | 124,236  |    943    |    73     |
|5       |Easy 🔗 - Psycho Break                 | 487    |     115ᵗʰ    |      5ᵗʰ     |     724ᵗʰ    |    10ᵗʰ    | 124,152  |    942    |    73     |
|4       |Medium 🚩 - Cold VVars                 | 486    |     113ʳᵈ    |      5ᵗʰ     |     579ᵗʰ    |    10ᵗʰ    | 124,048  |    941    |    73     |
|4       |Medium 🔗 - IP and Domain Threat Intel | 486    |     113ʳᵈ    |	    5ᵗʰ     |     579ᵗʰ     |    10ᵗʰ    | 124,018  |   940     |    73     |
|3       |Easy 🔗 - Malware Classification       | 485    |     112ⁿᵈ    |      5ᵗʰ     |     714ᵗʰ    |    13ʳᵈ    | 123,882  |    939    |    73     |
|2       |Medium 🔗 - Session Forensics          | 484    |     111ˢᵗ    |      5ᵗʰ     |     706ᵗʰ    |    14ᵗʰ    | 123,786  |    938    |    73     |
|1       |Medium 🚩 - Voyage                     | 483    |     111ˢᵗ    |      5ᵗʰ     |     849ᵗʰ    |    15ᵗʰ    | 123,636  |    937    |    73     |

</h6></div><br>

<br>

<p align="center">Global All Time:   108ᵗʰ<br><img width="250px"  src="https://github.com/user-attachments/assets/07e7aea8-bc4a-411c-876c-e4f94282d626"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/d75449a7-d6e0-418d-9d51-2271549a98e4"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/d0b61639-3279-4c0a-8b7d-22c4e11c2f62"><br>
                  Global monthly:    365ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/dd292cc7-02ad-4703-85c9-3976a5bcba24"><br>
                  Brazil monthly:      7ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/c190f845-1b7f-4935-ab5d-8a2e245d52ff"><br>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
