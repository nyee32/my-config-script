#!/usr/bin/python

import os
import commands
import sys

UNDEF_STAT = 127
ApplicationList = ['emacs', 'git', 'synaptic', 'rxvt', 'aterm']
ENVCONFIG = "git clone https://github.com/nyee32/Linux_config.git ~/"


def installApp (app):
    print "Installing %s" % app
    installCmd = "sudo apt-get -y install %s" % app
    execRet = commands.getstatusoutput(installCmd)
    exitStat = os.WEXITSTATUS(execRet[0])
    retOutput = execRet[1]

    if exitStat != 0:
        print "Something went wrong with the install\n"
        print "Error: %s" % retOutput
        sys.exit(1)

    print "----------------------------"


def execCommand (cmd):
    exitStat = os.WEXITSTATUS(commands.getstatusoutput(cmd)[0])
    if exitStat == UNDEF_STAT:
        print "Command '%s' not found\n" % cmd
    else:
        print "Unknown exit status %d\n" % exitStat


# Clone config files from my github
def setupEnv ():
    execCommand (ENVCONFIG)

def installSpotify():
    execCommand ('chmod 700 spotify.sh && spotify.sh')





def main ():
    # Update the OS first
    exeCommand ('sudo apt-get update && sudo apt-get upgrade')

    for apps in ApplicationList:
        installApp (apps)

    setupEnv()
    installSpotify()


if __name__ == "__main__":
    main()

