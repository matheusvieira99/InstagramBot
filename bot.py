from selenium import webdriver
from time import sleep
from password import password
from password import username

class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Edge("C:\\Users\\mathe\\Desktop\\PYTHON WORKSPACE\\tutorial-env\\Scripts\\msedgedriver.exe")
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(password)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]")\
            .click()
        sleep(2)
        # self.driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]")\
        #     .click()
        # sleep(2)
    
    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(username))\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        sleep(2)
        # sugs = self.driver.find_element_by_xpath("//h4[contains(text(), )]");
        self.driver.execute_script('window.scrollBy(0,1000)')
        sleep(3)
        # print("im here")
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div[3]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        

    
bot = InstaBot(username, password)
bot.get_unfollowers()
