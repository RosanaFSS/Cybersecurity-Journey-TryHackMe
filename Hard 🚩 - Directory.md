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




tcp.flags.syn == 1 && tcp.flags.ack == 1 && http.response.code == 200 ip.sr == 10.0.2.75

smb2.preauth_hash != ""




smb2.preauth_hash != ""

_ws.col.info == "HTTP/1.1 200   (application/http-spnego-session-encrypted)"


packet 4887

username = larry.doe
domain = directory.thm
nt proof string = e18eca5d5ed8a7a08682a3cd4e993b3e
session key = ecec611716ddf3199dfebd17161a37fc
session id = 0x000014 0000000019
server challenge = ec89ba 38b848e655

00000000000001ec89ba38b848e655

00140000000019ec89ba38b848e655

larry.doee  directory.thm  18eca5d5ed8a7a08682a3cd4e993b3e
01010000000000008212cb751250da01fc1010028b6c723900000000020012004400490052004500430054004f0052005900010010004100440053004500520056004500520004001a006400690072006500630074006f00720079002e00740068006d0003002c00410044005300650072007600650072002e006400690072006500630074006f00720079002e00740068006d0005001a006400690072006500630074006f00720079002e00740068006d00070008008212cb751250da0109001e00570053004d0041004e002f00310030002e0030002e0032002e003700350006000400020000000000000000000000


-Y "ntlmssp.messagetype == 0x00000003 || ntlmssp.messagetype == 0x00000002": Filters for NTLM messages (type 3 for authentication, type 2 for challenge).

$ tshark -r trafficc.pcap -Y "ntlmssp.messagetype == 0x00000002" -T fields -e ntlmssp.auth.username -e ntlmssp.auth.domain -e ntlmssp.ntlmv2_response.ntproofstr -e ntlmssp.auth.sesskey -e smb2.sesid -e ntlmssp.ntlmserverchallenge
                                0x0000140000000019      481505fc3d08ad40
                                        4d466ef19179c690
                                        ec89ba38b848e655
$ tshark -r trafficc.pcap -Y "ntlmssp.messagetype == 0x00000003" -T fields -e ntlmssp.auth.username -e ntlmssp.auth.domain -e ntlmssp.ntlmv2_response.ntproofstr -e ntlmssp.auth.sesskey -e smb2.sesid -e ntlmssp.ntlmserverchallenge
NULL    NULL            eb6bc50093580c7ede4d6929150ad05d        0x0000140000000019
larry.doe       directory.thm   e18eca5d5ed8a7a08682a3cd4e993b3e        ecec611716ddf3199dfebd17161a37fc
larry.doe       NULL    f6dd396748ca42ed9b5c4dedf23aeec0        08c0b176a089fbb82149510f3663a96d




]^ N;>uPlr9DIRECTORYADSERVERdirectory.thm,ADServer.directory.thmdirectory.thmuP	WSMAN/10.0.2.75

e18eca5d5ed8a7a08682a3cd4e993b3e01010000000000008212cb751250da01fc1010028b6c723900000000020012004400490052004500430054004f0052005900010010004100440053004500520056004500520004001a006400690072006500630074006f00720079002e00740068006d0003002c00410044005300650072007600650072002e006400690072006500630074006f00720079002e00740068006d0005001a006400690072006500630074006f00720079002e00740068006d00070008008212cb751250da0109001e00570053004d0041004e002f00310030002e0030002e0032002e0037003500

00040
00200
00000
00000
00000
00000


