Using '''configure''' script is a method to generate makefiles before compilation in Unix systems.

When installing Hercules, configure script should be run after [[Git Clone]] and before compiling.

== Basic usage ==
<onlyinclude><includeonly><blockquote>''Main article: [[Configure]].''</blockquote></includeonly>
To avoid errors in server-client communication, <code>[[PACKETVER]]</code> must be set to date the client you're going to use has been released at (in YYYYMMDD format), eg <code>20100730</code> for 2010-07-30aRagexeRE. Instead of editing [[mmo.h]] directly, <code>PACKETVER</code> can be set to desired date with configure switch <code>--enable-packetver=YYYYMMDD</code>.

Run following command, replacing ''YYYYMMDD'' with your client release date, eg ''20100730''.
  ./configure --enable-packetver=YYYYMMDD
Configure script will perform necessary tests and generate makefiles.
</onlyinclude>
=== Sample output ===
<pre>checking whether make sets $(MAKE)... yes
checking for gcc... gcc
checking for C compiler default output file name... a.out
checking whether the C compiler works... yes
checking whether we are cross compiling... no
checking for suffix of executables...
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether gcc accepts -g... yes
checking for gcc option to accept ANSI C... none needed
checking how to run the C preprocessor... gcc -E
checking whether byte ordering is bigendian... no
checking whether pointers can be stored in ints (old code)... yes
checking whether gcc supports -Wno-unused-parameter... yes
checking whether gcc supports -Wno-pointer-sign... yes
checking whether gcc can actually use -Wno-pointer-sign... yes
checking whether gcc supports -Wno-switch... yes
checking whether gcc supports -fPIC... yes
checking whether gcc needs -fPIC for shared objects... no
checking whether gcc supports -fno-strict-aliasing... yes
checking whether gcc is able to typecast to union... yes
checking for setrlimit... yes
checking for strnlen... yes
checking for inflateEnd in -lz... yes
checking zlib.h usability... yes
checking zlib.h presence... yes
checking for zlib.h... yes
checking for library containing sqrt... -lm
checking for library containing clock_gettime... -lrt
checking whether CLOCK_MONOTONIC is supported and works... yes
checking for mysql_config... /usr/bin/mysql_config
checking for mysql_init in -lmysqlclient... yes
checking mysql.h usability... yes
checking mysql.h presence... yes
checking for mysql.h... yes
checking MySQL library (optional)... yes (5.0.51a)
checking for pcre_study in -lpcre... yes
checking PCRE library (optional)... yes
checking host OS... Linux
checking for MinGW... no
configure: creating ./config.status
config.status: creating Makefile
config.status: creating src/common/Makefile
config.status: creating 3rdparty/mt19937ar/Makefile
config.status: creating src/char/Makefile
config.status: creating src/login/Makefile
config.status: creating src/char_sql/Makefile
config.status: creating src/txt-converter/Makefile
config.status: creating src/map/Makefile
config.status: creating src/plugins/Makefile
config.status: creating src/tool/Makefile</pre>
=== Setting executable bit ===
In order to run configure script it must be executable, ie have the ''execute'' permission set. When checking out a working copy from a git repository repository, executable bit should be set automatically. However, if it fails for some reason, running <code>./configure</code> will bring the following message (or similar):
  bash: ./configure: Permission denied
To fix this, set executable permission with:
  chmod +x ./configure

== Additional switches ==
To display all available switches use:
  ./configure --help

=== Debug mode ===
It is possible to compile Hercules in debug mode with <code>--enable-debug</code> switch.
[[Category:Installation]]