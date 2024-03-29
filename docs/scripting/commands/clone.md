# `clone()`

!!! warning
	This page may contain outdated information, incompatible with the current version of Hercules and its coding standards.

## Syntax

```c
clone("<map name>", <x>, <y>, "<event>", <char id>{, <master_id>{, <mode>{, <flag>, <duration>}}});
```

## Description

This command creates a monster which is a copy of another player. The first
four arguments serve the same purpose as in the monster script command. The
`char id` is the character ID of the player to clone (player must be online).
If `master_id` is given, the clone will be a 'slave/minion' of it. `master_id`
must be a character ID of another online player.

The mode can be specified to determine the behavior of the clone, it's
values are the same as the ones used for the mode field in the mob_db. The
default mode is aggressive, assists, can move, can attack.

`flag` can be either zero or one currently. If zero, the clone is a normal
monster that'll target players, if one, it is considered a summoned monster,
and as such, it'll target other monsters. Defaults to zero.

The duration specifies how long the clone will live before it is auto-removed.
Specified in seconds, defaults to no limit (zero).

Returned value is the monster ID of the spawned clone. If command fails,
returned value is zero.

## Example

```c
clone("prontera", 150, 150, "Test::OnEvent", getcharid(0));
```
