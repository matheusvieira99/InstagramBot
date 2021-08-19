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
        following = self._get_names_following()
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        followers = self._get_names_followers()
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)
        
    def _get_names_following(self):
        sleep(2)
        # sugs = self.driver.find_element_by_xpath("//h4[contains(text(), )]");
        scroll_box = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[3]')
        self.driver.execute_script('window.scrollBy(0,1000)')
        sleep(3)
        # print("im here")
        # scroll_box = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')
        #'/html/body/div[6]/div/div/div[2]'
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name != '']
        self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div[1]/div/div[2]/button")\
            .click()
        return names
        # print(names)
    def _get_names_followers(self):
        sleep(2)
        # sugs = self.driver.find_element_by_xpath("//h4[contains(text(), )]");
        scroll_box = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')
        self.driver.execute_script('window.scrollBy(0,1000)')
        sleep(3)
        # print("im here")
        # scroll_box = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')
        #'/html/body/div[6]/div/div/div[2]'
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name != '']
        self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div[1]/div/div[2]/button")\
            .click()
        return names

    
bot = InstaBot(username, password)
bot.get_unfollowers()
bot._get_names_following()
bot._get_names_followers()
