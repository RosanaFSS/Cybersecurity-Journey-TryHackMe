<p>June 25, 2025</p>
<h1>Linux Agency</h1>
<p>This Room will help you to sharpen your Linux Skills and help you to learn basic privilege escalation in a HITMAN theme. So, pack your briefcase and grab your SilverBallers as its gonna be a tough ride.</p>

<h1>Task 1 . Deploy the Machine</h1>

<p>1.1. Deploy This Machine.<br>
<code>No answer needed</code></p>

<br>

<h1>Task 2 . Let´s jump in</h1>
<p>Please wait about 1 minute before SSH'ing into the box.<br>

SSH Username : agent47<br>

SSH Password : 640509040147<br>

Each flag found will serve as the password for the next user. The flag includes the username of the next user that is part of this challenge. The Flag format is : username{md5sum}<br>

The order of users: agent47 --> mission1 --> mission30 will be part of Task 3: Linux Fundamentals.<br>

After those missions, the next levels will be in Task 4: Privilege Escalation.</p>

<p>2.1. SSH into the box as agent47<br>
<code>No answer needed</code></p>

```bash
:~/LinuxAgency# ssh agent47@TargetIP
...
mission1{174dc8f191bcbb161fe25f8a5b58d1f0}
agent47@linuxagency:~$
```

![image](https://github.com/user-attachments/assets/705f61fb-3778-4271-83bd-c5dca0638918)

<br>

<h1>Task 3 . Linux Fundamentals</h1>
<p>Agent 47, we are ICA, the Linux Agency. We will test your Linux Fundamentals. Let's see if you can pass all these challenges of basic Linux. The password of the next mission will be the flag of that mission. Example: mission1{1234567890} will be the password for the mission1 user.
<h3>Mission Active</h3></p>

<p>3.1. What is the mission1 flag?<br>
<code>mission1{174dc8f191bcbb161fe25f8a5b58d1f0}</code></p>

<p>3.2. What is the mission2 flag?<br>
<code>mission1{174dc8f191bcbb161fe25f8a5b58d1f0}</code></p>

<p>used <code>mission2{8a1b68bb11e4a35245061656b5b9fa0d}</code> as password.</p>

```bash
:~/LinuxAgency# ssh agent47@TargetIP
...
mission1{174dc8f191bcbb161fe25f8a5b58d1f0}
agent47@linuxagency:~$ su mission1
Password: 
mission1@linuxagency:/home/agent47/Documents$ cd /home
mission1@linuxagency:/home$ ls
0z09e    jordan    mission10  mission14  mission18  mission21  mission25  mission29  mission5  mission9  silvio
agent47  ken       mission11  mission15  mission19  mission22  mission26  mission3   mission6  penelope  viktor
dalia    maya      mission12  mission16  mission2   mission23  mission27  mission30  mission7  reza      xyan1d3
diana    mission1  mission13  mission17  mission20  mission24  mission28  mission4   mission8  sean
mission1@linuxagency:/home$ cd mission1
mission1@linuxagency:~$ ls
mission2{8a1b68bb11e4a35245061656b5b9fa0d}
```

<p>3.3. What is the mission3 flag?<br>
<code>mission3{ab1e1ae5cba688340825103f70b0f976}</code></p>

```bash
mission1@linuxagency:~$ su mission2
Password: 
mission2@linuxagency:/home/mission1$ cd ..
mission2@linuxagency:/home$ cd mission2
mission2@linuxagency:~$ ls
flag.txt
mission2@linuxagency:~$ cat flag.txt
mission3{ab1e1ae5cba688340825103f70b0f976}
```

<p>3.4. What is the mission4 flag?<br>
<code>mission4{264a7eeb920f80b3ee9665fafb7ff92d}</code></p>

```bash
mission2@linuxagency:~$ su mission3
Password:
...
mission3@linuxagency:~$ cat flag.txt
I am really sorry man the flag is stolen by some thief's.
mission3@linuxagency:~$ 
mission3@linuxagency:~$ file flag.txt
flag.txt: ASCII text, with CR, LF line terminators
mission3@linuxagency:~$ strings flag.txt
mission4{264a7eeb920f80b3ee9665fafb7ff92d}
I am really sorry man the flag is stolen by some thief's.
```

<p>3.5. What is the mission5 flag?<br>
<code>mission5{bc67906710c3a376bcc7bd25978f62c0}</code></p>

```bash
mission3@linuxagency:~$ su mission4
Password: 
...
mission4@linuxagency:~$ ls -lah
total 20K
drwxr-x---  3 mission4 mission4 4.0K Jan 12  2021 .
drwxr-xr-x 45 root     root     4.0K Jan 12  2021 ..
lrwxrwxrwx  1 mission4 mission4    9 Jan 12  2021 .bash_history -> /dev/null
-rw-r--r--  1 mission4 mission4 3.7K Jan 12  2021 .bashrc
drwxr-xr-x  2 mission4 mission4 4.0K Jan 12  2021 flag
-rw-r--r--  1 mission4 mission4  807 Jan 12  2021 .profile
mission4@linuxagency:~$ cd flag
...
mission4@linuxagency:~/flag$ cat flag.txt
mission5{bc67906710c3a376bcc7bd25978f62c0}
mission4@linuxagency:~/flag$ 
```

<p>3.6. What is the mission6 flag?<br>
<code>mission6{1fa67e1adc244b5c6ea711f0c9675fde}</code></p>

```bash
mission4@linuxagency:/home$ su mission5
Password: 
...
mission5@linuxagency:~$ cat .flag.txt
mission6{1fa67e1adc244b5c6ea711f0c9675fde}
```

<p>3.7. What is the mission7 flag?<br>
<code>mission7{53fd6b2bad6e85519c7403267225def5}</code></p>

```bash
mission5@linuxagency:/home$ su mission6
Password: 
mission6@linuxagency:/home$ cd mission6
mission6@linuxagency:~$ find / -type f -name "flag.txt" 2>/dev/null
/home/mission6/.flag/flag.txt
/flag.txt
mission6@linuxagency:~$ cat ~/.flag/flag.txt
mission7{53fd6b2bad6e85519c7403267225def5}
```

<p>3.8. What is the mission8 flag?<br>
<code>mission7{53fd6b2bad6e85519c7403267225def5}</code></p>

```bash
mission6@linuxagency:~$ su mission7
Password:
```

