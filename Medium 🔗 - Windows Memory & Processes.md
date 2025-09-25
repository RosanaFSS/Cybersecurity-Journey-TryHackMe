<h1 align="center"> Windows Memory & Processes<br><img width="1200px" src="https://github.com/user-attachments/assets/3c611801-4d91-40e8-b35b-a2395cf04ada"><br>

<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/eec07c31-df33-48de-a52b-2b9b701ba625"><br>
May 28, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my $$\textcolor{#FF69B4}{\textbf{387}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a><br>
Analyze a memory dump of a Windows host and uncover malicious processes. Access it clicking <a href="https://tryhackme.com/room/windowsmemoryandprocs"</a>here.<br><br>
<img width="1000px" src="https://github.com/user-attachments/assets/b38ff0f8-0cac-4043-9249-4776d5c57a45"></p>

<br>
<br>

<p>THe hashes are the same.</p>

<br>

![image](https://github.com/user-attachments/assets/3399c45d-8f64-4da2-bbc8-3fa15993181f)

<br>

<p>- Extracted Processes.</p>

![image](https://github.com/user-attachments/assets/1bc0f1fc-0b28-43f8-8670-7f4739d42819)

<br>

<p>- Displayed Extracted Processes.</p>

<br>

<p>Comparing With a Baseline</p>

![image](https://github.com/user-attachments/assets/70a39d37-5a71-49e8-8c77-2689015b0b19)

<br>

![image](https://github.com/user-attachments/assets/5070d905-f8a5-4202-98fe-b6c535385b35)


<br>

<p>4.1. <code>440</code></p>

![image](https://github.com/user-attachments/assets/8cbb7472-e593-4c8d-8c1c-7aa77bcbcd1e)

<br>

<p>4.2. <code>0x990b29293080</code></p>

![image](https://github.com/user-attachments/assets/7e3be05b-9ca0-4ce8-9c1b-e8539aac6fc9)

<br>
<br>

<h2>Task 5 . Linking Processes</h2>

<p>[ ... ]</p>

<p>5.1. <code>524</code></p>

![image](https://github.com/user-attachments/assets/0eafbfb0-ed19-4ecc-916d-0a406f3fdde0)

<br>

<p>5.2. <code>FTK Imager.exe</code></p>

![image](https://github.com/user-attachments/assets/7047b0f2-9d5c-44a4-8813-898e1da531c8)


<br>
<br>

<h2>Task 6 . Digging Deeper</h2>

<br>

<p>[ ... ]</p>


<p>6.1. <code>3</code></p>

<p>6.2. <code>3</code></p>



![image](https://github.com/user-attachments/assets/b2d8b0c3-c2eb-439a-a48d-b409c81257d6)

<br>

![image](https://github.com/user-attachments/assets/0b042ab5-fb10-413d-8c21-c02638178a34)

<br>

<h3>-----------  PSSCAN -----------</h3>


```bash
ubuntu@tryhackme:~$ vol3 -f THM-WIN-001_071528_07052025.mem windows.psscan > psscan.txt
...
ubuntu@tryhackme:~$ awk 'NR==3 || $5 == "0"' psscan.txt
...
```


![image](https://github.com/user-attachments/assets/8c7d5620-2d7f-4773-8693-1f346e1fb8c6)


<br>

<h3>-----------  PSXVIEW -----------</h3>


```bash
ubuntu@tryhackme:~$ vol3 -f THM-WIN-001_071528_07052025.mem windows.psxview > psxview.txt
...

```

<br>

![image](https://github.com/user-attachments/assets/79d31b73-3d5f-4f13-ad84-e52d96f846bf)

<br>


```bash
ubuntu@tryhackme:~$ head -n 8 psxview.txt
...
```

<br>

![image](https://github.com/user-attachments/assets/47922075-9ebe-44f3-97d2-d78f1d09e3e4)

<br>


```bash
ubuntu@tryhackme:~$ sort -k8 -r psxview.txt
...
```

<br>

![image](https://github.com/user-attachments/assets/fe5545d6-5b7b-4076-9361-b4b0ed3d719e)

<br>
<br>

<h2>Task 7 . Dumping the Process Memory</h2>

<br>

<p>7.1. <code>C:\Program Files\AccessData\FTK Imager\FTK Imager.exe</code></p>

<br>

```bash
ubuntu@tryhackme:~$ vol3 -f THM-WIN-001_071528_07052025.mem windows.dlllist --pid 7788 > 7788_dlllist.txt
ubuntu@tryhackme:~$ cat 7788_dlllist.txt
...
```

<br>

![image](https://github.com/user-attachments/assets/ca75fb0d-d3d6-4666-9972-37739dd587c8)

<br>


<p>7.2. <code>file.0x990b2ae1ed40.0x990b29954a20.ImageSectionObject.FTK Imager.exe.img</code></p>


<br>

```bash
ubuntu@tryhackme:~$ vol3 -f THM-WIN-001_071528_07052025.mem windows.dlllist --pid 7788 > 7788_dlllist.txt
ubuntu@tryhackme:~$ cat 7788_dlllist.txt
...
```

<br>


![image](https://github.com/user-attachments/assets/73c8b295-b483-4b4c-a64f-23e2b38c375d)


<br>
<br>

<h2> Task 8 . Putting It All Together</h2>
<p>While analyzing the memory dump, you have uncovered possible indicators of compromise. Although, some of these indicators need to be analyzed further to be certain. With the artifacts gathered and observations made, it is possible to recreate a part of the kill chain. The table below shows all the gathered information.</p>

<br>

![image](https://github.com/user-attachments/assets/c4d5a76f-8cba-4bf0-b663-c3cf996b5cec)

<br>

![image](https://github.com/user-attachments/assets/3809f3e8-457b-4243-802a-af0896637e8f)



<p>8.1. <code>file.0x990b2ae1ed40.0x990b29954a20.ImageSectionObject.FTK Imager.exe.img</code></p>

<br>

```bash
ubuntu@tryhackme:~$ mkdir 5252
ubuntu@tryhackme:~$ cd 5252
ubuntu@tryhackme:~/5252$ vol3 -f ../THM-WIN-001_071528_07052025.mem windows.dumpfiles --pid 5252
...
ubuntu@tryhackme:~$ ls 5252 | grep -E ".docm|.dotm" -i
```

<br>


![image](https://github.com/user-attachments/assets/a45cf6c5-6d77-42b4-9abd-3d21e2046a5c)

<br>

![image](https://github.com/user-attachments/assets/3e2ceddc-a84d-49d1-967b-04b84c0d99f1)

<br>

![image](https://github.com/user-attachments/assets/887841bf-f9a3-4841-8198-a33a79d6edbf)

<br>

![image](https://github.com/user-attachments/assets/c8081bc8-4012-4069-a427-432a49dffeec)

<br>

![image](https://github.com/user-attachments/assets/50a49df6-9da1-4ebf-a31b-297bb9a44206)

<br>

![image](https://github.com/user-attachments/assets/1d975475-2277-4a26-b1a1-8726ca8f2efe)

<br>

<p>:-!</p>

<br>

```bash
ubuntu@tryhackme:~$ mkdir 5252
ubuntu@tryhackme:~$ cd 5252
ubuntu@tryhackme:~/5252$ vol3 -f ../THM-WIN-001_071528_07052025.mem windows.dumpfiles --pid 5252
...
ubuntu@tryhackme:~$ ls 5252 | grep -E ".docm|.dotm" -i

```

<br>

![image](https://github.com/user-attachments/assets/fd7582aa-3b17-406c-a64c-9378eb405e68)

<br>



![image](https://github.com/user-attachments/assets/f898bd32-9445-4f28-8f96-215382b057b3)


<br>




<p>8.2. <code>TA0011</code></p>


![image](https://github.com/user-attachments/assets/6c21cf3a-ab07-483d-bbb6-b9634e5b1cdf)



<br>

<h2>Task 9 . Conclusion</h2>
<p>This room was the first in a series of three that dives into analyzing a memory dump. You went through a real-life scenario and analyzed a memory dump with a focus on extracting processes and their information. You uncovered a potential attack chain and multiple suspicious artifacts.<br><br>

Analyzing processes is only the beginning. The next steps are analyzing user and network activity.</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>


> 9.1. <em>I am ready to apply my newly obtained skills!</em><br><a id='9.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>



<br>
<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/1a3111a6-ee8c-44ee-8e51-2baa60b2718b"><br>
                   <img width="1000px" src="https://github.com/user-attachments/assets/01d32ff6-51d5-45da-b262-094eea1c8208"></p>


<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$</h1>


<div align="center">

| Date<br>          |  Streak<br>|   All Time<br>Global   |   All Time<br>Brazil |  Monthly<br>Global   |  Monthly<br>Brazil   |  SHOGUN<br>points  |   Rooms<br>completed  |  Badges<br> |
| :---------------: | :--------: | :--------------------: | :------------------: | :------------------: | :------------------: | :----------------: | :-------------------: | :---------: |
| May 28, 2025      |     387    |         206ᵗʰ          |            4ᵗʰ       |        133rd         |           3ʳᵈ        |       105,249      |             753       |    62       |

</div>

<p align="center"> Global All Time:    206ᵗʰ<br><img width="300px" src="https://github.com/user-attachments/assets/02b37c5c-0d9f-4556-8d41-c3ba7bf9fced" alt="Your Image Badge"><br>
                                              <img width="1000px" src="https://github.com/user-attachments/assets/af4f172c-b35d-4f96-9fd1-54f65c68e2d9"><br><br>
                   Brazil All Time:     4ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/cc88a1eb-7ece-453f-a99d-e20dbfa244e8"><br><br>
                   Global monthly:    133rd<br><img width="1000px" src="https://github.com/user-attachments/assets/5672cee7-375e-4574-a526-91e2d39b3070"><br><br>
                   Brazil monthly:      3ʳᵈ<br><img width="1000px" src="https://github.com/user-attachments/assets/ecb82df8-78df-4e53-b500-faf3dffef7b0"><br><br></p>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Thanks for coming!}}$$</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
<br>
<h1 align="center">Thank you very much <a href="https://tryhackme.com/p/Gensane">Gensane</a>   for developinng this experience so that I could sharpen my skills!</h1>
