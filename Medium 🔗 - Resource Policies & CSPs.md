<p align="center">April 26, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{355}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/79cce19b-8806-489b-8b30-eaa78baed5ce" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/13f4c27b-45b5-4246-be5f-de6d1805ed82" alt="streak"><br></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Resource Policies and CSPs}}$$</h1>
<p align="center"><em>Learn how AWS resources can have their own permissions.</em>.<br>
It is classified as a medium-level walkthrough.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/resourcepoliciesscps">here</a>.</p>


<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/cf612069-cf5f-4f7f-8086-6c410b53f885"> </p>

<br>
<br>

<h2>Task 1 . Other Policy Types</h2>

<p>While 80% of the time when working with AWS you'll be using IAM Policies, there are two other types of policies you need to know about. They use the same statement structure as an IAM Policy but are attached to resources or accounts to affect how access is authorized.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 1.1. <em>Let's get started...</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 2 . Accessing the Environament</h2>

<p>[ ... ]</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 2.1. <em>Generate environment or set up your credentials.</em><br><a id='2.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 3 . Resource Policies</h2>

<p>IAM Policies are attached to a specific Principal and define the resources the Principal can act on whereas Resource Policies are attached to a resource and define the Principals that can act on the resource.  Many resource types can have Resource Policies, and resource policies are how things become public in AWS.<br><br>

For example, you can attach Resource-based Policies to:<br>

- S3 Buckets<br>
- KMS Keys<br>
- SQS Queues<br>
- SNS Topics<br>
- AWS Lambda<br>
- Secrets Manager Secrets<br>
- IAM Roles - yes, an assume role trust policy is a resource policy since it defines the Principal who can act.</p>

<p>The command to apply a resource policy varies based on the service. S3 buckets are one of the most common use cases for Resource Policies. For demonstration purposes, we've created a public S3 bucket in another TryHackMe account. That bucket is creatively named "tryhackme-public-bucket". The Bucket Policy for the bucket is:</p>

<br>

```bash
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Make Object Readable",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::tryhackme-public-bucket/*"
    },
    {
      "Sid": "Make Bucket Attributed World Readable",
      "Effect": "Allow",
      "Principal": {
        "AWS": "*"
      },
      "Action": [
        "s3:Get*",
        "s3:ListBucket"
      ],
      "Resource": "arn:aws:s3:::tryhackme-public-bucket"
    }
  ]
}
```

<br>

<p>In the case of S3, there are two AWS resources involved: the Bucket and the Objects in the bucket. The first statement allows anyone ("Principal": "*") to GetObject on all the objects in the bucket (arn:aws:s3:::tryhackme-public-bucket/*). The second statement applies only to the bucket itself (arn:aws:s3:::tryhackme-public-bucket) and allows anyone to get the attributes of the bucket (s3:Get*), and to list the objects in the bucket (s3:ListBucket).<br><br>

Give it a try. Run this command from your attack box or cloud-shell session:</p>

<br>

```bash
aws s3api get-bucket-policy-status --bucket tryhackme-public-bucket
```

<br>

<p>Now try and list the files in the bucket:</p>

<br>

```bash
aws s3 ls tryhackme-public-bucket
```

<br>

<p>Resource Policies also apply to whom can invoke a Lambda function. We'll cover Lambda in a future module, but try executing this Lambda, and then look at the output file:</p>

<br>

```bash
aws lambda invoke --function-name arn:aws:lambda:us-east-1:019181489476:function:TryHackMe-time time && cat time | jq -r
```

<br>

<p>Now try looking at the policy for that function:</p>

<br>

```bash
user@machine$ aws lambda get-policy --function-name arn:aws:lambda:us-east-1:019181489476:function:TryHackMe-time --query Policy --output text | jq
{
  "Version": "2012-10-17",
  "Id": "default",
  "Statement": [
    {
      "Sid": "THM-CommonResources-PublicLambdaGetPolicyPermission-1H4ZWNO1H6SFF",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "lambda:GetPolicy",
      "Resource": "arn:aws:lambda:us-east-1:019181489476:function:TryHackMe-time"
    },
    {
      "Sid": "THM-CommonResources-PublicLambdaInvokePermission-1KE9NRSHANU6U",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "lambda:InvokeFunction",
      "Resource": "arn:aws:lambda:us-east-1:019181489476:function:TryHackMe-time",
      "Condition": {
        "StringEquals": {
          "aws:PrincipalOrgID": "o-ad4l00k0ts"
        }
      }
    }
  ]
}
```

<br>

<p>As you can see, the resource policy for this function allows anyone to run lambda:GetPolicy, and all members of the AWS Organization o-ad4l00k0ts to run lambda:InvokeFunction.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 3.1. <em>Try running the s3api command "get-bucket-ownership-controls" against the tryhackme-public-bucket. What is the ObjectOwnership value set to?</em>Hint : <em>The command you need is: aws s3api get-bucket-ownership-controls --bucket tryhackme-public-bucket</em><br><a id='3.1'></a>
>> <strong><code>BucketOwnerPreferred</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/a8510244-87ea-4017-8dd1-237b0509ba8d)



<br>

![image](https://github.com/user-attachments/assets/727ad54f-c9ab-41d9-93ed-287580120d95)


<br>

> 3.2. <em>ry invoking the Lambda function "TryHackMe-quote" in the same 019181489476 Account. What's the quote returned from the function?</em>Hint : <em>The command you need is: aws lambda invoke --function-name arn:aws:lambda:us-east-1:019181489476:function:TryHackMe-quote flag ; cat flag | jq -r</em><br><a id='3.2'></a>
>> <strong><code>Most heard comment at #reinvent 'dude, lambda is the coolest shit, ever' -- Werner Vogles 2014</code></strong><br>
<p></p>

<br>

<p>Executed the command line suggested in the hint.</p>

<br>

```bash
aws lambda invoke --function-name arn:aws:lambda:us-east-1:019181489476:function:TryHackMe-quote flag ; cat flag | jq -r
```

<br>


![image](https://github.com/user-attachments/assets/d3d262ec-3bd2-4cbf-8389-cb30b01a4895)

<br>
<br>

<h2>Task 4 . Service Control Policies</h2>

<p>Service Control Policies are a function of AWS Organizations. They exist outside of the AWS Account and are applied by the parent Organizations’ Management Account. They apply to all principals in the account, including the root user. <br><br>

Service Control Policies are leveraged by enterprise Security or Compliance teams to ensure that the corporate directives for cloud usage bind to even account administrators across an AWS Organization. They can be configured to prevent disabling CloudTrail (the AWS auditing service) or prevent using AWS services that the legal department has not vetted. They can also limit actions to specific roles so that only the global network administrator role is permitted to manage VPC Route Tables. <br><br>

Users in an AWS account cannot view the Service control policies applied to the account. Until recently, AWS didn’t even tell a user that was Denied an action if an SCP was the reason. However, some AWS Error messages will now indicate if an SCP denied an action.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 4.1. <em>What are the last four words of the error message you get when attempting to disable GuardDuty with this command?</em><code>aws guardduty delete-detector --detector-id `aws guardduty list-detectors --query DetectorIds --output text`</code><br><a id='4.1'></a>
>> <strong><code>with an explicit deny</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/323bbd51-c459-48d8-8d2f-dee3f4195653)

<br>
<br>

<h2>Task 5 . Summary</h2>
<p>Now that you know about IAM Principals, how a policy is formed and how SCPs and resource policies interact, let’s dive into how authentication works in AWS in the next room: IAM Credentials.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 5.1. <em>Talk to me about AWS Credentials...</em><br><a id='5.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center">
<img width="1000px" src="https://github.com/user-attachments/assets/9ca71d7b-f04e-4a06-b7d3-39a1baa85a02"><br>
<img width="1000px" src="https://github.com/user-attachments/assets/53906d59-f4c6-427c-93ef-679d0eb8aec4"></p>

<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>


<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| April 26, 2025    | 355      |     254ᵗʰ    |      6ᵗʰ     |     50ᵗʰ    |     2ⁿᵈ    |  97,337  |    686    |     59    |

</div>

<br>


<p align="center"> Global All Time:  254ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/e4642f7c-d704-499a-9014-c394b1f1f36a"> </p>

<p align="center"> Brazil All Time:    6ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/a160d53e-b22e-4838-a6a7-5a59b54aa091"> </p>

<p align="center"> Global monthly:    50ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/7ec726de-359e-485e-8592-d21c157f40e3"> </p>

<p align="center"> Brazil monthly:    2ⁿᵈ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/6b8e50f6-e589-4524-bd86-ebfeabe6e250"> </p>

<br>


<br>

<p align="center"> Weekly League:    5ᵗʰ Gold<br><br><img width="1000px" src="https://github.com/user-attachments/assets/b0dcabfd-8284-4657-9252-b761c10c9d93"> </p>

<br>
<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/tryhackme">tryhackme</a> and <a href="https://tryhackme.com/p/jcfarris">jcfarris</a> for investing your time and effort to develop this challenge so that I could sharpen my skills!</p> 
