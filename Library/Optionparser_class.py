#!/usr/bin/python
# -*- coding: utf-8 -*-

#脚本帮助,参数传递类
#2016-06-30
#使用方法
'''
op = parse_argv()
op.AddOption('-p','--path','path',u'这里是解释')
op.AddOption('-n','--name','name',u'这里是作者')
opp = op.run()
print opp.name
'''

from optparse import OptionParser

class parse_argv:

    def __init__(self):
        '''
        -p 参数名
        --pdkb 参数全称
        action =(store options.pdcl的值,
                 store_true reutrn true
                 store_false, return false

        dest = 获取参数健options.pdcl
        default = 默认值
        help  --help
        '''
        self.parser = OptionParser()

    '''    self.parser.add_option("-e", "--env", action="store",
                              dest="env",
                              default="dev",
                              help=u"指定运行环境,不同的环境配置不同 dev, prod")'''

    def AddOption(self,argv,name,cdest,chelp,cdefault=False,caction="store"):
        self.parser.add_option(argv, name, action=caction,
                              dest=cdest,
                              default=cdefault,
                              help=chelp)
    def run(self):
       (option, argv) = self.parser.parse_args()
       return option
