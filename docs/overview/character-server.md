!!! warning
	This page may contain outdated information, incompatible with the current version of Hercules and its coding standards.

## Character Server Overview

Character Server is where users/players go through while Character Select or Making new character.
[Map Server](./map-server.md) also use this server to handle character data saving and load process. Character Server
also holding inside it a [Inter Server](./inter-server.md).

## Character Server Tasks

- Process Character Select / Making new Character
- Load/Save Character Data and send it to Map Server
- Load/Save Character and Account based variables

## Inter Server Overview

Inter Server is made to sync between all [Map servers](./map-server.md), in case you're using
Multi Zone System it will take care of sync all your servers.

## Inter Server Tasks

- Taking Care of Sync between all Map Servers
