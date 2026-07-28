This folder is what makes this a real proof of concept, here lies a virtual lab of all the components needed to execute this proof of concept, running in (containerlab)[].

(topology diagram)[./diagram.png]

This is deployed as a container running on the network to search for a root/emergency local user via syslog, if it finds the user then it sends an api call to a CI/automation tool to generate a new password, store it in the secret manager and deploy the new credential on the network device.

For this proof-of-concept I have used (Juniper's cSRX)[https://www.juniper.net/gb/en/products/security/srx-series/csrx-containerized-firewall.html] as the network device, (Gitea)[] as the code forge, (Woodpecker CI)[] as the CI engine, (OpenBao)[https://openbao.org/] as the secret manager and this application running on a containerised VM.

The code for the log generator can be found here: https://github.com/seth-paxton/syslog-generator
