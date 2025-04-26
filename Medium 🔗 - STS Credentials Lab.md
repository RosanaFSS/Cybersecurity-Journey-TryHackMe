<p align="center">April 26, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{355}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/13f4c27b-45b5-4246-be5f-de6d1805ed82" alt="streak"><br></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{STS Credentials Lab}}$$</h1>
<p align="center"><em>Learn how to assume roles and get temporary credentials.</em>.<br>
It is classified as a medium-level walkthrough.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/stscredentialslab">here</a>.</p>


<p align="center"> <img width="1000px" src=""> </p>

<br>
<br>

<h2>Task 1 . Introduction to STS Credentials</h2>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 1.1. <em>My AttackBox and CloudShell are ready to go!.</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 2 . Accessing the environment</h2>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 2.1. <em>Generate environment or set up your credentials</em><br><a id='2.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>


<h2>Task 3 . Create the Padawan User</h2>
<p>We will start by creating the IAM user "padawan". IAM Users are the easiest way to grant access to a system outside of your cloud environment. </p>

<br>

![image](https://github.com/user-attachments/assets/fd16a750-9bbc-4fea-b9ea-222a2d0ec8bf)

<br>

<p>Run these commands in your CloudShell:</p>

<br>

```bash
[cloudshell-user@ip-10-1-94-78 ~]$ aws iam create-user --user-name padawan
{
    "User": {
        "Path": "/",
        "UserName": "padawan",
        "UserId": "AIDAZOHYLBQBMPAQSXF3G",
        "Arn": "arn:aws:iam::123456789012:user/padawan",
        "CreateDate": "2021-10-30T22:48:36+00:00"
    }
}
```

<br>


<p>Next, grant that user some permission by adding them to the padawans group.</p>

<br>

```bash
aws iam add-user-to-group --user-name padawan --group-name padawans
```

<br>

<p>Now that you have created the user identity, we will create the access keys for use on your AttackBox in the next task. Save the output of the create-user command so you can validate your identity in a later task.</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

```bash
aws iam list-groups-for-user --user-name padawan
```

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 3.1. <em>What are the first four letters of the GroupId of the padawans group?</em><br><a id='3.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>


<h2>Task 4 . Create an Access Key for the Padwan</h2>
<p>Having created the identity and granted permissions (by adding the user to the group) you have configured authorization for this user. In this task we configure the ability to authenticate to the AWS APIs.<br><br>

To use the Padawan user on the AttackBox, you'll need to generate an access key like so:</p>

<br>

```bash
[cloudshell-user@ip-10-1-94-78 ~]$ aws iam create-access-key --user-name padawan
{
    "AccessKey": {
        "UserName": "padawan",
        "AccessKeyId": "AKIAZOEXAMPLE",
        "Status": "Active",
        "SecretAccessKey": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "CreateDate": "2021-10-30T22:48:53+00:00"
    }
}
```

<br>

<p>Using the information above, go to your AttackBox and issue these two commands:</p>

<br>


```bash
export AWS_SECRET_ACCESS_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
export AWS_ACCESS_KEY_ID=AKIAZOEXAMPLE
```

<br>

<p>Like running <code>aws configure</code>, setting these environment variables tells the AWS CLI what credentials to use. Next we will verify you're using the right set of credentials.</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 4.1. <em>What is the character length of the SecretAccessKey?</em><br><a id='4.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 5 . Validate Your Status on the AttackBox</h2>
<p>The <code>aws sts get-caller-identity</code> command is the AWS equivalent of the Unix command <code>whoami</code>. You should use it regularly to make sure you know which account and user/role you're working with.</p>

<br>


```bash
user@machine$ aws sts get-caller-identity
{
    "UserId": "AIDAZOHYLBQBMPAQSXF3G",
    "Account": "123456789012",
    "Arn": "arn:aws:iam::123456789012:user/padawan"
}
```

<br>

<p>The UserId you see here should match the one from Task 2.  Hold on to the account ID returned above. You will need it for the next task when our padawan user assumes a new role with more permissions.</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 5.1. <em>I can confirm I'm using the "padawan" user.</em><br><a id='5.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>


<h2>Task 6 . Assume the Role of Jedi Master</h2>
<p>Now that you've used long-term access keys from an IAM User, we are going to generate short-term keys for an IAM Role. In many attack scenarios, you'll be leveraging these short term credentials, so it's important to understand the basics of these role credentials.<br><br>

The next step is to assume the role of Jedi Master.</p>

<br>

![image](https://github.com/user-attachments/assets/0f8022d9-cdd3-4dad-8478-211d3f73a96a)

<br>

<p>To do this, you'll need three things:<br>

- Permission to assume the "jedi" role. This is provided by the policy attached to the "padawans" IAM Group. Refer to Task 2 where we added the user to the padawans IAM Group.<br>
- The Amazon Resource Name (ARN) of the Role you want to assume. This will be <code>arn:aws:iam::Account-ID-From-TASK4:role/jedi</code><br>
- A Role Session Name - This string will appear in CloudTrail logs and help administrators distinguish who or why a specific role was assumed. For this we shall use the name of someone who almost became a Jedi master.</p>

<br>

```bash
user@machine$ aws sts assume-role --role-arn arn:aws:iam::Account-ID-From-TASK4:role/jedi --role-session-name Ahsoka
{
    "Credentials": {
        "AccessKeyId": "ASIAZOHYLBQBDEXAMPLE",
        "SecretAccessKey": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "SessionToken": "IQoJb3JpZ2luX2VjEEgaCXVzLWVhc3QtMSJGMEQCIFTdMvEsoMLGygfmP5c9mjfWuUXAtro5oODwxSGgY7ncAiBvamMVsFfdaUDKjjDs/
        ucCGqaydbZYDRy2XqEcigBzBSqbAgjg//////////8BEAAaDDY0OTA2MDg3OTM2MiIM7DMiASHRTnXU+SJrKu8B+bTZr6DmOIKMai10A
        k2cnRQrcpvlfFLKQqhAOkfX6s3BJR0P6l3XNa7Bs3buoajzYlTvyBYw/1Bnn/DQ1yj+TZLsoM29pORwFbcAefaxUZjrXrcZORT97EeVj1ZrDw/
jFwQCS3Su2ETpBCNmbX4yTlNEUX8RWlRlCYRBSLbSa9ZfvGfVqJjG/
        7X8Xvh3R5E3IUjTcn/0pksOavXawxbRciDt0KKw87xFu1nzoAb1uj5u+drO1R1SWZBwgmDbYLGF2QrKMvs8U1NwTcBb0YAhK4JGKeOmL      
LpSNWsUrYXmapSzCwb8gfX9RDg0wF/0ilswpqb3iwY6ngFqjjSgiD+rikPTE9xYNMFdexpJ712iKHcnbjJU7VAnUv93RYZtZycj2yCTO9IwhJa8O484mxIMDg0VBV/
        lU5zkXsoihp0Z9dfFgvoPOOeKkeA5FYuTADK4iSR4YK6pEMenU5j8SeHt8aoR3WdYf3uObs0Zyts0XYx9hxLYXWayRNp7TushFaECg
        nkQRJYulS5DykRHiib5PfP/Xjjcrw==",
        "Expiration": "2021-10-31T00:20:06+00:00"
    },
    "AssumedRoleUser": {
        "AssumedRoleId": "AROAZOHYLBQBOHPGGIRC2:Ahsoka",
        "Arn": "arn:aws:sts::123456789012:assumed-role/jedi/Ahsoka"
    }
}
```

<br>

<p>Now take the output of the <code>assume-role</code> command and set the three AWS CLI environment variables required to use temporary credentials for the Role (rather than the user):</p>

<br>

```bash
export AWS_SECRET_ACCESS_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
export AWS_ACCESS_KEY_ID=ASIAZOHYLBQBDEXAMPLE
export AWS_SESSION_TOKEN=IQoJb3JpZ2luX2VjEEgaCXVzLWVhc3QtMSJGMEQCIFTdMvEsoMLGygfmP5c9mjfWuUXAtro5oODwxSGgY7ncAiBvam
MVsFfdaUDKjjDs/ucCGqaydbZYDRy2XqEcigBzBSqbAgjg//////////8BEAAaDDY0OTA2MDg3OTM2MiIM7DMiASHRTnXU+SJrKu8B+bTZr6DmOIKMa
i10Ak2cnRQrcpvlfFLKQqhAOkfX6s3BJR0P6l3XNa7Bs3buoajzYlTvyBYw/1Bnn/DQ1yj+TZLsoM29pORwFbcAefaxUZjrXrcZORT97EeVj1ZrDw/
jFwQCS3Su2ETpBCNmbX4yTlNEUX8RWlRlCYRBSLbSa9ZfvGfVqJjG/7X8Xvh3R5E3IUjTcn/
0pksOavXawxbRciDt0KKw87xFu1nzoAb1uj5u+drO1R1SWZBwgmDbYLGF2QrKMvs8U1NwTcBb0YAhK4JGKeOmLLpSNWsUrYXmapSzCwb8gfX9RDg0wF/
0ilswpqb3iwY6ngFqjjSgiD+rikPTE9xYNMFdexpJ712iKHcnbjJU7VAnUv93RYZtZycj2yCTO9IwhJa8O484mxIMDg0VBV/lU5zkXsoihp0Z9dfFgv
oPOOeKkeA5FYuTADK4iSR4YK6pEMenU5j8SeHt8aoR3WdYf3uObs0Zyts0XYx9hxLYXWayRNp7TushFaECgnkQRJYulS5DykRHiib5PfP/Xjjcrw==
```

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 6.1. <em>How many minutes are your session credentials good for?</em>Hint : <em>The API call will return the expiration time in UTC. If you need to see the current time in UTC, you can run `date` on your CloudShell session.</em><br><a id='6.1'></a>
>> <strong><code>__________________________________</code></strong><br>
<p></p>

<br>

> 6.2. <em>How many AWS CLI environment variables were required to be set?</em><br><a id='6.1'></a>
>> <strong><code>__________________________________</code></strong><br>
<p></p>

<br>
<br>


<h2>Task 7 . Validate Your Newly Found Powers</h2>


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
