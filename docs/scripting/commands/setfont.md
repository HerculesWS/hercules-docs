# `setfont()`

!!! warning
	This page may contain outdated information, incompatible with the current version of Hercules and its coding standards.

## Syntax

```c
setfont("< font >");
```

!!! warning
	The rest of this document hasn't been converted to Markdown yet.

==Description==
<p>This command sets the current RO client interface font to one of the fonts 
stored in data\*.eot by using an ID of the font. When the ID of the 
currently used font is used, default interface font is used again.</p>
	
:	0 - Default<br>
:	1 - RixLoveangel<br>
:	2 - RixSquirrel<br>
:	3 - NHCgogo<br>
:	4 - RixDiary<br>
:	5 - RixMiniHeart<br>
:	6 - RixFreshman<br>
:	7 - RixKid<br>
:	8 -: RixMagic<br>
:	9 - RixJJangu<br>

==Examples==
 	Id: 12287
 	AegisName: "Love_Angel"
 	Name: "Love Angel Magic Powder"
 	Type: 11
 	Buy: 0
 	Script: <" setfont 1; ">
