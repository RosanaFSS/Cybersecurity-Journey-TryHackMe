<p align="center">April 26, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{355}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/007808ba-c4d0-4c88-ac0e-e8f044734a4e" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/13f4c27b-45b5-4246-be5f-de6d1805ed82" alt="streak"><br></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{The Quest for Least Privilege}}$$</h1>
<p align="center"><em>Learn how to scope an IAM Policy down to only the necessary actions.</em>.<br>
It is classified as a medium-level walkthrough.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/thequestforleastprivilege">here</a>.</p>


<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/11b2517e-633a-478e-ba4b-159be32ac81f"> </p>

<br>
<br>

<h2>Task 1 . Introduction</h2>

<p>One of the most common tasks for anyone working in AWS IAM is to scope IAM Policies to include only the necessary privileges required to complete a task. This is commonly referred to as following the Principle of Least Privilege. In this room, we will take a broadly scoped rule and whittle down access to allow the policy to do three things:

- Audit all EC2 Settings<br>
- Launch machines in the Singapore Region<br>
- Access a specific corporate S3 bucket.<br><br>

We’ll start with the default AdministratorAccess policy:</p>

<br>

```bash
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "*",
            "Resource": "*"
        }
    ]
}
```

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 1.1. <em>If you are denied access while you have this policy, what type of policy is blocking you?</em>Hint : <em>A type of organization policy to manage permissions in your organization.</em><br><a id='1.1'></a>
>> <strong><code>Service Control Policy</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 2 . Accessing the Environment</h2>

<p>[ ... ]</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 2.1. <em>Generate environment or set up your credentials.</em><br><a id='2.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 3 . Limiting by Service</h2>
<p>The requirement is to allow access to EC2 and S3 only. To do that, you’ll need to restrict the actions by service. That would look like this:</p>

<br>

```bash
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PermitEC2",
            "Effect": "Allow",
            "Action": ["ec2:*", "XXX:*"],
            "Resource": "*"
        }
    ]
}
```

<br>

<p>However, we probably want to break this out to support two different resources, so we’ll do that now.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 3.1. <em>What action is needed in place of XXX?</em><br><a id='3.1'></a>
>> <strong><code>S3</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 4 . Limiting by Read vc Modify</h2>
<p>However, we probably want to break this out to support two different resources, so we’ll do that now.</p>

<br>

```bash
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PermitEC2",
            "Effect": "Allow",
            "Action": "ec2:*",
            "Resource": "*"
        },
        {
            "Sid": "Permit S3",
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "*"
        }
    ]
}
```

<br>

<p>To make this a read-only audit role, We need to limit the policy to only List/Describe/Get actions:</p>

<br>

```bash
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PermitEC2",
            "Effect": "Allow",
            "Action": [ "ec2:YYY*", "ec2:Get*" ],
            "Resource": "*"
        },
        {
            "Sid": "Permit S3",
            "Effect": "Allow",
            "Action": [ "s3:Get*", "s3:XXX*" ],
            "Resource": "*"
        }
    ]
}
```

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

>4.1. <em>What is the redacted EC2 Action required in place of YYY?</em>Hint : <em>When in doubt the AWS documentation for Actions, resources, and condition keys can be super helpful - https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html</em><br><a id='3.1'></a>
>> <strong><code>Describe</code></strong><br>
<p></p>

<br>

>4.2. <em>What is the redacted S3 Action required in place of XXX?</em>Hint : <em>When in doubt the AWS documentation for Actions, resources, and condition keys can be super helpful - https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html</em><br><a id='3.1'></a>
>> <strong><code>List</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 5 . Enumerating specific resources</h2>
<p>Finally, we’ll limit this policy to a subset of resources using wildcards and prefixes. We start with a new statement to allow all actions on instances in Singapore.<br><br>

We also need to add two resources to the S3 statement. The first statement refers to all the objects in the bucket and the second to the bucket itself.</p>

<br>


```bash
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PermitEC2",
            "Effect": "Allow",
            "Action": [
            	"ec2:Describe*",
            	"ec2:Get*"
            ],
            "Resource": "*"
        },
        {
            "Sid": "Singapore",
            "Effect": "Allow",
            "Action": [
            	"ec2:*"
            ],
            "Resource": "arn:aws:ec2:XXXX:*:instance/*"
        },
        {
            "Sid": "Permit S3",
            "Effect": "Allow",
            "Action": "s3:Get*",
            "Resource": [
            	"arn:aws:s3:::my_corporate_bucket/*",
            	"arn:aws:s3:::my_corporate_bucket"
            ]
        }
    ]
}
```

<br>

<p>There are two resources needed for the S3 statement. The first applies the s3:Get* actions to the objects in the bucket, while the second applies to the bucket itself.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

>5.1. <em>What is the element needed in place of XXXX to represent the AWS Region (Singapore)?</em>Hint : <em>It’s the regional identifier.</em><br><a id='3.1'></a>
>> <strong><code>ap-southeast-1</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/4dad797e-34e6-4610-882d-3e85256694fd)

<br>
<br>


<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center">
<img width="1000px" src="https://github.com/user-attachments/assets/335c04be-1dc5-4f86-8f71-625d98751153"><br>
<img width="1000px" src="https://github.com/user-attachments/assets/919c38bc-60dc-495c-8ceb-dccc7eda65af"></p>

<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>


<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| April 26, 2025    | 355      |     254ᵗʰ    |      6ᵗʰ     |     50ᵗʰ    |     2ⁿᵈ    |  97,337  |    687    |     59    |

</div>

<br>

<p align="center"> Global All Time:  254ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/93ee117c-f5d5-4034-a5ae-62a242bc2482"> </p>

<p align="center"> Brazil All Time:    6ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/bf547bea-c2c5-481b-a5fd-cfb6e5395d5d"> </p>

<p align="center"> Global monthly:    50ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/51837972-3297-41ac-a185-762dacba92a8"> </p>

<p align="center"> Brazil monthly:    2ⁿᵈ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/e4e2f957-1da4-417d-b798-f061e3a51a1d"> </p>

<br>
<br>

<p align="center"> Weekly League:    5ᵗʰ Gold<br><br><img width="1000px" src="https://github.com/user-attachments/assets/527a9117-2669-42f4-bcb2-f59ccad53cb6"> </p>

<br>
<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/tryhackme">tryhackme</a> and <a href="https://tryhackme.com/p/jcfarris">jcfarris</a> for investing your time and effort to develop this challenge so that I could sharpen my skills!</p> 
