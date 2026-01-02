<h3> Welcome to the <em>TryHackMe ...</em></h3>
<h1>Cyber Security 101 learning path > Networking ></h1>
<h2>Networking Concepts</h2>
<p>Learn about the ISO OSI model and the TCP/IP protocol suite.</p><br>
<p>October 26, 2024<br></p><br>

<img src="https://github.com/user-attachments/assets/fbf371c4-79e4-4920-abae-bb19e5db3aea" height="200" width="200">

![image](https://github.com/user-attachments/assets/4454654a-ca03-4e24-9d49-e219bafc1fe8)


<p>Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure. It´s key part of my 173-day-streak. Let´s get started!!<br><br>
Access this TryHackMe Room clicking <a href="https://tryhackme.com/r/room/networkingconcepts">Networking Concepts</a></p>

<h2>Task 1 - Introduction</h2>

<p>Have you ever wondered why you need an IP address to access the Internet? Is it true that an IP address can uniquely identify the user? Are you curious to learn what the life of a packet looks like? If the answer is yes, let’s dive in!<br><br>

This room is the first room in a series of four rooms dedicated to introducing the user to vital networking concepts and the most common networking protocols:</p>

<ol type="1. ">
  <li>Networking Concepts (this room)</li>
  <li>Networking Essentials</li>
  <li>Networking Core Protocols</li>
  <li>Networking Secure Protocols</li>
</ol></p>

<h2>Room Prerequisites</h2>
<p>This room expects that you know terms such as IP address and TCP port number; however, we don’t expect that the reader is able to explain such terms in proper technical depth. If you are unfamiliar with these terms, please consider joining the Pre Security path.</p>

<h2>Learning Objectives</h2>
<p></p>By the time you finish this room, you will have learned about the following:
<ol type="1. ">
  <li>ISO OSI network model</li>
  <li>IP addresses, subnets, and routing</li>
  <li>TCP, UDP, and port numbers</li>
  <li>How to connect to an open TCP port from the command line</li>
</ol></p>

> 1.1 - <em>Get your notepad ready, and let’s begin.</em><br>
>> <strong><code>No answer needed</code></strong><br>
<p><br></p>

<h2>Task 2 - OSI Model</h2>

<p>Before we start, we should note that the OSI model might initially seem complicated. Don’t worry if you encounter cryptic acronyms, as we provide examples of the OSI model layers. We assure you that by the time you finish this module, this task will feel like a piece of cake.<br><br>

The OSI (Open Systems Interconnection) model is a conceptual model developed by the International Organization for Standardization (ISO) that describes how communications should occur in a computer network. In other words, the OSI model defines a framework for computer network communications. Although this model is theoretical, it is vital to learn and understand as it helps grasp networking concepts on a deeper level. The OSI model is composed of seven layers:</p>
<h3>Learning Objectives</h3>
<ol type="1. ">
  <li>Physical Layer</li>
  <li>Data Link Layer</li>
  <li>Network Layer</li>
  <li>Transport Layer</li>
  <li>Session Layer</li>
  <li>Presentation Layer</li>
  <li>Application Layer</li>
</ol></p>

<p>The numbering starts with the physical layer being layer 1, while the top layer, the application layer, is layer 7. To help you remember the layers from bottom to top, you can use a mnemonic such as “Please Do Not Throw Spinach Pizza Away.” You can check the Internet for other easy-to-remember acronyms if this helps you memorise them. Remembering the OSI model layers with their layer numbers is important; otherwise, you will struggle to understand terms such as “layer 3 switch” or “layer 7 firewall.”</p>

![image](https://github.com/user-attachments/assets/fcf444e2-4e46-4b3b-b8ad-0cc011eb623d)

<p><br></p>


<table border="10">
	<col style="width:10%">
	<col style="width:30%">
        <col style="width:45%">
	<thead>
	<tr height="80px">
		<th><strong>Number</strong></th>
		<td>Name</td>
		<td>Description</td>
	</tr>
	</thead>
	<tbody>
	<tr height="60px">
		<th>7</th>
		<td>$\LARGE\color{orange}{\textsf{Application}}$</td>
		<td><p>The application layer provides network services directly to end-user applications. Your web browser would use the HTTP protocol to request a file, submit a form, or upload a file.<br>

The application layer is the top layer, and you might have encountered many of its protocols as you use different applications. Examples of Layer 7 protocols are HTTP, FTP, DNS, POP3, SMTP, and IMAP. Don’t worry if you are not familiar with all of them.</p></td>
	</tr>
	<tr height="60px">
		<th>6</th>
		<td>Presentation</td>
		<td><p>The presentation layer ensures the data is delivered in a form the application layer can understand. Layer 6 handles data encoding, compression, and encryption. An example of encoding is character encoding, such as ASCII or Unicode.<br>

Various standards are used at the presentation layer. Consider the scenario where we want to send an image via email. First, we use JPEG, GIF, and PNG to save our images; furthermore, although hidden from the user by the email client, we use MIME (Multipurpose Internet Mail Extensions) to attach the file to our email. MIME encodes a binary file using 7-bit ASCII characters.</p></td>
	</tr>
	<tr height="60px">
		<th>5</th>
		<td>Session</td>
		<td><p>The session layer is responsible for establishing, maintaining, and synchronising communication between applications running on different hosts. Establishing a session means initiating communication between applications and negotiating the necessary parameters for the session. Data synchronisation ensures that data is transmitted in the correct order and provides mechanisms for recovery in case of transmission failures.<br>

Examples of the session layer are Network File System (NFS) and Remote Procedure Call (RPC).</p></td>
	</tr>
	<tr height="60px">
		<th>4</th>
		<td>Transport</td>
		<td><p>Layer 4, the transport layer, enables end-to-end communication between running applications on different hosts. Your web browser is connected to the TryHackMe web server over the transport layer, which can support various functions like flow control, segmentation, and error correction.<br>

Examples of layer 4 are Transmission Control Protocol (TCP) and User Datagram Protocol (UDP).</p></td>
	</tr>
	<tr height="60px">
		<th>3</th>
		<td>Network</td>
		<td><p> The data link layer focuses on sending data between two nodes on the same network segment. The network layer, i.e., layer 3, is concerned with sending data between different networks. In more technical terms, the network layer handles logical addressing and routing, i.e., finding a path to transfer the network packets between the diverse networks.<br>

In the data link layer, we gave an example of one company office with ten computers, where the data link layer is responsible for providing a connection between them. Let’s say that this company has multiple offices distributed across various cities, countries, or even continents. The network layer is responsible for connecting the different offices together.<br>

The network below shows that computers A and B are connected, although on different networks. You can also notice two paths connecting the two computers; the network layer will route the network packets through the path it deems better.<br>
Examples of the network layer include Internet Protocol (IP), Internet Control Message Protocol (ICMP), and Virtual Private Network (VPN) protocols such as IPSec and SSL/TLS VPN.</p></td>
		</tr>
	<tr height="60px">
		<th>2</th>
		<td>Data Link</td>
		<td><p>The physical layer defines a medium to transmit our signal. The data link layer, i.e., layer 2, represents the protocol that enables data transfer between nodes on the same network segment. Let’s put it in simpler terms. The data link layer describes an agreement between the different systems on the same network segment on how to communicate. A network segment refers to a group of networked devices using a shared medium or channel for information transfer. For example, consider a company office with ten computers connected to a network switch; that’s a network segment.<br>

Examples of layer 2 include Ethernet, i.e., 802.3, and WiFi, i.e., 802.11. Ethernet and WiFi addresses are six bytes. Their address is called a MAC address, where MAC stands for Media Access Control. They are usually expressed in hexadecimal format with a colon separating each two bytes. The three leftmost bytes identify the vendor.<br>
We expect to see two MAC addresses in each frame in real network communication over Ethernet or WiFi. The packet in the screenshot below shows:<br>

- The destination data-link address (MAC address) highlighted in yellow
- The source data link address (MAC address) is highlighted in blue
- The remaining bits show the data being sent</p></td>
	</tr>
	<tr height="60px">
		<th>1</th>
		<td>Physical</td>
		<td><p>The physical layer, also referred to as layer 1, deals with the physical connection between devices; this includes the medium, such as a wire, and the definition of the binary digits 0 and 1. Data transmission can be via an electrical, optical, or wireless signal. Consequently, we need data cables or antennas, depending on our physical medium.<br><br>In addition to Ethernet cable, shown in the illustration below, and optical fibre cable, examples of the physical layer medium include the WiFi radio bands, the 2.4 GHz band, the 5 GHz band, and the 6 GHz band.</p></td>
	</tr>
	</tbody>
</table>

<h3>Summary</h3>
<p>Reading about the ISO OSI model for the first time can be intimidating; however, it becomes easier as you progress in your study of networking protocols. To help with your studies, we have summarised the ISO OSI layers in the table below.</p>

<table border="10" align="center">
	<col style="width:10%">
	<col style="width:15%">
	<col style="width:30%">
        <col style="width:45%">
	<thead>
	<tr height="80px">
		<th><strong>Number</strong></th>
		<td>Name</td>
  		<td>Main Function</td>
		<td>Example Protocols and Standards</td>
	</tr>
	</thead>
	<tbody>
	<tr height="60px">
		<th>7</th>
		<td>$\LARGE\color{orange}{\textsf{Application}}$</td>
		<td>Providing services and interfaces to applications</td>
		<td>HTTP, FTP, DNS, POP3, SMTP, IMAP</td>
	</tr>
	<tr height="60px">
		<th>6</th>
		<td>Presentation</td>
		<td>Data encoding, encryption, and compression</td>
		<td>Unicode, MIME, JPEG, PNG, MPEG</td>
	</tr>
	<tr height="60px">
		<th>5</th>
		<td>Session</td>
		<td>Establishing, maintaining, and synchronising sessions</td>
		<td>NFS, RPC</td>
	</tr>
	<tr height="60px">
		<th>4</th>
		<td>Transport</td>
		<td>End-to-end communication and data segmentation</td>
		<td>UDP, TCP</td>
	</tr>
	<tr height="60px">
		<th>3</th>
		<td>Network</td>
		<td>Logical addressing and routing between networks</td>
		<td>IP, ICMP, IPSec</td>
	</tr>
	<tr height="60px">
		<th>2</th>
		<td>Data Link</td>
		<td>Reliable data transfer between adjacent nodes</td>
		<td>Ethernet (802.3), WiFi (802.11)</td>
	</tr>
	<tr height="60px">
		<th>1</th>
		<td>Physical</td>
		<td>Physical data transmission media</td>
		<td>Electrical, optical, and wireless signals</td>
	</tr>
	</tbody>
</table>
<br>

> 2.1 - <em>Which layer is responsible for connecting one application to another?</em><br>
>> <strong><code>Layer 4</code></strong><br>
<p><br></p>

> 2.2 - <em>Which layer is responsible for routing packets to the proper network?</em><br>
>> <strong><code>Layer 3 </code></strong><br>
<p><br></p>

> 2.3 - <em>In the OSI model, which layer is responsible for encoding the application data?</em><br>
>> <strong><code>Layer 6</code></strong><br>
<p><br></p>

> 2.4 - <em>Which layer is responsible for transferring data between hosts on the same network segment?</em><br>
>> <strong><code>Layer 2 </code></strong><br>
<p><br></p>

<h2>Task 3 - TCP/IP Model</h2>
<br>

> 3.1 - <em>To which layer does HTTP belong in the TCP/IP model?</em><br>
>> <strong><code>Application Layer</code></strong><br>
<p><br></p>

> 3.2 - <em>How many layers of the OSI model does the application layer in the TCP/IP model cover?</em><br>
>> <strong><code>3</code></strong><br>
<p><br></p>

<h2>Task 4 - IP Addresses and Subnets</h2>
<br>

> 4.1 - <em>Which of the following IP addresses is not a private IP address?</em><br>
> - 192.168.250.125
> - 10..20.141.132
> - 49.69.147.197
> - 172.23.182.251
>> <strong><code>49.69.147.197</code></strong><br>
<p><br></p>

> 4.2 - <em>Which of the following IP addresses is not a valid IP address?</em><br>
> - 192.168.250.15
> - 192.168.254.17
> - 192.168.305.19
> - 192.168.199.13
>> <strong><code>192.168.305.19</code></strong><br>
<p><br></p>

<h2>Task 5 - UDP and TCP</h2>
<br>

> 5.1 - <em>Which protocol requires a three-way handshake?</em><br>
>> <strong><code>TCP</code></strong><br>
<p><br></p>

> 5.2 - <em>What is the approximate number of port numbers (in thousands)?</em><br>
>> <strong><code>65</code></strong><br>
<p><br></p>

<h2>Task 6 - Encapsulation</h2>
<br>

> 6.1 - <em>On a WiFi, within what will an IP packet be encapsulated?</em><br>
>> <strong>Frame</strong><br>
<p><br></p>

> 6.2 - <em>What do you call the UDP data unit that encapsulates the application data?</em><br>
>> <strong>Datagram</strong><br>
<p><br></p>

> 6.3 - <em>What do you call the data unit that encapsulates the application data sent over TCP?</em><br>
>> <strong>Segment</strong><br>
<p><br></p>

<h2>Task 7 - Telnet</h2>
<br>

> 7.1 - <em>Use telnet to connect to the web server on MACHINE_IP. What is the name and version of the HTTP server?</em><br>
>> <strong><code>lighttpd/1.4.63</code></strong><br>
<p></p>

<pre><code>$ telnet 10.10.239.204 80
Trying 10.10.239.204...
Connected to 10.10.239.204.
Escape character is '^]'.
GET / HTTP/1.1

HTTP/1.1 400 Bad Request
Content-Type: text/html
Content-Length: 345
Connection: close
Date: Thu, 24 Oct 2024 00:44:20 GMT
Server: lighttpd/1.4.63
...
</code></pre><br>

> 7.2 - <em>What flag did you get when you viewed the page?</em><br>
>> <strong><code>THM{TELNET_MASTER}</code></strong><br>
<p></p>

![image](https://github.com/user-attachments/assets/c9971021-2130-43ac-9374-c115c88246c9)


<h2>Task 8 - Conclusion</h2>
<br>

> 8.1 - <em>Please note and remember all the concepts, network layers, and protocols explained in this room.</em><br>
>> <strong><code>No answer needed</code></strong><br>
<p><br></p>

<h2>Room Complete</h2>

![image](https://github.com/user-attachments/assets/9d09eef5-b70b-44ca-a114-736afa9684e1)




