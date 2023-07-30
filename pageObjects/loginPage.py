from selenium import webdriver
class Login:
    txtbox_username_id="Username"
    txtbox_password_id="Password"
    btn_login_xpath="//input[@type='submit']"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        user=self.driver.find_element("id",self.txtbox_username_id).send_keys(username)
        #self.driver.find_element_by_id(self.txtbox_username_id).sendKeys


    def setUserPassword(self, password):
        self.driver.find_element("id",self.txtbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element("xpath",self.btn_login_xpath).click()



