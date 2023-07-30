import configparser
import os,sys

config=configparser.RawConfigParser()
#config.read(".\\Configuration\\config.ini")
config.read(os.path.join(sys.path[0]+"\\Configuration"+"\\config.ini"))

class ReadConfig:

    @staticmethod
    def get_AppURL():
        url=config.get('common info','url')
        return url

    @staticmethod
    def getUsername():
        user=config.get('common info','username')
        return user

    @staticmethod
    def getPassword():
        pwd=config.get('common info','password')
        return pwd
