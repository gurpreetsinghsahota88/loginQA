#Login Function file
import time
from utilities.readproperties import ReadConfig
from pageobjects.LoginPage import login
from utilities.customLogger import LogGen

#creating a class
class Test_001_Login:
    #calling url and info from config file
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
# calling the log file
    logger = LogGen.loggen()


    def test_homePageTitle(self,setup):
        #calling log file & showing log information
        self.logger.info("***********Test_001_Login*********")
        self.logger.info("***********verify Home Page Title**********")
        #calling webdriver function from conftest.py
        self.driver = setup
        self.driver.get(self.baseURL)
        #act_title = self.driver.title
        time.sleep(0)


       # if act_title == "Your store.Login":
         #   assert True
        #else:
         # screenshot command
         #   self.driver.save_screenshot("C:\\Users\\GURPREET\\PycharmProjects\\hybridproject\\screenshots\\"+"Test_001_Login.png")
          #  assert False

    def test_login(self,setup):
        self.logger.info("*************verify Login test************")
        # calling function to perform loginpage
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        time.sleep(0)
        #act_title=self.driver.title
        #if act_title == "Dashboard/nonCommerce administration":
         #   assert True
        #else:
         #   self.driver.save_screenshot("C:\\Users\\GURPREET\\PycharmProjects\\hybridproject\\screenshots\\" + "Test_001_Login.png")
        # self.logger.error("**************Home page title is failed**********")
          #  assert False
        self.driver.close()
