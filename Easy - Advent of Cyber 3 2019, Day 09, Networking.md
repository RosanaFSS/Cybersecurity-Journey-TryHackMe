<p align="center">March 20, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{318}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
  <img width="160px" src="https://github.com/user-attachments/assets/67d84414-d9e4-4068-be03-f10e812305dd"></p>


<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{[ Day 9 ] - Advent of Cyber 3 (2021)}}$$
</h1>
<p align="center">Get started with Cyber Security in 25 Days - Learn the basics by doing a new, beginner friendly security challenge every day leading up to Christmas. It is classified as an easy-level walkthrough, and you can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed. <a href="https://tryhackme.com/room/adventofcyber3">Advent of Cyber 3 (2021)</a>.</p>
                                                              
<p align="center"> <img width="900px" src=""> </p>

<br>

<p align="center"> <img width="900px" src=""> </p>

<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{Networking | Where is All This Data Going}}$$
</h1>

<p>McSkidy recently found out that a large amount of traffic is entering one system on the network. Use your traffic analysis skills to determine what kind of activities Grinch Enterprises are performing.</p>

<p>In this task, we will walk you through the required skills and knowledge to perform a basic packet analysis using Wireshark.<br>

Packet analysis is a technique used to capture and intercept network traffic that passes the computer’s network interfaces. Packet analysis may also be called with different terms such as packet sniffer, packet analyzer, protocol analyzer, or network analyzer. As a cybersecurity individual, gaining packet analysis skills is an important requirement for network troubleshooting and communication protocol analysis. Using network analysis tools such as Wireshark, it captures network packets in real-time and displays them in a human-readable format. It provides many advanced features, including the live capture and offline analysis. This task covers the packet analysis steps in detail using Wireshark to analyze various protocols (unencrypted protocols) such as HTTP, DNS, and FTP.</p>

<h3>Required Skills and Knowledge</h3>

<p>We’re assuming that the user has basic background skills to complete this task, requires theoretical and practical knowledge, including basic networking concepts, TCP/IP Stack, OSI Model, and TCP handshake. This applies not only to packet analysis but also to most other topics we will deal with in cybersecurity.</p>

<br>

<h3>Packet Analysis Tools</h3>

<p>There are many tools that are used in network traffic analysis and network sniffing. Each of these tools provides a different way to capture or dissect traffic. Some offer ways to copy and capture, while others read and ingest using different interfaces. In this room, we will explore Wireshark. Keep in mind that these tools require administrator privileges.</p>

<br>

<h3>What is Wireshark?</h3>

<p>Wireshark is pre-installed on the THM AttackBox, and you can just launch the THM AttackBox by using the Start AttackBox button and opening Wireshark.</p>

<p>If you want to do this challenge on your own computer, Wireshark can be downloaded from here: <a href="https://www.wireshark.org/download.html"><code>Download Wireshark</code></a>.<br>

For this task, we have prepared a PCAP file to download and follow the instructions and apply the required packet analysis skills using different scenarios. If you're using the AttackBox you don't need to download the file as it's already on the machine; the AoC3.pcap file is in the following location: /root/Rooms/AoC3/Day9/AoC3.pcap.<br>

We can run Wireshark and import the provided PCAP file as follows,</p>

![image](https://github.com/user-attachments/assets/59ff6856-ca18-4fdb-8481-ac2d7333a05f)

<p>The Wireshark interface has five major components: The command menus are standard pulldown menus located at the top of the window. Of interest to us now are the File and Capture menus. The File menu allows you to save captured packet data or open a file containing previously captured packet data, and exit the Wireshark application.<br>

The display filter section is where we can specify rules to find certain packets. The listing of captured packets shows all sent and received network packets. This section includes important fields that are used in the filter section, such as source and destination IP addresses, protocols, and information. Next, the details of a selected packet header. This section shows details about selected network packets and shows all headers, including all TCP layers information. Finally, the packet content which shows the packet content in hexadecimal and ASCII format.</p>



![image](https://github.com/user-attachments/assets/f2d50d29-fbc2-44eb-8075-f16fd13a0c98)

<br>

<h3>Filters</h3>

<p>Berkeley Packet Filter (BPF) syntax is used in packet analyzers to filter specific packets pre-capture. Filtering packets is beneficial when locating information within a packet capture process. Wireshark's syntax is the primary method we will use in this room to locate certain protocols and information. Below we have included some examples of using Wireshark display filters:<br>

Let's assume that we are looking for all packets that have been sent or received by the following IP address: 172.21.2.116. Thus, the following filter is helping us to display all network packets that have the IP address 172.21.2.116: ip.addr == 172.21.2.116 </p>

![image](https://github.com/user-attachments/assets/c58c4163-85ad-48d4-ae6f-2afe6ff1ff70)

<p>As a result, we can see that we were able to show only the packet(s) that we needed.<br>

Next, we can also specify certain protocols, such as HTTP showing all packets for this protocol. We can also specify a domain name to narrow down the search. The following example shows that we are looking for HTTP packets that have the google.com  domain name: http contains google.com </p>

![image](https://github.com/user-attachments/assets/a01f3f06-a746-4d04-83e9-55846714590f)

<p>Next, we can also look at a specific port. Let's try to filter and list all packets for remote desktop protocol. We can do that by using tcp.port : tcp.port == 3389 </p>

![image](https://github.com/user-attachments/assets/975af0d4-c909-4086-8954-38d68b0381b7)

<p>However, assume that you are monitoring the network traffic and you want to exclude the RDP packets. In this case, we can use the not Wireshark rule as shown below.</p>

![image](https://github.com/user-attachments/assets/5b9d58ee-34d7-476c-b73e-4779970c8b31)

<p>Next, we will perform the packet analysis technique using Wireshark on various protocols, including HTTP, FTP, and DNS. <br>

Note: Make sure to open the Wireshark tool, and the AoC3.pcap file is imported to follow up with the content.</p>

<br>

<h3>HTTP #1 - GET</h3>

<p>We will be performing a packet analysis on the pre-captured network packets in the PCAP to analyze HTTP traffic. Once we open the PCAP using Wireshark, it will show a lot of network traffic since we connect using RDP protocol, making our work harder. However, we will be using a Wireshark filter to focus on web requests only. In this case, we are dealing with the HTTP protocol. Therefore, we can use Wireshark rules to make it easier. We can apply the following rule to the Wireshark filter to show only the HTTP traffic: http.<br>

The following figure shows all HTTP traffic that has been sent to and from the webserver. In the first packet, we can see that the web request is sent from our machine 192.168.100.95  to the webserver, which is also our machine. In the information section, we can see also that we sent a GET request trying to get /admin content. On the next packet, the webserver replied to the sender with an HTTP response code 404, which means it is not found. Suppose we need more details on a particular packet. In that case, we can expand (using the > sign) the Hypertext transfer protocol subtree for more details about the sender request, such as the IP address of the host, web user agent, and other information.</p>

![image](https://github.com/user-attachments/assets/52a374ab-9d1a-4cd9-8a7d-a50c52894a36)

<p>We can specify the HTTP method. In this case, we can specify to show all the GET requests using the following filter: <br>http.request.method == GET. Keep following the GET HTTP requests and answer the question in this task.</p>

<br>

<h3>HTTP #1 - POST</h3>

<p>In the second scenario, we check HTTP POST requests used to log into a web portal. In this section, we will be performing packet analysis to capture the username and password of the POST request. Make sure to open the PCAP file to perform the packet analysis. Your goal in this section is to inspect the HTTP packet to get the username and password. For more details, you double-click on the required packet that has the POST request. We can see all the required information we need in the hexadecimal section in cleartext. In addition, there are other ways that show more information the HTTP request, which is to follow the HTTP stream. We can do that by right-clicking on the required packet and then selecting follow -> TCP Stream to see the web requests and their details.<br>

In this section, we have to find the POST request and explore all packet information to answer question 2 and 3 in this task.</p>

<br>

<h3>DNS</h3>
<p>DNS is like a giant phone book that takes a URL (Like https://tryhackme.com/) and turns it into an IP address. This means that people don’t have to remember IP addresses for their favorite websites.<br>

The provided PCAP file has DNS packets that have been received by our server. The domain name that we will look into is packet.tryhackme.com. Please note that is the domain name used in the PCAP file as an example.<br>

First, make sure that you open the PCAP file. Then, using the Wireshark filter, we will specify DNS packets. This can be done using the udp.port filter. By default, the DNS protocol is running on UDP port 53 and sometimes on TCP port 53. In this task, we will go with the UDP port. Thus, the Wireshark filter will be as follows: udp.port == 53 or dns only.</p>


![image](https://github.com/user-attachments/assets/9b62b7a2-68d3-428b-bad0-adfc4849db17)

<p> By double-clicking on the first DNS packet, we can see as follows:</p>

![image](https://github.com/user-attachments/assets/93f34efe-2235-4d10-a9a0-f62e9c2618c2)

<p>By expanding the Domain Name System (query) subtree, it is obvious that this packet is a question Questions: 1, where the client queries a domain name and looks for an answer from the server. Also, by checking the Queries subtree, we can see that the client is asking for a type A record of the packet.tryhackme.com domain name.<br>

Next, we will be looking at the response to the DNS request. In Wireshark, note that in the query request, which is the first DNS request, in the info field, we can see Transaction ID with a value of query 0xef8e. Note that this query reference number may vary in your situation. Thus, this query reference number is used to find the right DNS response of that query. To confirm that, check the field section where showing query response 0xef8e A packet.tryhackme.com.</p>

![image](https://github.com/user-attachments/assets/656ef1e8-da09-4eba-9690-40485d543782)

<p>By double-clicking on the required packet, we can see that it has an answer section, where it has the answer to our query, which is Address: 127.0.0.1. This means that the type A DNS request of the packet.tryhackme.com  is 127.0.0.1. Note that the PCAP file may have different IPs or extra packets that have not been discussed. There are other DNS requests that have been generated in the PCAP file. Now, dig more into DNS queries and responses in Wireshark and answer question 4 in this task.</p>

<br>


<h3>FTP</h3>
<p>The provided PCAP file has FTP packets that have been received by our server. For this task,  we will be looking at FTP traffic in Wireshark. Like other protocols, we will be using Wireshark filters to look into FTP packets. By default, the FTP server is listening on TCP port 21. Therefore, we filter and list all FTP packets by using the following filter: ftp or tcp.port == 21 <br>

The following figure shows all FTP packets, and we can see all packet details by checking the field section. It is obvious that the sender is connected to the FTP server and the server responded with the FTP server header, vsFTPd 3.0.3. Next, the user sent an FTP request with tryhackftp as a user command which is the username of the FTP server.</p>

![image](https://github.com/user-attachments/assets/caabd409-431c-4e1c-9c69-aa41b56fecf1)


<p>Keep checking the FTP packets in Wireshark and answer question 5 and 6 in this task. We can also show all FTP commands by choosing the first FTP packet and right-clicking on it. Then, select follow -> TCP-Steam.<br>

The user logged into the FTP server using a username and password and uploaded a secret file. Thus, the current Wireshark filter will not show the packet of the actual uploaded file. Instead, we can use the ftp-data Wireshark filter to list the packets that have the content of the file. Apply this filter and answer the final question in this task.</p>


<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>


> 1.1. <em>In the HTTP #1 - GET requests section, which directory is found on the web server?
> <img width="700px" src="https://github.com/user-attachments/assets/bf7bcc5c-7ae3-45e1-a8d2-f2ac5ade0fa7"></em><br>Hint : Apply following filter: http.request.method == GET. Then Look for HTTP requests that have "200 OK" response.<a id='1.1'></a>
>> <code><strong>login</strong></code><br><br>


![image](https://github.com/user-attachments/assets/8989ef6a-219b-47a0-abc8-abb7b84ce052)


<br>

![image](https://github.com/user-attachments/assets/e7fb695c-8dca-4f21-85f6-995f1b6bf354)

<p>Clicked <code>Open</code>.</p>

<p>Typed <code>http.request.method == GET</code> in the <code>filter</code> field.<br>
Hit <code>ENTER</code>.</p>

![image](https://github.com/user-attachments/assets/8dac39e0-d78b-49b9-bc5a-2f738c040901)

<p>The major part of the requests are related to <code>/login</code>.</p>


<br>

> 1.2. <em>What is the username and password used in the login page in the HTTP #2 - POST section? 
> <img width="700px" src="https://github.com/user-attachments/assets/a1846739-2623-4a40-af49-cc8cea28ffc8"></em><br>Hint : Apply following filter: http.request.method == POST. Then select the required packet, and finally expand the HTML form URL encoded section.<a id='1.2'></a>
>> <code><strong>McSkidy:Christmas2021</strong></code><br><br>

<p>Typed <code>http.request.method == POST</code> in the <code>filter</code> field.<br>
Hit <code>ENTER</code>.</p>


![image](https://github.com/user-attachments/assets/7898dd39-79ee-4a8c-b404-ee44bc6b24af)

<br>

<p>Right-clicked over the first packet.<br>
Clicked <code>Follow</code>.<br>
Clicked <code>HTTP Stream</code>.</p>

![image](https://github.com/user-attachments/assets/9fdf6296-5746-41cc-9435-4791b45b3a1a)

<br>

![image](https://github.com/user-attachments/assets/258c043f-3410-4868-8c6f-5aa1990f88ff)


<br>

> 1.3. <em>What is the User-Agent's name that has been sent in HTTP #2 - POST section?</em><br>Hint : Apply following filter: http.request.method == POST. Then select the required packet, and finally expand the Hypertext Transfer Protocol section. Find the User-Agent value.<a id='1.3'></a>
>> <code><strongTryHackMe-UserAgent-THM{d8ab1be969825f2c5c937aec23d55bc9}</strong></code><br><br>

![image](https://github.com/user-attachments/assets/b3b1c75a-47f6-4bfb-a2c9-a21fda60da2f)

<br>

<p>Another way to discover the agent is perform the same steps as in 1.2..</p>


![image](https://github.com/user-attachments/assets/51dd78bf-1c64-4d7c-aec3-39b6239dcb37)

<br>

> 1.4. <em>In the DNS section, there is a TXT DNS query. What is the flag in the message of that DNS query?</em><br>
> <img width="700px" src="https://github.com/user-attachments/assets/802775c0-2e07-4b10-b8d5-4a52f69ed2f9"
> Hint : Apply the following filter: dns or udp.port==53. Then find the required response packet which has TXT record. Finally right click on it, Follow -> UDP Stream.<a id='1.4'></a>
>> <code><strongTryHackMe-UserAgent-THM{d8ab1be969825f2c5c937aec23d55bc9}</strong></code><br><br>


<p>Typed <code> dns or udp.port==53T</code> in the <code>filter</code> field.<br>
Hit <code>ENTER</code>.</p>


![image](https://github.com/user-attachments/assets/f83ecbe1-bad4-4057-93a1-202616228f2a)


<br>

<p>Right-clicked over the first packet.<br>
Clicked <code>Follow</code>.<br>
Clicked <code>UDP Stream</code>.</p>


![image](https://github.com/user-attachments/assets/6ac5fad5-ae4c-4986-90d1-9d30331d299f)

<br>

![image](https://github.com/user-attachments/assets/679120ff-7bb7-4665-9458-b20163c33567)


<br>

<p>Navigated to the <code>streams</code>.  Note: the one above is <code>Stream 3</code>.</p>


















<br>

<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$
</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          | WorldWide    | Brazil       | WorldWide   | Brazil     |          | Completed |           |
| March 20, 2025    | 318      |     354ᵗʰ    |        8ᵗʰ   |    835ᵗʰ    |      11ˢᵗ  |  87,001  |       621 |   59      |

</div>

<p align="center"> Global All Time: 354ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/ab1fa808-049c-4dad-a848-b609307283dc"> </p>

<p align="center"> Brazil All Time: 8ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/6d0501d4-836c-4397-90c3-f4fde161ae38"> </p>

<p align="center"> Global monthly: 835ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/edff857b-d678-4f7b-8d9f-183195ef936e)"> </p>

<p align="center"> Brazil monthly: 11ˢᵗ<br><br><img width="900px" src="https://github.com/user-attachments/assets/497d78b1-bef4-49d2-87db-c24261416a87"> </p></p>
