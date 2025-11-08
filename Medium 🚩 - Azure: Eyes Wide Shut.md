<h1 align="center">Azure: Eyes Wide Shut</h1>
<p align="center">2025, October 14<br>Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>526</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Azure challenge for cloud pentesters: Can you find the attack path and abuse it?</em><br>
<img width="60px" src="https://github.com/user-attachments/assets/975ffcd7-fd65-4f50-a6fa-01628efe7a91"><br>
Access it <a href="https://tryhackme.com/room/eyeswideshut">here</a>.<br>
<img width="1200px" src=""></p>

<h2>Task 1 . Introduction</h2>
<p>In this challenge, as a cloud pentester, you will <code>recon and attack an Azure tenant</code> to see if you can discover the attack path and move laterally to other resources.</p>

<h3>High-Level Guidance</h3>
<p>

- Perform <code>reconnaissance</code><br>
- Identify <code>attack paths</code><br>
- Determine your <code>coure of action</code><br>
- <code>Attack</code></p>

<h3>Rules of Engagement (ROE)</h3>
<p>Even if you can after successful privilege escalation or lateral movement:<br>

- Do NOT create additional users<br>
- Do NOT modify existing users<br>
- Do NOT temper with this Azure tenant by any means<br>
- This is a shared training tenant, and hence, respect the integrity of the environment<br>
- Leave it as you found it</p>

<h3>Start the Lab</h3>
<p>To start the challenge, click the <code>Cloud Details</code> button below. On the pop-up, click <code>Join Lab</code>. Then, click <code>Deploy Lab</code> in the <code>Actions</code> tab to deploy the cloud resources required for the challenge. Find your credentials in the  <code>Credentials</code> tab, click on  <code>Open Lab</code> and log in to the <a href="https://portal.azure.com/">Azure Portal</a>.<br><br>[ Cloud Details ]</p>

<p><em>Answer the question below</em></p>

<p>1.1. I have initiated the challenge deployment<br>
<code>No answer needed</code></p>

<p>
  
- <code>Cloud Details</code> > <code>Join Labs</code><br>
- <code>Actions</code> > <code>Deploy Lab</code><br>
- navigate to <code>Azure Portal</code><br>
- access Lab using <code>Username</code> and <code>Password</code> provided in the <code>Credential</code>´s section.</p>

<img width="396" height="206" alt="image" src="https://github.com/user-attachments/assets/3771bcd4-bdc3-44b8-aab5-4c1521b3bfca" />

<p>
  
- <code>Resources</code> > <code>View all resources</code></p>

<img width="1909" height="897" alt="image" src="https://github.com/user-attachments/assets/85ac21ca-9ca7-44bc-aa98-32f0e7621313" />

<p>
  
- <code>LinuxVM</code><br>
- <code>Connect</code> > <code>Connect</code><br>
- identify <code>azureuser</code><br>
- <code>Connect via Azure CLI</code><br>
- identify <code>ssh azureuser@20.42.104.23</code></p>


<img width="1894" height="901" alt="image" src="https://github.com/user-attachments/assets/766d720f-43de-4dc0-aef0-987a0f108685" />


<p>
  
- consider the discovery of <code>azureuser@20.42.104.23</code> in the reconnaissance --> <code>azureuser</code> : <code>WhereIsMyMind$#@!</code></p>


<img width="1916" height="892" alt="image" src="https://github.com/user-attachments/assets/e387843f-d756-42d8-93b5-d51652f63d2d" />


```bash
azureuser@LinuxVM:~$ curl "http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://management.azure.com/" -H "Metadata: true"
{"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6InlFVXdtWFdMMTA3Q2MtN1FaMldTYmVPYjNzUSIsImtpZCI6InlFVXdtWFdMMTA3Q2MtN1FaMldTYmVPYjNzUSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuYXp1cmUuY29tLyIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzkxNzE2YTlhLWY4ZmYtNDkwZi04ZjNhLWYyZTZkYTZlMTE2NS8iLCJpYXQiOjE3NjI2MTg1NDksIm5iZiI6MTc2MjYxODU0OSwiZXhwIjoxNzYyNzA1MjQ5LCJhaW8iOiJBV1FBbS84YUFBQUFFRlgrOHViamhicnRzc1BvZ1V4MlloTVFTVzM4N00yY0tFWTVZSVN5QUR3dXZBVjZMbWYyQ2hMTWg5VjI0NUpiQVRGcDBiaTN5UnI3TDdKdTdkUnpERHVZUDhIdE8wdXMyNzIzYnNYTmh3S0Z0Zk1NdXpNeXBwRnRkbGxkMys2SiIsImFwcGlkIjoiOWEyNjU2NzAtZDc3MS00YWI1LTkyZGYtYjVjN2EzODFjOWUwIiwiYXBwaWRhY3IiOiIyIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvOTE3MTZhOWEtZjhmZi00OTBmLThmM2EtZjJlNmRhNmUxMTY1LyIsImlkdHlwIjoiYXBwIiwib2lkIjoiNWE4ZTNkMzktNDcyMS00OTY0LThlNGEtOTY4NDMzOGQ5NzEzIiwicmgiOiIxLkFjb0FtbXB4a2ZfNEQwbVBPdkxtMm00UlpVWklmM2tBdXRkUHVrUGF3ZmoyTUJQNkFBREtBQS4iLCJzdWIiOiI1YThlM2QzOS00NzIxLTQ5NjQtOGU0YS05Njg0MzM4ZDk3MTMiLCJ0aWQiOiI5MTcxNmE5YS1mOGZmLTQ5MGYtOGYzYS1mMmU2ZGE2ZTExNjUiLCJ1dGkiOiJGQzh6YjhfaHhraWFVZjRUYl9ESEFBIiwidmVyIjoiMS4wIiwieG1zX2FjdF9mY3QiOiIzIDkiLCJ4bXNfZnRkIjoidnhkVEw0bjBuNFVoRWsxeGdoZ29QbUs5Q0dvVUtRQkVGQy1idnlJaG9lc0JkWE5sWVhOMExXUnpiWE0iLCJ4bXNfaWRyZWwiOiI3IDEwIiwieG1zX21pcmlkIjoiL3N1YnNjcmlwdGlvbnMvMTc0NjI5NGEtNWFhOC00Y2JiLTgyYTQtMTFlNzMxYjIwOTQyL3Jlc291cmNlZ3JvdXBzL3JnLTExMDgwODk0L3Byb3ZpZGVycy9NaWNyb3NvZnQuQ29tcHV0ZS92aXJ0dWFsTWFjaGluZXMvTGludXhWTSIsInhtc19yZCI6IjAuNDJMallCSmlPc1VvSk1MQktTVHc5RWpqUExXWGYzMGFmMDkxbkRXVFlUbFFsRU5Jd00yanZwSmgxM1hfWGM2M0R2NzRaaUFNQUEiLCJ4bXNfc3ViX2ZjdCI6IjMgOSIsInhtc190Y2R0IjoiMTcxMTk5MzE1OSJ9.XbxLltSDaMqpuWgM8OCmB6O82C4nQYZyLPPxyLEqHvpfiWSsJ-uget26TwnmaRc1X1zakUuzRN6wAWbAsE0V-Q2rzIRW1HtRBR3Hu-NyDTGmWgKbXp7U-CmPf-YpCGVUxy8eXqZPeIOtA0CVRGFK_66nrkL0rdXk97ultDybO-UML47yKWed3I4m3rp1E_SJKSnNEcCi6GW931n80KS-dkMBJSrKvTMAHDWkLikOKSjiFSv_OhrKava0sjv5oERXGzHr2Ncd-iIb97-kIWNcQexYOQ5LLlqOaDZXO5iJWWBZJi7JnoTrACokyBLmMoGqvrWNn-KpAY6WHSipX_QM2w","client_id":"9a265670-d771-4ab5-92df-b5c7a381c9e0","expires_in":"85829","expires_on":"1762705249","ext_expires_in":"86399","not_before":"1762618549","resource":"https://management.azure.com/","token_type":"Bearer"}
```

```bash
Connect-AzAccount -AccessToken eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6InlFVXdtWFdMMTA3Q2MtN1FaMldTYmVPYjNzUSIsImtpZCI6InlFVXdtWFdMMTA3Q2MtN1FaMldTYmVPYjNzUSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuYXp1cmUuY29tLyIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzkxNzE2YTlhLWY4ZmYtNDkwZi04ZjNhLWYyZTZkYTZlMTE2NS8iLCJpYXQiOjE3NjI2MTg1NDksIm5iZiI6MTc2MjYxODU0OSwiZXhwIjoxNzYyNzA1MjQ5LCJhaW8iOiJBV1FBbS84YUFBQUFFRlgrOHViamhicnRzc1BvZ1V4MlloTVFTVzM4N00yY0tFWTVZSVN5QUR3dXZBVjZMbWYyQ2hMTWg5VjI0NUpiQVRGcDBiaTN5UnI3TDdKdTdkUnpERHVZUDhIdE8wdXMyNzIzYnNYTmh3S0Z0Zk1NdXpNeXBwRnRkbGxkMys2SiIsImFwcGlkIjoiOWEyNjU2NzAtZDc3MS00YWI1LTkyZGYtYjVjN2EzODFjOWUwIiwiYXBwaWRhY3IiOiIyIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvOTE3MTZhOWEtZjhmZi00OTBmLThmM2EtZjJlNmRhNmUxMTY1LyIsImlkdHlwIjoiYXBwIiwib2lkIjoiNWE4ZTNkMzktNDcyMS00OTY0LThlNGEtOTY4NDMzOGQ5NzEzIiwicmgiOiIxLkFjb0FtbXB4a2ZfNEQwbVBPdkxtMm00UlpVWklmM2tBdXRkUHVrUGF3ZmoyTUJQNkFBREtBQS4iLCJzdWIiOiI1YThlM2QzOS00NzIxLTQ5NjQtOGU0YS05Njg0MzM4ZDk3MTMiLCJ0aWQiOiI5MTcxNmE5YS1mOGZmLTQ5MGYtOGYzYS1mMmU2ZGE2ZTExNjUiLCJ1dGkiOiJGQzh6YjhfaHhraWFVZjRUYl9ESEFBIiwidmVyIjoiMS4wIiwieG1zX2FjdF9mY3QiOiIzIDkiLCJ4bXNfZnRkIjoidnhkVEw0bjBuNFVoRWsxeGdoZ29QbUs5Q0dvVUtRQkVGQy1idnlJaG9lc0JkWE5sWVhOMExXUnpiWE0iLCJ4bXNfaWRyZWwiOiI3IDEwIiwieG1zX21pcmlkIjoiL3N1YnNjcmlwdGlvbnMvMTc0NjI5NGEtNWFhOC00Y2JiLTgyYTQtMTFlNzMxYjIwOTQyL3Jlc291cmNlZ3JvdXBzL3JnLTExMDgwODk0L3Byb3ZpZGVycy9NaWNyb3NvZnQuQ29tcHV0ZS92aXJ0dWFsTWFjaGluZXMvTGludXhWTSIsInhtc19yZCI6IjAuNDJMallCSmlPc1VvSk1MQktTVHc5RWpqUExXWGYzMGFmMDkxbkRXVFlUbFFsRU5Jd00yanZwSmgxM1hfWGM2M0R2NzRaaUFNQUEiLCJ4bXNfc3ViX2ZjdCI6IjMgOSIsInhtc190Y2R0IjoiMTcxMTk5MzE1OSJ9.XbxLltSDaMqpuWgM8OCmB6O82C4nQYZyLPPxyLEqHvpfiWSsJ-uget26TwnmaRc1X1zakUuzRN6wAWbAsE0V-Q2rzIRW1HtRBR3Hu-NyDTGmWgKbXp7U-CmPf-YpCGVUxy8eXqZPeIOtA0CVRGFK_66nrkL0rdXk97ultDybO-UML47yKWed3I4m3rp1E_SJKSnNEcCi6GW931n80KS-dkMBJSrKvTMAHDWkLikOKSjiFSv_OhrKava0sjv5oERXGzHr2Ncd-iIb97-kIWNcQexYOQ5LLlqOaDZXO5iJWWBZJi7JnoTrACokyBLmMoGqvrWNn-KpAY6WHSipX_QM2w","client_id":"9a265670-d771-4ab5-92df-b5c7a381c9e0 -AccountId 9a265670-d771-4ab5-92df-b5c7a381c9e0
```



<br>
<h2>Task 2 . Managed Identities</h2>
<p>A managed identity is a special type of service principal that can only be used with Azure resources. It provides an identity for applications to use when connecting to services that support Entra ID authentication. By using managed identities, developers can avoid managing credentials manually, simplifying security and reducing potential risks.<br>

For instance, suppose we want the managed identity assigned to our Azure virtual machine (VM) to access a Key Vault. All we need to do is assign the appropriate RBAC (Role-Based Access Control) role. When the VM attempts to access the Key Vault, it receives a token from the Instance Metadata Service (IMDS)—a backend service running on all Azure VMs. This service detects the attached managed identity and handles authentication automatically without requiring any hardcoded credentials.</p>

<h6 align="center"><img width="250px" src="https://github.com/user-attachments/assets/8fcb7fdd-2a7b-46ce-b32c-d5d2d15bf303"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h3>Types of Managed Identities</h3>
<p><code>System-Assigned Managed Identity</code>

- Automatically created and tied to a specific Azure resource (e.g., Virtual Machine, App Service).<br>
- When the resource is deleted, the identity is also deleted.<br>
- Only one system-assigned identity per resource.</p>

<p><code>User-Assigned Managed Identity</code>

- Created as a standalone Azure resource.<br>
- Can be assigned to one or more Azure resources.<br>
- Managed independently of the lifecycle of the resources it's assigned to.</p>

<h3>Key Benefits</h3>
<p>

- <code>No credential management</code>: Azure handles credential rotation and storage.<br>
- <code>Improved security</code>: Reduces the risk of leaking secrets or keys.<br>
- <code>Simplified access control</code>: Can be granted permissions via Azure RBAC or Entra ID.</p>

<p><em>Answer the question below</em></p>

<p>2.1. What type of managed identity's life cycle is independent from the resource? <br>
<code>•••••••••••••</code></p>

<br>
<h2>Task 3 . Attack Scenarios</h2>
<p>Managed identities in Azure are a powerful feature that improves security by eliminating the need to manage secrets or credentials manually. However, like any access control mechanism, <code>if misconfigured or compromised</code>, they can be abused by attackers.</p>

<h6 align="center"><img width="250px" src="https://github.com/user-attachments/assets/9e30439e-2131-48ee-9ef0-0e506b016809"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Here are several ways <code>Managed Identities</code> (MIs) can be exploited in an attack scenario:</p>

<h3>1. Privilege Escalation via Over-Permissioned Managed Identities</h3>
<p>If a managed identity is assigned overly permissive roles (e.g., <code>Contributor</code>, <code>Owner</code>, or <code>Key Vault Administrator</code>), an attacker who gains access to that identity (e.g., via a compromised VM or App Service) can perform high-privilege actions:<br>

- Access secrets in Azure Key Vault<br>
- Modify or delete Azure resources<br>
- Deploy new infrastructure</p>

<h3>2. Lateral Movement Between Resources</h3>
<p>Once an attacker compromises a resource (such as a VM or container), they can use the managed identity token from the <code>Instance Metadata Service</code> (IMDS) to:<br>
- Access other Azure services (e.g., storage, databases, Key Vaults)
- Move to other services where the identity has access, facilitating further exploitation</p>

<h3>3. Token Theft via the IMDS (Instance Metadata Service) Endpoint</h3>
<p>Azure VMs and other compute resources expose the IMDS endpoint at <code>http://xxx.xxx.xxx.xxx/</code>. If an attacker gains access to the machine (even via limited command execution), they can:<br>

- Query IMDS to obtain an access token for the managed identity<br>
- Use this token to access any Azure resource the identity is authorized for</p>

<h3>4. Persistence Through Managed Identity Abuse</h3>
<p>If an attacker compromises a resource and that resource's managed identity has write access to automation accounts, Logic Apps, or Functions, they could:<br>
- Create persistent scripts or backdoors<br>
- Establish scheduled tasks that keep calling external C2 (command and control) servers</p>

<h3>5. Misuse of User-Assigned Managed Identities (UAMI)</h3>
<p>User-assigned MIs can be attached/detached from different resources. If an attacker finds a UAMI with high privileges:<br>
- They could attach it to a compromised resource (like a VM they control)<br>
- Use the new token to escalate privileges or exfiltrate data</p>

<p>As listed above, there is quite a bit of attack surface when it comes to managed identities. Discovering the gaps and employing these techniques will depend on what type of managed identities are utilized and with which type of permissions.</p>

<p><em>Answer the question below</em></p>

<p>3.1. Where can the attackers obtain a token of managed identity if a resource is compromised?<br>
<code>•••••••• •••••••• •••••••</code></p>

<p align="left">Access the IMDS endpoint at http://xxx.xxx.xxx.xxx/<br><img width="700px" src="https://github.com/user-attachments/assets/f1d621b2-4c30-4519-97ee-cb2c7cef3b04"></p>

<br>
<h2>Task 4. Attack</h2>

<h6 align="center"><img width="250px" src="https://github.com/user-attachments/assets/8e5e19c7-bcc4-490b-89ca-45b8c8fdc013"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h3>Lab Scenario</h3>
<p>

- During the reconnaissance, you came across a password: <code>WhereIsMyMind$#@!</code><br>
- You don't know much about which permissions you have on the Azure Portal.<br>
- You don't know much about which resources you can access on the Azure Portal.<br>
- All you have is a compromised password!<br>
- How far can you go with it?<br>
- Which attack path(s) can you discover and how will you exploit it?<br>

Show us what you can do with the compromised password and the managed identities!<br>

Good luck!</p>

<p><em>Answer the questions below</em></p>

<p>4.1. Where can the attackers obtain a token of managed identity if a resource is compromised?<br>
<code>••••••••••••••••• ••••••• ••••••••••</code></p>

<p>4.2. What is the flag?<br>
<code>__________________________________</code></p>


<br>
<br>
<br>


<p>breakglass@tryhackmelabs.onmicrosoft.com : WhereIsMyMind$#@!</p>

oz@thmtraininglabs.onmicrosoft.com

oz_thmtraininglabs.onmicrosoft.com#EXT#@tryhackmelabs.onmicrosoft.com

qa-breakglass@tryhackmelabs.onmicrosoft.com
WhereIsMyMind$#@!
-----------------
5&EHc666vsT@c$V&
----------------
