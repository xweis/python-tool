#!/usr/bin/env python
# coding:utf-8

# 安装xwLibrary

import sys
import os
import shutil

installPath = ''
for path in sys.path:
    if 'site-packages' in path:
        installPath = path

try :
    installPath = installPath + "/xwLibrary"
    if os.path.exists(installPath) :
        #os.rename(installPath,installPath + ".tmp")
        shutil.rmtree(installPath)
        shutil.copytree("xwLibrary", installPath)
    else :
        shutil.copytree("xwLibrary", installPath)
    print "\033[0;31;1mxwLibrary\033[0m install Success"
except Exception,e :
    print Exception,":",e
