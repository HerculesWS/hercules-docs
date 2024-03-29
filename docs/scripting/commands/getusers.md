# `getusers()`

!!! warning
	This page may contain outdated information, incompatible with the current version of Hercules and its coding standards.

## Syntax

```c
getusers(<type>);
```

## Description

This function will return a number of users on a map or the whole server. What it returns is specified by `Type`.

Type can be one of the following values, which control what will be returned:

- 0 - Count of all characters on the map of the invoking character.
- 1 - Count of all characters in the entire server.
- 8 - Count of all characters on the map of the NPC the script is running in.

## Example

```c
mes(getusers(1) + " players on the server");
close();
```

## See Also

- [`getmapusers()`](getmapusers.md);
- [`getareausers()`](getareausers.md);
