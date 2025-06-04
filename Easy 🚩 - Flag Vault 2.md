<h1 align="center">Flag Vault 2</h1>
<p align="center"><img width="90px" src="https://github.com/user-attachments/assets/2e72733c-cd92-4538-b4c0-84c751d46db1"><br>Jun 4, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure,<br> part of my 394-day-streak in  <a href="https://tryhackme.com">TryHackMe</a><br>
Exploit a simple format string vulnerability. <a href="https://tryhackme.com/room/hfb1flagvault2"</a>here.<br><br>
<img width="1000px" src=""></p>

<br>
<h2>Task 1 . Binay Exploitation - Flag Vault 2</h2>
<p> [ ... ] </p>

<h3 align="left">Answer the question below</h3>

> 1.1. <em>What is the flag?</em><br><a id='1.1'></a>
>> <strong><code>THM{format_issues}</code></strong><br>
<p></p>

<h3>pwnc1.c</h3>
<p>- Navigate to the link provided to visualized the code <code>pwn1.c</code>.</p>


![image](https://github.com/user-attachments/assets/e94ef8e0-9858-4abb-ac1f-8f004e2e7c87)

<p>The <code>flag.txt</code> is not enabled to be printed.<br>
It is about <code>Format Memory Vulnerability</code>.<br>
Learned more about it in <code>OWASP</code> web site --> https://owasp.org/www-community/attacks/Format_string_attack.</p>>

![image](https://github.com/user-attachments/assets/fea741b1-f0a7-4616-8975-ef9a3676e042)

<br>

![image](https://github.com/user-attachments/assets/f6f29adc-9d82-41f1-a0b0-fa58799515c6)

<br>

![image](https://github.com/user-attachments/assets/d8e2f4c9-608d-4e33-8703-78988131c2a3)

<br>

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
		"Version 2.1 - Fixed print_flag to not print the flag. Nothing you can do about it!\n"
		"==================================================================\n\n"
	      );
}

void print_flag(char *username){
        FILE *f = fopen("flag.txt","r");
        char flag[200];

        fgets(flag, 199, f);
        //printf("%s", flag);
	
	//The user needs to be mocked for thinking they could retrieve the flag
	printf("Hello, ");
	printf(username);
	printf(". Was version 2.0 too simple for you? Well I don't see no flags being shown now xD xD xD...\n\n");
	printf("Yours truly,\nByteReaper\n\n");
}

void login(){
	char username[100] = "";

	printf("Username: ");
	gets(username);

	// The flag isn't printed anymore. No need for authentication
	print_flag(username);
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

![image](https://github.com/user-attachments/assets/572fe66c-ccf0-4e86-89d9-8392edc1a397)


<br>
<br>

<h1 align="center">Room Completed</h1>
<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/b9fd7425-0875-45ad-a523-1033a8c91bec"><br>
                   <img width="1000px" src="https://github.com/user-attachments/assets/b7553c80-a6aa-49d8-9bf2-20c390d02f2f"></p>
                   
<h1 align="center">My TryHackMe Journey</h1>


<div align="center">

| Date<br>          |  Streak<br>|   All Time<br>Global   |   All Time<br>Brazil |  Monthly<br>Global   |  Monthly<br>Brazil   |  SHOGUN<br>points  |   Rooms<br>completed  |  Badges<br> |
| :---------------: | :--------: | :--------------------: | :------------------: | :------------------: | :------------------: | :----------------: | :-------------------: | :---------: |
| Jun 4, 2025       |     394    |          199ᵗʰ         |            4ᵗʰ       |       2,296ᵗʰ        |           30ᵗʰ        |       106,211      |             765       |    62       |

</div>

<p align="center"> Global All Time: 200ᵗʰ <br><img width="300px" src="https://github.com/user-attachments/assets/726b48c7-e7fa-4124-b670-1bf6225a3a4d" alt="Your Image Badge"><br>
                                              <img width="1000px" src="https://github.com/user-attachments/assets/c181343e-bb88-4df3-9163-09919d4c2c9c0"><br><br>
                   Brazil All Time:   4ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/60ebc257-4bcc-498d-8642-37e47cbd23f9"><br><br>
                   Global monthly:  2,296ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/a4b1f7e8-111d-4722-8600-e71084bf47a1"><br><br>
                   Brazil monthly:   30ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/c72015e8-fb63-4030-acc6-ab8ef7b90bda"><br><br></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
<br>
<h1 align="center">Thank you very much tryhackme, munra, and hadrian3689 for developinng this experience so that I could sharpen my skills!</h1>

