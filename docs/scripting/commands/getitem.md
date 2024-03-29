# `getitem()`

!!! warning
	This page may contain outdated information, incompatible with the current version of Hercules and its coding standards.

## Syntax

```c
getitem(<item id>, <amount>{, <account ID>});
```

```c
getitem("<item name>", <amount>{, <account ID>});
```

## Description

This command will give a specific amount of specified items to the target character. If the character is not online, nothing will happen.

If `character ID` is not specified, items will be created in the invoking character inventory instead.

In the first and most commonly used version of this command, items are referred to by their database ID number, which can be found in `db/pre-re/item_db.txt` or `db/re/item_db.txt`.

Giving an item ID of -1 will give a specified number of random items from the list of those that fall out of Old Blue Box. Unlike in all other cases, these will be unidentified, if they turn out to be equipment. This is exactly what's written in the Old Blue Box's item script.

Other negative IDs also correspond to other random item generating item tables:

- Giving an item ID of -2 will produce the effects of Old Violet Box.
- Giving an item ID of -3 will produce the effects of Old Card Album.
- Giving an item ID of -4 will produce the effects of Gift Box.
- Giving an item ID of -5 will produce the effects of Worn Out Scroll, which drops only Jellopies anyway.

This transaction is logged if the log script generated transactions option is enabled.

You may also create an item by it's name in the 'english name' field in the item database:

Which will do what you'd expect. If it can't find that name in the database, apples will be created anyway. It is often a VERY GOOD IDEA to use it like this.

This is used in pretty much all NPC scripts that have to do with items and quite a few item scripts. For more examples check just about any official script.

## Examples

```c
getitem(502, 10); // The person will receive 10 apples
getitem(617, 1);  // The person will receive 1 Old Violet Box
getitem("RED_POTION", 10);
```

## See Also

- [`getitem2()`](getitem2.md)
