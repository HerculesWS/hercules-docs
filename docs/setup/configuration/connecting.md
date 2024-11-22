!!! warning
	This page may contain outdated information, incompatible with the current version of Hercules and its coding standards.

This article covers taking the configuration steps to ensure a successful connection to your servers. You are required
to know the in and outs of your OS, as well as what a [LAN IP](https://en.wikipedia.org/wiki/Local_area_network) and a [WAN
IP](https://en.wikipedia.org/wiki/Wide_area_network) are.

## Basics of the three servers

### Login Server

The login server handles all login packets from the client. The client sees the login server first and connects to it
first. The login server listens on the port 6900 by default and usually reads data from the login table. The login
server connects directly to the character server and passes it's information to it once the client has successfully
logged in. If your login server won't connect, your players cannot login in, but can play.

### Character Server

The character server handles all character selection and character loading for the map server. The character server
receives commands to primarily display characters once the client has logged in. The character server listens on the
port 6121 by default. It also handles the loading and saving of most character data. If the character server becomes
disconnected, character data saving is not possible.

### Map Server

The map server handles all map functions, including, but not limited to, mob functions, map functions, NPC loading and
unloading, as well as NPC processing. the map server is your bread and butter and allows people to play on your server.
It listens on the port 5121 by default.

If the character server becomes disconnected from your map server, it's likely the mapserver will disconnect everyone
from it. This is not the case when the MySQL server loses its connection to Hercules, as Hercules currently does not
restore this connection.

### Port Forwarding

If you intend to let your players play from an external internet connection, you *must* forward ports 6900, 6121, and
5121 respectively in your router's control panel. Simply forwarding port 6900 is not enough to allow clients to connect,
and traffic will not be passed solely through your login server, even though they can communicate with one another
internally on your localhost address.

## Configuring Hercules for use

After you have finished [compiling](compiling "wikilink") Hercules, you can set it up for use. There will be four files
that we will concentrate on. Any settings we change in these files should **always** be moved to the relevant import
folder files. If your compiler hasn't already made a copy of the
\[\`conf/import-tmpl\`\](https://github.com/HerculesWS/Hercules/tree/stable/conf/import-tmpl) folder and named it
/conf/import do that now.

##### Using the /conf/import/ folder (\[\`conf/import-tmpl/\`\](https://github.com/HerculesWS/Hercules/tree/stable/conf/import-tmpl))

In this folder, you can 'import' your settings into each of the respected files. All you need is each parameter. When
you do this, your settings will never be overwritten when you need to update your GIT, as the import folder is built
once. You can throw all of your settings in here and they will remain as they are, and will read AFTER the main
settings, which means these settings will take priority.

### Step 1. Interserver Communication Passwords

First, you will need to set an intercommunication password and user. This is one of the most important steps to securing
your server.

In order for the char-server to accept commands and packets from the login server, and for the map-server to accept
commands and packets from the char-server they have to 'log-in' to each other, using the Server Communication passwords.
You MUST set these to something other than defaults, but you can set them to random characters, as long as they are the
same in the three places they appear in, which are:
\[\`conf/char-server.conf\`\](https://github.com/HerculesWS/Hercules/blob/stable/conf/char-server.conf),
\[\`conf/map-server.conf\`\](https://github.com/HerculesWS/Hercules/blob/stable/conf/map-server.conf) and your login sql
table. They are defaulted to s1/p1, and **MUST** be changed.

Changes must be made to the import folder to ensure proper upgradability. A good habit to get into when working with
GIT. Simply copy and paste the lines you wish to alter from the .conf file to the relevant .txt file in the import
folder. Your /conf/import/char_conf.txt *and* /conf/import/map_conf.txt files should look as follows, with *no* changes
made to \[\`conf/char-server.conf\`\](https://github.com/HerculesWS/Hercules/blob/stable/conf/char-server.conf) or
\[\`conf/map-server.conf\`\](https://github.com/HerculesWS/Hercules/blob/stable/conf/map-server.conf):  
<code>

    // Server Communication username and password.
    userid: [new user]
    passwd: [new password]

</code>

Your login table should match. Use this SQL query (or make the changes using your favourite SQL gui): <code>

    use databasename_rag;
    UPDATE login
    set `userid` = "[new user]", `user_pass` = "[new password]" where `account_id` = 1;

</code>

After the user and password is set, you can move on down the page.

### Step 2. \[\`conf/login-server.conf\`\](https://github.com/HerculesWS/Hercules/blob/stable/conf/login-server.conf)

Usually there is nothing to be done here in terms on connection. You may want to edit your login_port to something other
than default, but it must be an unused port by your OS.

You can find this out by starting all the services that you need on the server and issuing the following commands to
your console:

**If using Windows:**  
Goto Start, then click 'Run'. Type 'cmd' and press enter. Run the following command: <code>

    netstat -a

</code> **If using \*nix:** <code>

    $ lsof -i

</code>

Once you have selected a port if you're going to change it, your /conf/import/login_conf.txt file should look as
follows, with *no* changes made to
\[\`conf/login-server.conf\`\](https://github.com/HerculesWS/Hercules/blob/stable/conf/login-server.conf) (again just
copy pasting the lines we want to change from one file to the other):  
<code>

    // Login Server Port
    login_port: [new port]

</code>

### Step 3. \[\`conf/char-server.conf\`\](https://github.com/HerculesWS/Hercules/blob/stable/conf/char-server.conf)

This file sets parameters for the char-server to read. When you open this up, there are a few things we need to do in
here.

Firstly we should name our server:

When setting server_name, be sure to not use spaces as it says. <code>

    // Server name, use alternative character such as ASCII 160 for spaces.
    // NOTE: Do not use spaces in the name, or guild emblems won't work client-side!
    server_name: [new server name]

</code>

<code>

    // Wisp name for server: used to send wisp from server to players (between 4 to 23 characters)
    wisp_server_name: [new server name]

</code>

Usually, Hercules will auto-detect your external and internal IP if the IP fields are [commented
out](comments "wikilink"), but let's go ahead and remove the two slashes (//) from login_ip and char_ip.

The login_ip will point to the IP address where the login server will be running. Usually this is the localhost, or
127.0.0.1. If the login-server is to be located on the same network as the char-server (but on a different PC), use the
LAN IP of the login server's machine. If you are running a dedicated machine in a datacenter, or you know your IP is not
going to change, you can set this to your WAN IP.

<code>

    // Login Server IP
    // The character server connects to the login server using this IP address.
    // NOTE: This is useful when you are running behind a firewall or are on
    // a machine with multiple interfaces.
    login_ip: [new ip here]

</code>

The char_ip parameter will **ALWAYS** be your WAN IP, no exceptions. This is the IP that the char-server will accept
connections with.

<code>

    // Character Server IP
    // The IP address which clients will use to connect.
    // Set this to what your server's public IP address is.
    char_ip: [your wan ip here]

</code>

If you changed the login_port in login-server.conf, this setting here will need to match it. <code>

    // Login Server Port
    login_port: [new port]

</code>

Make sure to make any changes in the import folder as always.

### Step 4. \[\`conf/map-server.conf\`\](https://github.com/HerculesWS/Hercules/blob/stable/conf/map-server.conf)

This file sets parameters for the map-server to read.

The char_ip will point to the IP address where the login server will be running. Usually this is the localhost, or
127.0.0.1. If the char-server is to be located on the same network as the map-server (but on a different PC), use the
LAN IP of the char server's machine. If you are running a dedicated machine in a datacenter, or you know your IP is not
going to change, you can set this to your WAN IP.

<code>

    // Character Server IP
    // The map server connects to the character server using this IP address.
    // NOTE: This is useful when you are running behind a firewall or are on
    // a machine with multiple interfaces.
    char_ip: [new ip here]

</code>

The map_ip parameter will **ALWAYS** be your WAN IP, no exceptions. This is the IP that the map-server will accept
connections with.

<code>

    // Map Server IP
    // The IP address which clients will use to connect.
    // Set this to what your server's public IP address is.
    map_ip: [your wan ip here]

</code>

Make sure to make any changes in the import folder as always.

### Step 5. \[\`conf/inter-server.conf\`\](https://github.com/HerculesWS/Hercules/blob/stable/connf/inter-server.conf)

About midway down this file, you will find your SQL settings. These will be set as accordingly.

- The 'sql.db' settings control what the login-server reads for it's database settings.
- Hostname is the IP of the SQL server.
- Username is the username you use to login. For security, this should **NEVER** be root!
- Password is the password that the user will login with.
- The database is set to whatever the database name will be. Usually, this is just 'ragnarok'.

If you make any changes in here, copy paste the lines you change into /conf/import/inter_conf.txt and modify them there.

## Starting Hercules

When you're all done configuring Hercules, you can start it up. You can do this by simply running each of the three
servers, or athena-start.

## Client Side

### Diff your client

See [Hexing](Hexing#Creating_custom_RagRE_client_using_a_DIFF_patcher "wikilink").

### Data Folder

1.  Download the most recent data folder [here](http://svn6.assembla.com/svn/ClientSide/).
2.  Edit your [clientinfo.xml](Clientinfo "wikilink") as needed.

### Connect

Execute your exe.

## Trouble Shooting

Its always best to post in the [client support](https://herc.ws/board/forum/31-client-side-support/) sub-forum for
things that go wrong with the client, and [server support](https://herc.ws/board/forum/14-general-server-support/)
sub-forum for things that go wrong with Hercules connecting or if errors pop up in your server log.

### CHARACTER_INFO size error!!

To fix this, locate the src/common folder and open mmo.h in notepad. Find the following line: <code>

    #ifndef PACKETVER
    	#define PACKETVER 20110609

Edit this Part, put:

    #define PACKETVER YOURCLIENTDATE

So if my client was 2011-10-25aRagexeRE it would look like:

    #define PACKETVER 20111025

[Category:Configuration](Category:Configuration "wikilink")
