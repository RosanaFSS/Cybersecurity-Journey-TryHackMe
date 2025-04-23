<p align="center">April 22, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{351}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="" alt="Your Image Badge"><br>
<img width="300px" src="https://github.com/user-attachments/assets/1b3a99ee-a16e-4f56-88bc-89b58dc29dc4" alt="streak"><br></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{IAM Principals}}$$</h1>
<p align="center"><em>An overview of the different types of actors in IAM.</em>.<br>
It is classified as an easy-level walkthrough.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/iamprincipals">here</a>.</p>

<p align="center"> <img width="1000px" src=""> </p>
<br>
<br>

<h2>Task 1 . Introduction</h2>
<p>IAM Identities, sometimes referred to as IAM Principals, provide access to an AWS Account and its resources. These principals typically provide for authentication or validate authentication was performed. Principals are a core concept for Resource Policies that are attached to resources (like an S3 Bucket) and define who is allowed to act on the resource.<br><br>

This room will explain the multiple types of IAM Principals and their significance for attack and defense tactics.</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 1.1. <em>I understand IAM is important and I'm ready to move on.</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 2 . Access the environment</h2>
<p>[ ... ]</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 2.1. <em>Generate environment or set up your credentials</em><br><a id='2.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 3 . IAM Users</h2>
<p>[ ... ]</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 3.1. <em>There are two IAM Users in your account. The one you're using is the 12-digit account ID. What is the name of the other user?</em><br><a id='3.1'></a>
>> <strong><code>TryHackMe-IAM-User</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/be980847-6eda-4b5e-ad9c-db853ab0036b)

<br>
<br>

<h2>Task 4 . IAM Roles</h2>
<p>[ ... ]</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 4.1. <em>There are several roles in your account. What is the Trusted Entity for the OrganizationAccountAccessRole role?</em>Hint : <em>Enter the full string starting with arn.</em><br><a id='4.1'></a>
>> <strong><code>arn:aws:iam::XXXXXXXXXXXX:root</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/5125b98c-94d3-405b-9b7b-54575e37493c)

<br>

![image](https://github.com/user-attachments/assets/778edf02-8bd2-4fb4-b289-5da828b9e6b4)

<br>
<br>

<h2>Task 5 . Root User & AWS Account</h2>
<p>[ ... ]</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 5.1. <em>What is the MasterAccountEmail for your TryHackMe account?</em><br><a id='5.1'></a>
>> <strong><code>Redacted</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/12876445-b5b3-4388-a845-81260c6b52d6)

<br>
<br>

<h2>Task 6 . IAM Groups</h2>
<p>[ ... ]</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 6.1. <em>What is the name of the IAM Group your IAM User is currently a member of?</em><br><a id='6.1'></a>
>> <strong><code>IAMModule-Group</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/d949fc09-94e0-4379-9255-9616fde23107)

<br>
<br>

<h2>Task 7 . AWS Services</h2>
<p>[ ... ]</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 7.1. <em>What AWS Service is trusted to assume the Role “AWSServiceRoleForCloudFormationStackSetsOrgMember”?</em><br><a id='7.1'></a>
>> <strong><code>member.org.stacksets.cloudformation.amazonaws.com</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/7c452b1e-a8f2-4359-91f8-76d66ffb2a8c)

<br>

![image](https://github.com/user-attachments/assets/32ce057f-efd3-4fb9-9f68-735fb633f5af)

<br>

![image](https://github.com/user-attachments/assets/3f05e99e-fc17-4068-a20b-9f9380d476fa)

<br>
<br>

<h2>Task 8 . Everyone</h2>
<p>[ ... ]</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 8.1. <em>Just agree you're going to do your best to not win a Bucket Negligence Award.</em><br><a id='8.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 9 . Federated Identities</h2>
<p>[ ... ]</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 9.1. <em>What is the name of the Sample SAML Identity Provider in your account?</em><br><a id='9.1'></a>
>> <strong><code>TryHackMe-IAM-SAMLProvider</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/ae5a2d37-2329-4d1e-b686-80cc663e3b6d)

<br>
<br>

<h2>Task 10 . Conclusion</h2>
<p>ow that we have defined the various actors in the AWS IAM space, the next room, IAM Permissions, will go into how those actors are authorized to operate on cloud resources as we dive into the structure of an IAM Policy statement.</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 10.1. <em>I've completed this room</em><br><a id='10.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>


<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center">
<img width="900px" src="https://github.com/user-attachments/assets/ffb73840-6758-4acd-a6f7-0efb9d1ba1ab"><br>
<img width="900px" src="https://github.com/user-attachments/assets/df32ba12-7889-4f73-b6e3-41fcbc050aec"></p>

<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>


<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| April 22, 2025    | 351      |     267ᵗʰ    |      6ᵗʰ     |     50ᵗʰ    |     2ⁿᵈ    |  96,233  |    676    |     59    |

</div>


<br>

<p align="center"> Global All Time: 267ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/5d716d7b-5872-45b5-b405-8c454a77e1e1"> </p>

<p align="center"> Brazil All Time:   6ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/48521f38-b866-42f6-840a-3feb0eaa086b"> </p>

<p align="center"> Global monthly:    50ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/df83c339-6265-4677-9689-bbf637564af1"> </p>

<p align="center"> Brazil monthly:    2ⁿᵈ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/e92e8f82-3098-4d3f-870b-e60619716aae"> </p>

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/tryhackme">tryhackme</a>, <a href="https://tryhackme.com/p/wesladd">wesladd</a>, <a href="https://tryhackme.com/p/1337rce">1337rce</a> and  <a href="https://tryhackme.com/p/MonAha">MonAha</a> for investing your time and effort to develop this challenge so that I could sharpen my skills!</p> 





