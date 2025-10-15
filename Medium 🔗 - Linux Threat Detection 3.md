<h1 align="center">Linux Threat Detection 3</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/252f521c-30a8-456d-9e0f-367c9e42d96c"><br>
2025, October 15<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>527</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Cover the last stages of attacks on Linux and learn how they look in system logs.</em>.<br>
Access it <a href="https://tryhackme.com/room/linuxthreatdetection3">here</a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/5f68a06d-e228-49fe-9617-73a9175d5551"></p>

<h2 align="center">Task 1 . Introduction</h2>
<br>

<p><em>Answer the question below</em></p>

<p>1.1. Let´s go!<br>
<code>No answer needed</code></p>

<h2 align="center">Task 2 . Reverse Shells</h2>
<br>

<p><em>Answer the questions below</em></p>
    
<p>2.1. Run 127.0.0.1 && whoami in the TryPingMe web app. What output do you see after the ping results?<br>
<code>svctrypingme</code></p>

```bash
127.0.0.1 && ls -lah cat /opt/trypingme/main.py
```

<img width="909" height="268" alt="image" src="https://github.com/user-attachments/assets/8b1f0c28-e141-4639-8fd1-cf326b4ec9a2" />

<br>
<br>
<br>
<p>2.2. What is the flag returned in the TryPingMe response?<br>
<code>THM{revshells_practitioner!}</code></p>

```bash
127.0.0.1 && ls -lah cat /opt/trypingme/main.py
```

<p>2.3. Now look at the exported auditd logs at /home/ubuntu/scenario. Which IP spawned a similar reverse shell via the TryPingMe app?<br>
<code>xx.xx.xxx.xxx</code></p>

```bash
root@thm-vm:/home/ubuntu/scenario$ ausearch -i -if audit.log | grep proctitle=socat
```

```bash
root@thm-vm:/home/ubuntu/scenario$ ausearch -i -if audit.log | grep socat
```

<h2 align="center">Task 3 . Privilege Escalation</h2>
<br>

<p><em>Answer the questions below</em></p>
    
<p>3.1. Which command line was used to look for the "pass" keyword in files?<br>
<code>grep -iR pass .</code></p>

```bash
root@thm-vm:/home/ubuntu/scenario$ ausearch -i -if audit.log
```

<img width="1286" height="312" alt="image" src="https://github.com/user-attachments/assets/a9d48d88-6c51-4fb4-ad58-67a6620f1d0f" />


<p>3.2. Which command line was used to escalate privileges to root?<br>
<code>su root</code></p>

```bash
root@thm-vm:/home/ubuntu/scenario$ ausearch -i -if audit.log
```

<img width="1255" height="81" alt="image" src="https://github.com/user-attachments/assets/744ded39-102f-45cb-98d0-c7be27a0cffa" />

<p>3.3. Looking at the detected .env file, what was the root password?<br>
<code>**********</code></p>

```bash
127.0.0.1 && cat /opt/trypingme/.env.local
```

<img width="905" height="314" alt="image" src="https://github.com/user-attachments/assets/a57dc430-1e49-4055-8bc9-ceda3f07e903" />

<br>
<br>
<br>
<h2 align="center">Task 4 . Startup Persistence</h2>
<br>

<p><em>Answer the questions below</em></p>
    
<p>4.1. What flag did you get after running the malware persisting as a service?<br>
<code>_____________________</code></p>

<p>4.2. What flag did you get after running the malware persisting as a cron job?<br>
<code>_____________________</code></p>


<h2 align="center">Task 5 . Account Persistence</h2>
<br>

<p><em>Answer the questions below</em></p>
    
<p>5.1. Which user was created and added to the sudo group?<br>
<code>******</code></p>

```bash
root@thm-vm:/var/log$ cat auth.log | grep add
```

<p>5.2. Which file was changed to allow SSH key persistence?<br>
<code>******</code></p>

```bash
root@thm-vm:/home/ubuntu$ ausearch -i -f  /.ssh/authorized_keys
```

<h2 align="center">Task 6 . Targeted Attacks and Recape</h2>
<br>

<p><em>Answer the questions below</em></p>
    
<p>6.1. Does Linux ransomware exist and impact organizations worldwide? (Yea/Nay)<br>
<code>Yea</code></p>

<p>6.2. Should you learn Linux threats even if working with Windows? (Yea/Nay)<br>
<code>Yea</code></p>


<h2 align="center">Task 7 . Conclusion</h2>
<p>Throughout a series of scenarios and real-world examples, you explored more complex, targeted Linux attacks: How adversaries overcome access constraints, how they maintain long-term persistence, and what goals they pursue.<br>

Many SOC teams skip Linux monitoring, but now you know why it's a dangerous blind spot and are prepared to detect complete attack chains in SIEM or directly on the host. We hope the auditd practice wasn't too painful, and that you enjoyed the Linux Threat Detection journey!</p>

<p><em>Answer the question below</em></p>
    
<p>7.1. Complete the room!<br>
<code>No answer needed</code></p>

<br>
<br>
<br>

<h1 align="center">In Progress</h1>
<p align="center"><img width="1200px" src=""><br>
                  <img width="1200px" src=""></p>

<h1 align="center">My TryHackMe Journey ・ 2025, October</h1>


<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|15      |Medium 🔗 - Linux Threat Detection 3   | 527    |      92ⁿᵈ    |      4ᵗʰ     |      83ʳᵈ    |     2ⁿᵈ    | 131,034  |  1,002    |    79     |
|14      |Medium 🔗 - Windows PrivEsc, in progress| 526   |      92ⁿᵈ    |      4ᵗʰ     |      85ʰ     |     2ⁿᵈ    | 130,954  |  1,002    |    79     |
|13      |Hard 🚩 - M4tr1x: Exit Denied          | 525    |      92ⁿᵈ    |      4ᵗʰ     |      76ᵗʰ    |     2ⁿᵈ    | 130,938  |  1,002    |    79     |
|12      |Easy 🔗 - Atlas                        | 524    |     101ˢᵗ    |      4ᵗʰ     |     251ˢᵗ    |     3ʳᵈ    | 129,902  |  1,001    |    76     |
|11      |Easy 🔗 - Brute Force Heroes           | 523    |     101ˢᵗ    |      4ᵗʰ     |     217ᵗʰ    |     3ʳᵈ    | 129,878  |  1,000    |    76     |
|11      |Hard 🚩 - Rocket                       | 523    |     102ⁿᵈ    |      4ᵗʰ     |     211ˢᵗ    |     3ʳᵈ    | 129,870  |    999    |    76     |
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


<p align="center">Global All Time:   92ⁿᵈ<br><img width="250px" src="https://github.com/user-attachments/assets/889f629c-a423-4c63-a1d9-12aabb03b6f7"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/0c47caa7-a7b2-4f67-9d52-44524e4287e4"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/80632e89-2a79-471c-b603-48d25981076b"><br>
                  Global monthly:     83ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/711eca7f-16a8-4888-8df8-5d15985459e7"><br>
                  Brazil monthly:      2ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/a53f9590-55f3-4775-a02f-4a95d658d779"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
