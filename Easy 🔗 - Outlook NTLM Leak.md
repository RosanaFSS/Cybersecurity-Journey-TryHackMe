<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/0984f3eb-caec-4caa-8946-909847138306b"><br>
June 16, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure,<br>
part of my <code>406</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br>
Leak password hashes from a user by sending them an email by abusing CVE-2023-23397. Click <a href="https://tryhackme.com/room/outlookntlmleak"</a> here to access this challenge.<br>
<img width="1200px" src=""></p>



<h2> Task 1 . Flags</h2>

```bash
root@ip-10-10-13-46:~/Heist# RPC_URL=http://10.10.141.163:8545
root@ip-10-10-13-46:~/Heist# API_URL=http://10.10.141.163
root@ip-10-10-13-46:~/Heist# PRIVATE_KEY=$(curl -s ${API_URL}/challenge | jq -r ".player_wallet.private_key")
root@ip-10-10-13-46:~/Heist# CONTRACT_ADDRESS=$(curl -s ${API_URL}/challenge | jq -r ".contract_address")
root@ip-10-10-13-46:~/Heist# PLAYER_ADDRESS=$(curl -s ${API_URL}/challenge | jq -r ".player_wallet.address")
root@ip-10-10-13-46:~/Heist# is_solved=`cast call $CONTRACT_ADDRESS "isSolved()(bool)" --rpc-url ${RPC_URL}`
root@ip-10-10-13-46:~/Heist# echo "Check if is solved: $is_solved"
Check if is solved: false
root@ip-10-10-13-46:~/Heist# ls
root@ip-10-10-13-46:~/Heist# 

```
