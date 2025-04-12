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

<p>Once we have identified the OS and account information, we can start looking into the system configuration of the host.</p>

<h3>Hostname</h3>

<p>The hostname is stored in the <code>/etc/hostname</code> file on a Linux Host. It can be accessed using the <code>cat</code> utility.</p>

<p><em>Hostname</em></p>

```bash
user@machine$ cat /etc/hostname 
tryhackme

```

<br>

<h3>Timezone</h3>

<p>Timezone information is a significant piece of information that gives an indicator of the general location of the device or the time window it might be used in. Timezone information can be found at the location <code>/etc/timezone</code> and it can be read using the <code>cat</code> utility.</p>

<p><em>Timezone</em></p>

```bash
user@machine$ cat /etc/timezone
Etc/UTC

```

<br>

<h3>Network Configuration</h3>

<p>To find information about the network interfaces, we can <code>cat</code> the <code>/etc/network/interfaces</code> file. The output on your machine might be different from the one shown here, depending on your configuration.</p>

<p><em>Network Configuration</em></p>

```bash
user@machine$ cat /etc/network/interfaces
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/*

# The loopback network interface
auto lo
iface lo inet loopback

auto eth0
iface eth0 inet dhcp

```

<br>

<p>Similarly, to find information about the MAC and IP addresses of the different interfaces, we can use the <code>ip</code> utility. To learn more about the <code>ip</code> utility, we can see its <code>man</code> page.<br>

<code>man ip/code><br>

The below terminal shows the usage of the <code>ip</code> utility. Note that this will only be helpful on a live system.</p>

<p><em>IP Information</em></p>

```bash
user@machine$ ip address show 
1: lo:  mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0:  mtu 9001 qdisc mq state UP group default qlen 1000
    link/ether 02:20:61:f1:3c:e9 brd ff:ff:ff:ff:ff:ff
    inet 10.10.95.252/16 brd 10.10.255.255 scope global dynamic eth0
       valid_lft 2522sec preferred_lft 2522sec
    inet6 fe80::20:61ff:fef1:3ce9/64 scope link 
       valid_lft forever preferred_lft forever

```

<br>

<h3>Active network connections</h3>

<p>On a live system, knowing the active network connections provides additional context to the investigation. We can use the <code>netstat</code> utility to find active network connections on a Linux host. We can learn more about the <code>netstat</code> utility by reading its <code>man</code> page.<br>

<code>man netstat</code><br>

The below terminal shows the usage of the <code>netstat</code> utility.</p>

<p><em>Active network connections</em></p>

```bash
user@machine$ netstat -natp
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.1:5901          0.0.0.0:*               LISTEN      829/Xtigervnc       
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:631           0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:60602         127.0.0.1:5901          ESTABLISHED -                   
tcp        0      0 10.10.95.252:57432      18.66.171.77:443        ESTABLISHED -                   
tcp        0      0 10.10.95.252:80         10.100.1.33:51934       ESTABLISHED -                   
tcp        0      0 127.0.0.1:5901          127.0.0.1:60602         ESTABLISHED 829/Xtigervnc       
tcp6       0      0 ::1:5901                :::*                    LISTEN      829/Xtigervnc       
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
tcp6       0      0 ::1:631                 :::*                    LISTEN      -               
```

<h3>Running processes</h3>

<p>If performing forensics on a live system, it is helpful to check the running processes. The  <code>ps</code> utility shows details about the running processes. To find out about the <code>ps</code> utility, we can use the <code>man</code> page.</p>

<code>man ps</code><br>

The below terminal shows the usage of the <code>ps</code> utility.</p>

<p><em>Running processes</em></p>

```bash
user@machine$ ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         729  0.0  0.0   7352  2212 ttyS0    Ss+  17:28   0:00 /sbin/agetty -o -p -- \u --keep-baud 115200,38400,9600 ttyS0 vt220
root         738  0.0  0.0   5828  1844 tty1     Ss+  17:28   0:00 /sbin/agetty -o -p -- \u --noclear tty1 linux
root         755  0.0  1.5 272084 63736 tty7     Ssl+ 17:28   0:00 /usr/lib/xorg/Xorg -core :0 -seat seat0 -auth /var/run/lightdm/root/:0 -nolisten tcp vt7 -novtswitch
ubuntu      1672  0.0  0.1   5264  4588 pts/0    Ss   17:29   0:00 bash
ubuntu      1985  0.0  0.0   5892  2872 pts/0    R+   17:40   0:00 ps au          
```

<br>

<h3>DNS Information</h3>

<p>The file <code>/etc/hosts</code> contains the configuration for the DNS name assignment. We can use the <code>cat</code> utility to read the hosts file. To learn more about the hosts file, we can use the <code>man</code> page.<br>

<code>man hosts</code><br>

The below terminal shows a sample output of the hosts file.</p>


<p><em>hosts file</em></p>

```bash
user@machine$ cat /etc/hosts
127.0.0.1 localhost

# The following lines are desirable for IPv6 capable hosts
::1 ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
ff02::3 ip6-allhosts     
```

<p>The information about DNS servers that a Linux host talks to for DNS resolution is stored in the resolv.conf file. Its location is <code>/etc/resolv.conf</code>. We can use the <code>cat</code> utility to read this file.</p>

<p><em>Resolv.conf</em></p>

```bash
user@machine$ cat /etc/resolv.conf 
# This file is managed by man:systemd-resolved(8). Do not edit.
#
# This is a dynamic resolv.conf file for connecting local clients to the
# internal DNS stub resolver of systemd-resolved. This file lists all
# configured search domains.
#
# Run "resolvectl status" to see details about the uplink DNS servers
# currently in use.
#
# Third party programs must not access this file directly, but only through the
# symlink at /etc/resolv.conf. To manage man:resolv.conf(5) in a different way,
# replace this symlink by a static file or a different symlink.
#
# See man:systemd-resolved.service(8) for details about the supported modes of
# operation for /etc/resolv.conf.

nameserver 127.0.0.53
options edns0 trust-ad
search eu-west-1.compute.internal
```

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 4.1. <em>What is the hostname of the attached VM?</em><br><a id='4.1'></a>
>> <strong><code>Linux4n6</code></strong><br>
<p></p>

<br>

> 4.2. <em>What is the timezone of the attached VM?</em><br><a id='4.2'></a>
>> <strong><code>Asia/Karachi</code></strong><br>
<p></p>

<br>

> 4.3. <em>What program is listening on the address 127.0.0.1:5901?</em><br><a id='4.3'></a>
>> <strong><code>Xtigervnc</code></strong><br>
<p></p>

<br>

> 4.4. <em>What is the full path of this program?</em><br><a id='4.4'></a>
>> <strong><code>/usr/bin/Xtigervnc</code></strong><br>
<p></p>

<br>

> 4.5. <em>Read about the flags used above with the netstat and ps commands in their respective man pages.</em><br><a id='4.5'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br><br>

<h2>Task 5 . Persistance Mechanisms</h2>
<p>Knowing the environment we are investigating, we can then move on to finding out what persistence mechanisms exist on the Linux host under investigation. Persistence mechanisms are ways a program can survive after a system reboot. This helps malware authors retain their access to a system even if the system is rebooted. Let's see how we can identify persistence mechanisms in a Linux host.</p>

<h3>Cron jobs</h3>

<p>Cron jobs are commands that run periodically after a set amount of time. A Linux host maintains a list of Cron jobs in a file located at <code>/etc/crontab</code>. We can read the file using the <code>cat</code> utility.</p>

<p><em>Ccron jobs</em></p>

```bash
user@machine$ cat /etc/crontab 
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name command to be executed
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#
```

<p>The above terminal output shows the contents of a sample /etc/crontab file. As can be seen, the file contains information about the time interval after which the command has to run, the username that runs the command, and the command itself. It can also contain scripts to run, where the script that needs to be run will be placed on the disk, and the command to run it will be added to this file.</p>

<h3>Service startup</h3>

<p>Like Windows, services can be set up in Linux that will start and run in the background after every system boot. A list of services can be found in the <code>/etc/init.d</code> directory. We can check the contents of the directory by using the <code>ls</code> utility.</p>

<p><em>Ccron jobs</em></p>

```bash
user@machine$ ls /etc/init.d/
acpid       avahi-daemon      cups          hibagent           kmod             networking     pppd-dns                     screen-cleanup     unattended-upgrades
alsa-utils  bluetooth         cups-browsed  hwclock.sh         lightdm          open-iscsi     procps                       speech-dispatcher  uuidd
anacron     console-setup.sh  dbus          irqbalance         lvm2             open-vm-tools  pulseaudio-enable-autospawn  spice-vdagent      whoopsie
apparmor    cron              gdm3          iscsid             lvm2-lvmpolld    openvpn        rsync                        ssh                x11-common
apport      cryptdisks        grub-common   kerneloops         multipath-tools  plymouth       rsyslog                      udev
atd         cryptdisks-early  hddtemp       keyboard-setup.sh  network-manager  plymouth-log   saned                        ufw
```

<h3>.Bashrc</h3>

<p>When a bash shell is spawned, it runs the commands stored in the <code>.bashrc</code> file. This file can be considered as a startup list of actions to be performed. Hence it can prove to be a good place to look for persistence. <br>

The following terminal shows an example .bashrc file.</p>

<p><em>Bashrc</em></p>

```bash
user@machine$ cat ~/.bashrc
# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi
```

<p>System-wide settings are stored in <code>/etc/bash.bashrc</code> and <code>/etc/profile</code> files, so it is often a good idea to take a look at these files as well.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 5.1. <em>In the bashrc file, the size of the history file is defined. What is the size of the history file that is set for the user Ubuntu in the attached machine?</em><br><a id='5.1'></a>
>> <strong><code>2000</code></strong><br>
<p></p>

<br><br>

<h2>Task 6 . Evidence of Execution</h2>

<p>Knowing what programs have been executed on a host is one of the main purposes of performing forensic analysis. On a Linux host, we can find the evidence of execution from the following sources.</p>

<h3>Sudo Execution history</h3>
<p>All the commands that are run on a Linux host using <code>sudo</code> are stored in the auth log. We already learned about the auth log in Task 3. We can use the <code>grep</code> utility to filter out only the required information from the auth log.</p>

<p><em>Auth logs</em></p>

```bash
user@machine$ cat /var/log/auth.log* |grep -i COMMAND|tail
Mar 29 17:28:58 tryhackme pkexec[1618]: ubuntu: Error executing command as another user: Not authorized [USER=root] [TTY=unknown] [CWD=/home/ubuntu] [COMMAND=/usr/lib/update-notifier/package-system-locked]
Mar 29 17:49:52 tryhackme sudo:   ubuntu : TTY=pts/0 ; PWD=/home/ubuntu ; USER=root ; COMMAND=/usr/bin/cat /etc/sudoers
Mar 29 17:55:22 tryhackme sudo:   ubuntu : TTY=pts/0 ; PWD=/home/ubuntu ; USER=root ; COMMAND=/usr/bin/cat /var/log/btmp
Mar 29 17:55:39 tryhackme sudo:   ubuntu : TTY=pts/0 ; PWD=/home/ubuntu ; USER=root ; COMMAND=/usr/bin/cat /var/log/wtmp
Mar 29 18:00:54 tryhackme sudo:   ubuntu : TTY=pts/0 ; PWD=/home/ubuntu ; USER=root ; COMMAND=/usr/bin/tail -f /var/log/btmp
Mar 29 18:01:24 tryhackme sudo:   ubuntu : TTY=pts/0 ; PWD=/home/ubuntu ; USER=root ; COMMAND=/usr/bin/last -f /var/log/btmp
Mar 29 18:03:58 tryhackme sudo:   ubuntu : TTY=pts/0 ; PWD=/home/ubuntu ; USER=root ; COMMAND=/usr/bin/last -f /var/log/wtmp
Mar 29 18:05:41 tryhackme sudo:   ubuntu : TTY=pts/0 ; PWD=/home/ubuntu ; USER=root ; COMMAND=/usr/bin/last -f /var/log/btmp
Mar 29 18:07:51 tryhackme sudo:   ubuntu : TTY=pts/0 ; PWD=/home/ubuntu ; USER=root ; COMMAND=/usr/bin/last -f /var/log/utmp
Mar 29 18:08:13 tryhackme sudo:   ubuntu : TTY=pts/0 ; PWD=/home/ubuntu ; USER=root ; COMMAND=/usr/bin/last -f /var/run/utmp

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

<p>The above terminal shows commands run by the user ubuntu using <code>sudo</code>.</p>

<h3>Bash history</h3>

<p>Any commands other than the ones run using <code>sudo</code> are stored in the bash history. Every user's bash history is stored separately in that user's home folder. Therefore, when examining bash history, we need to get the bash_history file from each user's home directory. It is important to examine the bash history from the root user as well, to make note of all the commands run using the root user as well.</p>

<p><em>Bash history</em></p>

```bash
user@machine$ cat ~/.bash_history 
cd Downloads/
ls
unzip PracticalMalwareAnalysis-Labs-master.zip 
cd PracticalMalwareAnalysis-Labs-master/
ls
cd ..
ls
rm -rf sality/
ls
mkdir wannacry
mv Ransomware.WannaCry.zip wannacry/
cd wannacry/
unzip Ransomware.WannaCry.zip 
cd ..
rm -rf wannacry/
ls
mkdir exmatter
mv 325ecd90ce19dd8d184ffe7dfb01b0dd02a77e9eabcb587f3738bcfbd3f832a1.7z exmatter/
cd exmatter/
strings -d 325ecd90ce19dd8d184ffe7dfb01b0dd02a77e9eabcb587f3738bcfbd3f832a1|sort|uniq>str-sorted
cd ..
ls
```

<h3>Files accessed using vim</h3>

<p>The Vim text editor stores logs for opened files in Vim in the file named .viminfo in the home directory. This file contains command line history, search string history, etc. for the opened files. We can use the cat utility to open .viminfo.</p>

<p><em>Viminfo</em></p>

```bash
user@machine$ cat ~/.viminfo
# This viminfo file was generated by Vim 8.1.
# You may edit it if you're careful!

# Viminfo version
|1,4

# Value of 'encoding' when this file was written
*encoding=utf-8


# hlsearch on (H) or off (h):
~h
# Command Line History (newest to oldest):
:q
|2,0,1636562413,,"q"

# Search String History (newest to oldest):

# Expression History (newest to oldest):

# Input Line History (newest to oldest):

# Debug Line History (newest to oldest):

# Registers:

# File marks:
'0  1139  0  ~/Downloads/str
|4,48,1139,0,1636562413,"~/Downloads/str"

# Jumplist (newest first):
-'  1139  0  ~/Downloads/str
|4,39,1139,0,1636562413,"~/Downloads/str"
-'  1  0  ~/Downloads/str
|4,39,1,0,1636562322,"~/Downloads/str"

# History of marks within files (newest to oldest):

> ~/Downloads/str
	*	1636562410	0
	"	1139	0
```


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 6.1. <em>The user tryhackme used apt-get to install a package. What was the command that was issued?</em><br><a id='6.1'></a>
>> <strong><code>sudo apt-get install apache2</code></strong><br>
<p></p>

<br>

> 6.2. <em>What was the current working directory when the command to install net-tools was issued?</em><br><a id='6.2'></a>
>> <strong><code>/home/ubuntu</code></strong><br>
<p></p>

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

