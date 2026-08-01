# Util docker-compose file

This folder is what makes this a real proof of concept, here lies the systems side of the proof of concept, what pulls it together.

(topology diagram)[./diagram.png]

This (at present) is a series of python scripts (to be packaged at a later date) but they're useless when used as a part of a wider network automation service. To replicate this, I've added this `docker-compose.yaml` file to simulate this.

The compose file is brought up by entering this dir then running `docker-compose up -d`. once the containers are up you'll need to visit gitea at [git.localhost](git.localhost) to create an Oauth application to sync with [Woodpecker](woodpecker.localhost). More instructions are in `docker-compose.yaml`.

Additionally, code secrets (especially not a break-glass credential) should not be stored in plaintext anywhere so the secret will be stored within hashicorp [vault](vault.localhost), a secrets manager.
