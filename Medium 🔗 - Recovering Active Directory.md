<h1 align="center">Recovering Active Directory</h1>
<p align="center">2025, August 4 - Day 455<br>
Learn basic techniques to recover an AD in case of compromise</strong>.<br>
Access it clicking <a href="https://tryhackme.com/room/recoveringactivedirectory">here </a>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/a180eb09-b28c-4d55-95a2-7d4a94cc8368"><br><br>
<img width="1200px" src="https://github.com/user-attachments/assets/b2bf7e3e-a2c4-450f-b7fe-2c71b64e1a29"></p>


<br>
<h2>Task 1 . Introduction</h2>
<p>We learned basic concepts on implementing group policies and the least privilege model in the previous room (Active Directory Hardening).<br>
In this room, we will focus on Active Directory vulnerabilities, methods for recovering the compromised Active Directory domain controller, and preventive measures to avoid hacking attempts.<br>
We will also discuss the Active Directory red architecture to implement operating system hardening and benchmarks defined for the server environment.</p>

<h3>Room Objectives</h3>
<p>The topics that we will cover in this room include:<br>

- Immediate actions after infection<br>
- Identifying attack patterns and how to locate an infection vector<br>
- Basic recovery process<br>
- Common misconfigurations by domain administrators<br>
- Post-recovery steps</p>

<h3>Room Prerequisites</h3>
<p>We will use Windows Server 2019, serving a <strong>compromised domain controller</strong> throughout the room.<br>
We assume that the hackers somehow got access to the domain controller on Apr 10, 2023, and now <em>creating additional accounts, modifying group policies, and disrupting essential services</em> of our network.<br>
The credentials to access the VM are mentioned below:<br>
  
- IP: 10.201.9.134<br>
- Username: THM\Administrator<br>
- Password: recover@123<br><br>
You can access the VM by clicking <code>Start Machine</code>.<br>
The machine will start in a split-screen view.<br>
If the VM is not visible, use the blue <code>Show Split View</code> button at the top-right of the page.<br>
Alternatively, you can access the VM through Remote Desktop using the above credentials<br><br>

Let's begin.</p>

<p><em>Answer the questions below</em></p>

<p>1.1. I can connect to the machine.<br>
<code>No answer needed</code></p>

<br>

<p>1.2. What is the flag value after connecting to the machine? Hint: <em>Check the flag file on the Desktop.</em><br>
<code>THM{I_CAN_CONNECT}</code></p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/d9e0a233-5472-45fc-a782-6399f2075f93"></p>

<br>
<h2>Task 2 . Immediate Actions - First Response</h2>
<p>The foremost important attempt of hackers is to gain persistent access to the system. Evicting threat actors entirely from a system is a complex and time-taking process; therefore, it is of utmost importance to <strong>limit the attack surface for the attacker and isolate the infrastructure</strong> (servers, objects) that are probably not compromised. Below is a quick checklist of steps that are recommended to be carried out before digging deep into the recovery process.<br>

- Take a backup of the compromised AD server using the built-in utility "<strong>Windows Server Backup</strong>". You can access it through <code>Run > wbadmin.msc</code>. Analysts would use the backup later for detailed malware and threat analysis.<br>
Note:  Please do not attempt to create a backup in the attached VM.</p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/92ae3a51-3839-4c3b-b45c-1e0e1f0cf52b"><br>
This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>

- Restore the <code>trusted backup</code> of the Windows Server. This restore operation will result in the loss of some data, like AD objects (users, computers, etc.) that were added to the domain after creating the trusted backup.<br>
- Segregate the network and activate the <code>secondary domain controller</code> to provide non-disruptive services to the user.<br>
- Enable <code>enhanced monitoring and filtering of traffic</code> from the restored AD server to identify any attack pattern at the network level.<br>
- Limit the creation and modification of new user accounts, GPOs etc., till the completion of the recovery process (if possible).</p>

<p><em>Answer the questions below</em></p>

<p>2.1. What type of backups can be obtained from the Windows Server Backup utility (write the correct option only)? A: One-time B: Incremental C: Both A and B.<br>
<code>C</code></p>

<br>

<p>2.2. How would you launch the Windows Server Backup utility through the Run dialog box?<br>
<code>wbadmin.msc</code></p>

<br>

<p>2.3. Is it good practice to isolate the infected network infrastructure for detailed network monitoring? (yea/nay).<br>
<code>yea</code></p>

<br>

<h2>Task 3 . How did it happen? Identifying Attack Pattern</h2>
<p>Understanding how the attack occurred is crucial to recover a compromised machine, as every device prepares logs based on specific events that help troubleshoot and investigate. Below is a list of tools used to analyse an Active Directory compromise incident.</p>

<br>
<h3>Event Viewer </h3>
<p>Event Viewer is a valuable tool for troubleshooting errors regarding Windows and applications. The event log service automatically starts with Windows and gives you detailed information about all critical events on your system. For example, if a computer program crashes or your system encounters a famous blue screen of death. You can read more about Windows services and Telemetry in the Windows Hardening room.<br>
Events are grouped as Error, Warning, and Information, whereas significant categories are as below:<br>

- <code>Application</code>: Records events of already installed programs.<br>
- <code>System</code>: Records events of system components.<br>
- <code>ASecurity</code>: Logs events related to security and authentication.<br><br>

We can access Event Viewer by typing eventvwr in the Run dialog.</p>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/58796366-c300-49ac-a138-a7752faa942b"><br>
This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<br>
<h3>BloodHound </h3>
<p>BloodHound is an Active Directory relational graphing tool with two primary functions:<br>
  
- It can amazingly reveal the Active Directory's hidden relationships.<br>
- It can miraculously determine the attack paths in an Active Directory environment.<br><br>

The assessment of BloodHound can be helpful for any organisation or company to outpace a wide array of security concerns. It utilises graph theory to perform the above-listed primary functions. It has an ingestor (called SharpHound) for data collection from all AD computers, groups, and users. Besides, it offers several benefits, like online backups and high-availability extensions (licensed ones). If you require the tool, you can easily download it from this link. You can visit the MITRE ATT&CK website to see the techniques used by this software.</p>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/8788f479-736f-406a-905c-a4bdcec5a2af"><br>
This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<br>
<h3>Powerview</h3>
<p>PowerView is a famous tool used by red teamers for Active Directory enumeration and identification of privileged accounts. Enumeration or profiling of AD is the first step taken by hackers to increase the attack surface and maximise the digital footprint of the target. Therefore, during the security assessment of an Active Directory, PowerView identifies loopholes that may result in a complete compromise of AD. You can download the PowerView PowerShell script from this link. The link contains various PowerShell scripts for LDAP, domain trust, user enumeration etc. <br>
We can execute PowerView in the attached VM through the following:<br>
  
- Run the command Import-Module C:\Users\Administrator\Desktop\PowerView\pw.ps1 in a PowerShell terminal.<br>
- Once the module is imported, we can run various commands like Get-NetDomainController, which gets information about the domain controller.</p>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/78ed1941-322d-4968-902c-10362bad331c"><br>
This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p><em>Answer the questions below</em></p>

<p>3.1. How many machines in the domain can you find when using PowerView? Hint: <em>Use "Get-NetComputer | select name"</em>.<br>
<code>11</code></p>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/33645439-76fb-466e-a7ce-6083861355af"><br><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/f2687c95-41d3-4e2d-ba8c-a4123797615d"></p>

<br>

<p>3.2. What is the name of the utility in Windows that displays and keeps track of all the events? <br>
<code>Event Viewer</code></p>

<br>

<h3>Task 4 . Who did this? Locating and Infection Vector</h3>
<p>If a domain controller is compromised, we can track the changes in the domain objects like users, computers, and group policies based on intruders' activities. Usually, once gained access to the system, the hackers create additional users, modify group policies, and try to become part of the domain Tier 0 group for persistent access. </p>

<h3>Tracking the changes </h3>
<p>[ ... ]</p>
<br>

<h3>Detection of User(s) Creation/Modifications</h3>
<p>[ ... ]</p>
<br>

<h3>Detection of Computers Joined the Domain</h3>
<p>[ ... ]</p>
<br>

<h3>Group Membership Modification </h3>
<p>[ ... ]</p>
<br>

<p>We can see the event log for ID 4728, which shows that user evil.guy was added to a global security group.
Note: The logs may be overwritten, which means that certain event IDs may not be available (as shown in the image).</p>

<h3>Identifying Group Policy Changes</h3>
<p>Event ID <code>4719</code> = <code>policy modification</code></p>
<p>After gaining access to the system, an attacker modifies the group policies to weaken the system's overall strength and enable multiple entry points. The event ID 4719 is associated with policy modification, which means that if any valid or invalid user tries to update the system audit policy, this action will generate an event log with ID 4719. Similarly, event ID 4739 is associated with domain policy change. We can search the Event Viewer for the ID as shown below:</p>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/542504cb-ed2d-4f51-a3d1-74689e9990cd"><br>
This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>We can see that the system audit policy was updated on Mar 2, 2023, and an event was logged into the system.<br>
Note: The logs may be overwritten, which means that certain event IDs may not be available (as shown in the image).<br>
Several tools are used for auditing Active Directory group policies, like NetWrix, ManageEngine, and SolarWinds ARM. These tools simplify the monitoring process and provide an interactive GUI for prompt response and security loophole identification. However, as a security engineer, it is also recommended to have a hold on essential commands and scripts that assists in recovering an AD.</p>

<p><em>Answer the questions below</em></p>

<p>4.1. What is the email address for the user evil.guy?</em>.<br>
<code>hack@crypto</code></p>

```bash
PS C:\Users> Get-ADUser -Identity username -Properties EmailAddress | Select-Object Name, EmailAddress
```

<p align="center"><img width="12000px" src="https://github.com/user-attachments/assets/0d11cb22-4434-452e-9826-ecc3a07cd0e3"></p>

<br>

<p>4.2. What is the total number of users logged on after Dec 1, 2022?</em>.<br>
<code>1</code></p>

```bash
PS C:\Users> Get-ADUser -Filter * -Properties LastLogonDate | Where-Object { $_.LastLogonDate -gt (Get-Date "2022-12-01") } | Select-Object Name, LastLogonDate | Sort-Object LastLogonDate -Descending
```

<p align="center"><img width="12000px" src="https://github.com/user-attachments/assets/5773c733-2522-40c2-9ec6-e645d14af48e"></p>

<br>

<p>4.3.What event ID will be logged if a user is removed from a universal security group?</em>.<br>
<code>4757</code></p>


<p align="center"><img width="12000px" src="https://github.com/user-attachments/assets/4206449e-7fae-477e-80ad-0879527a8e8f"></p>

<br>
<h2>Task 5. How to get it back? Domain Takback</h2>
<p>Due to the enormous usage of AD in organisations, hackers always seek to compromise a less secure system. In this regard, a Post-Compromise plan must be in place to ensure the availability of services and minimise downtime for AD users. The process of recovering an AD after being compromised is called Domain Takeback. 
</p>

<h3>Steps for Recovery Plan</h3>

<p>A few essential things that might be part of this plan are as follows:<br>
  
- Reset the password for Tier 0 accounts. You can reset or disable an account by simply selecting the desired option.<br>
- Look for possibly compromised (suspicious) accounts and reset their password to avoid privilege escalation.<br>
- Change the password for the Kerberos service account and make it unusable for the attacker.<br>
- Reset the passwords of accounts with administrative privileges.<br>
- Use the Reset-ComputerMachinePassword PowerShell command to perform reset operations for computer objects on the domain.<br>
- Reset the password of the domain controller machine to prevent silver ticket abuse. You can learn more about the different types of Kerberos-based attacks here. <br>
- Domain Controllers are the essential element for protection and recovery. If you have configured a writable domain controller (DC) as a backup for a compromised one, you can restore it -to avoid disruption (Be careful while performing this step. Do not restore an instance of a compromised DC).<br>
- Perform malware analysis on any targeted domain controller server for identification of malicious scripts.<br>
- Verify that the attacker has not added any scheduled tasks or start-up applications for persistent access. You can access the task scheduler through Run > taskschd.msc.<br>
- Check event logs, Access Control Lists (ACLs), and group policies for any possible change.<br>
- Enable traffic filtering on inbound and outbound traffic to identify Indicators of Compromise (IOC) at the network level (to be carried out at the Security Operation Center level).</p>

<p>Several AD protection and risk assessment tools, like Ping Castle, are available for auditing and identifying AD environment loopholes. Moreover, we can also forward logs to some SIEM solutions like Wazuh and Splunk, for detailed network analysis.</p>

<p><em>Answer the questions below</em></p>

<p>5.1. Reset the password for the user evil.guy.<br>
<code>No answer needed</code></p>

<p align="center"><img width="12000px" src="https://github.com/user-attachments/assets/5acee92a-c4c5-47d6-8b3b-4a67c7cf4a0f"></p>

<br>

<p>5.2. What is the command to perform the password reset operation for a computer in the domain?<br>
<code>Reset-ComputerMachinePassword</code></p>

<br>

<p>5.3. What is the security vulnerability that involves abusing Kerberos service tickets called?<br>
<code>Silver ticket abuse</code></p>

<br>

<h2>Task 6 . Why did it happen? Common misconfigurations</h2>
<p>Misconfigured servers, clients, and applications can offer an easy entry point for attackers to exploit. We have seen some common attacks in the AD hardening room and how to mitigate them. Below is a list of some more attacks that are typically not taken care of by system administrators. </p>

<h3>Boot source in BIOS</h3>
<p>Due to improperly configured BIOS boot order, attackers can also boot their devices and change login passwords to compromise the server. Configure the BIOS to prevent booting from CD/DVD, external devices (USB), or a floppy drive.</p>

<h3>AD Server Administrator Group Members</h3>
<p>Controlling who can log into workstations is one of the biggest challenges while hardening an AD environment.  All members of the Domain Users group can log into any workstation in the AD by default. Therefore, we must take preventive measures to limit users who can log in locally on computers with privileged access or domain controller. This is possible through the "Allow log on locally" policy that allows you to select a specific user or group who can log on on a particular computer. You can enable the policy through the following steps:<br><br>
  
Go to the group policy by typing gpedit.msc in the Run dialog and then navigate to Computer Configuration > Policies > Windows Settings > Security Settings > Local Policies > User Rights Assignment, and double-click on Allow log on locally and then select the users and groups we want to be able to log in to the DC.</p>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/6cd3e23c-ae53-4f17-b598-75bedcbf363b"><br>
This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h3>Weak Passwords</h3>
<p>Attackers with no access rights in the environment could effectively compromise your AD accounts by acquiring passwords through a dictionary or brute force attack. You might wonder how vulnerable your organisation is to such attacks. Tools like Mimikatz offer various ways to extract credentials; one is the DCSync attack. It is a feature of Mimikatz that try to imitate a domain controller and can retrieve password-relevant data like the hash of targeted user accounts. Attackers can get any account's NTLM password hash or plaintext password. You can learn more about the different types of Kerberos-based attacks here. </p>

<h3>Preventing DCSync Attack</h3>
<p>The DCSync attack enables an attacker to impersonate a domain controller and receive requests on behalf of that domain controller. A DCSync attack can be prevented by identifying accounts that have permission to replicate information in the domain. An attacker can launch the attack without even logging in the domain controller. Therefore, effective network monitoring is the key for mitigating such attacks. If you detect a DCSync attack, immediately disabling the compromised account can prevent privilege escalation by the attacker and limit their ability to make other changes to the network via Group Policy Objects.  </p>

<h3>Scripts and Applications Permissions on Workstations</h3>
<p>If a domain client can run unauthorised applications or scripts, then attackers can easily enumerate the whole network and run exploits as per vulnerability found in a target system. Many malware executes using command prompt, PowerShell and batch files. Restriction policy on scripts and applications can protect against many cyber-attacks on the AD server. </p>

<h3>Configure Network Time Synchronization</h3>
<p>Network devices and applications must be able to use the same time zones for security information and event management. The practice assists in the identification of threat actors and correlating attack patterns.</p>

<p><em>Answer the questions below</em></p>

<p>6.1. The type of attack that allows attackers to impersonate a domain controller and receive/forward requests on behalf of the domain controller is called?<br>
<code>DCSync</code></p>

<br>

<p>6.2. Is synchronising time on all network devices important to correlate logs on different devices? (yea/nay).<br>
<code>yea</code></p>

<br>

<h2>Task 7 . Post Recovery Actions</h2>
<p>Once the domain controller is recovered, a complete incident response plan must be developed to identify loopholes that enabled attackers to gain ingress to the system. A few of the essential actions after recovering the domain are mentioned below:</p>


<h3>Policy Decisions</h3>
<p>
  
- A detailed cyber security plan must be developed in line with some international frameworks like NIST.<br>
- Develop a disaster management policy to avoid such attacks in the future.<br>
- Detailed cyber security audit of the infrastructure to locate the infection vector of the incident and determine the root cause.<br>
- Ensure that logs from all the servers, computers, and network devices are maintained and forwarded to a reputable SIEM solution.</p>


<h3>Domain Controller</h3>
<p>
  
- Adding permanent rules in SIEM to block command and control (C2) domains and IP addresses used by the attacker.<br>
- Patching all vulnerable systems to prevent exploitation of systems through publicly available exploits.<br>
- Perform a thorough malware scanning of all domain controllers and domain-joined systems.<br>
- Perform operating system upgrades to the latest version of Windows Server as it offers more security features, like it provides AES encryption and supports red architecture more efficiently.<br>
- Remove the file shares on the domain controllers.<br>
- Disable the use of removable media on host computers, as attackers may propagate the malware on the whole network.</p> 


<h3>Backups</h3>
<p>
  
- The organisation network must have redundant domain controllers in high availability (primary/secondary layout).<br>
- Implement automated backup and recovery mechanisms.<br>
- Regularly verifying the trusted backups for validating integrity.</p>

<h3>Implementation of CIS benchmarks</h3>
<p>Critical systems are being exposed to the external world, and there is a dire need for advanced mechanisms to implement security policies. The Center for Internet Security (CIS) has established benchmarks to help secure computer systems, they can be downloaded depending on the operating system. These benchmarks ensure necessary configuration changes at the user and server levels. Moreover, pre-built scripts are available online for the rapid deployment of these policies. However, it is also crucial to understand the organisation's requirements before applying such hardening at the user/server level. </p>

<p><em>Answer the question below</em></p>

<p>7.1. Click the View Site button at the top of the task to launch the static site in split view. What is the flag after completing the exercise?<br>
<code>THM{I_HAVE_RECOVERED_AD}</code></p>

<p align="center"><img width="12000px" src="hhttps://github.com/user-attachments/assets/e5195936-32cf-4c4f-b9d1-08c8e9906eef"></p>

<br>

<h2>Task 8 . Conclusion</h2>
<p>Security is the most crucial part of the IT infrastructure. All organisations invest considerable efforts in implementing security controls to avoid financial and reputation loss. Most organisations prefer to implement AD services to manage resources centrally and securely. AD provides simplified management of all its objects like accounts, groups, computers, and file shares on the one hand. Still, on the other hand, it has some misconfigurations which attackers often exploit.<br>

In this room, we have learned that the monitoring and identification of attacks in a running AD smoothly and securely are ensured by implementing controls and procedures. Benchmarks have been set for AD security and must be followed to provide a secure environment. Lastly, a well-defined incident response plan must be implemented to tackle the attacks. Other preventive measures, such as deploying additional domain controllers and backup domain controllers, must be implemented to ensure recovery of the compromised primary domain server. </p>

<p><em>Answer the question below</em></p>

<p>8.1. I have completed the room.<br>
<code>No answer needed</code></p>


<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/b2baaca3-ff09-47d0-9e31-e1855a0cfe8f"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/83e25d27-25cd-4542-8aa9-a7f85e1263dc"></p>


<br>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 4    | 455      |    134ᵗʰ     |      5ᵗʰ     |   1,082ⁿᵈ   |    23ʳᵈ    | 119,074  |    893    |    73     |

</div>

<p align="center">Global All Time:   134ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/5459cd2e-5427-4e04-91bc-5a519c34326f"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/39a1775e-ca0f-4082-9ee8-458f7e4f114c"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/451c3694-381f-4f8b-8d96-0e75198f91a8"><br>
                  Global monthly:  1,082ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/d877d4d5-f85f-4d28-ba89-83230b7bbbb7"><br>
                  Brazil monthly:    23ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/9a2c57ec-4e36-4225-8cc3-fa54877bb3fd"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
