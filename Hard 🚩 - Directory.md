<h1 align="center">Directory</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/ab43a0db-8c50-40e9-abc1-31e4bdd49630"><br>
July 18, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, 
and I’m excited to join you on this adventure, part of my <code>438</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Do you have what it takes to crack this case?</em>.<br>
Access it <a href="https://tryhackme.com/room/directorydfirroom">here</a>.<br><br>
<img width="1200px" src=""></p>

<br>


<br>


<h2>Task 1 . The Case</h2>
<p>A small music company was recently hit by a threat actor.<br>
The company's Art Directory, Larry, claims to have discovered a random note on his Desktop.<br>
Given that they are just starting, they did not have time to properly set up the appropriate tools for capturing artifacts. Their IT contact only set up Wireshark, which captured the events in question.<br>

You are tasked with finding out how this attack unfolded and what the threat actor executed on the system.<br>

Click on the Download Task Files button at the top of this task. You will be provided with an traffic.pcap file. Once downloaded, you can begin your analysis in order to answer the questions.<br>

Note: For free users using the AttackBox, the challenge is best done using your own environment. Some browsers may detect the file as malicious. The PCAP file is safe to download with md5 of 23393189b3cb22f7ac01ce10427886de. In general, as a security practice, download the PCAP and analyze it on a dedicated virtual machine, and not on your host OS.</p>

<h3 align="left"> Answer the questions below</h3>

<p>1.1. <em>What ports did the threat actor initially find open? Format: from lowest to highest, separated by a comma.</em><br>
<code>53,80,88,135,139,389,445,464,593,636,3268,3269,5357</code></p>

<br>

<p><em>WireShark</em></p>

```bash
tcp.completeness.syn-ack == True && ip.src == 10.0.2.75 && tcp.dstport == 47879
```

<img width="1386" height="306" alt="image" src="https://github.com/user-attachments/assets/67e912ce-a77f-4244-8bbf-441aa3d47a45" />

<br>

<p><em>TShark</em></p>

```bash
$ tshark -r trafficc.pcap -Y "ip.src == 10.0.2.75 && tcp.dstport ==47879 && tcp.flags.syn == 1 && tcp.flags.ack ==1" -T fields -e tcp.srcport
445
80
139
53
135
464
3269
88
593
3268
389
5357
636
```

```bash
$ tshark -r trafficc.pcap -Y "ip.src == 10.0.2.75 && tcp.dstport ==47879 && tcp.flags.syn == 1 && tcp.flags.ack ==1" -T fields -e tcp.srcport | sort -n
53
80
88
135
139
389
445
464
593
636
3268
3269
5357
```
