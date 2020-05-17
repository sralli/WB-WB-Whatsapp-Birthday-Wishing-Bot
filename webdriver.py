from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time


class Initialze_Script:
    '''
        Docstring: Initializes the webdriver for Firefox, along with the default profile for it to automatically load whatsapp web. 
    '''
    def __init__(self):
        '''
            Contains both the commads for Chrome/Firefox, Comment/Uncomment the ones that you want to use. 
            Advice: Use the browser that you don't use often, for selenium requres a new clean instance to run on the default profile
        '''

        '''Chrome : 
                self.chropt = webdriver.ChromeOptions() 
                self.chropt.add_argument("user-data-dir=<ENTER THE PATH TO THE CHROME USER DATA>")
                self.driver = webdriver.Chrome(options = self.chropt)
        '''

        '''Firefox: '''
        self.profile = webdriver.FirefoxProfile("<PATH TO DEFAULT FIREFOX PROFILE")
        self.driver = webdriver.Firefox(self.profile)


        self.driver.get("https://web.whatsapp.com/")
        time.sleep(30)
        

    def Search_and_enter_chat(self, person):
        eleFind = self.driver.find_element_by_class_name("_2S1VP")
        eleFind.send_keys(person)
        time.sleep(5)
        eleNM = self.driver.find_element_by_xpath("//span[@title='"+person+"']") 
        eleNM.click() 
           

    def send_message(self, name,  message):
        namev = [name]
        for inp in namev: 
            self.Search_and_enter_chat(inp)  
            # Finds the chat box element 
            inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
            eleTF =  self.driver.find_element_by_xpath(inp_xpath)
            time.sleep(15)
            # Writes the message for the birthday 
            eleTF.send_keys(message + Keys.ENTER) 
            time.sleep(5)
        self.driver.quit()
