<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Mr. Phisher}}$$</h1>
<p align="center"><img width="180px" src="https://github.com/user-attachments/assets/d0253d1c-4959-41c1-808d-ed5900a04f55"><br>
May 27, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my $$\textcolor{#FF69B4}{\textbf{386}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a><br>
I received a suspicious email with a very weird looking attachment. It keeps on asking me to "enable macros". What are those? Access it clicking <a href="https://tryhackme.com/room/mrphisher"</a>here.<br><br>
<img width="1000px" src="https://github.com/user-attachments/assets/43ed89e7-ca62-4a8d-8c52-ed18ff3bba68"></p>

<br>
<br>


<h2>Task 1 . Mr. Phisher</h2>

<p>I received a suspicious email with a very weird-looking attachment. It keeps on asking me to "enable macros". What are those?<br><br>



Access this challenge by deploying the machine attached to this task by pressing the green "Start Machine" button. The files you need are located in /home/ubuntu/mrphisher on the VM.<br><br>

Can't see the VM? Press the "Split Screen" button at the top of the page.<br><br>

<em>Please note that the document may take approximately a minute to launch for the first time.</em><br><br>

Check out similar content on TryHackMe: <code>Phishing Module>/code></p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>


> 1.1. <em>Uncover the flag in the email attachment!</em><br><a id='1.1'></a>
>> <strong><code>flag{a39a07a239aacd40c948d852a5c9f8d1}</code></strong><br>
<p></p>

<br>

<p>Navigated to <code>mrphisherv3 VM</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/2341c378-4b48-4409-b477-024ed0d291ef)

<br>

<p>Extracted <code>mr-phisher.zip</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/3d1608f9-36c4-41be-b73b-b7118d424fe5)

<br>

<p>Extracted <code>MrPhisher.docm(2)</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/4c39da3d-e401-430c-9caf-953268e7fae0)

<br>

<p>Accessed <code>MrPhisher.docm(2)_FILES</code>´s directory.</p>

<br>

![image](https://github.com/user-attachments/assets/b638f4d5-6548-462c-a891-dab464901d67)


<br>

![image](https://github.com/user-attachments/assets/a5ca5903-faf3-4fdd-931e-90a136f463a0)


<br>

<p>Identified a <code>.jpg</code> file.</p>

<br>

![image](https://github.com/user-attachments/assets/399f1dfa-0d2c-43b9-9ce6-15ac9d8a9f8b)

<br>

<p>There is a hint: <code>not sure if LINK or malware</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/f79be34c-6d5e-4d20-a04d-f2eb3049069e)

<br>


<p>Opened <code>MrPhisher.docm</code></p>

<br>

![image](https://github.com/user-attachments/assets/fdbecad2-8227-49bf-a1cd-6d5b531c5370)

<br>


![image](https://github.com/user-attachments/assets/43a045ae-0680-4fb0-84bd-38557b35494d)


<br>

![image](https://github.com/user-attachments/assets/3e84318b-be56-420e-b5f0-7fa2adc53ea7)




<br>

<p>Identified the content of a macro.</p>

<br>

![image](https://github.com/user-attachments/assets/cf51a32f-5922-4931-91a6-834bb4334c5f)


<br>

<p>Created a brakpoint.</p>

<br>

![image](https://github.com/user-attachments/assets/fe53849f-ee06-4808-b88b-f7be223067e0)

<br>

<p>Set up to watch variable <code>b</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/d71869cc-b1b3-479d-888c-233d2c190dd1)

<br>

![image](https://github.com/user-attachments/assets/dc2c1a7b-fdfe-45b5-aa89-419c99da1bba)


<br>

![image](https://github.com/user-attachments/assets/67992857-1bca-46b3-a854-2795ad7b0087)

<br>

```bash
b = ""
a = [102, 109, 99, 100, 127, 100, 53, 62, 105, 57, 61, 106, 62, 62, 55, 110, 113, 114, 118, 39, 36, 118, 47, 35, 32, 125, 34, 46, 46, 124, 43, 124, 25, 71, 26, 71, 21, 88]
for i in range(len(a)):
     b += chr(a[i] ^ i)
print(b)

```

<br>



![image](https://github.com/user-attachments/assets/f113c834-afe5-4540-b899-1900d166eccc)


<br>
<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/1d0ed272-4793-4959-b891-0340d4bcfcb0"><br>
                   <img width="1000px" src="https://github.com/user-attachments/assets/db6ef239-fa08-42e2-88b5-d1e27241b551"></p>


<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$</h1>


<div align="center">

| Date<br>          |  Streak<br>|   All Time<br>Global   |   All Time<br>Brazil |  Monthly<br>Global   |  Monthly<br>Brazil   |  SHOGUN<br>points  |   Rooms<br>completed  |  Badges<br> |
| :---------------: | :--------: | :--------------------: | :------------------: | :------------------: | :------------------: | :----------------: | :-------------------: | :---------: |
| May 27, 2025      |     386    |         206ᵗʰ          |            4ᵗʰ       |        147ᵗʰ         |           3ʳᵈ        |       105,097      |             752       |    62       |

</div>

<p align="center"> Global All Time:    206ᵗʰ<br><img width="300px" src="https://github.com/user-attachments/assets/6a3f4f40-451b-4231-be41-e34cba94d38e" alt="Your Image Badge"><br>
                                              <img width="1000px" src="https://github.com/user-attachments/assets/b740ad71-5488-4541-bf75-c0ef9f1f8010"><br><br>
                   Brazil All Time:     4ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/65d17fb1-178a-45cc-8754-e497a2b65b2f"><br><br>
                   Global monthly:    147ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/1ada0fba-b629-4c2c-805a-f66f9ae7b80e"><br><br>
                   Brazil monthly:      3ʳᵈ<br><img width="1000px" src="https://github.com/user-attachments/assets/15b883b7-8f78-4706-9f35-85ecb7dc8084"><br><br></p>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Thanks for coming!}}$$</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
<br>
<h1 align="center">Thank you very much <a href="https://tryhackme.com/p/tryhackme">tryhackme</a>  and <a href="https://tryhackme.com/p/cmnatic">cmnatic</a> for developinng this experience so that I could sharpen my skills!</h1>

