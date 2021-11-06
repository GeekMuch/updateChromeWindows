import sys
import time
import logging
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

options = Options()
# options.add_argument("--headless")
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver1 = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver2 = webdriver.Chrome(ChromeDriverManager().install(), options=options)



def setup():
    print("\n[ * ] Openening in")
    driver1.get("https://cyberkill.haaukins.com/teams")
    time.sleep(1)
    driver2.get("https://cyberkill5.ntp-event.dk/teams")


    while 1:
        driver1.refresh()
        driver2.refresh()
        time.sleep(5)

def SirSpamAlot():
    count = 0
    # driver.find_element_by_css_selector('.closeButton-3PJ-TM').click()
    time.sleep(3)
    print("\n[ * ] Starting to spam")
    # logger.info("Starting SirSpamAlot")
    while(1):
        with open("profanity________list.txt","r") as dd:
            for i in dd:
                count += 1
                actions = ActionChains(driver)
                actions.send_keys('!urban '+i)
                actions.perform()
                send = driver.find_element_by_css_selector(".slateTextArea-1Mkdgw")
                send.send_keys(Keys.ENTER)
                
                print("[ + ] Word -> %s\t :\t Count -> %d " % (i.strip("\n"), count))
                time.sleep(5)
        dd.close()

if __name__ == "__main__":
    setup()
    # SirSpamAlot()
    