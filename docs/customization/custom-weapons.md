== The ID ==
Why the ID first?  The ID controls what type of weapon sprite is displayed.  Going outside the ID range will cause you to "punch" when attacking.

Open your [`db/re/item_db.conf`](https://github.com/HerculesWS/Hercules/blob/stable/db/re/item_db.conf) or [`db/pre-re/item_db.conf`](https://github.com/HerculesWS/Hercules/blob/stable/db/pre-re/item_db.conf) and find the section with the weapon type you need.  The allowable range is usually obvious.

{| {| class="wikitable" border="1"
!Item ID
!Item Type
|-
|1100-1149, 13400-13499||One-Handed Swords
|-
|1150-1199, 21000-21999||Two-Handed Swords
|-
|1200-1249, 13000-13099||Knives, Daggers, Etc.
|-
|1250-1299||Katars
|-
|1300-1349||One-Handed Axes
|-
|1350-1399||Two-Handed Axes
|-
|1400-1449||One-Handed Spears
|-
|1450-1471, 1474-1499||Two-Handed Spears
|-
|1500-1549, 16000-16999||Maces
|-
|1550-1599||Books
|-
|1600-1699||One Handed Rods/Staves
|-
|1700-1749, 18100-18499||Bows
|-
|1750-1799||Arrows
|-
|1800-1849||Knuckles
|-
|1900-1949||Guitars/Instruments
|-
|1950-1999||Whips
|-
|1472,1473,2000-2099||Two Handed Rods/Staves
|-
|13100-13149||Handgun
|-
|13150-13199||Other Guns
|-
|13300-13399||Ninja Weapons
|}

=== Example ===

To make a custom bow, searching for "Bows" in item_db shows that bow IDs start at 1701 and end at 1749. Since there are no remaining IDs, commenting out an unused bow would work.

Otherwise, skip to the next set of bows, which start at 18101.  Select an open ID in that range.

== The Sprite ==
The client requires a sprite for every job the weapon can be used by.  Some programs can automatically organize the files:
* [http://rathena.org/board/files/file/2494-ra-sprite-name-gen/ clydelion's Sprite Name Generator]<br>
* [http://rathena.org/board/files/file/2386-ea-sprite-name-generator/ Myzter's Sprite Name Generator]

Don't forget to give the weapon an icon in '''/sprite/¾ÆÀÌÅÛ/''', as well as an inventory icon and collection image in '''/texture/À¯ÀúÀÎÅÍÆäÀÌ½º/item/''' and '''/texture/À¯ÀúÀÎÅÍÆäÀÌ½º/collection/'''.

== Other Client Data ==
Lastly, the client data tables need to be filled out:

*'''idnum2itemdesctable.txt''': Identified item description.
*'''idnum2itemdisplaynametable.txt''': Identified item display name.
*'''idnum2itemresnametable.txt''': Identified sprite name.
*'''itemslotcounttable.txt''': Number of weapon slots, if necessary (skip if 0).
*'''num2itemdesctable.txt''': Unidentified item description, if necessary.
*'''num2itemdisplaynametable.txt''': Unidentified item display name, if necessary.
*'''num2itemresnametable.txt''': Unidentified sprite name, if necessary.

''And... you are done!''

== Troubleshooting ==
'''Q: Weapon is an Unknown Item.'''

A: An error in resnametable. The client is not reading any value, so it becomes unknown.

'''Q: The weapon sprite shows fine when standing, turns to punches when attacking.'''

A: The ID for the weapon isn't in the allowed range.  Make sure the value is correct.

'''Q: The weapon sprite doesn't show at all.'''

A: Re-check file/folder names and placement.

==Weapon Sprite Solution (Renewal Clients <= 2012-04-10a & Main Clients <= 2012-07-10a)==
For these clients, Weapons are limited to use a range of Item IDs hardcoded in the clientn for each type.
For e.g.

 1265,Bloody_Roar,Bloody Roar,4,,10,1000,120,,1,0,4096,7,2,34,4,75,1,16,{ bonus bIgnoreDefRace,RC_DemiHuman; bonus bFlee,-160; bonus bFlee2,-160; bonus bNoRegen,1; bonus bNoRegen,2; },{},{}
 1266,Test,Test,4,4000,2000,10,165,,1,0,4096,7,2,34,3,33,1,16,{}

 // 1-Handed Axes
 1301,Axe,Axe,4,500,,800,38,,1,3,8803555,7,2,2,1,3,1,6,{}

Here the item 1266 is a custom katar and it does show up as a katar (if you have the proper sprite files ofcourse). but if i use some id like say 22000, client wont display it. So what is the range of item ids you can use? Look below:

* One handed Swords = 1100-1149, 13400-13499
* Two handed Swords = 1150-1199, 21000-21999
 
* Knives, Daggers etc = 1200-1249, 13000-13099
* Katars = 1250-1299 ; Has 35 free IDs
 
* One handed Axes = 1300-1349; Has 43 free IDs
* Two handed Axes = 1350-1399; Has 32 free IDs
 
* One handed Spears = 1400-1449; Has 34 free IDs
* Two Handed Spears = 1450-1471, 1474-1499
 
* Maces = 1500-1549, 16000-16999
* Books = 1550-1599 ; Has only 2 IDs.
* Knuckles = 1800-1899 ; Has 95 free IDs
 
* One Handed Staves/Rods = 1600-1699; Has 79 free IDs
* Two Handed Staves/Rods = 1472,1473,2000-2099
 
* Bows = 1700-1749, 18100-18499
* Guitars = 1900-1949 ; Has 32 free IDs
* Whips = 1950-1999 ; Has 130 free IDs
 
* Handguns = 13100-13149
* Other guns = 13150-13199
 
* Ninja weapons = 13300-13399

The number of unused Item IDs left known for a range has also been mentioned above. Best practice to follow check in your range in official db before adding custom weapon.

==Weapon Sprite Solution (For New Clients) ==
For new clients the view id system is also applicable to client. To add a custom weapon you need to first edit a file
called weapontable.lub in your data folder
 data/luafiles514/lua files/datainfo/weapontable.lub

I will be adding <b>Oriental_Sword</b> which will be a 1-Handed sword. Open weapontable.lub.
First you will see a table called <b>Weapon_IDs</b>. Take note of the first 30 values in this table - these are the only available Weapon types in the client right now.

Anyways go to the last entry which should be for Wizardy Staff = 97. You can use a view id after that like shown below
  WEAPONTYPE_Oriental_Sword = 98,
*Attention: The last lines usually don't has the ","
 e.g: 
 WEAPONTYPE_Oriental_Sword = 98,
 WEAPONTYPE_Western_Sword = 99

Come down and you see the next table called <b>WeaponNameTable</b>. Here is where you add your sprite name suffix.<br>
What do i mean by that? Its the last part in your weapon sprite & act file. Before it used to be _<Item ID>.
 data/sprite/<job dependent folder>/<job dependent prefix>_<gender><weapon suffix>.spr

OK Back to topic. so I add my entry like shown below.
 [Weapon_IDs.WEAPONTYPE_Oriental_Sword] = "_Oriental"

Lastly come down further in weapontable.lub and you see the last table called <b>Expansion_Weapon_IDs</b>.<br>
Remember the 30 types i told you to take note of ? here we assign one of those to our custom (like a mapping or connection).<br>
Since mine is a 1-Handed Sword I specify it like below.
 [Weapon_IDs.WEAPONTYPE_Oriental_Sword] = Weapon_IDs.WPCLASS_WEAPONTYPE_SWORD 

<b>Now for the most important part. For our client to actually pick up all these details we need to provide the view id which we used in Weapon_IDs table as the ClassNum value in ItemInfo.lua. Check the [[Custom_Items#System.2FItemInfo.lub|ItemInfo.lub format]] shown above for details.</b>

With this your weapon sprite will become visible while attacking.

[[Category:Customization]]
