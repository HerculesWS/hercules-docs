# `getpartymember()`

!!! warning
	This page may contain outdated information, incompatible with the current version of Hercules and its coding standards.

## Syntax

```c
getpartymember(<party id>{, <type>});
```

## Description

This command will find all members of a specified party and returns their names (or character id or account id depending on the value of `type`) into an array of temporary global variables. There's actually quite a few commands like this which will fill a special variable with data upon execution and not do anything else.

Upon executing this,

| Array | Description |
| ----- | ----------- |
| `$@partymembername$[]` | is a global temporary string array which contains all the names of these party members (only set when type is 0 or not specified). |
| `$@partymembercid[]` | is a global temporary number array which contains the character id of these party members (only set when type is 1). |
| `$@partymemberaid[]` | is a global temporary number array which contains the account id of these party members (only set when type is 2). |
| `$@partymembercount` | is the number of party members that were found. |

The party members will (apparently) be found regardless of whether they are online or offline. Note that the names come in no particular order.

!!! remark
	Be sure to use `$@partymembercount` to go through this array, and not [`getarraysize()`](getarraysize.md), because it is not cleared between runs of `getpartymember()`. If someone with 7 party members invokes this script, the array would have 7 elements. But if another person calls up the NPC, and he has a party of 5, the server will not clear the array for you, overwriting the values instead. So in addition to returning the 5 member names, the 6th and 7th elements from the last call remain, and you will get 5+2 members, of which the last 2 don't belong to the new guy's party. `$@partymembercount` will always contain the correct number, (5) unlike [`getarraysize()`](getarraysize.md) which will return 7 in this case.

## Examples

### Example 1

```c
// get the party member names
getpartymember(getcharid(1), 0);

// It's a good idea to copy the global temporary $@partymember***** 
// variables to your own scope variables because if you have pauses in this 
// script (sleep(), sleep2(), next(), close2(), input(), menu(), select(), or prompt()), 
// another player could click this NPC, trigger getpartymember(), and 
// overwrite the $@partymember***** variables.
set(.@count, $@partymembercount);
copyarray(.@name$[0], $@partymembername$[0], $@partymembercount);

// list the party member names
for (set(.@i, 0); .@i < .@count; set(.@i, .@i + 1)) {
	mes((.@i +1) + ". ^0000FF" + .@name$[.@i] + "^000000");
}
close();
```

### Example 2

```c
set(.register_num, 5); // How many party members are required?

// get the charID and accountID of character's party members
getpartymember(getcharid(1), 1);
getpartymember(getcharid(1), 2);

if ($@partymembercount != .register_num) {
	mes("Please form a party of "+ .register_num +" to continue");
	close();
}

// loop through both and use isloggedin() to count online party members
for (set(.@i, 0); .@i < $@partymembercount; set(.@i, .@i + 1)) {
	if (isloggedin($@partymemberaid[.@i], $@partymembercid[.@i])) {
		set(.@count_online, .@count_online + 1);
	}
}
// We search AID & CID because a single party can have multiple 
// characters from the same account. Without searching through the charID, 
// if a player has 2 characters from the same account inside the party but 
// only 1 char online, it would count their online char twice.

if (.@count_online != .register_num) {
	mes("All your party members must be online to continue");
	close();
}

// copy the array to prevent players cheating the system
copyarray(.@partymembercid, $@partymembercid, .register_num);

mes("Are you ready ?");
next(); // careful here
select("Yes");

// When a script hits a next(), menu(), sleep() or input() that pauses the script, 
// players can invite or /leave and make changes in their party. To prevent 
// this, we call getpartymember() again and compare with the original values.

getpartymember(getcharid(1), 1);
if ($@partymembercount != .register_num) {
	mes("You've made changes to your party !");
	close();
}
for (set(.@i, 0); .@i < $@partymembercount; set(.@i, .@i + 1)) {
	if (.@partymembercid[.@i] != $@partymembercid[.@i]) {
		mes("You've made changes to your party !");
		close();
	}
}

// Finally, it's safe to start the event!
warpparty("event_map", 0, 0, getcharid(1));
```
