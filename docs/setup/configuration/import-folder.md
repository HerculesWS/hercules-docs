!!! warning
	This page may contain outdated information, incompatible with the current version of Hercules and its coding standards.


# Import folder Introduction

The Import Folder is used to import virtually all of your configuration changes and settings into the core of the
Hercules emulator without ever making changes to any .conf files after it is initially configured. This is very helpful
when Creating a New Server Build, Compiling , or Updating to the Latest version this will allow retention of all the
settings you previously configured without having to deal with possible overwrite conflicts from a git pull or change
over to a New Server Build.

# How it works

So, It works as such; Once you have configured all of the files you wish to configure within the Conf directory of your
server side you will take those same settings and copy them to the corresponding import directory files. For Example:
Lets say you make the following changes to;

**conf/battle/client.conf** ---\> Make your desired changes, in this case we are changing hair and dye settings.

`// Valid range of dyes and styles on the client.`  
`min_hair_style: 0`  
`max_hair_style: 27 ----> Changing to 40`  
`min_hair_color: 0`  
`max_hair_color: 8 ----> Changing to 200`  
`min_cloth_color: 0 `  
`max_cloth_color: 4 ----> Changing to 100`

**conf/battle/client.conf** ---\> We then simply copy only the changed setting lines into ---\>
conf/import/client_conf.txt

`max_hair_style: 40`  
`max_hair_color: 200`  
`max_cloth_color: 100`

Since these three settings were the only ones we changed in this example these are the only configuration lines to copy
from the .conf file into the corresponding import.txt file. This will now allow the server to directly import these
changed settings. This can be done with any of the configuration files. The server reads .confs files within the conf
directory first, however any settings configured within the /import/ folder will be read second, thus overwriting
default settings. Please note over time settings have changed, so please compare Import.txt Files to any New Server
Configuration Settings.

# Commonly Imported Settings

The most common use of these files is for the following parameters:  
**/conf/login_athena.conf** -\> /conf/import/login_conf.txt

`login_port: 6900`  
`account.engine: auto`  
`account.sql.db_hostname: 127.0.0.1`  
`account.sql.db_port: 3306`  
`account.sql.db_username: ragnarok`  
`account.sql.db_password: ragnarok`  
`account.sql.db_database: ragnarok`

**/conf/char_athena.conf** -\> /conf/import/char_conf.txt

`userid: s1`  
`passwd: p1`  
`server_name: Hercules`  
`login_port: 6900`  
`char_ip: 127.0.0.1`  
`char_port: 6121`  
`start_point: new_1-1,53,111`

**/conf/map_athena.conf** -\> /conf/import/map_conf.txt

`userid: s1`  
`passwd: p1`  
`char_ip: 127.0.0.1`  
`char_port: 6121`  
`map_ip: 127.0.0.1`  
`map_port: 5121`

**/conf/inter_athena.conf** -\> /conf/import/inter_conf.txt

`sql.db_hostname: 127.0.0.1`  
`sql.db_port: 3306`  
`sql.db_username: ragnarok`  
`sql.db_password: ragnarok`  
`sql.db_database: ragnarok`  
`char_server_ip: 127.0.0.1`  
`char_server_port: 3306`  
`char_server_id: ragnarok`  
`char_server_pw: ragnarok`  
`char_server_db: ragnarok`  
`map_server_ip: 127.0.0.1`  
`map_server_port: 3306`  
`map_server_id: ragnarok`  
`map_server_pw: ragnarok`  
`map_server_db: ragnarok`  
`log_db_ip: 127.0.0.1`  
`log_db_port: 3306`  
`log_db_id: ragnarok`  
`log_db_pw: ragnarok`  
`log_db_db: ragnarok`  
`log_login_db: loginlog`  
`use_sql_db: no`

# Conclusion

The Import Folder is a powerful tool and is often overlooked by amateur developers, but it saves a lot of time and
effort it is highly recommended to use. The import.txt files can be saved and used in any new build, just ensure you
double check the pathways and corresponding configuration settings. The import folder is often incomplete or blank when
downloading latest revisions, you will have to add the necessary files or overwrite the blank template files.

[Category:Configuration](Category:Configuration "wikilink")
