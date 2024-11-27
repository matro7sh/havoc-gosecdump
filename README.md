# havoc-gosecdump

>This module will upload the gosecdump binary to a temporary folder under windows  (it's better to use AppData or ProgramData)


> This plugin embeds a compiled version of go-secdump, if ever the binary gets caught after upload, modify the code a little, recompile and it will pass

# Usage

Go to `Script > Script Manager ` and load the .py file

> !! edit the path into.py file 4 before !! 

`gosecdump <target_ip> <user> <password> <sam/lsa/dcc2>`


![demo](img/poc.png)


It can be used in 127.0.0.1 but it is more intended to dumper the SAM/LSA/DCC2 on a remote machine that our compromised machine can reach.

This binary bypasses EDR-type solutions


### Other options : 

you can upload the binary yourself and run it with the `shell` command, but this will create a new process.

the other option is to use the “noconsolation” mode - don't drop the binary on the target 
