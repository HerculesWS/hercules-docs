# Installation (Debian)

This guide covers how to install [Hercules](Hercules "wikilink") on [Debian](https://en.wikipedia.org/wiki/Debian) and other
[versions of Linux](https://en.wikipedia.org/wiki/List_of_Linux_distributions#Debian-based) that use apt-get.

## Requirements

- [Debian](https://en.wikipedia.org/wiki/Debian) or an
  [wikipedia:List_of_Linux_distributions##Debian-based](https://en.wikipedia.org/wiki/List_of_Linux_distributions##Debian-based)
  that has the apt-get command
- root access or access to an account that has [sudo privileges](https://en.wikipedia.org/wiki/Sudo)
- an Internet connection to download install packages

## Prerequisites

All of these commands will be typed at the [command-line interface](https://en.wikipedia.org/wiki/Command-line_interface).

### Install Prerequisites

1.  Login to your server via [SSH](https://en.wikipedia.org/wiki/Secure_Shell), or if you are already logged into a
    [GUI](https://en.wikipedia.org/wiki/Graphical_user_interface) press Ctrl+Alt+T to open a terminal window.

apt-get update apt-get upgrade apt-get dist-update // To update to the latest version of Debian

1.  Type the following command (this will install GCC, Make, MySQL Server, MySQL header files, PCRE header files, git,
    and Zlib header files)
      
        apt-get install git make gcc mysql-server libmysqlclient-dev zlib1g-dev libpcre3-dev screen

### Create a non-root Linux user

By the [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege), it is recommended you do
**NOT** run Hercules as root.

1.  Type the following command to create a non-root Linux account:
      
        useradd hercuser
2.  Be sure not to forget setting new password for new user
      
        passwd hercuser

## Install [Hercules](Hercules "wikilink")

### Login as your non-root Linux user

The rest of the setup is done as hercuser (the Linux user you created earlier)

1.  Logout from root SSH (or minimize the window).
2.  Login to your server via SSH as the hercuser Linux user.

### Git Clone

    git clone https://github.com/HerculesWS/Hercules.git ~/Hercules

### [Import](http://dev.mysql.com/doc/refman/5.5/en/batch-commands.html) MySQL Tables

1.  Change directory to the **sql-files** folder.
      
        cd sql-files/
2.  Execute these commands:
      
    *When prompted, enter your MySQL root password.*

        mysql -u root -prootpassword hercuser_rodb < main.sql

        mysql -u root -prootpassword hercuser_rodblog < logs.sql
3.  If your Control Panel software or website requires it, you may also import the item, monster and monster skill
    databases (not necessary for the correct operation of Hercules)
      
    (pre-renewal)

        mysql -u root -prootpassword hercuser_rodb < item_db.sql

        mysql -u root -prootpassword hercuser_rodb < mob_db.sql

        mysql -u root -prootpassword hercuser_rodb < mob_skill_db.sql

    (renewal)

        mysql -u root -prootpassword hercuser_rodb < item_db_re.sql

        mysql -u root -prootpassword hercuser_rodb < mob_db_re.sql

        mysql -u root -prootpassword hercuser_rodb < mob_skill_db_re.sql

    (common to renewal and pre-renewal)

        mysql -u root -prootpassword hercuser_rodb < item_db2.sql

        mysql -u root -prootpassword hercuser_rodb < mob_db2.sql

        mysql -u root -prootpassword hercuser_rodb < mob_skill_db2.sql

NOTE: if you want to use different SQL DBs for login/char/map servers this is the list of databases each server use:

1.  login-server: global_acc_reg_num_db, global_acc_reg_str_db, ipbanlist, login, loginlog
2.  map-server: autotrade_data, autotrade_merchants, mapreg, npc_market_data
3.  char-server: everything else

Note that the sql_updates table is needed by all three servers.

### [Configure Hercules](:Category:Configuration "wikilink")

### Compile Source Code

`cd Hercules`  
`./configure`  
`make sql`

**Note:** If during the configure step you run into the "MySQL not found or incompatible" error, you may be able to fix
it by installing "libssl-dev" and/or "default-libmysqlclient-dev".

- If you have added plugins for use with Hercules please use the below syntax instead of the above:

`cd Hercules`  
`./configure`  
`make sql plugins`

##### How to Recompile

In the future (after you update or edit any file in /src) to recompile, add *make clean* before make sql:

`cd Hercules`  
`./configure`  
**`make clean`**  
`make sql plugins`

## Start your Hercules Server

`//change access mode of athena-start file so that you can execute it.`  
`//Use (dos2unix athena-start) if you are getting ^M errors ie. newline errors `  
`chmod a+x athena-start`

`//To Start`  
`./athena-start start`  
`//To Stop`  
`./athena-start stop`  
`//To Restart`  
`./athena-start restart`

## See Also

[Debian Linux](Category:Installation_Guides "wikilink")
