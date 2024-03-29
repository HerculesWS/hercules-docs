# Installation (Debian)

This guide covers how to install [[Hercules]] on [[wikipedia:Debian|Debian]] and other [[wikipedia:List_of_Linux_distributions#Debian-based|versions of Linux]] that use apt-get.

== Requirements ==
* [[wikipedia:Debian|Debian]] or an [[wikipedia:List_of_Linux_distributions##Debian-based]] that has the apt-get command
* root access or access to an account that has [[wikipedia:Sudo|sudo privileges]]
* an Internet connection to download install packages


== Prerequisites ==
All of these commands will be typed at the [[wikipedia:Command-line_interface|command-line interface]].
=== Install Prerequisites ===
# Login to your server via [[wikipedia:Secure_Shell|SSH]], or if you are already logged into a [[wikipedia:Graphical_user_interface|GUI]] press Ctrl+Alt+T to open a terminal window.
apt-get update
apt-get upgrade
apt-get dist-update  // To update to the latest version of Debian
# Type the following command (this will install GCC, Make, MySQL Server, MySQL header files,  PCRE header files, git, and Zlib header files) 
#: <pre>apt-get install git make gcc mysql-server libmysqlclient-dev zlib1g-dev libpcre3-dev screen</pre>

=== Create a non-root Linux user ===
By the [[wikipedia:Principle_of_least_privilege|principle of least privilege]], it is recommended you do '''NOT''' run Hercules as root. 
# Type the following command to create a non-root Linux account:
#: <pre>useradd hercuser</pre>
# Be sure not to forget setting new password for new user
#: <pre>passwd hercuser</pre>

== Install [[Hercules]] ==

=== Login as your non-root Linux user ===
The rest of the setup is done as hercuser (the Linux user you created earlier)
# Logout from root SSH (or minimize the window).
# Login to your server via SSH as the hercuser Linux user.

=== Git Clone ===
<pre>git clone https://github.com/HerculesWS/Hercules.git ~/Hercules</pre>

=== [http://dev.mysql.com/doc/refman/5.5/en/batch-commands.html Import] MySQL Tables ===
# Change directory to the '''sql-files''' folder.
#: <pre>cd sql-files/</pre>
# Execute these commands: 
#: ''When prompted, enter your MySQL root password.''
#: <pre>mysql -u root -prootpassword hercuser_rodb < main.sql</pre>
#: <pre>mysql -u root -prootpassword hercuser_rodblog < logs.sql</pre>
# If your Control Panel software or website requires it, you may also import the item, monster and monster skill databases (not necessary for the correct operation of Hercules)
#: (pre-renewal)
#: <pre>mysql -u root -prootpassword hercuser_rodb < item_db.sql</pre>
#: <pre>mysql -u root -prootpassword hercuser_rodb < mob_db.sql</pre>
#: <pre>mysql -u root -prootpassword hercuser_rodb < mob_skill_db.sql</pre>
#: (renewal)
#: <pre>mysql -u root -prootpassword hercuser_rodb < item_db_re.sql</pre>
#: <pre>mysql -u root -prootpassword hercuser_rodb < mob_db_re.sql</pre>
#: <pre>mysql -u root -prootpassword hercuser_rodb < mob_skill_db_re.sql</pre>
#: (common to renewal and pre-renewal)
#: <pre>mysql -u root -prootpassword hercuser_rodb < item_db2.sql</pre>
#: <pre>mysql -u root -prootpassword hercuser_rodb < mob_db2.sql</pre>
#: <pre>mysql -u root -prootpassword hercuser_rodb < mob_skill_db2.sql</pre>

NOTE: if you want to use different SQL DBs for login/char/map servers this is the list of databases each server use:
#login-server: global_acc_reg_num_db, global_acc_reg_str_db, ipbanlist, login, loginlog
#map-server: autotrade_data, autotrade_merchants, mapreg, npc_market_data
#char-server: everything else
Note that the sql_updates table is needed by all three servers.

=== [[:Category:Configuration|Configure Hercules]]===

=== Compile Source Code ===
 cd Hercules
 ./configure
 make sql

'''Note:''' If during the configure step you run into the "MySQL not found or incompatible" error, you may be able to fix it by installing "libssl-dev" and/or "default-libmysqlclient-dev".

*If you have added plugins for use with Hercules please use the below syntax instead of the above:
 cd Hercules
 ./configure
 make sql plugins


===== How to Recompile =====
In the future (after you update or edit any file in /src) to recompile, add ''make clean'' before make sql: 
 cd Hercules
 ./configure
 '''make clean'''
 make sql plugins

== Start your Hercules Server ==
 //change access mode of athena-start file so that you can execute it.
 //Use (dos2unix athena-start) if you are getting ^M errors ie. newline errors 
 chmod a+x athena-start

 //To Start
 ./athena-start start
 //To Stop
 ./athena-start stop
 //To Restart
 ./athena-start restart

== See Also ==

[[Category:Installation Guides|Debian Linux]]
