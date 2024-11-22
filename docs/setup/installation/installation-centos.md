# Installation (CentOS)

This guide covers how to install [Hercules](Hercules "wikilink") on [CentOS](https://en.wikipedia.org/wiki/CentOS) and other
[versions of Linux](https://en.wikipedia.org/wiki/List_of_Linux_distributions#RPM-based) that use
[yum](https://en.wikipedia.org/wiki/Yellowdog_Updater,_Modified).

## Requirements

- [CentOS](https://en.wikipedia.org/wiki/CentOS) or an [RPM-based
  Linux](https://en.wikipedia.org/wiki/List_of_Linux_distributions#RPM-based) that has the
  **[yum](https://en.wikipedia.org/wiki/Yellowdog_Updater,_Modified)** command
- root access or access to an account that has [sudo privileges](https://en.wikipedia.org/wiki/Sudo)
- an Internet connection to download install packages

## Prerequisites

All of these commands will be typed at the [command-line interface](https://en.wikipedia.org/wiki/Command-line_interface).

### Install Prerequisites

1.  Login to your server via [SSH](https://en.wikipedia.org/wiki/Secure_Shell), or if you are already logged into a
    [GUI](https://en.wikipedia.org/wiki/Graphical_user_interface) press Ctrl+Alt+T to open a terminal window.
2.  Type the following command (this will install GCC, Make, MySQL, MySQL header files, MySQL Server, PCRE header files,
    Git, and Zlib header files)
      
        yum install gcc make mysql mysql-devel mysql-server pcre-devel git zlib-devel
3.  (Optional) type the following command to install some additional packages:
      
        yum -y install dos2unix gdb nano screen unzip wget zip

### Create a non-root Linux user

By the [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege), it is recommended you do
**NOT** run Hercules as root.

1.  Type the following command to create a non-root Linux account:
      
        useradd --create-home --shell /bin/bash hercules1234

    `--create-home` = create the user's home directory

    `--shell` = sets their login shell to [Bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell))

    **`hercules1234`** = the login name of the new Linux account

    *`1234`* = pick your own random numbers to make the username more unique
2.  Set a password for the new user (run this command and follow the prompts):
      
        passwd hercules1234

### Configure MySQL

#### Set a root password

The default MySQL Server install creates a MySQL user 'root'@'localhost' with NO password. It is recommended you create
a password for the root user.

1.  Run this command and follow the prompts:
      
    First Start MySQL:

        /etc/init.d/mysqld start 

    Then configure MySQL by:

        mysql_secure_installation
2.  Login to your MySQL Server as root:
      
    *When prompted, enter your root MySQL password.*

        mysql --user=root -p
3.  Now your prompt should look like this (the MySQL command prompt):
      
        mysql> 

#### Create SQL database for Hercules

1.  At the MySQL prompt, type this to [create a database](http://dev.mysql.com/doc/refman/5.5/en/create-database.html)
    (replace `hercules1234` with the Linux username you created earlier):
      
        mysql> CREATE DATABASE hercules1234_rag;
2.  Create a separate database for logs:
      
        mysql> CREATE DATABASE hercules1234_log;

#### Setup a MySQL user for Hercules

1.  At the MySQL prompt, type something like this to create a new MySQL user:
      
        mysql> CREATE USER 'hercules1234'@'localhost' IDENTIFIED BY 'secretpassword';

    `hercules1234` = the name of the MySQL user (we named it the same as the Linux user to make it easier to identify)

    `localhost` = the hostname or IP it will connect from

    **`secretpassword`** = the password for this MySQL user
2.  [Grant privileges](http://dev.mysql.com/doc/refman/5.5/en/grant.html) to the 'hercules' MySQL user:
      
        mysql> GRANT SELECT,INSERT,UPDATE,DELETE ON `hercules1234\_rag`.* TO 'hercules1234'@'localhost';

        mysql> GRANT SELECT,INSERT ON `hercules1234\_log`.* TO 'hercules1234'@'localhost';

    (note the [escaped
    underscore](http://dev.mysql.com/doc/refman/5.5/en/string-literals.html#character-escape-sequences))

## Install [Hercules](Hercules "wikilink")

### Login as your non-root Linux user

The rest of the setup is done as hercules1234 (the Linux user you created in step 2.2)

1.  Logout from root SSH (or minimize the window).
2.  Login to your server via SSH as the hercules1234 Linux user.

### Git Clone

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

##### How to Recompile

In the future (after you update or edit any file in /src) to recompile, add *make clean* before make sql:

`cd Hercules`  
`./configure`  
**`make clean`**  
`make sql`

## Start your Hercules Server

`//change access mode of athena-start file so that you can execute it.`  
`//Use (dos2unix athena-start) if yo uare getting ^M errors ie. newline errors `  
`chmod a+x athena-start`

`//To Start`  
`./athena-start start`  
`//To Stop`  
`./athena-start stop`  
`//To Restart`  
`./athena-start restart`

## See Also

[CentOS](Category:Installation_Guides "wikilink")
