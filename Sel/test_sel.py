from selenium import webdriver
import os,sys

def test_open():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.co.in")
    print("Title:"+driver.title)
    print(os.path.join(sys.path[0]+"\\Configuration"+"\\config.ini"))


def ftest_open1():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.co.in")
    print("Title:"+driver.title)

def ftest_open2():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.co.in")
    print("Title:"+driver.title)

