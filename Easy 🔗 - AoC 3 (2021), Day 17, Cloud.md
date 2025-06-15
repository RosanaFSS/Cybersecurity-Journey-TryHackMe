<h1 align="center">Advent of Cyber 3 (2021) - Cloud - Day 17 -  Elf Leaks</h1> 
<p align="center"><img width="200px" src="https://github.com/user-attachments/assets/6371db5c-9eec-4f49-bdff-02ec11b425c9"><br>Jun 3, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my 393-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>
<br>Access Advent of Cyber 3 (2021) clicking <a href="https://tryhackme.com/room/adventofcyber3"</a>here.<br><br>
<img width="1000px" src="https://github.com/user-attachments/assets/8616be45-ce7a-4986-a200-2cd588cf410e"></p>

<br>
<br>

<p>1.1. What is the name of the S3 Bucket used to host the HR Website announcement?<br>
<code>images.bestfestivalcompany.com</code><br></p>

<p>

- Right-clicked the image.<br>
- Clicked <code>Copy image address</code>.<br>
- Launched the web browser.<br>
- Navigated to <code>https://tryhackme.com/img/events/christmas/tree.png</code>.</p>

![image](https://github.com/user-attachments/assets/be9a1f54-83d6-4fe2-9f53-64572242b279)

<br>

![image](https://github.com/user-attachments/assets/b02a32af-f65b-453a-8973-104331f4ce58)

<p>

- Right-clicked the other image.<br>
- Clicked <code>Copy image address</code>.<br>
- Navigated to <code>https://s3.amazonaws.com/images.bestfestivalcompany.com/tree.png</code>.</p>

![image](https://github.com/user-attachments/assets/f9ea44f0-382f-4f49-b6a4-9a90620e2fe2)

<br>

![image](https://github.com/user-attachments/assets/c4123bcb-7645-4c02-821e-657e8e330598)

<br>

![image](https://github.com/user-attachments/assets/926a2212-2fb5-4e94-b5d6-4f032ab4c7e1)

<br>


<p>1.2. What is the message left in the flag.txt object from that bucket?<br>
<code>It's easy to get your elves data when you leave it so easy to find!</code><br></p>

![image](https://github.com/user-attachments/assets/1d186d58-74d3-41f2-b784-55a54d3f3b00)

<br>

<p>1.3. What other file in that bucket looks interesting to you?<br>
<code>wp-backup.zip</code><br></p>

![image](https://github.com/user-attachments/assets/d455eadd-fb2b-4c4d-92f7-e2128f48123f)

<br>

<p>1.4. What is the AWS Access Key ID in that file? Hint : Hint: If you cannot curl the file, can you download it via the AWS CLI? Remember the string you're looking for begins with AKIA.<br>
<code>No answer needed</code><br></p>


![image](https://github.com/user-attachments/assets/d4b6fc1a-bbcf-4d95-9107-f5c5e1ef09f9)

<br>

![image](https://github.com/user-attachments/assets/4a968ed2-b710-4387-b747-7a76c2fa92c0)

<br>

![image](https://github.com/user-attachments/assets/93f695c3-011b-4b67-bd0e-63d77d004e77)

<br>

<p>1.5. What is the AWS Account ID that access-key works for?<br>
<code>019181489476</code><br></p>

![image](https://github.com/user-attachments/assets/2d657ba0-f795-4d72-a9d6-1361e67fe6cc)

<br>

![image](https://github.com/user-attachments/assets/56225f5c-38f5-48a0-bf9e-302d91137cdb)

<br>

<p>1.6. What is the Username for that access-key?<br>
<code>ElfMcHR@bfc.com</code><br></p>

![image](https://github.com/user-attachments/assets/fe8e5f1f-8745-476e-b957-a65b2659722d)


<br>


<p>1.7. There is an EC2 Instance in this account. Under the TAGs, what is the Name of the instance?<br>
<code>HR-Portal</code><br></p>

![image](https://github.com/user-attachments/assets/1e9ce646-75c2-43bb-a52f-19b81838f511)

<br>

<p>1.7. What is the database password stored in Secrets Manager?<br>
<code>Winter2021!</code><br></p>

![image](https://github.com/user-attachments/assets/ca3657a5-18b4-4d32-ac19-67775417d4e2)

<br>

![image](https://github.com/user-attachments/assets/f533edff-6a53-4c58-b001-c3b2a0fb1d11)

<br>


![image](https://github.com/user-attachments/assets/8aa03d1c-6974-43b5-9040-33f339f9bca3)

<br>
<br>


<h1 align="center">Challenge in Progress, 73%</h1>
<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/a4bf4153-52bd-4171-a84f-3548ec24a44c"></p>
                   
<h1 align="center">My TryHackMe Journey</h1>


<div align="center">

| Date<br>          |  Streak<br>|   All Time<br>Global   |   All Time<br>Brazil |  Monthly<br>Global   |  Monthly<br>Brazil   |  SHOGUN<br>points  |   Rooms<br>completed  |  Badges<br> |
| :---------------: | :--------: | :--------------------: | :------------------: | :------------------: | :------------------: | :----------------: | :-------------------: | :---------: |
| Jun 3, 2025       |     393    |          200ᵗʰ         |            4ᵗʰ       |        5,829ᵗʰ       |         108ᵗʰ        |       106,091      |             762       |    62       |

</div>

<p align="center"> Global All Time: 200ᵗʰ <br><img width="300px" src="https://github.com/user-attachments/assets/d5da6831-af8e-49e9-b006-ff6e740afb62" alt="Your Image Badge"><br>
                                              <img width="1000px" src="https://github.com/user-attachments/assets/87889441-1727-4ba4-bea1-a6d5a272b8b1"><br><br>
                   Brazil All Time:   4ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/150d78bd-674a-418e-bda6-f4ffa93f63de"><br><br>
                   Global monthly: 5,829ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/a27b7605-47b3-4500-abc8-b0bb36c51799"><br><br>
                   Brazil monthly:   108ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/d99c5b06-4261-4c04-93c5-7897755dc669"><br><br></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
<br><br>
<h1 align="center">Thank you very much ben, ashu, tryhackme, cmnatic, timtaylor, strategos, umairalizafar, jcfarris, and wesladd for developinng this experience so that I could sharpen my skills!</h1>

