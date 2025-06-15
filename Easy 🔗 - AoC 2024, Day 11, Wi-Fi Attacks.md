

![image](https://github.com/user-attachments/assets/a2998cb3-0fed-4afd-ae1e-a8d0f633aae8)





<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 1.1. <em>What is the BSSID of our wireless interface?</em><br><a id='1.1'></a>
>> <code><strong>02:00:00:00:02:00</strong></code>

<br>

![image](https://github.com/user-attachments/assets/a2ffc4ec-0831-4042-b321-99470085ea4b)


<br>

> 1.2. <em>What is the SSID and BSSID of the access point? Format: SSID, BSSID</em><br><a id='1.2'></a>
>> <code><strong>MalwareM_AP, 02:00:00:00:00:00</strong></code>

<br>

![image](https://github.com/user-attachments/assets/1ac4ed09-38a4-43a1-bcc1-a3afa4770610)


<br>

> 1.3. <em>What is the BSSID of the wireless interface that is already connected to the access point?</em><br><a id='1.3'></a>
>> <code><strong>02:00:00:00:01:00</strong></code>

<br>

![image](https://github.com/user-attachments/assets/e61993de-8050-432e-90de-9795ba52223b)

<br>


> 1.4. <em>WWhat is the PSK after performing the WPA cracking attack?</em><br><a id='1.4'></a>
>> <code><strong>fluffy/champ24</strong></code>

<br>

![image](https://github.com/user-attachments/assets/81a80d1b-4c45-4536-a985-7a33aef8ca78)

<br>

> 1.5. <em>If you enjoyed this task, feel free to check out the Networking module.</em><br><a id='1.4'></a>
>> <code><strong>No answer needed</strong></code>

<br>

<p>Running <code>iw dev</code> and then <code>sudo iw dev wlan2 scan</code> we find a <code>BSSID</code> and <code>SSID</code> of the devicd of <code>02:00:00:00:00:00</code> and <code>MalwareM_AP</code>.</p>

![image](https://github.com/user-attachments/assets/faafb102-cc73-4058-b6a6-77df09fa1658)

<br>

![image](https://github.com/user-attachments/assets/5ecfba29-ae68-4241-be2d-990720eae759)


<br>

![image](https://github.com/user-attachments/assets/62c10a85-5757-4cb5-b474-726e3ab04bb8)

<br>

<p>Now instead of <code>managed</code> type it is <code>monitor</code> type.a</p>

<br>


![image](https://github.com/user-attachments/assets/ac6fe811-fe67-468c-9105-b642a3b8737b)

<br>

<p>From now on we will work with two terminals. One will sniff the packets on the network, and the other to execute commands. </p>

<br>

![image](https://github.com/user-attachments/assets/cd87b04d-5896-4997-a310-69f480ae10eb)

<br>


![image](https://github.com/user-attachments/assets/544b6dcf-f985-4d94-9e64-ed75f0eb47b7)

<br>

<p>Running <code>sudo airodum-ng wlan2</code> we we can see the Wireless Access Point that we already know is on the network.<br>
Here we can clearly see the <code>BSSID</code> of the router which is <code>02:00:00:00:00:00</code>, and also the <code>ESSID</code> which is <code>MalwareM_AP</code>.</p>

![image](https://github.com/user-attachments/assets/b8987a7a-cfe6-42cb-9647-1347d2a6346b)

<p>I used <code>Ctrl + C</code> for <code>Quitting</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/12e7c4a2-213b-4701-83a6-b31d54b77b45)


<br>

<p>Oned more time we can see the <code>BSSID</code> of the router which is <code>02:00:00:00:00:00</code>, and also the <code>ESSID</code> which is <code>MalwareM_AP</code>.<br>
But this time it is only listening to that router and the output is captured on the file that we specified.<br>
It is necessary to allow 1 to 5 minutes to show which clients are connected to that router.<br>

And after that time, we can notice that one station has a different <code>BSSID</code> related to the previous one, which is <code>02:00:00:00:01:00</code>.<br>
<code>02:00:00:00:01:00</code> is a client connected to that router.</p>

<br>

![image](https://github.com/user-attachments/assets/22f21e88-e334-4d87-aab8-578f7f90da30)

<br>


<p>Next we will send an <code>authentication package</code> to our router to make it disconnect and force it to restablish the 4-way handshake where the ata encrypted with the <code>PSK</code> will be exchanged and then we can brute force it.</p>

<br>

![image](https://github.com/user-attachments/assets/96d1964c-4c61-4b32-8d33-d9430bc6282f)

<br>

![image](https://github.com/user-attachments/assets/8546eda9-48f3-4e9f-abff-18e9b0a84980)

<br>

<p>It "says" <code>directed DeAuth</code> which stands for the authentication.<br>
So we can notice that the <code>authentication</code> was successful.<br>
And we can also notice evidence of the 4-way handshake occurring.<br><br>
This means that in the file where we captured that output somewhere in this file is a captured challenge that´s is encrypted to <code>psk</code> that we can simply Brute Force to get the <code>psk</code>password.</p>


<br>

![image](https://github.com/user-attachments/assets/544729f6-dcec-4ed5-8b18-6fff58218758)

<br>

<p>Now we found the <code>KEY</code>c which is <code>fluffly/champ24</code>.</p>


![image](https://github.com/user-attachments/assets/81a80d1b-4c45-4536-a985-7a33aef8ca78)

<br>


![image](https://github.com/user-attachments/assets/92b3e93f-14bb-462b-a3e5-cfb5a4d06c7a)

<br>

![image](https://github.com/user-attachments/assets/030ebb36-f6e2-4dbd-9d6f-c7b33236b567)





<br>
<h2>Room Complete</h2>
<p>Keep learning, keep growing!</p>

<p align="center"> <img width="750px" src="https://github.com/user-attachments/assets/a70777d5-a011-4193-89cd-3683b8afde67"></p>

<br>

<p align="center"> <img width="750px" src="https://github.com/user-attachments/assets/c5b646cf-4bb4-4f82-bc0d-c740d7add5ae7"></p>


<br>

<br>


<h2>My Journey<a id='7'></a></h2>
<p>Following I share the status of my journey in TryHackMe.</p>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     |
| :---------------: | :------- | :----------- | :----------- | :---------- | :--------- | :------  | :-------- |
|                   |          | WorldWide    | Brazil       | WorldWide   | Brazil     |          | Completed |
| December 12, 2024 | 220      |       940 th |        19 th |      392 nd |       2 nd | 61,356   |       468 |

</div>


<p align="center"> <img width="750px" src="https://github.com/user-attachments/assets/7fe44db6-822f-4780-8953-54b8da6b45cc"></p>

<br>

<p align="center"> <img width="750px" src="https://github.com/user-attachments/assets/566f1796-b1b3-4886-9622-6f7de2885ebd"></p>


<p style="text-align: center;">Thank you for coming. Hope to learn together again!!</p>


