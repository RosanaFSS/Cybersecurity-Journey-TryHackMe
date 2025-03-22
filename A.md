
<p align="center">March 22, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{320}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
  <img width="160px" src="https://github.com/user-attachments/assets/d6a17ea6-e8be-4bf5-ab73-75f2d3f3a21a"></p>


<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{The Hidden Gateway}}$$
</h1>
<p align="center">Is a web and boot-to-root CTF challenge. Navigate through web vulnerabilities, exploit misconfigurations, and escalate privileges to ultimately gain root access. Only the most skilled hackers will unlock the hidden gateway and conquer the system. It is classified as a medium-level CTF, and you can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed. <a href="https://tryhackme.com/room/thehiddengateway3">The Hidden Gateway</a>.</p>
                                                              
<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/d6a17ea6-e8be-4bf5-ab73-75f2d3f3a21a"> </p>

<br>
<br>

<h2 align="center">$$\textcolor{white}{\textnormal{Enumeration}}$$</h2>


<p align="center">$$\textcolor{white}{\textnormal{Used <code>nmap</code>.<br>Noticed the <code>cache</code>}}$$</p>

<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/e96407fa-6f81-4e43-9aec-93da93c8c174"> </p>


<br>

<p>Used <code>ftp</code>, <code>ls</code>, and <code>mget *.txt</code>code>.<br>

![image](https://github.com/user-attachments/assets/3a5d72c0-da0e-43d9-adeb-a192516a2f79)

<br>

<p>FLAG 4  :  FLAG{9b91f372b5600f14b3a0e2b520a0a8b8}</p>

<p>Used <code>cat</code>.</p>

![image](https://github.com/user-attachments/assets/59b1225b-3c23-4840-a6b4-13fc7aab60e4)

<br>

<p>cat  --> detail of <code>additional_notes.txt</code></p>

![image](https://github.com/user-attachments/assets/79a88c89-91d8-4e2b-8dcb-eb582c813b4f)


<br>
<p>/etc/hosts --> Target_IP + domain name = TheHiddenGateway.thm </p>

![image](https://github.com/user-attachments/assets/4025f4a1-0337-4be5-9859-ef68f2d50639)

<br>

<p>Used <code>gobuster</code>.</p>

![image](https://github.com/user-attachments/assets/74441b60-16bf-4637-85d5-8b302d181f40)


<br>

<p>Navigated to <code>http://thehiddengateway.thm/robots.txt</code>.</p>

<br>
<p>FLAG 7  :  FLAG{9c1061fd4b34bba667fa11877474f19e}</p>

![image](https://github.com/user-attachments/assets/531560d4-3de9-46cc-8c15-75a168011b23)

<br>


<p>Navigated to <code>http://thehiddengateway.thm/index.html</code>.</p>


![image](https://github.com/user-attachments/assets/7276d3a8-5586-4e87-917d-6b15c4e24618)

<br>

![image](https://github.com/user-attachments/assets/abe1e86a-6f32-4cf5-b32f-bd1f60f95966)

<br>
<p>FLAG 2  :  FLAG{19a3b5e6d14acb9ed0e66d3c22ad86b3}</p>

![image](https://github.com/user-attachments/assets/2254eeb9-fdd4-40f0-9078-fb4525c35671)

<br>

<p>Navigated to <code>http://thehiddengateway.thm/Database</code>.</p>

![image](https://github.com/user-attachments/assets/a605dae6-9c78-447d-b416-e4ee3b01e57c)

<p>Navigated to <code>http://thehiddengateway.thm/Database/DB.py</code>.<br>
Discovered <code>abood</code> : <code>b9ed0e66d3c22a</code></p>

<p>Used <code>ssh</code> and <code>abood</code>.</p>

<br>
<p>FLAG 12  :  FLAG{d1d1f383ae6c8e7d983586572145da21}</p>

![image](https://github.com/user-attachments/assets/586dece1-b0f0-4398-8521-3c126db1044b)


<br>

<p>Transfered <code>Hi-abood.zip</code> using <code>scp</code>.</p>

![image](https://github.com/user-attachments/assets/71aa7d7c-6eb6-4468-a885-96c07bccd3a2)

<br>

<p>Used <code>zip2john</code> to get the hash of the file.<br>
Used <code>john</code> to discover the password of the zip file.</p>

![image](https://github.com/user-attachments/assets/48dbc7ff-0d30-4d9e-8eae-63f60318fcb9)

<br>

<p>Used <code>unzip</code>.</p>

![image](https://github.com/user-attachments/assets/005730ea-0510-4653-8435-7e56652eb3b4)

<p>Used <code>cat</code>.</p>

![image](https://github.com/user-attachments/assets/ea8db7c1-08e9-44f4-a90d-3432c664269b)

<p>...</p>

![image](https://github.com/user-attachments/assets/89ee0188-ddeb-4d80-b492-4f1c206ffe0c)

```bash
Hey abood,

I just wanted to let you know that the encryption method you used is really powerful! I'm impressed by how strong it is.

However, I wanted to point out that to prove its strength, here\u2019s my account password: C27B6748A18F65B3FEA73A226C730767C4789C37EE1966F6F6666031EB3A4300341DF88C4A28398A8E49D90BFAFD509F (in AES encryption) and the key used: 03228cfe5e8f261fe90b2aa2daawwaaf.

I hope this helps you evaluate the method even better.

Cheers,
ehxb

...

3954C412C5F0F9C77AE385F84A04DCB8ED3198C2843CA66CBAF3F2FB04C3482D75D40079C6536B38C5CA368BE854A3B20E8F9BD45743F4DA51190D50692CF173

```
<br>

https://www.devglan.com/online-tools/aes-encryption-decryption

<br>
<p>FLAG 11: FLAG{b8f60273a80bbd8b7c2a2433456fb5ff}</p>

![image](https://github.com/user-attachments/assets/89801b4b-1019-4d5a-8391-094fb1125f9a)

<p>password: 4312a11c9e4e9cb9ed0e66d3c22asdda</p>

![image](https://github.com/user-attachments/assets/4ec29604-80ee-4bb2-a9e5-8d2eead13b4d)


<br>
<p>FLAG 15: FLAG{3f64e31c87d7f6f3fa5d24b7e35ac4da}</p>

<p>Used <code>su</code>.</p>

![image](https://github.com/user-attachments/assets/ebee9df3-0363-4b72-817c-30fcdc1b10dd)


<br>

<p>Used <code>sudo -l</code>.</p>

![image](https://github.com/user-attachments/assets/be58dc31-1778-466e-bb9e-a1422e76364d)


<br>
<p>FLAG 14: FLAG{74b87a9ec54d5a22c029763730d32ac3}</p>

<p>Used <code>ls</code>.<br>
Used <code>nano</code>.</p>

![image](https://github.com/user-attachments/assets/1b2e303a-d945-49c7-aede-c7ef51a44bdc)

<p>Used <code>sudo /home/ehxb/system_dashboard.sh</code>.</p>

![image](https://github.com/user-attachments/assets/ffc2e5d2-1705-4175-b201-790100f6b7c7)

<br>

![image](https://github.com/user-attachments/assets/7743808f-2773-4d4c-ab12-fd9a24c678ad)

<br>
<p>FLAG 6: FLAG{91f66a5ea7b8a54e0e720a04ad6dbb8e}</p>



![image](https://github.com/user-attachments/assets/28753db4-2f8a-44bf-8027-533d8594c4c0)



<br>
<p>FLAG 3: FLAG{d8f2a19e9469b7c85c4d12389f65beeb}}</p>


![image](https://github.com/user-attachments/assets/4ff6df59-56fb-4ae2-b2d1-76b00ac3a008)


<br>
<br>
<br>



![image](https://github.com/user-attachments/assets/6a0a7585-a215-44a2-96d0-f91e3a92ca78)

<p>Explored the Database using <code>mysql</code> command.</p>

```bash
# mysql -u abood -p -h Target-IP
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 10
Server version: 8.0.40-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2025, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 

```

<p>Discovered the Databases available.</p>

```bash
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| admin_db           |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| users_db           |
+--------------------+
6 rows in set (0.00 sec)

mysql> 

```

<p>Selected the <code>admin_db</code> database, checked the <code>tables</code> availabled, output <code>admins</code> information.</p>

```bash
mysql> use admin_db;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+--------------------+
| Tables_in_admin_db |
+--------------------+
| admins             |
+--------------------+
1 row in set (0.00 sec)

mysql> select * from admin;
ERROR 1146 (42S02): Table 'admin_db.admin' doesn't exist
mysql> select * from admins;
+----+---------+------------------------------+----------------------------------+------------+---------------------+
| id | name    | email                        | password                         | role       | created_at          |
+----+---------+------------------------------+----------------------------------+------------+---------------------+
|  1 | ehxb    | ehxb@thehiddengateway.thm    | 9015d7a0004e724719122195f019debd | superadmin | 2024-11-27 02:33:55 |
|  2 | salameh | salameh@thehiddengateway.thm | 5f4dcc3b5aa765d61d8327deb882cf99 | admin      | 2024-11-27 02:33:55 |
+----+---------+------------------------------+----------------------------------+------------+---------------------+
2 rows in set (0.01 sec)

mysql> 

```


```bash
...




```

<p>Navigated to <code>Hashes.com</code></p>

<br>

![image](https://github.com/user-attachments/assets/5bef8900-afb2-451e-89f6-c76069256e65)

<br>


![image](https://github.com/user-attachments/assets/fa228cdc-2d6b-4a18-b399-4cc5a1caa303)


<br>



![image](https://github.com/user-attachments/assets/f0bd0a04-9907-4872-b4e6-2616965256a1)

<br>

<p>Used <code>hashcat</code></p>

```bash

:~/TheHiddenGateway# hashcat -m 0 -a 3 5f4dcc3b5aa765d61d8327deb882cf99 /usr/share/wordlists/rockyou.txt
hashcat (v6.1.1-66-g6a419d06) starting...
...
```

![image](https://github.com/user-attachments/assets/d9f89da2-3915-4c6f-bd7a-7881891216fe)

<p>Discovered <code>admin</code> password.</p>


```bash

:~/TheHiddenGateway# hashcat -m 0 -a 3 5f4dcc3b5aa765d61d8327deb882cf99 /usr/share/wordlists/rockyou.txt
hashcat (v6.1.1-66-g6a419d06) starting...
...
5f4dcc3b5aa765d61d8327deb882cf99:password        
                                                 
Session..........: hashcat
Status...........: Cracked
Hash.Name........: MD5
Hash.Target......: 5f4dcc3b5aa765d61d8327deb882cf99
Time.Started.....: Sat Mar 22 ... 2025 (0 secs)
Time.Estimated...: Sat Mar 22 ... 2025 (0 secs)
Guess.Mask.......: password [8]
Guess.Queue......: 4/14336792 (0.00%)
Speed.#1.........:     1064 H/s (0.01ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests
Progress.........: 1/1 (100.00%)
Rejected.........: 0/1 (0.00%)
Restore.Point....: 0/1 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: password -> password


```

![image](https://github.com/user-attachments/assets/7b1e15bf-e8ee-4e72-b123-7a5c1e424e44)

<p>Used <code>ssh</code>, and discovered flag 10.</p>

<br>

<p>FLAG 10  :  FLAG{b21c93b1e8c074d31f1ab9d65d7f95ad}</p>

![image](https://github.com/user-attachments/assets/741d2a42-1f0d-44c6-a2ac-62f63bd17041)

<br>

<p>Used <code>cat</code> to view <code>HeySalameh.txt</code>´s content.</p>

<p>Note: <code>HeySalameh.txt</code> may not run sudo.</p>

![image](https://github.com/user-attachments/assets/406b1a2a-af9a-4744-a419-7c561ebd987e)

<br>

![image](https://github.com/user-attachments/assets/aeed8b7b-7246-41db-ae37-8ad7a0729bbb)


<br>

![image](https://github.com/user-attachments/assets/bef7ba3d-99ca-4836-9c90-c9571afc7f29)

<p><code>hashcat</code> did not crack the <code>superadmin</code> hash.</p>





<p>Selected the <code>users_db</code> database.</p>

```bash
mysql> use users_db;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql>

```

<p>Checked the available <code>tables</code>, selected <code>users</code> table, filtered <code>users</code> information.</p>

<p>FLAG 9  :  FLAG{eaeb216e0d60a3d9a64fb1c925f83a85}</p>

```bash
mysql> show tables;
+--------------------+
| Tables_in_users_db |
+--------------------+
| users              |
+--------------------+
1 row in set (0.00 sec)

mysql> select * from users;
+----+-----------------+--------------------------------------------------+----------------------------------+---------------------+
| id | name            | email                                            | password                         | created_at          |
+----+-----------------+--------------------------------------------------+----------------------------------+---------------------+
|  1 | John Doe        | john.doe@thehiddengateway.thm                    | b6a5b813b7ca05eb016b970429728ae4 | 2024-11-27 02:33:55 |
|  2 | Jane Smith      | jane.smith@thehiddengateway.thm                  | 3e9ea03d7e5a0621f39e787356014e4e | 2024-11-27 02:33:55 |
|  3 | Michael Brown   | FLAG{eaeb216e0d60a3d9a64fb1c925f83a85} => flag 9 | 57e79c5e82fcd548104a50e6823a1e54 | 2024-11-27 02:33:55 |
|  4 | Emily Davis     | emily.davis@thehiddengateway.thm                 | 3ec3a146cfe486290f97f288c8ffe00a | 2024-11-27 02:33:55 |
|  5 | David Wilson    | david.wilson@thehiddengateway.thm                | ce9b2339c03d8a984ae6492e1b0c3db0 | 2024-11-27 02:33:55 |
|  6 | Sophia Miller   | sophia.miller@thehiddengateway.thm               | c5ec7e8c9ceaf106b0ae926db05c08e0 | 2024-11-27 02:33:55 |
|  7 | Liam Anderson   | liam.anderson@thehiddengateway.thm               | d699dd200552bacdcd7cfd08c96c21b4 | 2024-11-27 02:33:55 |
|  8 | Olivia Johnson  | olivia.johnson@thehiddengateway.thm              | 7a179078a0a5a232c64e68ee6894c7e0 | 2024-11-27 02:33:55 |
|  9 | Daniel Martinez | daniel.martinez@thehiddengateway.thm             | d8819a22459909c36a1bf4249da37454 | 2024-11-27 02:33:55 |
| 10 | Isabella Garcia | isabella.garcia@thehiddengateway.thm             | b6195665420e1e03cd5f49e424771d92 | 2024-11-27 02:33:55 |
| 11 | Ethan Thomas    | ethan.thomas@thehiddengateway.thm                | b9a86c7329aa46c799987dbacb6fc209 | 2024-11-27 02:33:55 |
| 12 | Mason Jackson   | mason.jackson@thehiddengateway.thm               | 3de9165348c8ebd2fb860e35d24ad8b9 | 2024-11-27 02:33:55 |
| 13 | Ava White       | ava.white@thehiddengateway.thm                   | 53fc7d86d98d7d3b30cc38da6f584d12 | 2024-11-27 02:33:55 |
| 14 | Lucas Harris    | lucas.harris@thehiddengateway.thm                | 75053c11d24e844728e98ab27062cd1e | 2024-11-27 02:33:55 |
| 15 | Amelia Lee      | amelia.lee@thehiddengateway.thm                  | cd471ece63ae39103e847822a81af9f4 | 2024-11-27 02:33:55 |
+----+-----------------+--------------------------------------------------+----------------------------------+---------------------+
15 rows in set (0.00 sec)

mysql> 

```

<p></p>


<br>
<p>FLAG 13  : FLAG{ec16fcb9d51c178f8cbf91fc1edaa445}</p>

![image](https://github.com/user-attachments/assets/ee2bc28d-e644-48ce-a4ef-4006efe16bd4)

<br>



<p>Navigated to <code>http://thehiddengateway.thm/images/</code>.</p>

![image](https://github.com/user-attachments/assets/fcc3a88f-c131-45e4-90d5-74d820c517d5)


<p>Navigated to <code>http://thehiddengateway.thm/welcome.html</code>.</p>

![image](https://github.com/user-attachments/assets/076c5a5e-204e-473e-a4dc-f68cd7566ce9)

<p>Navigated to <code>http://thehiddengateway.thm/welcome.html</code>.<br>
Discovered <code>Ehxb@thehiddengateway.thm</code></p>

![image](https://github.com/user-attachments/assets/63fa4d05-4e35-4712-8d0b-97d29b5c9d3a)


<br>
<p>FLAG 1  :  FLAG{b3f6f539c4312a11c9e4e9c88c1d3d7e}</p>


![image](https://github.com/user-attachments/assets/09c17091-4629-4a03-ac27-3eb8188beff1)


<br>

![image](https://github.com/user-attachments/assets/d934c431-96ef-43c0-88a7-25956836f95f)

<br>

<p>FLAG 5  :  FLAG{56a8b3be0e927a99d85fc6ec4a12fb35}</p>

![image](https://github.com/user-attachments/assets/e16b2c5f-cd92-441b-8130-8154ae6f81fa)

<br>

<h3>FLAG 8  :  FLAG{501fe2f1a7c9f69b68f0f0cb4a3c9d3e}}</h3>

![image](https://github.com/user-attachments/assets/cf5be001-4009-4e91-a7c2-0b608bcb837c)


<br>
<br>
<br>

<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$
</h1>

![image](https://github.com/user-attachments/assets/7990cf70-676c-43ef-b234-54991484da83)

<br>

![image](https://github.com/user-attachments/assets/d2869321-7046-49bd-a183-a5b0fef85cfa)



<br>

<br>

<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$
</h1>


<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          | WorldWide    | Brazil       | WorldWide   | Brazil     |          | Completed |           |
| March 22, 2025    | 320      |     350ᵗʰ    |        8ᵗʰ   |    794ᵗʰ    |      9ᵗʰ   |  87,428  |       622 |   59      |

</div>

<p align="center"> Global All Time: 352ⁿᵈ<br><br><img width="900px" src="https://github.com/user-attachments/assets/f014dd91-4bf4-4b94-8d86-1c0e4e8cccfa"> </p>

<p align="center"> Brazil All Time: 8ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/b054fd8c-1aa2-431b-bbed-21dad5364a6"> </p>

<p align="center"> Global monthly: 926ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/daafd34b-3a15-4281-abd8-54f88aaf8929"> </p>

<p align="center"> Brazil monthly: 13ʳᵈ<br><br><img width="900px" src="https://github.com/user-attachments/assets/90d8d44d-9f24-49bb-a1e6-2119b7b1f0e4"> </p>
