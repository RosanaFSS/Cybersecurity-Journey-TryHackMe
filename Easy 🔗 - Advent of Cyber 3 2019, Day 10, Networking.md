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

<h2>Check out Philip Wylie's walkthrough video for day 10 here</h2>h2>

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
. Secure Shell (SSH) for secure remote login</p>





