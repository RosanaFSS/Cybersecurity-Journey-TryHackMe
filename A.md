

<p>nmap</p>

![image](https://github.com/user-attachments/assets/e96407fa-6f81-4e43-9aec-93da93c8c174)

<br>

<p>ftp<br>
ls<br>
mget *.txt</p>

![image](https://github.com/user-attachments/assets/3a5d72c0-da0e-43d9-adeb-a192516a2f79)

<br>

<h3>FLAG 4  :  FLAG{9b91f372b5600f14b3a0e2b520a0a8b8}</h3>

<p>cat</p>

![image](https://github.com/user-attachments/assets/59b1225b-3c23-4840-a6b4-13fc7aab60e4)

<br>

<p>cat  --> detail of <code>additional_notes.txt</code></p>

![image](https://github.com/user-attachments/assets/79a88c89-91d8-4e2b-8dcb-eb582c813b4f)


<br>
<p>/etc/hosts --> Target_IP + domain name = TheHiddenGateway.thm </p>

![image](https://github.com/user-attachments/assets/4025f4a1-0337-4be5-9859-ef68f2d50639)

<br>

<p>gobuster</p>

![image](https://github.com/user-attachments/assets/74441b60-16bf-4637-85d5-8b302d181f40)


<br>

<p>Navigated to <code>http://thehiddengateway.thm/robots.txt</code>.</p>

<br>
<h3>FLAG 7  :  FLAG{9c1061fd4b34bba667fa11877474f19e}</h3>

![image](https://github.com/user-attachments/assets/531560d4-3de9-46cc-8c15-75a168011b23)

<br>


<p>Navigated to <code>http://thehiddengateway.thm/index.html</code>.</p>


![image](https://github.com/user-attachments/assets/7276d3a8-5586-4e87-917d-6b15c4e24618)

<br>

![image](https://github.com/user-attachments/assets/abe1e86a-6f32-4cf5-b32f-bd1f60f95966)

<br>
<h3>FLAG 2  :  FLAG{19a3b5e6d14acb9ed0e66d3c22ad86b3}</h3>

![image](https://github.com/user-attachments/assets/2254eeb9-fdd4-40f0-9078-fb4525c35671)

<br>

<p>Navigated to <code>http://thehiddengateway.thm/Database</code>.</p>

![image](https://github.com/user-attachments/assets/a605dae6-9c78-447d-b416-e4ee3b01e57c)

<p>Navigated to <code>http://thehiddengateway.thm/Database/DB.py</code>.<br>
Discovered <code>abood</code> : <code>b9ed0e66d3c22asdda</code></p>


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

<p>Discovered <code>admin</code>, and <code>superadmin</code> passwords.</p>


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

<h3>FLAG 10  :  FLAG{b21c93b1e8c074d31f1ab9d65d7f95ad}</h3>

![image](https://github.com/user-attachments/assets/741d2a42-1f0d-44c6-a2ac-62f63bd17041)

<br>

<p>Used <code>cat</code> to view <code>HeySalameh.txt</code>´s content.</p>

![image](https://github.com/user-attachments/assets/406b1a2a-af9a-4744-a419-7c561ebd987e)


```bash

:~/TheHiddenGateway# hashcat -m 0 -a 3 9015d7a0004e724719122195f019debd /usr/share/wordlists/rockyou.txt
hashcat (v6.1.1-66-g6a419d06) starting...
...
```






<p>Selected the <code>users_db</code> database.</p>

```bash
mysql> use users_db;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql>

```

<p>Checked the available <code>tables</code>, selected <code>users</code> table, filtered <code>users</code> information.</p>

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
<h3>FLAG 13  : FLAG{ec16fcb9d51c178f8cbf91fc1edaa445}</h3>

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
<h3>FLAG 1  :  FLAG{b3f6f539c4312a11c9e4e9c88c1d3d7e}</h3>


![image](https://github.com/user-attachments/assets/09c17091-4629-4a03-ac27-3eb8188beff1)


<br>

![image](https://github.com/user-attachments/assets/d934c431-96ef-43c0-88a7-25956836f95f)

<br>

<h3>FLAG 5  :  FLAG{56a8b3be0e927a99d85fc6ec4a12fb35}</h3>

![image](https://github.com/user-attachments/assets/e16b2c5f-cd92-441b-8130-8154ae6f81fa)

<br>

<h3>FLAG 8  :  FLAG{501fe2f1a7c9f69b68f0f0cb4a3c9d3e}}</h3>

![image](https://github.com/user-attachments/assets/cf5be001-4009-4e91-a7c2-0b608bcb837c)






