<h1 align="center">Sea Surfer</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/65646d1b-002b-4dbb-bd9f-4b240f90f042"><br>
2025, September 18<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>483</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Ride the Wave!</em>.<br>
Access it <a href="https://tryhackme.com/room/seasurfer"</a>here.<br>
<img width="1200px" src=" "></p>


<br>
<h2>Task 1 . Let´s go!</h2>
<p>It's a beautiful day to hit the beach and do some surfing.<br>

<em>Please allow up to 5 minutes for the machine to boot up.</em></p>

<p><em>Answer the questions below</em></p>


<br>
<h2>nikto</h2>
<p>

- Server leaks inodes via ETags, header found with file /, fields: 0x2aa6 0x5dcde2b3f2ff9 <br>
- Uncommon header 'x-backend-server' found, with contents: seasurfer.thm</p>

```bash
:~/SeaSurfer# nikto -h xx.xxx.xxx.xxx
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xxx.xxx
+ Target Hostname:    ip-xx-xxx-xxx-xxx.ec2.internal
+ Target Port:        80
+ Start Time:         2025-09-01 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ Server leaks inodes via ETags, header found with file /, fields: 0x2aa6 0x5dcde2b3f2ff9 
+ The anti-clickjacking X-Frame-Options header is not present.
+ Uncommon header 'x-backend-server' found, with contents: seasurfer.thm
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: GET, POST, OPTIONS, HEAD 
+ 6544 items checked: 0 error(s) and 4 item(s) reported on remote host
+ End Time:           2025-09-01 xx:xx:xx (GMT1) (13 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```






