# `mmo.h`

!!! warning
	This page may contain outdated information, incompatible with the current version of Hercules and its coding standards.

\[\`src/common/mmo.h\`\](https://github.com/HerculesWS/Hercules/blob/stable/src/common/mmo.h) This source file holds
global declarations and hard-coded settings, that are used by the login, char and map server. If you modify anything,
you have to recompile all three servers, otherwise you may run into errors.

### PACKETVER

Specifies the packet version to use for server-client communication. It must be set to date, your client has been
released at, e. g. 20090922 for 2009-09-22aRagexeRE. Note: If you have a client, that is newer, than the latest packet
version in the comment, some things might not work properly, if the client packets have changed since then.

### ENABLE_SC_SAVING

If you disable this define, all status changes get discarded upon logout.

### HOTKEY_SAVING

When enabled, the server stores client hotkeys. While older clients save them locally in the registry, newer clients
require this define to be enabled.

### MAX_MAP_PER_SERVER

Sets how many maps a single map server may manage. This also includes instanced maps.

### MAX_INVENTORY

Sets maximum amount of item slots in the character item inventory. If you set this above 127, some scripts, that
enumerate characters' inventory will break.

### MAX_CHARS

Max number of characters per account. Note, that changing this setting alone is not enough if the client is not hexed to
support more characters as well.

### GLOBAL_REG_NUM

Max number of permanent [char variables](Variables#Player_Variables "wikilink").

### ACCOUNT_REG_NUM

Max number of permanent [account variables](Variables#Account_Variables "wikilink").

### ACCOUNT_REG_NUM2

Max number of permanent [global account variables](Variables#Global_Account_Variables "wikilink").

### MAX_QUEST_DB

Maximum number of Quest database to be loaded. File is located in db/questdb.txt note: if you have too many quests, your
map server will show errors that there's too many quest db. remember to recompile your server if you do!

[Category:Incomplete](Category:Incomplete "wikilink") [Category:Configuration](Category:Configuration "wikilink")
