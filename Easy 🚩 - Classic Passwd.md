<h1 align="center">Classic Passwd</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/8b7b3986-9a26-40dc-95de-8adb373b7f0c"><br>
2025, September 6<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>488</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Practice your skills in reversing and get the flag bypassing the login</em>.<br>
Access it <a href="https://tryhackme.com/room/classicpasswd"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/8b7b3986-9a26-40dc-95de-8adb373b7f0c"></p>

<h2>Task 1 . Get Connected</h2>
<p>I forgot my password, can you give me access to the program?</p>

<p><em>Answer the question belos</em></p>

```bash
$ mv 'Challenge_1609966715991 (1).Challenge'  challenge
cyberlaser@DESKTOP-0AHBUE8:/mnt/c/Users/Rosana/TryHackMe$ chmod +x challenge
cyberlaser@DESKTOP-0AHBUE8:/mnt/c/Users/Rosana/TryHackMe$ ./challenge
Insert your username: e

Authentication Error
```

```bash
$ ltrace ./challenge
printf("Insert your username: ")                                          = 22
__isoc99_scanf(0x57df6b64101b, 0x7ffdc8d93110, 0, 0Insert your username: t
)                      = 1
strcpy(0x7ffdc8d93080, "t")                                               = 0x7ffdc8d93080
strcmp("t", "xxxxxxxxxxxxx")                                              = 51
puts("\nAuthentication Error"
Authentication Error
)                                            = 22
exit(0 <no return ...>
+++ exited (status 0) +++
```


```bash
$ ./challenge
Insert your username: xxxxxxxxxxxxx

Welcome
THM{***********}
```

<br>
<p>1.1. What is the flag?<br>
<code>THM{***********}</code></p>

<br>
<br>

<img width="1898" height="890" alt="image" src="https://github.com/user-attachments/assets/439b3da2-90b6-4879-9682-0b2283d5f38f" />
