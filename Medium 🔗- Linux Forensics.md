<p align="center">2024<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Linux Forensics}}$$</h1>
<p align="center"><em>Learn about the common forensic artifacts found in the file system of Linux Operating System</em> It is classified as a medium-level walkthrough.<br>
It is premium: only for subscribers.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/linuxforensics">here</a>.</p>

<p align="center"> <img width="900px" src=""> </p>

<br>
<br>

<h2>Task 1 . Introduction</h2>

<p>In the previous few rooms, we learned about performing forensics on Windows machines. While Windows is still the most common Desktop Operating System, especially in enterprise environments, Linux also constitutes a significant portion of the pie. Especially, Linux is very common in servers that host different services for enterprises. 

<h3>LearningObjectives</h3>

<p>After completing this room, we will have learned:<br>

<p>. An introduction to Linux and its different flavors.<br>
.  Finding OS, account, and system information on a Linux machine.<br>
.  Finding information about running processes, executed processes, and processes that are scheduled to run.<br>
.  Finding system log files and identifying information from them.<br>
.  Common third-party applications used in Linux and their logs</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 1.1. <em>Go through the Learning Objectives.</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br><br>

<h2>Task 2 . Linux Forensics</h2>

<p>The Linux Operating System can be found in a lot of places. While it might not be as easy to use as Windows or macOS, it has its own set of advantages that make its use widespread. It is found in the Web servers you interact with, in your smartphone, and maybe, even in the entertainment unit of your car. One of the reasons for this versatility is that Linux is an open-source Operating System with many different flavors. It is also very lightweight and can run on very low resources. It can be considered modular in nature and can be customized as per requirements, meaning that only those components can be installed which are required. All of these reasons make Linux an important part of our lives.<br>

For learning more about Linux, it is highly recommended that you go through the Linux Fundamentals 1, Linux Fundamentals 2, and Linux Fundamentals 3 rooms on TryHackMe.</p>

<h3>Linux Distributions</h3>
<p>Linux comes in many different flavors, also called distributions. There are minor differences between these distributions. Sometimes the differences are mostly cosmetic, while sometimes the differences are a little more pronounced. Some of the common Linux distributions include::<br>

<p align="center"><br><br><img width="400px" src="https://github.com/user-attachments/assets/0d6779b2-d284-454b-a025-a941a364ce8d"> </p>

<p>. An introduction to Linux and its different flavors.<br>
.  Ubuntu<br>
.  Redhat<br>
.  ArchLinux<br>
.  Open SUSE<br>
.  Linux Mint<br>
.  CentOS<br>
.  Debian</p>

<p>For the purpose of this room, we will be working on the Ubuntu distribution. So let's move on to the next task to learn to perform forensics on Linux.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 2.1. <em>Can you tell which distribution is represented by which logo in the image?</em><br><a id='2.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br><br>

<h2>Task 3 . OS and account information</h2>

<br><br>

<h2>Task 4 . System Configuration</h2>

<br><br>

<h2>Task 5 . Persistance Mechanisms</h2>

<br><br>

<h2>Task 6 . Evidence of Execution</h2>

<br><br>

<h2>Task 7 . Log Files</h2>

<p>One of the most important sources of information on the activity on a Linux host is the log files. These log files maintain a history of activity performed on the host and the amount of logging depends on the logging level defined on the system. Let's take a look at some of the important log sources. Logs are generally found in the <code>/var/log</code> directory.</p>

<h3>Syslog</h3>
<p>The Syslog contains messages that are recorded by the host about system activity. The detail which is recorded in these messages is configurable through the logging level. We can use the <code>cat</code> utility to view the Syslog, which can be found in the file <code>/var/log/syslog</code>. Since the Syslog is a huge file, it is easier to use <code>tail</code>,<code>head</code>, <code>more</code> or <code>less</code>utilities to help make it more readable.</p>

<p><em>Syslog</em></p>

```bash
user@machine$ cat /var/log/syslog* | head
Mar 29 00:00:37 tryhackme systemd-resolved[519]: Server returned error NXDOMAIN, mitigating potential DNS violation DVE-2018-0001, retrying transaction with reduced feature level UDP.
Mar 29 00:00:37 tryhackme rsyslogd: [origin software="rsyslogd" swVersion="8.2001.0" x-pid="635" x-info="https://www.rsyslog.com"] rsyslogd was HUPed
Mar 29 00:00:37 tryhackme systemd[1]: man-db.service: Succeeded.
Mar 29 00:00:37 tryhackme systemd[1]: Finished Daily man-db regeneration.
Mar 29 00:09:01 tryhackme CRON[7713]: (root) CMD (   test -x /etc/cron.daily/popularity-contest && /etc/cron.daily/popularity-contest --crond)
Mar 29 00:17:01 tryhackme CRON[7726]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
Mar 29 00:30:45 tryhackme snapd[2930]: storehelpers.go:721: cannot refresh: snap has no updates available: "amazon-ssm-agent", "core", "core18", "core20", "lxd"
Mar 29 00:30:45 tryhackme snapd[2930]: autorefresh.go:536: auto-refresh: all snaps are up-to-date
Mar 29 01:17:01 tryhackme CRON[7817]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
Mar 29 01:50:37 tryhackme systemd[1]: Starting Cleanup of Temporary Directories...

```
<p>The above terminal shows the system time, system name, the process that sent the log [the process id], and the details of the log. We can see a couple of cron jobs being run here in the logs above, apart from some other activity. We can see an asterisk(*) after the syslog. This is to include rotated logs as well. With the passage of time, the Linux machine rotates older logs into files such as syslog.1, syslog.2 etc, so that the syslog file doesn't become too big. In order to search through all of the syslogs, we use the asterisk(*) wildcard.</p>

<h3>Auth logs</h3>
<p>We have already discussed the auth logs in the previous tasks. The auth logs contain information about users and authentication-related logs. The below terminal shows a sample of the auth logs..</p>

<p><em>Auth logs</em></p>

```bash
user@machine$ cat /var/log/auth.log* |head
Feb 27 13:52:33 ip-10-10-238-44 useradd[392]: new group: name=ubuntu, GID=1000
Feb 27 13:52:33 ip-10-10-238-44 useradd[392]: new user: name=ubuntu, UID=1000, GID=1000, home=/home/ubuntu, shell=/bin/bash, from=none
Feb 27 13:52:33 ip-10-10-238-44 useradd[392]: add 'ubuntu' to group 'adm'
Feb 27 13:52:33 ip-10-10-238-44 useradd[392]: add 'ubuntu' to group 'dialout'
Feb 27 13:52:33 ip-10-10-238-44 useradd[392]: add 'ubuntu' to group 'cdrom'
Feb 27 13:52:33 ip-10-10-238-44 useradd[392]: add 'ubuntu' to group 'floppy'
Feb 27 13:52:33 ip-10-10-238-44 useradd[392]: add 'ubuntu' to group 'sudo'
Feb 27 13:52:33 ip-10-10-238-44 useradd[392]: add 'ubuntu' to group 'audio'
Feb 27 13:52:33 ip-10-10-238-44 useradd[392]: add 'ubuntu' to group 'dip'
Feb 27 13:52:33 ip-10-10-238-44 useradd[392]: add 'ubuntu' to group 'video'

```

<p>We can see above that the log stored information about the creation of a new group, a new user, and the addition of the user into different groups.</p>

<h3>Third-party logs</h3>

<p>Similar to the syslog and authentication logs, the <code>/var/log/</code> directory contains logs for third-party applications such as webserver, database, or file share server logs. We can investigate these by looking at the <code>/var/log/</code>code> directory.</p>

<p><em>Third-party logs</em></p>

```bash
user@machine$ ls /var/log
Xorg.0.log          apt                    cloud-init.log  dmesg.2.gz      gdm3                    kern.log.1         prime-supported.log  syslog.2.gz
Xorg.0.log.old      auth.log               cups            dmesg.3.gz      gpu-manager-switch.log  landscape          private              syslog.3.gz
alternatives.log    auth.log.1             dist-upgrade    dmesg.4.gz      gpu-manager.log         lastlog            samba                syslog.4.gz
alternatives.log.1  btmp                   dmesg           dpkg.log        hp                      lightdm            speech-dispatcher    syslog.5.gz
amazon              btmp.1                 dmesg.0         dpkg.log.1      journal                 openvpn            syslog               unattended-upgrades
apache2             cloud-init-output.log  dmesg.1.gz      fontconfig.log  kern.log                prime-offload.log  syslog.1             wtmp
```

<p>As is obvious, we can find the apache logs in the apache2 directory and samba logs in the samba directory.</p>

<p><em>Apache Logs</em></p>

```bash
user@machine$  ls /var/log/apache2/
access.log  error.log  other_vhosts_access.log
```

<p>Similarly, if any database server like MySQL is installed on the system, we can find the logs in this directory.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 7.1. <em>Though the machine's current hostname is the one we identified in Task 4. The machine earlier had a different hostname. What was the previous hostname of the machine?</em><br><a id='7.1'></a>
>> <strong><code>tryhackme</code></strong><br>
<p></p>

<br><br>

<h2>Task 8 . Conclusions</h2>

<p>Well, that's a wrap for this room. That was interesting!!<br>

If you found it difficult to remember all the forensic artifacts, here is a cheatsheet that you can reference. </p>

<br>

<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/f0f87d05-1803-4189-8293-00ca93bc2e05"> </p>

<br>

<p>You can stick around and find out what other exciting artifacts you found in the VM. You can let us know what you found interesting in this room using our Discord channel or Twitter account.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 8.1. <em>Check out the cheat sheet and social links</em><br><a id='8.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

