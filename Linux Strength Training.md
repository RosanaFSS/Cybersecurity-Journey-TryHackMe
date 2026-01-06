
<h2>Task 4 . Hashing - Introduction</h2>

<img width="912" height="214" alt="image" src="https://github.com/user-attachments/assets/986012b0-0bf4-46d9-aee9-77a597ba3117" />


<img width="1341" height="531" alt="image" src="https://github.com/user-attachments/assets/7ffd68f6-de64-40be-bb79-52199f8f7f60" />


<img width="1108" height="433" alt="image" src="https://github.com/user-attachments/assets/b854cc93-2f93-44ab-a786-420faaebf0e7" />

```bash
sarah@james:~$ find / -name hashA.txt 2>/dev/null
/home/sarah/system AB/server_mail/server settings/hashA.txt
```

<img width="1350" height="533" alt="image" src="https://github.com/user-attachments/assets/a13ac7ac-2d2c-4dc8-97e2-38a6b6bec67f" />


<p>4.5. <em>Find a wordlist  with the file extention of '.mnf' and use it to crack the hash with the filename hashC.txt. What is the password?</em><<br>
<code>unacvaolipatnuggi</code></p>

```bash
sarah@james:~$ find / -name hashC.txt 2>/dev/null
/home/sarah/system AB/server_mail/hashC.txt
```

```bash
sarah@james:~/system AB/server_mail$ cat hashC.txt
c05e35377b5a31f428ccda9724a9dfbd0c5d71dccac691228d803c78e2e8da29
```

<img width="991" height="413" alt="image" src="https://github.com/user-attachments/assets/7697277a-a497-4fff-a046-ae6676e703f0" />

<img width="1121" height="119" alt="image" src="https://github.com/user-attachments/assets/fa923f99-3e5e-4c35-b463-f47930c12a47" />

<br>

<img width="987" height="108" alt="image" src="https://github.com/user-attachments/assets/4a638655-2e55-43e7-addb-854c38696b94" />

<br>
<br>
<br>
<p>https://github.com/blackploit/hash-identifier</p>

<img width="992" height="607" alt="image" src="https://github.com/user-attachments/assets/a5d4bc01-f743-4243-a4ec-74c7f132f215" />

<br>
<br>
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
<br>
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

<img width="1336" height="528" alt="image" src="https://github.com/user-attachments/assets/26366642-6709-4d28-9c1c-9de405917716" />

<br>
<h2>Task 5 . Decoding base64</h2>


<br>
<h2>Task 6 . Encryption/Decryption using gpg</h2>



:~# echo 'oi' > secret.txt
:~# gpg --cipher-algo AES-256 --symmetric secret.txt
:~# ls
secret.txt secret.txt.gpg


<img width="996" height="129" alt="image" src="https://github.com/user-attachments/assets/0a6e776c-dc62-4596-b408-0f812611bd2d" />


:~# gpg secret.txt.gpg
gpg: WARNING: no command supplied.  Trying to guess what you mean ...
gpg: AES256 encrypted data
gpg: encrypted with 1 passphrase
File 'secret.txt' exists. Overwrite? (y/N) N
Enter new filename: secret_decrypted.txt


:~# cat secret_decrypted.txt
oi



sarah@james:~$ find / -type f -name layer4.txt 2>/dev/null
/home/sarah/system AB/keys/vnmA/layer4.txt


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


sarah@james:~/system AB$ find / -type f -name layer3.txt 2>/dev/null
/home/sarah/oldLogs/2014-02-15/layer3.txt

sarah@james:~/oldLogs/2014-02-15$ gpg layer3.txt
gpg: WARNING: no command supplied.  Trying to guess what you mean ...
gpg: AES256 encrypted data
gpg: encrypted with 1 passphrase
gpg: layer3.txt: unknown suffix
Enter new filename [layer3.txt]: layer3d.txt
sarah@james:~/oldLogs/2014-02-15$ ls
layer3d.txt  layer3.txt

sarah@james:~/oldLogs/2014-02-15$ cat layer3d.txt
1. Find a file called layer2.txt, its password is tony.

2. sarah@james:~$ find / -type f -name layer2.txt 2>/dev/null
/home/sarah/oldLogs/settings/layer2.txt


sarah@james:~/oldLogs/settings$ ls
cACOjol  cbYcJfh  cHETaUf  craft  dYFvVaE  EVLzbKB  FIVOxAr  hGbPbqz  KCEGxit  layer2.txt  mZsFcHB
sarah@james:~/oldLogs/settings$ gpg layer2.txt
gpg: WARNING: no command supplied.  Trying to guess what you mean ...
gpg: AES256 encrypted data
gpg: encrypted with 1 passphrase
gpg: layer2.txt: unknown suffix
Enter new filename [layer2.txt]: layer2d.txt
sarah@james:~/oldLogs/settings$ 


sarah@james:~/oldLogs/settings$ cat layer2d.txt
MS4gRmluZCBhIGZpbGUgY2FsbGVkIGxheWVyMS50eHQsIGl0cyBwYXNzd29yZCBpcyBoYWNrZWQu



sarah@james:~/oldLogs/settings$ echo 'MS4gRmluZCBhIGZpbGUgY2FsbGVkIGxheWVyMS50eHQsIGl0cyBwYXNzd29yZCBpcyBoYWNrZWQu' | base64 -d
1. Find a file called layer1.txt, its password is hacked.


sarah@james:~/oldLogs/settings$ find / -type f -name layer1.txt 2>/dev/null
/home/sarah/logs/zmn/layer1.txt


sarah@james:~/logs/zmn$ ls
 layer1.txt  'old stuff'

 
sarah@james:~/logs/zmn$ gpg layer1.txt
gpg: WARNING: no command supplied.  Trying to guess what you mean ...
gpg: AES256 encrypted data
gpg: encrypted with 1 passphrase
gpg: layer1.txt: unknown suffix
Enter new filename [layer1.txt]: layer1d.txt


sarah@james:~/logs/zmn$ ls
 layer1d.txt   layer1.txt  'old stuff'

 
sarah@james:~/logs/zmn$ cat layer1d.txt
Flag{B07$f854f5ghg4s37}


<h2>Task 7 . Cracking encrypted gpg files</h2>


<img width="1179" height="282" alt="image" src="https://github.com/user-attachments/assets/8847f973-89c9-4ded-a64c-e1e1cd7e65f2" />

sarah@james:~$ find / -type f -name personal.txt.gpg 2>/dev/null
/home/sarah/oldLogs/units/personal.txt.gpg

sarah@james:~$ find / -type f -name data.txt 2>/dev/null
/home/sarah/logs/zmn/old stuff/-mvLp/data.txt


:~# scp 'sarah@10.66.143.143:/home/sarah/oldLogs/units/personal.txt.gpg' .
sarah@10.66.143.143's password: 
personal.txt.gpg                                                                                 100%  579   483.9KB/s   00:00


:~# scp 'sarah@10.66.143.143:/home/sarah/logs/zmn/old\ stuff/-mvLp/data.txt' .
sarah@10.66.143.143's password: 
data.txt                                                                                         100% 1053KB  73.6MB/s   00:00





:~# tac data.txt > data_reverse.txt


:~# john --format=gpg --wordlist=data_reverse.txt rose



<img width="1266" height="327" alt="image" src="https://github.com/user-attachments/assets/528b6392-0b28-4b0f-ac58-13b0a04dadff" />

:~# gpg personal.txt.gpg
gpg: WARNING: no command supplied.  Trying to guess what you mean ...
gpg: AES256 encrypted data
gpg: encrypted with 1 passphrase


<img width="1109" height="762" alt="image" src="https://github.com/user-attachments/assets/c98c4a3e-7691-4990-90f6-cbe99c8bf74e" />


<h2>Task 8 . Reading SQL Databases</h2>


<img width="1205" height="287" alt="image" src="https://github.com/user-attachments/assets/7a38684e-cc47-4f0a-a51d-a576877ded5e" />


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



<img width="1199" height="333" alt="image" src="https://github.com/user-attachments/assets/c4c0e069-d7fe-43e9-a650-3dd80b94353d" />

mysql> source employees.sql

<img width="1215" height="293" alt="image" src="https://github.com/user-attachments/assets/2c326bf9-acb8-4c27-ae23-00c74ac83e23" />

<img width="1226" height="309" alt="image" src="https://github.com/user-attachments/assets/aea523a9-d3f4-4000-b098-d5df69ea78ce" />


<img width="1198" height="688" alt="image" src="https://github.com/user-attachments/assets/859aae63-fe1e-49df-850a-8c7c37edf499" />

<h2>Task 9 . Challenge</h2>


<img width="1206" height="336" alt="image" src="https://github.com/user-attachments/assets/028dd2a9-0e5f-41f1-8289-91a616c89354" />

<img width="1212" height="639" alt="image" src="https://github.com/user-attachments/assets/d7c57398-b436-4f47-aaa9-1318b43b0a46" />







