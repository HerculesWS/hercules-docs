# `setlook()`

!!! warning
	This page may contain outdated information, incompatible with the current version of Hercules and its coding standards.

{{outdated}}

## Syntax

```c
setlook(<look type>, <look value>);
```

!!! warning
	The rest of this document hasn't been converted to Markdown yet.

== Description ==
[[setlook]] will alter the look data for the invoking character. It is used mainly for changing the palette used on hair and clothes: you specify which look type you want to change, then the palette you want to use. Make sure you specify a palette number that exists/is usable by the client you use. [[changelook]] works the same, but is only client side (it doesn't save the look value).

 // This will change your hair(6), so that it uses palette 8, what ever your 
 // palette 8 is, your hair will use that color
 
 setlook 6,8;
 
 // This will change your clothes(7), so they are using palette 1, whatever 
 // your palette 1 is, your clothes will then use that set of colors.
 
 setlook 7,1;

Here are the possible look types:
* 0 - Base sprite
* 1 - Hairstyle
* 2 - Weapon
* 3 - Head bottom
* 4 - Head top
* 5 - Head mid
* 6 - Hair color
* 7 - Clothes color
* 8 - Shield
* 9 - Shoes

Whatever 'shoes' means is anyone's guess, ask Gravity - the client does nothing with this value. It still wants it from the server though, so it is kept, but normally doesn't do a thing.
 
Only the look data for hairstyle, hair color and clothes color are saved to the char server's database and will persist. The rest freely change as the character puts on and removes equipment, changes maps, logs in and out and otherwise you should not expect to set them. In fact, messing with them is generally hazardous, do it at your own risk, it is not tested what will this actually do - it won't cause database corruption and probably won't cause a server crash, but it's easy to crash the client with just about anything unusual.

However, it might be an easy way to quickly check for empty view IDs for sprites, which is essential for making custom headgear.

Since a lot of people have different palettes for hair and clothes, it's impossible to tell you what all the color numbers are. If you want a serious example, there is a Stylist script inside the default Hercules installation that you can look at, this may help you create a Stylist of your own: [`npc/custom/stylist.txt`](https://github.com/HerculesWS/Hercules/blob/stable/npc/custom/stylist.txt)
