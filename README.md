# havoc-gosecdump

>This module will upload the gosecdump binary to a temporary folder under windows  (it's better to use AppData or ProgramData)

# Usage

Go to `Attack > Extensions ` and select havoc-gosecdump + install

you now have a new gosecdump command available


to use it, here are the parameters to pass: `gosecdump <target_ip> <user> <password> <sam/lsa/dcc2>`


![demo](img/poc.png)


It can be used in 127.0.0.1 but it is more intended to dumper the SAM/LSA/DCC2 on a remote machine that our compromised machine can reach.

This binary bypasses EDR-type solutions


### Other options : 

you can upload the binary yourself and run it with the `shell` command, but this will create a new process.

the other option is to use the “noconsolation” mode - don't drop the binary on the target 
