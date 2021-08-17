from selenium import webdriver

class InstaBot:
    def __init__(self):
        self.driver = webdriver.Edge("C:\\Users\\mathe\\Desktop\\PYTHON WORKSPACE\\tutorial-env\\Scripts\\msedgedriver.exe")
        self.driver.get("https://instagram.com")

    
InstaBot()
