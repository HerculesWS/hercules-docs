# `specialeffect()`

!!! warning
	This page may contain outdated information, incompatible with the current version of Hercules and its coding standards.

## Syntax

```c
specialeffect(<effect>{, <target>{, "<NPC name>"}});
```

!!! warning
	The rest of this document hasn't been converted to Markdown yet.

==Description==

This script command will display a given special effect on the attached, or specified if <NPC name> is provided, NPC. If <NPC name> is provided but the NPC does not exist then the script command will not perform. If the NPC does exist, but has no visible presence on the screen, then it is possible that the client may crash or behave peculiarly.

==Parameters==
===Effect===

The effect to display in the client. Some effects are unsupported in the client so it is recommended to find the ID of a working effect before using the ID in this command.
'''For a list of IDs''', please see [`doc/effect_list.txt`](https://github.com/HerculesWS/Hercules/blob/stable/doc/effect_list.txt)

===Target===

Specifies how the effect should be distributed graphically. By default, the target is flagged as AREA which means all players within client range will see the effect. Otherwise, when specified the effect will only apply and be sent to clients which match the target property.

===NPC Name===

Specifies which NPC the effect should apply to, rather than the NPC which is currently running. If the NPC named does not exist then the effect will not be performed.

==Examples==
* Perform the item heal effect on the running NPC.
<pre>specialeffect 7;</pre>
* Perform the item heal effect on the running NPC, but only visible to the attached player.
<pre>specialeffect 7, SELF;</pre>
* Perform the item heal effect on the running NPC, but only visible to party members of the player attached, excluding the player.
<pre>specialeffect 7, PARTY_WOS;</pre>
