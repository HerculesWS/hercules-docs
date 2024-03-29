# `autobonus3()`

!!! warning
	This page may contain outdated information, incompatible with the current version of Hercules and its coding standards.

## Syntax

```c
autobonus3(<bonus script>, <rate>, <duration>, <skill id>, {<other script>});
autobonus3(<bonus script>, <rate>, <duration>, "<skill name>", {<other script>});
```

## Description

These commands are meant to be used in item scripts. They will probably 
work outside item scripts, but the bonus will not persist for long. They, 
as expected, refer only to an invoking character.

What these commands do is "attach" a script to the player which will get
executed on attack (or when attacked in the case of [`autobonus2()`](autobonus2.md)).

`rate` is the trigger rate of the script (10000 = 100%). 

`duration` is the time that the bonus will last for since the script has 
triggered.

`skill ID`/`skill name` the skill which will be used as trigger to start the 
bonus (for `autobonus3()`).

The optional argument `flag` is used to classify the type of attack where 
the script can trigger (it shares the same flags as the `bAutoSpell` bonus 
script):

Range criteria:
- `BF_SHORT`:  Trigger on melee attack
- `BF_LONG`:   Trigger on ranged attack
- Default:   `BF_SHORT + BF_LONG`

Attack type criteria:
- `BF_WEAPON`: Trigger on weapon skills
- `BF_MAGIC`:  Trigger on magic skills
- `BF_MISC`:   Trigger on misc skills
- Default:   `BF_WEAPON`

Skill criteria:
- `BF_NORMAL`: Trigger on normal attacks
- `BF_SKILL`:  Trigger on skills
- Default:   If the attack type is `BF_WEAPON` (only) `BF_NORMAL` is used, otherwise `BF_SKILL + BF_NORMAL` is used.

The difference between the optional argument `other script` and the `bonus script` is that, the former one triggers only when attacking (or attacked) 
and the latter one runs on status calculation as well, which makes sure, within the duration, the bonus that get lost on status calculation is 
restored. So, `bonus script` is technically supposed to accept [`bonus()`](bonus.md) command only. And we usually use `other script` to show visual effects.

In all cases, when the script triggers, the attached player will be the one who holds the bonus. There is currently no way of knowing within this
script who was the other character (the attacker in [`autobonus2()`](autobonus2.md), or the target in [`autobonus()`](autobonus.md) and `autobonus3()`).

## Example

```c
//Grants a 1% chance of starting the state "all stats +10" for 10 seconds 
//when using weapon or misc attacks (both melee and ranged skills) and 
//shows a special effect when the bonus is active.
autobonus("{ bonus(bAllStats, 10); }", 10, 10000, BF_WEAPON | BF_MISC, "{ specialeffect2(EF_FIRESPLASHHIT); }");
```
