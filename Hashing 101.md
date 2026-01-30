<h1 align="center"><a href="https://tryhackme.com/room/hashingcrypto101aa">Hashing 101</a></h1>
<p align="center">An introduction to Hashing, as part of a series on crypto<br><br><img width="1200px" src="https://github.com/user-attachments/assets/e4326f5b-686c-4383-b1a0-bea3798e8fae"><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20JAN%2029-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>

<br>

<h2>Task 1 .  Key Terms</h2>
<br>
<p><em>Answer the question below</em></p>

<p>1.1. Read the words, and understand the meanings!Is base64 encryption or encoding?<br>
<code>encoding</code></p>

<br>
<h2>Task 2 . What is a hash function?</h2>
<br>
<p><em>Answer the questions below</em></p>

<p>2.1. What is the output size in bytes of the MD5 hash function?<br>
<code>16</code></p>

<br>
<p>2.2. Can you avoid hash collisions? (Yea/Nay)<br>
<code>Nay</code></p>

<br>
<p>2.3. If you have an 8 bit hash output, how many possible hashes are there?<br>
<code>256</code></p>

<br>
<h2>Task 3 . Uses of hashing</h2>
<h3>What can we do with hashing?</h3>
<p>Hashing is used for 2 main purposes in Cyber Security. To verify integrity of data (More on that later), or for verifying passwords.</p>

<h3>Hashing for password verification</h3>

<h3>Protecting against rainbow tables</h3>
<p>To protect against rainbow tables, we add a salt to the passwords. The salt is randomly generated and stored in the database, unique to each user. In theory, you could use the same salt for all users but that means that duplicate passwords would still have the same hash, and a rainbow table could still be created specific passwords with that salt.<br>

The salt is added to either the start or the end of the password before it’s hashed, and this means that every user will have a different password hash even if they have the same password. Hash functions like bcrypt and sha512crypt handle this automatically. Salts don’t need to be kept private.</p>
<br>
<p><em>Answer the questions below</em></p>

<p>3.1. Crack the hash "d0199f51d2728db6011945145a1b607a" using the rainbow table manually.<br>
<code>basketball</code></p>

<br>
<p>3.2. Crack the hash "5b31f93c09ad1d065c0491b764d04933" using online tools<br>
<code>p4ssw0rd</code></p>

<p>https://md5decrypt.net/</p>

<img width="958" height="64" alt="image" src="https://github.com/user-attachments/assets/0c7dbfca-cc32-4587-b2fb-01b8b1f34ce9" />

<br>
<br>
<br>
<p>3.3. If you have an 8 bit hash output, how many possible hashes are there?<br>
<code>Nay</code></p>

<br>
<h2>Task 4 . Recognising password hashes</h2>
<br>


<p><em>Answer the questions below</em></p>

<p>4.1. How many rounds does sha512crypt ($6$) use by default? Hint: Do some research!<br>
<code>5000</code></p>
                   
<br>
<p>4.2. What's the hashcat example hash (from the website) for Citrix Netscaler hashes? Hint: Example page.<br>
<code>1765058016a22f1b4e076dccd1c3df4e8e5c0839ccded98ea</code></p>

<p>https://hashcat.net/wiki/doku.php?id=example_hashes</p>

<img width="1198" height="77" alt="image" src="https://github.com/user-attachments/assets/880b72f3-b9e5-493f-bbeb-8c93e30dfbff" />

<br>
<br>
<br>
<p>4.3. How long is a Windows NTLM hash, in characters?<br>
<code>32</code></p>

<img width="1058" height="135" alt="image" src="https://github.com/user-attachments/assets/f62377b4-852e-451e-ba8a-b85f42d59888" />

<br>
<br>
<br>
<h2>Task 5 . Password Cracking</h2>

<br>
<p><em>Answer the questions below</em></p>

<p>5.1. Crack this hash: $2a$06$7yoU3Ng8dHTXphAg913cyO6Bjs3K5lBnwq5FJyA6d01pMSrddr1ZG<br>
<code>85208520</code></p>

<img width="1082" height="49" alt="image" src="https://github.com/user-attachments/assets/2f4a2beb-4852-43b2-a8a4-a9840ced436f" />

<br>
<br>
<br>

:~/hashing101# hashcat -m 3200 '$2a$06$7yoU3Ng8dHTXphAg913cyO6Bjs3K5lBnwq5FJyA6d01pMSrddr1ZG' /usr/share/wordlists/rockyou.txt

<img width="1038" height="230" alt="image" src="https://github.com/user-attachments/assets/ca5bfc6d-44e0-425c-afa1-ae47a91bb93a" />

<br>
<br>
<br>
<p>5.2. Crack this hash: 9eb7ee7f551d2f0ac684981bd1f1e2fa4a37590199636753efe614d4db30e8e1   Hint: SHA2-256<br>
<code>halloween</code></p>


<img width="1195" height="28" alt="image" src="https://github.com/user-attachments/assets/c35a9af5-60f1-40df-a9ba-8dac3a9f8791" />


<br>
<br>
<br>

:~/hashing101# hashcat -m 1400 '9eb7ee7f551d2f0ac684981bd1f1e2fa4a37590199636753efe614d4db30e8e1' /usr/share/wordlists/rockyou.txt

<img width="1112" height="245" alt="image" src="https://github.com/user-attachments/assets/b5841a91-e8e6-4587-9d54-9a7f5e7d5245" />

<br>
<br>
<br>
<p>5.3. Crack this hash: $6$GQXVvW4EuM$ehD6jWiMsfNorxy5SINsgdlxmAEl3.yif0/c3NqzGLa0P.S7KRDYjycw5bnYkF5ZtB8wQy8KnskuWQS3Yr1wQ0<br>
<code>spaceman</code></p>

<img width="1078" height="39" alt="image" src="https://github.com/user-attachments/assets/36133ea3-4f2b-4496-9d13-531c056f4e49" />

<br>
<br>
<br>

:~/hashing101# hashcat -m 1800 '$6$GQXVvW4EuM$ehD6jWiMsfNorxy5SINsgdlxmAEl3.yif0/c3NqzGLa0P.S7KRDYjycw5bnYkF5ZtB8wQy8KnskuWQS3Yr1wQ0' /usr/share/wordlists/rockyou.txt


<img width="1116" height="226" alt="image" src="https://github.com/user-attachments/assets/db925610-360b-4e98-8614-f426e4aa038a" />

<br>
<br>
<br>
<p>5.4. Bored of this yet? Crack this hash: b6b0d451bbf6fed658659a9e7e5598fe Hint: Try online, rockyou isn't always enough.<br>
<code>	funforyou</code></p>
                  
<img width="1326" height="530" alt="image" src="https://github.com/user-attachments/assets/40965ea3-4f3e-4c7e-b71b-98f4df8856f2" />


<br>
<br>
<br>
<h1 align="center">Walkthrough Room Completed</h1>

<p align="center"><img width="900px" src="https://github.com/user-attachments/assets/ffbd2144-46b1-4197-977d-a47bec739f10"><br>
                  <img width="900px" src="https://github.com/user-attachments/assets/19bf04eb-9733-49bb-8d30-aeef6b3e49cc"><br>
                  <img width="900px" src="https://github.com/user-attachments/assets/452c61a1-4ed0-456b-97ed-fa44a900c35b"><br>
                  <img width="900px" src="https://github.com/user-attachments/assets/3ae3a9e2-1a5c-41ae-b848-26e6f1cde37e"></p>

                
<h1 align="center">My TryHackMe Journey ・ 2026, January</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|29     |Medium 🔗 - Hashing 101               |28|      59ᵗʰ  |     3ʳᵈ    |       59ᵗʰ   |        2ⁿᵈ     |    145,279  |    1,075    |    90     |
|29     |Hard ⚙️ - Initial Drift               |28|      59ᵗʰ  |     3ʳᵈ    |       59ᵗʰ   |        2ⁿᵈ     |    145,279  |    1,075    |    90     |
|29     |Easy 🔗 - Cloud Security Pitfalls     |28|      60ᵗʰ  |     3ʳᵈ    |       67ᵗʰ   |        2ⁿᵈ     |    144,704  |    1,075    |    90     |    
|29     |Medium 🚩 - First Shift CTF           |28|      61ˢᵗ  |     3ʳᵈ    |       66ᵗʰ   |        2ⁿᵈ     |    144,624  |    1,075    |    90     |
|27     |Medium 🔗 - GeoServer: CVE-2025-58360 |26 |     67ᵗʰ  |     3ʳᵈ    |       73ʳᵈ   |        2ⁿᵈ     |    144,174  |    1,074    |    90     |
|26     |Medium 🚩 - First Shift CTF, in progress|25|    66ᵗʰ  |     3ʳᵈ    |       73ʳᵈ   |        2ⁿᵈ     |    144,102  |    1,073    |    90     |
|25     |Medium 🔗 - MS Entra ID: Zero Trust   |24 |     70ᵗʰ  |     3ʳᵈ    |       79ᵗʰ   |        2ⁿᵈ     |    143,292  |    1,073    |    88     |
|24     |Medium 🚩 - First Shift CTF, in progress|23|    70ᵗʰ  |     3ʳᵈ    |       76ᵗʰ   |        2ⁿᵈ     |    143,104  |    1,072    |    88     |
|24     |Easy ⚔️ - Health Hazard               |23 |     78ᵗʰ  |     3ʳᵈ    |       94ᵗʰ   |        2ⁿᵈ     |    142,264  |    1,072    |    88     |
|23     |Medium ⚙️ - BlackCat                  |22 |     79ᵗʰ  |     3ʳᵈ    |      104ᵗʰ   |        2ⁿᵈ     |    142,189  |    1,072    |    88     |
|22     |Hard 🚩 - Azure: Tapper               |21 |     82ⁿᵈ  |     3ʳᵈ    |      176ᵗʰ   |        2ⁿᵈ     |    141,154  |    1,072    |    88     |
|22     |Easy ⚙️ - Hidden Hooks                |21 |     82ⁿᵈ  |     3ʳᵈ    |      189ᵗʰ   |        3ʳᵈ     |    141,059  |    1,071    |    88     |
|22     |Medium 🔗 - ret2libc                  |21 |     82ⁿᵈ  |     3ʳᵈ    |      193ʳᵈ   |        3ʳᵈ     |    140,979  |    1,071    |    88     |
|20     |Easy 🔗 - MS Entra ID: Hybrid Identities|19|    82ⁿᵈ  |     3ʳᵈ    |      184ᵗʰ   |        2ⁿᵈ     |    140,971  |    1,069    |    88     |
|19     |Easy ⚙️ - Upload and Conquer          |18 |     81ˢᵗ  |     3ʳᵈ    |      181ˢᵗ   |        2ⁿᵈ     |    140,859  |    1,068    |    88     |
|18     |Easy 🔗 - MS Entra ID: Identities     |17 |     83ʳᵈ  |     3ʳᵈ    |      341ˢᵗ   |        3ʳᵈ     |    139,864  |    1,068    |    88     |
|18     |Easy ⚙️ - APT28: Initial Access       |17 |     84ᵗʰ  |     3ʳᵈ    |      341ˢᵗ   |        3ʳᵈ     |    139,752  |    1,067    |    88     |
|18     |Easy ⚙️ - Hidden Hooks                |17 |           |     3ʳᵈ    |              |                |             |    1,067    |    88     |
|17     |Easy 🔗 - MS Entra ID: Introduction   |17 |     83ʳᵈ  |     3ʳᵈ    |      359ᵗʰ   |        3ʳᵈ     |    139,657  |    1,067    |    88     |
|17     |Easy ⚙️ - APT28: Credential Access    |17 |           |     3ʳᵈ    |              |                |             |    1,067    |    88     |
|17     |Medium ⚙️ - Open Door                 |17 |           |     3ʳᵈ    |              |                |             |     1,067   |    88     |
|17     |Easy 🔗 - Offensive Security Intro    |16 |     87ᵗʰ  |     3ʳᵈ    |      504ᵗʰ   |        5ᵗʰ     |    139,099  |    1,067    |    88     |
|16     |Hard 🚩 - Spring                      |15 |     87ᵗʰ  |     3ʳᵈ    |      540ᵗʰ   |        4ᵗʰ     |    138,942  |    1,066    |    87     |
|14     |Insane 🚩 - Scheme Catcher            |13 |     87ᵗʰ  |     3ʳᵈ    |      534ᵗʰ   |        5ᵗʰ     |    138,822  |    1,065    |    87     |
|13     |Hard 🚩 - Breachblocker Unlocker      |12 |     86ᵗʰ  |     3ʳᵈ    |      526ᵗʰ   |        5ᵗʰ     |    138,732  |    1,064    |    87     |
|11     |Medium 🚩 - Azure: Eyes Wide Shut     |10 |     86ᵗʰ  |     3ʳᵈ    |      558ᵗʰ   |        5ᵗʰ     |    138,450  |    1,063    |    86     |
|8      |Medium ⚙️ - Phishing Unfolding        | 7 |     86ᵗʰ  |     3ʳᵈ    |      508ᵗʰ   |        4ᵗʰ     |    138,372  |    1,062    |    84     |
|8      |Easy ⚙️ - Introduction to Phishing    | 7 |     96ᵗʰ  |     3ʳᵈ    |    2,479ᵗʰ   |       32ⁿᵈ     |    137,117  |    1,062    |    84     |
|8      |Medium 🔗 - KaffeeSec - SoMeSINT      | 7 |     98ᵗʰ  |     3ʳᵈ    |    2,847ᵗʰ   |       38ᵗʰ     |    137,052  |    1,062    |    84     |
|7      |Hard 🚩 - Hack Back                   | 6 |     98ᵗʰ  |     3ʳᵈ    |    2,798ᵗʰ   |       37ᵗʰ     |    136,908  |    1,061    |    84     |
|7      |Hard 🚩 - Dead End?                   | 6 |     99ᵗʰ  |     3ʳᵈ    |    2,924ᵗʰ   |       37ᵗʰ     |    136,788  |    1,060    |    84     |
|6      |Easy 🔗 - Linux Strength Training     | 5 |     98ᵗʰ  |     3ʳᵈ    |    3,172ⁿᵈ   |       47ᵗʰ     |    136,608  |    1,059    |    84     |
|4      |Medium 🚩 - JVM Reverse Engineering   | 3 |     96ᵗʰ  |     3ʳᵈ    |    3,031ˢᵗ   |       46ᵗʰ     |    136,450  |    1,058    |    84     |
|3      |Medium 🚩 - Carrotbane of My Existence| 2 |     96ᵗʰ  |     3ʳᵈ    |    3,468ᵗʰ   |       49ᵗʰ     |    136,150  |    1,057    |    84     |
|2      |Easy 🔗 - Learn Rust                  | 1 |     96ᵗʰ  |     3ʳᵈ    |    5,152ⁿᵈ   |       67ᵗʰ     |    136,030  |    1,056    |    84     |

</h6></div><br>

<p align="center">Global All Time:     59ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/1f7641b6-5ad9-487d-8058-0557bf52663e"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/80a32b64-23e8-440c-b0bb-b5a56f099e52"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/96ef053a-26ad-447d-9d85-d477fd4c042a"><br><br>
                  Global monthly:      67ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/7c3d5e68-3771-41e0-bbab-fdc79432008b"><br><br>
                  Brazil monthly:       2ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/283896ca-842e-47dd-8030-e136d9e15f35"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
