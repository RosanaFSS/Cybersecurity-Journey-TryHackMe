<h3 align="center">Advent of Cyber 2025 &nbsp;&nbsp; ·  &nbsp;&nbsp; Day 14 &nbsp;&nbsp; ·  &nbsp;&nbsp; Containers - DoorDasher's Demise</h3>
<p align="center">2025, December 20  &nbsp; ·  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure in <a href="https://tryhackme.com">TryHackMe</a>.<br>Continue your Advent of Cyber journey and learn about container security. &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/container-security-aoc2025-z0x3v6n9m2">here</a>.<br><img width="80px" src="https://github.com/user-attachments/assets/95aa42fd-4fa1-434a-9578-defd0f0a46ef"<br><br><img width="1200px" src="https://github.com/user-attachments/assets/b2de14e0-0cdd-419a-aecb-7c699765f761"></p>

<h2>Task 1 &nbsp; ·  &nbsp; Introduction</h2>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/0049020f-9444-4e3b-81c2-1ccf9897def0"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>It seemed as the sun rose this morning, it had already been decided that today would be another day of chaos in Wareville. At least that’s the feeling all the folks at “DoorDasher” got. DoorDasher is Warevilles local food delivery site, a favourite of the workers in The Best Festival Company, especially on long days when they get home from work and just can’t bring themself to make dinner. We’ve all been there, I’m sure.<br>

Well, one Wareville resident was feeling particularly tired this morning and so decided to order breakfast. Only to find King Malhare and his bandit bunny battalions had seized control of yet another festive favourite. DoorDasher had been completely rebranded as Hopperoo. All of the ware’s favourite dishes had been changed as well. Reports started flooding into the DoorDasher call centre. And not just from customers. The health and safety food org was on the line too, utterly panicked. Apparently, multiple Wareville residents were choking on what turned out to be fragments of Santa’s beard. Wareville authorities were left tangled in confusion today as Hopperoo faced mounting backlash over reports of “culinary impersonation.” Customers across the region claim to have been served what appears to be authentic strands of Santa’s beard in place of traditional noodles.<br>

A spokesperson for the Health & Safety Food Bureau confirmed that several diners required “gentle untangling” and one incident involved a customer “achieving accidental facial hair synchronisation.”</p>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/2968e331-376c-4093-9d5d-e3873547f0f6"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Immediately, one of the security engineers managed to log on and make a script that would restore DoorDasher to its original state, but just before he was able to run it, Sir CarrotBaine caught wind of his attempt and locked him out of the system. All was lost, until the SOC team realised they still had access to the system via their monitoring pod, an uptime checker for the site. Your job? As a SOC team member of DoorDasher, can you escape the container and escalate your privileges so you can finish what your team started and save the site!</p>

<h3>Learning Objectives</h3>
<p>

- Learn how containers and Docker work, including images, layers, and the container engine<br>
- Explore Docker runtime concepts (sockets, daemon API) and common container escape/privilege-escalation vectors<br>
- Apply these skills to investigate image layers, escape a container, escalate privileges, and restore the DoorDasher service<br>
- DO NOT order “Santa's Beard Pasta”</p>

<h3>Connecting to the Machine</h3>
<p>Before moving forward, review the questions in the connection card shown below:</p>

<h6 align="center"><img width="400px" src="https://github.com/user-attachments/assets/425e0359-26a1-4e74-a14e-bb7426c097dd"><br><br>This image and all the theoretical content of<br> the present article is TryHackMe´s property.</h6>

<p>Start the lab by clicking the <strong>Start Machine</strong> button below. The machine will start in split view and will take about two minutes to load. In case the machine is not visible, click the <strong>Show Split View</strong> button at the top of the page. Once the machine has loaded, you should be given access to the <code>mrbombastic</code> user. You will be given commands to run on this virtual machine in the next task. Additionally, start the AttackBox by pressing <strong>Start AttackBox</strong> down below.</p>

<h3>Set up your virtual environment</h3>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting both your AttackBox (if you're not using your VPN) and Target Machines, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.</p>

<p><strong>Note</strong>: It’s recommended to open both machines in full-screen view using the small icon on the far left in the screenshot below; otherwise, you might get kicked out of the Docker container when switching tabs in split view. If you still prefer to use split view, you can switch between the target machine and the AttackBox using the bottom tabs, as shown below:</p>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/8dce91db-5333-4fac-9a71-4b86b4f73e77"><br><br>This image and all the theoretical content of<br> the present article is TryHackMe´s property.</h6>

<p><em>Answer the question below</em></p>

<p>1.1. <em>Tell me more!</em><br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 &nbsp; ·  &nbsp; Container Security</h2>
<h3>What Are Containers?</h3>
<p>To understand what a container is, we first need to understand the problem it fixes. Put plainly, modern applications can be quite complex:<br>

- <strong>Installation</strong>: Depending on the environment the application is being installed in, it’s not uncommon to run into “configuration quirks” which make the process time-consuming and frustrating.<br><br>
- <strong>Troubleshooting</strong>: When an application stops working, a lot of time can be wasted determining if it is a problem with the application itself or a problem with the environment it is running in.<br><br>
- <strong>Conflicts</strong>: Sometimes multiple versions of an application need to be run, or perhaps multiple applications which need (for example) different versions of Python to be installed. This can sometimes lead to conflicts, complicating the process further.<br><br>

If reading these problems, your brain conjured up the word “isolation” as a solution, well, you’re onto the right track. Containerisation solves these problems by packing applications, along with their dependencies, in one isolated environment. This package is known as a container. In addition to solving all the above problems, containerisation also offers further benefits. One key benefit is how lightweight they are. To understand this, we will now take a (brief) look at container architecture.</p>

<h4>Containers vs VMs</h4>
<p></p>To illustrate container architecture, let's examine another form of virtualisation: Virtual Machines. Virtual Machines, like the ones you have been booting up on this platform throughout Advent of Cyber.</p>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/ada7258b-513e-4e84-842e-6aceb1323705"><br><br>This image and all the theoretical content of<br> the present article is TryHackMe´s property.</h6>

<p>A virtual machine runs on a hypervisor (software that emulates and manages multiple operating systems on one physical host). It includes a full guest OS, making it heavier but fully isolated. Containers share the host OS kernel, isolating only applications and their dependencies, which makes them lightweight and fast to start. Virtual machines are ideal for running multiple different operating systems or legacy applications, while containers excel at deploying scalable, portable micro-services.</p>

<h4>Applications at Scale</h4>
<p>Microservices are a switch in the style of application architecture, where before it was a lot more common to deploy apps in a monolithic fashion (built as a single unit, a single code base, usually as a single executable ), more and more companies are choosing to break down their application into parts based on business function. This way, if a specific part of their application receives high traffic loads, they can scale that part without having to scale the entire application. This is where the lightweight nature of containers comes into play, making them incredibly easy to scale to meet increasing demands. They became the go-to choice for this (increasingly popular) architecture, and this is why, over the last 10 years, you have started seeing the term more and more.<br>

You may have noticed a layer labelled “Container Engine” in the diagram. A container engine is software that builds, runs, and manages containers by leveraging the host system’s OS kernel features like namespaces and cgroups. One example of a container engine is Docker, which we will examine in more detail. Docker is a popular container engine that uses Dockerfiles, simple text scripts defining app environments and dependencies, to build, package, and run applications consistently across different systems. Docker is the container engine of choice at “DoorDasher” and so is what we will be interacting with in our interactive lab.</p>

<h4>Docker</h4>
<p>Docker is an open-source platform for developers to build, deploy, and manage containers. Containers are executable units of software which package and manage the software and components to run a service. They are pretty lightweight because they isolate the application and use the host OS kernel.</p>


<h6 align="center"><img width="280px" src="https://github.com/user-attachments/assets/27e6b990-a0b5-4dd0-b117-2eb29af092a4"><br><br>This image and all the theoretical content of<br> the present article is TryHackMe´s property.</h6>

<h4>Escape Attack & Sockets</h4>
<p>A container escape is a technique that enables code running inside a container to obtain rights or execute on the host kernel (or other containers) beyond its isolated environment (escaping). For example, creating a privileged container with access to the public internet from a test container with no internet access.<br> 

Containers use a client-server setup on the host. The CLI tools act as the client, sending requests to the container daemon, which handles the actual container management and execution. The runtime exposes an API server via Unix sockets (runtime sockets) to handle CLI and daemon traffic. If an attacker can communicate with that socket from inside the container, they can exploit the runtime (this is how we would create the privileged container with internet access, as mentioned in the previous example).</p>

<h3>Challenge</h3>
<p>A container escape is a technique that enables code running inside a container to obtain rights or execute on the host kernel (or other containers) beyond its isolated environment (escaping). For example, creating a privileged container with access to the public internet from a test container with no internet access. 

Containers use a client-server setup on the host. The CLI tools act as the client, sending requests to the container daemon, which handles the actual container management and execution. The runtime exposes an API server via Unix sockets (runtime sockets) to handle CLI and daemon traffic. If an attacker can communicate with that socket from inside the container, they can exploit the runtime (this is how we would create the privileged container with internet access, as mentioned in the previous example).</p>

<h4>Access Points</h4>
<p>Now it's time to start using the machine you booted up in task 1. Let's check which services are running with Docker. Run the following command:<br>

<code>docker ps</code><br>

You should see a few services running:</p>

<h6 align="center"><img width="400px" src="https://github.com/user-attachments/assets/93a13c58-0065-4fe6-a34e-e23ad9c48b9f"><br><br>This image and all the theoretical content of<br> the present article is TryHackMe´s property.</h6>

<p>The main service runs at <code>http://MACHINE_IP:5001</code>. Explore the web application, and notice the defaced system “Hopperoo”. We know DoorDasher is a food delivery service. Let's explore <code></code>uptime-checker</code>. Sounds interesting.<br>

Run the following command to access the <code>uptime-checker</code> container:<br>

<code>docker exec -it uptime-checker sh</code><br>

After logging in, check the socket access by running: <code>ls -la /var/run/docker.sock</code><br>

The Docker documentation mentions that by default, there is a setting called “Enhanced Container Isolation” which blocks containers from mounting the Docker socket to prevent malicious access to the Docker Engine. In some cases, like when running test containers, they need Docker socket access. The socket provides a means to access containers via the API directly. Let's see if we can. Your output should be something like:</p>

<h6 align="center"><img width="400px" src="https://github.com/user-attachments/assets/c564d9fd-9f45-4671-ab09-cc56e557bdfb"><br><br>This image and all the theoretical content of<br> the present article is TryHackMe´s property.</h6>

<p>I wonder what happens if we try to run Docker commands inside the container. By running <code>docker</code> ps again, we can confirm we can perform Docker commands and interact with the API; in other words, we can perform a Docker Escape attack!<br>

Let's instead try to access the <code>deployer</code> container, which is a privileged container. Run the following command:<br>

<code>docker exec -it deployer bash</code><br>

Type <code>whoami</code> and check which user we are currently logged in as. Explore the container and find the flag.<br>

Okay, we made it! We have managed to make it to the container where the script to restore the site to its former version is! Save the day, run the recovery_script in the root directory to recover the app using sudo:<br>

<code>sudo /recovery_script.sh</code><br>

With that run, you can see for yourself by refreshing the site (<code>http://MACHINE_IP:5001</code>)! As a reward, you should be able to find a flag in the same directory as the script (<code>/</code>), which you can read using the <code>cat</code> command.</p>

<p><em>Answer the questions below</em></p>

<p>2.1. <em>What exact command lists running Docker containers?</em><br>
<code>docker ps</code></p>

<br>
<p>2.2. <em>What file is used to define the instructions for building a Docker image?</em><br>
<code>Dockerfile</code></p>

<br>
<p>2.3. <em>What's the flag?</em><br>
<code>THM{DOCKER_ESCAPE_SUCCESS}</code></p>

```bash
mrbombastic@tryhackme-2204:~$ docker ps
CONTAINER ID   IMAGE                    COMMAND                  CREATED         STATUS         PORTS                                         NAMES
1739548b8eb8   wareville-times:latest   "/docker-entrypoint.…"   6 minutes ago   Up 6 minutes   0.0.0.0:5002->80/tcp, [::]:5002->80/tcp       wareville-times
2876aa751fc0   uptime-checker:latest    "/docker-entrypoint.…"   6 minutes ago   Up 6 minutes   0.0.0.0:5003->80/tcp, [::]:5003->80/tcp       uptime-checker
d9abba6c2fbc   dasherapp:latest         "python app.py"          6 minutes ago   Up 6 minutes   0.0.0.0:5001->5000/tcp, [::]:5001->5000/tcp   dasherapp
558392b26962   deployer:latest          "tail -f /dev/null"      6 minutes ago   Up 6 minutes                                                 deployer
```

<br>
<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/2b823ded-136f-4992-97c3-904f4bed58eb"><br><br>
                   <img width="1200px" src="https://github.com/user-attachments/assets/5771d6a4-f5ac-4795-ac52-c010e59bdc43"><br><br>
                   <img width="1200px" src="https://github.com/user-attachments/assets/0b2230f5-ef10-4df8-bab4-ec2871cb3c26"><br><br>
                   <img width="1200px" src="https://github.com/user-attachments/assets/d5531e0f-cbe6-495e-a6ae-55618eb742dc"><br><br>
                   <img width="1200px" src="https://github.com/user-attachments/assets/259a3be0-f8a1-4bd9-8d26-9c94ee5102d1"><br><br>
                   <img width="1200px" src="https://github.com/user-attachments/assets/334e41b6-44a3-4818-8e69-f5fbbe9bf9fb"><br><br>
                   <img width="1200px" src="https://github.com/user-attachments/assets/849215ba-5e2d-4a77-99e0-e24ae3e5b782"><br><br>Rosana´s hands-on</h6>


<br>
<p>2.4. <em>Bonus Question: There is a secret code contained within the news site running on port <code>5002</code>code>; this code also happens to be the password for the deployer user! They should definitely change their password. Can you find it?</em><br>
<code>DeployMaster2025!</code></p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/bfbff953-1582-46ea-99a6-96888b930ec5"><br><br>Rosana´s hands-on</h6>


<br>
<p>2.5. <em>Liked the content? We have plenty more where this came from! Try our <a href="https://tryhackme.com/room/containervulnerabilitiesDG">Container Vulnerabilities</a> room.</em><br>
<code>No answer needed</code></p>

<br>
<br>
<h1 align="center">Completed</h1>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/6bf0b55f-41e0-431d-8786-3c92cce89afd"><br><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/0eabd2f5-b6ea-49d4-b151-5b6b3eed68d1"><br><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/c406163b-6c06-4400-850c-0d79e931bd21"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, December</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|20      |Medium 🔗 - Containers - DoorDasher's Demise     |4 |     100ᵗʰ  |     3ʳᵈ    |   18,059ᵗʰ   |      206ᵗʰ     |    134,864  |    1,043    |    84     |
|20      |Medium 🔗 - Forensics - Registry Furensics       |4 |     100ᵗʰ  |     3ʳᵈ    |   20,497ᵗʰ   |      239ᵗʰ     |    134,832  |    1,042    |    84     |
|20      |Medium 🔗 - Web Attack Forensics - Drone Alone   |4 |     100ᵗʰ  |     3ʳᵈ    |   21,935ᵗʰ   |      243ʳᵈ     |    134,808  |    1,041    |    84     |
|20      |Easy 🔗 - XSS - Merry XSSMas                     |4 |     100ᵗʰ  |     3ʳᵈ    |   23,069ᵗʰ   |      256ᵗʰ     |    134,792  |    1,040    |    84     |
|20      |Easy 🔗 -  Race Conditions - Toy to The World    |4 |     100ᵗʰ  |     3ʳᵈ    |   24,717ᵗʰ   |      275ᵗʰ     |    134,768  |    1,039    |    84     |
|20      |Medium 🔗 -  SOC Alert Triaging - Tinsel Triage  |4 |     100ᵗʰ  |     3ʳᵈ    |   25,202ⁿᵈ   |      286ᵗʰ     |    134,752  |    1,038    |    84     |
|19      |Medium 🔗 -  ICS/Modbus - Claus for Concern      |3 |     101ˢᵗ  |     3ʳᵈ    |   28,869ᵗʰ   |      337ᵗʰ     |    134,658  |    1,037    |    84     |
|19      |Easy 🔗 -  Passwords - A Cracking Christmas      |3 |     101ˢᵗ  |     3ʳᵈ    |   29,583ʳᵈ   |      340ᵗʰ     |    134,642  |    1,036    |    84     |
|18      |Easy 🔗 -  Prompt Injection - Sched-yule conflict|2 |     101ˢᵗ  |     3ʳᵈ    |   30,518ᵗʰ   |      353ʳᵈ     |    134,626  |    1,035    |    84     |
|18      |Medium 🔗 -  Obfuscation - The Egg Shell File    |2 |     101ˢᵗ  |     3ʳᵈ    |   30,967ᵗʰ   |      358ᵗʰ     |    134,618  |    1,034    |    84     |
|17      |Medium 🔗 - CyberChef - Hoperation Save McSkidy  |1 |     101ˢᵗ  |     3ʳᵈ    |   32,378ᵗʰ   |      374ᵗʰ     |    134,602  |    1,033    |    84     |
|7       |Medium 🔗 - Malware Analysis - Egg-xecutable     |2 |      95ᵗʰ  |     3ʳᵈ    |   11,604ᵗʰ   |      145ᵗʰ     |    134,544  |    1,034    |    84     |
|7       |Easy 🔗 - Network Discovery - Scan-ta Clause     |2 |      95ᵗʰ  |     3ʳᵈ    |   18,575ᵗʰ   |      208ᵗʰ     |    134,522  |    1,033    |    84     |
|7       |Easy 🔗 - React2Shell: CVE-2025-55182            |2 |      95ᵗʰ  |     3ʳᵈ    |   28,593ʳᵈ   |      326ᵗʰ     |    134,474  |    1,032    |    81     |
|6       |Medium 🔗 - IDOR - Santa´s Little IDOR           |1 |      95ᵗʰ  |     3ʳᵈ    |   27,309ᵗʰ   |      328ᵗʰ     |    134,450  |    1,031    |    81     |
|6       |Easy 🔗 - AI in Security - old sAInt nick        |1 |      95ᵗʰ  |     3ʳᵈ    |   41,626ᵗʰ   |      526ᵗʰ     |    134,426  |    1,030    |    81     |
|6       |Medium 🔗 - Splunk Basics - Did you SIEM?        |1 |      95ᵗʰ  |     3ʳᵈ    |   44,647ᵗʰ   |      560ᵗʰ     |    134,410  |    1,029    |    81     |
|6       |Easy 🔗 - Phishing - Merry Clickmas              |1 |      96ᵗʰ  |     3ʳᵈ    |   55,824ᵗʰ   |      674ᵗʰ     |    134,370  |    1,028    |    81     |
|6       |Easy 🔗 - Linux CLI - Shells Bells               |1 |      97ᵗʰ  |     3ʳᵈ    |   53,003ʳᵈ   |      712ⁿᵈ     |    134,354  |    1,027    |    81     |

</h6></div><br>

<p align="center">Global All Time:    100ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/b4ac8690-b695-444f-af6b-485a8301ff1a"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/dd872015-6fe6-4c60-a590-111d36dae615"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/7239539e-c215-4618-91d6-b64f48ba5c67"><br><br>
                  Global monthly:  18,059ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/f171697c-827d-46cc-aec3-b1b0c731c762"><br><br>
                  Brazil monthly:     206ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/1385d800-0934-4285-982a-a44ede24c5a6"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
