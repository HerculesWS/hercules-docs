# Compiling

## What is Compiling and what does Compile mean?

> A compiler is a computer program that translates computer code written in one programming language into another programming language. -[Simple Wikipedia](https://simple.wikipedia.org/wiki/Compiler?oldformat=true)

Given that definition, **to compile your source code** means to transform Hercules code from a set of `.c` and `.h` files into executable programs that your machine can run:

* `map-server.exe`, `char-server.exe`, `login-server.exe` files for Windows system.
* `map-server`, `char-server`, `login-server` for Unix systems.

### Why are the resulting files named differently?

Notice how `.exe` files are what are produced for Windows systems and how Unix systems use no file extension? That's because [different operating systems use different computer languages to run programs](https://superuser.com/questions/209703/why-wont-windows-exes-work-on-linux). (Think: Windows speaks English and Unix speaks French). That's why not all Windows applications work in Unix systems, and vice-versa. 

This is why you must compile the source code. Because you might have a Unix-based machine, while another person has a Windows-based machine. The source code is released by Hercules, so that you can build the appropriate program for your operating system.

**Definitions**

By _source code_, we mean the `.c` files that can be found in the `src/` folder.

# How do I compile my server or my plugins?

The first step is figuring out what your operating system is. This is because running programs in Windows is different from running programs in Unix systems (Linux, OSX).

## Unix

### Using configure & make

Configure and make are commands used commonly to configure, build and
install Linux applications.

#### Configure

#### Make

`make sql`

You should be now noticing that you have 3 new files: **char-server**,
**map-server**, and **login-server**. Make install is not yet supported.

### Using cmake & make

[Cmake](http://www.vtk.org/Wiki/CMake) is a cross-platform configure.

Start creating a new sub directory and move there

`  mkdir build`  
`  cd build`

#### Building makefiles

Generate the make files by cmake

`  cmake -G"Unix Makefiles" -DINSTALL_TO_SOURCE=ON ..`

    -- The C compiler identification is GNU
    -- Check for working C compiler: /usr/bin/gcc
    -- Check for working C compiler: /usr/bin/gcc -- works
    -- Detecting C compiler ABI info
    -- Detecting C compiler ABI info - done
    -- Detecting system MYSQL
    -- Found MYSQL: /usr/lib/libmysqlclient.so (found version "5.1.58")
    -- Detecting system MYSQL - done
    -- Configuring for system MYSQL
    -- Configuring for system MYSQL - done
    -- Detecting system PCRE
    -- Found PCRE: /usr/lib/i386-linux-gnu/libpcre.so (found version "8.12")
    -- Detecting system PCRE - done
    -- Configuring for system PCRE
    ...
    -- Creating target login-server_sql
    -- Creating target login-server_sql - done
    -- Creating target char-server_sql
    -- Creating target char-server_sql - done
    -- Creating target map-server_sql
    -- Enabled PCRE code
    -- Creating target map-server_sql - done
    -- Creating target mapcache
    -- Creating target mapcache - done
    -- Disabled dbghelpplug plugin target (requires WIN32 and HAVE_DBGHELP_H)
    -- Available targets:
    --  common_base
    --  common_sql
    --  login-server_sql
    --  map-server_sql
    --  mapcache
    -- Configuring done
    -- Generating done
    -- Build files have been written to: /home/*/Hercules/build

#### Compilation

Then compile

`  make install`

    Scanning dependencies of target common_base
    [  1%] Building C object src/common/CMakeFiles/common_base.dir/__/__/3rdparty/mt19937ar/mt19937ar.c.o
    [  1%] Building C object src/common/CMakeFiles/common_base.dir/core.c.o
    [  2%] Building C object src/common/CMakeFiles/common_base.dir/db.c.o
    [  3%] Building C object src/common/CMakeFiles/common_base.dir/des.c.o
    ...
    [ 98%] Building C object src/tool/CMakeFiles/mapcache.dir/__/common/grfio.c.o
    [ 99%] Building C object src/tool/CMakeFiles/mapcache.dir/__/common/utils.c.o
    [100%] Building C object src/tool/CMakeFiles/mapcache.dir/mapcache.c.o
    ...
    -- Installing: ~/Hercules/./login-server_sql
    -- Installing: ~/Hercules/./char-server_sql
    -- Installing: ~/Hercules/./map-server_sql
    -- Installing: ~/Hercules/./mapcache

You'll see nice green output progression then finally login-server\_sql,
map-server\_sql, char-server\_sql, in main folder

## Windows

See this guide for [Compiling on Windows](https://github.com/HerculesWS/Hercules/wiki/Compiling-Windows).
