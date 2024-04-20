# Installation (FreeBSD)

This article is aimed at installing and getting [Hercules](Hercules "wikilink") to run successfully on a machine running
[FreeBSD](https://en.wikipedia.org/wiki/FreeBSD) 9.1-RELEASE. It is assumed that FreeBSD was installed with the ports collection
and enabled Linux Threading on install. This guide will NOT teach you how to network FreeBSD, install FreeBSD or
configure any additional system settings (besides the ones needed to run Hercules and its dependencies).

# Before we Start

We will primarily working from the /home/user directory. Your primary user will need to be in the 'wheel' group and be
able to su into root. Remember that I will include either \$ or \#, depending on who you should be. \$ indicates you
should be your primary user, and \# indicates you should be root.

# Required software

We are going to use FreeBSD's ports collection to download, install and use most of these programs. It is assumed you
already installed the ports collection, if you have not, I suggest you do that now.

## Ports Collection

The Ports Collection is a set of files used to compile and install applications on FreeBSD. While this is not a guide
for FreeBSD, its recommended to obtain the same as given below: <code>

    # portsnap fetch
    Download a compressed snapshot of the Ports Collection into /var/db/portsnap.

    # portsnap extract
    When running Portsnap for the first time, extract the snapshot into /usr/ports

</code>

## wget

wget is a download manager available on FreeBSD and can be your bread and butter while working on FreeBSD. <code>

    # whereis wget
    wget: /usr/ports/www/wget
    # cd /usr/ports/www/wget && make && make install
    # make clean
    # rehash

</code>

## gmake

gmake, or GNUMake, is the GCC compiler used for FreeBSD. <code>

    # whereis gmake
    gmake: /usr/ports/devel/gmake
    # cd /usr/ports/devel/gmake && make && make install
    # make clean
    # rehash

</code>

## unrar

unrar is a tool to unrar .rar's in BSD. <code>

    # whereis unrar
    unrar: /usr/ports/archivers/unrar
    $ cd /usr/ports/archivers/unrar
    $ make clean
    $ make install
    $ rehash

</code>

## GCC

GCC is the GNU Compiler Collection and front ends for C, C++ and other languages. This may not be available on the
system but it can be obtained as below: <code>

    # wget http://www.netgull.com/gnu/gcc/gcc-###.tar.gz (Where ## is the version number. visit the mirror to find out)
    # tar -xvf gcc-###.tar.gz
    # cd gcc*
    # make && make install
    # make clean
    # rehash

</code>

## gdb

GDB is handy tool to have on a development machine, as it can take backtraces of crashes and help you find what went
wrong. It is probable that this is already available on your FreeBSD, but if it's not, here's how you can install it:
<code>

    # wget http://ftp.gnu.org/gnu/gdb/gdb-###.tar.gz (again, where ### is the version number, check out the mirror)
    # tar -xvf gdb-###.tar.gz
    # cd gdb*
    # make && make install
    # make clean 
    # rehash

</code>

## git

[Git](Git "wikilink") is the versioning system used for Hercules and how we will get our copy of Hercules. <code>

    # whereis git
    git: /usr/ports/devel/git
    # cd /usr/ports/devel/git && make && make install
    # make clean
    # rehash

</code>

Now, let's go ahead and download Hercules. We'll use git for this.

    $ su root
    # adduser //create a Hercules user
    # exit
    $ su hercules
    $ cd /home/hercules
    $ git clone https://github.com/HerculesWS/Hercules.git Hercules
    $

Now, we can populate the tables with the .sql files in Hercules. Navigate to your /sql-files/ folder in the Hercules
files you just checked out.

    $ cd /home/hercules/trunk/sql-files
    $ mysql -uuser -ppassword myr-odb < main.sql
    $ mysql -uuser -ppassword myro-db < logs.sql

Now, you'll want to follow the steps in the [:Category:Configuration](:Category:Configuration "wikilink") and
[Connecting](Connecting "wikilink") pages to get your Hercules configured. Once you've made all your source changes, you
can compile Hercules. While you're in the root of your Hercules folder, issue the following commands to compile your
server:

    $ ./configure
    $ gmake clean
    $ gmake sql
    $ rehash

**Important Note:** If you are using a 32 bit FreeBSD you have to use

    chmod 777 configure
    $ ./configure --disable-64bit

instead

*NOTE:* You should **NEVER** run Hercules as the root user!. Always setup a new user and this cannot be stressed enough
on! This will also prevent your from having difficulties with file permissions.

And to start your servers, you can simply use the following command:

    $ ./athena-start <command> (start | stop | restart | status)

And that's it! You now have Hercules running on your FreeBSD machine!

[Category:Installation Guides](Category:Installation_Guides "wikilink")
