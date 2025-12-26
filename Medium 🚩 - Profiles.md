<h3 align="center">Profiles</h3>
<p align="center">2025, October 7 - December 25  &nbsp; ·  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure in <a href="https://tryhackme.com">TryHackMe</a>.<br>No profile? No problem. &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/profilesroom">here</a>.<br><img width="80px" src="https://github.com/user-attachments/assets/4817e0d9-acce-4959-9f6c-4cdc8cc92462"><br><br><img width="1200px" src="https://github.com/user-attachments/assets/9f57bbcf-9bc4-47f3-9829-dc5317bd1eb9"></p>
<br>





<h2>Task 1 . The Incident</h2>
<p>The incident response team has alerted you that there was some suspicious activity on one of the Linux database servers.<br>

A memory dump of the server was taken and provided to you for analysis. You advise the team that you are missing crucial information from the server, but it has already been taken offline. They just made your job a little harder, but not impossible.<br>

Click on the <strong>Download Task Files</strong> button at the top of this task. You will be provided with an <strong>evidence.zip</strong> file.<br>

Extract the zip file's contents and begin your analysis in order to answer the questions.<br>
Note: The challenge is best done using your own environment. I recommend using Volatility 2.6.1 to handle this task and strongly advise using this article by Sean Whalen to aid you with the Volatility installation.</p>

<p><em>Answer the questions below</em></p>

<p>1.1. What is the exposed root password?<br>
<code>Ftrccw45PHyq</code></p>

<p>

- download <strong>Task File</strong> evidence-•••••••••••••.zip<br>
- extract the <code>linux.mem</code> memory dump<br>
- generate a file containing its strings</p>

```bash
$ strings -a -td linux.mem > challenge_strings.txt
```

<p>
  
- locate commands related to <strong>root</strong> user access<br>
- analyze the output at <strong>3853033984</strong> offset</p>

```bash
$ grep -E 'su root' challenge_strings.txt
789842768 su root
794655216 _CMDLINE=su root
2810770992 _CMDLINE=su root
2814347152 su root
3799619328 su root
3853033984 su rootFtrccw45PHyq
4169226848 su root
```

<img width="1687" height="128" alt="image" src="https://github.com/user-attachments/assets/e1b01cb8-79c1-40b1-b619-70236d5ca344" />

<br>
<br>
<br>
<p>1.2. And what time was the users.db file approximately accessed? Format is YYYY-MM-DD HH:MM:SS<br>
<code>2023-11-07 03:49:45</code></p>

<p>
  
- filter, parse, and sort string artifacts to reconstruct a chronological timeline of events</p>


```bash
$ grep -E '7 03:[0-6][0-9]:[0-6][0-9]' challenge_strings.txt | awk '{match($0, /03:[0-9]{2}:[0-9]{2}/); print substr($0, RSTART, RLENGTH), $0}' | sort | cut -d' ' -f2-
```

<p>

- isolate all logs matching the <strong>7 03:</strong> timestamp pattern into a separate timed.txt file</p>


```bash
$ grep '7 03:' challenge_strings.txt > timed.txt
```

<p>
  
- search the isolated logs for the <strong>paco</strong> keyword to locate specific module execution details<br>
- correlate <strong>sshd</strong> and <strong>systemd</strong> logs to identify the session start<br>807196475 Nov  7 03:49:41 dbserver systemd[1]: systemd-timedated.service: Succeeded.<br>807196550 Nov  7 03:49:45 dbserver systemd[1]: Started Session 3 of user paco.<br>
- identify the <code>users.db</code> access time as <strong>2023-11-07 03:49:45</strong></p>

```bash
$ grep 'paco' timed.txt
794860667 2023-11-07 03:49:12,960 - modules.py[DEBUG]: Running module final_message (<module 'cloudinit.config.cc_final_message' from '/usr/lib/python3/dist-packages/cloudinit/config/cc_final_message.py'>) with frequency always
794860885 2023-11-07 03:49:12,960 - handlers.py[DEBUG]: start: modules-final/config-final_message: running config-final_message with frequency always
794861025 2023-11-07 03:49:12,960 - helpers.py[DEBUG]: Running config-final_message using lock (<cloudinit.helpers.DummyLock object at 0x7f6a65feac70>)
794861167 2023-11-07 03:49:12,960 - util.py[DEBUG]: Reading from /proc/uptime (quiet=False)
794861249 2023-11-07 03:49:12,960 - util.py[DEBUG]: Read 10 bytes from /proc/uptime
794861323 2023-11-07 03:49:12,963 - util.py[DEBUG]: Cloud-init v. 23.3.1-0ubuntu1~20.04.1 finished at Tue, 07 Nov 2023 03:49:12 +0000. Datasource DataSourceNone.  Up 9.16 seconds
794861492 2023-11-07 03:49:12,963 - util.py[DEBUG]: Writing to /var/lib/cloud/instance/boot-finished - wb: [644] 68 bytes
794861604 2023-11-07 03:49:12,963 - cc_final_message.py[WARNING]: Used fallback datasource
794861685 2023-11-07 03:49:12,963 - handlers.py[DEBUG]: finish: modules-final/config-final_message: SUCCESS: config-final_message ran successfully
794861822 2023-11-07 03:49:12,963 - main.py[DEBUG]: Ran 11 modules with 0 failures
794861895 2023-11-07 03:49:12,964 - atomic_helper.py[DEBUG]: Atomically writing to file /var/lib/cloud/data/status.json (via temporary file /var/lib/cloud/data/tmp2al6wg8d) - w: [644] 570 bytes/chars
794862085 2023-11-07 03:49:12,964 - atomic_helper.py[DEBUG]: Atomically writing to file /var/lib/cloud/data/result.json (via temporary file /var/lib/cloud/data/tmp870arbyp) - w: [644] 65 bytes/chars
794862274 2023-11-07 03:49:12,964 - util.py[DEBUG]: Creating symbolic link from '/run/cloud-init/result.json' => '../../var/lib/cloud/data/result.json'
794862416 2023-11-07 03:49:12,964 - util.py[DEBUG]: Reading from /proc/uptime (quiet=False)
794862498 2023-11-07 03:49:12,964 - util.py[DEBUG]: Read 10 bytes from /proc/uptime
794862572 2023-11-07 03:49:12,964 - util.py[DEBUG]: cloud-init mode 'modules' took 0.113 seconds (0.11)
794862666 2023-11-07 03:49:12,964 - handlers.py[DEBUG]: finish: modules-final: SUCCESS: running modules for final
794999913 2023-11-07 03:49:12,565 - util.py[DEBUG]: Reading from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json (quiet=False)
795000066 2023-11-07 03:49:12,565 - util.py[DEBUG]: Read 136743 bytes from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json
795000215 2023-11-07 03:49:12,567 - util.py[DEBUG]: Reading from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json (quiet=False)
795000368 2023-11-07 03:49:12,567 - util.py[DEBUG]: Read 136743 bytes from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json
795000517 2023-11-07 03:49:12,569 - util.py[DEBUG]: Reading from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json (quiet=False)
795000670 2023-11-07 03:49:12,569 - util.py[DEBUG]: Read 136743 bytes from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json
795000819 2023-11-07 03:49:12,570 - util.py[DEBUG]: Reading from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json (quiet=False)
795000972 2023-11-07 03:49:12,570 - util.py[DEBUG]: Read 136743 bytes from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json
795001121 2023-11-07 03:49:12,571 - util.py[DEBUG]: Reading from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json (quiet=False)
795001274 2023-11-07 03:49:12,572 - util.py[DEBUG]: Read 136743 bytes from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json
795001423 2023-11-07 03:49:12,573 - util.py[DEBUG]: Reading from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json (quiet=False)
795001576 2023-11-07 03:49:12,573 - util.py[DEBUG]: Read 136743 bytes from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json
795001725 2023-11-07 03:49:12,574 - util.py[DEBUG]: Reading from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json (quiet=False)
795001878 2023-11-07 03:49:12,574 - util.py[DEBUG]: Read 136743 bytes from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json
795002027 2023-11-07 03:49:12,575 - stages.py[DEBUG]: Using distro class <class 'cloudinit.distros.ubuntu.Distro'>
795002132 2023-11-07 03:49:12,576 - modules.py[INFO]: Skipping modules 'wireguard,snap,ubuntu_autoinstall,keyboard,apt_pipelining,ubuntu_advantage,ntp,timezone,disable_ec2_metadata,runcmd' because no applicable config is provided.
795002353 2023-11-07 03:49:12,576 - modules.py[DEBUG]: Running module ssh_import_id (<module 'cloudinit.config.cc_ssh_import_id' from '/usr/lib/python3/dist-packages/cloudinit/config/cc_ssh_import_id.py'>) with frequency once-per-instance
795002582 2023-11-07 03:49:12,576 - handlers.py[DEBUG]: start: modules-config/config-ssh_import_id: running config-ssh_import_id with frequency once-per-instance
795002734 2023-11-07 03:49:12,577 - helpers.py[DEBUG]: config-ssh_import_id already ran (freq=once-per-instance)
795002837 2023-11-07 03:49:12,577 - handlers.py[DEBUG]: finish: modules-config/config-ssh_import_id: SUCCESS: config-ssh_import_id previously ran
795002973 2023-11-07 03:49:12,577 - modules.py[DEBUG]: Running module locale (<module 'cloudinit.config.cc_locale' from '/usr/lib/python3/dist-packages/cloudinit/config/cc_locale.py'>) with frequency once-per-instance
795003181 2023-11-07 03:49:12,577 - handlers.py[DEBUG]: start: modules-config/config-locale: running config-locale with frequency once-per-instance
795003319 2023-11-07 03:49:12,577 - helpers.py[DEBUG]: config-locale already ran (freq=once-per-instance)
795003415 2023-11-07 03:49:12,577 - handlers.py[DEBUG]: finish: modules-config/config-locale: SUCCESS: config-locale previously ran
795003537 2023-11-07 03:49:12,577 - modules.py[DEBUG]: Running module set_passwords (<module 'cloudinit.config.cc_set_passwords' from '/usr/lib/python3/dist-packages/cloudinit/config/cc_set_passwords.py'>) with frequency once-per-instance
795003766 2023-11-07 03:49:12,577 - handlers.py[DEBUG]: start: modules-config/config-set_passwords: running config-set_passwords with frequency once-per-instance
795003918 2023-11-07 03:49:12,577 - helpers.py[DEBUG]: confi
807193685 Nov  7 03:49:12 dbserver cloud-init[800]: 2023-11-07 03:49:12,963 - cc_final_message.py[WARNING]: Used fallback datasource
807193808 Nov  7 03:49:12 dbserver systemd[1]: Finished Execute cloud user/final scripts.
808279104 -07 03:49:12,929 - util.py[DEBUG]: Read 136743 bytes from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json
808279246 2023-11-07 03:49:12,930 - util.py[DEBUG]: Reading from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json (quiet=False)
808279399 2023-11-07 03:49:12,930 - util.py[DEBUG]: Read 136743 bytes from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json
808279548 2023-11-07 03:49:12,932 - util.py[DEBUG]: Reading from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json (quiet=False)
808279701 2023-11-07 03:49:12,932 - util.py[DEBUG]: Read 136743 bytes from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json
808279850 2023-11-07 03:49:12,933 - util.py[DEBUG]: Reading from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json (quiet=False)
808280003 2023-11-07 03:49:12,934 - util.py[DEBUG]: Read 136743 bytes from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json
808280152 2023-11-07 03:49:12,935 - util.py[DEBUG]: Reading from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json (quiet=False)
808280305 2023-11-07 03:49:12,935 - util.py[DEBUG]: Read 136743 bytes from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json
808280454 2023-11-07 03:49:12,937 - util.py[DEBUG]: Reading from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json (quiet=False)
808280607 2023-11-07 03:49:12,938 - util.py[DEBUG]: Read 136743 bytes from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json
808280756 2023-11-07 03:49:12,939 - util.py[DEBUG]: Reading from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json (quiet=False)
808280909 2023-11-07 03:49:12,939 - util.py[DEBUG]: Read 136743 bytes from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json
808281058 2023-11-07 03:49:12,941 - util.py[DEBUG]: Reading from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json (quiet=False)
808281211 2023-11-07 03:49:12,941 - util.py[DEBUG]: Read 136743 bytes from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json
808281360 2023-11-07 03:49:12,942 - util.py[DEBUG]: Reading from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json (quiet=False)
808281513 2023-11-07 03:49:12,942 - util.py[DEBUG]: Read 136743 bytes from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json
808281662 2023-11-07 03:49:12,943 - util.py[DEBUG]: Reading from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json (quiet=False)
808281815 2023-11-07 03:49:12,943 - util.py[DEBUG]: Read 136743 bytes from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json
808281964 2023-11-07 03:49:12,944 - util.py[DEBUG]: Reading from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json (quiet=False)
808282117 2023-11-07 03:49:12,945 - util.py[DEBUG]: Read 136743 bytes from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json
808282266 2023-11-07 03:49:12,946 - util.py[DEBUG]: Reading from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json (quiet=False)
808282419 2023-11-07 03:49:12,946 - util.py[DEBUG]: Read 136743 bytes from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json
808282568 2023-11-07 03:49:12,947 - util.py[DEBUG]: Reading from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json (quiet=False)
808282721 2023-11-07 03:49:12,947 - util.py[DEBUG]: Read 136743 bytes from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json
808282870 2023-11-07 03:49:12,948 - util.py[DEBUG]: Reading from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json (quiet=False)
808283023 2023-11-07 03:49:12,948 - util.py[DEBUG]: Read 136743 bytes from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json
808283172 2023-11-07 03:49:12,949 - ut| --skip | --edit-todo
813939778 2023-11-07 03:49:12,959 - helpers.py[DEBUG]: config-scripts_per_once already ran (freq=once)
813939871 2023-11-07 03:49:12,959 - handlers.py[DEBUG]: finish: modules-final/config-scripts_per_once: SUCCESS: config-scripts_per_once previously ran
813940012 2023-11-07 03:49:12,959 - modules.py[DEBUG]: Running module scripts_per_boot (<module 'cloudinit.config.cc_scripts_per_boot' from '/usr/lib/python3/dist-packages/cloudinit/config/cc_scripts_per_boot.py'>) with frequency always
813940239 2023-11-07 03:49:12,959 - handlers.py[DEBUG]: start: modules-final/config-scripts_per_boot: running config-scripts_per_boot with frequency always
813940385 2023-11-07 03:49:12,959 - helpers.py[DEBUG]: Running config-scripts_per_boot using lock (<cloudinit.helpers.DummyLock object at 0x7f6a65feaf10>)
813940530 2023-11-07 03:49:12,959 - handlers.py[DEBUG]: finish: modules-final/config-scripts_per_boot: SUCCESS: config-scripts_per_boot ran successfully
813940673 2023-11-07 03:49:12,959 - modules.py[DEBUG]: Running module scripts_per_instance (<module 'cloudinit.config.cc_scripts_per_instance' from '/usr/lib/python3/dist-packages/cloudinit/config/cc_scripts_per_instance.py'>) with frequency once-per-instance
813940923 2023-11-07 03:49:12,959 - handlers.py[DEBUG]: start: modules-final/config-scripts_per_instance: running config-scripts_per_instance with frequency once-per-instance
813941088 2023-11-07 03:49:12,959 - helpers.py[DEBUG]: config-scripts_per_instance already ran (freq=once-per-instance)
813941198 2023-11-07 03:49:12,959 - handlers.py[DEBUG]: finish: modules-final/config-scripts_per_instance: SUCCESS: config-scripts_per_instance previously ran
813941347 2023-11-07 03:49:12,959 - modules.py[DEBUG]: Running module scripts_user (<module 'cloudinit.config.cc_scripts_user' from '/usr/lib/python3/dist-packages/cloudinit/config/cc_scripts_user.py'>) with frequency once-per-instance
813941573 2023-11-07 03:49:12,959 - handlers.py[DEBUG]: start: modules-final/config-scripts_user: running config-scripts_user with frequency once-per-instance
813941722 2023-11-07 03:49:12,959 - helpers.py[DEBUG]: config-scripts_user already ran (freq=once-per-instance)
813941824 2023-11-07 03:49:12,959 - handlers.py[DEBUG]: finish: modules-final/config-scripts_user: SUCCESS: config-scripts_user previously ran
813941957 2023-11-07 03:49:12,959 - modules.py[DEBUG]: Running module ssh_authkey_fingerprints (<module 'cloudinit.config.cc_ssh_authkey_fingerprints' from '/usr/lib/python3/dist-packages/cloudinit/config/cc_ssh_authkey_fingerprints.py'>) with frequency once-per-instance
813942219 2023-11-07 03:49:12,960 - handlers.py[DEBUG]: start: modules-final/config-ssh_authkey_fingerprints: running config-ssh_authkey_fingerprints with frequency once-per-instance
813942392 2023-11-07 03:49:12,960 - helpers.py[DEBUG]: config-ssh_authkey_fingerprints already ran (freq=once-per-instance)
813942506 2023-11-07 03:49:12,960 - handlers.py[DEBUG]: finish: modules-final/config-ssh_authkey_fingerprints: SUCCESS: config-ssh_authkey_fingerprints previously ran
813942663 2023-11-07 03:49:12,960 - modules.py[DEBUG]: Running module keys_to_console (<module 'cloudinit.config.cc_keys_to_console' from '/usr/lib/python3/dist-packages/cloudinit/config/cc_keys_to_console.py'>) with frequency once-per-instance
813942898 2023-11-07 03:49:12,960 - handlers.py[DEBUG]: start: modules-final/config-keys_to_console: running config-keys_to_console with frequency once-per-instance
813943053 2023-11-07 03:49:12,960 - helpers.py[DEBUG]: config-keys_to_console already ran (freq=once-per-instance)
813943158 2023-11-07 03:49:12,960 - handlers.py[DEBUG]: finish: modules-final/config-keys_to_console: SUCCESS: config-keys_to_console previously ran
813943297 2023-11-07 03:49:12,960 - modules.py[DEBUG]: Running module install_hotplug (<module 'cloudinit.config.cc_install_hotplug' from '/usr/lib/python3/dist-packages/cloudinit/config/cc_install_hotplug.py'>) with frequency once-per-instance
813943532 2023-11-07 03:49:12,960 - handlers.py[DEBUG]: start: modules-final/config-install_hotplug: running config-install_hotplug with frequency once-per-instance
813943687 2023-11-07 03:49:12,960 - helpers.py[DEBUG]: config-install_hotplug already ran (freq=once-per-instance)
813943792 2023-11-07 03:49:12,960 - handlers.py[DEBUG]: finish: modules-final/config-insta
853199989 2023-11-07 03:49:12,577 - handlers.py[DEBUG]: finish: modules-config/config-set_passwords: SUCCESS: config-set_passwords previously ran
853200125 2023-11-07 03:49:12,577 - modules.py[DEBUG]: Running module grub_dpkg (<module 'cloudinit.config.cc_grub_dpkg' from '/usr/lib/python3/dist-packages/cloudinit/config/cc_grub_dpkg.py'>) with frequency once-per-instance
853200342 2023-11-07 03:49:12,577 - handlers.py[DEBUG]: start: modules-config/config-grub_dpkg: running config-grub_dpkg with frequency once-per-instance
853200486 2023-11-07 03:49:12,577 - helpers.py[DEBUG]: config-grub_dpkg already ran (freq=once-per-instance)
853200585 2023-11-07 03:49:12,577 - handlers.py[DEBUG]: finish: modules-config/config-grub_dpkg: SUCCESS: config-grub_dpkg previously ran
853200713 2023-11-07 03:49:12,577 - modules.py[DEBUG]: Running module apt_configure (<module 'cloudinit.config.cc_apt_configure' from '/usr/lib/python3/dist-packages/cloudinit/config/cc_apt_configure.py'>) with frequency once-per-instance
853200942 2023-11-07 03:49:12,577 - handlers.py[DEBUG]: start: modules-config/config-apt_configure: running config-apt_configure with frequency once-per-instance
853201094 2023-11-07 03:49:12,578 - helpers.py[DEBUG]: config-apt_configure already ran (freq=once-per-instance)
853201197 2023-11-07 03:49:12,578 - handlers.py[DEBUG]: finish: modules-config/config-apt_configure: SUCCESS: config-apt_configure previously ran
853201333 2023-11-07 03:49:12,578 - modules.py[DEBUG]: Running module byobu (<module 'cloudinit.config.cc_byobu' from '/usr/lib/python3/dist-packages/cloudinit/config/cc_byobu.py'>) with frequency once-per-instance
853201538 2023-11-07 03:49:12,578 - handlers.py[DEBUG]: start: modules-config/config-byobu: running config-byobu with frequency once-per-instance
853201674 2023-11-07 03:49:12,578 - helpers.py[DEBUG]: config-byobu already ran (freq=once-per-instance)
853201769 2023-11-07 03:49:12,578 - handlers.py[DEBUG]: finish: modules-config/config-byobu: SUCCESS: config-byobu previously ran
853201889 2023-11-07 03:49:12,578 - main.py[DEBUG]: Ran 6 modules with 0 failures
853201961 2023-11-07 03:49:12,578 - atomic_helper.py[DEBUG]: Atomically writing to file /var/lib/cloud/data/status.json (via temporary file /var/lib/cloud/data/tmps7qco3z6) - w: [644] 542 bytes/chars
853202151 2023-11-07 03:49:12,578 - util.py[DEBUG]: Reading from /proc/uptime (quiet=False)
853202233 2023-11-07 03:49:12,578 - util.py[DEBUG]: Read 10 bytes from /proc/uptime
853202307 2023-11-07 03:49:12,578 - util.py[DEBUG]: cloud-init mode 'modules' took 0.098 seconds (0.10)
853202401 2023-11-07 03:49:12,578 - handlers.py[DEBUG]: finish: modules-config: SUCCESS: running modules for config
853202507 2023-11-07 03:49:12,919 - util.py[DEBUG]: Cloud-init v. 23.3.1-0ubuntu1~20.04.1 running 'modules:final' at Tue, 07 Nov 2023 03:49:12 +0000. Up 9.08 seconds.
853202664 2023-11-07 03:49:12,921 - util.py[DEBUG]: Reading from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json (quiet=False)
853202817 2023-11-07 03:49:12,921 - util.py[DEBUG]: Read 136743 bytes from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json
853202966 2023-11-07 03:49:12,923 - util.py[DEBUG]: Reading from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json (quiet=False)
853203119 2023-11-07 03:49:12,923 - util.py[DEBUG]: Read 136743 bytes from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json
853203268 2023-11-07 03:49:12,925 - util.py[DEBUG]: Reading from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json (quiet=False)
853203421 2023-11-07 03:49:12,925 - util.py[DEBUG]: Read 136743 bytes from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json
853203570 2023-11-07 03:49:12,926 - util.py[DEBUG]: Reading from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json (quiet=False)
853203723 2023-11-07 03:49:12,927 - util.py[DEBUG]: Read 136743 bytes from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json
853203872 2023-11-07 03:49:12,929 - util.py[DEBUG]: Reading from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json (quiet=False)
854322365 2023-11-07 03:49:12,949 - util.py[DEBUG]: Read 136743 bytes from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json
854322514 2023-11-07 03:49:12,951 - util.py[DEBUG]: Reading from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json (quiet=False)
854322667 2023-11-07 03:49:12,951 - util.py[DEBUG]: Read 136743 bytes from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json
854322816 2023-11-07 03:49:12,952 - util.py[DEBUG]: Reading from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json (quiet=False)
854322969 2023-11-07 03:49:12,952 - util.py[DEBUG]: Read 136743 bytes from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json
854323118 2023-11-07 03:49:12,953 - util.py[DEBUG]: Reading from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json (quiet=False)
854323271 2023-11-07 03:49:12,953 - util.py[DEBUG]: Read 136743 bytes from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json
854323420 2023-11-07 03:49:12,955 - util.py[DEBUG]: Reading from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json (quiet=False)
854323573 2023-11-07 03:49:12,955 - util.py[DEBUG]: Read 136743 bytes from /usr/lib/python3/dist-packages/cloudinit/config/schemas/schema-cloud-config-v1.json
854323722 2023-11-07 03:49:12,956 - stages.py[DEBUG]: Using distro class <class 'cloudinit.distros.ubuntu.Distro'>
854323827 2023-11-07 03:49:12,957 - modules.py[INFO]: Skipping modules 'package_update_upgrade_install,fan,landscape,lxd,ubuntu_drivers,write_files_deferred,puppet,chef,ansible,mcollective,salt_minion,phone_home,power_state_change' because no applicable config is provided.
854324091 2023-11-07 03:49:12,958 - modules.py[DEBUG]: Running module reset_rmc (<module 'cloudinit.config.cc_reset_rmc' from '/usr/lib/python3/dist-packages/cloudinit/config/cc_reset_rmc.py'>) with frequency once-per-instance
854324308 2023-11-07 03:49:12,958 - handlers.py[DEBUG]: start: modules-final/config-reset_rmc: running config-reset_rmc with frequency once-per-instance
854324451 2023-11-07 03:49:12,958 - helpers.py[DEBUG]: config-reset_rmc already ran (freq=once-per-instance)
854324550 2023-11-07 03:49:12,958 - handlers.py[DEBUG]: finish: modules-final/config-reset_rmc: SUCCESS: config-reset_rmc previously ran
854324677 2023-11-07 03:49:12,958 - modules.py[DEBUG]: Running module rightscale_userdata (<module 'cloudinit.config.cc_rightscale_userdata' from '/usr/lib/python3/dist-packages/cloudinit/config/cc_rightscale_userdata.py'>) with frequency once-per-instance
854324924 2023-11-07 03:49:12,958 - handlers.py[DEBUG]: start: modules-final/config-rightscale_userdata: running config-rightscale_userdata with frequency once-per-instance
854325087 2023-11-07 03:49:12,958 - helpers.py[DEBUG]: config-rightscale_userdata already ran (freq=once-per-instance)
854325196 2023-11-07 03:49:12,958 - handlers.py[DEBUG]: finish: modules-final/config-rightscale_userdata: SUCCESS: config-rightscale_userdata previously ran
854325343 2023-11-07 03:49:12,958 - modules.py[DEBUG]: Running module scripts_vendor (<module 'cloudinit.config.cc_scripts_vendor' from '/usr/lib/python3/dist-packages/cloudinit/config/cc_scripts_vendor.py'>) with frequency once-per-instance
854325575 2023-11-07 03:49:12,958 - handlers.py[DEBUG]: start: modules-final/config-scripts_vendor: running config-scripts_vendor with frequency once-per-instance
854325728 2023-11-07 03:49:12,958 - helpers.py[DEBUG]: config-scripts_vendor already ran (freq=once-per-instance)
854325832 2023-11-07 03:49:12,958 - handlers.py[DEBUG]: finish: modules-final/config-scripts_vendor: SUCCESS: config-scripts_vendor previously ran
854325969 2023-11-07 03:49:12,958 - modules.py[DEBUG]: Running module scripts_per_once (<module 'cloudinit.config.cc_scripts_per_once' from '/usr/lib/python3/dist-packages/cloudinit/config/cc_scripts_per_once.py'>) with frequency once
854326194 2023-11-07 03:49:12,958 - handlers.py[DEBUG]: start: modules-final/config-scripts_per_once: running config-scripts_per_once with frequency onc
807193888 Nov  7 03:49:13 dbserver systemd[1]: Reached target Cloud-init target.
807193959 Nov  7 03:49:13 dbserver systemd[1]: Startup finished in 2.835s (kernel) + 6.375s (userspace) = 9.210s.
807194063 Nov  7 03:49:13 dbserver systemd[1]: dmesg.service: Succeeded.
807194126 Nov  7 03:49:13 dbserver ModemManager[682]: <info>  [base-manager] couldn't check support for device '/sys/devices/pci0000:00/0000:00:03.0': not supported by any plugin
792046608 Nov  7 03:49:18 2023 from 10.0.2.72
792945836 Last login: Tue Nov  7 03:49:18 2023 from 10.0.2.72
807194295 Nov  7 03:49:18 dbserver systemd[1]: Created slice User Slice of UID 1000.
807194370 Nov  7 03:49:18 dbserver systemd[1]: Starting User Runtime Directory /run/user/1000...
807194457 Nov  7 03:49:18 dbserver systemd[1]: Finished User Runtime Directory /run/user/1000.
807194542 Nov  7 03:49:18 dbserver systemd[1]: Starting User Manager for UID 1000...
807194617 Nov  7 03:49:18 dbserver systemd[841]: Reached target Paths.
807194678 Nov  7 03:49:18 dbserver kernel: [   14.730108] systemd-journald[369]: File /var/log/journal/4f0071a3652e44d1a2fe6090a2ad34b5/user-1000.journal corrupted or uncleanly shut down, renaming and replacing.
807194880 Nov  7 03:49:18 dbserver systemd[841]: Reached target Timers.
807194942 Nov  7 03:49:18 dbserver systemd[841]: Starting D-Bus User Message Bus Socket.
807195021 Nov  7 03:49:18 dbserver systemd[841]: Listening on GnuPG network certificate management daemon.
807195118 Nov  7 03:49:18 dbserver systemd[841]: Listening on GnuPG cryptographic agent and passphrase cache (access for web browsers).
807195244 Nov  7 03:49:18 dbserver systemd[841]: Listening on GnuPG cryptographic agent and passphrase cache (restricted).
807195357 Nov  7 03:49:18 dbserver systemd[841]: Listening on GnuPG cryptographic agent (ssh-agent emulation).
807195458 Nov  7 03:49:18 dbserver systemd[841]: Listening on GnuPG cryptographic agent and passphrase cache.
807195558 Nov  7 03:49:18 dbserver systemd[841]: Listening on debconf communication socket.
807195640 Nov  7 03:49:18 dbserver systemd[841]: Listening on REST API socket for snapd user session agent.
807195738 Nov  7 03:49:18 dbserver systemd[841]: Listening on D-Bus User Message Bus Socket.
807195821 Nov  7 03:49:18 dbserver systemd[841]: Reached target Sockets.
807195884 Nov  7 03:49:18 dbserver systemd[841]: Reached target Basic System.
807195952 Nov  7 03:49:18 dbserver systemd[841]: Reached target Main User Target.
807196024 Nov  7 03:49:18 dbserver systemd[841]: Startup finished in 51ms.
807196089 Nov  7 03:49:18 dbserver systemd[1]: Started User Manager for UID 1000.
807196161 Nov  7 03:49:18 dbserver systemd[1]: Started Session 1 of user paco.
813562668 Last login: Tue Nov  7 03:49:18 2023 from 10.0.2.72
847035616 Tue Nov  7 03:49:18 2023
794654736 SYSLOG_TIMESTAMP=Nov  7 03:49:31
807196230 Nov  7 03:49:31 dbserver systemd-resolved[637]: Using degraded feature set (UDP) for DNS server 192.168.1.1.
794658136 SYSLOG_TIMESTAMP=Nov  7 03:49:33
807196339 Nov  7 03:49:37 dbserver systemd[1]: systemd-fsckd.service: Succeeded.
794659256 SYSLOG_TIMESTAMP=Nov  7 03:49:38
807196410 Nov  7 03:49:38 dbserver systemd[1]: session-1.scope: Succeeded.
807196475 Nov  7 03:49:41 dbserver systemd[1]: systemd-timedated.service: Succeeded.
807196550 Nov  7 03:49:45 dbserver systemd[1]: Started Session 3 of user paco.
807196619 Nov  7 03:49:50 dbserver systemd-timesyncd[604]: Timed out waiting for reply from 185.125.190.58:123 (ntp.ubuntu.com).
807196738 Nov  7 03:49:53 dbserver systemd-timesyncd[604]: Initial synchronization to time server 185.125.190.56:123 (ntp.ubuntu.com).
807196863 Nov  7 03:50:17 dbserver kernel: [   71.350925] process 'pkexecc' launched '/bin/sh' with NULL argv: empty string added
773835917 Nov  7 03:51:49 dbserver systemd[1118]: Listening on GnuPG cryptographic agent (ssh-agent emulation).
773836019 Nov  7 03:51:49 dbserver systemd[1118]: Listening on GnuPG cryptographic agent and passphrase cache.
773836120 Nov  7 03:51:49 dbserver systemd[1118]: Listening on debconf communication socket.
773836203 Nov  7 03:51:49 dbserver systemd[1118]: Listening on REST API socket for snapd user session agent.
773836302 Nov  7 03:51:49 dbserver systemd[1118]: Listening on D-Bus User Message Bus Socket.
773836386 Nov  7 03:51:49 dbserver systemd[1118]: Reached target Sockets.
773836450 Nov  7 03:51:49 dbserver systemd[1118]: Reached target Basic System.
773836519 Nov  7 03:51:49 dbserver systemd[1118]: Reached target Main User Target.
773836592 Nov  7 03:51:49 dbserver systemd[1118]: Startup finished in 50ms.
773836658 Nov  7 03:51:49 dbserver systemd[1]: Started User Manager for UID 0.
773836727 Nov  7 03:51:49 dbserver systemd[1]: Started Session 4 of user root.
807196983 Nov  7 03:51:49 dbserver systemd[1]: Created slice User Slice of UID 0.
807197055 Nov  7 03:51:49 dbserver systemd[1]: Starting User Runtime Directory /run/user/0...
807197139 Nov  7 03:51:49 dbserver systemd[1]: Finished User Runtime Directory /run/user/0.
807197221 Nov  7 03:51:49 dbserver systemd[1]: Starting User Manager for UID 0...
807197293 Nov  7 03:51:49 dbserver systemd[1118]: Reached target Paths.
807197355 Nov  7 03:51:49 dbserver systemd[1118]: Reached target Timers.
807197418 Nov  7 03:51:49 dbserver systemd[1118]: Starting D-Bus User Message Bus Socket.
807197498 Nov  7 03:51:49 dbserver systemd[1118]: Listening on GnuPG network certificate management daemon.
807197596 Nov  7 03:51:49 dbserver systemd[1118]: Listening on GnuPG cryptographic agent and passphrase cache (access for web browsers).
807197723 Nov  7 03:51:49 dbserver systemd[1118m]|o[dt][tspgfc]|od[bm]|oxt|epub|apk|aab|ipa|do[ct][xm]|p[op]t[mx]|xl[st][xm]|pyz|whl)
817769604 Nov  7 03:51:49 dbserver systemd: pam_unix(systemd-user:session): session opened for user root by (uid=0)
773836796 Nov  7 03:52:01 dbserver cron[653]: (root) INSECURE MODE (mode 0600 expected) (crontabs/root)
773836890 Nov  7 03:52:37 dbserver kernel: [  211.110934] lime: module verification failed: signature and/or required key missing - tainting kernel
...
```

<p>

- identify the <strong>Linux kernel</strong> and <strong>OS version</strong></p>


```bash
(volatility) ...$ python3 vol.py -f linux.mem banners.Banners
Volatility 3 Framework 2.27.0
Progress:  100.00               PDB scanning finished
Offset  Banner

0x2f9c4c88      Linux version 5.4.0-166-generic (buildd@lcy02-amd64-011) (gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.2)) #183-Ubuntu SMP Mon Oct 2 11:28:33 UTC 2023 (Ubuntu 5.4.0-166.183-generic 5.4.252)
0xa707c8c8      Linux version 5.4.0-166-generic (buildd@lcy02-amd64-011) (gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.2)) #183-Ubuntu SMP Mon Oct 2 11:28:33 UTC 2023 (Ubuntu 5.4.0-166.183-generic 5.4.252)
0xd46001a0      Linux version 5.4.0-166-generic (buildd@lcy02-amd64-011) (gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.2)) #183-Ubuntu SMP Mon Oct 2 11:28:33 UTC 2023 (Ubuntu 5.4.0-166.183-generic 5.4.252)
0xd619de54      Linux version 5.4.0-166-generic (buildd@lcy02-amd64-011) (gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.2)) #183-Ubuntu SMP Mon Oct 2 11:28:33 UTC 2023 (Ubuntu 5.4.0-166.183-generic 5.4.252)
0x106d64c88     Linux version 5.4.0-166-generic (buildd@lcy02-amd64-011) (gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.2)) #183-Ubuntu SMP Mon Oct 2 11:28:33 UTC 2023 (Ubuntu 5.4.0-166.183-generic 5.4.252)
```

<img width="1892" height="168" alt="image" src="https://github.com/user-attachments/assets/d78403c1-9670-4779-9683-5bfdb86f15dc" />


<br>
<br>
<br>
<p>1.3. What is the MD5 hash of the malicious file found?<br>
<code>0511ccaad402d6d13ce801e1e9136ba2</code></p>


```bash
(volatility) ...$ python3 vol.py -f linux.mem linux.pagecache.InodePages --find /home/paco/pkexecc --dump rose
```

```bash
(volatility) ...$ md5 rose
0511ccaad402d6d13ce801e1e9136ba2  rose
```

<br>
<br>
<br>
<p>1.4. What is the IP address and port of the malicious actor? Format is IP:Port<br>
<code>10.0.2.72:1337</code></p>

```bash
$ cat challenge_strings.txt | grep success | grep -E hostname=
788623280 op=PAM:session_open grantors=pam_selinux,pam_loginuid,pam_keyinit,pam_permit,pam_umask,pam_unix,pam_systemd,pam_mail,pam_limits,pam_env,pam_env,pam_selinux acct="root" exe="/usr/sbin/sshd" hostname=10.0.2.72 addr=10.0.2.72 terminal=ssh res=success
794885520 op=PAM:setcred grantors=pam_permit,pam_cap acct="paco" exe="/usr/sbin/sshd" hostname=10.0.2.72 addr=10.0.2.72 terminal=ssh res=success
797840336 unit=user-runtime-dir@0 comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=success
797849440 unit=user@1000 comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=success
798330560 unit=networkd-diunit=user@1000 comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=success
```

```bash
$ cat challenge_strings.txt  | grep '03:49:' | grep 10.0.2.72
792046608 Nov  7 03:49:18 2023 from 10.0.2.72
792945836 Last login: Tue Nov  7 03:49:18 2023 from 10.0.2.72
813562668 Last login: Tue Nov  7 03:49:18 2023 from 10.0.2.72
```

```bash
$ cat challenge_strings.txt  | grep 'login' | grep 10.0.2.72
788623280 op=PAM:session_open grantors=pam_selinux,pam_loginuid,pam_keyinit,pam_permit,pam_umask,pam_unix,pam_systemd,pam_mail,pam_limits,pam_env,pam_env,pam_selinux acct="root" exe="/usr/sbin/sshd" hostname=10.0.2.72 addr=10.0.2.72 terminal=ssh res=success
792945836 Last login: Tue Nov  7 03:49:18 2023 from 10.0.2.72
802203095 ntors=pam_selinux,pam_loginuid,pam_keyinit,pam_permit,pam_umask,pam_unix,pam_systemd,pam_mail,pam_limits,pam_env,pam_env,pam_selinux acct="paco" exe="/usr/sbin/sshd" hostname=10.0.2.72 addr=10.0.2.72 terminal=ssh res=success
805753872 op=login id=1000 exe="/usr/sbin/sshd" hostname=10.0.2.72 addr=10.0.2.72 terminal=/dev/pts/0 res=success
813562668 Last login: Tue Nov  7 03:49:18 2023 from 10.0.2.72
821611600 op=login id=1000 exe="/usr/sbin/sshd" hostname=10.0.2.72 addr=10.0.2.72 terminal=/dev/pts/0 res=success
```

<br>
<br>
<br>
<p>1.5. What is the full path of the cronjob file and its inode number? Format is filename:inode number<br>
<code>/var/spool/cron/crontabs/root:******</code></p>

```bash
$ cat challenge_strings.txt | grep 'crontab' | sort
2794780940 crontab:x:105:
2800802112 crontabs/root
2800804240 echo '* * * * * cp /opt/.bashrc /root/.bashrc' >> /crontabs/root
2800804384 echo '* * * * * cp /opt/.bashrc /root/.bashrc' >> /var/spool/cron/crontabs/root
2800804656 crontabs/root
2811377564 crontab:x:105:
2821608752 echo '* * * * * cp /opt/.bashrc /root/.bashrc' >> /var/spool/cron/crontabs/root
2821609056 /var/spool/cron/crontabs/root
2831895612 Nov  7 03:52:01 dbserver cron[653]: (root) INSECURE MODE (mode 0600 expected) (crontabs/root)
2832019324 crontab:x:105:
3766027520 crontab
3766062588 crontab:x:105:
3777316064 crontabs/root
3837163628 crontab:x:105:
3850116140 crontab:x:105:
3850347340 crontab:x:105:
3851054988 crontab:x:105:
3868154672 <78>Nov  7 03:52:01 cron[653]: (root) INSECURE MODE (mode 0600 expected) (crontabs/root)
3885059984 crontabZ1
3973092864 MESSAGE=(root) INSECURE MODE (mode 0600 expected) (crontabs/root)
4055705702 aP 7 03:52:01 cron[653]: (root) INSECURE MODE (mode 0600 expected) (crontabs/root)
4101957468 crontab:x:105:
4102338592 root) INSECURE MODE (mode 0600 expected) (crontabs/root)gent.e..restricted).eb browsers).0000:00:03.0': not supported by any plugin
4102969760 <78>Nov  7 03:52:01 cron[653]: (root) INSECURE MODE (mode 0600 expected) (crontabs/root)
4114833051 crontabs
4114833060 /etc/crontab
4114833520 Error: %s; while reading crontab for user %s
4114833568 fdopen on crontab_fd in load_user
4114833880 Missing newline before EOF, this crontab file will be ignored
4114833944 Syntax error, this crontab file will be ignored
4114833992 crontab must not be longer than 10000 lines, this crontab file will be ignored
4114834071 Out of memory parsing crontab
4121795744 crontabs
4130013516 crontab:x:105:
4170038368 # /etc/crontab: system-wide crontab
4170038404 # Unlike any other crontab you don't have to run the `crontab'
4170038595 # that none of the other crontabs do.
4170753024 :01 cron[653]: (root) INSECURE MODE (mode 0600 expected) (crontabs/root)
4170914108 crontab:x:10
4185965159 I 7 03:52:01 cron[653]: (root) INSECURE MODE (mode 0600 expected) (crontabs/root)
4192950616 crontab
4192950808 crontabs
4223050740 crontabt
773836796 Nov  7 03:52:01 dbserver cron[653]: (root) INSECURE MODE (mode 0600 expected) (crontabs/root)
773960508 crontab:x:105:
788715760 echo '* * * * * cp /opt/.bashrc /root/.bashrc' >> /var/spool/cron/crontabs/root
788716064 /var/spool/cron/crontabs/root
795261788 crontab:x:105:
805657856 crontabs/root
805659984 echo '* * * * * cp /opt/.bashrc /root/.bashrc' >> /var/spool/cron/crontabs/root
805660128 echo '* * * * * cp /opt/.bashrc /root/.bashrc' >> /var/spool/cron/crontabs/root
805660400 crontabs/root
808025292 crontab:x:105:
```

<br>
<br>
<br>
<p>1.6. What command is found inside the cronjob file?r<br>
<code>* * * * * cp /opt/.bashrc /root/.bashrc</code></p>

```bash
$ strings -a -td linux.mem > challenge_strings.txt
```

```bash
$ grep -A 2 "crontabs/root" challenge_strings.txt | grep "echo"
788715760 echo '* * * * * cp /opt/.bashrc /root/.bashrc' >> /var/spool/cron/crontabs/root
805659984 echo '* * * * * cp /opt/.bashrc /root/.bashrc' >> /var/spool/cron/crontabs/root
805660128 echo '* * * * * cp /opt/.bashrc /root/.bashrc' >> /var/spool/cron/crontabs/root
```

<img width="1640" height="64" alt="image" src="https://github.com/user-attachments/assets/2796e8ad-43d2-4833-b1e9-a8a2ebc2ce39" />

<br>
<br>
<br>
<h1 align="center">Completed</h1>

<p align="center"><img width="800px" src="https://github.com/user-attachments/assets/44aead2d-c8eb-467c-80be-1320b3a325ee"><br><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/d97b3d68-c9ad-4232-bb26-196140c95590"></p>


<h1 align="center">My TryHackMe Journey ・ 2025, December</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|25      |Medium 🚩 - Profiles                             |9 |     100ᵗʰ  |     3ʳᵈ    |   13,969ᵗʰ   |      156ᵗʰ     |    135,198  |    1,051    |    84     |
|24      |Medium 🔗 - YARA Rules - YARA mean one!          |8 |     100ᵗʰ  |     3ʳᵈ    |   10,263ʳᵈ   |      127ᵗʰ     |    135,168  |    1,050    |    84     |
|24      |Easy 🔗 - Exploitation with cURL - Hoperation Eggsploit|8 |100ᵗʰ |     3ʳᵈ    |   12,804ᵗʰ   |      154ᵗʰ     |    135,144  |    1,049    |    84     |
|24      |Medium 🔗 - Phishing - Phismas Greetings         |8 |     100ᵗʰ  |     3ʳᵈ    |   14,507ᵗʰ   |      174ᵗʰ     |    135,112  |    1,048    |    84     |
|24      |Easy 🔗 - n8n: CVE-2025-68613                    |8 |     102ⁿᵈ  |     3ʳᵈ    |   18,279ᵗʰ   |      205ᵗʰ     |    135,064  |    1,047    |    84     |
|24      |Medium 🔗 - C2 Detection - Command & Carol       |8 |     101ˢᵗ  |     3ʳᵈ    |   17,260ᵗʰ   |      193ʳᵈ     |    135,048  |    1,046    |    84     |
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

<p align="center">Global All Time:    100ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/e6386fad-578c-4e77-bab0-897b1ceb479a"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/730057cc-4d06-4eb8-9130-044859636a54"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/ae500d44-8f2b-4830-a2d4-c2b0e0e1fa55"><br><br>
                  Global monthly:  13,969ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/a58a5e76-4f9e-417d-a907-19d2e384ed8c"><br><br>
                  Brazil monthly:     156ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/45bdf71e-ec5a-4f29-bfb0-deab6fe36d8f"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
