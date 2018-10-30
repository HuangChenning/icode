# !/usr/bin/env python
# -*- coding: utf-8 -*-
# /*
#  * @Author: Huangcn
#  * @Date: 2018-10-30 09:33:27
#  * @LastEditors: Huangcn
#  * @LastEditTime: 2018-10-30 09:33:27
#  * @Description: 自动安装主程序
#  */


import sys
import os


#sys.path.append(os.getcwd()+'/bin/createUser.py')
from bin.createUser import createUser

import logging



# def main(argv):
#     if argv == None:
#         print('world~!')
#     else:
#         print(argv)
#print('hello')


# print os.getcwd()
# var_cwd = os.getcwd()

LOG_FORMAT = "%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s"
logging.basicConfig(filename=os.getcwd()+'/log/my.log', level=logging.DEBUG, format=LOG_FORMAT)

# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='./install_logs/oracleClone_{0}.log'.format(init_p.db_unique_name),
#                     filemode='a')

if __name__ == '__main__':
    # main(sys.argv)
    logging.info("**************Auto Install*****************")
    cUser = createUser("Oracle","oracle_123")
    cUser.createOracle()
    print("222")