May 9, 2025<br>
Day 368<br>

<h1>NerdHerd</h1>

<br>
<br>

<h2 align="center">$$\textcolor{white}{\textnormal{Nmap}}$$</h2>

<p align="center">There are have 4 ports open: <code>21/ftp</code>, <code>22/ssh</code>, <code>139/smbd</code> and <code>445/smdb</code>. </p>

```bash
~# nmap -sC -sV -sS -A -O TargetIP
...
PORT    STATE SERVICE     VERSION
21/tcp  open  ftp         vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxr-xr-x    3 ftp      ftp          4096 Sep 11  2020 pub
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:AttackIP
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp  open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
...

Host script results:
|_clock-skew: mean: -1h00m00s, deviation: 1h43m55s, median: 0s
|_nbstat: NetBIOS name: NERDHERD, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: nerdherd
|   NetBIOS computer name: NERDHERD\x00
|   Domain name: \x00
|   FQDN: nerdherd
|_  System time: 2025-05-10T02:54:26+03:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2025-05-09T23:54:26
|_  start_date: N/A

```

<h2 align="center">$$\textcolor{white}{\textnormal{ftp}}$$</h2>

```bash
ftp TargetIP
...
Name (TargetIP:root): Anonymous
230 Login successful.
...
ftp> dir
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    3 ftp      ftp          4096 Sep 11  2020 pub
226 Directory send OK.
ftp> ls -la
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    3 ftp      ftp          4096 Sep 11  2020 .
drwxr-xr-x    3 ftp      ftp          4096 Sep 11  2020 ..
drwxr-xr-x    3 ftp      ftp          4096 Sep 11  2020 pub
226 Directory send OK.
ftp> cd pub
250 Directory successfully changed.
ftp> ls -la
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    3 ftp      ftp          4096 Sep 11  2020 .
drwxr-xr-x    3 ftp      ftp          4096 Sep 11  2020 ..
drwxr-xr-x    2 ftp      ftp          4096 Sep 14  2020 .jokesonyou
-rw-rw-r--    1 ftp      ftp         89894 Sep 11  2020 youfoundme.png
226 Directory send OK.
ftp> get youfoundme.png
local: youfoundme.png remote: youfoundme.png
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for youfoundme.png (89894 bytes).
226 Transfer complete.
89894 bytes received in 0.00 secs (49.5547 MB/s)
ftp> cd .jokesonyou
250 Directory successfully changed.
ftp> ls -lah
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp          4096 Sep 14  2020 .
drwxr-xr-x    3 ftp      ftp          4096 Sep 11  2020 ..
-rw-r--r--    1 ftp      ftp            28 Sep 14  2020 hellon3rd.txt
226 Directory send OK.
ftp> get hellon3rd.txt
local: hellon3rd.txt remote: hellon3rd.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for hellon3rd.txt (28 bytes).
226 Transfer complete.
28 bytes received in 0.00 secs (60.8992 kB/s)
ftp> exit
221 Goodbye.
:~# 
```

<br>

<h2 align="center">$$\textcolor{white}{\textnormal{youfoundme.png}}$$</h2>

<p>Discovered <code>Owner Name</code> : <code>fijbxslz</code>.<br><br>
Googled <code>fijbxslz</code> and discovered it is about <code>Vigenére cipher</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/96a8df77-97c4-47bf-bbbb-3efcdb949bdb)

<br>


```bash
exiftool youfoundme.png
ExifTool Version Number         : 11.88
File Name                       : youfoundme.png
Directory                       : .
File Size                       : 88 kB
File Modification Date/Time     : 2025:05:10 00:59:40+01:00
File Access Date/Time           : 2025:05:10 00:59:40+01:00
File Inode Change Date/Time     : 2025:05:10 00:59:40+01:00
File Permissions                : rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 894
Image Height                    : 894
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Background Color                : 255 255 255
Pixels Per Unit X               : 3543
Pixels Per Unit Y               : 3543
Pixel Units                     : meters
Warning                         : [minor] Text chunk(s) found after PNG IDAT (may be ignored by some readers)
Datecreate                      : 2010-10-26T08:00:31-07:00
Datemodify                      : 2010-10-26T08:00:31-07:00
Software                        : www.inkscape.org
EXIF Orientation                : 1
Exif Byte Order                 : Big-endian (Motorola, MM)
Resolution Unit                 : inches
Y Cb Cr Positioning             : Centered
Exif Version                    : 0231
Components Configuration        : Y, Cb, Cr, -
Flashpix Version                : 0100
Owner Name                      : fijbxslz
Image Size                      : 894x894
Megapixels                      : 0.799
```


<h2 align="center">$$\textcolor{white}{\textnormal{hellon3rd.txt}}$$</h2>

```bash
~# cat hellon3rd.txt
all you need is in the leet
```

<h2 align="center">$$\textcolor{white}{\textnormal{1337}}$$</h2>


![image](https://github.com/user-attachments/assets/7cb0cb54-c55a-4942-8ace-351e3e900b01)

<br>


<h2 align="center">$$\textcolor{white}{\textnormal{http://TargetIP:1337}}$$</h2>

```bash
~# curl http://TargetIP:1337
<!DOCTYPE html>
<html>
<body>
...

<!--
	hmm, wonder what i hide here?
 -->
...
<!--
	maybe nothing? :)
 -->
...
<!--
	keep digging, mister/ma'am
 -->
...
<body onload="alertFunc()">

<script>
function alertFunc() {
  alert("HACKED by 0xpr0N3rd");
  alert("Just kidding silly.. I left something in here for you to find")
}
</script>

<p>Maybe the answer is in <a href="https://www.youtube.com/watch?v=9Gc4QTqslN4">here</a>.</p>

</body>
</html>
```


<h2 align="center">$$\textcolor{white}{\textnormal{Youtube}}$$</h2>

![image](https://github.com/user-attachments/assets/1fe91c07-98a9-4bbd-b65b-1428d04467f3)


<br>

<p>Did not find anything valuable from this <code>bird</code> hint.</p>

<br>






