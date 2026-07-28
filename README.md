# Breakglass Dynamic Secrets

### Background
A breakglass user is a user with elevated privileges that can be used to access a system or network device in case of emergency or unforeseen circumstances where other (externally authenticated) users are inaccessible.

In order to preserve the secret, this codebase aims to provide a proof-of-concept in Python that:
* Ingests syslog from a network device
* Parses the syslog to see when a targeted user logs in to the device
* Generates a new secret for the user
* Deploys the secret in the secret manager
* Deploys the secret to the network device

This solution also supports triggering a secret rotation ad-hoc.

### Prerequisites

This is ideally fit into a solution with pre-existing network automation as the device configuration would be stored within the codeforge (in Gitea in this case).
