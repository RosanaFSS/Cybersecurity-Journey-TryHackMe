<p align="center">April 22, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{351}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/eb11741e-e8de-491b-bf9f-de81cb57c2fe" alt="Your Image Badge"><br>
<img width="300px" src="https://github.com/user-attachments/assets/1b3a99ee-a16e-4f56-88bc-89b58dc29dc4" alt="streak"><br></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{IAM Permissions}}$$</h1>
<p align="center"><em>Learn how authorization is handled in AWS IAM.</em>.<br>
It is classified as a medium-level walkthrough.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/iampermissions">here</a>.</p>

<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/1063c27f-4aad-4aa2-b2fe-3a94ea5ac669"> </p>

<br>
<br>

<h2>Task 1 . Structure of an IAM Policy</h2>
<p>[ ... ]</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 1.1. <em>What is the PolicyId of the ReadOnlyAccess managed policy?</em><br><a id='1.1'></a>
>> <strong><code>ANPAILL3HVNFSB6DCOWYQ</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/fd3c048d-8e46-42e0-a23a-70a8742c740b)


<br>

<h2>Task 2 . Accessing the environment</h2>
<p>[ ... ]</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 2.1. <em>Generate environment or set up your credentials</em><br><a id='2.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 3 . Action</h2>
<p>[ ... ]</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 3.1. <em>What action "Grants permission to create access key and secret access key for the specified IAM user"? You can find a hint in the Service Authorization docs for IAM</em><br><a id='3.1'></a>
>> <strong><code>iam:CreateAccessKey</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/39d895ee-9d10-4ae2-9a1a-867d72d0d17a)


<br>
<br>

<h2>Task 4 . Resource</h2>
<p>[ ... ]</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 4.1. <em>TIn your account, there is a bucket that begins with "tryhackme-bucket-" and ends with your unique account ID. What is the ARN of that bucket excluding the last 12 digit account ID?</em>Hint : <em>Bucket ARNs are global, but you can find it in the Bucket Policy with this command: aws s3api get-bucket-policy --bucket tryhackme-bucket-YOURACCOUNTID --query Policy --output text | jq.</em><br><a id='4.1'></a>
>> <strong><code>arn:aws:s3:::tryhackme-bucket-</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/53d08a79-366d-49e7-966b-68799a62164c)


<br>
<br>

<h2>Task 5 . Effect</h2>
<p>[ ... ]</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 5.1. <em>Given the policy above, can this user get the HR Password (Y/N)?</em><br><a id='5.1'></a>
>> <strong><code>N</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 6 . Principal</h2>
<p>[ ... ]</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 6.1. <em>Look in your account. What is the Principal that is allowed to assume the OrganizationAccountAccessRole role?</em>Hint : <em>Be sure to include everything inside the Principal: {} curly-braces.</em><br><a id='6.1'></a>
>> <strong><code>"AWS": "arn:aws:iam::116457965582:root"</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/d949fc09-94e0-4379-9255-9616fde23107)

<br>
<br>

<h2>Task 7 .Conditions</h2>
<p>[ ... ]</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 7.1. <em>The Glue Service, running in vpc-12345, can write an object to the my-logs-bucket? (T/F)</em>Hint : <e.Because the sourceVPC and PrincipalServiceName conditions are AND'ed inside the StringNotEquals, both conditions must be true to evaluate as true.</em><br><a id='7.1'></a>
>> <strong><code>F</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 8 . NotAction, NotResource, NotPrincipal</h2>
<p>[ ... ]</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 8.1. <em>As headmaster, Dumbledore's IAM policy is: <code>{"Effect": "Allow", "Action": "*", "Resource": "*"}</code>Would he have access to the ForbiddenForest if the second policy were in place? (Y/N)</em><br><a id='8.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>


<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>


<br>
<p align="center">

  
<img width="1000px" src="https://github.com/user-attachments/assets/b1d27ef7-c2e6-4803-97ce-bbd982d1ba9d"><br>
<img width="1000px" src="https://github.com/user-attachments/assets/fc99757b-6dd3-4d38-bead-483d5ddd06f4"></p>

<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>


<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| April 23, 2025    | 352      |     263ʳᵈ    |      6ᵗʰ     |     48ᵗʰ    |     2ⁿᵈ    |  96,595  |    680    |     59    |

</div>


<br>

<p align="center"> Global All Time: 263ʳᵈ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/3edcca92-e077-4717-8a4b-4e64f1a9f2a9"> </p>

<p align="center"> Brazil All Time:   6ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/1ef03d8a-6e0f-40aa-afdb-a336b36c2af7"> </p>

<p align="center"> Global monthly:    48ʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/a4ae9a01-d629-4501-a02a-3e3952904c6e"> </p>

<p align="center"> Brazil monthly:    2ⁿᵈ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/a1b6ae83-9052-42d3-8598-ef055a8387e8"> </p>

<br>


<p align="center"> Weekly League: 6ᵗʰ Gold<br><br><img width="1000px" src="https://github.com/user-attachments/assets/1da81abb-58c3-4326-b6f1-c18ffe6b4139"> </p>

<br>


<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/tryhackme">tryhackme</a> and  <a href="https://tryhackme.com/p/jcfarris">jcfarris</a> for investing your time and effort to develop this challenge so that I could sharpen my skills!</p> 
