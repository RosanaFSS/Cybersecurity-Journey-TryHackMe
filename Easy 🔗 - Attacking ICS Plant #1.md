<h1 align="center">Attacking ICS Plant #1</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/5f6218cd-69b3-4aa6-a51f-b1e035c69ec4"><br>
2025, September 10<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>492</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Learn how to discover and attack ICS plants using modbus protocol (Modicon / Schneider Electric).</em>.<br>
Access it <a href="https://tryhackme.com/room/attackingics1"</a>here.<br>
<img width="1200px" src=""></p>


<h2>Task 1 . Introduction</h2>

<p><em>Answer the question below</em></p>

<p>1.1. No answer needed<br>
<code>No answer needed</code></p>

<h2>Introduction to OT/ICS</h2>
<p>[ Download Task Files ]</p>
<p>Modbus is an industrial protocol developed by Modicon, acquired by Schneider Electric. Modbus is widely used to connect industrial devices; protocol specification is available and royalty-free.<br>

Modbus protocol is a master/slave protocol: the master reads and writes slaves' registers.<br>

Modbus RTU is usually used via RS-485 (serial network): one master is present with one or more slaves. Each slave has an unique 8-bit address.<br>

Modbus data is used to read and write "registers" which are 16-bit long. The most common register is called "holding register" which is readable and writable; registry type "input register" is readable only. The registers "coil" and "discrete input" are 1-bit long: coils are readable and writable, discrete inputs are readable only.<br>

Modbus register types:<br>

- Discrete Input (Status Input): 1bit, RO<br>
- Coil (Discrete Output): 1bit, R/W<br>
- Input Register: 16bit, RO<br>
- Holding Register: 16bit R/W<br><br>

Most commonly Modbus function:</p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/0b7972f6-fa6b-4866-bd12-ab7e3c1b722b"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Modbus TCP encapsulates Modbus RTU request and response data packets in a TCP packet transmitted over standard Ethernet networks. The TCP Modbus standard port is 502.<br>

For more information see  <a href="https://www.csimn.com/CSI_pages/Modbus101.html">Modbus 101 - Introduction to Modbus</a>.<br>

Before starting, download the attached script package and install the Modbus TCP library for Python with the following command:<br>

<code>pip3 install pymodbus==1.5.2</code></p>

<p><em>Answer the question below</em></p>

<p>2.1. Which is the function used to read holding registers in pymodbus library? Hint: <em>See discovery.py</em><br>
<code>read_holding_registers</code></p>

<p>

- https://pymodbus.readthedocs.io/en/latest/source/client.html</p>

<img width="1316" height="290" alt="image" src="https://github.com/user-attachments/assets/cbe0bfca-ea41-43ba-be58-b60f9714afb8" />

<br>
<br>

<img width="1287" height="435" alt="image" src="https://github.com/user-attachments/assets/dc13c86d-e151-4ced-a3ea-477cd9721f52" />

<br>
<br>
<p>2.2. Which is the function used to write holding registers in pymodbus library? Hint: <em>See any attack*.py files.</em><br>
<code>write_register</code></p>

<img width="1315" height="371" alt="image" src="https://github.com/user-attachments/assets/4dfd5dfc-fc42-48f0-a731-af0edd573f3e" />

<br>
<br>
<h2>Introduction to Modbus protocol</h2>


<h2>Discovery</h2>


<h2>Platy to learn</h2>


<h2>Attack</h2>
