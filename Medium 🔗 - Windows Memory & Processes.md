
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


![image](https://github.com/user-attachments/assets/f898bd32-9445-4f28-8f96-215382b057b3)


<br>




<p>8.2. <code>TA0011</code></p>


![image](https://github.com/user-attachments/assets/6c21cf3a-ab07-483d-bbb6-b9634e5b1cdf)



