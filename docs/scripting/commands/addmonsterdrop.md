# `addmonsterdrop()`

!!! warning
	This page may contain outdated information, incompatible with the current version of Hercules and its coding standards.

## Syntax

```c
addmonsterdrop(<mob id or name>, <item id>, <rate>);
```

## Description

This command will temporarily add a drop to an existing monster. If the
monster already drops the specified item, its drop rate will be updated to the
given value.

Both the monster and the item must be valid.  Acceptable values for the drop
rate are in the range `[1:10000]`.

Return value will be 1 in case of success (the item was added or its drop rate
was updated), and 0 otherwise (there were no free item drop slots).

## Example

```c
// Add Poring Doll (741) to the Poring's (1002) drops, with 1% (100) rate
addmonsterdrop(1002, 741, 100);
```

## See Also

- [`delmonsterdrop()`](delmonsterdrop.md)
