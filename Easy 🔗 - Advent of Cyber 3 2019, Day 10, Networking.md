<p align="center">March 20, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{318}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
  <img width="160px" src="https://github.com/user-attachments/assets/67d84414-d9e4-4068-be03-f10e812305dd"></p>


<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{[ Day 10 ] - Advent of Cyber 3 (2021)}}$$
</h1>
<p align="center">Get started with Cyber Security in 25 Days - Learn the basics by doing a new, beginner friendly security challenge every day leading up to Christmas. It is classified as an easy-level walkthrough, and you can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed. <a href="https://tryhackme.com/room/adventofcyber3">Advent of Cyber 3 (2021)</a>.</p>
                                                              
<p align="center"> <img width="900px" src=""> </p>

<br>

<p align="center"> <img width="900px" src=""> </p>

<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{Offensive Is the Best Defence | Networking}}$$
</h1>

<br>

<p>McSkidy is trying to discover how the attackers managed to penetrate the network and cause damage to the Best Festival Company’s infrastructure. She decided to start doing a security assessment of her systems to discover how Grinch Enterprises managed to cause this damage. She started by conducting a security assessment of her systems to discover how Grinch Enterprises managed to cause this damage and wonders what service they exploited.<br>

Before McSkidy starts firing up Nmap, let’s review some keywords related to her task. If you are familiar with the terms IP address, protocol, server, and port number, feel free to skip the following three sections and start directly with the Nmap section.</p>

<h2>Check out Philip Wylie's walkthrough video for day 10 here</h2>

<h3>IP Addresses</h3>
<p>Every computer (host) that connects to a network needs to have a logical address. For instance, a host can be any system with network access, such as a laptop, a smartphone, and a Raspberry Pi. We refer to this address as logical because it's assigned by software and could change over time, for example, when the host connects to a new network. The logical address, in this case, is the IP address.<br>

IP stands for Internet Protocol. To keep things simple, we will consider Internet Protocol version 4 (IPv4). An IPv4 address is made up of 4 decimal numbers. The range for each number is from 0 to 255. Example IPv4 addresses are:<br>

. 192.168.0.10<br>
. 172.16.0.100<br>
. 10.10.11.12<br>
. 1.1.1.1<br>


The first 3 IP addresses in the list above are private, meaning that they can only be accessed from the private network they belong to. The last IP address, 1.1.1.1, is a public IP address that can be accessed by the whole Internet and belongs to Cloudflare.<br>

Some IP addresses serve a special purpose. For example, 127.0.0.1 is often referred to as the 'loopback address' or 'localhost'. By default, any packet or traffic destined to this address won't leave the host.<br>

On Microsoft Windows, one way to find your IP address is by running ipconfig in the command prompt or PowerShell. On Linux and macOS, you can find your IP address by executing ip address show on the terminal. Note that ip will accept abbreviations of arguments such as ip addr show or even ip a s.</p>

![image](https://github.com/user-attachments/assets/377af30c-c9fe-482c-9087-6666bc5d7608)

<p>The terminal output above shows that this Linux system has a wireless adaptor with the IP address 192.168.0.202.<br>

If you want to learn more about computer networking, we recommend the Network Fundamentals module.</p>

<h3>Protocols and Servers</h3>
<p>Let’s say that we want to set up a website and we've made it accessible to the whole Internet. In order to make our website accessible to the users on the Internet, a public IP address is required. A web server is a program that listens for incoming connections, usually from web browsers, and responds to their requests.<br>

A server usually refers to a computer system that provides services to other clients, i.e. other computers, over a network. Example services include serving webpages, delivering email, and facilitating video conferencing.<br>

For the client computer to communicate with the server, a specific protocol must be followed. Consider the following analogy. You want to order an espresso from a coffee shop for takeaway. The protocol to get an espresso might go as follow:
. Customer: Hello<br>
. Barista: Hello<br>:
. Customer: I want one espresso, please<br>
. Barista: That would be £3<br>
. Customer: Here you are, £3<br>
. Barista: Thank you. Your espresso is ready.<br>
. Customer: Thank you.</p>

![image](https://github.com/user-attachments/assets/550899e4-484d-4a6e-978e-fefffa2b8542)

<p>Since I follow this “protocol”, other customers might follow a slightly different “protocol” based on the coffee shop and the country’s culture. Some might skip the “hello” at the beginning or drop the “thank you” at the end. In the human world, this would still work; however, for computers, we need to adopt a strict protocol that both clients and servers need to adhere to. This is why we have standard protocols for computers.<br>

To name a few, these are some example TCP/IP protocols:<br>

. Hypertext Transfer Protocol (HTTP) for serving webpages<br>
. Domain Name System (DNS) for resolving hostnames to IP addresses<br>
. Post Office Protocol version 3 (POP3) for delivering email<br>
. Simple Mail Transfer Protocol (SMTP) for sending email<br>
. Telnet for remote login<br>
. Secure Shell (SSH) for secure remote login<br>

Each of these protocols are defined in detail in a Request for Comment (RFC) document. If you want to know more about these protocols, we suggest joining the Protocols and Servers room.</p>

<h3>Ports</h3>h3>
On a host, multiple processes (programs) can be accessing the network at the same time. These processes can use the network simultaneously. For the host to tell which process receives which packet, we need to use port numbers. To better understand the concept of IP addresses and port numbers, let’s consider the following analogy.<br>

Let’s imagine TryHackMe’s company in London, and let’s imagine there are 100 offices for 100 content engineers there. The company address is like a public IP address. With the company address, the mailman (analogy for a router) knows how to reach the company and deliver mail packages. The port number is like the office number within the company. The mailman can deliver to the company address and hand it to the receptionist; however, a TryHackMe employee will deliver the package to the internal office.<br>

When multiple processes are using the network or Internet simultaneously, each process can be recognized by the port number it is using. In public servers, default port numbers are used by different protocols so that clients don’t need to guess. The table below shows some of the common protocols and the port numbers they use by default.</p>


![image](https://github.com/user-attachments/assets/aabd918b-cd2f-43da-8e47-4f18d802d550)


<p>onsider the figure below. IP packets coming to the server with the IP address 10.10.13.13 will be delivered to the running process based on the destination port number.<br>

. For packets of type TCP with port number 22, the destination process is the SSH server.<br>
. For packets of type TCP with port number 80, the destination process is the HTTP server.<br>
. For packets of type UDP (or TCP) with port number 53, the destination process is the DNS server.</p>

![image](https://github.com/user-attachments/assets/66b4a7f4-4a10-4fa3-a0db-b2854fef75a8)

<p>We will not cover TCP and UDP in detail in this task. All you need to know for now is that these two protocols live on top of the IP protocol and connect processes running on different hosts. Moreover, TCP requires a three-way handshake for a connection to be established, while UDP does not.</p>

<h3>Nmap</h3>
<p>McSkidy wants to discover what the attacker learned about her hosts and servers. She starts the AttackBox and starts the attached Virtual Machine (VM), and waits for both to fully load.<br>

She wants to check which services she has installed on the VM. On the AttackBox, she opens a terminal and rushes to run an Nmap scan against the VM. McSkidy can run a very basic network port scan using the command nmap -sT MACHINE_IP or nmap -sS MACHINE_IP. By default, Nmap checks the 1000 most common TCP ports.<br>
. TCP Connect Scan: To run this type of scan, the -sT option is required. Nmap will attempt to complete the three-way handshake in order to establish a connection with each port scanned.<br>
. TCP SYN Scan: You can select this scan with the -sS option, and Nmap will not make a complete connection if the port is open. Technically speaking, Nmap does not complete a TCP three-way handshake.<br>
To better understand the difference between -sT and -sS, we can use the analogy of knocking on a door. The TCP connect scan (-sT) is like knocking on a door, waiting for someone to open it, greeting each other, then excusing yourself to leave. The TCP SYN scan (-sS) resembles knocking, and once someone answers, you pretend that it was not you that knocked and walk away innocently. The latter will make it more difficult for the other party to remember you.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>


> 1.1. <em>Help McSkidy and run <code>nmap -sT MACHINE_IP</code>. How many ports are open between 1 and 100?</em><a id='1.1'></a>
>> <code><strong>_____</strong></code><br><br>

```bash
:~/Day10# nmap -sT Target_IP
```

![image](https://github.com/user-attachments/assets/42b91c24-8afe-4d35-951c-bbb4a71c57e6)


<br>

> 1.2. <em>What is the smallest port number that is open?</em><a id='1.2'></a>
>> <code><strong>22</strong></code><br><br>

<p>Discovered the answer in 1.1.</p>

<br>

> 1.3. <em>What is the service related to the highest port number you found in the first question?</em><a id='1.3'></a>
>> <code><strong>http</strong></code><br><br>

<p>I thought it was necessary to use namp to scan all ports. By doing this I discovered that port 20212 is open.<br>
But the correct answer is http relative to port 80.</p>

```bash
:~/Day10# nmap -sT -p- Target_IP
```

![image](https://github.com/user-attachments/assets/227579f9-26e5-4df3-9eed-70c590fad22f)


<br>

> 1.4. <em>Now run nmap -sS MACHINE_IP. Did you get the same results? (Y/N)</em><a id='1.4'></a>
>> <code><strong>Y</strong></code><br><br>

```bash
:~/Day10# nmap -sS Target_IP
```


![image](https://github.com/user-attachments/assets/02ca4f53-88a1-4dd8-bd5c-7763c9eaece9)


<br>

> 1.5. <em>If you want Nmap to detect the version info of the services installed, you can use nmap -sV MACHINE_IP. What is the version number of the web server?</em><a id='1.5'></a>
>> <code><strong>Apache httpd 2.4.49</strong></code><br><br>

```bash
:~/Day10# nmap -sV Target_IP
```

![image](https://github.com/user-attachments/assets/ede60193-b65a-495d-ab58-0d2633a4e1f2)

<br>


> 1.6. <em>By checking the vulnerabilities related to the installed web server, you learn that there is a critical vulnerability that allows path traversal and remote code execution. Now you can tell McSkidy that Grinch Enterprises used this vulnerability. What is the CVE number of the vulnerability that was solved in version 2.4.51?</em><br> Hint : 2.4.50 provided an incomplete fix for CVE-2021-41773.<a id='1.6'></a>
>> <code><strong>_____</strong></code><br><br>

<p>Googled <code>"Apache" AND "CVE-2021-41773" AND "fix"</code> .<br>
Discovered the following...</p>

![image](https://github.com/user-attachments/assets/b332bfc7-0c6f-4975-a460-59d8b0d8c83e)


<p>Accessed it here <a href="https://httpd.apache.org/security/vulnerabilities_24.html">here</a></p>

![image](https://github.com/user-attachments/assets/7cb4f236-5a05-4146-b0b4-74244217e469)


<br>


> 1.7. <em>You are putting the pieces together and have a good idea of how your web server was exploited. McSkidy is suspicious that the attacker might have installed a backdoor. She asks you to check if there is some service listening on an uncommon port, i.e. outside the 1000 common ports that Nmap scans by default. She explains that adding -p1-65535 or -p- will scan all 65,535 TCP ports instead of only scanning the 1000 most common ports. What is the port number that appeared in the results now?</em><br> Hint : If the scan takes more than a few minutes, consider using Nmap with the options -sT -p20000-21000 -T4 (where -p20000-21000 limits the scan to ports between 20,000 and 21,000, while T4 makes Nmap aggressive and increases the speed).<a id='1.7'></a>
>> <code><strong>_____</strong></code><br><br>

<br>


> 1.8. <em>What is the name of the program listening on the newly discovered port?</em><br> Hint : Using Nmap with the option -sV should reveal the name under VERSION for the specified port(s). You may add something like -p20000-21000 to limit the range of ports you want to check.<a id='1.8'></a>
>> <code><strong>_____</strong></code><br><br>

<br>


> 1.9. <em>If you would like to learn more about the topics covered in today’s tasks, we recommend checking out the Network Security module.</em><a id='1.9'></a>
>> <code><strong>No answer needed</strong></code><br><br>

<br>












