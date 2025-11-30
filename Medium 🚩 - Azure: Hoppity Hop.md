<h1 align="center">Azure: Hoppity Hop</h1>
<p align="center">2025, November 30  &nbsp; .  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure on my <code>1</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>Azure challenge for cloud pentesters: Can you find the attack path and exploit it? &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/azhoppityhop">here</a>.<br><br><img width="1200px" src="https://github.com/user-attachments/assets/c1cd36ae-a483-4469-8f34-5dd449021f94"></p>

<h2>Task 1 . Introduction</h2>
<p>In this challenge, as a cloud pentester, you will recon and attack an Azure tenant to see if you can discover the attack path.</p>

<h3>Rules of Engagement (ROE)</h3>
<p>Even if you can after successful privilege escalation or lateral movement:<br>

- Do NOT create additional users<br>
- Do NOT modify existing users<br>
- Do NOT tamper with this Azure tenant by any means<br>
- This is a shared training tenant, and hence, respect the integrity of the environment<br>
- Leave it as you found it</p>


<h3>Start the Lab</h3>

<p>Even if you can after successful privilege escalation or lateral movement:<br>

- Click the <strong>Cloud Details</strong> button<br>
- On the modal box, click <strong>Join Lab</strong><br>
- Find your credentials in the  <strong>Credentials</strong> tab<br
- Click <strong>Open Lab</strong> and log in to the Azure Portal<br
- Then, click the <strong>Deploy Lab</strong> in the <strong>Actions</strong> tab to deploy the cloud resources required for the challenge</p>


<p><em>Answer the question below</em></p>

<p>1.1. <em>I have initiated the challenge deployment.</em><br>
<code>NO answer needed</code></p>

<br>

<h2>Task 2 . Attack</h2>
<h3></h3>Lab Scenario</h3>

<p>
  
- During the reconnaissance, you came across a password: <code>WhereIsMyMind$#@!</code><br>
- You don't know much about which permissions you have on the Azure Portal<br>
- You don't know much about which resources you can access on the Azure Portal<br>
- All you have is a compromised password<br>
- Which attack path(s) can you discover and how will you exploit them?<br>

Good luck!</p>

<p><em>Answer the question below</em></p>

<p aligned="center">I followed <a href="https://0xb0b.gitbook.io/writeups/tryhackme/2025/azure-hoppity-hop">0xb0b</a></p>

<p>
  
- select <code>All resources</code> > <code>LinuxVM</code></p>

<img width="1217" height="315" alt="image" src="https://github.com/user-attachments/assets/7100db06-f938-4d1e-ba86-236d853a976b" />

<br>
<br>

<p>

- select <code>Connect</code> > <code>Connect</code></p>

<img width="1211" height="649" alt="image" src="https://github.com/user-attachments/assets/0e8763a3-7304-4663-b252-e46cd2af1507" />

<br>
<br>
<p>
  
- <code>SSH</code> as <code>azureuser</code></p>

<img width="1007" height="650" alt="image" src="https://github.com/user-attachments/assets/ffa093b2-db3b-465e-aac4-a41fee4aa039" />

<br>
<br>
<p>
  
- id<br>
- pwd</p>

<img width="1118" height="145" alt="image" src="https://github.com/user-attachments/assets/a5bce437-2783-4769-8f2f-4f4efbde7990" />

<br>
<br>
<p>
  
- select <code>LinuxVM1</code> > <code>Connect</code> > <code>Connect</code></p>

<img width="1209" height="642" alt="image" src="https://github.com/user-attachments/assets/8dfe0126-ae3e-4c6f-bbef-8b3913e60b57" />

<br>
<br>

```bash
azureuser@LinuxVM:~$ curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

<img width="1119" height="131" alt="image" src="https://github.com/user-attachments/assets/0528f01e-f69c-41a2-bcc1-6cd70368764a" />

<br>
<br>

```bash
azureuser@LinuxVM:~$ az login --identity
  {
    "environmentName": "AzureCloud",
    "homeTenantId": "········-····-····-····-············",
    "id": "◦◦◦◦◦◦◦◦-◦◦◦◦-◦◦◦◦-◦◦◦◦-◦◦◦◦◦◦◦◦◦◦◦◦",
    "isDefault": true,
    "managedByTenants": [],
    "name": "Az-Subs-B2C-1",
    "state": "Enabled",
    "tenantId": "········-····-····-····-············",
    "user": {
      "assignedIdentityInfo": "MSI",
      "name": "systemAssignedIdentity",
      "type": "servicePrincipal"
    }
  }
]
```

<img width="1124" height="363" alt="image" src="https://github.com/user-attachments/assets/16842ed6-2dea-49dc-8004-fd6c0ef68f8f" />

<br>
<br>

```bash
azureuser@LinuxVM:~$ az group list -o table
```

```bash
azureuser@LinuxVM:~$ az vm list -g rg-•••••••• -o table
```

```bash
azureuser@LinuxVM:~$ az resource list -g rg-•••••••• -o table
```

<img width="1120" height="462" alt="image" src="https://github.com/user-attachments/assets/e1010978-dae7-455e-911c-0ca9b684ec43" />

<br>
<br>

```bash
azureuser@LinuxVM:~$ az vm identity show -g rg-•••••••• -n LinuxVM
{
  "principalId": "f4105788-4b0d-49c0-b5cf-1f3495419249",
  "tenantId": "········-····-····-····-············",
  "type": "SystemAssigned",
  "userAssignedIdentities": null
}
```

```bash
azureuser@LinuxVM:~$ az resource list -g rg-•••••••• -n LinuxVM
[
  {
    "changedTime": "2025-11-30Txx:xx:xx.xxxxxx+00:00",
    "createdTime": "2025-11-30Txx:xx:xx.xxxxxx+00:00",
    "extendedLocation": null,
    "id": "/subscriptions/◦◦◦◦◦◦◦◦-◦◦◦◦-◦◦◦◦-◦◦◦◦-◦◦◦◦◦◦◦◦◦◦◦◦/resourceGroups/rg-••••••••/providers/Microsoft.Compute/virtualMachines/LinuxVM",
    "identity": {
      "principalId": "f4105788-4b0d-49c0-b5cf-1f3495419249",
      "tenantId": "········-····-····-····-············",
      "type": "SystemAssigned",
      "userAssignedIdentities": null
    },
    "kind": null,
    "location": "eastus",
    "managedBy": null,
    "name": "LinuxVM",
    "plan": null,
    "properties": null,
    "provisioningState": "Succeeded",
    "resourceGroup": "rg-••••••••",
    "sku": null,
    "tags": {},
    "type": "Microsoft.Compute/virtualMachines"
  }
]
```

```bash
azureuser@LinuxVM:~$ az resource list -g rg-•••••••• -n LinuxVM1
[
  {
    "changedTime": "2025-11-30Txx:xx:xx.xxxxxx+00:00",
    "createdTime": "2025-11-30Txx:xx:xx.xxxxxxx+00:00",
    "extendedLocation": null,
    "id": "/subscriptions/◦◦◦◦◦◦◦◦-◦◦◦◦-◦◦◦◦-◦◦◦◦-◦◦◦◦◦◦◦◦◦◦◦◦/resourceGroups/rg-••••••••/providers/Microsoft.Compute/virtualMachines/LinuxVM1",
    "identity": null,
    "kind": null,
    "location": "eastus",
    "managedBy": null,
    "name": "LinuxVM1",
    "plan": null,
    "properties": null,
    "provisioningState": "Succeeded",
    "resourceGroup": "rg-••••••••",
    "sku": null,
    "tags": {},
    "type": "Microsoft.Compute/virtualMachines"
  }
]
```

```bash
azureuser@LinuxVM:~$ az role assignment list --assignee ♥♥♥♥♥♥♥♥-♥♥♥♥-♥♥♥♥-♥♥♥♥-♥♥♥♥♥♥♥♥♥♥♥♥--scope /subscriptions/◦◦◦◦◦◦◦◦-◦◦◦◦-◦◦◦◦-◦◦◦◦-◦◦◦◦◦◦◦◦◦◦◦◦/resourceGroups/rg-•••••••• -o table
Principal                             Role                         Scope
------------------------------------  ---------------------------  ------------------------------------------------------------------------------
▼▼▼▼▼▼▼▼-▼▼▼▼-▼▼▼▼-▼▼▼▼-▼▼▼▼▼▼▼▼▼▼▼▼  Virtual Machine Contributor  /subscriptions/◦◦◦◦◦◦◦◦-◦◦◦◦-◦◦◦◦-◦◦◦◦-◦◦◦◦◦◦◦◦◦◦◦◦/resourcegroups/rg-••••••••
```

```bash
azureuser@LinuxVM:~$ az role assignment list --assignee ♥♥♥♥♥♥♥♥-♥♥♥♥-♥♥♥♥-♥♥♥♥-♥♥♥♥♥♥♥♥♥♥♥♥--scope /subscriptions/◦◦◦◦◦◦◦◦-◦◦◦◦-◦◦◦◦-◦◦◦◦-◦◦◦◦◦◦◦◦◦◦◦◦/resourceGroups/rg-••••••••
[
  {
    "condition": null,
    "conditionVersion": null,
    "createdBy": "...",
    "createdOn": "2025-11-30Txx:xx:xx.xxxxxx+00:00",
    "delegatedManagedIdentityResourceId": null,
    "description": null,
    "id": "/subscriptions/◦◦◦◦◦◦◦◦-◦◦◦◦-◦◦◦◦-◦◦◦◦-◦◦◦◦◦◦◦◦◦◦◦◦/resourcegroups/rg-••••••••/providers/Microsoft.Authorization/roleAssignments/ae0fd9d1-7523-4ac9-b7c6-d1ef4912e12e",
    "name": "ae0fd9d1-7523-4ac9-b7c6-d1ef4912e12e",
    "principalId": "♥♥♥♥♥♥♥♥-♥♥♥♥-♥♥♥♥-♥♥♥♥-♥♥♥♥♥♥♥♥♥♥♥♥",
    "principalName": "▼▼▼▼▼▼▼▼-▼▼▼▼-▼▼▼▼-▼▼▼▼-▼▼▼▼▼▼▼▼▼▼▼▼",
    "principalType": "ServicePrincipal",
    "resourceGroup": "rg-••••••••",
    "roleDefinitionId": "/subscriptions/◦◦◦◦◦◦◦◦-◦◦◦◦-◦◦◦◦-◦◦◦◦-◦◦◦◦◦◦◦◦◦◦◦◦/providers/Microsoft.Authorization/roleDefinitions/9980e02c-c2be-4d73-94e8-173b1dc7cf3c",
    "roleDefinitionName": "Virtual Machine Contributor",
    "scope": "/subscriptions/◦◦◦◦◦◦◦◦-◦◦◦◦-◦◦◦◦-◦◦◦◦-◦◦◦◦◦◦◦◦◦◦◦◦/resourcegroups/rg-••••••••",
    "type": "Microsoft.Authorization/roleAssignments",
    "updatedBy": "...",
    "updatedOn": "2025-11-30Txx:xx:xx.xxxxxx+00:00"
  }
]
```

```bash
azureuser@LinuxVM:~$ az role definition show --id /subscriptions/◦◦◦◦◦◦◦◦-◦◦◦◦-◦◦◦◦-◦◦◦◦-◦◦◦◦◦◦◦◦◦◦◦◦/providers/Microsoft.Authorization/roleDefinitions/9980e02c-c2be-4d73-94e8-173b1dc7cf3c --query "permissions"
[
  {
    "actions": [
      "Microsoft.Authorization/*/read",
      "Microsoft.Compute/availabilitySets/*",
      "Microsoft.Compute/locations/*",
      "Microsoft.Compute/virtualMachines/*",
      "Microsoft.Compute/virtualMachineScaleSets/*",
      "Microsoft.Compute/cloudServices/*",
      "Microsoft.Compute/disks/write",
      "Microsoft.Compute/disks/read",
      "Microsoft.Compute/disks/delete",
      "Microsoft.Compute/hostgroups/write",
      "Microsoft.Compute/hostgroups/hosts/write",
      "Microsoft.DevTestLab/schedules/*",
      "Microsoft.Insights/alertRules/*",
      "Microsoft.Network/applicationGateways/backendAddressPools/join/action",
      "Microsoft.Network/loadBalancers/backendAddressPools/join/action",
      "Microsoft.Network/loadBalancers/inboundNatPools/join/action",
      "Microsoft.Network/loadBalancers/inboundNatRules/join/action",
      "Microsoft.Network/loadBalancers/probes/join/action",
      "Microsoft.Network/loadBalancers/read",
      "Microsoft.Network/locations/*",
      "Microsoft.Network/networkInterfaces/*",
      "Microsoft.Network/networkSecurityGroups/join/action",
      "Microsoft.Network/networkSecurityGroups/read",
      "Microsoft.Network/publicIPAddresses/join/action",
      "Microsoft.Network/publicIPAddresses/read",
      "Microsoft.Network/virtualNetworks/read",
      "Microsoft.Network/virtualNetworks/subnets/join/action",
      "Microsoft.RecoveryServices/locations/*",
      "Microsoft.RecoveryServices/Vaults/backupFabrics/backupProtectionIntent/write",
      "Microsoft.RecoveryServices/Vaults/backupFabrics/protectionContainers/protectedItems/*/read",
      "Microsoft.RecoveryServices/Vaults/backupFabrics/protectionContainers/protectedItems/read",
      "Microsoft.RecoveryServices/Vaults/backupFabrics/protectionContainers/protectedItems/write",
      "Microsoft.RecoveryServices/Vaults/backupPolicies/read",
      "Microsoft.RecoveryServices/Vaults/backupPolicies/write",
      "Microsoft.RecoveryServices/Vaults/read",
      "Microsoft.RecoveryServices/Vaults/usages/read",
      "Microsoft.RecoveryServices/Vaults/write",
      "Microsoft.ResourceHealth/availabilityStatuses/read",
      "Microsoft.Resources/deployments/*",
      "Microsoft.Resources/subscriptions/resourceGroups/read",
      "Microsoft.SerialConsole/serialPorts/connect/action",
      "Microsoft.SqlVirtualMachine/*",
      "Microsoft.Storage/storageAccounts/listKeys/action",
      "Microsoft.Storage/storageAccounts/read",
      "Microsoft.Support/*"
    ],
    "condition": null,
    "conditionVersion": null,
    "dataActions": [],
    "notActions": [],
    "notDataActions": []
  }
]
```

<p>

- change tyler´s password</p>

```bash
azureuser@LinuxVM:~$ az vm user update -u tyler -p 'Password123!' -n LinuxVM1 -g rg-••••••••
{
  "autoUpgradeMinorVersion": false,
  "id": "/subscriptions/◦◦◦◦◦◦◦◦-◦◦◦◦-◦◦◦◦-◦◦◦◦-◦◦◦◦◦◦◦◦◦◦◦◦/resourceGroups/rg-••••••••/providers/Microsoft.Compute/virtualMachines/LinuxVM1/extensions/enablevmaccess",
  "location": "eastus",
  "name": "enablevmaccess",
  "provisioningState": "Succeeded",
  "publisher": "Microsoft.OSTCExtensions",
  "resourceGroup": "rg-••••••••",
  "settings": {},
  "type": "Microsoft.Compute/virtualMachines/extensions",
  "typeHandlerVersion": "1.5",
  "typePropertiesType": "VMAccessForLinux"
}
```

<p>

- SSH as <code>tyler</code></p>

<img width="1163" height="803" alt="image" src="https://github.com/user-attachments/assets/b53838b1-a184-4dbe-9771-78fbccf9d7eb" />

<br>
<br>

<img width="1162" height="241" alt="image" src="https://github.com/user-attachments/assets/846c41a1-cfef-4cc2-8fbd-503d4e5fe766" />

<br>
<br>
<p>2.1. <em>What is the flag?</em><br>
<code>THM{••••••••••••••••••••••••••••••••••••}</code></p>

<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/e7d2f3b3-83cb-433d-ab8a-2a04084718b0"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/540a0cdc-43b6-4851-b48f-bece0093ea57"></p>



<h1 align="center">My TryHackMe Journey ・ 2025, November</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|30      |Medium 🚩 - Azure: Hoppity Hop         |   1    |      94ᵗʰ    |     3ʳᵈ    |     437ᵗʰ   |      5ᵗʰ     |    134,276  |    1,038    |    81     |
|30      |Medium 🚩 - Juicy                      |   1    |      94ᵗʰ    |     3ʳᵈ    |     432ⁿᵈ   |      5ᵗʰ     |    134,246  |    1,037    |    81     |
|26      |Easy 🚩 - The Case: Seven Minutes on the Seine| 1  |   94ᵗʰ    |     3ʳᵈ    |     410ᵗʰ   |      6ᵗʰ     |    134,126  |    1,036    |    81     |
|26      |Easy 🚩 - BankGPT                      |   1    |      94ᵗʰ    |     3ʳᵈ    |     443ʳᵈ   |      6ᵗʰ     |    134,066  |    1,035    |    81     |
|26      |Easy 🚩 - HealthGPT                    |   1    |      94ᵗʰ    |     3ʳᵈ    |     470ᵗʰ   |      6ᵗʰ     |    134,021  |    1,034    |    81     |
|23      |Medium 🚩 - Padelify                   |   2    |      93ʳᵈ    |     3ʳᵈ    |     436ᵗʰ   |      6ᵗʰ     |    133,976  |    1,033    |    80     |
|23      |Medium 🚩 - Farewell                   |   2    |      93ʳᵈ    |     3ʳᵈ    |     483ʳᵈ   |      6ᵗʰ     |    133,886  |    1,032    |    80     |
|23      |Medium 🔗 - WAF: Exploitation Techniques|  2    |      92ⁿᵈ    |     3ʳᵈ    |     516ᵗʰ   |      6ᵗʰ     |    133,826  |    1,031    |    80     |
|22      |Hard 🚩 - The Last Trial               |   1    |      91ˢᵗ    |     3ʳᵈ    |     532ⁿᵈ   |      6ᵗʰ     |    133,762  |    1,030    |    80     |
|22      |Medium 🔗 - Data Integrity & Model Poisoning|   1|     94ᵗʰ    |     3ʳᵈ    |     762ⁿᵈ   |      7ᵗʰ     |    133,492  |    1,029    |    80     |
|22      |Easy 🔗 - LLM Output Handling and Privacy Risks|   1|  94ᵗʰ    |     3ʳᵈ    |     809ᵗʰ   |      7ᵗʰ     |    133,444  |    1,028    |    80     |
|22      |Easy 🔗 - Advent of Cyber Prep Track   |   1    |      94ᵗʰ    |     3ʳᵈ    |     826ᵗʰ   |      8ᵗʰ     |    133,428  |    1,027    |    80     |
|19      |Easy 🔗 - WAF: Introduction            |   2    |      91ˢᵗ    |     3ʳᵈ    |     737ᵗʰ   |      7ᵗʰ     |    133,348  |    1,026    |    80     |
|19      |Easy 🔗 - Django: CVE-2025-64459       |   2    |      93ʳᵈ    |     3ʳᵈ    |     877ᵗʰ   |      8ᵗʰ     |    133,224  |    1,025    |    80     |
|19      |Easy 🔗 - Django: CVE-2025-64459       |   2    |      93ʳᵈ    |     3ʳᵈ    |     877ᵗʰ   |      8ᵗʰ     |    133,224  |    1,025    |    80     |
|18      |Easy 🔗 - OWASP Top 10 2025: Insecure Data Handling| 1        |      93ʳᵈ    |     3ʳᵈ    |     894ᵗʰ   |      8ᵗʰ     |    132,207  |    1,024    |    80     |
|18      |Easy 🔗 - OWASP Top 10 2025: Application Design Failures| 1   |      93ʳᵈ    |     3ʳᵈ    |     927ᵗʰ   |      8ᵗʰ     |    132,183  |    1,023    |    80     |
|18      |Easy 🔗 - OWASP Top 10 2025: IAAA Failures| 1   |      93ʳᵈ    |     3ʳᵈ    |     971ˢᵗ   |      8ᵗʰ     |    132,151  |    1,022    |    80     |
|14      |Hard 🚩 - Shock and Silence            |   1    |      94ᵗʰ    |     4ᵗʰ    |     749ᵗʰ   |      7ᵗʰ     |    133,095  |    1,021    |    80     |
|14      |Easy 🔗 - Input Manipulation & Prompt Injection| 1 |   95ᵗʰ    |     4ᵗʰ    |   1,290ᵗʰ   |     12ⁿᵈ     |    132,822  |    1,020    |    80     |
|14      |Hard 🚩 - CRM Snatch                   |   1    |      95ᵗʰ    |     4ᵗʰ    |   1,526ᵗʰ   |     12ⁿᵈ     |          -  |    1,019    |    80     |
|8       |Easy 🔗 - Living of the Land Attacks   |   1    |      91ˢᵗ    |     4ᵗʰ    |   1,759ᵗʰ   |     17ᵗʰ     |    132,642  |    1,018    |    80     |
|8       |Hard 🚩 - Lost in RAMslation           |   1    |      91ˢᵗ    |     4ᵗʰ    |   2,547ᵗʰ   |     25ᵗʰ     |    132,580  |    1,017    |    80     |
|8       |Easy 🔗 - MITRE                        |   1    |       -      |     4ᵗʰ    |      -      |      -       |          -  |       -     |    80     |

</h6></div><br>

<p align="center">Global All Time:     94ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/12442e2f-9395-46ef-9769-59cd30a04a24"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/a381c057-7950-492b-8c4d-5cae896d2433"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/f611a742-8f61-40c9-acd8-df2a1afd66a6"><br><br>
                  Global monthly:    437ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/bf504f5c-1111-4941-94c4-9d1177cc2314"><br><br>
                  Brazil monthly:       5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/8900d576-f959-44dd-bc73-8effe201e537"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
