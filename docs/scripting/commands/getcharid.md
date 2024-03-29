# `getcharid()`

!!! warning
	This page may contain outdated information, incompatible with the current version of Hercules and its coding standards.

## Syntax

```c
getcharid(<type>{, "<character name>"});
```

## Description

This function will return a unique ID number of the invoking character, or, if a character name is specified, of that character.

For most purposes other than printing it, a number is better to have than a name (people do horrifying things to their character names).

If the character is not in a party or not in a guild, the function will return 0 if guild or party number is requested. If a name is specified and the character is not found, 0 is returned.

If `getcharid(0)` returns a zero, the script got called not by a character and doesn't have an attached [RID](../RID.md). Note that this will cause the map server to print "player not attached!" error messages, so it is preferred to use [`playerattached()`](playerattached.md) to check for the character attached to the script.

### Type Values

| Value | Description |
| ----- | ----------- |
| 0 | Character ID number. |
| 1 | Party ID number. |
| 2 | Guild ID number. |
| 3 | Account ID number. |
| 4 | Battleground ID number. |

## Examples

```c
if (getcharid(2) == 0)
	mes("Only members of a guild are allowed here!");

// This code will get charid from not attached player, if he is online (useful in dialogues)
input(.@charname$);
if (getcharid(.@charname$,0) > 0) {
	do_something();
}
```
