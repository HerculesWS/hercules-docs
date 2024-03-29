# `isloggedin()`

!!! warning
	This page may contain outdated information, incompatible with the current version of Hercules and its coding standards.

## Syntax

```c
isloggedin(<account id>[, <char id>]);
```

## Description

This function checks, whether an character with given [account id](../AID.md) is currently online (1) or not (0). Additionally a [char id](../CID.md) can be specified, for exact character matching.

## Examples

```c
input(.@aid);
if (isloggedin(.@aid)) {
	mes("A character with account id " + .@aid + " is currently around.");
} else {
	mes("Sorry, there is no character online with account id "+.@aid+",");
	mes("or the account does not exist.");
}
```

## See Also

- [`attachrid()`](attachrid.md)
