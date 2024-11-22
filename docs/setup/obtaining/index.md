# Obtaining Hercules

Hercules is available through GitHub, a web-based hosting service for software development projects that use the GIT
revision control system.

# Obtaining Hercules on Windows

### Downloads

In order to get GIT on Windows properly, you need to download two things: MSysGit and TortoiseGIT.

` `[`Download and Install MSysGit`](http://code.google.com/p/msysgit/downloads/list?can=2)  
` `[`Download the latest TortoiseGit`](http://code.google.com/p/tortoisegit/wiki/Download?tm=2)

### Installation

Alright, first go through MSysGit installer and just set it up (its used as a base for TortoiseGit). then once you
install MSysGit, launch the installer you just downloaded for TortoiseGit, you'll be prompted by a window similar to the
following


![](assets/tgit-1.jpeg)

The next window is "Choose SSH Client", select "TortoisePLink", hit Next.

[](assets/tgit-2.jpeg)

The next window is "Custom Setup", do not change anything unless you know what you're doing, hit Next.

![](assets/tgit-3.jpeg)

We're done with the installation, that was easy, wasn't it?

![](assets/tgit-4.jpeg)

### Obtaining Hercules

Go to the folder where you want Hercules to be placed, right click and select "Git Clone..."

![](assets/tgit-5.jpeg)

in the URL field, type the following:

` `[`https://github.com/HerculesWS/Hercules.git`](https://github.com/HerculesWS/Hercules.git)

ensure the 'Directory' field is as desired, and hit 'OK' 

![](assets/tgit-6.jpeg)

Now Hercules is being downloaded

![](assets/tgit-7.jpeg)

Just wait for it to complete the download of your working copy and you'll be good to go.

### Updating Hercules

Right-Click the folder where you downloaded your working copy and within the TortoiseGit menu, select "Pull..." as shown below

![](assets/tgit-8.jpeg)

On the following window just hit 'OK', and your working copy will update.

![](assets/tgit-9.jpeg)

# Obtaining Hercules on Linux

### CentOS

- Step 1:

` rpm -Uvhhttp://repo.webtatic.com/yum/centos/5/latest.rpm`

- Step 2:

` yum install --enablerepo=webtatic git-all`

- Step 3:

` yum install --enablerepo=webtatic --disableexcludes=main git-all`

### Debian/Others

- Step 1:

` apt-get install git`

### Obtaining a Working Copy

Type the following to create a Hercules working copy in your home (~) directory:

` git clone `[`https://github.com/HerculesWS/Hercules.git`](https://github.com/HerculesWS/Hercules.git)` ~/Hercules`

### Updating a Working Copy

Type the following when inside your working copy:

` git pull`
