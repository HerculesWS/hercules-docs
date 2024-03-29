# `do { ... } while (...)`

## Syntax

```c
do {
	<statement>;
} while (<condition>);
```

## Description

The `do { ... } while (...)` is the only post-test loop structure available in this script language. With a post-test, the statements are executed once before the condition is tested. When the condition is true, the statement(s) are repeated. When the condition is false, control is transferred to the statement following the `do { ... } while (...)` loop expression.

```c
do {
	Code to execute(1);
} while (expression(2));
```

!!! example
	Example 1: sentinel-controlled loop

```c
mes("This menu will keep appearing until you pick Cancel");
do {
	set(.@menu, select("One:Two:Three:Cancel"));
} while (.@menu != 4);
```

!!! example
	Example 2: counter-controlled loop

```c
mes("This will countdown from 10 to 1.");
set(.@i, 10);
do {
	mes(.@i);
	set(.@i, .@i - 1);
} while (.@i > 0);
```
