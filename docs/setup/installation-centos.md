# Installation (CentOS)

This guide covers how to install [[Hercules]] on [[wikipedia:CentOS|CentOS]] and other [[wikipedia:List_of_Linux_distributions#RPM-based|versions of Linux]] that use [[wikipedia:Yellowdog_Updater,_Modified|yum]].

== Requirements ==
* [[wikipedia:CentOS|CentOS]] or an [[wikipedia:List_of_Linux_distributions#RPM-based|RPM-based Linux]] that has the '''[[wikipedia:Yellowdog_Updater,_Modified|yum]]''' command
* root access or access to an account that has [[wikipedia:Sudo|sudo privileges]]
* an Internet connection to download install packages


== Prerequisites ==
All of these commands will be typed at the [[wikipedia:Command-line_interface|command-line interface]].
=== Install Prerequisites ===
# Login to your server via [[wikipedia:Secure_Shell|SSH]], or if you are already logged into a [[wikipedia:Graphical_user_interface|GUI]] press Ctrl+Alt+T to open a terminal window.
# Type the following command (this will install GCC, Make, MySQL, MySQL header files, MySQL Server, PCRE header files, Git, and Zlib header files) 
#: <pre>yum install gcc make mysql mysql-devel mysql-server pcre-devel git zlib-devel</pre>
# (Optional) type the following command to install some additional packages: 
#: <pre>yum -y install dos2unix gdb nano screen unzip wget zip</pre>

=== Create a non-root Linux user ===
By the [[wikipedia:Principle_of_least_privilege|principle of least privilege]], it is recommended you do '''NOT''' run Hercules as root. 
# Type the following command to create a non-root Linux account:
#: <pre>useradd --create-home --shell /bin/bash hercules1234</pre>
#: <code>--create-home</code> = create the user's home directory
#: <code>--shell</code> = sets their login shell to [[wikipedia:Bash_(Unix_shell)|Bash]]
#: '''<code>hercules1234</code>''' = the login name of the new Linux account
#: ''<code>1234</code>'' = pick your own random numbers to make the username more unique
# Set a password for the new user (run this command and follow the prompts):
#: <pre>passwd hercules1234</pre>

=== Configure MySQL ===

==== Set a root password ====
The default MySQL Server install creates a MySQL user 'root'@'localhost' with NO password. It is recommended you create a password for the root user. 
# Run this command and follow the prompts: 
#: First Start MySQL:
#: <pre>/etc/init.d/mysqld start </pre>
#: Then configure MySQL by:
#: <pre>mysql_secure_installation</pre>
# Login to your MySQL Server as root: 
#: ''When prompted, enter your root MySQL password.''
#: <pre>mysql --user=root -p</pre>
# Now your prompt should look like this (the MySQL command prompt): 
#: <pre>mysql> </pre>

==== Create SQL database for Hercules ====
# At the MySQL prompt, type this to [http://dev.mysql.com/doc/refman/5.5/en/create-database.html create a database] (replace <code>hercules1234</code> with the Linux username you created earlier): 
#: <pre>mysql> CREATE DATABASE hercules1234_rag;</pre>
# Create a separate database for logs: 
#: <pre>mysql> CREATE DATABASE hercules1234_log;</pre>

==== Setup a MySQL user for Hercules ====
# At the MySQL prompt, type something like this to create a new MySQL user: 
#: <pre>mysql> CREATE USER 'hercules1234'@'localhost' IDENTIFIED BY 'secretpassword';</pre>
#: <code>hercules1234</code> = the name of the MySQL user (we named it the same as the Linux user to make it easier to identify)
#: <code>localhost</code> = the hostname or IP it will connect from
#: '''<code>secretpassword</code>''' = the password for this MySQL user
# [http://dev.mysql.com/doc/refman/5.5/en/grant.html Grant privileges] to the 'hercules' MySQL user:
#: <pre>mysql> GRANT SELECT,INSERT,UPDATE,DELETE ON `hercules1234\_rag`.* TO 'hercules1234'@'localhost';</pre>
#: <pre>mysql> GRANT SELECT,INSERT ON `hercules1234\_log`.* TO 'hercules1234'@'localhost';</pre> (note the [http://dev.mysql.com/doc/refman/5.5/en/string-literals.html#character-escape-sequences escaped underscore])

== Install [[Hercules]] ==

=== Login as your non-root Linux user ===
The rest of the setup is done as hercules1234 (the Linux user you created in step 2.2)
# Logout from root SSH (or minimize the window).
# Login to your server via SSH as the hercules1234 Linux user.

=== Git Clone ===
{{:Git Clone/Unix}}

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

===== How to Recompile =====
In the future (after you update or edit any file in /src) to recompile, add ''make clean'' before make sql: 
 cd Hercules
 ./configure
 '''make clean'''
 make sql

== Start your Hercules Server ==
 //change access mode of athena-start file so that you can execute it.
 //Use (dos2unix athena-start) if yo uare getting ^M errors ie. newline errors 
 chmod a+x athena-start

 //To Start
 ./athena-start start
 //To Stop
 ./athena-start stop
 //To Restart
 ./athena-start restart

== See Also ==

[[Category:Installation Guides|CentOS]]
