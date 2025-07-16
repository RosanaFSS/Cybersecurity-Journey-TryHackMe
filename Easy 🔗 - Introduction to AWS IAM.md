<p align="center">April 22, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{351}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/5332a860-5457-4fd7-b33c-98869f5beac9" alt="Your Image Badge"><br></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Introduction to AWS IAM}}$$</h1>
<p align="center"><em>A Brief introduction to the importance of IAM and the IAM Module.</em>.<br>
It is classified as an easy-level walkthrough.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/introductiontoawsiam">here</a>.</p>


<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/1790477a-cd2f-48a2-88fa-62200466abaf"> </p>
<br>

<h2>Task 1 . Introduction</h2>
<p>Understanding IAM - AWS’s Identity and Access Management service - is critical to attacking or defending an AWS account. IAM is a highly complex service with multiple parts. In this module, you’ll learn about:</p>

<br>

![image](https://github.com/user-attachments/assets/64dbaa16-ae92-4056-92a0-36d784dae0d1)

<br>

<p>Why is IAM so important? With traditional network-centric security, you’re dealing with two dimensions. You are either inside the firewall or outside the firewall. With public clouds, like AWS, the network is Software Defined. I issue API calls to AWS to control the network. All of these API calls introduce a third dimension. Suddenly you’re no longer defending castles from opposing armies; you’re defending castles from dragons.</p>

<p>IAM is how AWS manages access to the APIs that control your network - and all the other resources that exist in your account. With the right IAM permissions, I can change your firewalls, update routing tables of your network, and exfiltrate data from your NoSQL databases or object storage. AWS even has several system management tools that efficiently allow you to pop shells on a machine.<br><br>

As a defender, you need to understand how to defend your cloud accounts and resources against attacks that leverage IAM. As an attacker, you can leverage AWS IAM in a number of ways to compromise a target, move laterally, and exfiltrate data. </p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 1.1. <em>I understand IAM is important and I'm ready to move on.</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 2 . Introduction to AWS IAM</h2>
<p>One of the core principles of identity and access control in AWS is the concept of an AWS Account.  Amazon treats each account as an independent customer of AWS, and each account is its own independent trust boundary.  Inside an AWS Account, there can be multiple IAM Users, Groups, and Roles.<br><br>

Terminology can be confusing, and people often refer to granting access as "giving someone an IAM Account".  For clarity, we shall always refer to the AWS Account as an Account and an IAM User inside that account as an IAM User.<br><br>

Every AWS Account has a root user, and AWS considers that root user the customer.  Major customer-service interactions need to occur from that root user, including billing changes and closing the account.  The root user is all-powerful and has complete control over all resources in the account (except for AWS Organizational Service Control Policies which we will discuss in a future room). <br><br>

Since the root user is all-powerful, and since there is only one, best-practice is to create individual IAM Users for each person who needs access to the account and only grant the level of access required for their job function.  When creating an account for the first time, the common practice is for the root user to create an Admin IAM User and never use root again. <br><br>

At this point, day-to-day access should occur via either IAM Users or IAM Roles.  IAM Users combine authentication, identity, and authorization into a single unit.  IAM Roles typically delegate the authentication and identity to another system and primarily manage authorization.  We will discuss Users and Roles in the next Room.<br><br>

Both IAM Users and IAM Roles require IAM Policies to be able to do anything.  By default, all API requests are implicitly denied.  We will discuss policies and how they work in a future room.  For introductory purposes, the User or Role is the "who" can do something, and the Policy defines the "what" they can do. <br><br>

IAM Policies define the actions that the user or role can perform on a resource.  Almost everything you create in AWS is a Resource, and almost all Resources can be identified by their Amazon Resource Name or ARN.  AWS defines an ARN as: <br><br>

Amazon Resource Names (ARNs) uniquely identify AWS resources.  We require an ARN when you need to specify a resource unambiguously across all of AWS, such as in IAM policies, Amazon Relational Database Service (Amazon RDS) tags, and API calls (source)<br><br>

An ARN consists of the AWS Region, AWS Account ID, Service, and some identifiers for the Resource, commonly the Resource's name.  ARNs are unique across all of AWS.  For example, this is the ARN for an EC2 Instance and an IAM Role:<br>

arn:aws:ec2:us-east-1:123456789012:instance/i-00c07e4f8c9affca3:<br>

arn:aws:iam::123456789012:role/admin-role<br><br>

Trivia - ARNs almost always begin with "arn:aws:".  The second field is called the partition.  Most AWS customers are in the AWS partition, but there are several other partitions, including GovCloud (aws-us-gov), AWS China Region (aws-cn), and a handful of other Top Secret partitions built for the US Government.  For instance, Chinese Law requires AWS China to operate in partnership with Chinese companies and not solely by Amazon. <br><br>

AWS requires the use of an Access Key and Secret Key (and an optional Session Token) to authenticate calls to the AWS APIs.  These keys sign the request and identify which user or role and which AWS account the request comes from.  We will discuss credentials in more detail in a later room.<br><br>

Multiple AWS Accounts can be members of an AWS Organization.  This is typically done for management and consolidated billing purposes.  Typically there is no implicit trust across accounts in an organization; however, AWS has introduced some new features that blur the boundary and allow the organization management account to modify and manage the member accounts.</p>

<br>

![image](https://github.com/user-attachments/assets/237b5e04-7661-4da7-877f-424efde6449a)

<br>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 2.1. <em>Complete this room and move on to IAM Principals</em><br><a id='2.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center">
<img width="1000px" src="https://github.com/user-attachments/assets/afacb8b5-3bf8-4afc-a2c4-ba022a964b8c"><br>
<img width="1000px" src="https://github.com/user-attachments/assets/7a96407f-a9ca-4117-b993-e8e9a66390cb"></p>

<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>


<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| April 22, 2025    | 351      |     266ᵗʰ    |      6ᵗʰ     |     50ᵗʰ    |     2ⁿᵈ    |  96,337  |    678    |     59    |

</div>


<br>

<p align="center"> Global All Time: 266ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/f58dcb58-9e44-49d5-8d4f-47da80208d3a"> </p>

<p align="center"> Brazil All Time:   6ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/01d0931c-485d-4087-a725-8eef9d62a84f"> </p>

<p align="center"> Global monthly:    50ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/34359231-0dc8-4ce3-a750-8174091d1fdd"> </p>

<p align="center"> Brazil monthly:    2ⁿᵈ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/fadbb87e-a446-4eb1-8a50-9f83c2739b1c"> </p>

<br>

<p align="center"> Weekly League: 14ᵗʰ Gold<br><br><img width="1000px" src="https://github.com/user-attachments/assets/b3c46ae3-055b-432d-ae0e-a469a323377a"> </p>

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/tryhackme">tryhackme</a>, <a href="https://tryhackme.com/p/wesladd">wesladd</a> and <a href="https://tryhackme.com/p/jcfarris">jcfarris</a> for investing your time and effort to develop this challenge so that I could sharpen my skills!</p> 

