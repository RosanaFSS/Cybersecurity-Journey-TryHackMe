<h1 align="center"><a href="https://tryhackme.com/room/entraidintroduction">MS Entra ID: Hybrid Identities</a></h1>
<h3 align="center">Defending Azure Learning Path &nbsp;|&nbsp; Microsot Entra ID</h3>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/c8ae3f01-1e14-44e3-969d-5f3c854514ab"><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20JAN%2020-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>

<h2>Task 1 . Introduction</h2>
<h3>What Is Hybrid Identity?</h3>
<p>This is an approach that combines both on-premises and cloud-based identity management to provide a unified, secure, and seamless experience for users accessing various resources. It allows organizations to integrate their existing on-premises Active Directory (AD) infrastructure with cloud-based identity services like Microsoft Entra ID.<br>

With Microsoft hybrid identity a unified user identity is created across on-premises and cloud-based environments for authentication and authorization of all resources, regardless of the identity's location.<br>

<strong>Hybrid Identity</strong> consists of two fundamental concepts: Provisioning and Synchronization.<br>

- <strong>Provisioning</strong> is the process of:<br>- Creating an object based on certain conditions<br>- Keeping the object up-to-date<br>- Deleting the object when conditions are no longer met<br><br>
- <strong>Synchronization</strong> is the process of:<br>Ensuring identity information for on-premises users and groups is the same as the identity information in the cloud</p>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/1ca2a165-30c7-4aa4-9b64-c454e3f9942d"><br>This image and all the theoretical content of the present article is TryHackMe´s property.<br></h6>

<p>The two concepts above are the pillars of any <strong>cloud transformation</strong> project and are significant in every organization's transition to the cloud. In this room, we will mainly focus on <strong>identity synchronization</strong> concepts and how they are achieved in Microsoft Entra.</p>

<p><em>Answer the questions below</em></p>

<p>1.1. <em>What is the concept of creating a common user identity regardless of the identity's location being called?</em><br>
<code>hybrid identity</code></p>

<p>1.2. <em>Which hybrid identity concept deals with creating identity objects based on certain conditions?</em><br>
<code>provisioning</code></p>

<br>
<h2>Task 2 . Microsoft Entra Connect</h2>
<h3>What Is Microsoft Entra Connect?</h3>
<p><strong>Microsoft Entra Connect</strong> is a Microsoft tool designed to connect on-premises Active Directory environments with Microsoft Entra ID. It allows for the synchronization of identities and provides single sign-on capabilities for users across on-premises and cloud services.</p>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/68bb254e-4809-4a9a-a8bd-7c83515c7db6"><br>This image and all the theoretical content of the present article is TryHackMe´s property.<br></h6>

<h3>Why Microsoft Entra Connect?</h3>
<p>The objective is to enhance productivity by establishing a unified identity for accessing both cloud and on-premises resources. From the users' perspectives, the physical location of their identities should be irrelevant. They should be able to use the <strong>same login credentials</strong> for both cloud and on-premises environments.</p>

<h4>Key Features</h4>
<p>Here are some key concepts and features of <strong>Microsoft Entra Connect</strong>. In upcoming tasks, we will explore these further.<br>

- <strong>Synchronization</strong>: Responsible for creating users, groups, and other objects. Ensures identity information for on-premises users and groups matches the cloud. This synchronization also includes <strong>password hashes</strong>.<br>
- <strong>Password Hash Synchronization (PHS)</strong>: This sign-in method synchronizes the hash of a user's on-premises AD password with Microsoft Entra ID. Instead of storing actual passwords in Entra ID, Password Hash Sync synchronizes a hash of the user's on-premises Active Directory password to Entra ID. This enables users to use the same password for both on-premises and cloud-based services.<br>
- <strong>Pass-through Authentication (PTA)</strong>: This sign-in method allows users to use the same password on-premises and in the cloud but doesn't require the additional infrastructure of a federated environment. Users sign in to the Entra ID sign-in page with their on-premises username and password. Pass-through authentication validates the credentials against the on-premises Active Directory.<br>
- <strong>Federation integration</strong>: A Federation is a collection of domains that have established trust. A typical federation might include several organizations that have established a trust for shared access to resources. With the Federation integration option of Microsoft Entra Connect, a hybrid environment can be configured using an on-premises Active Directory Federated Service (ADFS) infrastructure. This sign-in method ensures that all user authentication occurs on-premises and allows administrators to implement more rigorous levels<br>

After this introduction, let's see how each feature works and what their roles are in a hybrid identity environment.</p>

<p><em>Answer the questions below</em></p>

<p>2.1. <em>What is the name of the <strong>identity synchronization</strong> tool deployed on-premises?</em><br>
<code>Microsoft Entra Connect</code></p>

<p>2.2. <em>Which hybrid identity concept deals with creating identity objects based on certain conditions?</em><br>
<code>Password Hash Synchronization</code></p>

<br>
<h2>Task 3 .Password Hash Synchonization (PHS)</h2>
<p><strong>Password hash synchronization</strong> is a method for signing in that supports hybrid identity where Microsoft Entra Connect synchronizes password hashes to Entra ID for cloud authentication. This feature builds on the directory synchronization functionality that Microsoft Entra Connect Sync provides when you want to allow sign-in to Microsoft Entra services such as Microsoft 365 using the same password as your on-premises Active Directory account. It is the most widely used method by organizations to synchronize an on-premises Active Directory with Entra ID since it enables users to authenticate directly against Entra ID without needing access to on-premises infrastructure.</p>

<h3>How Does It Work?</h3>
<p>A <strong>hash</strong> value  is a result of a one-way mathematical function (the hashing algorithm). There is no method to revert the result of a one-way function to the plain text version of a password. All users and a hash of the password hashes are synchronized from the on-prem to Entra ID. Extra security processing is applied to the password hash before synchronising to the Microsoft Entra ID authentication service. However, clear-text passwords or the original hashes are not sent to the cloud, and built-in security groups (like domain admins) are also not synced to Entra ID. The <strong>hashes synchonization</strong> occurs every 2 minutes.  When an on-prem user wants to access an Azure resource, the authentication takes place on Entra ID, not on-prem.</p>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/b6584c17-271e-4118-9f71-e7e11abf32b5"><br><br><img width="900px" src="https://github.com/user-attachments/assets/eca2d939-3b2c-4c8c-a947-44d3f1f0645c"><br>This images and all the theoretical content of the present article is TryHackMe´s property.<br></h6>

<h3>Why Use PHS?</h3>
<p>The main advantage of using PHS in a hybrid identity scenario is that users can use the same username and password that they use on-premises. This improves productivity and reduces helpdesk costs due to lower identity management overhead.</p>

<h3>Pivoting</h3>
<p>From an attacker's perspective, this scenario is a potential pivoting opportunity. We will look further into the details of this attack surface later, but let's note it here.</p>

<p><em>Answer the questions below</em></p>

<p>3.1. <em>With PHS, where is authentication performed?</em><br>
<code>In the cloud</code></p>

<p>3.2. <em>What value is a result of a one-way mathematical function that cannot be reverted?</em><br>
<code>hash</code></p>

<p>3.3. <em>Is single sign-on possible with PHS? (Yea/Nay)</em><br>
<code>Yea</code></p>


<h2> Task 4 . Pass-through Authentication (PTA</h2>
<p>Similar to Password Hash Synchronization (PHS), <strong>Pass-through Authentication (PTA)</strong> provides the same benefits of the cloud authentication experience to users, but with a main difference. In PTA, authentication is performed against an on-premises Active Directory environment instead of the cloud. In this case, one or more on-prem servers are needed to run <strong>authentication agents</strong>.  From a network security perspective, authentication agents only require outbound communication using these standard ports (port 80 and port 443). You don't need to open inbound ports on your firewall. This was not the case with the PHS authentication option.</p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/b573157f-fcf7-43c1-99d8-f5f276675888"><br>This image and all the theoretical content of the present article is TryHackMe´s property.<br></h6>

<h3>Why Use Pass-Through Authentication (PTA)?</h3>
<p>Certain organizations may want to enforce their on-premises security and password policies. Likewise, some organizations may have policies in place stating that hashes of passwords shall not be synced to the cloud due to data residency restrictions. In such cases, PTA would be the right authentication option.</p>

<h3>Decision Tree</h3>
<p>Here is a flowchart to help you determine which choice to make and at what time.</p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/1285731d-9d2b-469d-8934-85ec60960b0b"><br>This image and all the theoretical content of the present article is TryHackMe´s property.<br></h6>

<p>From a security standpoint, administrators must treat the server running the PTA agent as if it were a domain controller. The PTA agent servers should be hardened to the same security standards as domain controllers.</p>

<p><em>Answer the questions below</em></p>

<p>4.1. <em>When using PTA, is authentication performed on-premises or in the cloud?</em><br>
<code>on-premises</code></p>

<p>4.2. <em>Is PTA an agent-less authentication option? (Yea/Nay)</em><br>
<code>Nay</code></p>

<p>4.3. <em>PTA authentication agents require which communication access to Entra ID? Inbound/Outbound?</em><br>
<code>outbound</code></p>

<br>
<h2>Task 5 . Seamless SSO</h2>
<p>Microsoft Entra seamless single sign-on (seamless SSO) automatically signs users in from their network-connected corporate desktops. Seamless SSO provides users easy access to cloud-based applications without needing other on-premises components.<br>

The key point with this scenario is that organizations keep passwords on-premises. They do not leave the organization's internal boundaries. Also, when users try to log in to cloud applications using a domain-joined machine, they will not be prompted with an additional login page.</p>

<h3>How Does Seamless SSO Work?</h3>
<p>

- Entra Connect creates a computer account (<strong>AZUREADSSOACC</strong>) representing Entra ID inside the on-premises Active Directory during setup.<br>
- The AZUREADSSOACCT computer account’s <strong>Kerberos decryption key</strong> is shared with Entra ID.<br>
- When the user visits the Entra ID sign-in page, JavaScript is used to request a <strong>Kerberos ticket</strong> for the computer account.<br>
- The user's machine, accessible to the domain controller, acquires the Kerberos ticket.<br>
- The ticket includes the user's identity and is then forwarded to Entra ID.<br>
- Entra ID validates the ticket; if all is good, the user silently signs in to the cloud application.<br>
- No password is required.<br>
- Also, the on-prem computer doesn't need to be <strong>Entra ID joined</strong>, only domain-joined!<br>
- Endpoints need to be added to the <strong>intranet zone</strong>, which is done with group policies.</p>

<h6 align="center"><img width="500px" src="https://github.com/user-attachments/assets/0a41cb58-626d-43e2-b8ba-94e62ef4b07b"><br>This image and all the theoretical content of the present article is TryHackMe´s property.<br></h6>

<h3>Important Security Best Practices For the AZUREADSSOACC Account</h3>
<p>

- The (<strong>AZUREADSSOACC</strong> computer account needs to be strongly protected for security reasons.<br>
- Only <strong>Domain Admins</strong> should be able to manage the computer account.<br>
- Ensure that <strong>Kerberos delegation</strong> on the computer account is disabled and that no other account in Active Directory has delegation permissions on the (<strong>AZUREADSSOACC</strong> computer account.<br>
- Store the computer account in an Organization Unit (OU) where they are safe from accidental deletions and where only Domain Admins have access.<br>
- The <strong>Kerberos decryption key</strong> on the computer account should also be treated as sensitive.<br>
- Roll over the Kerberos decryption key of the (<strong>AZUREADSSOACC</strong> computer account at least every 30 days.</p>

<p><em>Answer the questions below</em></p>

<p>5.1. <em>What service provides easy access to cloud-based applications without needing any other on-premises components?</em><br>
<code>seamless sso</code></p>

<p>5.2. <em>Which computer account does Entra Connect create during seamless SSO setup?</em><br>
<code> AZUREADSSOACC</code></p>

<p>5.3. <em>Does Seamless SSO only work with PTA, not with PHS? (Yea/Nay)</em><br>
<code>Nay</code></p>

<p>5.4. <em>As a security best practice, who should be able to manage the computer account?</em><br>
<code>Domain Admins</code></p>

<br>

<h2>Task 6 . Conclusion</h2>
<h3>Summary</h3>
<p>In this room, we have looked into hybrid identity and how Microsoft Entra Connect achieves a common identity for users by synchronizing on-premises and cloud identities. In addition, we discussed the specific authentication options for Microsoft Entra Connect. Specifically, we have covered the following topics:<br>

- Hybrid identity<br>
- Microsoft Entra Connect<br>
- Synchronizing on-premise and cloud identities<br>
- Password Hash Synchronization (PHS)<br>
- Pass-Through Authentication (PTA)<br>
- Seamless SSO<br>

<strong>Hybrid identity</strong> is a vast topic and may include nuances based on different cloud/on-premises architectures, topologies, and your organization's synchronization needs. If you want to explore this topic further, you can find more details and scenarios here.</p>

<p><em>Answer the question below</em></p>

<p>6.1. <em>I understand the <strong>hybridy identity</strong> and where <strong>Microsoft Entra Connect</strong> fits. I am ready for the MS Entra: External ID room.</em><br>
<code>No answer needed</code></p>

<br>
<h1 align="center">Walkthrough Completed</h1>


<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/c8c27ceb-ec7f-4e8c-a2f7-59e77af3b8ee"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/f1bfc6a7-afef-4669-930d-a81f25bea77b"></p>


<h1 align="center">My TryHackMe Journey ・ 2026, January</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|20     |Easy 🔗 - MS Entra ID: Hybrid Identities|19 |   82ⁿᵈ  |     3ʳᵈ    |      184ᵗʰ   |        2ⁿᵈ     |    140,971  |    1,069    |    88     |
|19     |Easy ⚙️ - Upload and Conquer          |18 |     81ˢᵗ  |     3ʳᵈ    |      181ˢᵗ   |        2ⁿᵈ     |    140,859  |    1,068    |    88     |
|18     |Easy 🔗 - MS Entra ID: Identities     |17 |     83ʳᵈ  |     3ʳᵈ    |      341ˢᵗ   |        3ʳᵈ     |    139,864  |    1,068    |    88     |
|18     |Easy ⚙️ - APT28: Initial Access       |17 |     84ᵗʰ  |     3ʳᵈ    |      341ˢᵗ   |        3ʳᵈ     |    139,752  |    1,067    |    88     |
|18     |Easy ⚙️ - Hidden Hooks                |17 |           |     3ʳᵈ    |              |                |             |    1,067    |    88     |
|17     |Easy 🔗 - MS Entra ID: Introduction   |17 |     83ʳᵈ  |     3ʳᵈ    |      359ᵗʰ   |        3ʳᵈ     |    139,657  |    1,067    |    88     |
|17     |Easy ⚙️ - APT28: Credential Access    |17 |           |     3ʳᵈ    |              |                |             |    1,067    |    88     |
|17     |Medium ⚙️ - Open Door                 |17 |           |     3ʳᵈ    |              |                |             |     1,067   |    88     |
|17     |Easy 🔗 - Offensive Security Intro    |16 |     87ᵗʰ  |     3ʳᵈ    |      504ᵗʰ   |        5ᵗʰ     |    139,099  |    1,067    |    88     |
|16     |Hard 🚩 - Spring                      |15 |     87ᵗʰ  |     3ʳᵈ    |      540ᵗʰ   |        4ᵗʰ     |    138,942  |    1,066    |    87     |
|14     |Insane 🚩 - Scheme Catcher            |13 |     87ᵗʰ  |     3ʳᵈ    |      534ᵗʰ   |        5ᵗʰ     |    138,822  |    1,065    |    87     |
|13     |Hard 🚩 - Breachblocker Unlocker      |12 |     86ᵗʰ  |     3ʳᵈ    |      526ᵗʰ   |        5ᵗʰ     |    138,732  |    1,064    |    87     |
|11     |Medium 🚩 - Azure: Eyes Wide Shut     |10 |     86ᵗʰ  |     3ʳᵈ    |      558ᵗʰ   |        5ᵗʰ     |    138,450  |    1,063    |    86     |
|8      |Medium ⚙️ - Phishing Unfolding        | 7 |     86ᵗʰ  |     3ʳᵈ    |      508ᵗʰ   |        4ᵗʰ     |    138,372  |    1,062    |    84     |
|8      |Easy ⚙️ - Introduction to Phishing    | 7 |     96ᵗʰ  |     3ʳᵈ    |    2,479ᵗʰ   |       32ⁿᵈ     |    137,117  |    1,062    |    84     |
|8      |Medium 🔗 - KaffeeSec - SoMeSINT      | 7 |     98ᵗʰ  |     3ʳᵈ    |    2,847ᵗʰ   |       38ᵗʰ     |    137,052  |    1,062    |    84     |
|7      |Hard 🚩 - Hack Back                   | 6 |     98ᵗʰ  |     3ʳᵈ    |    2,798ᵗʰ   |       37ᵗʰ     |    136,908  |    1,061    |    84     |
|7      |Hard 🚩 - Dead End?                   | 6 |     99ᵗʰ  |     3ʳᵈ    |    2,924ᵗʰ   |       37ᵗʰ     |    136,788  |    1,060    |    84     |
|6      |Easy 🔗 - Linux Strength Training     | 5 |     98ᵗʰ  |     3ʳᵈ    |    3,172ⁿᵈ   |       47ᵗʰ     |    136,608  |    1,059    |    84     |
|4      |Medium 🚩 - JVM Reverse Engineering   | 3 |     96ᵗʰ  |     3ʳᵈ    |    3,031ˢᵗ   |       46ᵗʰ     |    136,450  |    1,058    |    84     |
|3      |Medium 🚩 - Carrotbane of My Existence| 2 |     96ᵗʰ  |     3ʳᵈ    |    3,468ᵗʰ   |       49ᵗʰ     |    136,150  |    1,057    |    84     |
|2      |Easy 🔗 - Learn Rust                  | 1 |     96ᵗʰ  |     3ʳᵈ    |    5,152ⁿᵈ   |       67ᵗʰ     |    136,030  |    1,056    |    84     |

</h6></div><br>

<p align="center">Global All Time:     82ⁿᵈ<br><img width="250px" src="https://github.com/user-attachments/assets/f15c05ca-8ca8-424d-b9be-26037e05ba09"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/0ae28950-9a26-4837-902a-4b4b8f06b010"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/006c1679-0f6b-4de0-b726-a867ff49f065"><br><br>
                  Global monthly:     184ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/ddd69014-1bf9-4087-a9d1-c6f57da33857"><br><br>
                  Brazil monthly:       2ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/7ce0c8d6-0270-4376-8484-36293d27d1e2"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
