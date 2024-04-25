# Timers

Here I will try to better explain timers. To understand half of what's going on here, I suggest you already know how the
basics of [scripting](./index.md).

Many people are confused as to the use of timers, and this guide aims to lend a helping hand. So you might be wondering
"What do we use timers for?" Well, my friend, this guide shall explain some of the many uses of timers. Also, I will explain the
usage and format of different kinds of timers in detail.

# Use Number 1: NPC Speech

NPC Speech can be triggered using timers, and can make NPCs partition a long paragraph instead of spamming 3 instant
lines.  
  
Here's an example of it in proccess.  
We'll take this apart after we look at it.

```HercScript
prontera,23,20,2	script	Non-spamming-NPC-Talker	1_M_JOBGUIDER,{
	end;

OnInit:
	startnpctimer;
	end;

OnTimer1000:
    npctalk("Y hallo dar lol.");
    end;

OnTimer3000:
	npctalk("Lawl I'm not spamming.");
	end;
  
OnTimer4000:
	setnpctimer(0);
	end;
}
```

- [`Command: npctalk`](commands/npctalk.md)
- [`Command: setnpctimer`](commands/setnpctimer.md)
- [`Command: startnpctimer`](commands/startnpctimer.md)
- [`Event: OnInit`](events/oninit.md)
- [`Event: OnTimer`](events/ontimer.md)

Now, let's take a look at this script.  
We'll start with "OnInit:".  
  
Q: What is "OnInit:"?  
A: "OnInit:" is the commands you wish the NPC to execute right after the NPC is loaded.

```HercScript
OnInit:
	$GlobalVariable = 10;
	end;
```

Would set the variable (integer) `$GlobalVariable` to 10 when the server starts.  
* also see: [More About Variables](./variables.md)

Let's move on to the next item, shall we?
	`end;`

`end;` is always needed to show that a label starting with `On`,  
*(and is a valid label that the server sees other functions for than just a custom label)*  
has ended.  

**If you do not end the "On" label with "end;", horrible things will happen, such as running through other labels.**

```HercScript
OnInit:
	$GlobalVariable = 10;

LOtherLabel:
	$GlobalVariable = $GlobalVariable + 3;
	end;
```

When the NPC is run, the variable `$GlobalVariable` would be 35, since 32 + 3 = 35  

Note that the initiation label is executed, and proceedes to run through `LOtherLabel`.  
This is because I did not insert an `end;` after `OnInit` ended, but instead, after `LOtherLabel`.  
Note: Sometimes this is usefull too...  

Example:

```HercScript
// ...

OnClock2100:
OnClock2300:
	// your script here
	end;

// ...
```

- [`Event: OnClock`](events/onclock.md)

This Script will run at 21:00 AND at 23:00 (c&p from the woe-starting-script)

# Use Number 2: Delayed Warp

Delayed warping is a feature you can put in your script to add more drama, or to automatically warp someone from a room
when the player has exceeded the allotted time for being there. Here is an example of a delayed warp:

```HercScript
prontera,23,20,2	script	Bomb Squad	1_M_JOBGUIDER,{
	mes("[Dismantler]");
	mes("Where is the bomb? WHERE IS IT??");
	mes("Please help me find it before it explodes.");
	close2();
	addtimer(15000, "Bomb Squad::OnWarn");
	addtimer(30000, "Bomb Squad::OnBoom");
	dispbottom("Dismantler : The bomb will detonate in 30 seconds!");
	end;

OnWarn:
	dispbottom("Dismantler : OH MY GOD! ONLY 15 SECONDS LEFT - HURRY!!!!");
	end;

OnBoom:
	dispbottom("*time slows down as suddenly the ticking stops*");
	dispbottom("....");
	dispbottom("BOOOOOOOM");
	dispbottom("The blast flings you away.");
	warp("prontera",0,0);
	end;
}
```

- [`Command: addtimer`](commands/addtimer.md)
- [`Command: close2`](commands/close2.md)
- [`Command: dispbottom`](commands/dispbottom.md)
- [`Command: warp`](commands/warp.md)


First thing that probably comes to your mind is: How can I find the bomb? The answer is simple, you cannot. I didn't
include that NPC \*evil grin\*  

Now, let's walk over this script in more detail. The start is nothing new, just a simple NPC header with a text box.
Then there appears to be a close2;. This is not a typo. Close2; behaves a bit like close;, it displays a close button.
However, the script will keep on running in the background, after the close button has been pushed. So, after the player
presses the close button, it continues with the next line. For you lazy bums, here is an outtake of the script to
prevent your scrolling finger from getting tired.

```HercScript
	addtimer(15000, "Bomb Squad::OnWarn");
	addtimer(30000, "Bomb Squad::OnBoom");
	dispbottom("Dismantler : The bomb will detonate in 30 seconds!");
	end;
```

Addtimer creates a player tagged timer. It is really simple to work with, although it can be inaccurate.

- `addtimer(<ticks>, "NPC::OnEvent");`

So, in our case, we start a timer that lasts for 15000ms, converted, 15 seconds. When the timer ends, it triggers "Bomb
Squad::OnWarn". In human language: It jumps to the label named OnWarn: within the NPC called "Bomb Squad". We also
create another timer, that lasts for 30 seconds, and will trigger the label OnBoom: Then a simple dispbottom, to display
some text in the player's chat, and an end; to terminate the script.  
  
Q: Why not use NPC timers?  
A: NPC timers do not remember which player triggered the script, and addtimer does remember the so called RID. Since we
need to manipulate the player later on, we need the script to remember the RID.  
  
  
Anyway, after 15 seconds, if the player hasn't logged out, the script will restart at the following point:

```HercScript
OnWarn:
	dispbottom("Dismantler : OH MY GOD! ONLY 15 SECONDS LEFT - HURRY!!!!");
	end;
```

What it does here, is another text display in the chat of the player, and then end the script again. So, we wait, and we
wait, and then, after another 15 seconds, the second timer triggers the label OnBoom:, and starts this piece of code:

```HercScript
OnBoom:
	dispbottom("*time slows down as suddenly the ticking stops*");
	dispbottom("....");
	dispbottom("BOOOOOOOM");
	dispbottom("The blast flings you away.");
	warp("prontera", 0, 0);
	end;
```

Again the dispbottoms, and then, a random warp, because the bomb exploded. Then another end; terminates the script
again.  
  
If you would have done this all with NPC timers, your mapserver would have smacked you and perhaps even tackled itself.
Why? Well, the dispbottom and the warp command can only be executed on a player. To execute something on a player, the
script needs to have a so called RID. Addtimer remembers this RID, a NPC timer does not.  
  
Q: What if I click the NPC before both timers run out.  
A: This can be done by setting a player variable @boom before the close2; See
[Variables#Player_Variables](./variables.md#player-variables). Temporary player variable works well along with
addtimer command, as they both behave the same.

- they are attached to the player
- both will disappear when player log out

so the Bomb Squad npc script now look like this

```HercScript
prontera,155,188,2	script	Bomb Squad	1_M_JOBGUIDER,{
	mes("[Dismantler]");
	mes("Where is the bomb? WHERE IS IT??");
	mes("Please help me find it before it explodes.");
	if (@boom == 1)
		close();
	close2();
	@boom = 1;
	addtimer(15000, "Bomb Squad::OnWarn");
	addtimer(30000, "Bomb Squad::OnBoom");
	dispbottom("Dismantler : The bomb will detonate in 30 seconds!");
	end;

OnWarn:
	dispbottom("Dismantler : OH MY GOD! ONLY 15 SECONDS LEFT - HURRY!!!");
	end;

OnBoom:
	dispbottom("*time slows down as suddenly the ticking stops*");
	dispbottom("....");
	dispbottom("BOOOOOOOM");
	dispbottom("The blast flings you away.");
	warp("prontera",0,0);
	@boom = 0;
	end;
}
```

In the code above, we have manipulated the behavior of the NPC to have two separate live states. The first state is
before anyone has clicked the NPC, after which the player variable(@ prefix) boom is set to a value of 1 immediately
following the [close2](./commands/close2.md) command by sending "[set](./commands/set.md) @boom, 1". Then upon clicking the
NPC during the timer sessions the NPC will have a regular [close](./commands/close.md) command after displaying the message
to the player due to the if( @boom == 1 ) check; instead of creating more timers. Once the second timer finishes we also
see the player variable boom set back to 0 with "[set](./commands/set.md) @boom,0;", it's off state.  
  
Now, on to the bomb npc.

```HercScript
prontera,50,50,2	script	Bomb	HIDDEN_NPC,{
	if (@boom == 0)
		end;

	mes("*The bomb has been disarmed*");
	deltimer("Bomb Squad::OnWarn");
	deltimer("Bomb Squad::OnBoom");
	@boom = 0;
	close();
}
```

deltimer command will remove the timer that has previously attached to the player. So if the player previously talk to
the Bomb Squad, will able to disarm the bomb. This will prevent the addtimer from invoking the OnWarn: and OnBoom:
label.  
  
Q: What happens if the player click on the Bomb after 15 seconds, will the server throw error for OnWarn: label already
executed ?  
A: Nope, the server doesn't seem to care about that. This means you can put as many addtimer command, and deltimer all
of them without additional checks. Neat, isn't it?  
  
**Note** : addtimer can only attached to the up to 31 instances on that player. This means, if you have more than a
number of scripts using addtimer command on that player, on 32th queue will throw an error on the server to notify some
of your script has over abuse this command. To lift off this limit, simply increase the MAX_EVENTTIMER in src\map\map.h,
and recompile your server.

# Use Number 3: Deny Usage

Let's start with another example:

```HercScript
prontera,23,20,2	script	Daily Healer	1_M_JOBGUIDER,{
	mes("[Healer]");
	mes("Hello there.");
	mes("I am a special healer, who will fully restore your HP and SP.");
	mes("However, my powers are limited, and I need to rest for a full day after healing you, before I can help you again.");
	next();
	mes("[Healer]");
	mes("Do you want me to heal you?");
	next();
	if (select("Yes", "No") == 2) {
		mes("[Healer]");
		mes("Ok, good bye then.");
		close();
	}

	if (TimeHealed + 86400 > gettimetick(GETTIMETICK_UNIXTIME)) {
		mes("[Healer]");
		mes("I am sorry, but I am not a robot.");
		mes("I am exhausted from the last time I healed you.");
		close();
	}

	mes("[Healer]");
	mes("Ok, here goes!");
	close2();
	percentheal(100, 100);
	TimeHealed = gettimetick(GETTIMETICK_UNIXTIME);
	dispbottom("Healer : Please give me at least a day to recover.");
	end;
}
```

Q: I see no timers?  
A: That is correct. This NPC uses what I would like to call a Static Timer. We will review it in detail below.  
  
Ok, at a first glance, this is a normal healer NPC that fully heals your HP and SP. The interesting part though is at
the bottom. Let's start with the bottom most part:

```HercScript
	close2();
	percentheal(100, 100);
	TimeHealed = gettimetick(GETTIMETICK_UNIXTIME);
	dispbottom("Healer : Please give me at least a day to recover.");
	end();
```

The NPC does the healing here, but after the healing, it sets a weird value to TimeHealed. First, it gets a value from
`gettimetick(GETTIMETICK_UNIXTIME)`. This command returns the amount of seconds elapsed since 1/1/1970, based on your server current time.

```HercScript
	if (TimeHealed + 86400 > gettimetick (GETTIMETICK_UNIXTIME)) {
```

When the player wants to use the NPC again, the NPC first checks if the player is still allowed to be healed. How? Well,
remember, in TimeHealed, we stored the time when the player last used the NPC. With gettimetick(GETTIMETICK_UNIXTIME) we get the current
time in seconds that has elapsed since 1/1/1970, and by adding 86400, which is the amount of seconds that goes in a day
(24 \* 60 \* 60). Those two combined give us the next time the player is allowed to use the NPC again. If the player is
allowed to use the NPC again, the combined value should be in the past, so it should be less than what gettimetick(GETTIMETICK_UNIXTIME)
will return to us. If it is the other way around, the player is not allowed to use the NPC yet, and it will jump inside
the if-statement.  
  
Please note, that using a Static Timer comes with some disadvantages. First, it uses a player variable. Second, the more
dynamic you make it, the more resources it will cost. Although it should be less CPU intensive than a normal timer,
making it dynamic means.  
  
By turning that numbers into a Global variable,

```HercScript
	if ((TimeHealed + $HealInterval) > Gettimetick(GETTIMETICK_UNIXTIME)) {
```

\$HealInterval will be a variable that you can set as a GM through another NPC, to determine the time between two heal
possibilities in seconds.

# Difference between Timers

First, let's give an overview of the different kinds of timers or time triggered labels.

- [NPC Timers](#npc-timers)
- [Player Timers](#player-timers)
- [Label Timers](#label-timers)
- [Other Timers](#other-timers)

## NPC Timers

NPC timers are timers that are executed from the NPC's point of view. This means that it does not require a player to
initiate it, nor a player to use it. A perfect example of this is the Speaking NPC at the start of this article. NPC
timers use the following seven commands:

- `initnpctimer({"NPC Name"}, {<Player RID>});`
- `startnpctimer({"NPC Name"}, {<Player RID>});`
- `stopnpctimer({"NPC Name"}, {<flag>});`
- `getnpctimer(<type>{, "NPC Name"});`
- `setnpctimer(<amount>{, "NPC Name"});`
- `attachnpctimer({<Player RID>});`
- `detachnpctimer({"NPC Name"});`

## Player Timers

Player timers are used for NPCs that can interact with players, and need to have a specific count down or up per player.
Unlike a NPC timer, a Player timer remembers which player started the timer. In other words, it remembers the RID and
reattaches it again when needed. This allows you to alter a player's variable later on in the script, where this is not
possible with a NPC timer. Player timers use similar commands as NPC timers. However, there are only three of them:

- `addtimer(<ticks>, "NPC::OnEvent");`
- `addtimercount(<ticks>, "NPC::OnEvent");`
- `deltimer("NPC::OnEvent");`

## Label Timers

Label Timers aren't timers actually. They are labels that are triggered depending on the current time of the server.
There are several different kinds of them, but they all almost work in the same way. You simply put them in your script
as a label, and they look like this:

- `OnClockXXXX:`
- `OnDayXXXX:`
- `OnHourXX:`
- `OnMinuteXX:`

Where XX is a two digit number and XXXX is a four digit number. SSSXXXX is three letters followed by four digits.  
How they work? Relatively easy. OnClock is already explained in the first part of this article, but here is the recap in
case you forgot. To make it work, you replace XXXX by an actual time in the 24 hour format. The time you put there, is
when the label is triggered. So, for example:

```HercScript
OnClock0700: // This label is triggered at 7 AM servertime.
OnClock1414: // This label is triggered at 2:14 PM servertime.
```

Just like normal labels, you can use the same OnClock label in different NPCs, but, it cannot occur twice in the same
NPC. You can have different OnClocks in the same NPC though.  
OnDayXXXX works a bit like OnClock. The XXXX here stands for a specific day in a specific month. The first XX is the
month, the second XX is the day of that month. When it is that day, it will be triggered. Assumed is, that this happens
only once at the start of that day, or the first time that your server is up during that day. Here are a couple of
examples:

```HercScript
OnDay0101: // This label is triggered on the first day of January.
OnDay0515: // This one is triggered on the fifteenth day of May.
OnDay1231: // This one is triggered on the last day of December.
OnDay0229: // This label is only triggered when it is February 29th, so once every four years
```


OnHourXX and OnMinuteXX are similar in use. With OnHour, the XX stands for a specific hour during the day when it is
triggered. The XX within OnMinute stands for a specific minute per hour. Some examples to make it clear:

```HercScript
OnHour01: // Triggers at 1 AM every day.
OnHour20: // Triggers at 8 PM every day.
OnMinute00: // Triggers at each new hour, so 1:00, 2:00, 3:00, 4:00 etc.
OnMinute17: // Triggers each hour at 17 minutes past. So, 8:17, 9:17, 10:17 etc.
```

Last, and probably the least known is OnSSSXXXX. The best way to describe this one is an OnWeekday label. (OnWeekday
does not exist.) In this label, SSS is replaced by one of the following: Sun, Mon, Tue, Wed, Thu, Fri, Sat. XXXX is
replaced by a number in the same way as the XXXX in OnClockXXXX. It notes a specific time of the day. This label is
triggered on the specified day of the week (SSS) at the specified time in 24 hour format (XXXX). At least, that is the
theory. Here are some examples you can work with:

```HercScript
OnSat1200: // Triggers at noon on each Saturday.
OnTue0707: // Triggers at 7 past 7 AM on Tuesday.
```


Note: Although there is no OnSecondXX or OnMillisecondXXXX label, you can simulate this. Be aware though, this causes a
heavy load on your server. To do this, you will have to use a NPC. Here is a short example simulating OnSecond30 using a
NPC timer:

```HercScript
-	script	Annoying Announcer	FAKE_NPC,{
OnInit:
	initnpctimer();
	end;

OnTimer1000:
	if (gettime(GETTIME_SECOND) != 30)
		end;
	announce("I'm very annoying.", bc_all);
	initnpctimer();
	end;
}
```

And one that triggers every 40 milliseconds:

```HercScript
-	script	Flooder	FAKE_NPC,{
OnInit:
	initnpctimer();
	end;

OnTimer40:
	announce("Flood!", bc_all);
	initnpctimer();
	end;
}
```

## Other Timers

These timers are actually nowhere related to timers. To be exact, they are event triggered labels, but let's go over
them anyway, because they are useful. The timers I'm referring to are the following:

- [Event: OnInit](./events/oninit.md): - Is triggered on server start up.
- [Event: OnInterIfInit](./events/oninterifinit.md): - Is triggered when the mapserver connects to the charserver.
- [Event: OnInterIfInitOnce](./events/oninterifinitonce.md): - Is only triggered on the first time the map server connects to
  the char server. If it loses connection after that, and gets a connection again, these labels are no longer triggered
  (unless the map server is really restarted).
- [Event: OnAgitInit](./events/onagitinit.md): - Is triggered when WoE is initiated.
- [Event: OnAgitStart](./events/onagitstart.md): - Is triggered when WoE is started.
- [Event: OnAgitEnd](./events/onagitend.md): - Is triggered when WoE ends.
- [Event: OnTimerX](./events/ontimer.md): - Is triggered when a player or NPC timer reaches the value X in milliseconds.

There are many more of these kinds of special event triggered labels, like the login event, but these, with the
exception of OnTimerX, are all triggered without the need of a player. With OnTimerX, the X should be replaced by a time
in milliseconds, for example:

```HercScript
OnTimer100: // Triggers 100ms after a player timer or NPC timer is started in the same NPC.
OnTimer3600000: // Triggers 1 hour after a player timer or NPC timer is started in the same NPC.
```

## Recap

The above information should help you make a decission on what timertype to use. For example, if you do not need to do
anything with the player who starts it, or don't need a player to start it, use a NPC timer. When you want to do stuff
related to a player, or which needs an RID, use a player timer. When you want something to happen at a specific moment
in time, use one of the On labels. And when you want your server to lag badly, simulate OnMillisecondXXXX.

# NPC Timers in detail

In this section, we will explain how each NPC Timer command works in detail. First another quick list of the available
NPC Timers:

- `initnpctimer({"NPC Name"}, {<Player RID>});`
- `startnpctimer({"NPC Name"}, {<Player RID>});`
- `stopnpctimer({"NPC Name"}, {<flag>});`
- `getnpctimer(<type>{, "NPC Name"});`
- `setnpctimer(<amount>{, "NPC Name"});`
- `attachnpctimer({<Player RID>});`
- `detachnpctimer({"NPC Name"});`

Now that you know the commands, you will have to know how NPC Timers actually work. It is quite easy to be honest. A NPC
can have one timer attached to it, which basically is a stopwatch. When you start a timer, a kind of NPC like variable
will start running, often from 0. Every millisecond (1 second is 1000 milliseconds or 1000 ms), 1 is added to this
variable. So, after 1 second, the variable will be 1000. After 12.5 seconds, the variable will be 12500.  
Now, on each tick (tick means every increment of this variable), the timer will check if inside the NPC it is running
from or attached to, if there is a label that matches his current value. The labels have a special format, and look like
this:

`OnTimerXXXXX:`

Where XXXXX is a number that can be as small as 0, or as big as 2,147,483,647 (roughly 24 days). If the value of the
timer matches one of those labels, then the NPC will start running at that specific label. So, let's say you have a
label OnTimer1000: (1 second), and you have started a NPC timer, then one second later, the script will jump to that
label, and start executing the code underneath it.  
Often, when using NPC Timers, you want to stop them at some point, or reset them, to make the NPC start over again. For
this purpose, the developers have written several commands that are now at our disposal, which
allow us to manipulate this NPC based timer.  
A last thing you need to know, before we go into detail on the specific commands, is that by default a NPC Timer will
run in the same NPC as where the command is found, and that there is no player attached. The last part means, that you
will be unable by default to manipulate the player, variable wise or command wise.  

## InitNPCTimer

This command allows you create a new NPC timer, if it doesn't already exist, and have it start counting from 0. The NPC
timer is attached to a NPC, normally the one you start it from. This means, that it will look for certain OnTimer labels
inside that NPC alone. However, you can also make the command start a NPC Timer in another NPC. To do this, you will
have to specify a NPC Name. You can even attach a player to the NPC Timer. To do this, you must specify the RID when
using `initnpctimer`. This will allow your timer to execute commands that require a player's RID, like warp or
countitem.  
On top of that, you can also specify both a NPC Name and a Player RID. For that, put the NPC Name first, then a comma,
and then the player's RID.  
For those unfamiliar of what an RID is, the RID is a kind of hook with which online players are recognized. When coming
online, the player's RID will be set equal to his account ID (`getcharid(CHAR_ID_ACCOUNT)`).  
  
Some examples:

```HercScript
initnpctimer(); // Start a new NPC timer and make it count from 0.
initnpctimer("My Other NPC"); // Start a new NPC timer in the NPC named "My Other NPC" and make it count from 0.

initnpctimer(getcharid(CHAR_ID_ACCOUNT)); // Start a new NPC timer and make it count from 0. Also, attach the current player to the timer.
initnpctimer("My Other NPC", getcharid(CHAR_ID_ACCOUNT)); // Start a new NPC timer in the NPC named "My Other NPC". Also, attach the current player to the timer.
```

## StartNPCTimer

This command almost works the same as [InitNPCTimer](./commands/initnpctimer.md). The only major difference is that it
doesn't set the counter, or if you like, the timer variable, to 0. It simply continues where it was. So, if you started
the NPC Timer with `initnpctimer`, and stopped it later on, but want it to start again where it left off, then you use
this command. If you like you can read `continuenpctimer` instead of `startnpctimer`.  

Again, for the various options, you might want to look at `InitNPCTimer`. We will just show
some examples here:  

```HercScript
startnpctimer(); // Continues the NPC timer where it left off, or start a new one if there isn't a timer already.

startnpctimer("My Other NPC"); // Same as above, but starts it in the NPC named "My Other NPC".
startnpctimer(getcharid(CHAR_ID_ACCOUNT)); // Same as the first one, but attaches the current player to the timer.
startnpctimer("My Other NPC", getcharid(CHAR_ID_ACCOUNT)); // Combination of the two above.
```

## StopNPCTimer

This command is the counterpart of `StartNPCTimer`. What it does, you've guessed it, it stops
(or pauses) the timer. As for the parameters, the NPC Name part is exactly the same as with
`InitNPCTimer`. If you specify a flag value (can be any non-zero value, zero will simply be
ignored), then **stopnpctimer** will also detach the player, if any was attached to it.  
  
Some examples again:

```HercScript
stopnpctimer(); // Pauses the NPC timer in the current NPC.
stopnpctimer("My Other NPC"); // Pauses the NPC timer in the NPC named "My Other NPC"
stopnpctimer(1); // Pauses the NPC timer in the current NPC and detaches any attached player.
stopnpctimer("My Other NPC", 1); // Combination of the two above.
```

## GetNPCTimer

[GetNPCtimer](./commands/getnpctimer.md) is a bit of a tricky command. Basically it can be used to read out the statistics
on a certain NPC Timer. (Either the one in the current NPC, or the one defined by the parameter "NPC Name".) There are
three different statistics for a NPC Timer, which are:  
  
\* 0 - Current Tick Count

- 1 - Remaining OnTimer labels
- 2 - Already executed OnTimer labels

  
  
The first one (0), basically is a variable which holds the amount of milliseconds that the timer is on.  
  
The second one (1), holds the amount of labels that the timer will still have to do in the NPC, if it is not reset or
stopped prematurely.  
  
The third one (2), holds the amount of OnTimer labels which the timer already has executed. Most likely,
**initnpctimer** resets this counter. What **startnpctimer** does to this statistic, is unknown at the moment.  
  
[GetNPCimer](./commands/getnpctimer.md) always needs to have a type (one of the three above) specified when being used. For
the second stat of the three, when there was originally a player attached, then it will still need this player to be
attached, or it will give you back an error and return 0.  
  
Some examples:

```HercScript
getnpctimer(0); // Returns the current amount of ticks.
getnpctimer(0,"My Other NPC"); // Does the same, only for the NPC named "My Other NPC".
getnpctimer(1); // Returns the amount of OnTimer labels that are still untriggered.
getnpctimer(1,"My Other NPC"); // Same as above, but for the NPC named "My Other NPC".
getnpctimer(2); // Returns the amount of OnTimer labels that have already been triggered.
getnpctimer(2,"My Other NPC"); // Same as above, but for the NPC named "My Other NPC".
```

**Note:** Currently there is no way to retrieve the value of getnpctimer(0) with attachnpctimer;. It's still mark as a
[TODO](https://github.com/HerculesWS/Hercules/blob/e711753b9d584845e385ada29780b9ed216c4f55/src/map/npc.c#L771) in the
source code ;-)

## SetNPCTimer

[SetNPCTimer](./commands/setnpctimer.md) is the counterpart of [GetNPCTimer](./commands/getnpctimer.md). However, it only
allows you to change the current amount of ticks (elapsed milliseconds) of a specific timer. If you define a NPC Name
with it, it will use the timer in that NPC, otherwise, it will try to alter the timer in the NPC where the command is
in. The amount you set the NPC Timer to, should be given in ticks, or milliseconds. The command theoritically works even
when a NPC timer is stopped, but probably does not work when no NPC Timer has ever started in the NPC. This is about all
there is to this command. It works, no matter if there is a player attached to it or not.  
  
Some examples again:

```HercScript
setnpctimer(10000); // Sets the NPC Timer of the current NPC to 10 seconds.
setnpctimer(2345, "My Other NPC"); // Sets the NPC Timer in the NPC named "My Other NPC" to 2345 ticks or ms.
setnpctimer(0); // Sets the current NPC Timer to 0.
```

  
Note:  
In the current revisions, **setnpctimer** also pauses the timer when changing the value. So, do not forget to use
**startnpctimer**; after using **setnpctimer**, or your timer will not continue to run. (This might be changed in later
revisions)  
  

## AttachNPCTimer

[AttachNPCTimer](./commands/attachnpctimer.md) allows you to attach a player to a NPC later on. This can only be done to
the NPC Timer that is in the same NPC as where this command is used. To attach a player, you will simply have to give
his account id or RID (or UID/GID in some devs words) as a parameter.  
  
Examples:

```HercScript
attachnpctimer(getcharid(3)); // Attaches current player to the NPC Timer.`  
attachnpctimer(2000000); // Attaches the player with account id 2000000 to the NPC Timer, if he is online.`
```

## DetachNPCTimer

[DetachNPCTimer](./commands/detachnpctimer.md) is the opposite of [AttachNPCTimer](./commands/attachnpctimer.md). Unlike its
counterpart however, you can use it outside its current NPC. To do this, simply specify the name of the other NPC as
parameter. This is optional of course.  
  
Examples:

```HercScript
detachnpctimer(); // Detaches the attached player from the NPC Timer, if anyone was attached.`  
detachnpctimer("My Other NPC"); // Does the same, only for the NPC named "My Other NPC".`
```

## Pro's and Cons

Using NPC Timers have specific advantages and disadvantages. These will be listed in a compact way next.  
Advantages:

- Can be specific bound to any NPC.
- No need for a player, but can be attached.
- Can be used on start up or time triggered labels.
- Can be looped/resetted easily.
- Can be manipulated/read out in various ways.

Disadvantages:

- NPC bound, so, if multiple players use the NPC, the timer will restart each time. (Can cause unexpected results.)
- Only one NPC Timer can run per NPC.

# Player Timers in detail

In this section, we will explain how each Player Timer command works in detail. First another quick list of the
available Player Timers:

- [addtimer](./commands/addtimer.md)`(<ticks>, "NPC::OnEvent")`;
- [addtimercount](./commands/addtimercount.md)`(<ticks>, "NPC::OnEvent")`;
- [deltimer](./commands/deltimer.md)`("NPC::OnEvent")`;

The list of player timer commands is significally shorter than the list of NPC Timers. This is right away one of the
well.., downsides of the player timer. It has less flexibility. However, player timers are easier to work with for the
same reason.  
Player timers work in a reverse way from NPC Timers. Basically you enter a number in milliseconds (1 second is 1000
milliseconds), and a timer attached to the player who triggered it, will run down from that number to 0. When it reaches
0, it will jump to the eventlabel specified in the second parameter of addtimer.  
Besides starting a timer, and let it run it's course, you can also delay it, and even delete it before it reaches 0.
Also, a player timer, is like the word indicates, unique for each player for each label. So, a player will not influence
the timer of another player in normal circumstances, and you can even start different timers for the same player, as
long as the event label is different each time.  

## AddTimer

Addtimer allows you to start a new timer for the player who is currently interacting with the script. It has two
parameters, which are not optional:

- ticks
- "NPC::OnEvent"

Ticks is a number which you specify, which is the starting time, in milliseconds. The timer will start to run
immediately after this line, substracing 1 from the tickcount each millisecond, until it reaches 0.  
The NPC::OnEvent, is an event label which you must specify. It must be for the following format: "NPC
NAME::OnYourLabel", where OnYourLabel is an existing label that starts with On, in the NPC named NPC NAME. When the
timer runs down to 0, it will jump to that label in that NPC. For easiness sake, let's call the "NPC::OnEvent" part of
the command, and the upcoming commands, also the name of the player timer.  
Well, that is all there is to the addtimer command, so some last examples:

```HercScript
addtimer(1000, "My NPC::OnMyLabel"); // Starts a timer that runs out after 1000 ms (1 second), and then jumps to OnMyLabel in My NPC.
addtimer(60000, "NPC1::OnLoser"); // After 60 seconds, this timer runs out, and jumps to OnLoser in the NPC named NPC1.
```

## AddTimerCount

Addtimercount allows you to 'delay' a previously started timer. It takes the current amount of ticks left, and add the
amount specified by the parameter ticks. So, in essence, this delays the timer by `<ticks>` amount of milliseconds. For
which timer it does this, is up to you and the player who is currently attached to the script. Which timer you want to
alter, is what you specify with the second parameter, "NPC::OnEvent" (or as said earlier, the name of the timer).  
Some examples:

```HercScript
addtimercount(5000, "My NPC::OnMyLabel"); // Adds 5 seconds to the timer with the name "My NPC::OnMyLabel".
addtimercount(-10000, "NPC1::OnLoser"); // Removes 10 seconds from the timer with the name "NPC1::OnLoser".
```

## DelTimer

Deltimer is the counterpart of [Addtimer](./commands/addtimer.md). It stops and deletes a previously created timer that had
the same event label/name as specified in the parameter. Of course, it only does this for the timer of the player that
is currently attached to the script, but well, that is all it does.  
Some examples:

```HercScript
deltimer("My NPC::OnMyLabel"); // Erases the timer that was supposed to jump to OnMyLabel in the NPC named My NPC.
deltimer("NPC1::OnLoser"); // Erases the timer named NPC1::OnLoser. (Name == Event label)
```

## Pro's and Cons

Using Player Timers have specific advantages and disadvantages. These will be listed in a compact way next.  
Advantages:

- Multiple Player Timers can run per NPC.
- Multiple Player Timers can be run per player.
- Can be manipulated easily.

Disadvantages:

- You always need a player attached to the script to use this.
- The timer is erased on log out. (Can be an advantage as well.)
- Cannot be read out without abusing a variable.
- Cannot be used when server start up or npc only triggered labels, otherwise the server will throw `*Player not
  Attached!*` error
