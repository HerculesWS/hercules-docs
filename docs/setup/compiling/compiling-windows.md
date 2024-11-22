# Compiling (Windows)

For compiling on Windows, Visual Studio is the preferred method, although using Cygwin is also possible.

### Using Visual Studio

<img src="Compile_hercules.PNG"
title="MS Visual Studio 2012: Compile configuration (red) and solution (blue) with it&#39;s child projects." width="300"
alt="MS Visual Studio 2012: Compile configuration (red) and solution (blue) with it&#39;s child projects." /> Hercules
ships with solution and project files for Visual Studio from 2012 onwards.

- Download the latest version of [Visual Studio](https://www.visualstudio.com) (at the time of writing, MS Visual Studio
  2015 Community Edition) and install it, if you do not have Visual Studio already installed.
- Open **Hercules-14.sln** in your Hercules folder if you use Visual Studio 2015, for Visual Studio 2013, you need to
  open **Hercules-12.sln**, for Visual Studio 2012, you need to open **Hercules-11.sln** instead.
- Select the desired compile configuration (marked <span style="color:red;">red</span>). Use **Release** when you
  compile the server, where players will be playing on. **Debug** compiles the server without optimizations and with
  debugging information.
- Right-click the solution node (marked <span style="color:blue;">blue</span>) and select **Build solution**. If you
  have compiled the server before, it is recommended to use **Rebuild solution**, as it forces the compiling of all
  components, not just those, which seem to have changed since last compile.
- If the compilation was successful, the resulting executables are in the same folder as the solution named
  *login-server.exe*, *char-server.exe*, *map-server.exe* and *mapcache.exe*.

### Using Cygwin

[Cygwin](http://www.cygwin.com/) is a POSIX compatibility layer for Windows. As such it enables compiling the way it
would be done on Linux. Compiling in Cygwin is **not recommended** due to lower performance and increased installation
complexity.

- Download [Cygwin](http://www.cygwin.com/setup.exe) and install it, if not already done so. When installing, select
  following packages:
  - from *Devel*: *cmake*, *gcc* and *make*
  - from *Lib*: *libidn-devel*, *libpcre-devel*, *readline*, *zlib-devel*
- Running Cygwin Terminal will create folder **`home/user`** inside Cygwin installation folder, where *user* is the name
  currently logged on Windows user.
- SQL server needs to be installed in Cygwin so the compiler can access the SQL libraries. Download the .tar.gz archive
  from the [MySQL website](http://dev.mysql.com/downloads/mysql/?current_os=src), such as **mysql-5.5.20.tar.gz**.
- Place the archive into **`/home/user`** and execute following inside Cygwin Terminal to unpack it:

` cd ~`  
` tar xvzf mysql-5.5.20.tar.gz`

- Navigate to directory with unpacked archive:

` cd mysql-5.5.20`

- To avoid conficts, replace *dtoa()* with *\_dtoa()* in *strings/dtoa.c* file:

` sed -i 's/dtoa(/_dtoa(/g' ./strings/dtoa.c`

- Build MySQL with following commands:

` cmake .`  
` make mysqlclient libmysql`  
` make install`

- After everything completes, Cygwin is ready for compiling Hercules. Navigate to the Hercules folder in Cygwin. Windows
  drives are accesible as `/cygdrive/x` where *x* is the letter assigned to the drive by Windows.
- Execute following commands inside Hercules folder to compile it:

` ./configure --with-mysql=/usr/local/mysql/bin/mysql_config`  
` make sql`

- If the compilation was successful, the resulting executables are in the Hercules folder named *login-server_sql.exe*,
  *char-server_sql.exe* and *map-server_sql.exe*.
- Server executables can be run inside Cygwin Terminal or directly, but in this case you need to copy required libraries
  to Hercules folder:
  - *cygwin1.dll*, *cygz.dll*, *cyggcc_s-1.dll*, *cygpcre-0.dll* from `/bin`
  - *cygmysqlclient-18.dll* from `/usr/local/mysql/lib`
