# `strnpcinfo()`

!!! warning
	This page may contain outdated information, incompatible with the current version of Hercules and its coding standards.

## Syntax

```c
strnpcinfo(<type>);
```

!!! warning
	The rest of this document hasn't been converted to Markdown yet.

==Description==
This function will return the various parts of the name of the calling [[NPC]]. Whatever it returns is determined by type.

==Type Values==
{| {| class="wikitable" border="1"
!Value
!Description
|-
|0||The NPC's display name (visible#hidden).
|-
|1||The visible part of the NPC's display name.
|-
|2||The hidden part of the NPC's display name
|-
|3||The NPC's unique name (::name).
|-
|4||The name of the map the NPC is in.
|}

==Examples==
 monk_test,306,151,5	script	Sealed Shrine#1::SS_1	111,{
 	[[mes]] '''strnpcinfo'''(0); // Sealed Shrine#1
 	mes strnpcinfo(1); // Sealed Shrine
 	mes strnpcinfo(2); // 1
 	mes strnpcinfo(3); // SS_1
 	mes strnpcinfo(4); // monk_test
 	[[close]];
 }
