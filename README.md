# get_Team_Pass

Get teamviewer's ID and password from a remote computer in the LAN

This program gets teamviewer's ID and password from a remote
computer in the LAN. 

Most useful for postexploitation or sysadmins

Tested on windows 7 and windows 10 x86 and x64

# Prerequisites

You must have valid credentials on the remote computer
Port 445 must be accesible on target machine

# Execution examples:

hook.exe must be in same folder as get_Team_Pass.exe

 		get_Team_Pass.exe -h for printing the help
    get_Team_Pass.exe -t [targetIp] -u [Username] -p [UsernamePassword] -d [usernameDomain]  # -d parameter is optional
 		get_Team_Pass.exe -t 192.168.175.136 -u administrator -p Password2018
 		get_Team_Pass.exe -t 192.168.175.136 -u administrator -p Password2018 -d domain

# Execution video
https://goo.gl/VhWF4g 

# Blog
https://kr1shn4murt1.blogspot.com/2018/12/obtener-el-id-y-password-de-teamviewer.html 
    
# Sha-256 checksums of files

Algorithm       Hash                                                                   File
---------       ----                                                                   ----
SHA256          28F71132305CFA45F4335FA8F9E3ADE52CC9E3339AECDCA795FBD5EA51894351       get_Team_Pass.exe
SHA256          57F62D0CB5656ED2D79DC16C25A9B0D3AACC307D945CED5B0F1CAA1F563735C1       hook.exe

# Authors

@kr1shn4murt1
@t1gr385
kronux.com.co
    
# TODO

Reduce the final size of the compiled files
Add more exception handling
Add network range capabilities to check all computers in a lan
In the future if teamviewer is not found in the remote machine, inject it
Add linux support


