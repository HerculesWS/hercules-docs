# `network.conf`

Network.conf consists of three main sections:

## lan_subnets

This section is where you put the subnets your server is on internally behind your router or other networking equipment.

It is unclear if you should place your WAN IP in here somewhere in order to allow external connections or not. The old
subnet system did require this, though it seems like it might not be required here.

## allowed

This is a list of IPs your char-server and map-server are allowed to connect from. Default is 0.0.0.0:0.0.0.0 (any IP
and any subnet), though it is recommended to change this to the specific IPs they will be connecting from. It is unclear
if this needs to be your WAN or LAN address though.

## trusted

Same as "allowed", except the IPs on this list are exempt from being banned for failed passwords and such.

This configuration file is in dire need of better documentation.
