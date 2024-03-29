# `misceffect()`

!!! warning
	This page may contain outdated information, incompatible with the current version of Hercules and its coding standards.

## Syntax

```c
misceffect(<effect number>);
```

!!! warning
	The rest of this document hasn't been converted to Markdown yet.

== Description ==
This command, if run from an NPC object that has a sprite, will call up a specified effect number, centered on the NPC sprite. If the running code does not have an object ID (a 'floating' NPC) or is not running from an NPC object at 
all (an item script) the effect will be centered on the character who's RID got attached to the script, if any. For usable item scripts, this command will create an effect centered on the player using the item.

A full list of known effects is found in [`doc/effect_list.txt`](https://github.com/HerculesWS/Hercules/blob/stable/doc/effect_list.txt) The list of those that actually work may differ greatly between client versions.
