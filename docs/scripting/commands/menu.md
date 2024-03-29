# `menu()`

!!! warning
	This page may contain outdated information, incompatible with the current version of Hercules and its coding standards.

{{obsolete|type=script command|when=long time ago}}

## Syntax

```c
menu("<option_text>", <target_label>{, "<option_text>", <target_label>, ...});
```

!!! warning
	The rest of this document hasn't been converted to Markdown yet.

== Description ==
This command will create a selectable menu for the invoking character. Only one menu can be on screen at the same time.

Depending on what the player picks from the menu, the script execution will continue from the corresponding label (it's string-label pairs, not label-string).

Options can be grouped together, separated by the character ':'.
 menu "A:B",L_Wrong,"C",L_Right;

It also sets a special temporary character variable @menu, which contains the number of option the player picked. (Numbering of options starts at 1.) This number is consistent with empty options and grouped options.

== Examples ==
 	[[menu]] "A::B",L_Wrong,"",L_Impossible,"C",L_Right;
 L_Wrong:
 	// If they click "A" or "B" they will end up here
 	// @menu == 1 if "A"
 	// @menu == 2 will never happen because the option is empty
 	// @menu == 3 if "B"
 L_Impossible:
 	// Empty options are not displayed and therefore can't be selected
 	// this label will never be reached from the menu command
 L_Right:
 	// If they click "C" they will end up here
 	// @menu == 5

If a label is '-', the script execution will continue right after the menu command if that option is selected, this can be used to save you time, and optimize big scripts.

 	[[menu]] "A::B:",-,"C",L_Right;
 	// If they click "A" or "B" they will end up here
 	// @menu == 1 if "A"
 	// @menu == 3 if "B"
 L_Right:
 	// If they click "C" they will end up here
 	// @menu == 5

Both these examples will perform the exact same task.

If you give an empty string as a menu item, the item will not display. This can effectively be used to script dynamic menus by using empty string for entries that should be unavailable at that time.

You can do it by using arrays, but watch carefully - this trick isn't high wizardry, but minor magic at least. You can't expect to easily duplicate it until you understand how it works.

Create a temporary array of strings to contain your menu items, and populate it with the strings that should go into the menu at this execution, making sure not to leave any gaps. Normally, you do it with a loop and an extra counter, like this:

 [[setarray]] @possiblemenuitems$[0],<list of potential menu items>;
 [[set]] @j,0; // That's the menu lines counter.
 
 // We loop through the list of possible menu items.
 // @i is our loop counter.
 [[for]]( [[set]] @i,0; @i<[[getarraysize]](@possiblemenuitems$) ; [[set]] @i,@i+1 )
 {
 	// That 'condition' is whatever condition that determines whether 
 	// a menu item number @i actually goes into the menu or not.
 	
 	[[if]] (<condition>)
 	{
 		// We record the option into the list of options actually available.
 		
 		[[set]] @menulist$[@j], @possiblemenuitems$[@i];
 		
 		// We just copied the string, we do need it's number for later 
 		// though, so we record it as well.
 		
 		[[set]] @menureference[@j],@i;
 		
 		// Since we've just added a menu item into the list, we increment 
 		// the menu lines counter.
 		
 		[[set]] @j,@j+1;
 	}
 	
 	// We go on to the next possible menu item.
 }

This will create you an array @menulist$ which contains the text of all items that should actually go into the menu based on your condition, and an array @menureference, which contains their numbers in the list of possible menu items. (Remember, arrays start with 0.) There's less of them than the possible menu items you've defined, but the menu command can handle the empty lines - only if they are last in the list, and if it's made this way, they are. Now comes a dirty trick:

 	// X is whatever the most menu items you expect to handle.
 	[[menu]] @menulist$[0],-,@menulist$[1],-,....@menulist$[<X>],-;

This calls up a menu of all your items. Since you didn't copy some of the possible menu items into the list, it's end is empty and so no menu items will show up past the end. But this menu call doesn't jump anywhere, it just continues execution right after the menu command. (And it's a good thing it doesn't, cause you can only explicitly define labels to jump to, and how do you know which ones to define if you don't know beforehand which options will end up where in your menu?) But how do you figure out which option the user picked? Enter the @menu.

'''@menu''' contains the number of option that the user selected from the list, starting with 1 for the first option. You know now which option the user picked and which number in your real list of possible menu items it translated to:

 mes "You selected "+@possiblemenuitems$[@menureference[@menu-1]]+"!";

* @menu is the number of option the user picked.
* @menu-1 is the array index for the list of actually used menu items that we 
made.
* @menureference[@menu-1] is the number of the item in the array of possible menu items that we've saved just for this purpose.

And @possiblemenuitems$[@menureference[@menu-1]] is the string that we used to display the menu line the user picked. (Yes, it's a handful, but it works.)

You can set up a bunch of 'if (@menureference[@menu-1]==X) goto Y' statements to route your execution based on the line selected and still generate a different menu every time, which is handy when you want to, for example, make users select items in any specific order before proceeding, or make a randomly shuffled menu.

Kafra code bundled with the standard distribution uses a similar array-based menu technique for teleport lists, but it's much simpler and doesn't use @menu, probably since that wasn't documented anywhere.

See also '[[select]]', which is probably better in this particular case. Instead of menu, you could use 'select' like this:

 [[set]] @dummy, [[select]](@menulist$[0],@menulist$[1],....@menulist$[<X>]);
    
For the purposes of the technique described above these two statements are perfectly equivalent.

== See Also ==
* [[Menus]]
