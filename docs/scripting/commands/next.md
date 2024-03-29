# `next()`

!!! warning
	This page may contain outdated information, incompatible with the current version of Hercules and its coding standards.

## Syntax

```c
next();
```

!!! warning
	The rest of this document hasn't been converted to Markdown yet.

== Description ==
This command will display a 'next' button in the message window for the invoking character. Clicking on it will cause the window to clear and display a new one. Used to segment NPC-talking, next is often used in combination with [[mes]] and [[close]].

If no window is currently on screen, one will be created, but once the invoking character clicks on it, a warning is thrown on the server console and the script will terminate.

== Example ==
 [[mes]] "[Next Example]";
 mes "Click the next button to see next part of npc.";

 '''next'''; //This will display the button.

 mes "[Next Example]";
 mes "This is rest of the part.";
 [[close]]; //Closes the window and ends the script.
