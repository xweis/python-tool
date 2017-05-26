#!/usr/bin/env python
# coding:utf-8

# 安装xwLibrary

import sys
import os
import shutil

if __name__ == '__main__' :
    installPath = ''

    for path in sys.path:
        strfind = 'site-packages'
        if strfind in path:
            installPath = path
            if installPath[len(strfind) - len(strfind) * 2 :] == strfind :
                break

    installPath = installPath + "/xwLibrary"

    st = "install"
    if len(sys.argv) > 1 :
        st = sys.argv[1]

    if st == "install" :
        try :
            if os.path.exists(installPath) :
                shutil.rmtree(installPath)
                shutil.copytree("xwLibrary", installPath)
            else :
                shutil.copytree("xwLibrary", installPath)
            print "\033[0;31;1mxwLibrary\033[0m install Success"
        except Exception,e :
            print Exception,":",e
    elif st == "uninstall":
        try :
            shutil.rmtree(installPath)
            print "\033[0;31;1mxwLibrary\033[0m uninstall Success"
        except Exception,e :
            print Exception,":",e
