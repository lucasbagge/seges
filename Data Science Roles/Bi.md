# BI Foundations with SQL, ETL and Data Warehousing Specialization

## Hands-on Introduction to Linux Commands and Shell Scripting

I atvangate in learning Linux and shell scripting makes you more flexiable. 

A operating system is a system that operates hardware ans resources. 

Unix is a family of OS, here is Oracle Solaris an example like macbook os is a example. 

Linux is alike Unix-like OS. It was created as a free source. GNU was developed in 1980. The pingvin which is the maskot is called Tux. 

Linux is used in phones. IN supercomputers for high performance. Cloud center also use it. 

In a linux system there is five distinct layers:

1) USER
* The one to perform a task.  
2) Application
   1) system daemons
   2) shells
   3) user apps
   4) tools
3) OPerating system for unning tasks.Controls jobs, assign software. 
4) kernal most vital jobs. Manage memori and security. Lowest level software. Bridge betweenapps and hardware. 
5) harward 

### Linux distribution

Is a specific flavour of LINX OS also called `distro`.
Uses linux kernal.

FOr each distro there can come with different system utilities, GUI and shell commands.

`Debian` is one of the first in 1993. It is stable, reliable and open source. 

`Ubunto` also an popular one. It is build on top of debian. Canonical is the contributor. 

`Red hat Linux` is a core Linux distro and not build on top of any other. 

`Fedora`, support many archeticture. 

### Linux terminal

A `Shell` is the place where we interact with linux. for Shell `bash` and `zsh` is very popular. 

A temrinal command can be `cd` which stand for *change directory*.

FOr going back to parent folder 

```
cd ..
```

There is multiple `Text editor` like command GNU, vi, vim (mode based). A GUI based.

`gedit` general purpoe editor easy to use with simple gui. Many features, integraed file browser. 

`GNU nano` made possible to seach and replace, highlight, line numbers. 


VIM has two modes; `Insert` and `Command `. Press `i` for enter Insert mode and `esc` for comming out again. When in COmmand mode we can save a file.

```
:sav ecamplevim.txt
```

For exting write `:q`

For qutting and discard changes `:q!`

Packages are importing for instaliing and updating software in linux. 

Deb and RPM are packages for Linux OS. Deb is used for Ubuntu. 
.rpm for Red hat.

deb and RPM format are equivalent. 

They can be convertet

`Update Manager` check for updates and is a HUI tools. 

`apt` is a command line for checking updates. 

```
sudo apt uågrade
```

`PackageKit` notifices when updates is avaiable. 

`yum` is command line that updates

```
sudo yum update
```

Command lines can used to installe new

```
sudo apt install <packagename>

sudo yum install <package-name>
```

Pip is an example for package manager. 


### Hand on project

~ Home Directory
/ Root Dir
. Current dir
.. Parent dir

`ls` for looking into a directory and for ls/ to look at the content in a folder. 

`nano` is a simple command that enables you to use the terminal as a text editor.


Create file 

```
nano mypro.py
```

`ctrl+x` for saving

then it can be runed.

Summary & Highlights
Congratulations! You have completed this module. At this point, you know: 

Linux originated in the 1990s when Linus Torvalds developed a free, open source version of the Unix kernel. 

Linux is multi-user, portable, and supports multitasking. 

Linux is widely used today in mobile devices, desktops, supercomputers, data centers, and cloud servers. 

Linux distributions (also known as distros) differ by their UIs, shell, applications, and how the OS is supported and built. 

The design of a distro is catered toward its specific audience and/or use case. 

Popular Linux distributions include Red Hat Enterprise Linux (RHEL), Debian, Ubuntu, Suse (SLES, SLED, OpenSuse), Fedora, Mint, and Arch. 

The Linux system consists of five key layers: user, application, OS, kernel, and hardware. 

The kernel is the lowest-level software and it enables applications to interact with your hardware. 

The shell is an OS-level application for running commands. 

You use a terminal to send commands to the shell. 

You can use the cd command to navigate around your Linux filesystem. 

You can use a variety of command-line or GUI-based text editors such as GNU nano, vim, vi, and gedit. 

Deb and RPM packages contain software updates and installation files. 

You can use GUI-based and command-line package managers to update and install software on Linux systems.



### Linux command

Shell is a interface for running command. It has interactive language, scripting language and automate task.
The default is `bash`. (born again)

print out default in ubundu
```
printenv SHELL
```

For using shelle we use it for get infromation, monitorin performance and status and running jobs. like etl.

* whoami - username
* id - user id and goruüname - operatin sys
* ps - running process
* top - resource usage
* df - mounted file systems
* man - reference manual
* date - today

worikin 

* cp - copy file 
* mv - change file name
* rm - remoce file
* tocuh - create file
* chmod - change file
* wc - get count of lines, word
* grep - return lines in fie matching pattern

navigating

* ls - list files
* find - find that match
* pwd - current dir
* mkdir - new dir
* cd - change dir
* rmdir - remode dir

print files

* cat - print conten
* more - print file contenst
* head - head
* tail - lowers
* echo - print string or vcariable value


compressing and arhces

* tar - archive files
* zip - compres files
* unzip - uncompres files

networking

* hostname - print name
* ping - send package to url and print response
* ifconfig - display or configure system network
* curl .- dusplkay coneten at url
* wget - download file form url

By use df -h we can list disk usage

```
root@PC10230:~# df -h ~
Filesystem      Size  Used Avail Use% Mounted on
/dev/sdb        251G  1.1G  238G   1% /
```

echo print the content, and we can use it to view path 

```
echo $PATH # will print
root@PC10230:~# echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/lib/wsl/lib:/mnt/c/Program Files/WindowsApps/CanonicalGroupLimited.Ubuntu_2204.1.7.0_x64__79rhkp1fndgsc:/mnt/c/Program Files (x86)/Common Files/Oracle/Java/javapath:/mnt/c/Oracle/Ora92/bin:/mnt/c/WINDOWS/system32:/mnt/c/WINDOWS:/mnt/c/WINDOWS/System32/Wbem:/mnt/c/WINDOWS/System32/WindowsPowerShell/v1.0/:/mnt/c/Users/lucb/AppData/Local/Programs/Python/Python310/Scripts:/mnt/c/Program Files (x86)/Microsoft SQL Server/150/DTS/Binn/:/mnt/c/Program Files/Azure Data Studio/bin:/mnt/c/Program Files/MySQL/MySQL Shell 8.0/bin/:/mnt/c/Users/lucb/AppData/Local/Microsoft/WindowsApps:/mnt/c/Users/lucb/AppData/Local/Programs/Microsoft VS Code/bin:/mnt/c/Users/lucb/AppData/Local/Programs/Git/cmd:/snap/bin
```

dates

```
root@PC10230:~# date '+%j day of the %Y'
321 day of the 2022
```

for a manuel type man id for getting list of id commands.