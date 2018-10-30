# /*
#  * @Description: In User Settings Edit
#  * @Author: your name
#  * @Date: 2018-10-30 01:49:00
#  * @LastEditTime: 2018-10-30 08:05:11
#  * @LastEditors: Huangcn
#  */
import logging
import os

print os.getcwd()
var_cwd = os.getcwd()

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename=var_cwd+'/log/my.log', level=logging.DEBUG, format=LOG_FORMAT)

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")



