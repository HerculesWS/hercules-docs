# `set()`

!!! warning
	This page may contain outdated information, incompatible with the current version of Hercules and its coding standards.

## Syntax

```c
set(<variable>, <expression>);
```

```c
<variable> = <expression>;
```

!!! warning
	The rest of this document hasn't been converted to Markdown yet.

== Description ==
This command will set a variable to the value that the expression results in. <br />

This is the most basic script command and is used a lot whenever you try to do 
anything more advanced than just printing text into a message box.

Returns the variable reference (since trunk {{rev|12870}}).

== Examples ==
 [[set]] .@x,100;  // will make .@x equal 100.
 
 [[set]] .@x,1+5/8+9;  // will compute 1+5/8+9 (which is, surprisingly, 10 - remember, all numbers are integer in this language) and make .@x equal it.

or
 .@x = 100;  // will make .@x equal 100.
 
 .@x = 1+5/8+9;  // will compute 1+5/8+9 (which is, surprisingly, 10 - remember, all numbers are integer in this language) and make .@x equal it.

For more information read: [http://rathena.org/board/topic/62395-r15982-script-engine-update/ r15982: Script Engine Update]
