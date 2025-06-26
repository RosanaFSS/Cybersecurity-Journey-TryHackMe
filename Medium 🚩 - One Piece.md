<p>June 26, 2025</p>
<h1>One Piece</h1>
<p>A CTF room based on the wonderful manga One Piece. Can you become the Pirate King?</p>

<br>

<h2>Task 1 . Set Sail</h2>
<p>Welcome to the One Piece room.<br>

Your dream is to find the One Piece and hence to become the Pirate King.<br>

Once the VM is deployed, you will be able to enter a World full of Pirates.<br>

Please notice that pirates do not play fair. They can create rabbit holes to trap you.<br>

This room may be a bit different to what you are used to:<br>

- Required skills to perform the intended exploits are pretty basic.<br>
- However, solving the (let's say) "enigmas" to know what you need to do may be trickier.<br>

This room is some sort of game, some sort of puzzle.<br>

Please note that if you are currently reading/watching One Piece and if you did not finish Zou arc, you will get spoiled during this room.</p>

<p>1.1. Deploy the machine and hoist the sails<br>
<code>No answer needed</code></p>

<br>

<h2>Task 2 . Road Poneglyphs</h2>
<p>In order to reach Laugh Tale, the island where the One Piece is located, you must collect the 4 Road Poneglyphs.</p>

<p>2.1. What is the name of the tree that contains the 1st Road Poneglyph?<br>
<code>the whale_</code></p>


<h3>Nmap</h3>
<p><code>21/ftp/vsftpf,Anonynous<code>, <code>22/ssh</code> and <code>80/Apache</code></p>

```bash
:~# nmap -sC -sV -sS -v -T4 TargetIP
...
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 0        0             187 Jul 26  2020 welcome.txt
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.51.154
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-favicon: Unknown favicon MD5: C31581B251EA41386CB903FC27B37692
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: New World
...
```

<h3>FTP</h3>

```bash
:~# ftp TargetIP
...
Name (TargetIPy the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -la
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    3 0        0            4096 Jul 26  2020 .
drwxr-xr-x    3 0        0            4096 Jul 26  2020 ..
drwxr-xr-x    2 0        0            4096 Jul 26  2020 .the_whale_tree
-rw-r--r--    1 0        0             187 Jul 26  2020 welcome.txt
226 Directory send OK.
ftp> get welcome.txt
local: welcome.txt remote: welcome.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for welcome.txt (187 bytes).
226 Transfer complete.
187 bytes received in 0.00 secs (324.9416 kB/s)
ftp> cd .the_whale_tree
250 Directory successfully changed.
ftp> ls -la
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Jul 26  2020 .
drwxr-xr-x    3 0        0            4096 Jul 26  2020 ..
-rw-r--r--    1 0        0            8652 Jul 26  2020 .road_poneglyph.jpeg
-rw-r--r--    1 0        0            1147 Jul 26  2020 .secret_room.txt
226 Directory send OK.
ftp> get .road_poneglyph.jpeg
local: .road_poneglyph.jpeg remote: .road_poneglyph.jpeg
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for .road_poneglyph.jpeg (8652 bytes).
226 Transfer complete.
8652 bytes received in 0.00 secs (9.8112 MB/s)
ftp> get .secret_room.txt
local: .secret_room.txt remote: .secret_room.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for .secret_room.txt (1147 bytes).
226 Transfer complete.
1147 bytes received in 0.00 secs (1.7558 MB/s)
ftp> exit
221 Goodbye.
```

<h3>welcome.txt</h3>
<p>
  
- Island = <code>Zou</code><br>
- elephant named <code>Zunesah</code><br>
- <code>New World</p>

```bash
:~# cat welcome.txt
Welcome to Zou. It is an island located on the back of a massive, millennium-old elephant named Zunesha that roams the New World.
Except this, there is not much to say about this island.

```
