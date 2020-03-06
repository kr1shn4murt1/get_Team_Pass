# get_Team_Pass

Get teamviewer's ID and password from a remote computer in the LAN

This program gets teamviewer's ID and password from a remote
computer in the LAN. 

Most useful for postexploitation or sysadmins

Tested on windows 7 and windows 10 x86 and x64

Download binaries from releases folder
https://github.com/kr1shn4murt1/get_Team_Pass/releases/latest

# Prerequisites

You must have valid credentials on the remote computer
Port 445 must be accesible on target machine
Teamviewer must be installed on target machine, you can get id and password from a temporary teamviewer execution also but you need to modify the code

# Execution examples:

hook.exe must be in same folder as get_Team_Pass.exe
If execution fails execute again until you get the ID and password

 get_Team_Pass.exe -h for printing the help
   get_Team_Pass.exe -t [targetIp] -u [Username] -p [UsernamePassword] -d [usernameDomain]  # -d parameter is optional
 	 get_Team_Pass.exe -t 192.168.175.136 -u administrator -p Password2018
 		get_Team_Pass.exe -t 192.168.175.136 -u administrator -p Password2018 -d domain

# Execution video
https://goo.gl/VhWF4g 

# Blog
https://kr1shn4murt1.blogspot.com/2018/12/obtener-el-id-y-password-de-teamviewer.html 

# Compilation

This commands will generate files get_Team_Pass and hook.exe

pip install -r extras/requirements.txt

pyinstaller --onefile --icon=k.ico --version-file=get_Team_Pass_Version.txt get_Team_Pass.py 

pyinstaller --onefile --icon=k.ico --version-file=hook_Version.txt hook.py 

    
# Sha-256 checksums of files

The checksum of the files can be found on the corresponding releases folder
https://github.com/kr1shn4murt1/get_Team_Pass/releases


# Authors

@kr1shn4murt1
kronux.com.co

# NOTES

This program uses pywinauto lib to get the ID and password from the graphical teamviewer window

It also uses psexec, so if execution fails, test this command:
psexec.exe -u user -p password \\\targetip cmd -accepteula
https://download.sysinternals.com/files/PSTools.zip

if the command works, this tool should work
    
# TODO

Reduce the final size of the compiled files

Add more exception handling

Add network range capabilities to check all computers in a lan

In the future if teamviewer is not found in the remote machine, inject it

Add linux support
