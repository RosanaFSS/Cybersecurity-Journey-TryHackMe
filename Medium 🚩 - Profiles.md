<h1 align="center">Profiles</h1>
<p align="center">2025, October 7<br>Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>519</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>No profile? No problem</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/c35ae659-464e-4886-96fe-7599c5a6a72a"><br>
Access it <a href="https://tryhackme.com/room/profilesroom">here</a>.<br>
<img width="1200px" src=""></p>


<h2>Task 1 . The Incident</h2>
<p>The incident response team has alerted you that there was some suspicious activity on one of the Linux database servers.<br>

A memory dump of the server was taken and provided to you for analysis. You advise the team that you are missing crucial information from the server, but it has already been taken offline. They just made your job a little harder, but not impossible.<br>

Click on the <strong>Download Task Files</strong> button at the top of this task. You will be provided with an <strong>evidence.zip</strong> file.<br>

Extract the zip file's contents and begin your analysis in order to answer the questions.<br>
Note: The challenge is best done using your own environment. I recommend using Volatility 2.6.1 to handle this task and strongly advise using this article by Sean Whalen to aid you with the Volatility installation.</p>

<p><em>Answer the questions below</em></p>

<p>1.1. What is the exposed root password?<br>
<code>Ftrccw45PHyq</code></p>

```bash
$ strings -a -td linux.mem > challenge_strings.txt
```

```bash
$ grep -E 'su root' challenge_strings.txt
789842768 su root
794655216 _CMDLINE=su root
2810770992 _CMDLINE=su root
2814347152 su root
3799619328 su root
3853033984 su rootFtrccw45PHyq
4169226848 su root
```

<img width="1687" height="128" alt="image" src="https://github.com/user-attachments/assets/e1b01cb8-79c1-40b1-b619-70236d5ca344" />

<br>
<br>
<p>1.2. And what time was the users.db file approximately accessed? Format is YYYY-MM-DD HH:MM:SS<br>
<code>2023-11-07 03:49:45</code></p>

<p>

<p>Extracted and ordered by time. Analyzed.</p>

```bash
$ grep -E '7 03:[0-6][0-9]:[0-6][0-9]' challenge_strings.txt | awk '{match($0, /03:[0-9]{2}:[0-9]{2}/); print substr($0, RSTART, RLENGTH), $0}' | sort | cut -d' ' -f2-
```

<p>Extracted just the ones with timestamp.</p>

```bash
$ grep '7 03:' challenge_strings.txt > timed.txt
```

<p>Filtered paco:<br>

- 03:49:45<br>. <code>dbserver</code> systemd[1]: Started Session 3 of user paco.<br>. sshd[1002]: pam_unix(sshd:session): session opened for user paco by (uid=0)<br>. <code>dbserver</code> sshd[1002]: Accepted password for paco from 10.0.2.72 port 53888 ssh2<br>. <code>dbserver</code> sshd[1002]: pam_unix(sshd:session): session opened for user paco by (uid=0)<br>. <code>dbserver</code> systemd-logind[676]: New session 3 of user paco.</p>

```bash
$ grep 'paco' timed.txt
807196161 Nov  7 03:49:18 dbserver systemd[1]: Started Session 1 of user paco.
807196550 Nov  7 03:49:45 dbserver systemd[1]: Started Session 3 of user paco.
2793951809 Nov  7 03:49:18 dbserver systemd[1]: Started Session 1 of user paco.
2793952198 Nov  7 03:49:45 dbserver systemd[1]: Started Session 3 of user paco.
4013805672  7 03:49:45 sshd[1002]: pam_unix(sshd:session): session opened for user paco by (uid=0)
4016538728  7 03:51:18 su: (to root) paco on none
4055703654 iP 7 03:49:18 systemd[1]: Started Session 1 of user paco.
4094508163 Nov  7 03:41:43 dbserver sshd[826]: pam_unix(sshd:session): session opened for user paco by (uid=0)
4094508263 Nov  7 03:41:43 dbserver systemd-logind[681]: New session 1 of user paco.
4094508337 Nov  7 03:41:43 dbserver systemd: pam_unix(systemd-user:session): session opened for user paco by (uid=0)
4094508443 Nov  7 03:41:53 dbserver su: pam_unix(su:auth): authentication failure; logname=paco uid=1000 euid=0 tty=pts/0 ruser=paco rhost=  user=root
4094508583 Nov  7 03:41:55 dbserver su: FAILED SU (to root) paco on pts/0
4094508646 Nov  7 03:42:05 dbserver su: (to root) paco on pts/0
4094508699 Nov  7 03:42:05 dbserver su: pam_unix(su:session): session opened for user root by paco(uid=1000)
4094509414 Nov  7 03:45:37 dbserver sshd[822]: Accepted password for paco from 10.0.2.72 port 49606 ssh2
4094509508 Nov  7 03:45:37 dbserver sshd[822]: pam_unix(sshd:session): session opened for user paco by (uid=0)
4094509608 Nov  7 03:45:37 dbserver systemd-logind[676]: New session 1 of user paco.
4094509682 Nov  7 03:45:37 dbserver systemd: pam_unix(systemd-user:session): session opened for user paco by (uid=0)
4094509788 Nov  7 03:46:02 dbserver su: (to root) paco on pts/0
4094509841 Nov  7 03:46:02 dbserver su: pam_unix(su:session): session opened for user root by paco(uid=1000)
4094510556 Nov  7 03:49:18 dbserver sshd[819]: Accepted password for paco from 10.0.2.72 port 54510 ssh2
4094510650 Nov  7 03:49:18 dbserver sshd[819]: pam_unix(sshd:session): session opened for user paco by (uid=0)
4094510750 Nov  7 03:49:18 dbserver systemd-logind[676]: New session 1 of user paco.
4094510824 Nov  7 03:49:18 dbserver systemd: pam_unix(systemd-user:session): session opened for user paco by (uid=0)
4094510930 Nov  7 03:49:31 dbserver su: (to root) paco on pts/0
4094510983 Nov  7 03:49:31 dbserver su: pam_unix(su:session): session opened for user root by paco(uid=1000)
4094511268 Nov  7 03:49:38 dbserver sshd[958]: Disconnected from user paco 10.0.2.72 port 54510
4094511353 Nov  7 03:49:38 dbserver sshd[819]: pam_unix(sshd:session): session closed for user paco
4094511606 Nov  7 03:49:45 dbserver sshd[1002]: Accepted password for paco from 10.0.2.72 port 53888 ssh2
4094511701 Nov  7 03:49:45 dbserver sshd[1002]: pam_unix(sshd:session): session opened for user paco by (uid=0)
4094511802 Nov  7 03:49:45 dbserver systemd-logind[676]: New session 3 of user paco.
4094511876 Nov  7 03:51:18 dbserver su: (to root) paco on none
4104415033 Nov  7 03:45:37 dbserver systemd[1]: Started Session 1 of user paco.
```


```bash
$ python3 vol.py -f linux.mem banners.Banners
Volatility 3 Framework 2.27.0
Progress:  100.00               PDB scanning finished
Offset  Banner

0x2f9c4c88      Linux version 5.4.0-166-generic (buildd@lcy02-amd64-011) (gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.2)) #183-Ubuntu SMP Mon Oct 2 11:28:33 UTC 2023 (Ubuntu 5.4.0-166.183-generic 5.4.252)
0xa707c8c8      Linux version 5.4.0-166-generic (buildd@lcy02-amd64-011) (gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.2)) #183-Ubuntu SMP Mon Oct 2 11:28:33 UTC 2023 (Ubuntu 5.4.0-166.183-generic 5.4.252)
0xd46001a0      Linux version 5.4.0-166-generic (buildd@lcy02-amd64-011) (gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.2)) #183-Ubuntu SMP Mon Oct 2 11:28:33 UTC 2023 (Ubuntu 5.4.0-166.183-generic 5.4.252)
0xd619de54      Linux version 5.4.0-166-generic (buildd@lcy02-amd64-011) (gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.2)) #183-Ubuntu SMP Mon Oct 2 11:28:33 UTC 2023 (Ubuntu 5.4.0-166.183-generic 5.4.252)
0x106d64c88     Linux version 5.4.0-166-generic (buildd@lcy02-amd64-011) (gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.2)) #183-Ubuntu SMP Mon Oct 2 11:28:33 UTC 2023 (Ubuntu 5.4.0-166.183-generic 5.4.252)
```

<img width="1892" height="168" alt="image" src="https://github.com/user-attachments/assets/d78403c1-9670-4779-9683-5bfdb86f15dc" />




<img width="1606" height="97" alt="image" src="https://github.com/user-attachments/assets/3e7508b5-ac04-4fe5-9753-ddf6bec1a646" />



<p>1.3. What is the MD5 hash of the malicious file found?<br>
<code>______________________</code></p>


```bash
(volatility) ...$ python3 vol.py -f linux.mem linux.pagecache.InodePages --find /home/paco/pkexecc --dump pkexecc
```

<br>
<p>1.4. What is the IP address and port of the malicious actor? Format is IP:Port<br>
<code>10.0.2.72:1337</code></p>

```bash
$ cat challenge_strings.txt | grep success | grep -E hostname=
788623280 op=PAM:session_open grantors=pam_selinux,pam_loginuid,pam_keyinit,pam_permit,pam_umask,pam_unix,pam_systemd,pam_mail,pam_limits,pam_env,pam_env,pam_selinux acct="root" exe="/usr/sbin/sshd" hostname=10.0.2.72 addr=10.0.2.72 terminal=ssh res=success
794885520 op=PAM:setcred grantors=pam_permit,pam_cap acct="paco" exe="/usr/sbin/sshd" hostname=10.0.2.72 addr=10.0.2.72 terminal=ssh res=success
797840336 unit=user-runtime-dir@0 comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=success
797849440 unit=user@1000 comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=success
798330560 unit=networkd-diunit=user@1000 comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=success
```

```bash
$ cat challenge_strings.txt  | grep '03:49:' | grep 10.0.2.72
792046608 Nov  7 03:49:18 2023 from 10.0.2.72
792945836 Last login: Tue Nov  7 03:49:18 2023 from 10.0.2.72
813562668 Last login: Tue Nov  7 03:49:18 2023 from 10.0.2.72
```

```bash
$ cat challenge_strings.txt  | grep 'login' | grep 10.0.2.72
788623280 op=PAM:session_open grantors=pam_selinux,pam_loginuid,pam_keyinit,pam_permit,pam_umask,pam_unix,pam_systemd,pam_mail,pam_limits,pam_env,pam_env,pam_selinux acct="root" exe="/usr/sbin/sshd" hostname=10.0.2.72 addr=10.0.2.72 terminal=ssh res=success
792945836 Last login: Tue Nov  7 03:49:18 2023 from 10.0.2.72
802203095 ntors=pam_selinux,pam_loginuid,pam_keyinit,pam_permit,pam_umask,pam_unix,pam_systemd,pam_mail,pam_limits,pam_env,pam_env,pam_selinux acct="paco" exe="/usr/sbin/sshd" hostname=10.0.2.72 addr=10.0.2.72 terminal=ssh res=success
805753872 op=login id=1000 exe="/usr/sbin/sshd" hostname=10.0.2.72 addr=10.0.2.72 terminal=/dev/pts/0 res=success
813562668 Last login: Tue Nov  7 03:49:18 2023 from 10.0.2.72
821611600 op=login id=1000 exe="/usr/sbin/sshd" hostname=10.0.2.72 addr=10.0.2.72 terminal=/dev/pts/0 res=success
```

<br>
<p>1.5. What is the full path of the cronjob file and its inode number? Format is filename:inode number<br>
<code>/var/spool/cron/crontabs/root:******</code></p>

```bash
$ cat challenge_strings.txt | grep 'crontab' | sort
2794780940 crontab:x:105:
2800802112 crontabs/root
2800804240 echo '* * * * * cp /opt/.bashrc /root/.bashrc' >> /crontabs/root
2800804384 echo '* * * * * cp /opt/.bashrc /root/.bashrc' >> /var/spool/cron/crontabs/root
2800804656 crontabs/root
2811377564 crontab:x:105:
2821608752 echo '* * * * * cp /opt/.bashrc /root/.bashrc' >> /var/spool/cron/crontabs/root
2821609056 /var/spool/cron/crontabs/root
2831895612 Nov  7 03:52:01 dbserver cron[653]: (root) INSECURE MODE (mode 0600 expected) (crontabs/root)
2832019324 crontab:x:105:
3766027520 crontab
3766062588 crontab:x:105:
3777316064 crontabs/root
3837163628 crontab:x:105:
3850116140 crontab:x:105:
3850347340 crontab:x:105:
3851054988 crontab:x:105:
3868154672 <78>Nov  7 03:52:01 cron[653]: (root) INSECURE MODE (mode 0600 expected) (crontabs/root)
3885059984 crontabZ1
3973092864 MESSAGE=(root) INSECURE MODE (mode 0600 expected) (crontabs/root)
4055705702 aP 7 03:52:01 cron[653]: (root) INSECURE MODE (mode 0600 expected) (crontabs/root)
4101957468 crontab:x:105:
4102338592 root) INSECURE MODE (mode 0600 expected) (crontabs/root)gent.e..restricted).eb browsers).0000:00:03.0': not supported by any plugin
4102969760 <78>Nov  7 03:52:01 cron[653]: (root) INSECURE MODE (mode 0600 expected) (crontabs/root)
4114833051 crontabs
4114833060 /etc/crontab
4114833520 Error: %s; while reading crontab for user %s
4114833568 fdopen on crontab_fd in load_user
4114833880 Missing newline before EOF, this crontab file will be ignored
4114833944 Syntax error, this crontab file will be ignored
4114833992 crontab must not be longer than 10000 lines, this crontab file will be ignored
4114834071 Out of memory parsing crontab
4121795744 crontabs
4130013516 crontab:x:105:
4170038368 # /etc/crontab: system-wide crontab
4170038404 # Unlike any other crontab you don't have to run the `crontab'
4170038595 # that none of the other crontabs do.
4170753024 :01 cron[653]: (root) INSECURE MODE (mode 0600 expected) (crontabs/root)
4170914108 crontab:x:10
4185965159 I 7 03:52:01 cron[653]: (root) INSECURE MODE (mode 0600 expected) (crontabs/root)
4192950616 crontab
4192950808 crontabs
4223050740 crontabt
773836796 Nov  7 03:52:01 dbserver cron[653]: (root) INSECURE MODE (mode 0600 expected) (crontabs/root)
773960508 crontab:x:105:
788715760 echo '* * * * * cp /opt/.bashrc /root/.bashrc' >> /var/spool/cron/crontabs/root
788716064 /var/spool/cron/crontabs/root
795261788 crontab:x:105:
805657856 crontabs/root
805659984 echo '* * * * * cp /opt/.bashrc /root/.bashrc' >> /var/spool/cron/crontabs/root
805660128 echo '* * * * * cp /opt/.bashrc /root/.bashrc' >> /var/spool/cron/crontabs/root
805660400 crontabs/root
808025292 crontab:x:105:
```




<br>
<p>1.6. What command is found inside the cronjob file?r<br>
<code>______________</code></p>







<br>
<br>





