
[[Category:incomplete]]
== Map Flags are used to set serval permissions on maps. ==
<br /><br /><br />

# Battleground
# GvG
# Nightenabled
# Nightmare
# Nobranch
# Noexp
# Noicewall
# Noloot
# Nomemo
# Nopenalty
# Nopvp
# Noreturn
# Nosave
# Noskill
# Noteleport
# Novending
# Nowarp
# Nowarpto
# Partylock
# Pvp
# Pvpnoguild
# Pvpnoparty
# Reset
# Skillduration
# Skillmodifier
# Town
# Zone





Battleground<br />
 '''Description:''' Defines the Map as Battleground.<br />
 '''File:''' npc/mapflag/battleground.txt<br />
 '''Parameter:''' 2 ( Activate Scoreboard )<br />

<code> usage: <map> mapflag battleground <parameter(Optional)></code><br />
<br /><br />
Gvg <br />
 '''Description:''' Defines the Map as Guild Vs. Guild Map, so Guilds can Fight each other.<br />
 '''File:''' npc/mapflag/gvg.txt<br />
 '''Parameter:''' <none><br />

<code> usage: <map> mapflag gvg</code><br /> 
 
<br /><br />
Nightenabled <br />
 '''Description:''' Nightmode Effects on defined Maps.<br />
 '''File:''' npc/mapflag/night.txt <br />
 '''Parameter:''' <none><br />

<code> usage: <map> mapflag nightenabled</code><br />
<br /><br />


Nightmare <br />
 '''Description:''' Drops Player Items or Equipments on player death.<br />
 '''File:''' npc/mapflag/nightmare.txt<br />
 '''ID:''' ItemID,random<br />
 '''Type:''' inventory, equip, all<br />
 '''Percent:''' Droprate<br />

<code> usage: <map> mapflag pvpnightmaredrop <id>,<type>,<percent></code><br />

<br /><br />
Nobranch<br />
 '''Description:''' Disables Dead Branch / Bloody Brunch / Red Brunch and Porinx Box.<br />
 '''File:''' npc/mapflag/nobranch.txt<br />
 '''Parameter:''' <none><br />

<code> usage: <map> mapflag nobranch
</code><br /><br /><br />


Noexp<br />
 '''Description:''' Disable Exp gain for Players.<br />
 '''File:'''npc/mapflag/noexp.php<br />
 '''Parameter:''' <none><br />

<code> usage: <map> mapflag noexp</code><br />
<br /><br />


Noicewall<br />
 '''Description:''' Disable Icewall on a Map.<br />
 '''File:''' npc/mapflag/noicewall.txt<br />
 '''Parameter:'''<br />

<code> usage: <map> mapflag noicewall</code><br />
<br /><br />

Noloot<br />
 '''Description:''' Disable loot on a Map.<br />
 '''File:''' npc/mapflag/noloot.txt<br />
 '''Parameter:''' <map> mapflag noloot<br />

<code> usage: <map> mapflag noloot</code><br />
<br /><br />


Nomemo<br />
 '''Description:''' Disable /memo on a Map<br />
 '''File:''' npc/mapflag/nomemo.txt<br />
 '''Parameter:''' <none><br />

<code> usage: <map> mapflag nomemo</code><br />

<br /><br />
Nopenalty<br />
 '''Description:''' Disable death penalty.<br />
 '''File:''' npc/mapflag/nopenalty.txt<br />
 '''Parameter:''' <none><br />

<code> usage: <map> mapflag nopenalty</code><br />
<br /><br />


Nopvp<br />
 '''Description:''' Disable PvP (Player vs. Player) on a Map<br />
 '''File:''' npc/mapflag/nopvp.txt<br />
 '''Parameter:''' off<br />

<code> usage: <map> mapflag pvp <parameter></code><br />
<br /><br />

Noreturn<br />
 '''Description:''' Disables the Return Warp.<br />
 '''File:''' npc/mapflag/noreturn.php<br />
 '''Parameter:''' <none><br />

<code> usage: <map> mapflag noreturn</code><br />
<br /><br />

Nosave<br />
 '''Description:''' Disables Autosave on a Map, if the Parameter isnt defined, Warp to the last field.<br />
 '''File:''' npc/mapflag/nosave.txt<br />
 '''Parameter:''' SavePoint<br />

<code> usage: <map> mapflag nosave <parameter(Optional)></code><br />
<br /><br />

Noskill<br />
 '''Description:''' Disable Skills<br />
 '''File:''' npc/mapflag/noskill.txt<br />
 '''Parameter:''' <none><br />

<code> usage: <map> mapflag noskill</code><br />
<br /><br />


Noteleport<br />
 '''Description:''' Disable all kinds of Teleport.<br />
 '''File:''' npc/mapflag/noteleport.txt<br />
 '''Parameter:''' <none><br />

<code> usage: <map> mapflag noteleport</code><br />
<br /><br />

Novending<br />
 '''Description:''' Disable Vending<br />
 '''File:''' npc/mapflag/novending.txt<br />
 '''Parameter:''' <none><br />

<code> usage: <map> mapflag novending</code><br />
<br /><br />

Nowarp<br />
 '''Description:''' Disable @GO<br />
 '''File:''' npc/mapflag/nowarp.txt<br />
 '''Parameter:''' <none><br />

<code> usage: <map> mapflag nowarp</code><br />
<br /><br />

Nowarpto<br />
 '''Description:''' Disable Warp to<br />
 '''File:''' npc/mapflag/nowarpto.txt<br />
 '''Parameter:''' <none><br />

<code> usage: <map> mapflag nowarpto</code><br />
<br /><br />

Partylock<br />
 '''Description:''' Disables Party modifications<br />
 '''File:''' npc/mapflag/partylock.txt<br />
 '''Parameter:''' <none><br />

<code> usage: <map> mapflag partylock</code><br />
<br /><br />

Pvp<br />
 '''Description:''' Defines the Map as Player vs Player Map<br />
 '''File:''' npc/mapflag/pvp.txt<br />
 '''Parameter:''' <none><br />

<code> usage: <map> mapflag pvp</code><br />
<br /><br />

Pvpnoguild<br />
 '''Description:''' Ignore Aliances on Guild vs Guild Maps<br />
 '''File:''' npc/mapflag/pvpnoguild.txt<br />
 '''Parameter:''' <none><br />

<code> usage: <map> mapflag pvpnoguild </code><br />
<br /><br />

Pvpnoparty<br />
 '''Description:''' Ignore Party on Player vs Player Maps<br />
 '''File:''' npc/mapflag/pvpnoparty.txt<br />
 '''Parameter:''' <none><br />

<code> usage: <map> mapflag pvpnoparty</code><br />
<br /><br />

Reset<br />
 '''Description:''' Disable Neuralizer Item(12213) usage<br />
 '''File:''' npc/mapflag/reset.txt<br />
 '''Parameter:''' <none><br />

<code> usage: <map> mapflag reset</code><br />
<br /><br />

Skillduration<br />
 '''Description:''' Set Duration for a Skill on a Map<br />
 '''File:''' npc/mapflag/skillduration.txt<br />
 '''Parameter:''' 0-...(?) <br />

<code> usage: <map> mapflag skillduration <parameter></code><br />
<br /><br />

Skillmodifier<br />
 '''Description:''' Set the Damage for a Skill on a Map<br />
 '''File:''' npc/mapflag/skillmodifier.txt<br />
 '''Parameter:'''0-...(?)<br />

<code> usage: <map> mapflag skillmodifier <parameter></code><br />
<br /><br />

Town<br />
 '''Description:''' Defines a Map as a Town.<br />
 '''File:''' npc/mapflag/town.txt<br />
 '''Parameter:''' <none><br />

<code> usage: <map> mapflag town</code><br />
<br /><br />

Zone<br />
 '''Description:''' Flags maps as part of zones<br />
 '''File:''' npc/mapflag/zone.txt<br />
 '''Parameter:''' see mapzonedb.txt<br />

<code> usage: (?)	mapflag	zone	Aldebaran Turbo Track (?)</code><br />
<br /><br />
