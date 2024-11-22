This article is aimed at configuration of Hercules for use. It is assumed that you have
[downloaded](Installation "wikilink") Hercules, have it [compiled](Compiling "wikilink") and
[configured](Connecting "wikilink") to connect.

# Hercules File Structure

When you open up your copy of Hercules for the first time, you may notice a lot of folders and files, we'll walk through
briefly what each one is for.

| Location           | Description                                                                                                                        |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------|
| **/3rdparty/**     | 3rd party files, such as mysql.h                                                                                                   |
| **/conf/**         | Main configuration settings, such as connection settings, battle settings and [mapflags](mapflag "wikilink").                      |
| /conf/import/      | [Import folder](Import_folder "wikilink"), mainly used to keep your configuration settings after an SVN update.                    |
| /conf/battle/      | Where you will find settings to change the rates, drops, max stats and such for your server.                                       |
| /conf/mapflags/    | Folder with all the [mapflags](mapflag "wikilink"), such as noteleport, pvp and gvg.                                               |
| **/db/**           | Databases, such as the job_db, experience tables, item and mob flat-file databases.                                                |
| **/doc/**          | Various documented settings, mainly for database settings.                                                                         |
| **/npc/**          | Any NPC/spawn file you will find in the game is in here.                                                                           |
| /npc/airports/     | The airports and airship scripts are in here, and any NPC related to them.                                                         |
| /npc/battlegrounds | Battlegrounds scripts can be found in here.                                                                                        |
| /npc/cities/       | Any non-quest, non-kafra [NPC](NPC "wikilink") found in the towns are here.                                                        |
| /npc/custom/       | Any NPC not officially supported by Hercules is located in here. Here is where you will find your healers, warpers and MVP arenas. |
| /npc/events/       | Any official events, such as twin-towers or Christmas events on the official servers.                                              |
| /npc/guides/       | Any guides in the cities.                                                                                                          |
| /npc/guild/        | [WoE](War_of_Emperium "wikilink") scripts and functions are in here.                                                               |
| /npc/guild2/       | WoE:SE scripts and functions.                                                                                                      |
| /npc/jobs/         | Job changing scripts and quests, as well as functions.                                                                             |
| /npc/kafras/       | Kafra scripts and functions.                                                                                                       |
| /npc/merchants/    | Any official merchants in here.                                                                                                    |
| /npc/mobs/         | Spawn scripts for fields, dungeons as well as city cleaners in here.                                                               |
| /npc/other/        | Scripts that don't really fit anywhere else, like the marriage script.                                                             |
| /npc/quests/       | Official Quests, such as the Sign Quest or Thanatos Tower.                                                                         |
| /npc/warps/        | Warp portals, and scripts, that behave that way.                                                                                   |
| **/sql-files/**    | If using SQL, this is where the pre-made database dumps are, that will populate your database with the correct tables and such.    |
| **/src/**          | All source files, the meat and potatoes of the emu.                                                                                |
| /src/char/         | Character server source files.                                                                                                     |
| /src/common/       | Common server settings. [mmo.h](mmo.h "wikilink") is in here, the file that will modify most of the hard-coded server settings.    |
| /src/login/        | Login server source files.                                                                                                         |
| /src/map/          | Map server source files.                                                                                                           |
| /src/plugins/      | Plugins source files.                                                                                                              |
| /src/tool/         | \[Tools\](https://github.com/HerculesWS/Hercules/tree/stable/src/tool) source files, such as the mapcache builder.                 |
| **/tools/**        | Contains tool scripts for various maintenance-related tasks.                                                                       |
| **/vcproj-9/**     | Project 9 Files,Files used if Using MS Visual Studio C++ 2008                                                                      |
| **/vcproj-10/**    | Project 10 Files,Files used if using MS Visual Studio C++ 2010                                                                     |
| **/vcproj-12/**    | Project 12 Files,Files used if using MS Visual Studio C++ 2012                                                                     |

We're mainly focused on the **/conf/** folder in this article.

# /conf/

In the /conf/ folder, holds all of the configuration settings for a quick customization. Here are the locations for a
frequent number of configuration changes. Remember that after changing any of these settings, it is always best to
restart your servers for the changes to take effect.

## Changing the base/job experience rates

Open up /conf/battle/exp.conf. Look for: <code>

    // Rate at which exp. is given. (Note 2)
    base_exp_rate: 100

    // Rate at which job exp. is given. (Note 2)
    job_exp_rate: 100

</code>

and change to whatever you want, in multiples of 100. A good rule of thumb is to get your number, say you want 10x
rates. Input 10, then add 2 zero's (0) to it to make it 1000.

## Changing multi level ups

Open up /conf/battle/exp.conf. Search for: <code>

    // Turn this on to allow a player to level up more than once from a kill. (Note 1)
    multi_level_up: no

</code> and change it to a 'yes'.

## Changing the required DEX for insta-cast

Open up /conf/battle/skill.conf. Search for: <code>

    // At what dex does the cast time become zero (instacast)?
    castrate_dex_scale: 150

</code> And change to whatever you want it to be.

## Changing the max stats

Open up /conf/battle/player.conf. Search for: <code>

    // Max limit of char stats. (agi, str, etc.)
    max_parameter: 99

    // Same as max_parameter, but for 3rd classes.
    max_third_parameter: 120

    // Same as max_parameter, but for baby classes.
    max_baby_parameter: 80

    // Same as max_parameter, but for baby 3rd's.
    max_baby_third_parameter: 108

</code> And change it to whatever you want it to be.

## Setting the max levels

Please see [Edit Max Level](Edit_Max_Level "wikilink").

## Setting PK in your server

Navigate to /conf/battle/misc.conf. Find: <code>

    // PK Server Mode.  Turns entire server pvp(excluding towns). Experience loss is doubled if killed by another player.
    // When players hunt monsters over 20 levels higher, they will receive 15% additional exp., and 25% chance of receiving more items. 
    // There is a nopvp.txt for setting up maps not to have pk on in this mode.  Novices cannot be attacked and cannot attack.
    // Normal pvp counter and rank display are disabled as well.
    // Note: If pk_mode is set to 2 instead of 1 (yes), players will receive a 
    //   manner penalty of 5 each time they kill another player (see manner_system 
    //   config to adjust how this will affect players)
    pk_mode: 0

</code> Set this to a '1' for PK mode without karma/manner system, set to '2' to enable karma/manner system.

You should also take a look at: <code>

    // For PK Server Mode. Change this to define the minimum level players can start PK-ing
    pk_min_level: 55

</code> And change that setting accordingly as well.

## Monsters with HP/MaxHP/Level/percent HP displays

To get your monsters to display either their level, HP/MAXHP or percent of HP remaining, open up
/conf/battle/monster.conf. Look for: <code>

    // Display some mob info next to their name? (add as needed)
    // (does not works on guardian or emperium)
    // 1: Display mob HP (Hp/MaxHp format)
    // 2: Display mob HP (Percent of full life format)
    // 4: Display mob's level
    show_mob_info: 0

</code> You can change this setting to anything, either 1, 2, 3, 4, 5, 6 or 7, by adding what you want to display
together. Please note that not all of the information, if multiple things are displayed, may fit.

For example, I want mob level and mob percent of HP showing, I would set this to 6.

## Setting Drop rates

Open up /conf/battle/drops.conf and look for the following:

`// The rate the common items are dropped (Items that are in the ETC tab, besides card)`  
`item_rate_common: 100`  
`item_rate_common_boss: 100`  
`item_drop_common_min: 1`  
`item_drop_common_max: 10000`  
  
`// The rate healing items are dropped (items that restore HP or SP)`  
`item_rate_heal: 100`  
`item_rate_heal_boss: 100`  
`item_drop_heal_min: 1`  
`item_drop_heal_max: 10000`  
  
`// The rate at which usable items (in the item tab) other then healing items are dropped.`  
`item_rate_use: 100`  
`item_rate_use_boss: 100`  
`item_drop_use_min: 1`  
`item_drop_use_max: 10000`  
  
`// The rate at which equipment is dropped.`  
`item_rate_equip: 100`  
`item_rate_equip_boss: 100`  
`item_drop_equip_min: 1`  
`item_drop_equip_max: 10000`  
  
`// The rate at which cards are dropped`  
`item_rate_card: 100`  
`item_rate_card_boss: 100`  
`item_drop_card_min: 1`  
`item_drop_card_max: 10000`  
  
`// The rate adjustment for the MVP items that the MVP gets directly in their inventory`  
`item_rate_mvp: 100`  
`item_drop_mvp_min: 1`  
`item_drop_mvp_max: 10000`  
  
`// The rate adjustment for card-granted item drops.`  
`item_rate_adddrop: 100`  
`item_drop_add_min: 1`  
`item_drop_add_max: 10000`  
  
`// Rate adjustment for Treasure Box drops (these override all other modifiers)`  
`item_rate_treasure: 100`  
`item_drop_treasure_min: 1`  
`item_drop_treasure_max: 10000`

All item_rate\_\* values can range from 0 to 1000000 (100 = 100%) and item_drop\_\* values can range from 1 to 10000
(100 = 1.00%). The meaning of the lines is explained using the common items block, but can be applied to other blocks as
well (read the comments of each block, to see, what they refer to). Where there is no 'boss' line, it is simply not
applicable to differentiate between normal and boss monsters.

`item_rate_common: 100`

Specifies the rate adjustment for (common) items dropped by non-boss monsters. This means, if this is set to 100 (100%),
all drop rates in the mob db are used, as is. If you set it to 600, drop rates will be 6 times high as in mob db. So
0.01% drop rate for cards would become 0.06%.

`item_rate_common_boss: 100`

Specifies the rate adjustment for (common) items dropped by boss monsters. Works like item_rate_common.

`item_drop_common_min: 1`

Specifies the minimum drop chance of (common) items. By default this is 1 (0.01%). All drop rates, which would render
lower than this value, due to the effect of their respective item_rate\_\* settings, will be set to this value. Having
this value set to 4 and rate to 100% would cause all cards and rare items, which are dropped at 0.01% being dropped at a
chance of 0.04%.

`item_drop_common_max: 10000`

Specifies the maximum drop chance of (common) items. By default this is 10000 (100%). Any drop chance, which would be
higher than this value, is set to this value.

## Setting a limit on the amount of castles a guild can own

You can limit the amount of castles a guild can hold. Any guild that has the allotted number of castles will deal '0'
damage to the emp they try to take after hitting the threshold. Open up /conf/battle/guild.conf. Find: <code>

    // Maximum castles one guild can own (0 = unlimited)
    guild_max_castles: 0

</code> Set this to whatever you want the maximum to be.

## Setting what characters are allowed in a character name

Typically, we don't want character names that contain ASCII weird characters or whatnot. Here is a great example that
will limit the characters a name can use to what's on the standard American Keyboard. Open up /conf/char_athena.conf and
look for: <code>

    // Manage possible letters/symbol in the name of charater. Control character (0x00-0x1f) are never accepted. Possible values are:
    // NOTE: Applies to character, party and guild names.
    // 0: no restriction (default)
    // 1: only letters/symbols in 'char_name_letters' option.
    // 2: Letters/symbols in 'char_name_letters' option are forbidden. All others are possibles.
    char_name_option: 1

    // Set the letters/symbols that you want use with the 'char_name_option' option.
    // Note: Don't add spaces unless you mean to add 'space' to the list.
    char_name_letters: `1234567890-=qwertyuiop[]\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?

</code> And set it to exactly what I have here.

## Changing "Welcome to Hercules SVN Version!" text

The "Welcome to Hercules SVN! Enjoy! Please report any bugs you find." text can be changed or removed. Open up
/npc/motd.txt and change as needed. Please keep note of the contents in the file:

`// Internal default is limited to 128 lines.  If you need more, you will need to modify the MOTD_LINE_SIZE definition in pc.c`

To disable this message altogether simply delete the contents of the file, \[b\]but do not delete the entire file
itself. Errors will arise in your map server\![/b\]

## Grf-files.txt

This is where you put the path to your Ragnarok Online directory. You only need to set *grf* and/or *data_dir*, if you
[load maps from GRFs rather than from map-cache](#Overriding_map-cache "wikilink").

Example:

`//-----------------------------------------`  
`// GRF List`  
`//-----------------------------------------`  
`// grf: C:\path\to\RO\data.grf`  
`// You may add more in this format`  
`// grf: `<data file path>  
`grf: C:\Program Files\Gravity\RO\data.grf`  
`grf: C:\Program Files\Gravity\RO\rdata.grf`  
`grf: C:\Program Files\Gravity\RO\YourRO.grf`  
  
`//------ Others ---------------------------`  
  
`// Data Directory (without the actual data\ though)`  
`// the below example would use C:\path\to\RO\data\`  
`//data_dir: C:\path\to\RO\`  
`data_dir: C:\Program Files\Gravity\RO\`

If you have a custom GRF you add it here. For 64-bit Windows the path will be Program Files(x86).

## Changing what displays with the command @help

Help.txt will change what displays for the @commands related to help (@h, @help), and help2.txt will change what
displays for @h2 and @help2. The first text basically explains it all, 0 to display the help line and you can use other
numbers for other GM levels.

## Changing the max number of hairstyles and palettes

In client.conf, change the following numbers to the number of hairstyles/palettes you have:

`// valid range of dye's and styles on the client`  
`min_hair_style: 0`  
`max_hair_style: 25`  
`min_hair_color: 0`  
`max_hair_color: 8`  
`min_cloth_color: 0 `  
`max_cloth_color: 4`

Don't go past the number of hairstyles/palettes you have though, or else you might get errors when using a
hairstyle/palette NPC, but only if the NPC goes over the number of hairstyles/palettes you have.

## Overriding map-cache

If you do not want to update your map-cache each time your maps change or are added, you might want to read map data
from GRFs. To do so, you need to edit map_athena.conf at:

`// Read map data from GATs and RSWs in GRF files or a data directory`  
`// as referenced by grf-files.txt rather than from the mapcache?`  
`use_grf: no`

Set this value to **yes**, to enable GRFs as map data storage. You need to set-up
[grf-files.txt](#Grf-files.txt "wikilink") to point to the archives, which contain your maps. Note, that
[resnametable.txt](resnametable.txt "wikilink") (which allows setting up map aliases) is currently read from GRF
archives only.

# /conf/atcommand.conf and /conf/groups.conf

As of Hercules trunk r15572, the charcommands and atcommands are configured in the groups.conf. The server reads this
file to decide who can use what command. normal players are id: 0, while the Administrators have the ultimate control at
id:99.

Removing a command from the group Id list will disable its use in game the syntax is this:

    <id>
    Unique group number. The only required field.

    <name>
    Any string. If empty, defaults to "Group <id>". It is used in several @who 
    commands.

    <level>
    Equivalent of GM level, which was used in revisions before r15572. You can 
    set it to any number, but usually it's between 0 (default) and 99. Members of 
    groups with lower level can not perform some actions/commands (like @kick) on 
    members of groups with higher level. It is what script command getgmlevel() 
    returns. Group level can also be used to override trade restrictions 
    (db/item_trade.txt).

    <commands>
    A group of settings
    	<command name> : <bool>
    or
    	<commandname> : [ <bool>, <bool> ]
    First boolean value is for atcommand, second one for charcommand. If set to 
    true, group can use command. If only atcommand value is provided, false is 
    assumed for charcommand. If a command name is not included, false is assumed for 
    both atcommand and charcommand.
    For a full list of available commands, see: doc/atcommands.txt.
    Command names must not be aliases.

    <log_commands>
    Boolean value. If true then all commands used by the group will be logged to 
    atcommandlog. If setting is omitted in a group definition, false is assumed.
    Requires 'log_commands' to be enabled in 'conf/log_athena.conf'.

    <permissions>
    A group of settings
    	<permission> : <bool>
    If a permission is not included, false is assumed.
    For a full list of available permissions, see: doc/permissions.txt

    <inherit>
    A list of group names that given group will inherit commands and permissions 
    from. Group names are case-sensitive.

For example, say I want to allow my level 60 GM's to use @baselevel, but I want my level 80 GM's to use the \#baselevel
counterpart to increase another players' base level.

The setting would be set as follows.

    {
       id: 60
       name: "Event Manager"
       inherit: ( "Support" )
       level: 1
       commands: {
           baselevel: [true,false]
       }
       log_commands: true
       permissions: {
           can_trade: false
           any_warp: true
       }
    },

    {
       id: 80
       name: "Law Enforcement"
       inherit: ( "Support" )
       level: 2
       commands: {
           baselevel: [false,true]
       }
       log_commands: true
       permissions: {
           join_chat: true
           kick_chat: true
           hide_session: true
           who_display_aid: true
           hack_info: true
           any_warp: true
           view_hpmeter: true
        }
    },

Notice that the first flag is for @, and the second is for \#.

**NOTE: If a group ID inherits another group ID, and you add the same command under both groups, it will cause
group.conf to act unpredictably. It has been noted that it may cause no groups, to have any atcommands. Including the
admin group.**
