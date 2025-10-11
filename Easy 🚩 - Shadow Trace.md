<h1 align="center">Shadow Trace</h1>
<p align="center">2025, October 10<br>Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>522</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Analyse a suspicious file, uncover hidden clues, and trace the source of the infection.</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/3bceeb7b-2d60-4a7f-8c4a-b96b56ff78f2"><br>
Access it <a href="https://tryhackme.com/room/shadowtrace">here</a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/b0ef3819-8224-4234-9edc-477f3ea0dd46"></p>

<h2>Task 1 . Scenario</h2>
<br>

<p><em>Answer the question below</em></p>
<br>

<p>1.1. Click here to start the challenge<br>
<code>No answer needed</code></p>
<br>

<h2>Task 2 . File analysis</h2>
<br>


<p><em>Answer the questions below</em></p>
<br>

<p>2.1. What is the architecture of the binary file windows-update.exe?<br>
<code>64-bit</code>

<img width="1279" height="297" alt="image" src="https://github.com/user-attachments/assets/711a0ff0-8e2a-4fbf-b6a9-758181fc7002" />

<br>
<br>
<br>
<p>2.2. What is the hash (sha-256) of the file windows-update.exe?<br>
<code>B**************************************************************C</code>

<img width="1285" height="168" alt="image" src="https://github.com/user-attachments/assets/331e485a-1f2b-47d4-a094-7a9c64addfbd" />

<br>
<br>
<br>
<p>2.3. Identify the URL within the file to use it as an IOC<br>
<code>http://tryhatme.com/update/security-update.exe</code>

<img width="1285" height="186" alt="image" src="https://github.com/user-attachments/assets/7f03ca76-56d2-4e28-bc49-3eaeaec0797d" />

<br>
<br>
<br>
<p>2.4. With the URL identified, can you spot a domain that can be used as an IOC?<br>
<code>responses.tryhatme.com</code>

<br>
<br>
<br>
<p>2.5. Input the decoded flag from the suspicious domain<br>
<code>THM{***_**_****_****_******}</code>

<img width="1069" height="185" alt="image" src="https://github.com/user-attachments/assets/84c2a431-d209-418a-b7eb-0065ebf62b5a" />

<br>
<br>
<br>
  
<img width="1290" height="258" alt="image" src="https://github.com/user-attachments/assets/d49be025-c067-4a75-bad8-43500f75e0a6" />

<br>
<br>
<br>
<p>2.6. What library related to socket communication is loaded by the binary?<br>
<code>WS2_32.dll</code></p>

<img width="868" height="162" alt="image" src="https://github.com/user-attachments/assets/2cfd1b76-0ced-4edc-a216-92757760b17d" />

<br>
<br>
<br>
<h3>Task 3 . Alerts Analysis</h3>
<p>Click on the View Site button attached to this task to display the static site in split view. Review the alternatives and answer the questions below.<br>

Alternatively, if you can not see all the columns in split view, you can open the static site in full screen by clicking the link below:</p>

<p><em>Answer the questions below</em></p>
<br>

<p>3.1. What is the architecture of the binary file windows-update.exe?<br>
<code>https://********.***/***/****.***)</code>

<p>

- decode From Base64</p>

<br>
<p>3.2. What is the architecture of the binary file windows-update.exe?<br>
<code>https://********.***/***/****.***)</code>

<img width="1086" height="195" alt="image" src="https://github.com/user-attachments/assets/a7a293bd-12a8-4fe6-bb0a-ab10d4af928d" />

<br>
<br>
<br>
<p>3.3.What's the name of the file saved in the alert triggered by chrome.exe?<br>
<code>****.***</code>
<p>

- it´s in plain text</p>

<br>
<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/85237056-26f4-42e2-9b20-0bc258bfadf2"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/10305172-6f77-46ea-aae1-84af9b2933bc"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, October</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|10      |Easy 🚩 - Shadow Trace                 | 522    |     101ˢᵗ    |      4ᵗʰ     |     159ᵗʰ    |     3ʳᵈ    | 129,810  |    998    |    76     |
|10      |Easy 🔗 - Defensive Security Intro     | 522    |     103ʳᵈ    |      4ᵗʰ     |     357ᵗʰ    |     3ʳᵈ    | 129,405  |    997    |    76     |
|10      |Easy 🔗 - 25 Days of Cyber Security, Day 2| 522|      103ʳᵈ    |      4ᵗʰ     |     355ᵗʰ    |     3ʳᵈ    | 129,405  |    996    |    76     |
|9       |Medium 🔗 - Linux Threat Detection 2   | 521    |     103ʳᵈ    |      4ᵗʰ     |     326ᵗʰ    |     3ʳᵈ    | 129,373  |    996    |    76     |
|9       |Medium 🚩 - WWBuddy                    | 521    |     103ʳᵈ    |      4ᵗʰ     |     390ᵗʰ    |     4ᵗʰ    | 129,293  |    995    |    76     |
|8       |Hard 🚩 - Motunui                      | 520    |     103ʳᵈ    |      4ᵗʰ     |     383ʳᵈ    |     4ᵗʰ    | 129,201  |    994    |    76     |
|8       |Easy 🔗 - Man-in-the-Middle            | 520    |     103ʳᵈ    |      4ᵗʰ     |     390ᵗʰ    |     4ᵗʰ    | 129,141  |    993    |    76     |
|7       |Medium 🚩 - Profiles, in progress      | 519    |              |              |              |            | 129,021  |    992    |    76     |
|6       |Medium 🚩 - VulnNet                    | 518    |     105ᵗʰ    |      4ᵗʰ     |     348ᵗʰ    |     5ᵗʰ    | 129,021  |    992    |    76     |
|6       |Easy 🚩 - DearQA                       | 518    |     105ᵗʰ    |      4ᵗʰ     |     333ʳᵈ    |     6ᵗʰ    | 128,991  |    991    |    76     |
|5       |Medium 🚩 - Frank & Herby try again.....| 517   |     106ᵗʰ    |      4ᵗʰ     |     300ᵗʰ    |     5ᵗʰ    | 128,931  |    990    |    76     |
|4       |Medium 🚩 - Frank & Herby make an app  | 516    |     105ᵗʰ    |      4ᵗʰ     |     233ʳᵈ    |     3ʳᵈ    | 128,871  |    989    |    76     |
|4       |Info ℹ️ - OverlayFS - CVE-2021-3493    | 516    |     105ᵗʰ    |      4ᵗʰ     |     235ᵗʰ    |     3ʳᵈ    | 128,841  |    988    |    76     |
|3       |Medium 🚩 - XDR: Operation Global Dagger2| 515  |     104ᵗʰ    |      4ᵗʰ     |     149ᵗʰ    |     3ʳᵈ    | 128,833  |    987    |    76     |
|3       |Medium 🚩 - VulnNet: dotpy             | 515    |     108ᵗʰ    |      4ᵗʰ     |     741ˢᵗ    |    11ˢᵗ    | 128,563  |    986    |    76     |
|2       |Medium 🔗 - Data Exfiltration Detection| 514    |     108ᵗʰ    |      4ᵗʰ     |     521ˢᵗ    |     8ᵗʰ    | 128,503  |    985    |    76     |
|1       |Medium 🔗 - Network Discovery Detection| 513    |     108ᵗʰ    |      4ᵗʰ     |     875ᵗʰ    |     7ᵗʰ    | 128,407  |    984    |    76     |
|1       |Medium 🚩 - Intranet                   | 513    |     108ᵗʰ    |      4ᵗʰ     |    3,357ᵗʰ   |    57ᵗʰ    | 128,335  |    983    |    76     |

</h6></div>

<br>

<img width="1881" height="893" alt="image" src="https://github.com/user-attachments/assets/99c4bac9-290b-4f03-9557-dc850f02f17e" />


<p align="center">Global All Time:   101ˢᵗ<br><img width="250px" src="https://github.com/user-attachments/assets/991caa23-09ce-43a5-81ee-ccdaff825913"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/1591ddce-f673-4819-8f1b-fbee751b1d6a"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/737dad79-b537-4728-acd3-020844fb9115"><br>
                  Global monthly:    159ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/99c4bac9-290b-4f03-9557-dc850f02f17e"><br>
                  Brazil monthly:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/a9d0cf10-32b1-415b-a22a-e33205711b55"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
