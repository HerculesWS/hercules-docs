# `night()`

!!! warning
	This page may contain outdated information, incompatible with the current version of Hercules and its coding standards.

## Syntax

```c
night();
```

!!! warning
	The rest of this document hasn't been converted to Markdown yet.

==Description==
These two commands will switch the entire server between day and night mode respectively. If your server is set to cycle between day and night by [[:Category:Configuration|configuration]], it will eventually return to that cycle.

==Examples==
 -	script	DayNight	-1,{
 	[[end]];
 [[OnClock]]0600:
 	day;
 	end;
 [[OnInit]]:
 	// setting correct mode upon server start-up
 	[[if]]([[gettime]](3)>=6 && gettime(3)<18)
 	{
 		end;
 	}
 OnClock1800:
 	night;
 	end;
 }
This script allows to emulate the day/night cycle as the server does, but also allows triggering additional effects upon change, like announces, gifts, etc. The day/night cycle set by configuration should be disabled, when this script is used.

==See Also==
* [[isday]]
* [[isnight]]
