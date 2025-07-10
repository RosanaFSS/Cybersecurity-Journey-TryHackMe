<h1 align="center">AI Forensics</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/b0287f17-65f7-4d3a-a1cd-c6ba11a21784"><br>
<p align="center">July 9, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, 
and I’m excited to join you on this adventure, part of my <code>429</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Explore AI DFIR and learn how it boosts your investigation capabilities</em>.<br>
Access it <a href=https://tryhackme.com/room/defadversarialattacks"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/13ec6995-ab55-4f35-a5c2-9258b1471fdd"></p>

<h2>Task 1 . Introduction</h2>

<br>

<h2>Task 2 . The AI Forensics Landscape</h2>

<br>

<h2>Task 3 . AI & DFIR</h2>

<br>

<h2>Task 4 . AI Legal & Ethical Implications</h2>

<br>

<h2>Task 5 . Practical - The Digital Trail</h2>

<br>

![image](https://github.com/user-attachments/assets/b370fe9a-7814-47e1-be7f-d7d4ac57bff5)

<br>

```bash
ubuntu@tryhackme:~$ source /opt/dfir-env/bin/activate
```

```bash
ubuntu@tryhackme:~$ python3 /opt/dfir-lab/classify_logs.py /var/log/auth.log
```

![image](https://github.com/user-attachments/assets/4f6f157e-68ca-4d96-a72a-4251122e916c)

<br>

```bash
(dfir-env) ubuntu@tryhackme:~$ python3 /opt/dfir-lab/file_anomalies.py
```

![image](https://github.com/user-attachments/assets/26bf3b6c-4676-460f-9251-aeeb93091889)

```bash
(dfir-env) ubuntu@tryhackme:/home/j.morgan$ ls -la
total 36
drwxr-xr-x 4 j.morgan j.morgan 4096 Jun 12 18:29 .
drwxr-xr-x 5 root     root     4096 May 16 10:02 ..
-rw-r--r-x 1 j.morgan j.morgan  151 Jun 12 18:29 .bash_history
-rw-r--r-x 1 j.morgan j.morgan  220 Feb 25  2020 .bash_logout
-rw-r--r-x 1 j.morgan j.morgan 3771 Feb 25  2020 .bashrc
-rw-r--r-x 1 j.morgan j.morgan  807 Feb 25  2020 .profile
-rw----r-x 1 j.morgan j.morgan  937 May 19 15:44 .viminfo
drwxr-xr-x 3 j.morgan j.morgan 4096 May 16 10:02 Documents
drwxrwxr-x 3 j.morgan j.morgan 4096 May 19 15:43 Mail
```

<br>

<p>

- <code>akeane@poseidonenergy.net</code><br>
- <code>invoice_Q1_2075.ods</code></p>

```bash
(dfir-env) ubuntu@tryhackme:/home/j.morgan/Mail/inbox$ cat email_invoice.eml
From: "A. Keane" <akeane@poseidonenergy.net>
To: j.morgan@robbco.com
Subject: URGENT - Outstanding Invoice Q1 2075

Dear Mr. Morgan,

Please find attached the invoice for the Q1 joint energy terminal upgrade project. This invoice is marked as overdue and must be reviewed immediately by RobbCo engineering.

Failure to process this may result in administrative escalation.

[Attached: invoice_Q1_2075.ods]

Regards,
A. Keane  
Director of Field Operations  
Poseidon Energy  
```

<br>

<p>

- <code>cd ~/Documents/Invoices/</code><br>
- <code>libreoffice invoice_Q1_2075.ods &</code><br>
- <code>sudo nano /home/r.house/.ssh/authorized_key</code></p>

```bash
(dfir-env) ubuntu@tryhackme:~$ cat /tmp/invoice_dump.txt
bash_history:
cd ~/Documents/Invoices/
libreoffice invoice_Q1_2075.ods &
cd ~
ls -la
cat .ssh/config
cat /etc/motd
sudo nano /home/r.house/.ssh/authorized_keys
exit

users:
root
daemon
bin
sys
sync
games
man
lp
mail
news
uucp
proxy
www-data
backup
list
irc
gnats
nobody
systemd-network
systemd-resolve
systemd-timesync
messagebus
syslog
_apt
tss
uuidd
tcpdump
sshd
landscape
pollinate
ec2-instance-connect
systemd-coredump
ubuntu
lxd
kernoops
lightdm
whoopsie
dnsmasq
avahi-autoipd
usbmux
rtkit
avahi
cups-pk-helper
geoclue
pulse
speech-dispatcher
saned
nm-openvpn
colord
hplip
gdm
fwupd-refresh
sssd
_flatpak
dhcpcd
cups-browsed
gnome-remote-desktop
polkitd
j.morgan
r.house

ssh_keys:
[no keys]

sessions:
```

<br>

<p>

- <code>cd /opt/robbco/engineering</code><br>
- <code>tar czf /tmp/src.tgz MFBootAgent/</code><br>
- <code>base64 /tmp/src.tgz > /dev/shm/.core_dump_2025.tgz.enc</code><br></p>

```bash
(dfir-env) ubuntu@tryhackme:/home/r.house$ ls -la
total 28
drwxr-xr-x 3 r.house r.house 4096 May 16 10:02 .
drwxr-xr-x 5 root    root    4096 May 16 10:02 ..
-rw-r--r-x 1 r.house r.house  116 May 16 10:02 .bash_history
-rw-r--r-x 1 r.house r.house  220 Feb 25  2020 .bash_logout
-rw-r--r-x 1 r.house r.house 3771 Feb 25  2020 .bashrc
-rw-r--r-x 1 r.house r.house  807 Feb 25  2020 .profile
drwx---r-x 2 r.house r.house 4096 May 16 10:02 .ssh
(dfir-env) ubuntu@tryhackme:/home/r.house$ strings .bash_history
cd /opt/robbco/engineering
tar czf /tmp/src.tgz MFBootAgent/
base64 /tmp/src.tgz > /dev/shm/.core_dump_2025.tgz.enc
```

<br>

<p>

- <code>/home/j.morgan/Documents/Invoices/invoice_Q1_2075.ods</code></p>

```bash
(dfir-env) ubuntu@tryhackme:/home/j.morgan/Documents/Invoices$ ls -la
total 12
drwxr-xr-x 2 j.morgan j.morgan 4096 Jun 12 18:10 .
drwxr-xr-x 3 j.morgan j.morgan 4096 May 16 10:02 ..
-rw-r--r-x 1 j.morgan j.morgan  532 Jun 12 18:10 invoice_Q1_2075.ods
(dfir-env) ubuntu@tryhackme:/home/j.morgan/Documents/Invoices$ pwd
/home/j.morgan/Documents/Invoices/invoice_Q1_2075.ods
```

<br>

<h2>Task 6 . Conclusion</h2>

<br>
<br>


<h1 align="center">Room Completed</h1>
<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/649fc42e-6c50-4e34-8614-e672ff6e11e3"><br>
<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/c8922d8e-4017-4d12-ab7a-12e88e291cce"><br>

<h1 align="center">Module Completed</h1>
<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/52991b53-b68b-439c-a9f2-e7f77a73b6ea"><br>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 9, 2025      | 429      |     162ⁿᵈ    |      5ᵗʰ     |    236ᵗʰ    |     8ᵗʰ    |  113,795 |    840    |     64   |

</div>

<p align="center"> Global All Time: 162ⁿᵈ <br><img width="300px" src="https://github.com/user-attachments/assets/1ee75b22-dfee-43b9-943a-2b9adca9caca" alt="Your Image Badge"><br>
                                              <img width="1000px" src="https://github.com/user-attachments/assets/529f9960-82ef-4962-9508-e76d8da56670"><br><br>
                   Brazil All Time:   5ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/a0819bba-9c92-4dc0-9871-0a0b194d5eef"><br><br>
                   Global monthly:  236ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/dfa85a7b-d5c3-4314-b114-3b7a41b8b08"><br><br>
                   Brazil monthly:    8ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/a0c333db-cdc9-483e-92a3-3cea126b8414"><br><br></p>
