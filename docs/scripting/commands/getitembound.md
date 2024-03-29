# `getitembound()`

!!! warning
	This page may contain outdated information, incompatible with the current version of Hercules and its coding standards.

## Syntax

```c
getitembound(<item id>, <amount>, <bound type>{, <account ID>});
```

```c
getitembound("<item name>", <amount>, <bound type>{, <account ID>});
```

## Description

These commands will create bounded items.

This command behaves identically to [`getitem()`](getitem.md), but the items created will be
bound to the target character as specified by the bound type. All items created
in this manner cannot be dropped, sold, vended, auctioned, or mailed, and in
some cases cannot be traded or stored.

Valid bound types are:

- 0 - Regular [`getitem()`](getitem.md)
- 1 - Account Bound
- 2 - Guild Bound
- 3 - Party Bound
- 4 - Character Bound

Default is 0 if not defined.

## Example

```c
getitembound(2220, 1, 1); // The person will receive 1 Account bounded Hat that can store in storage.
getitembound(2226, 1, 2);  // The person will receive 1 Guild Bound Cap that can share and store in Guild Storage.
getitembound("Crown", 1, 4); // The person will receive 1 Char Bound Crown that cannot store sell or drop.
```

## See Also

- [`getitembound2()`](getitembound2.md)
- [`countbound()`](countbound.md)
