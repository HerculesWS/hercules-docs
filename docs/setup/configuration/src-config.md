This page provides information on the **/src/config/** folder and its settings. The **/src/config/** folder contains
special server settings that allow you to further customize your server, the most popular of them being **RENEWAL**, a
switch to enable or disable Ragnarok Renewal mechanics

### /src/config/const.h

------------------------------------------------------------------------------------------------------------------------

This file does not posses any settings, it is used to store constants used by other settings.

### /src/config/core.h

------------------------------------------------------------------------------------------------------------------------

The core configuration file (which is inherited by map.h) that inherits all other configuration files, at this point in
time this file does not possess any settings

### /src/config/renewal.h

------------------------------------------------------------------------------------------------------------------------

This configuration files provides Ragnarok Renewal settings for you to further customize your server

#### RENEWAL

  
This setting affects the following mechanics

- Renewal MATK
- Renewal MDEF
- Renewal DEF
- Renewal Status Points
- Renewal Heal Formula
- Renewal ASPD Shield Penalty
- Renewal Stat Bonuses (str,agi,vit,flee,hit,etc)
- Renewal Files
  - *item_db_re.txt*, *statpoint_renewal.txt*, *job_db_re.txt*, [and others](DB_Folder_Inheritance "wikilink") are only
    loaded in this mode. [Check the DB Inheritance page for all](DB_Folder_Inheritance "wikilink")

**How to Disable**

- Commenting it's \#define RENEWAL line out makes it disable (add **//** before \#define)

#### RENEWAL_DROP

  
This setting enables or disables Ragnarok Renewal drop rate modifier, which is based on the level difference between a
character and the monster it killed

The modifier depends on the following table

{\|border="1" style="text-align:center;"

\|- \| **Difference in Base Level** \|\| **Drop Rate** \|- \| 30 levels above monster or more \|\|
<font color="red">50%</font> \|- \| + 15 ~ 29 \|\| <font color="red">60%</font> \|- \| + 10 ~ 14 \|\|
<font color="red">75%</font> \|- \| + 6 ~ 9 \|\| <font color="red">90%</font> \|- \| + 1 ~ 5 \|\| 100% \|- \| Equal \|\|
100% \|- \| - 1 ~ 10 \|\| 100% \|- \| - 11 ~ 13 \|\| <font color="red">75%</font> \|- \| 15 levels below monster or more
\|\| <font color="red">50%</font> \|}

  
**For Example**, if you are level 50, and you kill a monster level 10, which normally drops a item at 50%, for you it'd
drop at 25% (because you're 30 levels or higher than it)

**How to Disable**

- Commenting it's \#define RENEWAL_DROP line out makes it disable (add **//** before \#define)

#### RENEWAL_EXP

  
This setting enables or disables Ragnarok Renewal exp rate modifier, which is based on the level difference between a
character and the monster it killed

**How to Disable**

- Commenting it's \#define RENEWAL_DROP line out makes it disable (add **//** before \#define)

#### RENEWAL_CAST

  
This setting enables or disables **Renewal Casting** and in it, cast time is decreased by DEX\*2+INT, 20% of the cast
time is not reduced by stats, for example, on a skill whose cast time is 10s, only 8s may be reduced. other 2s are part
of a "fixed cast time" that is only reduced by special items and skills (such as Arch Bishop's Sacrament skill). **When
disabled** it uses the old cast time method, influenced by dex, items and skills  

**How to Disable**

- Commenting it's \#define RENEWAL_CAST line out makes it disable (add **//** before \#define)

#### RENEWAL_CAST_VMIN

:\* **Note**: This setting only matters if **RENEWAL_CAST** is enabled

  
This setting allows you to specify how many points a user is required to have to reach instant cast

- **VALUE**: The formula is (casterDex x 2) + (casterInt), **default value** is **530**

#### RENEWAL_EDP

  
This setting enables or disables Ragnarok Renewal mechanics for **Enchant Deadly Poison** skill,  

the changes compared to old mechanics are:

- EDP doesn't increases final damage by 400%, instead it increases your weapon atk and your stat atk
- EDP doesn't affect **Grimtooth** skill

**How to Disable**

- Commenting it's \#define RENEWAL_EDP line out makes it disable (add **//** before \#define)

### /src/config/secure.h

------------------------------------------------------------------------------------------------------------------------

This configuration files provides additional security features to your server

#### SECURE_NPCTIMEOUT

  
When enabled all npcs dialog will 'timeout' if user is on idle for longer than the amount of seconds allowed, on
'timeout' the npc dialog window changes it's next/menu to a 'close' button

- **VALUE** is the amount of **seconds** you want the server to wait prior to timeout an idle NPC dialog

#### SECURE_NPCTIMEOUT_INTERVAL

:\* **Note**: This setting only matters if **SECURE_NPCTIMEOUT** is enabled

  
This setting is the amount of **seconds** you want the server to wait prior to checking if an NPC dialog is idle

### /src/config/classes/general.h

This configuration files provides settings for you to further customize your server skills

#### RR_MAGIC_REFLECTION

:\* **Note**: This setting exists because server owners were exposed to the unofficial magical reflection for several
years, and expecting many to not want to change this setting was made.

  
When enabled the official magical reflection is used, official magical reflection damage is calculated against *the
caster*, while the unofficial magical reflection calculates the reflected damage against *the target*.  

**How to Disable**

- Commenting it's \#define MAGIC_REFLECTION_TYPE line out makes it disable (add **//** before \#define)

### /src/config/classes/swordsman.h

------------------------------------------------------------------------------------------------------------------------

This configuration files provides settings for you to further customize your server's swordsman skills

#### MAX_RUNE

  
This setting allows you to specify how many rune knight's runes of the same type an character is able to hold in his
inventory  

**Default** value for this setting is 20

[Category:Source Snippets](Category:Source_Snippets "wikilink")
