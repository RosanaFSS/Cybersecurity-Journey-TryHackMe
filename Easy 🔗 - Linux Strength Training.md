<h1 align="center">Linux Strength Training</h1>
<p align="center">2026, January 6 &nbsp; .  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>! Let´s learn together. Access this walkthrough room <a href="https://tryhackme.com/room/linuxstrengthtraining">here</a>.<br><br><img width="1200px" src="https://github.com/user-attachments/assets/2b245907-b535-4d7a-ae44-f3291310720a"></p>

<h2>Task 1 . Intro</h2>
<p>This room is intended to further the understanding of basic Linux command line skills for beginners.<br>

Therefore, before doing this room I would highly recommend that you finish the three Learn Linux rooms as it provides all the fundamental teachings that are vital to being able to successfully complete this room.<br>

Furthermore, this room can also serve as useful to intermediate users as it reinforces analytical skills when solving tasks.<br>


If you have read and understood this please begin by clicking the 'completed' button below and 'deploy' the room.</p>

<p><em>Answer the question below</em></p>

<p>1.1. <em>I understand</em><br>
<code>No answer needed</code></p>
<br>

<h2>Task 2 . Finding your way around linux - overview</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>2.1. <em>I have read and understood</em><br>
<code>No answer needed</code></p>
<br>

<p>2.2. <em>What is the correct option for finding files based on group</em><br>
<code>-group</code></p>
<br>

<p>2.3. <em>What is format for finding a file with the user named Francis and with a size of 52 kilobytes in the directory /home/francis/</em><br>
<code>find /home/francis -type f -user francis -size 52k</code></p>
<br>

<p>2.4. <em>SSH as <strong>topson</strong> using his password <strong>topson</strong>. Go to the /home/topson/chatlogs directory and type the following: grep -iRl 'keyword'. What is the name of the file that you found using this command?</em><br>
<code>2019-10-11</code></p>
<br>

<p>2.5. <em>Type: less [filename] to open the file. Then, before anything, type / before typing: keyword followed by [ENTER]. Notice how that allowed us to search for the first instance of that word in the entire document. For much larger documents this can be useful and if there are many more instances of that word in the document, we would be able to hit enter again to find the next instance in the document.</em><br>
<code>No answer needed</code></p>
<br>

<p>2.6. <em>What are the characters subsequent to the word you found?</em><br>
<code>ttitor</code></p>
<br>

<p>2.7. <em>What are the characters subsequent to the word you found?</em><br>
<code>Read the file named 'ReadMeIfStuck.txt'. What is the Flag?</code></p>
<br>


<h2>Task 3 . Working with files</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>3.1. <em>Hypothetically, you find yourself in a directory with many files and want to move all these files to the directory of /home/francis/logs. What is the correct command to do this?</em><br>
<code>mv * /home/francis/logs</code></p>
<br>

<p>3.2. <em>Hypothetically, you want to transfer a file from your /home/james/Desktop/ with the name script.py to the remote machine (192.168.10.5) directory of /home/john/scripts using the username of john. What would be the full command to do this?</em><br>
<code>scp /home/james/Desktop/script.py john@192.168.10.5:/home/john/scripts</code></p>
<br>

<p>3.3. <em>How would you rename a folder named -logs to -newlogs</em> Hint: Read the top section again</em><br>
<code>mv -- -logs -newlogs</code></p>
<br>

<p>3.4. <em>How would you copy the file named encryption keys to the directory of /home/john/logs</em><br>
<code>cp "encryption keys" /home/john/logs</code></p>
<br>

<p>3.5. <em>Find a file named readME_hint.txt inside topson's directory and read it. Using the instructions it gives you, get the second flag.</em><br>
<code>Flag{234@i4s87u5hbn$3}</code></p>
<br>

<h2>Task 4 . Hashing - Introduction</h2>
<h3>What is hashing?</h3>
<p>Next we will talk about hashing, which is important for any Linux security researcher. Hashing refers to taking any data input, such as a password and calculating its hash equivalent. The hash equivalent is a long string which cannot be reversed since the act of hashing is known as a one-way function. For example, if you visit: https://www.md5hashgenerator.com/ and type the following: mypassword123 or any other password, you will see how the hash algorithm known as MD5 will calculate and output a MD5 hash equivalent. Therefore, 'mypassword123' would have the MD5 hash equivalent of '9c87baa223f464954940f859bcf2e233'.</p>

<h6 align="center"><img width="400px" src="https://github.com/user-attachments/assets/b25df143-23a6-4cd2-8326-44e41c602c72"><br>This image and all the theoretical content of<br>the present article is TryHackMe´s property.</h6>

<h3>Why is hashing important?</h3>
<p>There are several reasons why hashing is important and I would encourage you to conduct some personal research after this, but the single most important use case you should concern yourself with in this room is integrity checking. For example, when you log into a website, your password must be checked with the local database to verify whether you should be allowed access. But think critically, if companies stored the username and password in plain text on the database, it would make it very easy for a successful hacker to be able to compromise every account. Therefore, it makes more sense to store the hash equivalent instead of storing the plain text credentials. So, when you send over your username and password to the database, the system will input these separately into a hash algorithm and if the output turns out to be equal to the hash equivalent stored in the database then it will allow you access. Sounds simple, right? If you are still confused, head over to this video and it should clarify any concerns:</p>

<p>Insert Video link</p>

<p>Note: MD5 and SHA1 are both examples of weak hash algorithms which have been proven to be vulnerable to something known as hash collision attacks which is explained further here: https://privacycanada.net/hash-functions/hash-collision-attack/. In short, do not use them because it has been proven that two different inputs can produce the same output (hash equivalent), thus, meaning that your password may produce the same hash as someone with a completely different password. Instead, SHA-256 is widely considered stronger as of today and is recommended.</p>

<h3>How to crack hashes?</h3>
<p>Hashes can be cracked through the method of brute-forcing. This essentially means using a wordlist and inputting each potential password from the wordlist into the hash function to see if we get a hash equivalent output that is equal to any of the hashes stored in the database. However, in the example we store the hash in a text file before specifying a wordlist to which we want to compare out calculated hashes with.</p>

<h6 align="center"><img width="400px" src="https://github.com/user-attachments/assets/eef1408a-af97-4592-98be-6bbd74219d24"><br>This image and all the theoretical content of<br>the present article is TryHackMe´s property.</h6>

<p>Using a program called John the Ripper we can specify the format of the hash we wish to crack (md5) the wordlist (rockyou.txt) and the wordlist (hash.txt). Please see the full man page for garnering a more complete understanding of all of the commands you can run with this program.</p>

<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/ec2af1d8-e5c5-4c99-8222-a8da9a269034"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>


<p>Eventually John the Ripper may find the password if it was contained the wordlist. In the real world, you may have to find a larger wordlist with a strong amount of common password/username combinations. In this example below the password was found to be 'password'.</p>

<h6 align="center"><img width="400px" src="https://github.com/user-attachments/assets/675903c2-09ad-4848-8d97-0693e259587d"><br>This image and all the theoretical content of<br>the present article is TryHackMe´s property.</h6>

<p>Note: If you ever encounter a hash that you do not know the type of you can use a tool called hash-identifier. However, with less widely used hashes the tool will not be accurate and therefore will still rely on you to develop the skill of manually identifying what type of hash it is, however this is out of the scope of this room. The syntax for identifying unknown hashes is as so:<br>

Hash-identifier [hash] as seen below in a real example:</p>

<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/a3fada0c-84a0-4428-885c-45c967055220"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Alternatively you could pipe the output of the file storing the hash to hash-identifier as shown below, which may be quicker.</p>

<h6 align="center"><img width="400px" src="https://github.com/user-attachments/assets/0ee06d52-2ae9-45eb-83c5-a36de01e1465"><br>This image and all the theoretical content of<br>the present article is TryHackMe´s property.</h6>

<p>The result should show us the most likely hash types that the hash most likely is. As you can see there are two most probable hashes. In this case the correct hash was in fact SHA-256, therefore you can see how in most cases the first result is the correct answer, but please be aware that this not always the case since many hash types can appear similar in terms of string formatting.</p>

<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/1dac309e-9225-4432-bb58-e8ad50598f7d"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6

<p><strong>Note</strong>: a more modern and powerful alternative to hash-identifer is a tool called haiti if you're interested: https://github.com/noraj/haiti</p>

<p><em>Answer the questions below</em></p>

<p>4.1. <em>Download the hash file attached to this task and attempt to crack the MD5 hash. What is the password?</em><br>
<code>secret123</code></p>

```bash
:~# hashid -e hash.txt
```

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/b854cc93-2f93-44ab-a786-420faaebf0e7"><br>Rosana´s hands-on</h6>
<br>

```bash
:~# john --format=raw--md5 --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/986012b0-0bf4-46d9-aee9-77a597ba3117"><br>Rosana´s hands-on</h6>
<br>

<p><a href="https://crackstation.net/">CrackStation</a></p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/7ffd68f6-de64-40be-bb79-52199f8f7f60"><br>Rosana´s hands-on</h6>

<br>
<p>4.2. <em>SSH as <strong>sarah</strong> using: sarah@[MACHINE_IP] and use the password: ----------------. What is the hash type stored in the file hashA.txt</em><br>
<code>MD4</code></p>

```bash
:~# ssh sarah@MACHINE_IP
...
sarah@james:~$
```

```bash
sarah@james:~$ find / -name hashA.txt 2>/dev/null
/home/sarah/system AB/server_mail/server settings/hashA.txt
```

```bash
sarah@james:~$ cat hashA.txt
f9d4049dd6...
```

<br>
<p>4.3. <em>Crack <code>hashA.txt</code> using john the ripper, what is the password?</em><br>
<code>admin</code></p>

<p><a href="https://crackstation.net/">CrackStation</a></p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/a13ac7ac-2d2c-4dc8-97e2-38a6b6bec67f"><br>Rosana´s hands-on</h6>

<br>
<p>4.4. <em>What is the hash type stored in the file <code>hashB.txt</code></em><br>
<code>SHA-1</code></p>

```bash
sarah@james:~$ 
...
```

```bash
sarah@james:~$
...
```

<br>
<p>4.5. <em>Find a wordlist  with the file extention of '.mnf' and use it to crack the hash with the filename <code>hashC.txt</code>. What is the password?</em> Hint: If you cannot find the mnf file try researching how to use the find command to find files based on file extentions. Don't forget to work out the type of hash used before attempting to crack the hash. The remote machine does not have john the ripper installed so make sure you perform the cracking on your own machine.<<br>
<code>unacvaolipatnuggi</code></p>

```bash
sarah@james:~$ find / -name hashC.txt 2>/dev/null
/home/sarah/system AB/server_mail/hashC.txt
```

```bash
sarah@james:~/system AB/server_mail$ cat hashC.txt
c05e35377b5a31f428ccda9724a9dfbd0c5d71dccac691228d803c78e2e8da29
```

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/7697277a-a497-4fff-a046-ae6676e703f0"><br><br>
                   <img width="900px" src="https://github.com/user-attachments/assets/fa923f99-3e5e-4c35-b463-f47930c12a47"><br><br>
                   <img width="900px" src="https://github.com/user-attachments/assets/4a638655-2e55-43e7-addb-854c38696b94"><br>Rosana´s hands-on</h6>


<p><a href="https://github.com/blackploit/hash-identifier">hash-identifier</a> documentation</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/a5d4bc01-f743-4243-a4ec-74c7f132f215"><br>Rosana´s hands-on</h6>
<br>


```bash
:~# john --format=raw-sha256 --wordlist=ww.mnf este.txt
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-SHA256 [SHA256 256/256 AVX2 8x])
No password hashes left to crack (see FAQ)
```

```bash
:~# john --show --format=raw-sha256 este.txt
?:unacvaolipatnuggi
```

<br>
<p>4.6. <em>Crack hashB.txt using john the ripper, what is the password?</em><<br>
<code>letmein</code></p>

```bash
sarah@james:~$ find / -name hashB.txt 2>/dev/null
/home/sarah/oldLogs/settings/craft/hashB.txt
```

```bash
sarah@james:~$ cat /home/sarah/oldLogs/settings/craft/hashB.txt
b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
```

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/26366642-6709-4d28-9c1c-9de405917716"><br>Rosana´s hands-on</h6>
<br>
<h2>Task 5 . Decoding base64</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>5.1. <em>what is the name of the tool which allows us to decode base64 strings?</em><br>
<code>base64</code></p>

<br>
<p>5.2. <em>find a file called encoded.txt. What is the special answer?</em><br>
<code>john</code></p>

<br>
<h2>Task 6 . Encryption/Decryption using gpg</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>6.1. <em>Now try it for yourself. Make a random text file and enter some readable sentences in there before encrypting and decrypting it as illustrated above.</em><br>
<code>No answer needed</code></p>

<br>
<p>6.2. <em>You wish to encrypt a file called history_logs.txt using the AES-128 scheme. What is the full command to do this?</em><br>
<code>gpg --cipher-algo AES-128 --symmetric history_logs.txt</code></p>

<br>
<p>6.3. <em>What is the command to decrypt the file you just encrypted?</em><br>
<code>gpg history_logs.txt.gpg</code></p>

<br>
<p>6.4. <em>Find an encrypted file called layer4.txt, its password is bob. Use this to locate the flag. What is the flag?</em><br>
<code>Flag{B07$f854f5ghg4s37}</code></p>

```bash
:~# echo 'oi' > secret.txt
:~# gpg --cipher-algo AES-256 --symmetric secret.txt
:~# ls
secret.txt secret.txt.gpg
```

<img width="996" height="129" alt="image" src="https://github.com/user-attachments/assets/0a6e776c-dc62-4596-b408-0f812611bd2d" />

```bash
:~# gpg secret.txt.gpg
gpg: WARNING: no command supplied.  Trying to guess what you mean ...
gpg: AES256 encrypted data
gpg: encrypted with 1 passphrase
File 'secret.txt' exists. Overwrite? (y/N) N
Enter new filename: secret_decrypted.txt
```

```bash
:~# cat secret_decrypted.txt
oi
```

```bash
sarah@james:~$ find / -type f -name layer4.txt 2>/dev/null
/home/sarah/system AB/keys/vnmA/layer4.txt
```

```bash
sarah@james:~/system AB/keys/vnmA$ gpg layer4.txt
gpg: WARNING: no command supplied.  Trying to guess what you mean ...
gpg: AES256 encrypted data
gpg: encrypted with 1 passphrase
gpg: layer4.txt: unknown suffix
Enter new filename [layer4.txt]: layer4_decrypted.txt
sarah@james:~/system AB/keys/vnmA$ ls
layer4_decrypted.txt  layer4.txt
sarah@james:~/system AB/keys/vnmA$ cat layer4_decrypted.txt
1. Find a file called layer3.txt, its password is james.
```

```bash
sarah@james:~/system AB$ find / -type f -name layer3.txt 2>/dev/null
/home/sarah/oldLogs/2014-02-15/layer3.txt
```

```bash
sarah@james:~/oldLogs/2014-02-15$ gpg layer3.txt
gpg: WARNING: no command supplied.  Trying to guess what you mean ...
gpg: AES256 encrypted data
gpg: encrypted with 1 passphrase
gpg: layer3.txt: unknown suffix
Enter new filename [layer3.txt]: layer3d.txt
sarah@james:~/oldLogs/2014-02-15$ ls
layer3d.txt  layer3.txt
```

```bash
sarah@james:~/oldLogs/2014-02-15$ cat layer3d.txt
1. Find a file called layer2.txt, its password is tony.

2. sarah@james:~$ find / -type f -name layer2.txt 2>/dev/null
/home/sarah/oldLogs/settings/layer2.txt
```

```bash
sarah@james:~/oldLogs/settings$ ls
cACOjol  cbYcJfh  cHETaUf  craft  dYFvVaE  EVLzbKB  FIVOxAr  hGbPbqz  KCEGxit  layer2.txt  mZsFcHB
sarah@james:~/oldLogs/settings$ gpg layer2.txt
gpg: WARNING: no command supplied.  Trying to guess what you mean ...
gpg: AES256 encrypted data
gpg: encrypted with 1 passphrase
gpg: layer2.txt: unknown suffix
Enter new filename [layer2.txt]: layer2d.txt
sarah@james:~/oldLogs/settings$ 
```

```bash
sarah@james:~/oldLogs/settings$ cat layer2d.txt
MS4gRmluZCBhIGZpbGUgY2FsbGVkIGxheWVyMS50eHQsIGl0cyBwYXNzd29yZCBpcyBoYWNrZWQu
```

```bash
sarah@james:~/oldLogs/settings$ echo 'MS4gRmluZCBhIGZpbGUgY2FsbGVkIGxheWVyMS50eHQsIGl0cyBwYXNzd29yZCBpcyBoYWNrZWQu' | base64 -d
1. Find a file called layer1.txt, its password is hacked.
```

```bash
sarah@james:~/oldLogs/settings$ find / -type f -name layer1.txt 2>/dev/null
/home/sarah/logs/zmn/layer1.txt
```

```bash
sarah@james:~/logs/zmn$ ls
 layer1.txt  'old stuff'
```

 ```bash
sarah@james:~/logs/zmn$ gpg layer1.txt
gpg: WARNING: no command supplied.  Trying to guess what you mean ...
gpg: AES256 encrypted data
gpg: encrypted with 1 passphrase
gpg: layer1.txt: unknown suffix
Enter new filename [layer1.txt]: layer1d.txt
```

```bash
sarah@james:~/logs/zmn$ ls
 layer1d.txt   layer1.txt  'old stuff'
```


```bash 
sarah@james:~/logs/zmn$ cat layer1d.txt
Flag{B07$f854f5ghg4s37}
```

<br>
<h2>Task 7 . Cracking encrypted gpg files</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>7.1. <em>Now try it yourself! Encrypt a file and use a common password contained in the wordlist you wish to use. Follow the instructions above to decrypt as if you are a hacker. If it worked, well done.</em><br>
<code>No answer needed</code></p>

<br>
<p>7.2. <em>Find an encrypted file called personal.txt.gpg and find a wordlist called data.txt. Use tac to reverse the wordlist before brute-forcing it against the encrypted file. What is the password to the encrypted file?</em> Hint: use gpg to decrypt it using the wordlist called data.txt. The find command will help you find these files. If you still get stuck read the information from this task again and perform the first task again. Remember, tac can be used to reverse the wordlist for bruteforcing.<br>
<code>valamanezivonia</code></p>

<br>
<p>7.3. <em>What is written in this now decrypted file?</em> Hint: Scroll down. you may need to maximize the terminal to properly see the enlarged words.<br>
<code>getting stronger in linux</code></p>


<img width="1179" height="282" alt="image" src="https://github.com/user-attachments/assets/8847f973-89c9-4ded-a64c-e1e1cd7e65f2" />

```bash
sarah@james:~$ find / -type f -name personal.txt.gpg 2>/dev/null
/home/sarah/oldLogs/units/personal.txt.gpg
```

```bash
sarah@james:~$ find / -type f -name data.txt 2>/dev/null
/home/sarah/logs/zmn/old stuff/-mvLp/data.txt
```

```bash
:~# scp 'sarah@10.66.143.143:/home/sarah/oldLogs/units/personal.txt.gpg' .
sarah@10.66.143.143's password: 
personal.txt.gpg                                                                                 100%  579   483.9KB/s   00:00
```

```bash
:~# scp 'sarah@10.66.143.143:/home/sarah/logs/zmn/old\ stuff/-mvLp/data.txt' .
sarah@10.66.143.143's password: 
data.txt                                                                                         100% 1053KB  73.6MB/s   00:00
```



```bash
:~# tac data.txt > data_reverse.txt
```

```bash
:~# john --format=gpg --wordlist=data_reverse.txt rose
```


<img width="1266" height="327" alt="image" src="https://github.com/user-attachments/assets/528b6392-0b28-4b0f-ac58-13b0a04dadff" />

```bash
:~# gpg personal.txt.gpg
gpg: WARNING: no command supplied.  Trying to guess what you mean ...
gpg: AES256 encrypted data
gpg: encrypted with 1 passphrase
```

<img width="1109" height="762" alt="image" src="https://github.com/user-attachments/assets/c98c4a3e-7691-4990-90f6-cbe99c8bf74e" />


<h2>Task 8 . Reading SQL Databases</h2>
<br>

<p><em>Answer the question below</em></p>

<p>8.1. <em>Find a file called employees.sql and read the SQL database. (Sarah and Sameer can log both into mysql using the password: password). Find the flag contained in one of the tables. What is the flag?</em> Hint: Look for someone with the first name of: Lobel.<br>
<code>Flag{13490AB8} </code></p>

<img width="1205" height="287" alt="image" src="https://github.com/user-attachments/assets/7a38684e-cc47-4f0a-a51d-a576877ded5e" />

```bash
sarah@james:~$ find / -type f -name *.sql 2>/dev/null
/home/sarah/serverLx/employees.sql
/home/sarah/serverLx/employees_partitioned.sql
/home/sarah/serverLx/employees_partitioned_5.1.sql
/home/sarah/serverLx/show_elapsed.sql
/home/sarah/serverLx/objects.sql
/home/sarah/serverLx/test_employees_md5.sql
/home/sarah/serverLx/test_employees_sha.sql
/home/sarah/serverLx/sakila/sakila-mv-data.sql
/home/sarah/serverLx/sakila/sakila-mv-schema.sql
/usr/share/mysql/mysql_system_tables_data.sql
/usr/share/mysql/debian_create_root_user.sql
/usr/share/mysql/innodb_memcached_config.sql
/usr/share/mysql/install_rewriter.sql
/usr/share/mysql/mysql_security_commands.sql
/usr/share/mysql/mysql_system_tables.sql
/usr/share/mysql/uninstall_rewriter.sql
/usr/share/mysql/mysql_test_data_timezone.sql
/usr/share/mysql/mysql_sys_schema.sql
/usr/share/mysql/fill_help_tables.sql
```


<img width="1199" height="333" alt="image" src="https://github.com/user-attachments/assets/c4c0e069-d7fe-43e9-a650-3dd80b94353d" />

```bash
mysql> source employees.sql
```

<img width="1215" height="293" alt="image" src="https://github.com/user-attachments/assets/2c326bf9-acb8-4c27-ae23-00c74ac83e23" />

<img width="1226" height="309" alt="image" src="https://github.com/user-attachments/assets/aea523a9-d3f4-4000-b098-d5df69ea78ce" />


<img width="1198" height="688" alt="image" src="https://github.com/user-attachments/assets/859aae63-fe1e-49df-850a-8c7c37edf499" />

<h2>Task 9 . Challenge</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>9.1. <em>Go to the /home/shared/chatlogs directory and read the first chat log named: LpnQ. Use this to help you to proceed to the next task.</em> Hint: You may need to use grep to find keywords based on what you would expect the next chat log to include? Perhaps names?<br>
<code>No answer needed</code></p>

<br>
<p>9.2. <em>What is Sameer's SSH password?</em> Hint: You may need to use grep to find keywords based on what you would expect the next chat log to include? Perhaps names?<br>
<code>thegreatestpasswordever000</code></p>

<br>
<p>9.3. <em>What is the password for the sql database back-up copy</em> Hint: Since the password begins with 'ebq', using grep to find all wordlists with this keyword may help. Once that's done, combining all wordlists with this keyword may help. Then you could find a way to cut out any words from the new created wordlist that do not begin with ebq. Also: can 'cat [wordlist.txt] >' be used to combine multiple wordlists into one?<br>
<code>_____________________</code></p>

<br>
<p>9.4. <em>Find the SSH password of the user James. What is the password?</em><br>
<code>_____________________</code></p>

<br>
<p>9.5. <em>SSH as james and change the user to root?</em> Hint: How do we change user again?<br>
<code>_____________________</code></p>

<br>
<p>9.6. <em>What is the root flag?</em> Hint: Look everywhere<br>
<code>_____________________</code></p>




<img width="1206" height="336" alt="image" src="https://github.com/user-attachments/assets/028dd2a9-0e5f-41f1-8289-91a616c89354" />

<img width="1212" height="639" alt="image" src="https://github.com/user-attachments/assets/d7c57398-b436-4f47-aaa9-1318b43b0a46" />


<img width="1211" height="143" alt="image" src="https://github.com/user-attachments/assets/12fa47c6-d92e-4072-8dd1-455d08099a5a" />

<img width="1210" height="150" alt="image" src="https://github.com/user-attachments/assets/1d591568-b143-4e93-aade-ab580f23ffd4" />

```bash
sarah@james:/home/shared$ find / -type f -size 50M 2>/dev/null
/home/shared/sql/conf/JKpN
```

<img width="1120" height="500" alt="image" src="https://github.com/user-attachments/assets/49fec986-1af7-4f99-8dfd-4af96de8b352" />



<img width="1124" height="138" alt="image" src="https://github.com/user-attachments/assets/bf86155b-9efd-4c00-88a5-ddf99605de24" />


<img width="1120" height="500" alt="image" src="https://github.com/user-attachments/assets/dbc3764e-bf42-47f5-8ed9-edf92ba47e6a" />

<img width="1119" height="84" alt="image" src="https://github.com/user-attachments/assets/a119f11a-4103-4345-aa9f-1f654d52799e" />

```bash
sameer@james:~/History LB/labmind/latestBuild/configBDB$ grep -iR ebq
pLmjwi:ebqiojsdfioj
pLmjwi:ebqiojsiodj
pLmjwi:ebqiojdifoj
pLmjwi:ebqiopsjdfopj
pLmjwi:ebqnice
pLmjwi:ebqops
LmqAQl:ebqiuiud
LmqAQl:ebqjoisjdfij
Ulpsmt:ebqkjjdd
Ulpsmt:ebqijsji
Ulpsmt:ebqopkopk
Ulpsmt:ebqattle
```

```bash
sameer@james:~/History LB/labmind/latestBuild/configBDB$ grep -ihR ebq wordlist.txt
ebqiojsdfioj
ebqiojsiodj
ebqiojdifoj
ebqiopsjdfopj
ebqnice
ebqops
ebqiuiud
ebqjoisjdfij
ebqkjjdd
ebqijsji
ebqopkopk
ebqattle
```

<img width="1205" height="286" alt="image" src="https://github.com/user-attachments/assets/a005bf96-752b-4895-8645-77446d167ba3" />


```bash
:~# scp 'sarah@10.66.143.143:/home/shared/sql/2020-08-13.zip.gpg' .
sarah@10.66.143.143's password: 
2020-08-13.zip.gpg                                                                                                          100%  102MB 112.7MB/s   00:00 
```




