#!/usr/bin/python

import os
import commands
import sys

UNDEF_STAT = 127
ApplicationList = ['emacs', 'synaptic', 'rxvt', 'aterm', 'openssh-server',
                   'openssh-client']
ENVCONFIG = "git clone https://github.com/nyee32/Linux_config.git"
CLEANUP = ['spotify.sh']


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
    os.system(cmd)


# Clone config files from my github
def setupEnv ():
    os.system(ENVCONFIG)
    os.system("cp -r Linux_config/ ~/")
    os.system("rm -fr Linux_config")

def installSpotify():
    execCommand ('chmod 700 spotify.sh && ./spotify.sh')

def cleanup():
    for stuff in CLEANUP:
        rmStr = 'rm %s' % stuff
        execCommand(rmStr)



def main ():
    # Update the OS first
    print "Updating OS. This will may take sometime\n"
    os.system('sudo apt-get -y update && sudo apt-get -y upgrade')
    print "update complete"

    for apps in ApplicationList:
        installApp (apps)

    setupEnv()
    installSpotify()

    print "Setup is complete. You can now delete this directory\n"



if __name__ == "__main__":
    main()

