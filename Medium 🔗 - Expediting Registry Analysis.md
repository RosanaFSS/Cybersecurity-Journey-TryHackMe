<p align="center">December 17, 2024</p>
<p align="center">Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{225}}$$-day-streak in  <a href="https://tryhackme.com/r/hacktivities">TryHackMe</a>.</p>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{ Expediting Registry Analysis }}$$ </h1>
<p align="center">This room explores different tools used to expedite analysis of registry data during investigation.</p>
<p align="center">Access this 🆓 TryHackMe CTF Room clicking <a href="https://tryhackme.com/r/room/expregistryforensics">Expediting Registry Analysis</a>.</p>
<p align="center">
  <img height="150px" hspace="20" src="https://github.com/user-attachments/assets/0a679284-0798-4f74-9098-92a98c6336e0"><br>
  <img width="800px" src="https://github.com/user-attachments/assets/5e6d554d-52b4-4702-bb04-1e3c78f25f6e">
</p>

<p align="center">Summary</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [1. Introduction](#1) &nbsp;&nbsp;&nbsp;&nbsp;▪️&nbsp;&nbsp;&nbsp;&nbsp; [2. Data Acquisition Considerations and the FTK Imager](#2) &nbsp;&nbsp;&nbsp;&nbsp;▪️&nbsp;&nbsp;&nbsp;&nbsp; [3. Data Acquisition Using KAPE](#3)

<br>
<br>
<br>
<h2 align="center">Task 1. Introduction<a id='1'></a></h2>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> 1.1. <em>I have completed the prerequisites for the room.</em><br><a id='1.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>

<h2 align="center">Task 2. Data Acquisition Considerations and the FTK Imager<a id='2'></a></h2>
<p>To start the investigation, Anna needs to acquire registry data. There are several ways to acquire registry data from a system. We will discuss the most common ones in this room. But before that, let's understand the difference between live and cold collections.</p>

<h3>Live Acquisition</h3>
<p>ive acquisition is done on a running system. In a live acquisition, the Windows OS is already loaded into the memory, and the configurations are all in the memory. In a live system, the registry hives files are locked and cannot be copied without special tools. However, in a live system, since the configuration is already loaded, we don't have to analyse the registry to identify the active configuration of the system (e.g., the CurrentControlSet key is already loaded, and we know which configuration is in use). However, the problem with acquiring registry data from a live system is that whatever tool we use will leave a trace and might overwrite some critical data points. For example, if we use FTK Imager to collect live data, we will have to execute FTK imager, adding an entry to all the registry keys that keep track of program execution. The most common reason a live acquisition is done is to save time. Taking a full disk image and then extracting data from that takes a lot of time and can be impractical when dealing with an outbreak or when quick results are required. It is often better to take a live collection when time is of the essence.</p>
<br>
<h3>Cold Acquisition</h3>
<p>A cold data acquisition is done when the system is not running. In such an acquisition, a full disk image is first taken of the system by putting the system's hard disk drive in a write blocker. The system is shut down at this point. This disk image is then hashed and copied, and all the analysis is done on a copy of the original disk image. This is done to maintain the integrity of the original evidence so that, if need be, it can be proven that the evidence was not tampered with and the results are reproducible. We first mount the disk image using image mounting software to analyse the registry from a cold acquisition and extract the data from the mounted image. Some tools like FTK Imager and Autopsy can perform both steps simultaneously, and we don't need a separate image mounting software to view the data. Though a cold acquisition takes a lot of time, as we can guess from the number of steps involved in this process, it is to be noted that a cold acquisition makes the most negligible impact on the system under analysis, as it can be done from a write-blocked disk image instead of an actual running system. A cold acquisition is more suitable if we have to ensure the integrity of the data for purposes such as going to court. </p>
<br>
<h3>Data Acquisition Using FTK Imager</h3>
<p>FTK Imager is a tool primarily used to take disk and memory images of a live system. However, it can also be used to read acquired disk images. Acquiring a full disk or memory image is out of the scope of this room. However, we will learn to acquire registry data using FTK Imager in this room.<br>

First, we must load the disk image from which we want to extract the data. In the attached VM, we can see the shortcut file for FTK Imager on the Desktop. After starting, we can <code>Add Evidence Item</code> by going to <code>File > Add Evidence Item</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/5493cc7a-b7cd-4c11-9a46-4f037173ddb4)

<br>

![image](https://github.com/user-attachments/assets/72d1b9c5-f9fd-4061-a22b-327725398420)

<br>

![image](https://github.com/user-attachments/assets/48d2dabf-a481-4059-a0f2-d4956a34e940)

<br>
<p>In a live system, this is generally the C drive of the system (or the drive where the OS is installed). We can do that by selecting <code>Logical Drive</code> in the Add Evidence Item menu. </p>

![image](https://github.com/user-attachments/assets/dc7a1764-c335-495c-96aa-e699f850bdaa)

<br>
<p>We can then select the OS drive from a list of available drives.</p>

![image](https://github.com/user-attachments/assets/ef8e8cdc-eea8-4502-9a3c-aa3840ef46ad)

<br>

![image](https://github.com/user-attachments/assets/7b8d197b-d806-4e5e-8124-511cde5d7105)

<br>
<p>In a cold system, instead of the C drive of the current system, we have to navigate to the path of the target system and select the disk image from which we want to extract the data. We do that by selecting <code>Image File</code> in the Add Evidence Item menu.</p>

![image](https://github.com/user-attachments/assets/a8cc8139-c40f-4b0d-9677-dfcf726c0f69)

<p>We can then browse where we saved the image file and add it to FTK Imager. This is the only difference between exporting files from a live disk or a cold disk image. Once we have added the evidence into FTK Imager, the rest of the process is the same.</p>

![image](https://github.com/user-attachments/assets/03cfcd97-9292-40e3-a491-afbf31f170fe)

<br>
<p>In a live system, we can collect the registry data by clicking the <code>Obtain Protected Files</code> option in FTK Imager. Remember that the registry files are locked and cannot be copied easily in a live system. Although we will not use this option now, it can help us get those locked and protected files. We could export these files to a location of our choice. </p>

![image](https://github.com/user-attachments/assets/ba735831-76b3-4bd2-a97b-28f3993f7fcf)


<br>
<p>However, the problem with the above method is that it does not acquire all the registry hives. For example, it does not copy the Amcache hive, which will make us leave out important information about program execution. As we can see in the bottom-left of the above screenshot, this option exports files to facilitate a SAM attack, which targets the SAM registry hive to exploit user credentials. 

A better way to export registry keys using FTK Imager is by navigating to the desired location where the hives are located and exporting the required files. We can do this by manually expanding the disk image and navigating to the directories. This method can be used for both live and cold acquisitions. Once we reach the desired location, we must select the files we want to export. We can then click the <code>Export Files</code> option to export the selected files to a location of our choice.</p>

![image](https://github.com/user-attachments/assets/390e7568-abd0-49f4-ab3b-a22134df675a)

<br>
<p>In the above screenshot, we are copying the registry hives, the transaction logs, and the backup files that contain the changes that are still not written in the registry hives but have been made already (we learned about these in the Windows Forensics 1 room). These can contain essential pieces of the information puzzle we want to extract, which must be utilised when analysing the registry data.<br>

In the scenario from Task 1, we outlined the information that Anna wants to extract from the system. As we learned in Windows Forensics 1, this information is generally present in the SAM, SYSTEM, and SOFTWARE registry hives in the <code>C:\Windows\System32\config</code> directory. Anna can extract those hives using FTK Imager to achieve her goal. To ensure the completeness of the information, she will also need to extract the transaction logs. She can do that using the FTK Imager, which is present on the Desktop in the attached VM.<br>

The most significant advantage of using FTK Imager to extract data is the specificity and granularity of the process. We can pick and choose the exact files we want to extract. However, this process generally requires precise knowledge and time to execute. Using tools to automate this process might be better in some scenarios, as we will learn in the coming tasks.<br>

Can you help Anna extract the registry data from the VM attached to Task 1, as shown in this task?</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 2.1. <em>I have collected registry data from the attached VM, as shown in this task.</em><br><a id='2.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>

> 2.2. <em>When we take a forensic data collection from the disk image of a system, what type of acquisition is it called?</em><br><a id='2.2'></a>
>> <code><strong>cold acquisition</strong></code>

<br>

> 2.3. <em>Is speed one of the advantages of collecting registry data from FTK Imager? Y or N?</em><br><a id='2.3'></a>
>> <code><strong>N</strong></code>

<br>
<h2 align="center">Task 3. Data Acquisition Using KAPE<a id='3'></a></h2>
<p>Anna could use FTK Imager to extract registry data, but it is a manual way of data acquisition. Ideally, she would like something that can remove the human element from the process so there are fewer chances of making a mistake and is easier to delegate to one of her team members. Usually, the advantage of an automatic process is speed and efficiency, but a manual way also has its benefits, and granularity and specificity are such. In this task, we will see how to automate the data acquisition process using KAPE. </p>

<br>
<h3>Data Acquisition Using KAPE</h3>
<p>We learned about KAPE in a dedicated room. KAPE (Kroll Artifact Parser and Extractor) is a tool that helps us collect and process triage data quickly from a system. KAPE is generally used on live systems. However, it can also be used on a disk image by mounting it and providing the target location as the mounted disk image drive. We can use any image mounting software to mount the disk image, and the rest of the process remains the same. FTK Imager can also mount images, but running KAPE while FTK Imager is running might cause issues, and we have to select the <code>Ignore FTK warning</code> checkbox to execute KAPE in that scenario.<br>

First, we can start with the <code>gkape.exe</code> executable, which we can find in the KAPE folder in the attached VM. It will open the KAPE GUI. This will look something like this:</p>

<br>

![image](https://github.com/user-attachments/assets/7c65151d-f598-4c97-bdce-676a877128e1)

<br>
<p>Since we are to collect data, we will select the <code>Use Target Options</code> checkmark. This will make the left side of the KAPE GUI available for us to modify.</p>

<br>





<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> 3.1. <em>I have collected the registry data from the attached system using KAPE, as shown in this task..</em><br><a id='1.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>

> 3.2. <em>What will be the contents of a _kape.cli file if we want to collect data from the C drive and save it to the D drive using the target RegistryHives?.</em><br><a id='3.2'></a>
>> <code><strong>--tsource C: --tdest D:\ --target RegistryHives</strong></code>




<br>

![December 17, 2024  - TryHackMe - 225-day-streak,  Expediting Registry Analysis - Room Completed White Background](https://github.com/user-attachments/assets/4f5fd570-bb62-4aaf-ba72-7ff55e466f88)

<br>

![December 17, 2024  - TryHackMe - 225-day-streak,  Expediting Registry Analysis - Header and Tasks](https://github.com/user-attachments/assets/ec10a85f-5357-44c0-a269-8042b1808d3d)

