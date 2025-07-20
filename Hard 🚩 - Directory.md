<h1 align="center">Directory</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/ab43a0db-8c50-40e9-abc1-31e4bdd49630"><br>
July 19, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, 
and I’m excited to join you on this adventure, part of my <code>438</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Do you have what it takes to crack this case?</em>.<br>
Access it <a href="https://tryhackme.com/room/directorydfirroom">here</a>.<br><br>
<img width="1200px" src="https://github.com/user-attachments/assets/07ccf47c-c3fa-4496-b8b7-92aa43c9cdb2"></p>

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

<p>1.1. What ports did the threat actor initially find open? <em>Format: from lowest to highest, separated by a comma.</em><br>
<code>53,80,88,135,139,389,445,464,593,636,3268,3269,5357</code></p>

<br>

<p><em>WireShark</em></p>

```bash
tcp.completeness.syn-ack == True && ip.src == 10.0.2.75 && tcp.dstport == 47879
```

<img width="1386" height="306" alt="image" src="https://github.com/user-attachments/assets/67e912ce-a77f-4244-8bbf-441aa3d47a45" />

<br>
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

<br>

<p>1.2. What ports did the threat actor initially find open? <em>Format: from lowest to highest, separated by a comma.</em><br>
<code>directory.thm\larry.doe</code></p>

<img width="1762" height="102" alt="image" src="https://github.com/user-attachments/assets/0c01ce32-537c-4814-9419-84b06956a4a2" />

<br>

<p>1.3. The threat actor captured a hash from the user in question 2. What are the last 30 characters of that hash?</em><br>
<code>55616532b664cd0b50cda8d4ba469f</code></p>

<img width="1740" height="503" alt="image" src="https://github.com/user-attachments/assets/627919d7-30b9-4b85-8254-b8a02bfeb7f7" />

<br>

<p>1.4. What is the user's password?</em><br>
<code>Password1!</code></p>

<img width="773" height="162" alt="image" src="https://github.com/user-attachments/assets/19955893-f22c-4560-89de-c1d035313cc2" />

```bash
larry.doe@DIRECTORY.THM:f8716efbaa984508ddde606756441480$805ab8be8cfb018a282718f7c040cd43924c6f9afeb6171230bbd3dccc79294dcf2f877a44c1a0981aadb7bb7a9510dd52d8dda4039ef4dcb444f18c9902be1623035e10aebf16ce4bdf5f7064f480e67e96ec2eb32bad95c5a1247bd7a241273fe80e281f4e6a99926f7969fcf803190c7096b947a33407f8578d4c0fb8b52d2aa8d0405a44b72bd21e014563cb71e82aee0e12538d0d440c930b98abf766e18ddc99a964e6e812ecf8dc8994a912a02074d40e5e6906915c1d216653d45df88636b51656f2c37de2020a2fd86ee7ecf6f0afe3f509fd31144e1573f9587155616532b664cd0b50cda8d4ba469f
```

<img width="1739" height="493" alt="image" src="https://github.com/user-attachments/assets/dd468948-5556-44ec-b502-c94df276edde" />

<br>

<p>1.5. What were the second and third commands that the threat actor executed on the system? Format: command1,command2</em><br>
<code>_____________________________</code></p>




```bash
tcp.flags.syn == 1 && tcp.flags.ack == 1 && http.response.code == 200 ip.sr == 10.0.2.75
```

```bash
smb2.preauth_hash != ""
```


```bash
$ tshark -r trafficc.pcap -Y "ntlmssp.messagetype == 0x00000002" -T fields -e ntlmssp.auth.username -e ntlmssp.auth.domain -e ntlmssp.ntlmv2_response.ntproofstr -e ntlmssp.auth.sesskey -e smb2.sesid -e ntlmssp.ntlmserverchallenge
                                0x0000140000000019      481505fc3d08ad40
                                        4d466ef19179c690

                                       ec89ba38b848e655
```

```bash
$ tshark -r trafficc.pcap -Y "ntlmssp.messagetype == 0x00000003" -T fields -e ntlmssp.auth.username -e ntlmssp.auth.domain -e ntlmssp.ntlmv2_response.ntproofstr -e ntlmssp.auth.sesskey -e smb2.sesid -e ntlmssp.ntlmserverchallenge
NULL    NULL            eb6bc50093580c7ede4d6929150ad05d        0x0000140000000019
larry.doe       directory.thm   e18eca5d5ed8a7a08682a3cd4e993b3e        ecec611716ddf3199dfebd17161a37fc
larry.doe       NULL    f6dd396748ca42ed9b5c4dedf23aeec0        08c0b176a089fbb82149510f3663a96d
```
