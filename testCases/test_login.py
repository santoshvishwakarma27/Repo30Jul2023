import openpyxl
from selenium import webdriver
from pageObjects.loginPage import Login
import pytest
from testCases import conftest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import excel
import os,sys

class Test_Login:
    url=ReadConfig.get_AppURL()
    #username=ReadConfig.getUsername()
    #password=ReadConfig.getPassword()
    #path=".//TestData/ExcelTestData.xlsx"
    path=os.path.join(sys.path[0]+"\\TestData"+"\\ExcelTestData.xlsx")
    logger=LogGen.loggen()

    def Ttest_successfulLogin(self,setup):
        #self.driver=webdriver.Chrome();
        self.logger.info("TC 1 Started")
        self.driver=setup
        self.driver.get(self.url)
        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()
        title=self.driver.title
        #print(title)
        #assert title=="Login - nopCommerce"
        if title=="Login - nopCommerce":
            assert True
            self.logger.info("TC 1 Passed")
        else:
            self.driver.save_screenshot("images.png")
            self.driver.close()
            self.logger.info("TC 1 Passed")
            assert False

    @pytest.mark.sanity
    def test_successfulLoginExcel(self,setup):
        #self.driver=webdriver.Chrome();
        self.logger.info("TC 1 Started")
        self.driver=setup
        self.driver.get(self.url)
        self.lp=Login(self.driver)
        user=excel.readData(self.path,'Sheet1',1,1)
        self.lp.setUserName(user)
        pwd = excel.readData(self.path,'Sheet1', 1,2)
        self.lp.setUserPassword(pwd)
        #self.lp.setUserName(self.username)
        #self.lp.setUserPassword(self.password)
        self.lp.clickLogin()
        title=self.driver.title
        #print(title)
        #assert title=="Login - nopCommerce"
        if title=="Login - nopCommerce":
            assert True
            self.logger.info("TC 1 Passed")
        else:
            self.driver.save_screenshot("images.png")
            self.driver.close()
            self.logger.info("TC 1 Passed")
            assert False


    @pytest.mark.regression
    def test_successfulLoginExcel1(self,setup):
        #self.driver=webdriver.Chrome();
        self.logger.info("TC 1 Started")
        self.driver=setup
        self.driver.get("https://www.google.co.in/")
        #self.lp=Login(self.driver)
        #user=excel.readData(self.path,'Sheet1',1,1)
        #self.lp.setUserName(user)
        #pwd = excel.readData(self.path,'Sheet1', 1,2)
        #self.lp.setUserPassword(pwd)
        #self.lp.setUserName(self.username)
        #self.lp.setUserPassword(self.password)
        #self.lp.clickLogin()
        title=self.driver.title
        #print(title)
        #assert title=="Login - nopCommerce"
        if title=="Google":
            assert True
            self.logger.info("TC 1 Passed")
        else:
            self.driver.save_screenshot("images.png")
            self.driver.close()
            self.logger.info("TC 1 Passed")
            assert False
