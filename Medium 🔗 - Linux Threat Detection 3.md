<h1 align="center">Linux Threat Detection 3</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/252f521c-30a8-456d-9e0f-367c9e42d96c"><br>
2025, October 16<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>528</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Cover the last stages of attacks on Linux and learn how they look in system logs.</em>.<br>
Access it <a href="https://tryhackme.com/room/linuxthreatdetection3">here</a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/a7fedf72-3ee4-4ed4-b17f-21532621a945"></p>

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

<p>
    
- launch a web browser<br>
- navigate to MachineIP:8000</p>

<img width="1308" height="323" alt="image" src="https://github.com/user-attachments/assets/32899111-b8a8-4a29-a258-cdbc937b4d8d" />

<p>

- in the <ins>Enter hostname or IP</ins> field type the command below, and hit ENTER.<br>
- identify svctrypingme.</p>

```bash
127.0.0.1 && whoami
```

<img width="1309" height="487" alt="image" src="https://github.com/user-attachments/assets/2ecffce2-e833-4caa-87db-8622665367cf" />

<br>
<br>
<br>
<p>2.2. What is the flag returned in the TryPingMe response?<br>
<code>THM{revshells_practitioner!}</code></p>
<p>

- in the <ins>Enter hostname or IP</ins> field type thw command below, and hit ENTER.<br>
- identify /opt/trypingme</p>

```bash
127.0.0.1 && pwd
```

<img width="1311" height="486" alt="image" src="https://github.com/user-attachments/assets/d72390a5-881c-4b3a-8b7b-57354bf98de8" />

<p>

- in the <ins>Enter hostname or IP</ins> field type thw command below, and hit ENTER.<br>
- identify .env.local, main.py, and templates</p>

```bash
127.0.0.1 && ls -lah /opt/trypingme
```

<img width="1306" height="574" alt="image" src="https://github.com/user-attachments/assets/65c5d968-8913-4311-bd8d-162c4c5b9b6e" />

<p>

- in the <ins>Enter hostname or IP</ins> field type thw command below, and hit ENTER.<br>
- scroll down.<br>
- identify the flag.</p>

```bash
127.0.0.1 && cat /opt/trypingme/main.py
```
<img width="926" height="818" alt="image" src="https://github.com/user-attachments/assets/50011343-9964-4e12-bd93-b287c2d602c7" />

<br>
<br>
<br>
<p>2.3. Now look at the exported auditd logs at /home/ubuntu/scenario. Which IP spawned a similar reverse shell via the TryPingMe app?<br>
<code>10.14.105.255</code></p>

<p>

- execute the command below.<br>

```bash
root@thm-vm:/home/ubuntu/scenario$ ausearch -i -if audit.log -x socat
```

<img width="1363" height="440" alt="image" src="https://github.com/user-attachments/assets/f6260fc0-81d7-4fe0-9714-a35f1bb39c4d" />



<h2 align="center">Task 3 . Privilege Escalation</h2>
<br>

<p><em>Answer the questions below</em></p>
    
<p>3.1. Which command line was used to look for the "pass" keyword in files?<br>
<code>grep -iR pass .</code></p>

<p>

- execute the command below.<br>

```bash
root@thm-vm:/home/ubuntu/scenario$ ausearch -i -if audit.log | grep proctitle
```

<img width="1374" height="604" alt="image" src="https://github.com/user-attachments/assets/bf6ba211-c409-41b6-9821-2a20c70ddb71" />

<br>
<br>
<br>
<p>3.2. Which command line was used to escalate privileges to root?<br>
<code>su root</code></p>

<p>

- execute the command below.<br>

```bash
root@thm-vm:/home/ubuntu/scenario$ ausearch -i -if audit.log | grep proctitle
```

<img width="1374" height="604" alt="image" src="https://github.com/user-attachments/assets/644c5171-3c91-44ee-b4a0-4d850e4c4e7d" />

<br>
<br>
<br>
<p>3.3. Looking at the detected .env file, what was the root password?<br>
<code>nGql1pQkGa</code></p>

<p>
    
- navigate to MachineIP:8000<br>
- in the <ins>Enter hostname or IP</ins> field type the command below, and hit ENTER.</p>

```bash
127.0.0.1 && cat /opt/trypingme/.env.local
```

<img width="1339" height="540" alt="image" src="https://github.com/user-attachments/assets/073f39e8-4f62-4bbc-9015-50d0bf26b5a0" />


<br>
<br>
<br>
<h2 align="center">Task 4 . Startup Persistence</h2>
<br>

<p><em>Answer the questions below</em></p>
    
<p>4.1. What flag did you get after running the malware persisting as a service?<br>
<code>THM{hidden_penguin!}</code></p>

<p>

- in Task 3 discover changes in <ins>systemd</ins>.<br>
- execute the command below<br>
- discover <ins>nano /etc/systemd/system/tux.service</ins></p>


```bash
root@thm-vm:/home/ubuntu/scenario$ ausearch -i -f /etc/systemd
```

<img width="1264" height="376" alt="image" src="https://github.com/user-attachments/assets/13a6e63b-d403-4e31-bee4-952225d7b9bb" />


<br>
<p>

- inspect <ins>tux.service</ins>´s content</p>

```bash
root@thm-vm:/home/ubuntu/scenario$ cat /etc/systemd/system/tux.service
```

<img width="1343" height="215" alt="image" src="https://github.com/user-attachments/assets/ab36e9fa-89dc-45e6-b5d1-75d78949cbea" />

<br>
<p>OR</p>

```bash
127.0.0.1 && cat /etc/systemd/system/tux.service
```

<p>

- execute <ins>tux.service</ins>´s content.<br>
- discover <ins>/var/lib/misc/tux</ins>.</p>

<img width="1328" height="614" alt="image" src="https://github.com/user-attachments/assets/69d8aeb7-8d87-4142-995e-1bb637203956" />

<p>

- execute <ins>tux</ins>.<br>
- uncover the flag.<br>

```bash
root@thm-vm:/var/lib/misc$ ./tux
```

<img width="1347" height="258" alt="image" src="https://github.com/user-attachments/assets/d9a51cb1-bdf8-4801-bdea-56f797cd9259" />

<br>
<br>
<br>
<p>4.2. What flag did you get after running the malware persisting as a cron job?<br>
<code>THM{ressurect_on_reboot!}</code></p>

<p>

- execute the command below.<br>
- identify <ins>/var/spool/cron/</ins>.</p>

```bash
root@thm-vm:/home/ubuntu/scenario$ ausearch -i -x crontab
```

<img width="1374" height="155" alt="image" src="https://github.com/user-attachments/assets/3867a057-bf53-47c1-aca7-fea200475806" />

<br>
<p>

- inspect <ins>/var/spool/cron/</ins> path.<br>
- identify <ins>/var/spool/cron/crontabs/root</ins>.<br>
- check <ins>root</ins>´s content.<br>
- discover <ins>/usr/sbin/phoenix</ins>.</p>

```bash
root@thm-vm:/home/ubuntu/scenario$ ls -lah /var/spool/cron
```

```bash
root@thm-vm:/home/ubuntu/scenario$ ls -lah /var/spool/cron/crontabs/
```

```bash
root@thm-vm:/home/ubuntu/scenario$ cat /var/spool/cron/crontabs/root
```

<img width="1365" height="592" alt="image" src="https://github.com/user-attachments/assets/9541c125-1589-465b-97fa-4739aa486927" />

<br>
<br>
<br>
<p>OR</p>

```bash
root@thm-vm:/home/ubuntu/scenario$ crontab -l
```

<img width="1368" height="398" alt="image" src="https://github.com/user-attachments/assets/3c6c49ec-2bf8-4fdf-bc0e-5f9149d5d76b" />

<br>
<p>

- execute <ins>phoenix</ins>.<br>
- uncover the flag.</p>

<img width="1315" height="215" alt="image" src="https://github.com/user-attachments/assets/02986e0d-654f-4c2c-836d-af8f81489f95" />

<br>
<br>
<br>
<h2 align="center">Task 5 . Account Persistence</h2>
<br>

<p><em>Answer the questions below</em></p>
    
<p>5.1. Which user was created and added to the sudo group?<br>
<code>koichi</code></p>

<p>

- execute the command belo</p>

```bash
ubuntu@thm-vm:/var/log$ grep -iE useradd auth.log
```

<img width="1365" height="110" alt="image" src="https://github.com/user-attachments/assets/19b7992c-02c1-4ce6-a341-b093b9cc2e69" />

<br>
<p>5.2. Which file was changed to allow SSH key persistence?<br>
<code>******</code></p>

<p>

- execute the command belo</p>

```bash
root@thm-vm:/home/ubuntu$ ausearch -i -f  /.ssh/authorized_keys
```

<img width="1364" height="383" alt="image" src="https://github.com/user-attachments/assets/f3bae13c-7b7d-427d-8339-bc1e9c2772eb" />

<br>
<h2 align="center">Task 6 . Targeted Attacks and Recape</h2>
<br>

<p><em>Answer the questions below</em></p>
    
<p>6.1. Does Linux ransomware exist and impact organizations worldwide? (Yea/Nay)<br>
<code>Yea</code></p>

<br>
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
<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/bb55fec6-0a92-4e92-8858-7b7b3854ac6d"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/eb66568e-1431-4234-b86c-ff97190bd3d9"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, October</h1>


<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|16      |Medium 🔗 - Linux Threat Detection 3   | 527    |      90ᵗʰ    |      4ᵗʰ     |      89ᵗʰ    |     2ⁿᵈ    | 131,066  |  1,003    |    79     |
|15      |Medium 🔗 - Windows PrivEsc, in progress| 527   |      91ˢᵗ    |      4ᵗʰ     |      83ʳᵈ    |     2ⁿᵈ    | 131,050  |  1,002    |    79     |
|15      |Medium 🔗 - Linux Threat Detection 3, in progress|527| 92ⁿᵈ    |      4ᵗʰ     |      83ʳᵈ    |     2ⁿᵈ    | 131,034  |  1,002    |    79     |
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

<p align="center">Global All Time:   90ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/25229477-1fdd-465e-a7d6-0bac60568dbf"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/1444686f-2d77-48f5-b2e0-dcc30f5422bd"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/f3e9d7d3-2e1d-4c8f-85c5-f6d1bf09d2a4"><br>
                  Global monthly:     89ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/c09ebe13-5b20-4df8-87e6-014897a9fb25"><br>
                  Brazil monthly:      2ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/fb8570de-0caa-43b0-8639-bb199c9b7909"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
