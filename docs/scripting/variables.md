# Variables

## Introduction

When you are writing a new script, or altering a current script, it is very likely that you will need to store values
and also look them up. Variables do exactly this. They are commonly compared to the files and folders in a filing
cabinet. You can store a value or text in a variable, and look it up later again, or even change it. This article will
cover the different kinds of variables which exist in the Athena Scripting Language. It will also process their common
use, their scopes and limits. Also, each variable will be accompanied by a small example.

## Overview of Variables

[Hercules](../about/index.md) uses different kind of variables for different kinds of situations. Variables come in
different forms and sizes. Each variable type has a different scope, from temporal player and NPC variables all up to
global system variables. Integer values (Integer values are whole numbers, like 0, 1, 2, 1487, -73452) are stored in a
different way than String values (String means text or a single letter, like "I love you!" or "x"). Some types of script
variables even support a single dimension array. But if this all is too much for you, it will all become clear in time.
First, the overview of which variables are allowed and which aren't.

### Allowed Variables

| Prefix | Type           | Normal | Array | Exceptions                      |
|--------|----------------|--------|-------|---------------------------------|
| *none* | Character      | OK!    | FAIL! | temporary version allows arrays |
| `#`    | Account        | OK!    | FAIL! | no temporary version            |
| `##`   | Global Account | OK!    | FAIL! | no temporary version            |
| `.`    | NPC            | OK!    | OK!   | *none*                          |
| `$`    | Global         | OK!    | OK!   | *none*                          |

The schema shown above goes for each type of variable, no matter if it is temporary or permanent, integer or a string
variable.

### Format of Variables

Unlike C, Java or any coding language, with scripting, the type of variable is determined by the name, not by the
declaration. For example, to make a variable in C an Integer variable, you will have to declare it by typing: "int
var;". Athena Scripting, is like the name already implies, a Scripting language. There is no need to declare a variable
before using it, it is all done by the name of variable. The most basic variable is the permanent integer player
variable. It looks like this:

`var`

To make it a string variable, all you have to do is put a `$` after it, like this:

`var$`

You can also make it a temporal variable. This means that the value is stored until the next reboot or crash of the map
server. All you need to do is add the prefix `@`. (Prefix means, something that is put in front.) So that makes the
variable look like this:

`@var`

And for a temporal player string variable, it looks like this:

`@var$`

Unfortunately, the array option fails for permanent player variables. However, it does work for the temporal version. To
make a variable behave like an array, all you have to do is add `[]` after the variable. We will get into it later on in
detail, but here is how it would look for a temporal player integer array variable and a temporal player string
variable:

`@var[]`  
`@var$[]`

As you can see, it is placed even after the string postfix when it is present. (Postfix means something at the end of
something. So, the string postfix is `$` and the array postfix is `[]`.)

Now, for a different type of variable, like global or account, you will have to use a different prefix. Kind of like the
temporal prefix @, only this gets even placed in front of that. The prefixes are noted in the schematic at the start of
the previous section. But, let's make an example list to show you all possible things:

| Type           | Normal    |           |
|----------------|-----------|-----------|
| Integer        |           | String    |
| Temporary      | Permanent | Temporary |
| Player         | `@var`    | `var`     |
| Account        | N/A       | `#var`    |
| Global Account | N/A       | `##var`   |
| NPC            | `.@var`   | `.var`    |
| Global         | `$@var`   | `$var`    |

## Using Variables

Now that we know which variables exist, it is time to elaborate on how you exactly use them.

### Setting/Modifying/Deleting Variables

#### Normal Variables

You set a variable by using the command set. The format is:

- [set](./commands/set.md)`(<variable>,<value>)`;

or

- `<variable> = <value>`;

Examples:

```C
set(var, 5); // Setting a permanent integer player variable to 5.
set($var$, "Hello"); // Setting a global string variable to "Hello".
set(.@var[5], 10); // Setting the sixth element (5 + 1) of the temporal integer NPC variable to 10.
set(#var, #var * 2); // Multiplying the value that is in #var by 2 and store it in #var again.
```

or
```C
var = 5; // Setting a permanent integer player variable to 5.
$var$ = "Hello"; // Setting a global string variable to "Hello".
.@var[5] = 10; // Setting the sixth element (5 + 1) of the temporal integer NPC variable to 10.
#var = #var * 2; // Multiplying the value that is in #var by 2 and store it in #var again. 
```

You can also unset a variable, which is not needed per se, but saves memory. To unset an integer value, you need to
store 0 in it, so like this:

```C
set var, 0;
var = 0;
```

To unset a string variable, you will have to set the variable to "". (An empty string.) Another example:

```C
set @var$, "";
@var$ = "";
```

Other possible examples

```C
@i = 1;
@i++;
@i *= 2;
@i = @j = 1;
@i -= @j;

for (@i = 0; 10 > @i; ++@i) { }
while ((.@j = .@i++) < 20) { }
```

#### Array Variables

An array is a variable that references consecutive memory blocks of the same type. In C or any other programming /
scripting language, an array has no limitation as in how many indexes (how many consecutive blocks of memory it
references to) it can hold, nor its dimensions (how many arrays can an array hold. It's like a matrix of 2x3, for
example).

In Hercules, The limitation is (int)2147483647 elements held by a single array, and a single dimension (mostly because
strings can use a full index regardless of the length of the string it references to).

Arrays can be set and unset using the default set. They also come with a special set of commands, to quickly set
multiple values, or cleaning them. These are the Array related commands.

- [cleararray](./commands/cleararray.md)
- [copyarray](./commands/copyarray.md)
- [deletearray](./commands/deletearray.md)
- [getarraysize](./commands/getarraysize.md)
- [getelementofarray](./commands/getelemenofarray.md)
- [setarray](./commands/setarray.md)

To quickly set multiple values in an array, you need to use setarray. It will look like this:

```C
setarray(@array[0],100,200,300);
```

This will result in this:

```C
@array[0] == 100;
@array[1] == 200;
@array[2] == 300;
```

`deletearray` is used to quickly erase a specified amount of elements of an array. It can also be used to completely unset
it.

```C
deletearray(@array[0], 1); // Deletes element 0 of the array, and moves every other entry up.
```

Result using the previous array:

```C
@array[0] == 200;
@array[1] == 300;
```

To completely erase an array using this command, you can do this:

```C
deletearray(@array[0]);
```

Another way to quickly set or unset an array is the cleararray command. Cleararray is actually better than setarray if
you want to fill an array with the same values, like this:

```C
cleararray(@array[0], 100, 57);
```

The result is this:

```C
@array[0] == 100;
@array[1] == 100;
// ...
@array[56] == 100;
```

Taking the previous @array as example variable, to clear it partially, you can use the command in this way:

```C
cleararray(@array[1], 0, 8);
```

Please note, that unlike `deletearray`, it will not shift the remaining values. The result will be this:

```C
@array[0], @array[9] ~ @array[56] == 100;
@array[1] ~ @array[8] == 0;
```

### Reading out Variables

#### Normal Variables

Storing and unsetting variables is one thing. Reading them out is something else. Thankfully, it is an easy something
else. We already actually read out a variable before, at the modifying part:

```C
set(#var, #var * 2); // Multiplying the value that is in #var by 2 and store it in #var again.
```

As you can see, all you need to do to read out a variable, is only typing the variable name. It works the same for any
command like the if statement:

```C
// If #var contains a value bigger than 2, then show a close button.
if (#var > 2)
  close();
```

If you are using the `mes` command, or another text displaying command, it works a bit differently:

```C
mes(#var + ""); // Will display a line with only the value of #var.
mes("You have killed " + dead_porings + " Porings."); // Will display this: "You have killed <value of dead_porings> Porings."
mes(@name$); // If @name$ contains "[Kafra]", it will display "[Kafra]"
mes("My name is " + @name$); // If @name$ contains "Trevor", it will display: "My name is Trevor"
```

!!! note
	While these examples are totally valid, it recommended the use of `mesf` and `sprintf` instead of concatenation
	when displaying variables. Using `mesf` and `sprintf` creates better strings for localization with HULD.


##### Other ways to check variables

There are other ways to check the value of a variable, as in if it has been declared or not.

You can check if a variable has been declared, different from 0, or not,equal to 0. A variable that has been declared
and set to 0 is said to be "undeclared".

To do so, you do:

```C
// this will check if 'foo' has been declared or not. If the value 'foo'
// holds is different from 0 (declared), it will return true. Otherwise it 
// will return false.
if (foo) {
	// ...
}

// Same as above
if (foo != 0) {
	// ...
}

// this will check if 'foo' has been declared or not. If the value 'foo'
// holds is equal to 0 (not declared), it will return true. Otherwise it 
// will return false.
if (!foo) {
	// ...
}

// Same as above
if (foo == 0) {
	// ...
}
```

! is a Logical Not operator. If you use it on the number 0 it will return 1. If you use it on anything other than 0 it
will return 0.

Note : ! doesn't support string variable

#### Array Variables

To read out a value of an array, you will have to specify which element of the array you want to see. Let's say, we have
the following array:

```C
@array[0] == 41;
@array[1] == 12;
@array[2] == 54;
@array[3] == 4;
@array[4] == 22;
@array[5] == 30;
@array[6] == 21;
```

And we have the following script:

```C
mes("[Lotto]");
mes("And today's numbers are:");
mes(@array[0]+", "+@array[1]+", "+@array[2]+", "+@array[3]+", "+@array[4]+" and "+@array[5]+".");
mes("And the bonus number is "+@array[6]+".");
```

Then it will display this:

	[Lotto]
	And today's numbers are:
	41, 12, 54, 4, 22 and 30.
	And the bonus number is 21.

### Temporal vs Permanent

When you use a variable, you can choose between making it temporal or permanent, with the exception of account
variables. Permanent variables survive everything, even a reboot of the server. Temporal variables however, do not
survive a reboot and are cleaned out when the map server is killed. This is useful when you only want to store simple
things, like a random number or the name of a NPC. Please note that the temporal NPC variable actually works a bit
different. It ceases to exist when the script encounters the close; command or the end; command.

## Variables in Detail

This section will cover each variable indepth, including examples of how and when to use them.

### Global Variables

#### Details

Global variables support the temporal option, the string option and the array option. The advantage of a global variable
is that they can be accessed by any NPC, function or subroutine. They also do not require the interaction of a player,
and can thus be used by time triggered events, or during start up events. When used without the @-prefix (Temporal
prefix), this variable survives a server restart, and thus can be used to store important information like announcement
messages.

Global permanent variables are stored in 'mapreg' table. Changing the value of a global variable while the server is up,
should only be done by using set, setd or one of the array commands. Altering the value of it in 'mapreg' table while
the server is running, will be ignored and overwritten by the next save sweep. If you want to alter the value of a
global variable manually, so without any of the NPC commands, then you must make sure that your server is completely
down. The temporal global variable is stored directly in the memory, and thus not accessible through any other way
besides the default NPC commands.

Another special thing about the way Global Variables are saved, is that they are always treated as if they are an Array.
In 'mapreg' table, the format is this: `<variable name>,<index>,<value>`

The prefix of a global variable is `$`

#### Example

Global variables are perfect to enable/disable NPCs on command. For example, if you want to host an event and you made a
warper for it, then you want the warper to do nothing, until a GM starts hosting the event. You will also want the NPC
to automatically be closed when the server crashes or reboots. This will prevent any players to go to the event before
the GM is online. Here is how you could code such a simple warper:

```C
prontera,147,177,7	script	Event Warper	4_F_KAFRA2,{
	if (getgmlevel() >= 60) {
		goto L_GMMenu; // If the player is a GM, go to the GM Menu.
	}

	if (!$@EW_Enable) { // If the event is disabled, tell the player.
		mes("[Event Warper]");
		mes("Sorry, but the event arena is closed for the moment.");
		close();
	}

	mes("[Event Warper]");
	mes("Do you want to go to the event?");
	next();
	if(select("Yes","No") == 1) {
		warp($@event_map$, $@event_x, $@event_y); // Warp to the map stored in $@event_map$, at the coords $@event_x and $@event_y
	}
	close();

L_GMMenu:
	mes("[Event Warper]");
	mes("Please choose an option.");
	next();
	switch(select("View Settings", "Set Destination", "Enable Warper", "Disable Warper", "Leave")) {
	case 1: // View Settings
		mes("[Event Warper]");
		if($@EW_Enable) {
			mes("I am currently enabled.");
		} else {
			mes("I am currently disabled.");
		}
		mesf("The current destination is: %s at %d, %d.", $@event_map$, $@event_x, $@event_y);
		break;
		
	case 2: // Set Destination
		mes("[Event Warper]");
		mes("Please enter the destination map.");
		next();
		input($@event_map$); // Setting the event map in $@event_map$
		mes("[Event Warper]");
		mes("Please enter the x coordinate.");
		next();
		input($@event_x); // Setting the x coordinate in $@event_x
		mes("[Event Warper]");
		mes("Please enter the y coordinate.");
		next();
		input($@event_y); // Setting the y coordinate in $@event_y
		mes("[Event Warper]");
		mes("Destination set.");
		break;

	case 3: // Enable Warper
		mes("[Event Warper]");
		if ($@EW_Enable) {
			mes("I am already enabled.");
		} else {
			$@EW_Enable = 1; // Setting $@EW_Enable to 1, to enable the NPC.
			mes("It has been done.");
		}
		break;
	
	case 4: // Disable Warper
		mes("[Event Warper]");
		if(!$@EW_Enable) {
			mes("I am already disabled.");
		} else {
			$@EW_Enable = 0; // Setting $@EW_Enable to 0, to disable the NPC.
			mes("It has been done.");
		}
		break;

	case 5: // Leave
		close();
	}
	next();
	goto L_GMMenu;
}

```

If you want a warper that is enabled for several days, like a special event that is always open in this period, then you
should use permanent global variables. This will allow the NPC to be active even after a server crash, so that the
people can access the special map right away, without having to wait for a GM to come online. So, instead of
`$@EW_Enable`, you should use `$EW_Enable`. And the map, x and y variables should become `$event_map$`, `$event_x` and
`$event_y`.

### Global Account Variables

#### Details

Global Account Variables aren't really of any use unless you run a server which has multiple map servers and only one
login server. This is why it is a rarely used variable. In theory, it is exactly the same as a normal account variable,
with one slight difference. It is kind of hard to explain if this is your first time using variables, but in essence, a
global account variable is stored by the login server instead of the char server. This makes it so that the value of the
account variable is the same for the player's account in each of the map servers of your server. The normal account
variable is unique on each map server. The global account variable does not support the temporal prefix (@) nor the
array. This means that they are less dynamic and always survive a server restart.

The global account variable is stored in "save/account.txt" for a TXT server, and for the SQL server it is stored in the
table called 'global_reg_value'. These locations are used for mixed storage. This means, that also the normal account
variable and the player variable is stored here. You can recognize a global account variable by the fact that the 'type'
field is set to 1 and that the 'char_id' field will contain a 0.

The rumours are that it is possible to alter a global variable without using NPC commands. However, the entire account
needs to be offline and out of the memory on ALL the login, char and mapservers, to make it so that changing it has any
effect. If you change the value of a global account variable and there is a character online of that account, then your
new value will be overwritten in time by the saving routine of the server.

The prefix of a global account variable is `##`

#### Example

Global account variables are useful when you use a voting NPC. If you want it so that each account can only vote once,
and you have multiple mapservers, then you want all the other mapservers to know if an account has already voted or not.
This will prevent a certain account to vote more than once. The script below is an example of such a voting NPC.

```C
prontera,147,177,7	script	Poll	4_F_KAFRA2,{
	if (##AlreadyVoted) { // Account has already voted on a mapserver.
		mes("These are the current results:");
		mesf("Yes : %d/%d votes (%d%%).", $Poll_Yes, $Poll_Yes + $Poll_No, (($Poll_Yes * 100)/($Poll_Yes + $Poll_No)));
		mesf("No : %d/%d votes (%d%%).", $Poll_No, $Poll_Yes + $Poll_No, (($Poll_No * 100)/($Poll_Yes + $Poll_No)));
		close();
	}

	mes("Poll of today:");
	mes("Do you like this server?");
	next();
	switch (select("Yes", "No")) {
	case 1: // Voted Yes.
		$Poll_Yes = $Poll_Yes + 1;
		break;
	
	case 2: // Voted No.
		$Poll_No = $Poll_No + 1;
		break;
	}
	##AlreadyVoted = 1; // Player has already voted. Setting global account variable ##AlreadyVoted to 1.
	mes ("Thank you for your vote.");
	mes ("These are the current results:");
	mesf("Yes : %d/%d votes (%d%%).", $Poll_Yes, $Poll_Yes + $Poll_No, (($Poll_Yes * 100)/($Poll_Yes + $Poll_No)));
	mesf("No : %d/%d votes (%d%%).", $Poll_No, $Poll_Yes + $Poll_No, (($Poll_No * 100)/($Poll_Yes + $Poll_No)));
	close();
}
```

### Account Variables

#### Details

Account variables work in a similar way as global account variables, and also have the same restrictions. It connects a
value to a player's account, which can be useful for a Vote NPC, or a quest NPC that a player is only allowed to do
once. Whereas a global account variable is the same for each mapserver, if you have a setup with multiple mapservers and
a single login server, a normal account variable will contain different values for each mapserver. The account variable
does not support the temporal prefix (@) nor the array. This means that they are less dynamic and always survive a
server restart.

The global account variable is stored in "save/account.txt" for a TXT server, and for the SQL server it is stored in the
table called 'global_reg_value'. These locations are used for mixed storage. This means, that also the global account
variable and the player variable is stored here. You can recognize a global account variable by the fact that the 'type'
field is set to 2 and that the 'char_id' field will contain a 0.

The rumours are that it is possible to alter a variable without using NPC commands. However, the entire account needs to
be offline and out of the memory to make it so that changing it has any effect. If you change the value of a account
variable and there is a character online of that account, then your new value will be overwritten in time by the saving
routine of the server.

The prefix of an account variable is `#`

#### Example

The account variable is, just like the global account variable, very suited for a voting NPC. Especially when you only
have one mapserver tied to your login server. Because this setup is very common, the normal account variable is often
used. Also, even if you have multiple mapservers, then you might want to allow players to do the same quest on each
mapserver, so that they can have the reward(s) on all the mapservers. To keep it easy, here is the voting NPC again,
only with normal account variables.

```C
prontera,147,177,7	script	Poll	4_F_KAFRA2,{
	if (#AlreadyVoted) { // Account has already voted on a current map-server.
		mes("These are the current results:");
		mesf("Yes : %d/%d votes (%d%%).", $Poll_Yes, $Poll_Yes + $Poll_No, (($Poll_Yes * 100)/($Poll_Yes + $Poll_No)));
		mesf("No : %d/%d votes (%d%%).", $Poll_No, $Poll_Yes + $Poll_No, (($Poll_No * 100)/($Poll_Yes + $Poll_No)));
		close();
	}

	mes("Poll of today:");
	mes("Do you like this server?");
	next();
	switch (select("Yes", "No")) {
	case 1: // Voted Yes.
		$Poll_Yes = $Poll_Yes + 1;
		break;
	
	case 2: // Voted No.
		$Poll_No = $Poll_No + 1;
		break;
	}
	#AlreadyVoted = 1; // Player has already voted. Setting account variable #AlreadyVoted to 1.
	mes ("Thank you for your vote.");
	mes ("These are the current results:");
	mesf("Yes : %d/%d votes (%d%%).", $Poll_Yes, $Poll_Yes + $Poll_No, (($Poll_Yes * 100)/($Poll_Yes + $Poll_No)));
	mesf("No : %d/%d votes (%d%%).", $Poll_No, $Poll_Yes + $Poll_No, (($Poll_No * 100)/($Poll_Yes + $Poll_No)));
	close();
}
```

### Player Variables

#### Details

Player variables are a type of variable that can only be accessed by the player who is using the script. The player
variable supports the temporal tag, and both also supports arrays. When you store a value in `var$` for PlayerA, it will
have a different value than the contents of `var$` for PlayerB. This comes in handy when you are writing a quest and need
to keep track of the progress. For example, when a player accepted a quest, you can set a variable named quest_progress
to 1. When he finishes the next part, you can set it to 2, etc. etc. Permanent player variables are also the way to deny
future access to a NPC or quest. Simply set a permanent player variable to a certain value at the end of the NPC or
quest, and check for that value at the start of the quest. Temporal player variables used to be widely used, and still
are in the older revisions. Nowadays it only use to store player's information that last until player logout, since it
behaved that way, without having to use OnPCLogoutEvent to clear them.

Permanent player variables are stored in the table called 'char_reg_num_db' for integer type, and 'char_reg_str_db' for
string type. The temporal player variable is directly stored in the memory.

You are able to manipulate the value of a permanent player variable without using script commands. Simply make sure the
character of which the variable is, is offline. Of course, this does not apply for a temporal player variable.

Player variables have no prefix

#### Example

A simple example of the usage of a permanent player variable, is a one time freebee giver. After the freebee has been
given, the variable is set and when the player talks to the NPC again, it will check for this and denies access.

```C
prontera,147,177,7	script	Freebee Giver	4_F_KAFRA2,{
	if (GotFreebee) { // If the permanent player variable GotFreebee is not 0, then do what is inside the { }.
		mes("You have already gotten the freebee.");
	} else {
		mes("Welcome to hour server.");
		mes("To show our gratitude, here is a one time free item.");
		next();
		getitem(999, 1);
		GotFreebee = 1; // Item given, sets permanent player variable GotFreebee to 1.
		mes("Have fun.");
	}
	close();
}
```


An example of using a temporal variable, is an interactive NPC system, responding to a random mood of a player. It can
look like this:

```C
-	script	mood	FAKE_NPC,{
OnPCLoginEvent:
	@mood = rand(3); // 0 == happy, 1 == sad, 2 == grumpy, 3 == in love.
	setarray(@moodtxt$[0], "happy", "sad", "grumpy", "in love");
	dispbottom(sprintf("You feel %s today.", @moodtxt$[@mood]);
	end;
}

prontera,147,177,7	script	Random Person	4_F_KAFRA2,{
	switch (@mood) { // Determine the setting of @mood.
	case 0: // happy
		mes("Oh my, we are cheerful today, aren't we!");
		break;

	case 1: // sad
		mes("Why are you so sad?");
		mes("Here, this might cheer you up.");
		close2();
		percentheal(100,100);
		end;

	case 2: // grumpy
		mes("Come on, cheer up. It's a nice day today.");
		break;
	
	case 3: // in love
		mes("Wow, did you find that one person? Cool!");
		break;
	}
	close();
}

prontera,147,175,7	script	Grumpy Person	4_F_KAFRA2,{
	if (@mood != 2) { // Only wants to talk to another grumpy person.
		mes("Go away!");
		close();
	}

	mes("What are you doing here?");
	next();
	mes(strcharinfo(0));
	mes("Go away!");
	next();
	mes("No, you go away!");
	next();
	// ... (rest of NPC)
	close();
}
```

### NPC Variables

#### Details

NPC variables support, just like global variables, the temporal prefix as well as the array postfix. They aren't in
existence for that long yet, but are already widely used. The reason for this, is that the temporal NPC variable is a
true temporal variable. It is unique per player per NPC, until the close; or end; command. This means it can be used to
temporary store a value, or an array or whatever to make coding easier for you. The permanent NPC variable is not as
permanent as it may sound at first. It is used to store a variable per NPC. This variable is accessible by any player
that uses that NPC. However, on server restart, the value of that variable is lost. NPCs are capable of requesting the
value of a permanent NPC variable owned by another NPC. For this, the getvariableofnpc command is used, which will be
explained further down in this article. Permanent NPC variables can be used in logging systems or for example a racing
event. That is, if you do not want to waste global variables. Note that if you duplicate the NPC, all those NPC share
the same NPC variable. But this might subject to change in the future.

All the NPC variables are directly stored in the memory, and are therefor not editable by anything else besides script
commands.

The prefix for a NPC variable is .

#### Example

Temporal NPC variables are widely used to temporary save a value. This can make customizing your script easier. For
example, you can store the NPC name in a temporal NPC variable, like shown in the script beneath:

```C
prontera,147,177,7	script	Random Person	4_F_KAFRA2,{
	.@name$ = "^FF0000"; // Setting the color, red in this case.
	.@name$ = .@name$ + "Sir Eduard"; // Setting the name of the NPC
	.@name$ = "["+.@name$+"^000000]"; // Finalizing the name. It will now show: "[Sir Eduard]", where Sir Eduard is written in red.
	mes(.@name$); // Display Name
	mes("Hello there.");
	mes("Welcome to our server.");
	next();
	mes(.@name$); // Display Name
	mes("I hope you will enjoy your stay here.");
	mes("We have a lovely fountain at the center, as well as some beautiful kafra spread out through the town.");
	next();
	mes(.@name$); // Display Name
	mes("So, feel free to look around.");
	mes("And have a nice day.");
	close();
}
```

All you have to do now to change the name being displayed is changing "Sir Eduard" into something else. In larger
scripts, this means that you do not have to edit the name at 100+ places. The same applies for the color, which can be
changed in the first line.

A short example of a permanent variable might be this 'logging' NPC:

```C
prontera,147,177,7	script	Random Person	4_F_KAFRA2,{
	mes("Hello!");
	mes("Do you have any gossip?");
	next();
	if (.LastPerson$ != "") { // If there is a name stored, do what is inside the { }
		mesf("%s had some really nice gossip.", .LastPerson$);
		next();
	}
	
	.LastPerson$ = strcharinfo(0); // Set the current player's name as the last player's name.
	mes("Aha, I see.");
	mes("Thank you for this new info.");
	mes("I should tell it to my friends right away.");
	mes("Good bye.");
	close();
}
```

## Special Commands

### Input

Input is the most basic command to get a player to input a value and store it in a variable. Input itself has some
safeguards placed inside that prevent entering faulty data. The format for input is:

- [input](./commands/input.md)`(<variable>{,<min>{,<max>}})`;

Despite it seems that you can enter anything in the input box as a player, this is not the case. Let's review the
following two cases:

`1. input @name$;`  
`2. input @number;`

The first one allows you to enter a string. A person can still input a number, but it will be stored as if it was a
string. The second one allows you to enter a number. If a person enters a negative number, it will store 0. If the
person tries to enter a string, or a letter, it will also store 0.

### Getd & Setd

Getd and Setd are a couple of special commands. They allow the use of dynamically named variables, as well as a way to
cheat and make multi-dimensional variables. Their format is like this:

- [getd](./commands/getd.md)`("Variable Name")`;
- [setd](./commands/setd.md)`("variable name",<value>)`;

The most common use of getd and setd is simulate Guild/Party Array or simulate multi-dimensional array.

#### Simulating Guild Variables

Guild Variables do not exist, and since an array is limited upto 128 elements, it is not adviced to use that for
storage. Yet it can be needed to store guild variables, when you want to do a ranking of some sort. The following
example is a snippet from gldfunc_ev_agit.txt, and stores the amount of times a guild has captured a castle.

```C
.@NameOfGuildVar$ = sprintf("$CastCapt%d", getcharid(CHAR_ID_GUILD));
// If your guild ID would be 204, the contents of .@NameOfGuildVar$ would be: "$CastCapt204"
.@Score = getd(.@NameOfGuildVar$); // Retrieve the current score.
.@Score = .@Score + 1; // Add one to it.
setd(.@NameOfGuildVar$, .@Score); // Put in the new score.
```

or you can just
```C
setd(sprintf("$CastCapt%d", getcharid(CHAR_ID_GUILD)), getd(sprintf("$CastCapt%d", getcharid(CHAR_ID_GUILD))) + 1);
```

Of course, the same can be done to simulate Party Variables, which also officially do not exist.

#### Simulating Multidimensional Arrays

Now, let's say you know your stuff, and really are used to using arrays. Then you might want to consider simulating
multi-dimensional arrays. This snippet will use the for command. If you do not know how to use it, it is best to skip
this example.

```C
// Example of iterating the 3-dimensional array $@array[100,100,100].
freeloop(true);
for (.@i = 0; .@i < 100; .@i++) {
	for (.@j = 0; .@j < 100; .@j++) {
		for (.@k = 0; .@k < 100; .@k++) {
			.@varname$ = sprintf("$@array%d_%d[%d]", .@i, .@j, .@k);
			// Let's say .@i is 50, .@j is 22 and .@k is 95. Then this will be in .@varname$:
			// $@array50_22[95]
			if (getd(.@varname$) == 5)
				.@FivesFound++;
		}
	}
}

announce(sprintf("I have found %d occurances of 5 in your multidimensional array.", .@FivesFound), bc_all);
```

### Getvariableofnpc

Getvariableofnpc is a method to get the value of a permanent NPC variable of another NPC. The official format is like
this:

- [getvariableofnpc](./commands/getvariableofnpc.md)`(<Variable Name>,"NPC Name")`;

It's uses can vary, but from what I've seen until now is that it is mainly used to sync several NPCs or to make checks
in a global temporal unlocking quest. To sync a variable NPC with the value of a variable of another NPC, you could use
this line:

```C
.v = getvariableofnpc(.var, "A NPC");
// Retreives value of .var of the NPC called "A NPC"
// and puts the found value in .v of this NPC.
```

A global temporal unlocking quest can be like this:

```C
prontera,147,177,7	script	PvP Warper	4_F_KAFRA2,{
	if (getvariableofnpc(.unlocked, "PvP Unlocker")) {
		mes("Want to go to the PvP room?");
		next();
		if (select("Yes","No") == 2) {
			mes("Ok, guess not.");
			mes("Good bye.");
			close();
		}
		close2();
		warp("pvp_n_1-1", 0, 0);
		end;
	}
	mes("No one has opened the PvP room yet.");
	mes("At least one person needs to visit the ^FF0000PvP Unlocker^000000, and help him to open up PvP.");
	close();
}

prontera,147,175,7	script	PvP Unlocker	4_F_KAFRA2,{
	if (.unlocked) {
		mes("To enter the PvP room, talk to the ^FF0000PvP Warper^000000.");
		close();
	}
	if (countitem(512) < 1) {
		mes("I will not open the PvP room until I get an apple!");
		close();
	}

	delitem(512, 1);
	mes("Thank you for that juicy apple.");
	mes("I will open the PvP room now.");
	mes("Enjoy.");
	.unlocked = 1;
	close();
}
```


## Other Important Info

### Naming your Variables

#### General Restrictions

Just like any other scripting or coding language, variable names have certain restrictions. Some things are simply not
accepted, and some things are accepted, but really bad to do.

- Permanent Character variable name must start with a letter after any prefix, if it is there.
- It also cannot have any arithmetic operators. (This means, none of the following signs: +, -, /, * and any other math
  sign.)
- Brackets of any kind are also not allowed, excluding the array postfix of course.
- Other restrictions to the variable are the length of the name, it is not allowed to succeed 32 characters.
- Never use a command name as a variable name.
- Never use a label, subroutine or function name as a variable name.

Basically, this all means, that the name part can only contain the following characters: a~z, A~Z, 0~9 and _

Lot's of restrictions, huh? Well, most of the above restrictions cause your mapserver to be mad at you.

#### Reserved Names

Some variable names are reserved by default. You should not touch these unless you know what you are doing. Why? Well,
changing them, may mean changing things to the invoking player, depending on the kind of reserved name.

##### Constants

One kind of reserved names are constants. These values are loaded upon start-up of the map-server and remain constant
during their entire life-time, means, they cannot be changed by any means during run-time. Constants are stored inside
**db/const.txt** and are all lines, where a constant name is followed by only one number, whether decimal or
hexadecimal.

Examples include:

`Job_Archer`  
`EAJ_SUPER_NOVICE`  
`cell_chkreach`  
`bUnstripableShield`

##### Parameter Constants

These behave almost like variables with side-effect. They are called constants, because they correspond to an constant
internal value, which describes their effect. Like-wise the constants, these values are loaded upon start-up of the
map-server from **db/const.txt**. They are defined by lines with the constant name being followed by two numbers, the
latter of them being always being 1.

When used inside scripts, their value is not always constant, but can change depending in context and time. Some of them
can be written as well, such as [Zeny](../basics/zeny.md#scripting).

Examples include:

`Zeny`  
`BaseLevel`  
`Class`  
`Weight`

#### Word of Advice

When using permanent variables, and even with temporal variables, it is very wise to use some sort of tag. This will
make sure that your variable name is unique. For example, if you have a godly equip quest, it is adviced to store the
status in a variable named like: `GEQ_Status`. `GEQ_` is the tag, and stands for Godly Equip Quest. This will make it
unique compared to other variables. Your variable names will become longer, yes, but it will prevent unknown or
unexpected results. Another example of tagging. Let's say you have a capture the flag event, run through NPCs, then
prefix your variable names with `CTF_`. So, some variables might be: `$CTF_ScoreTeam1`, `$CTF_ScoreTeam2`, etc. etc. Also,
please, keep in mind. Variables are case sensitive, just like labels! So, `$dummy` is not the same as `$Dummy`. Using both
are possible, as they are declare as 2 different variables.

#### Examples

Some examples of good and bad names. Good:

```C
$CTF_Winner$ // Winner of capture the flag
$CTF_Loser$ // Loser of capture the flag
$GQ_Winner$ // Winner of capture the flag
.npcname$ // Name of NPC. Using a permanent NPC variable will save memory space. (Increases CPU though.)
#SH_Item1 // Scavenger hunt, item 1.
#SH_Item2 // Scavenger hunt, item 2.
```

Bad:

```C
@Zeny // Zeny is a reserved name.
rand // Rand is a command.
@h-uy // - is an arithmetic operator, not allowed.
$winner and $winner$ // Mixed use of string and integer, bad.
```

### Minima and Maxima of Variables

Variables are restricted in the amounts that they can store, as well as how many variables you can have of a certain
kind. This section will deal with those restrictions, and even some ways to alter them.

  
**Maximum Values**  

- Integer: Can contain a value from -2147483648 to 2147483647 (Signed integer)
- String: Permanent Global = 255. Permanent Char/Account/Global Account = 254. Others = Unlimited.
- Array: Can have a maximum of 2147483648 elements (0~2147483647)

  
**Maximum Different Variables**  
All types are unlimited. Please note, that *unlimited* is actually still limited; by available memory and disk capacity
(permanent variables).

### Alive Time

Some variables are never erased, others are cleaned up after certain events. A rule of thumb is, that variables that are
only stored in memory are always erased on server restart or crash. Variables which are written to the SQL database or
the save folder, survive restarting the mapserver. When it comes to the alive time of a variable, there is no difference
between integer, string or array variables. There is only a difference between temporal and permanent.  
The following scedule displays when a variable gets erased from memory and is unrecoverable. Please note, that if a
variable is set to 0 (integer) or "" (string), that the variable is unset as well, and in a sense, erased as well.

| Prefix    | Name           | Alive Time               |
|-----------|----------------|--------------------------|
| Temporary | Permanent      |                          |
| *none*    | Player         | Erased on Server Restart |
| `#`       | Account        | N/A                      |
| `##`      | Global Account | N/A                      |
| `.`       | NPC            | Erased on End/Close      |
| `$`       | Global         | Erased on Server Restart |

Notes:

- Server Restart is equal to anything that makes the mapserver stop it's current session, including crashes.
- Global Account and Account variables do not have a Temporal version.
- Always Survives can still mean loss of data, if the server crashes/stops after such a variable was altered, but the
  periodical save process hasn't been executed yet.
- Erased on End/Close, means that the value of this variable is lost when the script finds the command "end;" or
  "close;".
- Like said above, unset a variable will also erase it from existence.

## Variable Related Errors

### Str&Int and Int&Str Errors

This specific error happens when you are comparing a String variable with an Integer variable, or when you want to add a
String to an Integer variable. This is often caused by a simply typo. Just go over your code, and make sure that you
didn't make any typos, and it should be fixed.

Examples of what can cause this error:

```C
if (.@value == .@name$) // Will error, because .@value is an Integer. .@name$ is a String.
.@value = "Blaat"; // Might error, because .@value is an Integer. "Blaat" is a String.
```

### No RID attached Error

You get this error, when you want to change a player or account variable, while the player is not attached anymore to
the NPC or script. A script requires a so called RID to change a value that is connected to a player or an account. You
can manually attach an RID to a script, but you need to have an account id to do this. To get an account id, you need to
do a getcharid(3,"Player's Name") and use the result with attachrid. Of course, for this, you will have to get a player
name.

If there is no way for you to have an RID attached, then it means that you are using the wrong variables. The following
example demonstrates this:

```C
OnInit: // Runs when the server starts
   StartUpTime = gettimetick(2); // This will give the no RID attached error.
   end;
```

The reason this gives the error is that you want to store the current time in a player variable. But on the start up,
there is no way for a player to be online, and even if, this script is triggered without invoking a player. The solution
to this is to change `StartUpTime` into `.StartUpTime`, `$StartUpTime` or `$@StartUpTime`.

### Attachrid giving unexpected values

This is a common mistake, but not a real error as detected by the mapserver. This problem can occur when using
attachrid. Let's take the following snippet taken from an OnPCKillEvent as example:

```C
Killer$ = strcharinfo(0); // Setting Killers Name in Killer$
attachrid(killedrid); // Attach to the person who got killed.
dispbottom(sprintf("You were killed by %s", Killer$));
```

Q: What this part is supposed to do?  
A: It should send a message to the person who got killed, saying who killed them.  
Q: What goes wrong here?  
A: The script will not display the name of the killer, or the player's own name.  
In case you see the error, you might laugh at this, but it is a very common mistake. The person who scripted this made a
faulty assumption. He thought that `Killer$` before the attachrid is the same as `Killer$` after the attachrid. This is
not the case. The `Killer$` before the attachrid is stored in player 1's character. The `Killer$` after the attachrid is
stored in player 2's character. This means that they are not the same.

Q: So what is the solution?  
A: Use the NPC variable -> `.@var`.  
  

### Variable keeps displaying 0 or ""

Also a common error with new scripters. Take the following snippet:

```C
@name$ = Patrick;
```

A new scripter often types this when he/she wants to put the String "Patrick" inside `@name$`. However, he/she forgot to
put Patrick between a " and a ". So, instead of storing the string "Patrick" inside `@name$`, the server will look up the
value of the variable named Patrick, and stores that value inside `@name$`. This can result in a 0 being stored in
`@name$`.
