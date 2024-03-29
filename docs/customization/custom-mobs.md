= Intro =
You can have up to 10,000 mob IDs. This guide was written without testing on Git; use at your own discretion.
Well, its pretty easy if you do it correctly and go step by step without rushing.

= Gettings Started =
== Database Structure ==
Let's take a look at the structure of the entries in mob_db.conf:

Note: If you're adding custom mobs, it's better to add them to mob_db2.conf

<pre>
{
	// =================== Mandatory fields ===============================
	Id: ID                                (int)
	SpriteName: "SPRITE_NAME"             (string)
	Name: "Mob name"                      (string)
	// =================== Optional fields ================================
	Lv: level                             (int, defaults to 1)
	Hp: health                            (int, defaults to 1)
	Sp: mana                              (int, defaults to 0)
	Exp: basic experience                 (int, defaults to 0)
	JExp: job experience                  (int, defaults to 0)
	AttackRange: attack range             (int, defaults to 1)
	Attack: [attack1, attack2]            (int, defaults to 0)
	Def: defence                          (int, defaults to 0)
	Mdef: magic defence                   (int, defaults to 0)
	Stats: {
		Str: strength                 (int, defaults to 0)
		Agi: agility                  (int, defaults to 0)
		Vit: vitality                 (int, defaults to 0)
		Int: intelligence             (int, defaults to 0)
		Dex: dexterity                (int, defaults to 0)
		Luk: luck                     (int, defaults to 0)
	}
	ViewRange: view range                 (int, defaults to 1)
	ChaseRange: chase range               (int, defaults to 1)
	Size: size                            (int, defaults to 1)
	Race: race                            (int, defaults to 0)
	Element: (type, level)
	Mode: {
		CanMove: true/false           (bool)
		Looter: true/false            (bool)
		Aggressive: true/false        (bool)
		Assist: true/false            (bool)
		CastSensorIdle:true/false     (bool)
		Boss: true/false              (bool)
		Plant: true/false             (bool)
		CanAttack: true/false         (bool)
		Detector: true/false          (bool)
		CastSensorChase: true/false   (bool)
		ChangeChase: true/false       (bool)
		Angry: true/false             (bool)
		ChangeTargetMelee: true/false (bool)
		ChangeTargetChase: true/false (bool)
		TargetWeak: true/false        (bool)
	}
	MoveSpeed: move speed                 (int, defaults to 0)
	AttackDelay: attack delay             (int, defaults to 4000)
	AttackMotion: attack motion           (int, defaults to 2000)
	DamageMotion: damage motion           (int, defaults to 0)
	MvpExp: mvp experience                (int, defaults to 0)
	MvpDrops: {
		AegisName: chance             (string: int)
		...
	}
	Drops: {
		AegisName: chance         (string: int)
		...
	}

},
</pre>

{| class="wikitable"
|-
! Fields !! Description
|-
| '''<u>Id</u>''' || ID of the mob
|-
| '''<u>SpriteName</u>''' || This first name is the DB name. When you use @spawn/@summon and you know the name of the mob, but not the ID, type this name instead. Try making the normal name the same as this so you wont get confused.
|-
| '''<u>Name</u>''' || This is the name the server shows.
|-
| '''<u>Lv</u>''' || Level of the mob
|-
| '''<u>Hp</u>''' || HP of the mob
|-
| '''<u>Sp</u>''' || SP of the mob
|-
| '''<u>Exp</u>''' || Exp granted by the mob
|-
| '''<u>JExp</u>''' || Job exp granted by the mob
|-
| '''<u>AttackRange</u>''' || Range of the mob attack. If set to 1 or 2, it will melee. 3 or more than 3 will set it to ranged
|-
| '''<u>Attack1</u>''' ||  Affects ATK of the mob
|-
| '''<u>Attack2</u>''' || Affects MATK of the mob
|-
| '''<u>Def</u>''' || Defense of the mob (Tip: 100 def = Invulnerability below 8K attack. Watch out, only melee/ranged attacks, but generally direct hits attacks are drastically reduced. Setting this high enough may make monks pretty cheap to level because of of Psychic Wave/Occult Impact/Investigate.)
|-
| '''<u>MDef</u>''' || Magic Defense of the mob (Hint: 100 mdef = golden thief bug effect below 9K magic attack. It's for all magic-using skills.)
|-
| '''<u>Stats</u>''' || All Stats of mobs belongs to this block.
{| class="wikitable"
|-
! Stats !! Description
|-
| '''<u>Str</u>''' || Strength of the mob. This also affects its ATK.
|-
| '''<u>Agi</u>''' || Agility of the mob. This also affects the mob flee rate.
|-
| '''<u>Vit</u>''' || Vitality of the mob. This affects the duration of stun status.
|-
| '''<u>Int</u>''' || Intelligence of the mob. This also affects its MATK.
|-
| '''<u>Dex</u>''' || Dexterity of the mob. This also affects the mob hit rate.
|-
| '''<u>Luk</u>''' || Luck of the mob. This also defines the mob perfect dodge/lucky flee/perfect flee/lucky dodge rate.
|}
|-
| '''<u>ViewRange</u>''' || Maximum Skill Range
|-
| '''<u>ChaseRange</u>''' || Sight limit for mobs. If set to 1000 or beyond, mobs will follow you all over the map.
|-
| '''<u>Size</u>''' ||
{| class="wikitable"
|-
| 0 || Small || Size_Small
|-
| 1 || Medium || Size_Medium
|-
| 2 || Large || Size_Large
|}
|-
| '''<u>Race</u>''' ||
{| class="wikitable"
|-
| 0 || formless || RC_Formless
|-
| 1 || undead || RC_Undead
|-
| 2 || animal || RC_Brute
|-
| 3 || plant || RC_Plant
|-
| 4 || insect || RC_Insect
|-
| 5 || fish || RC_Fish
|-
| 6 || demon || RC_Demon
|-
| 7 || demihuman || RC_DemiHuman
|-
| 8 || angel || RC_Angel
|-
| 9 || dragon || RC_Dragon
|}

|-
| '''<u>Element</u>''' || This is a two-digit number representing the rank (level) and element of the mob.<br />
|-
| '''<u>Element(Type)</u>''' || Element Type of mob as mentioned below.<br />
{| class="wikitable"
| 0 || Ele_Neutral
|-
| 1 || Ele_Water
|-
| 2 || Ele_Earth
|-
| 3 || Ele_Fire
|-
| 4 || Ele_Wind
|-
| 5 || Ele_Poison
|-
| 6 || Ele_Holy
|-
| 7 || Ele_Dark
|-
| 8 || Ele_Ghost
|-
| 9 || Ele_Undead
|}



|-
| '''<u>Element(Level)</u>''' || Element level of mob from (1-4).<br />
|-
| '''<u>Mode</u>''' || This defines the mob behaves.
|-
| '''<u>MoveSpeed</u>''' || Walking speed of the mob. 1 is the fastest, 1000 is the lowest. 100 is the normal walking speed.
|-
| '''<u>AttackDelay</u>''' || ADelay= Attack Delay, also known as ASPD. This one will change the aspd of the mob. The lower the faster, but don't make it too low or it will lag when mobbed by several of these.
|-
| '''<u>AttackMotion</u>''' || Attack animation motion. Lower this value and the mob's attack will be displayed in higher fps (making it shorter, too) (Thanks to Wallex for this)
|-
| '''<u>DamageMotion</u>''' || Damage animation motion, same as aMotion but used to display the "I am hit" animation. Coincidentally, this same value is used to determine how long it is before the mob/player can move again. Endure is dMotion = 0, obviously.
|-
| '''<u>MvpExp</u>''' || The MVP exp the mob gives when it is defeated (to the player who got the MVP reward) (This exp is a percentage of the exp the monster gives.)
|-
The following fields are for drops and drop rates. Remember that these are in percentages; i.e. 100 = 100%
|-
| '''<u>MvpDrops</u>''' || The MvP Drops goes here, format is:
<pre>AegisName: Chance</pre>
Example:
<pre>Poring_Card: 1000</pre>
|-
| '''<u>Drops</u>''' || The Normal Drops goes here, format is:
<pre>AegisName: Chance</pre>
Example:
<pre>Poring_Card: 1000</pre>
|}

== Making it visible ==
=== Server Side ===
If you've got a sprite and you're happy with it, then you can skip this part. If you would like to make your mob look like another mob, or even a player, then you need to take a look at [`db/mob_avail.txt`](https://github.com/HerculesWS/Hercules/blob/stable/conf/mob_avail.txt)

For normal mobs, you can use the data that's already in the file as an example to work on:
 // mob_id,sprite_id,equip #
 // iRO Halloween Event 2008
 //3000,1015,0
 //3001,1036,0
 //3002,1298,0
 
 // iRO Halloween Event 2009
 //3014,1179,0
 //3015,1272,0


However, if you would like to make your mob look like a character, you need to add more options:<br />
// Valaris
{| class="wikitable"
|-
| MobID || SpriteID || Sex || Hair || Hair_Color || Weapon || Shield || Head_Top || Head_Middle || Head_Bottom || Option || Dye_Color
|-
| 1900, || 4013, || 1, || 1, || 1, || 1254, || 0, || 67, || 12, || 54, || 16, || 1
|}
You will need to use the Item ID for your mob's weapon and shield instead of the View ID of the item. Doing so may have undesirable effects.

A more in-depth look at each value:<br />
<br>'''<u>MobID</u>''': This is your mob ID.
<br>'''<u>SpriteID</u>''': The Job number you want it to look like. They are:
<pre>Job_Novice 0
Job_Swordman 1
Job_Mage 2
Job_Archer 3
Job_Acolyte 4
Job_Merchant 5
Job_Thief 6
Job_Knight 7
Job_Priest 8
Job_Wizard 9
Job_Blacksmith 10
etc</pre>
They can also be found on [`db/const.txt`](https://github.com/HerculesWS/Hercules/blob/stable/db/const.txt) file.

<br>'''<u>Sex</u>''': 0 for female, 1 for male
<br>'''<u>Hair</u>''': The mob hair style, goes from 1 to 23
<br>'''<u>Hair_Color</u>''': The mob hair color. Goes from 0 to 8 or 10, but it depends on the server's palette files.
<br>'''<u>Weapon</u>''':The ID of the Weapon you want. See [[Custom_weapons|Custom Weapons]] for it. Also read at the end of the pre if you cant find the headgear you want. 
<br>'''<u>Shield</u>''': Same as above
<br>'''<u>Head_Top</u>''': Same as above
<br>'''<u>Head_Middle</u>''': Same as above
<br>'''<u>Head_Bottom</u>''': Same as above
<br>'''<u>Option</u>''': this option parameter will make the mob change its status, as well as give them carts, pecopecos, and falcons. In other words, this will change the visual effects of your mobs. The options are these*:
<pre>
 1 Sight             32 Peco Peco riding   2048 Orc Head
 2 Hide              64 GM Perfect Hide    4096 Wedding Sprites
 4 Cloak            128 Level 2 Cart       8192 Ruwach
 8 Level 1 Cart     256 Level 3 Cart
16 Falcon           512 Level 4 Cart
                   1024 Level 5 Cart
</pre>

<br>'''<u>Dye_Color</u>''': Same as hair color. It goes from 0 to 77


=== Client Side ===
For your mob to exist in the client, you need to add it to a few [[Lua]] files.
==== datainfo/npcidentity.lua ====
Example at the end of the file:<br />
 	["JT_4_F_TAEKWON"] = 644,
 	["JT_4_F_SWORDMAN"] = 645,
 	-- Custom Mobs
 	["JT_JACOB"] = 2500,
 	["JT_AQUARING"] = 2600
 }
The number after the = sign denotes the mob's database ID number. Other sprites in this file have their view ID e.g. [[Adding_a_Script#Client_Side|NPC sprite number]].

==== datainfo/jobname.lua ====
Example at the end of the file:<br />
 	[jobtbl.JT_GIBBET] = "GIBBET",
 	[jobtbl.JT_DULLAHAN] = "DULLAHAN",
 	[jobtbl.JT_LOLI_RURI] = "LOLI_RURI",
 	[jobtbl.JT_DISGUISE] = "DISGUISE",
 	-- Custom Mobs
 	[jobtbl.JT_JACOB] = "jacobmob",
 	[jobtbl.JT_AQUARING] = "aquaring"
 }
In this file, the value after the = sign is the name of the actual sprite in your data folder/[[GRF]]


== Your mob in other files ==
=== Dead Branch ===
Adding your mob to [`db/pre-re/mob_branch.txt`](https://github.com/HerculesWS/Hercules/blob/stable/db/pre-re/mob_branch.txt) or [`db/re/mob_branch.txt`](https://github.com/HerculesWS/Hercules/blob/stable/db/re/mob_branch.txt) will allow Dead Branches to summon it.

=== Bloody Branch ===
Adding your mob to [`db/pre-re/mob_boss.txt`](https://github.com/HerculesWS/Hercules/blob/stable/db/pre-re/mob_boss.txt) or [`db/re/mob_boss.txt`](https://github.com/HerculesWS/Hercules/blob/stable/db/re/mob_boss.txt) will allow Bloody Branches to summon it.

=== Poring Box ===
Adding your mob to [`db/pre-re/mob_poring.txt`](https://github.com/HerculesWS/Hercules/blob/stable/db/pre-re/mob_poring.txt) or [`db/re/mob_poring.txt`](https://github.com/HerculesWS/Hercules/blob/stable/db/re/mob_poring.txt) will make your mob spawnable via the Poring Box.

=== Monster Racial Groups ===
Adding your mob to [`db/pre-re/mob_race2_db.txt`](https://github.com/HerculesWS/Hercules/blob/stable/db/pre-re/mob_race2_db.txt) or [`db/re/mob_race2_db.txt`](https://github.com/HerculesWS/Hercules/blob/stable/db/re/mob_race2_db.txt) will add your mob to a [[Racial_Group|Racial Group]]. Guardians, Goblins and other mobs are members of particular Racial Groups.

=== Red Pouch of Surprise ===
Adding your mob to [`db/mob_pouch.txt`](https://github.com/HerculesWS/Hercules/blob/stable/db/mob_pouch.txt) will make your mob spawnable via the Red Pouch of Surprise.


== Spawn Points ==
Let's look at the syntax of a mob spawn point:

<pre>
<map name>,<x1>,<y1>,<x2>,<y2>%TAB%monster%TAB%<monster name>%TAB%<mob id>,<amount>,<delay1>,<delay2>,<event>{,<mob size>,<mob ai>}
</pre>

Only the things between <> are changed. Do not remove or change monster after the coordinates, because that's what tells the server that this line is a monster spawn script.

<br>'''<u>map name</u>''': Name of the map. Use /where along with the following coordinates
<br>'''<u>x1</u>''': X axis coordinates. It start from the left side of the map, and the higher it gets, the more it gets closer to the right side of the map.
<br>'''<u>y1</u>''': Y axis coordinates. It start from the bottom, and the higher it gets, the more it gets closer to the top of the map.
<br>'''<u>x2</u>''': X axis coordinates. It start from the left side of the map, and the higher it gets, the more it gets closer to the right side of the map.
<br>'''<u>y2</u>''': Y axis coordinates. It start from the bottom, and the higher it gets, the more it gets closer to the top of the map.
<br>These 4 coordinates will make a spawn area where the mob will spawn, however it won't limit its movement, so lets say you put 120,150 on the first pair, and 130,160 pair- That's a 10x10 cell area where the mob will spawn randomly.
<br>If you want the mob to spawn at a random point, use 0 for all the coordinates.
<br>'''<u>monster name</u>''': The name of the mob you want to be shown (using --ja-- in place of a name will display the "Japanese Name" from your database).
<br>You can specify a custom level to use for the mob different from the one of the database by adjoining the level after the name with a comma. eg: "Poring,50" for a name will spawn a monster with name Poring and level 50.
<br>'''<u>mob id</u>''': The ID of your mob.
<br>'''<u>amount</u>''': How many mobs you want to be spawned.
<br>'''<u>delay1</u>''': Minimum amount of time before a monster respawns.
<br>'''<u>delay2</u>''': Maximum amount of time before a monster respawns.
<br>delay1 and delay2 are used to define the time it takes for a monster to respawn; in milliseconds. Normal mobs usually have 0 (Instant Respawn), while MVPs have 7200000 (2 hours). If delay2 is greater than delay 1, the mob won't respawn until the map server restarts.
<br>'''<u>event</u>''': Script event to be executed when the mob is killed. The event must be in the form "NPCName::OnEventName" to execute, and the event name label should start with "On". As with all events, if the NPC is an on-touch NPC, the player who triggers the script must be within 'trigger' range for the event to work.
<br>'''<u>size</u>''': Optional. Size can be 0 (medium), 1 (small), or 2 (big).
<br>'''<u>ai</u>''': Optional. AI can be 0 (default), 1 (attack/friendly), 2 (sphere), 3 (flora), or 4 (zanzou).

== Adding Skills ==

Lets look at the syntax of a mob skill:

<pre>
MOB_ID, a unused dummy character sequence (for information only), STATE, SKILL_ID, SKILL_LV,
rate (10000 = 100%), casttime, delay, cancelable, a target, a condition type, a condition value,
a value 1, a value 2, a value 3, a value 4, a value 5, emotion
</pre>

<br>'''''
NOTE: I had to cut the mob_avail structure so it could fit.
It's a whole line, not 3 lines.
'''''

<br>'''<u>MOD_ID</u>''': your mob ID.
<br>'''<u>an unused.. etc etc</u>''': you can put any text here you want, its just for information and to know what does this do.* tip tip*You will see inside this file things like Poring@TF_POISON. Well, you could use this too. It would tell you: mob_name@DB_Skill_Name. *tip tip*
<br>'''<u>state</u>''': this is the state that the mob must accomplish before being able to use this skill. The states are:

<pre>
any, idle (in standby), walk (in movement), attack, dead (on killed), loot, chase (following target),
counterattack.
</pre>

<br>'''<u>SKILL_ID</u>''': The ID of the skill goes here. To look for one, go to your db folder and open the skill_db.txt file. You will see a lot of lines like this one:

<pre>2,0,0,0,0,0,10,0,no,0,0,0,weapon,0 //SM_SWORD#Œ•C—û#</pre>

And the syntax is:

<pre>
id,range,hit,inf,pl,nk,max,list_num,castcancel,cast_defence_rate,inf2,maxcount,skill_type,blow_count
</pre>

so, the ID of the SM_SWORD, which is the Swordman's Sword Mastery by the way, is 2:

<pre>'''2''',0,0,0,0,0,10,0,no,0,0,0,weapon,0 //SM_SWORD#Œ•C—û#</pre>

<br>'''<u>SKILL_LV</u>''': You can put the skill level as high as you want. Though, 100 is usually as far as most skills go.
<br>'''<u>rate</u>''': How frequent will the mob use the skill.
<br>'''<u>casttime</u>''': Skill's cast time.
<br>'''<u>delay</u>''': How much time must pass before the skill can be used again, in milliseconds.
<br>'''<u>cancelable</u>''': if the skill cast can be interrupted. Set it either '''yes''' or '''no'''.
<br>'''<u>a target</u>''': the target of the skill. It can be:
<pre>
target (player), self (the mob itself), friend (slaves)
</pre>

<br>'''<u>a condition type</u>''':a condition that also must be fulfilled before the mob is able to use this skill. There are two kinds of conditions:

1. Mob Condition:
<pre>//conditions: (condition type) (value which specifies a condition value)
// always            unconditional
// myhpltmaxrate     when the mob's hp drops to a certain %
// mystatuson        If the mob has any abnormalities in status (condition value),
// mystatusoff       If the mob has ended any abnormalities in status (condition value),
// friendhpltmaxrate when the mobs' friend's hp drops to a certain %
// friendstatuson    If the friend has any abnormalities in status (condition value),
// friendstatusoff   If the friend has ended any abnormalities in status (condition value),
// attackpcgt        Attack PC becomes more than the  number of specification
// attackpcge        Attack PC becomes equal or more than the number of specification.
// slavelt           when the number of slaves is lower than the original number of specification.
// slavele           when the number of slaves is lower or equal than the original number of specification.
// closedattacked    when melee attacked (close range attack)
// longrangeattacked when long ranged attacked (like bows and far range weapons)
// skillused         when a skill is used on the mob
// casttargeted      when a target is in cast range.
// rudeattacked      when a target is rude attacked
// hiding            when a target is hidden *not implemented yet*
</pre>


2. Target Conditions
<pre>
// The character's state which can be specified to be a condition value
// by the statuson/statusoff system
//
// anybad      any type of state change
// stone       condition of being in stone state
// freeze      condition of being in frozen state
// stan        condition of being in stunned state
// sleep       condition of being in sleep state
// poison      condition of being in poisoned state
// curse       condition of being in cursed state
// silence     condition of being in silenced state
// confusion   condition of being in confusion state
// blind       condition of being in blind state
// hiding      condition of being in hidden state
// sight       condition of being in unhidden state
</pre>

You can use only ONE of these conditions.

<br>'''<u>value1,value2,value3,value4,value5</u>''': Basically they're only the same but, when you want your mob using the same condition to trigger the skill, but in different times, in case of the myhpltmaxrate when the hp is being decreased, you can set them in a decreasing order, like:

<pre>80,60,40,20,10</pre>

<br>'''<u>emotion</u>''': Lets your mob use an emotion, at random times. The emotion IDs are:

<pre>
e_gasp 0
e_what 1
e_ho 2
e_lv 3
e_swt 4
e_ic 5
etc
</pre>

For more info, go to your [`db/const.txt`](https://github.com/HerculesWS/Hercules/blob/stable/db/const.txt) file.

== Making it talk! ==
Another add, suggested by chronocrosser_x and Fenrir Soarblade:

Well, I believe you have seen some mobs on your server talking when certain things happens. I never saw them again talking, dont know why but they used to talk. I believe they still do it.

Ok, go to your Data folder. If you look in the files, you should find a file called monstertalktable. If there isnt, we will create one with Wordpad =3!. If there is, open it with Wordpad, not Notepad.

Once there, we will copy and paste this:

<pre><nowiki><?xml version="1.0" encoding="euc-kr" ?>   

<enemy_monster_talk_table>   

<mob_db_name_here> 
  <discovery></discovery>
  <attack></attack>
  <hp50></hp50>
  <hp25></hp25>
  <kill></kill>
  <dead></dead>
</mob_db_name_here> 
</enemy_monster_talk_table></nowiki></pre>

Well, lets see step by step =3!:

<br>'''<u><enemy_monster_talk_table></u>''': This is the start of the monster talk table. Leave it as it is =3!
<br>'''<u><mob_db_name_here></u>''': The mob_db.txt first name you see, after the ID, goes here =3! Its used to identify the mob
<br>'''<u><discovery>%TAB%Text Here%TAB%</discovery></u>''': This is an event, same as the one below. When a monster see you, this one will be displayed =3!
<br>'''<u><attack>%TAB%Text Here%TAB%</attack></u>''': When a monster attacks you, this one will be displayed O_O!
<br>'''<u><hp50>%TAB%Text Here%TAB%</hp50></u>''': When a monster's hp is at 50%, this one will be displayed o..o!
<br>'''<u><hp25>%TAB%Text Here%TAB%</hp25></u>''': When a monster's hp is at 25%, this one will be displayed x,x
<br>'''<u><kill>%TAB%Text Here%TAB%</kill></u>''': When a monster kills a character/player, this one will be displayed T~T!
<br>'''<u><dead>%TAB%Text Here%TAB%</dead></u>''': When a monster dies by player hand, this one will be displayed ^__^!
<br>'''<u></mob_db_name_here></u>''': The same name of the mob_db.txt, the one after the ID.
<br>'''<u></enemy_monster_talk_table></u>''': Keep it like this.

I never messed with this, but i think its ok =3! Also for those spaces other than the messages spaces, use TAB, not the Space Bar for it ._.!

[[Category:Database]]
[[Category:Data]]
[[Category:Customization]]
