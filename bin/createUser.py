#!/usr/bin/env python
# -*- coding: utf-8 -*-
# /*
#  * @Author: Huangcn
#  * @Date: 2018-10-30 10:38:27
#  * @LastEditors: Huangcn
#  * @LastEditTime: 2018-10-30 10:44:52
#  * @Description: 创建用户
#  */



import logging
import os


class createUser(object):

    LOG_FORMAT = "%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s"
    logging.basicConfig(filename=os.getcwd()+'/log/my.log', level=logging.DEBUG, format=LOG_FORMAT)

    print(os.getcwd())

    def __init__(self,name,password):
        self.name=name
        self.password=password

        # connPool = {}
        # self.connPool = connPool
        pass

    def createOracle(self):
        logging.info("Create User Oracle")
        logging.info("Username:  "+self.name)
        logging.info("Password:  "+self.password)

        pass

    def createGrid(self):
        logging.info("Create User Grid")
        logging.info("Username:  "+self.name)
        logging.info("Password:  "+self.password)
        pass

